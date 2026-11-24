#!/usr/bin/env python3
"""复盘（1009 立·作者令「每一次任务都要复盘：踩的坑、哪里做了无用功、哪里花了大量 token 与时却无实果、
具体之改进方案；每回都要有详细之任务记录与具体耗费——越来越有效、越来越科学之 token 用法」）。

本器零 token 起草一份复盘：任务之记录（取自 `设定/工作流账.json`）＋每个 Run 之费审（`工具/费审.py`）自动填入；
「无用功」一节先列机器之疑点（来回最多之席、机器之活之占、超估之倍），**总编辑须亲写其判与改进方案**。
无复盘不许结案（`工具/工作流账.py --裁 W 取／重造` 先验 `设定/复盘/*W*.md` 三节俱在）。

用法：
  python3 工具/复盘.py W12 380造式 wf_e7912fa3-a0c [其他 Run ID…] [--自 2026-10-08T09:01]
      → 写 设定/复盘/<月日>_W12_380造式.md（已在则⛔覆）；自＝任务起时（缺则取工作流账之「起」）
  python3 工具/复盘.py 主环 二代定稿 --自 2026-10-09T03:05 [--至 2026-10-09T04:05]   # 非工作流之任务（总编辑亲手）亦须复盘
  python3 工具/复盘.py W61 401造式 wf_… --简 --平台 84.97   # --平台＝本会话 get_session 之 cost_usd（X56）； ★1021 章之简式：数归器、判只三问三句（作者令「总结⛔过度消耗」）
  python3 工具/复盘.py W72 题 wf_… --简 --平台 "不可分：<由>"   # 一会话跨数件、get_session 之 cost_usd 係累计而分不出者（由四字以上）
  ★1027（执行之审 #86）：--简 无 --平台 即拒（器计曾低估 2.4 倍·X56）。
  〔执行之制·治19、治12 之报（W918 环6）〕章之复盘（题＝第N章／N造式）之「## 效」添二行（零 token·只印⛔拦）：
      「封後之红：<名>」——取 备份/报 之 报/推/章-(N-1).json 之红（闸之红名、器之红；取不得即「封後之红：取不得」）；
      「费势：<近五÷前五>」——复用 法用之守.费势（⛔另算）；逾 1.05（或算不得）即添「数之退：‹判›｜治：‹X›」之空格（只 ⚠·⛔入每章一进之证）。
  python3 工具/复盘.py --验     # 闸：设定/复盘/ 诸档须有 耗费／无用功／改进方案／坑 四节，坑节须点坑账之号或写「无新坑」
      ★1027 起之档另验二样（执行之审 #5 #58 #81②·「立停」之证）：
        ①逾估：实费（平台之实，无则总费）＞工作流账该件预估×1.5 而档无「逾估：<由>」即红；
        ②机器之活：「机器能办而花token」占实费 >5% 者，其「进化」（简式）或「改进方案」须引瑕疵总账在账之 X 号、或「已行：工具/<器>.py」而其器在盘
      ★1105 起之简式另验一样（1104 作者问「方法是否不停进化、越来越好」之核·每章一进之实）：
        ③「进化」须可追——引瑕疵总账在账之 X／Y 号、或带凭（工具/<器>.py|.js 在盘、法用#<法> 在册、改单#G… 在账）；
          写「无：<由>」者由须八字以上；章之复盘（W…_第N章／N造式）连三章俱「无」即红（第三章须引账或已行）
  python3 工具/复盘.py --效账   # 诸复盘之「效」汇一表：总费、服务目标之费与其占、浪费、机器能办而花token；按类比上回
  python3 工具/复盘.py --自测

1009 作者令「每次总结方法：具体流程、具体制作过程、所踩之坑——一次又一次之经验让虫洞方法越来越好」：
  自动填：流程（各 Run 之席按时序）｜制作过程（任务起後之提交，git 自动）｜耗费（费审：逐回照官方价目精算美元）｜主环之费（费审 --主）｜资源分配（美元之占）
  并自动入 `设定/费账.json`（随时记）
  总编辑亲填：产出、与上回比之判、无用功之判、刀刃、改进方案、坑（新坑先 `工具/方法坑账.py --立`，旧坑复踩 `--复踩`；坑必入法典）
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import os, sys, io, json, glob, time, contextlib, tempfile, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import 费审


配额 = [('造', 75, '≥'), ('验', 20, '≤'), ('机器之活', 0, '≤')]


def 分配表(行):
    """资源分配官之表：实占（美元之占，费审精算）对配额（造≥75%、验≤20%、机器之活→0 归脚本、找料→0 归章料）。"""
    import re as _re
    总 = sum(x['金'] for x in 行) or 0
    if not 总:
        return '（无 Run 可审——非工作流之席，照回执手填分配）'
    出 = ['| 类 | 配额 | 实占 | 判 |', '|---|---|---|---|']
    已 = set()
    for 名, 额, 向 in 配额:
        pat = dict(费审.类)[名]
        s = [x for x in 行 if _re.search(pat, x['名']) and id(x) not in 已]
        for x in s:
            已.add(id(x))
        占 = 100.0 * sum(x['金'] for x in s) / 总
        合 = (占 >= 额) if 向 == '≥' else (占 <= 额 + (5 if 额 == 0 else 0))
        出.append('| %s | %s%d%% | %.0f%% | %s |' % (名, 向, 额, 占, '✓' if 合 else '⛔失配'))
    出.append('| 找料 | 0（章料） | 见「无用功」：执笔／魂之工具回数 | — |')
    return '\n'.join(出)


import re, subprocess


def 制作(自, root=ROOT, 至=None):
    """任务起後之提交（git 自动）：时、号、说明之首行。"""
    if not 自:
        return ['（无起时——以 --自 给之）']
    o = subprocess.run(['git', '-c', 'core.quotepath=off', 'log', '--since=%s' % 自.replace('Z', '+00:00'), '--reverse',
                        '--date=format:%m-%d %H:%M', '--format=- %ad｜%h｜%s'] + (['--until=%s' % 至.replace('Z', '+00:00')] if 至 else []), cwd=root, capture_output=True, text=True).stdout
    return [l[:220] for l in o.strip().split('\n') if l] or ['（任务起後无提交）']


def 坑号们(t):
    return set(re.findall(r'[\u2460-\u2473\u3251-\u325F\u32B1-\u32BF]|坑\d+', t))


新律起 = '1027'   # ★1027 执行之审 #5 #58 #81②：逾估之由、机器之活之引——自此日之档起验（旧档⛔追·同 1015／1018／1021 之例）
律起W = {'1015': 31, '1018': 52, '1021': 58, '1027': 72, '1105': 89}   # ★各律首档之 W 号（W 号只增）——档名之日只有月日（MMDD），跨年（0101 起）「≥1027」即不成立、新律静默失效，以 W 号接住


def 自律(名, 起):
    """档名之日 ≥ 起，或 W 号 ≥ 其律首档之 W，或日 < 1001（复盘档始於 1009：月日回到 01—09 者即跨年之後）。"""
    m = re.match(r'(\d{4})_', 名)
    w = re.match(r'\d{4}_W(\d+)_', 名)
    return bool(m and (m.group(1) >= 起 or m.group(1) < '1001')) or bool(w and int(w.group(1)) >= 律起W[起])


def 新律之档(名):
    """1027 之律：日 ≥ 1027 之档，或 W 号 ≥ 72 之档（跨年之後档名之日回到 01xx，以 W 号接住）。"""
    return 自律(名, 新律起)


进化律起 = '1105'   # ★1104 作者问「方法是否不停进化」之核：412—419 之「进化」虽俱有答，而旧验只认「X\d+|已行|无：」四样之字——
                     #   账上没有之号、「已行」而无凭、「无：」後空着俱过；连「无」亦无数。自此日（或 W ≥ 律起W 之数）之档起验其可追与连无之限
_章复盘式 = re.compile(r'^\d{4}_W(\d+)_第?(\d{3})(?:章|造式)')


def 进化之凭(文, root=ROOT):
    """「进化」之答所引可追之凭：瑕疵总账有其行之 X／Y 号、工具/ 下在盘之器（.py／.js）、法用册有其 id 之「法用#」、改单账有其号之「改单#G」。→ 凭之列"""
    def 读(p):
        try:
            return open(os.path.join(root, p), encoding='utf-8').read()
        except OSError:
            return ''
    账 = 读(os.path.join('设定', '瑕疵总账.md'))
    凭 = [x for x in re.findall(r'(?<![A-Za-z])([XY]\d+)', 文) if re.search(r'^\|\s*%s\s*\|' % x, 账, re.M)]
    凭 += [x for x in re.findall(r'工具/((?:席/)?[\w\u4e00-\u9fff]+\.(?:py|js))', 文) if os.path.isfile(os.path.join(root, '工具', x))]
    if '法用#' in 文:
        try:
            册 = json.loads(读(os.path.join('设定', '法用册.json')) or '{}')
        except ValueError:
            册 = {}
        ids = {str(x.get('id')) for k in ('法', '待', '废') for x in 册.get(k) or [] if x.get('id')}
        凭 += ['法用#' + i for i in re.findall(r'法用#([^\s，,；;|）)」』〕\]、。：:]+)', 文) if i in ids]   # 与 法用之守 之读法同
    if '改单#' in 文:
        try:
            号们 = {x.get('号') for x in json.loads(读(os.path.join('设定', '改单账.json')) or '{}').get('单') or []}
        except (ValueError, AttributeError):
            号们 = set()
        凭 += [x for x in re.findall(r'改单#(G\d{4}-\d+)', 文) if x in 号们]
    return 凭


def 进化之无(文, root=ROOT):
    """「无：」起手而无一可追之凭者，即「无」。"""
    return bool(re.match(r'\s*无[：:]', 文)) and not 进化之凭(文, root)


def 进化之坏(名, 文, root=ROOT):
    """★1105 起之简式：「进化」须可追（引凭），或「无：<由>」由八字以上。→ [坏]"""
    if 进化之凭(文, root):
        return []
    if re.match(r'\s*无[：:]', 文):
        if not re.match(r'\s*无[：:]\s*(?:\S\s*){8,}', 文):
            return ['%s 之三问「进化」写「无」而其由不足八字——须书所探之候与弃之之由（1104·每章一进之实）' % 名]
        return []
    return ['%s 之三问「进化」未引可追之凭：须引瑕疵总账在账之 X／Y 号（带限）、或「已行：」带凭（工具/<器> 在盘、法用#<法> 在册、改单#G… 在账）、或「无：<由>」（1104·每章一进之实）' % 名]


def 连无之坏(诸, root=ROOT):
    """章之复盘（每章取 W 最大者）按章号排：1105 律下之章写「无」，而前二章（章号相连）亦俱「无」→ 坏（连三无）。诸：{名: 进化之文}"""
    章 = {}
    for 名, 文 in 诸.items():
        m = _章复盘式.match(名)
        if m and (int(m.group(2)) not in 章 or int(m.group(1)) > 章[int(m.group(2))][0]):
            章[int(m.group(2))] = (int(m.group(1)), 名, 文)
    坏 = []
    for n, (w, 名, 文) in sorted(章.items()):
        if not 自律(名, 进化律起) or not 进化之无(文, root):
            continue
        if all(k in 章 and 进化之无(章[k][2], root) for k in (n - 1, n - 2)):
            坏.append('%s 之「进化」连三章俱「无」（%d、%d、%d）——第三章须引瑕疵总账之号带限、或已行带凭（心诀五：每章出一条更省更好之改，入账带限，做到为止）' % (名, n - 2, n - 1, n))
    return 坏


def _元(效文, 项):
    m = re.search(r'^- %s：(?:约\s*)?\$\s*(\d+(?:\.\d+)?)' % 项, 效文, re.M)
    return float(m.group(1)) if m else None


def 估之元(W, root=ROOT):
    """工作流账该件之「预估」之 $ 数（首见者）；无件、无 $ → None。"""
    try:
        件 = next((x for x in json.load(open(os.path.join(root, '设定', '工作流账.json'), encoding='utf-8'))['件'] if x.get('id') == W), {})
    except Exception:
        return None
    m = re.search(r'\$\s*(\d+(?:\.\d+)?)', str(件.get('预估', '')))
    if m:
        return float(m.group(1))
    return 方案之估(W, root)        # 〔执行之制·治13(a)〕件无估（或无件）→ 取方案之估，复起章之逾估之验


def 方案之估(W, root=ROOT):
    """〔执行之制·治13(a)（1124·482 主环收批）〕设定/方案/<W>.md 之「**费**」行（或「预估」行）之首个 $ 数 → float｜None。"""
    try:
        t = open(os.path.join(root, '设定', '方案', '%s.md' % W), encoding='utf-8').read()
    except Exception:
        return None
    m = re.search(r'(?m)^\s*[-*]\s*\**(?:费|预估)\**[：:][^\n$]*\$\s*(\d+(?:\.\d+)?)', t)
    return float(m.group(1)) if m else None


def 新律之坏(名, t, root=ROOT):
    """★1027 起之复盘：①逾估无由 ②机器之活逾 5% 而未引账／未行。→ [坏]"""
    坏 = []
    效 = re.search(r'^## 效[^\n]*\n(.*?)(?=^## |\Z)', t, re.M | re.S)
    if not 效:
        return 坏
    实 = _元(效.group(1), '平台之实') or _元(效.group(1), '总费')
    m = re.match(r'\d{4}_(W\d+)_', 名)
    估 = 估之元(m.group(1), root) if m else None
    if 实 and 估 and 实 > 1.5 * 估 and not re.search(r'逾估[：:]\s*(?:\S\s*){4,}', t):
        坏.append('%s 实费 $%.2f 逾预估 $%.2f 之 1.5 倍，而无「逾估：<由>」（立停之证·1027 执行之审 #81②）' % (名, 实, 估))
    机 = _元(效.group(1), '机器能办而花token')
    if 实 and 机 and 机 / 实 > 0.05:
        问 = re.search(r'^- 进化：(.*)$', t, re.M)
        改 = re.search(r'^## 改进方案[^\n]*\n(.*?)(?=^## |\Z)', t, re.M | re.S)
        文 = (问.group(1) if 问 else '') + '\n' + (改.group(1) if 改 else '')
        try:
            账 = open(os.path.join(root, '设定', '瑕疵总账.md'), encoding='utf-8').read()
        except OSError:
            账 = ''
        引 = [x for x in re.findall(r'X\d+', 文) if re.search(r'^\|\s*%s\s*\|' % x, 账, re.M)]
        行 = [x for x in re.findall(r'已行[：:][^\n]*?工具/([\w\u4e00-\u9fff]+\.py)', 文) if os.path.exists(os.path.join(root, '工具', x))]
        if not 引 and not 行:
            坏.append('%s 机器能办而花token $%.2f 占实费 %.0f%%（>5%%），而其「进化」／「改进方案」未引瑕疵总账在账之 X 号、亦无「已行：工具/<器>.py」（坑⑫·1027 执行之审 #5 #58）'
                      % (名, 机, 100 * 机 / 实))
    return 坏


def 验(root=ROOT):
    坏 = []
    进化诸 = {}
    try:
        import 方法坑账 as 坑账
        有号 = {坑账.圈(k['号']) for k in 坑账.读(root)['坑']}
    except Exception:
        有号 = None
    for f in sorted(glob.glob(os.path.join(root, '设定', '复盘', '*.md'))):
        t = open(f, encoding='utf-8').read()
        名 = os.path.basename(f)
        # ★1021 作者令「总结不要过度消耗……轻轻松松一想能想出来」：1021 起带「## 三问」之简式——数归器、判只三句
        简 = 自律(名, '1021') and '## 三问' in t
        for 节 in (('## 耗费', '## 三问', '## 坑') if 简 else ('## 耗费', '## 无用功', '## 改进方案', '## 坑')):
            if 节 not in t:
                坏.append('%s 缺「%s」' % (名, 节))
        效 = re.search(r'^## 效[^\n]*\n(.*?)(?=^## |\Z)', t, re.M | re.S)
        if not 效:
            坏.append('%s 缺「## 效」（总费、服务目标之费、浪费、机器能办而花token——俱须 $ 之数）' % 名)
        else:
            for 项 in ('类', '目标'):
                m = re.search(r'^- %s：(.*)$' % 项, 效.group(1), re.M)
                if not m or not m.group(1).strip() or m.group(1).strip().startswith('（填'):
                    坏.append('%s 之效缺「%s」' % (名, 项))
            for 项 in ('总费', '服务目标之费', '浪费', '机器能办而花token'):
                if not re.search(r'^- %s：(?:约\s*)?\$\d' % 项, 效.group(1), re.M):   # 1024 实踩（410）：「约 $1」亦是 $ 之数（--效账 之读法同）
                    坏.append('%s 之效「%s」须是 $ 之数' % (名, 项))
        if 简:
            问 = re.search(r'^## 三问[^\n]*\n(.*?)(?=^## |\Z)', t, re.M | re.S)
            for 项 in ('法行否', '最贵之席值否', '进化'):
                m = re.search(r'^- %s：(.*)$' % 项, 问.group(1), re.M) if 问 else None
                if not m or not m.group(1).strip() or m.group(1).strip().startswith('（填'):
                    坏.append('%s 之三问缺「%s」' % (名, 项))
                elif 项 == '进化' and not re.search(r'X\d+|Y\d+|已行|无[：:]', m.group(1)):
                    坏.append('%s 之三问「进化」须引瑕疵总账 X 号（带限）、或「已行：…」、或「无：<由>」' % 名)
                elif 项 == '进化':
                    进化诸[名] = m.group(1)
                    if 自律(名, 进化律起):
                        坏 += 进化之坏(名, m.group(1), root)
        elif 自律(名, '1015'):                 # ★1015 起之复盘须答虹吸之问（旧档⛔追）
            虹 = re.search(r'^## 虹吸之问[^\n]*\n(.*?)(?=^## |\Z)', t, re.M | re.S)
            if not 虹:
                坏.append('%s 缺「## 虹吸之问」（重付、可流、顺势、下一回之法）' % 名)
            else:
                if not re.search(r'^- 重付：\$\d', 虹.group(1), re.M):
                    坏.append('%s 之虹吸之问「重付」须是 $ 之数' % 名)
                for 项 in ('可流', '顺势', '下一回之法'):
                    m = re.search(r'^- %s：(.*)$' % 项, 虹.group(1), re.M)
                    if not m or not m.group(1).strip() or m.group(1).strip().startswith('（填'):
                        坏.append('%s 之虹吸之问缺「%s」' % (名, 项))
                # ★1017 作者铁律·开发不停（朝 B＋C）：1018 起之复盘，虹吸之问须有「B＋C 之候」——一条效↑费↓之候选新法，效与费俱有其计
                if 自律(名, '1018'):
                    m = re.search(r'^- B＋C 之候：(.*)$', 虹.group(1), re.M)
                    if not m or m.group(1).strip().startswith('（填') or not ('效' in m.group(1) and '费' in m.group(1)):
                        坏.append('%s 之虹吸之问缺「B＋C 之候」（一条效↑费↓之候选新法，效与费各写其计——1017 作者铁律·开发不停）' % 名)
                    # ★1021 作者问「为什么还是我自己发现」：B＋C 之候写了七回只行二回——1021 起须入瑕疵总账（引 X 号）或写「已行」，账限哨按其限催
                    elif 自律(名, '1021') and not re.search(r'X\d+|Y\d+|已行', m.group(1)):
                        坏.append('%s 之「B＋C 之候」未入账：须引瑕疵总账之 X 号（带限）或写「已行：<提交或器>」——账限哨按限催（1021）' % 名)
        if 自律(名, '1015') and not 简:     # ★1015 起之复盘须答完美之问（1021 简式免之）
            完 = re.search(r'^## 完美之问[^\n]*\n(.*?)(?=^## |\Z)', t, re.M | re.S)
            if not 完:
                坏.append('%s 缺「## 完美之问」（残缺、独立之眼、未验之断）' % 名)
            else:
                for 项 in ('残缺', '独立之眼', '未验之断'):
                    m = re.search(r'^- %s：(.*)$' % 项, 完.group(1), re.M)
                    if not m or not m.group(1).strip() or m.group(1).strip().startswith('（填'):
                        坏.append('%s 之完美之问缺「%s」' % (名, 项))
        if 新律之档(名):
            坏 += 新律之坏(名, t, root)
        坑节 = t.split('## 坑', 1)[1] if '## 坑' in t else ''
        号 = 坑号们(坑节)
        if '## 坑' in t and not re.search(r'^\s*[-*]?\s*无新坑', 坑节, re.M) and not 号:
            坏.append('%s 坑节既无坑账之号、又未写「无新坑」' % 名)
        if 有号 is not None and 号 - 有号:
            坏.append('%s 坑节点了坑账里没有之号：%s（先 工具/方法坑账.py --立）' % (名, ''.join(sorted(号 - 有号))))
    坏 += 连无之坏(进化诸, root)
    return not 坏, 坏


def 效账(root=ROOT):
    """自诸复盘之「## 效」汇一表（唯一之源即复盘档，⛔另存而失同步），按类比上回。"""
    行 = []
    for f in sorted(glob.glob(os.path.join(root, '设定', '复盘', '*.md'))):
        t = open(f, encoding='utf-8').read()
        效 = re.search(r'^## 效[^\n]*\n(.*?)(?=^## |\Z)', t, re.M | re.S)
        if not 效:
            continue
        g = lambda k: (re.search(r'^- %s：(.*)$' % k, 效.group(1), re.M) or [None, ''])[1].strip()
        金 = lambda k: float((re.search(r'\$(\d+(?:\.\d+)?)', g(k)) or [0, '0'])[1])
        行.append(dict(档=os.path.basename(f), 类=g('类').split('（')[0].strip(), 总=金('总费'), 目=金('服务目标之费'), 废=金('浪费'), 机=金('机器能办而花token')))
    print('%-34s %-8s %9s %9s %7s %9s %9s' % ('复盘', '类', '总费', '服务目标', '之占', '浪费', '机器能办'))
    上 = {}
    for r in 行:
        占 = 100.0 * r['目'] / r['总'] if r['总'] else 0
        比 = ''
        if r['类'] in 上:
            p = 上[r['类']]
            比 = '｜比上回同类：总费 %+.2f、浪费 %+.2f、之占 %+.0f%%' % (r['总'] - p['总'], r['废'] - p['废'], 占 - (100.0 * p['目'] / p['总'] if p['总'] else 0))
        print('%-34s %-8s %9.2f %9.2f %6.0f%% %9.2f %9.2f%s%s' % (r['档'][:34], r['类'][:8], r['总'], r['目'], 占, r['废'], r['机'], '  ⛔机器能办而花' if r['机'] > 0 else '', 比))
        上[r['类']] = r
    return 行


def 方法账之草(W, 题, 平台, 总金, root=ROOT):
    """★1113 X106①（451、452 二坐俱漏方法账升级链之行，皆由下一坐补）：章之简式起草时同草其行（零 token）——
    件名（段案之重、日，正文之名）、所废之默、费（平台与 Run）、较旧之费（比上一行之 Run）俱自填；总编辑只改「进化」一格与效。
    已有本 W 之行⛔重添。→ 所添之行或 None。"""
    p = os.path.join(root, '设定', '方法账.md')
    if not os.path.exists(p):
        return None
    t = open(p, encoding='utf-8').read()
    if re.search(r'^\| %s·' % re.escape(W), t, re.M):
        return None
    m = re.search(r'第(\d+)章', 题)
    名 = 题
    if m:
        n = int(m.group(1))
        try:
            import 章料
            节 = 章料.段案行(n, root)
        except Exception:
            节 = ''
        重 = (re.search(r'^- 重：(\S+)', 节, re.M) or [None, '?'])[1]
        日 = (re.search(r'^- 日：(\S+)', 节, re.M) or [None, '?·?'])[1]
        try:
            import 造式验
            档 = 造式验.正文档(n, root)
        except Exception:
            档 = None
        章名 = os.path.basename(档).rsplit('_', 1)[-1][:-3] if 档 else '?'
        名 = '第%d章（造式二代·%s·%s·%s）' % (n, 重, 日, 章名)
    前 = re.findall(r'^\| W\d+·第(\d+)章[^|]*\|[^|]*\| [^|]*Run \$([\d.]+)', t, re.M)
    较 = ''
    if 前 and 总金:
        k, v = 前[-1][0], float(前[-1][1])
        较 = 'Run %+.1f%%（%s $%.2f）' % ((总金 - v) / max(v, 0.01) * 100, k, v)
    费 = ('$%.2f（平台）' % 平台 if isinstance(平台, (int, float)) else '%s（平台）' % 平台) + '；Run $%.2f' % 总金
    行 = '| %s·%s | 所废：无（常章一件）；进化（总编辑填：入账 X 号／已行带凭／无：由） | %s | 较旧：效——（总编辑填）；费——%s |' % (W, 名, 费, 较 or '（无前行可比）')
    open(p, 'a', encoding='utf-8').write(('' if t.endswith('\n') else '\n') + 行 + '\n')
    return 行


def 执笔之终(诸, root=ROOT):
    """★X126（W906 环2）：诸 (Run 目录, 费审之行) → 「## 执笔之终」表之行（⛔手书败因：400—473 手书之误五）。
    终因、拒、API 错、撞顶取费审；稿在盘取其 Run 之 journal（执笔之 label → result 之 file），照 承.查 之尺：≥200 字节、有【本章亮点】。"""
    表 = []
    for d, 行 in 诸:
        档 = {}
        jp = os.path.join(d, 'journal.jsonl')
        if os.path.exists(jp):
            标 = {}
            for l in open(jp, encoding='utf-8', errors='replace'):
                try:
                    e = json.loads(l)
                except Exception:
                    continue
                if e.get('type') == 'started' and str(e.get('label', '')).startswith('执笔'):
                    标[e.get('key')] = e['label']
                elif e.get('type') == 'result' and e.get('key') in 标:
                    m = re.search(r'"file":\s*"([^"]+)"', json.dumps(e.get('result'), ensure_ascii=False))
                    if m:
                        档[标[e['key']]] = m.group(1)
        for r in 行:
            if not r['名'].startswith('执笔'):
                continue
            f = 档.get(r['名'])
            p = f if (f and os.path.isabs(f)) else os.path.join(root, f) if f else ''
            if not p:
                盘 = '无交'
            elif not os.path.exists(p) or os.path.getsize(p) < 200:
                盘 = '缺／不足200字节'
            else:
                盘 = '在' if '【本章亮点】' in open(p, encoding='utf-8', errors='replace').read() else '稿半（无【本章亮点】）'
            表.append('| %s | %s | %d | %s | %d | %s |' % (r['名'], r.get('终因') or '—', r.get('拒', 0), '/'.join(r.get('错') or []) or '—', r.get('截', 0),
                                                       ('%s（%s）' % (盘, os.path.basename(f))) if f else 盘))
    if not 表:
        return ['- （无执笔之席）']
    return ['| 席 | 终因（末回 stop_reason） | 拒 | API 错 | 撞顶 | 稿在盘 |', '|---|---|---|---|---|---|'] + 表


def 总编辑之件(W):
    """W9xx（W900 起）係总编辑之坐之件——其费入「总编辑之坐·<日>」，复盘⛔记主环切片。"""
    m = re.match(r'W(\d+)$', str(W or ''))
    return bool(m) and int(m.group(1)) >= 900


费势之界 = 1.05    # 〔执行之制·治12〕与 法用册「每章一进」之证同界（近五÷前五 ≤1.05）
数之退之格 = '- 数之退：‹判›｜治：‹X›'   # 空格：⛔中「每章一进」之证式（数之退[：:].{4,}治：X\d+）——总编辑填判与 X 号方中


def 题之章(题):
    """章之复盘之题（第482章／482造式，同 _章复盘式 之认）→ 章号｜None（非章之件⛔添治19、治12 之报）。"""
    m = re.match(r'第?(\d{3})(?:章|造式)', str(题 or ''))
    return int(m.group(1)) if m else None


def 封後之红(n, root=ROOT, 取=True, 读=None):
    """〔执行之制·治19（W918 环6·C2「封後之红没有入复盘」）〕零 token 取 备份/报 之 报/推/章-(n-1).json（推报.读·同 接棒守之尺）→ 一行。
    名＝闸之红（「✗」之格、「⛔全测未过：」之格，去器红）；无闸红而有器红即书器之红；红／拒／败而无格即书其果与首行；成而无红即「无」；
    无报、读不出、崩 → 「封後之红：取不得」。只印⛔拦（⛔入任何之证）。读：测之注（枝 → dict｜None）。"""
    枝 = '章-%d' % (int(n) - 1)
    try:
        if 读 is None:
            import 推报
            d = 推报.读(枝, root, 取=取)
        else:
            d = 读(枝)
    except Exception:
        d = None
    if not isinstance(d, dict) or not d.get('果'):
        return '封後之红：取不得'
    器 = [str(x) for x in d.get('器红') or [] if x]
    闸 = []
    for l in d.get('红') or []:
        s = str(l).strip()
        if s.startswith('✗'):
            名们 = s[1:].split()[:1]
        elif s.startswith('⛔全测未过：'):
            名们 = re.split(r'[、，,]', s.split('：', 1)[1])
        else:
            continue
        for x in 名们:
            x = re.split(r'[\s（(]', x.strip())[0]
            if x and x not in 器 and x not in 闸:
                闸.append(x)
    果 = str(d.get('果'))
    注 = ['报/推/%s·果 %s%s' % (枝, 果, '·因 %s' % d['因'] if d.get('因') else '')]
    if 闸:
        头 = '、'.join(闸)
        if 器:
            注.append('另器之红 %d：%s' % (len(器), '、'.join(器)))
    elif 器:
        头 = '器之红 %d：%s' % (len(器), '、'.join(器))
    elif 果 in ('红', '拒', '败'):
        首 = next((str(x).strip() for x in d.get('红') or [] if str(x).strip()), '')
        头 = '%s（%s）' % ('在飞' if 果 == '败' and d.get('因') == '重派' else 果, 首[:80] or '无红行')
    else:
        头 = '无'
    if d.get('逾'):
        注.append('器红逾限：%s' % '、'.join(str(x) for x in d['逾']))
    return '封後之红：%s（%s）' % (头, '；'.join(注))


def 费势之行(n, root=ROOT):
    """〔执行之制·治12 之报（W918 环6）〕→ (行们, 逾否)：「费势：<近五÷前五>」——复用 法用之守.费势（482 入主之算·数源同章量），⛔另算；
    逾 1.05（或算不得）即添「数之退：‹判›｜治：‹X›」之空格——只 ⚠（总章:58「钱已花，⛔以配额拦书」），⛔入每章一进之证。"""
    由 = '近五或前五缺一章之数（费账）'
    try:
        import 法用之守
        v = 法用之守.费势(int(n), root)
    except Exception as e:
        v, 由 = None, '算崩：%s' % str(e)[:80]
    窗 = '近五 %d—%d 之均 ÷ 前五 %d—%d 之均·法用之守.费势' % (n - 4, n, n - 9, n - 5)
    if v is not None and v <= 费势之界:
        return ['- 费势：%.3f（%s·≤%.2f）' % (v, 窗, 费势之界)], False
    return ['- 费势：%s（%s·%s）' % ('%.3f' % v if v is not None else '算不得', 窗, ('逾 %.2f' % 费势之界) if v is not None else 由),
            数之退之格 + '（⚠ 只报⛔拦：总编辑填数退之判与治之之号·带限、由账限哨管——⛔只写字）'], True


def 起草(W, 题, runs, root=ROOT, 日=None, 自=None, 至=None, 简=False, 平台=None, 取报=True):
    日 = 日 or time.strftime('%m%d', time.gmtime())
    出 = os.path.join(root, '设定', '复盘', '%s_%s_%s.md' % (日, W, 题))
    if os.path.exists(出):
        print('⛔ 已在：%s（⛔覆——要补就直接改它）' % os.path.relpath(出, root)); return None
    os.makedirs(os.path.dirname(出), exist_ok=True)
    件 = {}
    try:
        账 = json.load(open(os.path.join(root, '设定', '工作流账.json'), encoding='utf-8'))
        件 = next((x for x in 账['件'] if x['id'] == W), {})
    except Exception:
        pass
    自 = 自 or 件.get('起')
    费段, 疑 = [], []
    费审之行 = []
    诸终 = []
    流程 = []
    总金 = 0.0
    机总 = 0.0          # ★1027 复核所逮：诸 Run 之机器之活之席（费审.类）——简式之「机器能办而花token」照填（旧恒填 $0，#5 #58 之验遂空）
    for r in runs:
        d = r if os.path.isdir(r) else (glob.glob(os.path.expanduser('~/.claude/projects/*/*/subagents/workflows/%s' % r)) or [r])[0]
        if not os.path.isdir(d):
            费段.append('- Run %s：找不到其目录（非工作流之席，耗费照其回执手填）' % r); continue
        行 = 费审.审(d)
        费审之行 += 行
        诸终.append((d, 行))
        rid = os.path.basename(d.rstrip('/'))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            费审.印(行, rid=rid)
            费审.记(rid, '%s·%s' % (W, 题), 行, 费审.通知之数(rid), root)   # ★随时记：复盘起草即补记其 Run（⛔漏记）
        费段.append('### Run %s\n\n```\n%s```' % (r, buf.getvalue()))
        流程.append('- Run %s：%s' % (r, ' → '.join('%s(%s)' % (x['名'], x['起']) for x in 行)))
        金 = sum(x['金'] for x in 行) or 1e-9
        总金 += 金
        for x in sorted(行, key=lambda x: -x['金'])[:3]:
            疑.append('- 花费最多：%s（$%.2f；%d 回、工具 %d）——是在造，还是在翻料／办机器之活？' % (x['名'], x['金'], x['回'], x['具']))
        import re as _re
        机 = sum(x['金'] for x in 行 if _re.search(dict(费审.类)['机器之活'], x['名']))
        机总 += 机
        if 机:
            疑.append('- 机器之活（定位／机闸／案席／封版）占美元 %d%%——凡机器能办者，下回归脚本' % (100 * 机 / 金))
    主 = None
    if 自:
        try:
            主 = 费审.主环(自.replace('Z', ''), 至=至.replace('Z', '') if 至 else None)
        except Exception:
            主 = None
    载 = 费审.主环之重载(自.replace('Z', '') if 自 else None, 至.replace('Z', '') if 至 else None) if 自 else (0, 0.0)
    等 = 费审.主环之等(自.replace('Z', '') if 自 else None, 至.replace('Z', '') if 至 else None) if 自 else (0, 0.0)
    机段 = '- 主环非写作之活：（无起时）'
    if 自:
        try:
            import 机械账
            m = 机械账.账(自=自.replace('Z', ''), 至=至.replace('Z', '') if 至 else None)
            写 = {名 for 名, 是, _ in 机械账.类 if 是} | {'答话'}
            非 = sorted([(k, v) for k, v in m.items() if not k.startswith('（') and k not in 写], key=lambda kv: -kv[1][1])
            总 = sum(v[1] for k, v in m.items() if not k.startswith('（'))
            机段 = '- 主环非写作之活：机器自认 $%.2f（占主环 %d%%）——前三：%s（坑㉔：一件机械之活一条命令；候即止）' % (
                sum(v[1] for _, v in 非), 100 * sum(v[1] for _, v in 非) / 总 if 总 else 0,
                '；'.join('%s %.0f 回 $%.2f' % (k, v[0], v[1]) for k, v in 非[:3]))
        except Exception as e:
            机段 = '- 主环非写作之活：（机械账读不出：%s）' % e
    # 〔1124·执行之制 批二·乙〕W9xx（总编辑之件）其坐之日费已以「总编辑之坐·<日>」整记——⛔再记主环切片（重计）
    if 主 and not 总编辑之件(W):
        with contextlib.redirect_stdout(io.StringIO()):
            费审.记('主环:%s' % 自.replace('Z', ''), '%s·%s' % (W, 题), [主], None, root, 时=自)   # ★随时记
    # 〔执行之制·治19、治12 之报（W918 环6）〕章之复盘添二行（零 token·只印⛔拦）：封後之红（报/推/章-(N-1)）、费势（诸 Run 已记入费账之後算）
    章 = 题之章(题)
    章报, 势逾 = [], False
    if 章:
        势行, 势逾 = 费势之行(章, root)
        章报 = ['- ' + 封後之红(章, root, 取=取报)] + 势行
    主段 = ['- 主环（总编辑）自 %s 至 %s：美元 $%.2f｜来回 %d｜全量 %d｜缓存读 %d｜产出 %d（主环每回工具都重发整个上下文——坑⑮）' % (自, 至 or '今', 主['金'], 主['回'], 主['全'], 主['读'], 主['出'])] if 主 else ['- 主环之费：（无起时或读不出主会话之记）']
    文 = ['# 复盘·%s·%s（%s 立）' % (W, 题, 日), '',
         '## 任务', '',
         '- 名：%s' % 件.get('名', ''), '- 目的：%s' % str(件.get('目的', ''))[:400],
         '- 停止线：%s' % 件.get('停止线', ''), '- 预估：%s' % 件.get('预估', ''),
         '- 裁：%s' % '；'.join('%s %s' % (x.get('法'), str(x.get('由', ''))[:160]) for x in 件.get('裁', [])), '',
         '## 流程（实走·自动）', ''] + (流程 or ['- （无 Run——总编辑亲手之任务，照「制作过程」）']) + ['',
         '## 制作过程（任务起後之提交·git 自动）', ''] + 制作(自, root, 至) + ['',
         '## 产出', '', '（总编辑填：成了什么、质之实据——致命数、行家对拍库之分、盲读）', '',
         '## 耗费', '', '- 合计美元（诸席）：$%.2f（各 Run 详下；逐回照 设定/价目.json 精算，已入 设定/费账.json）' % 总金] + 主段 + [''] + 费段 + ['',
         '## 执笔之终（X126·器录⛔手书）', ''] + 执笔之终(诸终, root) + ['',
         '## 资源分配（资源分配官·1009）', '', 分配表(费审之行), '',
         '## 效（每任务必记·1009 作者令「token 有没有浪费、有没有服务於最该服务之目标」）', '',
         '- 类：（填：一章／造剧情／核验／治器设计……——效账按类比上回）',
         '- 目标：（填：此件最该服务之目标一句）',
         '- 总费：$%.2f（自动：诸席 $%.2f＋主环 $%.2f）' % (总金 + (主['金'] if 主 else 0), 总金, 主['金'] if 主 else 0),
         ] + (['- 平台之实：$%.2f（本会话 get_session 之 cost_usd·X56：以此为准；器计 $%.2f，差 %.1f 倍）' % (平台, 总金 + (主['金'] if 主 else 0), 平台 / max(总金 + (主['金'] if 主 else 0), 0.01))]
              if isinstance(平台, (int, float)) else ['- 平台之实：%s（以器计之总费为准）' % 平台] if 平台 else []) + [
         '- 服务目标之费：$（填：直接产出目标之席与来回之费，引费审之类或费账）',
         '- 浪费：$（填：无用功逐条之 $ 合计）',
         '- 机器能办而花token：$（填：须 $0；非零即入坑账。主环等待／轮询之回，机器自认：%d 回 $%.2f）' % 等,
         '- 闲置重载：机器自认 %d 回 $%.2f（会话闲逾一时、缓存过期而整份上下文重写——坑㉓；长停宜开新会话接交接档）' % 载,
         机段] + 章报 + ['',
         '## 与上回比（一次比一次好·1009）', '', '| 项 | 上回同类（填其复盘档名与数） | 本回 | 判 |', '|---|---|---|---|', '| 造之占 | | | 须↑ |', '| 总费（美元，费审精算） | | | 须↓ |', '| 质（致命数、拍库之分、盲读） | | | 须不劣 |', '', '（三样俱合方算进化；不合即写其因、其改）', '',
         '## 无用功', '', '机器之疑（总编辑逐条判：真费、或该花）：'] + (疑 or ['- （无 Run 可审）']) + ['', '（总编辑填：哪里花了大量 token 与时而无实果，其根）', '',
         '## 刀刃', '', '（总编辑填：钱花在哪儿真出了果）', '',
         '## 改进方案', '', '（总编辑填：具体到改哪档哪条；下回照办之验——下回之费审拿什么数比）', '',
         '## 虹吸之问（1015 作者令「方法照虹吸、虫洞不停进化，服务於中国最好看之小说」·法典一「虹吸之律」）', '',
         '- 重付：$（填：本件所付而早已付过之料——章记、病册、诸席之交、费账；须 $0，非零即入坑账）',
         '- 可流：（填：本件之活有无会重复者；已做成流水线之一环否——封版／记席／全测；未做者写其计）',
         '- 顺势：（填：本件有无另起一席专办、本可由已在做之事顺带产出者）',
         '- 下一回之法：（填：照上三问，此类之活下回之法比本回好在哪——具体到改哪档）',
         '- B＋C 之候：（填：一条效更好且费更省之候选新法——效之计、费之计、凭什么；下一件照上线之律试之）', '',
         '## 完美之问（1015 作者令「所有的一切都必须达到绝对的完美」·法典一「完美之律」）', '',
         '- 残缺：（填：本件交出後仍知之缺，逐条带限；无则写「无」）',
         '- 独立之眼：（填：谁验——驳席、盲读、负测、对照之试；逮了什么、治了没有）',
         '- 未验之断：（填：未经跑或测之断语；无则写「无」，有则逐条写其验之计）', '',
         '## 坑', '', '（每条点坑账之号：新坑先 `python3 工具/方法坑账.py --立 名 根 治 计`；旧坑复踩 `--复踩 号 "……；治：……"`；并入法典。无则写「无新坑」）', '']
    if 简:   # ★1021 简式：任务、流程、制作、耗费、效（数俱器填）＋三问三句＋坑；长节俱去（作者令「总结不要过度消耗」）
        止 = 文.index('## 与上回比（一次比一次好·1009）')
        文 = [x for x in 文[:止] if not x.startswith('## 产出') and not x.startswith('（总编辑填：成了什么')]
        _名 = str(件.get('名', '')) + ' ' + 题      # ★1027：类照件名（旧恒填「一章」——W72、W73 之治器与审入写书之占，费哨失真）
        _类 = ('一章' if re.search(r'第\d+章|\d{3}造式|造式二代', _名) else '造剧情' if '剧情庭' in _名
              else '核验' if re.search(r'审', _名) else '治器设计')
        文 = [('- 类：%s' % _类 if x.startswith('- 类：（填') else
              ('- 目标：写%s，以最少之钱写到最好' % 题 if _类 == '一章' else '- 目标：办%s，以最少之钱办到最好' % 题) if x.startswith('- 目标：（填') else
              '- 服务目标之费：$%.2f（自动：诸席）' % 总金 if x.startswith('- 服务目标之费：') else
              '- 机器能办而花token：$%.2f（自动：机器之活之席 $%.2f＋主环等待 %d 回 $%.2f）' % (机总 + 等[1], 机总, 等[0], 等[1])
              if x.startswith('- 机器能办而花token：') else x) for x in 文]
        文 += ['## 三问（1021 作者令：每章之始与末一想即得，⛔长文）', '',
              '- 法行否：（填一句：原法还靠谱否——费比上章、致命、盲读）',
              '- 最贵之席值否：（填一句：最贵之席值不值，可省之数）',
              '- 进化：（填一句：一条更省更好之改——入瑕疵总账 X 号带限，或「已行：」带凭（工具/<器>、法用#<法>、改单#G…），或「无：<所探之候与弃之之由>」；章之复盘⛔连三无）', '',
              '## 坑', '', '- 无新坑']
    open(出, 'w', encoding='utf-8').write('\n'.join(文))
    if 简 and _类 == '一章':                     # ★1113 X106①：方法账升级链之行同草（⛔下一坐补）
        _行 = 方法账之草(W, 题, 平台, 总金, root)
        if _行:
            print('✓ 方法账之行已草（设定/方法账.md 末行）——总编辑只改「进化」与「效」二格')
    print('✓ 起草 %s——%s' % (os.path.relpath(出, root), '三问三句与「浪费」之数须总编辑亲填（简式）' if 简 else '「产出」「与上回比」「无用功」之判「刀刃」「改进方案」「坑」须总编辑亲填'))
    if 章报:                                      # 〔治19、治12 之报〕只印⛔拦
        print('  %s' % 章报[0][2:])
        print(('⚠ %s——复盘「数之退：‹判›｜治：‹X›」之空格待总编辑填（只 ⚠·⛔拦封·⛔入每章一进之证）' if 势逾 else '  %s') % 章报[1][2:])
    return 出


def 自测():
    t = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(t, '设定'))
        json.dump({'件': [{'id': 'W9', '名': '测', '目的': '测', '裁': [{'法': '取', '由': '达'}]}]},
                  open(os.path.join(t, '设定', '工作流账.json'), 'w'), ensure_ascii=False)
        rd = os.path.join(t, 'run'); os.makedirs(rd)
        json.dump({'description': '封版'}, open(os.path.join(rd, 'agent-1.meta.json'), 'w'), ensure_ascii=False)
        open(os.path.join(rd, 'agent-1.jsonl'), 'w').write(json.dumps({'type': 'assistant', 'timestamp': '2026-10-09T01:00:00Z', 'message': {'usage': {'cache_read_input_tokens': 50}, 'content': []}}) + '\n')
        with contextlib.redirect_stdout(io.StringIO()):
            f = 起草('W9', '测', [rd], t, '1009')
            g = 起草('W9', '测', [rd], t, '1009')
        s = open(f, encoding='utf-8').read() if f else ''
        ok = bool(f) and g is None and all(k in s for k in ('## 耗费', '## 无用功', '## 改进方案', '## 坑', '## 流程', '## 制作过程')) and '机器之活' in s and '主环非写作之活' in s and '## 虹吸之问' in s and '## 完美之问' in s
        ok = ok and 验(t)[0] is False                                   # 草稿之坑节、效节未填 → 闸红
        ok = ok and '## 执笔之终' in s
        # ★X126：执笔之终——journal 之执笔 label 认其稿；拒、API 错、稿在盘照录
        稿 = os.path.join(t, '起草_稿一.md'); open(稿, 'w', encoding='utf-8').write('字' * 120 + '【本章亮点】')
        open(os.path.join(rd, 'journal.jsonl'), 'w').write('\n'.join(json.dumps(x, ensure_ascii=False) for x in (
            {'type': 'started', 'key': 'a', 'label': '执笔·甲·物证'}, {'type': 'result', 'key': 'a', 'result': {'draft': {'file': 稿}}},
            {'type': 'started', 'key': 'b', 'label': '执笔·乙·回声'})))
        表 = 执笔之终([(rd, [dict(名='执笔·甲·物证', 终因='end_turn', 拒=0, 错=[], 截=0), dict(名='执笔·乙·回声', 终因='API错:529', 拒=1, 错=['529'], 截=0),
                          dict(名='选·行家兼两眼', 终因='end_turn')])], t)
        ok = ok and len(表) == 4 and '在（起草_稿一.md）' in 表[2] and 'API错:529 | 1 | 529' in 表[3] and '无交' in 表[3]
        s2 = open(f, encoding='utf-8').read()
        s2 = re.sub(r'- 类：.*', '- 类：核验', s2); s2 = re.sub(r'- 目标：.*', '- 目标：测', s2)
        s2 = re.sub(r'- 服务目标之费：.*', '- 服务目标之费：$0', s2); s2 = re.sub(r'- 浪费：.*', '- 浪费：$0', s2)
        s2 = re.sub(r'- 机器能办而花token：.*', '- 机器能办而花token：$0', s2)
        open(f, 'w', encoding='utf-8').write(s2 + '无新坑\n')
        ok = ok and 验(t)[0] is True
        open(f, 'w', encoding='utf-8').write(re.sub(r'- 浪费：.*', '- 浪费：约 $1（估）', s2) + '无新坑\n')
        ok = ok and 验(t)[0] is True                                    # 「约 $N」亦过
        open(f, 'w', encoding='utf-8').write(re.sub(r'- 浪费：.*', '- 浪费：约一块', s2) + '无新坑\n')
        ok = ok and 验(t)[0] is False                                   # 无 $ 之数仍红
        os.remove(f)
        # ★1027 执行之审 #5 #58 #81②：1027 起之档——逾估无由即红、写「逾估：」即过；机器之活逾 5% 未引账即红、引在账之 X 或已行之器即过；旧档（1026）⛔追
        json.dump({'件': [{'id': 'W9', '名': '测', '目的': '测', '预估': '约 2 时、$10', '裁': []}]},
                  open(os.path.join(t, '设定', '工作流账.json'), 'w'), ensure_ascii=False)
        open(os.path.join(t, '设定', '瑕疵总账.md'), 'w', encoding='utf-8').write('## 未治\n| X7 | 机器之活 | s | t | 420 段前 |\n')
        os.makedirs(os.path.join(t, '工具'), exist_ok=True)
        open(os.path.join(t, '工具', '某器.py'), 'w').write('#')
        模 = ('# 复盘\n## 耗费\n- x\n## 效\n- 类：一章\n- 目标：测\n- 总费：$%s\n- 服务目标之费：$1\n- 浪费：$0\n- 机器能办而花token：$%s\n'
             '## 三问\n- 法行否：行\n- 最贵之席值否：值\n- 进化：%s\n%s## 坑\n- 无新坑\n')
        def 局(日, 总, 机, 进, 尾=''):
            for x in glob.glob(os.path.join(t, '设定', '复盘', '*.md')):
                os.remove(x)
            open(os.path.join(t, '设定', '复盘', '%s_W9_测.md' % 日), 'w', encoding='utf-8').write(模 % (总, 机, 进, 尾))
            return 验(t)
        r1 = 局('1027', 20, 0, '无：测')                                   # 20 > 10×1.5 而无由 → 红
        r2 = 局('1027', 20, 0, '无：测', '- 逾估：执笔撞顶重派三席，估未计重派\n')
        r3 = 局('1026', 20, 0, '无：测')                                   # 旧档⛔追
        r4 = 局('1027', 12, 1, '无：测')                                   # 机 1/12 > 5% 而未引 → 红
        r5 = 局('1027', 12, 1, '入账 X7（限 420 段前）')
        r6 = 局('1027', 12, 1, '已行：工具/某器.py 归脚本')
        r7 = 局('1027', 12, 1, '入账 X99（账上无此号）')
        r8 = 局('1027', 12, 0.5, '无：测')                                 # 0.5/12 ≈ 4% → 不红
        ok = ok and (r1[0] is False and '逾估' in r1[1][0] and r2[0] and r3[0] and r4[0] is False and '机器能办' in r4[1][0]
                     and r5[0] and r6[0] and r7[0] is False and r8[0])
        # 〔执行之制·治13(a)〕件无估（或无件）→ 取方案之「**费**」行之 $，逾估之验复起
        json.dump({'件': [{'id': 'W9', '名': '测', '目的': '测', '预估': '约 2 时', '裁': []}]},
                  open(os.path.join(t, '设定', '工作流账.json'), 'w'), ensure_ascii=False)
        os.makedirs(os.path.join(t, '设定', '方案'), exist_ok=True)
        open(os.path.join(t, '设定', '方案', 'W9.md'), 'w', encoding='utf-8').write('# W9\n- **费**：诸席 ≤$10（中章）\n')
        r9 = 局('1027', 20, 0, '无：测')
        ok = ok and 估之元('W9', t) == 10.0 and 估之元('W8', t) is None and r9[0] is False and '逾估' in r9[1][0]
        os.remove(os.path.join(t, '设定', '方案', 'W9.md'))
        json.dump({'件': [{'id': 'W9', '名': '测', '目的': '测', '预估': '约 2 时、$10', '裁': []}]},
                  open(os.path.join(t, '设定', '工作流账.json'), 'w'), ensure_ascii=False)
        # 跨年：「0105_W90_」仍验（W≥72）；「1026_W71_」、「1009_主环_」⛔追；「1027_主环_」验
        ok = ok and 总编辑之件('W911') and not 总编辑之件('W156') and not 总编辑之件('')   # 批二·乙
        ok = ok and 新律之档('0105_W90_第450章.md') and 新律之档('1027_W72_执行.md') and not 新律之档('1026_W71_第410章.md') \
            and not 新律之档('1009_主环_坑账.md') and 新律之档('1027_主环_x.md') \
            and 自律('0105_W90_第450章.md', '1015') and 自律('0105_主环_x.md', '1021') and not 自律('1014_W30_补因.md', '1015') \
            and 自律('1015_W31_388二代.md', '1015') and not 自律('1017_W51_全测并.md', '1018') and 自律('1020_W52_x.md', '1018')
        # --简 无 --平台 → 拒（rc=2）；--平台 不可分：由 → 起草（档记其由）
        p0 = subprocess.run([sys.executable, os.path.abspath(__file__), 'W9', '测', '--简'], capture_output=True, text=True, cwd=t)
        if p0.returncode != 2:                                          # 守未拦即会起草入真仓——当场清之（⛔留字）
            for x in glob.glob(os.path.join(ROOT, '设定', '复盘', '*_W9_测.md')):
                os.remove(x)
        ok = ok and p0.returncode == 2 and '--平台' in p0.stdout
        with contextlib.redirect_stdout(io.StringIO()):
            f2 = 起草('W9', '测二', [rd], t, '1027', 简=True, 平台='不可分：一会话跨三件')
        ok = ok and bool(f2) and '- 平台之实：不可分：一会话跨三件' in open(f2, encoding='utf-8').read()
        # ★1027 复核所逮（#5 #58 之验旧为空验）：简式之「机器能办而花token」旧恒填 $0——机器之活之席（封版）占满亦过；今照费审之类自填，
        #   1027 起之档其占逾 5% 而「进化」未引账即红；引在账之 X 号即过（放行之反例）
        rd2 = os.path.join(t, 'run2'); os.makedirs(rd2)
        json.dump({'description': '封版'}, open(os.path.join(rd2, 'agent-1.meta.json'), 'w'), ensure_ascii=False)
        open(os.path.join(rd2, 'agent-1.jsonl'), 'w').write(json.dumps({'type': 'assistant', 'timestamp': '2026-10-27T01:00:00Z', 'message': {
            'id': 'm1', 'model': 'claude-opus-5-5', 'usage': {'input_tokens': 10, 'cache_read_input_tokens': 4000000, 'output_tokens': 20000}, 'content': []}}) + '\n')
        for x in glob.glob(os.path.join(t, '设定', '复盘', '*.md')):
            os.remove(x)
        with contextlib.redirect_stdout(io.StringIO()):
            f3 = 起草('W9', '测三', [rd2], t, '1027', 简=True, 平台='不可分：一会话跨三件')
        s3 = open(f3, encoding='utf-8').read() if f3 else ''
        m3 = re.search(r'^- 机器能办而花token：\$(\d+\.\d+)（自动：机器之活之席 \$(\d+\.\d+)', s3, re.M)
        s3 = re.sub(r'- 法行否：.*', '- 法行否：行', s3); s3 = re.sub(r'- 最贵之席值否：.*', '- 最贵之席值否：值', s3)
        s3 = re.sub(r'- 浪费：.*', '- 浪费：$0', s3)
        s3 = re.sub(r'- 进化：.*', '- 进化：无：测', s3) + '\n无新坑\n'
        open(f3, 'w', encoding='utf-8').write(s3)
        r9 = 验(t)
        open(f3, 'w', encoding='utf-8').write(s3.replace('- 进化：无：测', '- 进化：入账 X7（限 420 段前）'))
        r10 = 验(t)
        ok = ok and bool(m3) and float(m3.group(1)) > 0 and m3.group(1) == m3.group(2) \
            and r9[0] is False and any('机器能办' in x for x in r9[1]) and r10[0] is True
        # ★1104 每章一进之实（1105 起之档）：进化须可追——在账之号、在盘之器、在册之法、在账之改单；「无：」由须八字；章之复盘连三无即红；旧档（1104）⛔追
        json.dump({'法': [{'id': '甲法'}], '待': [], '废': [{'id': '旧法'}]}, open(os.path.join(t, '设定', '法用册.json'), 'w'), ensure_ascii=False)
        json.dump({'单': [{'号': 'G1105-01'}]}, open(os.path.join(t, '设定', '改单账.json'), 'w'), ensure_ascii=False)
        长由 = '无：本章诸法俱已最省，所探二候俱效降而弃'
        def 进局(诸):
            for x in glob.glob(os.path.join(t, '设定', '复盘', '*.md')):
                os.remove(x)
            for 名, 进 in 诸:
                open(os.path.join(t, '设定', '复盘', 名), 'w', encoding='utf-8').write(模 % (12, 0, 进, ''))
            return 验(t)
        def 一(日, 进):
            return 进局([('%s_W9_测.md' % 日, 进)])[0]
        e = [一('1105', '已行：归脚本'), 一('1105', '已行：工具/某器.py 归脚本'), 一('1105', '已行：工具/无此器.py'),
             一('1105', '入账 X7（限 420 段前）'), 一('1105', '入账 X99（账上无此号）'), 一('1105', '无：测'), 一('1105', 长由),
             一('1105', '已行：法用#甲法'), 一('1105', '已行：法用#乙法'), 一('1105', '已行：法用#甲法乙'), 一('1105', '已行：改单#G1105-01'),
             一('1105', '已行：改单#G1105-09'), 一('1104', '无：测'), 一('1104', '已行：归脚本'), 一('0105', '无：测')]
        ok = ok and e == [False, True, False, True, False, False, True, True, False, False, True, False, True, True, False]
        c1 = 进局([('1105_W90_第500章.md', 长由), ('1105_W91_第501章.md', 长由), ('1105_W92_502造式.md', 长由)])
        c2 = 进局([('1105_W90_第500章.md', 长由), ('1105_W91_第501章.md', '入账 X7（限 520 段前）'), ('1105_W92_第502章.md', 长由)])
        c3 = 进局([('1104_W88_第498章.md', '无：旧档之由'), ('1104_W89_第499章.md', '无：旧档之由'), ('1105_W90_第500章.md', 长由)])
        c4 = 进局([('1105_W90_第500章.md', 长由), ('1105_W91_第501章.md', 长由), ('1105_W92_第502章.md', 长由), ('1105_W93_第502章.md', '已行：工具/某器.py')])
        c5 = 进局([('1105_W90_第500章.md', 长由), ('1105_W91_第502章.md', 长由), ('1105_W92_第503章.md', 长由)])
        ok = ok and c1[0] is False and any('连三章' in x and '502造式' in x for x in c1[1]) and c2[0] and c3[0] is False \
            and any('连三章' in x and '第500章' in x for x in c3[1]) and c4[0] and c5[0]
        # ★1113 X106①：方法账之行同草——添一行、件名自段案与正文、费比上一行之 Run；同 W 再草⛔重添
        open(os.path.join(t, '设定', '方法账.md'), 'w', encoding='utf-8').write(
            '| 件 | 法 | 费 | 判 |\n|---|---|---|---|\n| W1·第1章（造式二代·中·主·1·甲） | 所废：无 | $40.00（平台）；Run $40.00 | 较旧 |\n')
        r1 = 方法账之草('W2', '第2章', 30.0, 30.0, t); r2 = 方法账之草('W2', '第2章', 30.0, 30.0, t)
        ok = ok and r1 and r1.startswith('| W2·第2章（造式二代·') and 'Run -25.0%（1 $40.00）' in r1 and '进化（总编辑填' in r1 and r2 is None \
            and open(os.path.join(t, '设定', '方法账.md'), encoding='utf-8').read().count('| W2·') == 1
    finally:
        shutil.rmtree(t)
    过, 共 = 自测_报势()
    print('复盘·自测 %d/%d' % (int(ok) + 过, 1 + 共))
    return ok and 过 == 共


_样471 = {'ref': '章-471', '果': '红', '因': '', '器红': ['器物册·逐章回灌'], '逾': [], '红': [   # 回灌之料：备份/报 之 报/推/章-471.json 之红（原行照录）
    '✗ 全书检            ERROR=1', '✗ 分量闸            ⛔不足而无豁免：第468章',
    '✗ 器物册·逐章回灌       ★第463章·⛔ ★那一沓·「入」指拍1，而那一拍的白文里没有「纸」三字——拍号是抄的，不是数的',
    '⛔全测未过：全书检、分量闸、器物册·逐章回灌',
    '⛔推闸：读者可见之闸红 2（全书检、分量闸）——逐条治，⛔绕、⛔弱化；另器之红 1（器物册·逐章回灌）']}


def 自测_报势():
    """〔执行之制·治19、治12 之报（W918 环6）〕封後之红（回灌 471 → 全书检、分量闸；取不得；器之红；败）、费势（复用 法用之守.费势·逾 1.05 留空格）、
    起草之整局（临时之库·⛔网·⛔动真仓）、空格⛔中每章一进之证式。→ (过, 共)"""
    格 = []
    def T(名, 真):
        格.append(bool(真))
        if not 真:
            print('  ✗ 复盘·%s' % 名)
    # ① 封後之红：注其读（零网）
    s1 = 封後之红(472, 读=lambda 枝: _样471 if 枝 == '章-471' else None)
    T('治19 回灌 471：闸之红名（去器红）', s1.startswith('封後之红：全书检、分量闸（报/推/章-471·果 红') and '另器之红 1：器物册·逐章回灌' in s1)
    def 崩(枝):
        raise RuntimeError('网断')
    T('治19 取不得：无报、读崩、无果 → 「封後之红：取不得」', 封後之红(472, 读=lambda 枝: None) == '封後之红：取不得'
      and 封後之红(472, 读=崩) == '封後之红：取不得' and 封後之红(472, 读=lambda 枝: {'红': []}) == '封後之红：取不得')
    s3 = 封後之红(457, 读=lambda 枝: {'果': '成', '红': [], '器红': ['悬念哨', '复盘'], '逾': ['悬念哨']})
    s4 = 封後之红(478, 读=lambda 枝: {'果': '成', '红': [], '器红': []})
    s5 = 封後之红(475, 读=lambda 枝: {'果': '败', '因': 'merge', '红': ['⛔备候不成（因 merge）——未入片闸；看 run_url'], '器红': []})
    s6 = 封後之红(475, 读=lambda 枝: {'果': '败', '因': '重派', '红': [], '器红': []})
    T('治19 诸果：成而器红 → 器之红（并器红逾限）；成而无红 → 无；败 → 其果与首行；败·重派 → 在飞',
      s3.startswith('封後之红：器之红 2：悬念哨、复盘（报/推/章-456·果 成') and '器红逾限：悬念哨' in s3
      and s4.startswith('封後之红：无（报/推/章-477·果 成') and s5.startswith('封後之红：败（⛔备候不成') and '·因 merge' in s5
      and s6.startswith('封後之红：在飞（'))
    T('题之章：第482章／482造式 → 章；非章之题 → None', 题之章('第482章') == 482 and 题之章('482造式') == 482 and 题之章('测') is None
      and 题之章('执行之制批三批四') is None)
    证式 = r'数之退[：:].{4,}治：X\d+'     # 法用册「每章一进」之证式（执行之制·治12）
    t = tempfile.mkdtemp(prefix='复盘_报势_')
    try:
        os.makedirs(os.path.join(t, '设定'))
        def 账(费们):
            json.dump({'行': [{'名': 'W%d·第%d章' % (k, k), '键': 'wf_%d' % k, '美元': v} for k, v in 费们.items()]},
                      open(os.path.join(t, '设定', '费账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        # ③ 费势：复用 法用之守.费势（⛔另算）——升 20% → 逾、留空格；平 → 无空格；缺一章 → 算不得、留空格
        账({k: (10.0 if k <= 467 else 12.0) for k in range(463, 473)})
        行1, 逾1 = 费势之行(472, t)
        import 法用之守
        账({k: 10.0 for k in range(463, 473)})
        行2, 逾2 = 费势之行(472, t)
        账({k: 10.0 for k in range(463, 473) if k != 465})
        行3, 逾3 = 费势之行(472, t)
        T('治12 费势：升 20%% → 1.200 逾、留空格（%s）；平 → 1.000 无空格；缺一章 → 算不得、留空格' % 行1[0],
          逾1 and 行1[0].startswith('- 费势：1.200（近五 468—472 之均 ÷ 前五 463—467 之均') and 行1[1].startswith(数之退之格)
          and not 逾2 and len(行2) == 1 and 行2[0].startswith('- 费势：1.000') and 逾3 and 行3[0].startswith('- 费势：算不得') and len(行3) == 2)
        T('治12 空格（只 ⚠）⛔中每章一进之证式；总编辑填判与 X 号方中', not re.search(证式, 行1[1])
          and re.search(证式, 行1[1].replace('‹判›', '474 出前窗、费回 $55 而势仍逾').replace('‹X›', 'X140')))
        账({k: (10.0 if k <= 467 else 12.0) for k in range(463, 473)})
        T('治12 费势⛔另算：与 法用之守.费势 同数', 法用之守.费势(472, t) == 1.2)
        # ④ 起草之整局：临时之库立 备份/报 之 报/推/章-471.json（⛔网、⛔动真仓：去 GIT_* 之变、钩路置空）→ 章之复盘二行入「## 效」；非章之件⛔添
        env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
        def g(*a):
            return subprocess.run(['git', '-c', 'user.name=测', '-c', 'user.email=t@t', '-c', 'commit.gpgsign=false', '-c', 'core.hooksPath=/dev/null',
                                   '-c', 'init.defaultBranch=测'] + list(a), cwd=t, env=env, capture_output=True, text=True)
        os.makedirs(os.path.join(t, '报', '推'))
        json.dump(_样471, open(os.path.join(t, '报', '推', '章-471.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        g('init', '-q'); g('add', '报'); g('commit', '-q', '-m', '报')
        g('update-ref', 'refs/remotes/origin/备份/报', 'HEAD')
        T('治19 推报.读 之真路（临时之库·取=False）→ 全书检、分量闸', 封後之红(472, t, 取=False).startswith('封後之红：全书检、分量闸（'))
        with contextlib.redirect_stdout(io.StringIO()) as 印:
            f = 起草('W472', '第472章', [], t, '1124', 简=True, 平台=12.0, 取报=False)
            f2 = 起草('W9', '测', [], t, '1124', 简=True, 平台=12.0, 取报=False)
        s = open(f, encoding='utf-8').read() if f else ''
        效 = s.split('## 效', 1)[1].split('\n## ', 1)[0] if '## 效' in s else ''
        T('起草：章之复盘「## 效」添封後之红、费势与数之退之空格；印 ⚠；非章之件⛔添',
          '\n- 封後之红：全书检、分量闸（报/推/章-471·果 红' in 效 and '\n- 费势：1.200（' in 效 and ('\n' + 数之退之格) in 效
          and '⚠ 费势：1.200' in 印.getvalue() and not re.search(证式, s)
          and bool(f2) and '封後之红' not in open(f2, encoding='utf-8').read() and '费势' not in open(f2, encoding='utf-8').read())
        T('起草：二行⛔生 --验 之新坏', not [x for x in 验(t)[1] if re.search('封後|费势|数之退', x)])
    finally:
        shutil.rmtree(t, ignore_errors=True)
    return sum(格), len(格)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--自测']:
        sys.exit(0 if 自测() else 1)
    if a == ['--效账']:
        效账(); sys.exit(0)
    if a == ['--验']:
        o, 坏 = 验()
        print('✓ 复盘：诸档四节俱在、坑节俱点坑账之号' if o else '⛔ 复盘：\n  ' + '\n  '.join(坏))
        sys.exit(0 if o else 1)
    自 = 至 = None
    简 = '--简' in a
    a = [x for x in a if x != '--简']
    if '--自' in a:
        i = a.index('--自'); 自 = a[i + 1]; a = a[:i] + a[i + 2:]
    if '--至' in a:
        i = a.index('--至'); 至 = a[i + 1]; a = a[:i] + a[i + 2:]
    平台 = None
    if '--平台' in a:   # ★X56：本会话 get_session 之 cost_usd（器计曾低估 2.4 倍）
        i = a.index('--平台'); v = a[i + 1] if i + 1 < len(a) else ''; a = a[:i] + a[i + 2:]
        if re.match(r'不可分[：:]\s*(?:\S\s*){4,}', v):
            平台 = v
        else:
            try:
                平台 = float(v.lstrip('$'))
            except ValueError:
                print('⛔ --平台 须是 $ 之数（get_session 之 cost_usd），或「不可分：<由>」（由四字以上）'); sys.exit(2)
    if 简 and 平台 is None:   # ★1027 执行之审 #86：简式之费以平台之实为准——⛔无之即拒
        print('⛔ --简 须带 --平台 $X（本会话 get_session 之 cost_usd·X56：器计曾低估 2.4 倍）；一会话跨数件而分不出者写 --平台 "不可分：<由>"'); sys.exit(2)
    if len(a) < 2:
        print(__doc__); sys.exit(2)
    起草(a[0], a[1], a[2:], 自=自, 至=至, 简=简, 平台=平台)
