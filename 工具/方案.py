#!/usr/bin/env python3
"""方案（1009 立·作者令「设计方法之每一环都要绝对精准、绝对细心，⛔出任何差错——一环出错，整个方法就坏了；
每一环都要先精准确定它能做成，再去实施；⛔猜，要非常确定之後再去设计」）。

为何立：「零token之检」只问了「哪些机器能办、哪些非模型不可、多久、多少钱」——答案若是猜的，闸等於没有。
本器验 `设定/方案/<W>.md`：每一环都要有**确证**（实测之据），时与费要有数，败了怎么办要写明；
尚未确证之环须先列其「试」（小样实测之法），**未确证者有一条，即⛔开**——先试，确证了再移入逐环。

方案之格（`--模板 W 题` 生成）：
  ## 逐环
  | 环 | 做什么 | 谁办 | 确证 | 时 | 费 | 败则 |
    谁办：「脚本：<器>」或「模型：<为何机器办不了>」或「人：<谁>」
    确证：须引实据——费账之键（wf_…／主环:…）、Run、试：<命令及其果>、自测 n/n、工具/<器>
    时：带单位之数（秒／分／时）；费：$ 之数（照费账之实；模型之环须据费账同类之实）
    败则：此环败了怎么办（⛔空、⛔「—」）
  ## 未确证
  - 无      （或：- <何事未确证>；试：<怎么小样实测>）
  ## 合计
  - 时：…；费：$…；据：…
  ## 图之用        （W912 起·W9xx 总编辑之件；作者 1120 令「这不是每次都要用吗」：每件之设计必用体系总图）
  | 件 | 部 | 谁跑 | 谁读 | 判 |
    逐环「做什么」所书之件（工具/<x>.py、工具/席/<x>.js、.github/workflows/<x>.yml、设定/<x>.json|md）俱入其表（缺即坏；一件⛔书者⛔索其节）；
    其节由 `--图 W` 自 体系总图 之析机出（import 之·⛔另析）；表之「谁读」与今析不合、逐环书裸名（推.py、接棒守）而⛔入表只 ⚠。W1xx（写书之件）⛔索。
  ## 坑之检          （1027 起·W75 起之方案须有：逐坑写本法如何排除——坑㉛㊱）
  - ⑤ 等推用 推.py --等；⑰ pipefail；㊱ 改尺：消费者：grep -rn '<函名>' 工具/ → 工具/甲.py、工具/乙.py
    凡称改一把尺（取章、取镜、取线、计数之法……）者，须有「消费者：grep …」一行并列其档（坑㊱：一义跨器而漏其消费者）。

用法：
  python3 工具/方案.py --模板 W19 题      # 写 设定/方案/W19.md 之模板（已在则⛔覆）
  python3 工具/方案.py --验 W19           # 验一份；不过 rc=1
  python3 工具/方案.py --验全             # 验 设定/方案/ 下诸份（入全测）
  python3 工具/方案.py --图 W912          # 印「## 图之用」之节（逐环所改之件之部、谁跑、谁读、判·体系总图今树即算）以供贴入
  python3 工具/方案.py --自测
工作流账 `--开 W` 先验 设定/方案/W.md——不过即拒开。
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import os, sys, re, glob, time, tempfile, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
目录 = os.path.join('设定', '方案')
列 = ['环', '做什么', '谁办', '确证', '时', '费', '败则']
据式 = re.compile(r'wf_[0-9a-f]{8}-[0-9a-f]{3}|费账|主环:|Run|试[:：]|自测\s*\d+\s*/\s*\d+|工具/\S+\.(?:py|js)|设定/\S+\.(?:json|md)')
时式 = re.compile(r'\d+(?:\.\d+)?\s*(?:秒|分|时|小时)')
费式 = re.compile(r'\$\s*\d+(?:\.\d+)?')


def 节(文, 头):
    m = re.search(r'^## ' + re.escape(头) + r'[^\n]*\n(.*?)(?=^## |\Z)', 文, re.M | re.S)
    return m.group(1) if m else None


def 验文(文):
    坏 = []
    环节 = 节(文, '逐环')
    if 环节 is None:
        return ['无「## 逐环」一节']
    行 = [l.strip() for l in 环节.split('\n') if l.strip().startswith('|')]
    if not 行 or [c.strip() for c in 行[0].strip('|').split('|')] != 列:
        return ['逐环之表头须为：| %s |' % ' | '.join(列)]
    数据 = [l for l in 行[1:] if not re.fullmatch(r'\|[\s\-:|]+\|', l)]
    if not 数据:
        坏.append('逐环无一行')
    for l in 数据:
        c = [x.strip() for x in l.strip('|').split('|')]
        if len(c) != len(列):
            坏.append('行之栏数不对：%s' % l[:60]); continue
        环, 做, 谁, 证, 时, 费, 败 = c
        名 = '环 %s' % 环
        if not 做:
            坏.append('%s 缺「做什么」' % 名)
        m = re.match(r'(脚本|模型|人)\s*[:：]\s*(\S.*)', 谁)
        if not m:
            坏.append('%s 之「谁办」须为「脚本：<器>」「模型：<为何机器办不了>」「人：<谁>」' % 名)
        if not 据式.search(证):
            坏.append('%s 之「确证」无实据（须引费账之键、Run、试：命令及其果、自测 n/n、或工具之档）——⛔猜' % 名)
        if not 时式.search(时):
            坏.append('%s 之「时」须是带单位之数' % 名)
        if not 费式.search(费):
            坏.append('%s 之「费」须是 $ 之数' % 名)
        if not 败 or 败 in ('—', '-', '无'):
            坏.append('%s 缺「败则」（此环败了怎么办）' % 名)
    未 = 节(文, '未确证')
    if 未 is None:
        坏.append('无「## 未确证」一节（无则写「- 无」）')
    else:
        条 = [l.strip()[1:].strip() for l in 未.split('\n') if l.strip().startswith('-')]
        if not 条:
            坏.append('「未确证」一节空——无则写「- 无」')
        for x in 条:
            if x in ('无', '无。'):
                continue
            if not re.search(r'试[:：]', x):
                坏.append('未确证「%s」无「试：」（怎么小样实测）' % x[:40])
            坏.append('尚有未确证：「%s」——先跑其试，确证了再移入逐环，⛔开' % x[:40])
    合 = 节(文, '合计')
    if 合 is None or not 时式.search(合) or not 费式.search(合) or '据' not in 合:
        坏.append('「## 合计」须有时、$ 费与其据')
    # ★1014 上线之律（作者令「新弄出一个方法，要确定它绝对有效」）：方案之题标「新法」者，须有「## 前定之验」——
    #   试之前写死：比哪个基线、拿什么数、胜几分算胜、不胜即退（⛔先上线後找理由；⛔「再试一回」逾一次）
    首 = 文.split('\n', 1)[0]
    if '新法' in 首:
        前 = 节(文, '前定之验')
        if 前 is None:
            坏.append('题标「新法」而无「## 前定之验」（上线之律：基线、数、胜之界、不胜即退，试前写死）')
        else:
            for k in ('基线', '胜', '退'):
                if k not in 前:
                    坏.append('「前定之验」缺「%s」（上线之律）' % k)
    return 坏


坑之检之起 = 75          # 1027 立（坑㉛㊱·#42）：W75 起之方案须有「## 坑之检」；W74 以前之方案係史（⛔逼旧档补行）
改尺式 = re.compile(r'(?<![不无⛔未])(?:改|换|动)[^\n，。；|]{0,16}?(?:之)?(?:尺|计数之法|计数|取章|取镜|取线|取拍|取号)')
消费者式 = re.compile(r'消费者\s*[:：]\s*`?\s*grep\b[^\n]*')


def 坑之检之坏(文):
    """→ [坏]：须「## 坑之检」一节（非空）；逐环凡称改一把尺者，坑之检须有「消费者：grep …」一行且列其档（工具/…）。
    只认逐环（本法所做之事）——坑之检里述坑㊱之文⛔认作改尺（⛔误拦）。"""
    节文 = 节(文, '坑之检')
    if 节文 is None or not 节文.strip():
        return ['无「## 坑之检」一节（W%d 起·坑㉛㊱：逐坑写本法如何排除——踩过的坑⛔在新法里再现）' % 坑之检之起]
    坏 = []
    m = 改尺式.search(节(文, '逐环') or '')
    if m:
        行 = 消费者式.findall(节文)
        if not 行:
            坏.append('称改一把尺（「%s」）而坑之检无「消费者：grep -rn \'<函名>\' 工具/」一行（坑㊱）' % m.group(0)[:30])
        elif not re.search(r'工具/\S+\.(?:py|js)', 节文):
            坏.append('坑之检之「消费者」未列其档（grep 之果：工具/…）——坑㊱')
    return 坏


虫洞之择之起 = 910       # 1120 立（作者令「虫洞……就是找到最有效和最完美的方法……看看这个方法它是不是最好的方法，在各个方面」）：W910 起之方案须有「## 虫洞之择」
候式 = re.compile(r'^- 候[^:：\n]{0,8}[:：](.*)$', re.M)
取式 = re.compile(r'^- 取[:：](.*)$', re.M)


def 虫洞之择之坏(文):
    """→ [坏]：须「## 虫洞之择」一节——候选之法 ≥2（「- 候甲：<法>——效：…；费：…；险：…；质：…」，每候俱书效、费，并书险或质），
    并一「- 取：候X——由：…」（取之由：各方面最优）。⛔只列一法即取（无择即无虫洞）。"""
    节文 = 节(文, '虫洞之择')
    if 节文 is None or not 节文.strip():
        return ['无「## 虫洞之择」一节（W%d 起·作者 1120 令：先列候选之法 ≥2，逐法比其效、费、险、质，取各方面最优者并书其由）' % 虫洞之择之起]
    坏 = []
    候 = 候式.findall(节文)
    if len(候) < 2:
        坏.append('虫洞之择之候选之法只 %d（须 ≥2：「- 候甲：…」「- 候乙：…」——无择即无虫洞）' % len(候))
    for x in 候:
        缺 = [k for k in ('效', '费') if k not in x] + ([] if ('险' in x or '质' in x) else ['险或质'])
        if 缺:
            坏.append('候「%s」缺 %s 之比' % (x.strip()[:24], '、'.join(缺)))
    取 = 取式.findall(节文)
    if not 取:
        坏.append('虫洞之择无「- 取：候X——由：…」（取哪一法、凭什么各方面最优）')
    elif not any('由' in x for x in 取):
        坏.append('虫洞之择之「取」无其由（各方面何以最优）')
    return 坏


def _号(W):
    m = re.fullmatch(r'W(\d+)', str(W))
    return int(m.group(1)) if m else 0


图之用之起 = 912        # 1120 作者令（「跟执行主义不是都要结合起来会使用吗」·W912 环3）：W912 起之总编辑之件（W9xx）须有「## 图之用」——W1xx（写书之件）⛔索
件式 = re.compile(r'(工具/席/[\w\-]+\.js|工具/[\w\-]+\.py|\.github/workflows/[\w\-.]+\.yml|设定/[^\s/|，。、；：:（）()「」`*<>]+\.(?:json|md))')


def 要图(W):
    """须「## 图之用」否：W9xx 而号 ≥ 图之用之起（写书之件 W1xx ⛔索：⛔拖累写书）。"""
    return re.fullmatch(r'W9\d\d', str(W)) is not None and _号(W) >= 图之用之起


def 所改之件(文):
    """「## 逐环」表「做什么」栏所书之件（源序·去重）：工具/<x>.py、工具/席/<x>.js、.github/workflows/<x>.yml、设定/<x>.json|md
    （占位之「工具/<器>.py」⛔认）。"""
    出 = []
    for l in (节(文, '逐环') or '').split('\n'):
        l = l.strip()
        if not l.startswith('|') or re.fullmatch(r'\|[\s\-:|]+\|', l):
            continue
        c = [x.strip() for x in l.strip('|').split('|')]
        if len(c) != len(列) or c == 列:
            continue
        for m in 件式.finditer(c[1]):
            if m.group(1) not in 出:
                出.append(m.group(1))
    return 出


def 图之用之表(文):
    """「## 图之用」之表 → {件（去 `）: {栏: 值}}；无节 → None。"""
    t = 节(文, '图之用')
    if t is None:
        return None
    行 = [l.strip() for l in t.split('\n') if l.strip().startswith('|')]
    if not 行:
        return {}
    头 = [c.strip() for c in 行[0].strip('|').split('|')]
    出 = {}
    for l in 行[1:]:
        if re.fullmatch(r'\|[\s\-:|]+\|', l):
            continue
        c = [x.strip().strip('`') for x in l.strip('|').split('|')]
        if c and c[0]:
            出[c[0]] = dict(zip(头, c))
    return 出


def 图之用之坏(文):
    """→ [坏]：逐环书件者须「## 图之用」一节、其件俱在其表（以路或档名认）——缺即「图之用缺 <件>」；逐环⛔书一件者⛔索其节（无件可图）。"""
    表 = 图之用之表(文)
    if 表 is None:
        if not 所改之件(文):
            return []
        return ['无「## 图之用」一节（W%d 起·W9xx：逐环所改之件逐件书其部、谁跑、谁读、判——python3 工具/方案.py --图 W 自图机出其节）' % 图之用之起]
    名们 = set(表) | {os.path.basename(k) for k in 表}
    return ['图之用缺 %s（python3 工具/方案.py --图 W 重出其节）' % p for p in 所改之件(文) if p not in 名们 and os.path.basename(p) not in 名们]


def 图之析(root=ROOT):
    """→ (行之文, 件)：体系总图 之析（import 之·⛔另析·今树即算·⛔取远）。"""
    import 体系总图 as _图
    _, _, 件 = _图.生(root, 取=False)
    return _图.行之文, 件


def _图件(件, p):
    b = os.path.basename(p)
    if b in 件:
        return 件[b]
    return next((v for v in 件.values() if b in (v.get('员') or ())), None)


def _格(x):
    return str(x).replace('|', '｜').replace('\n', ' ').strip()


def 图之用之节(W, 文, 析=None):
    """→ 「## 图之用」之节（md 之行）：逐环所改之件逐件出 部、谁跑、谁读、判（体系总图之一件一行·全列⛔截）。析：(行之文, 件)（自测注之）。"""
    行文, 件 = 析 or 图之析()
    L = ['## 图之用', '', '> 由 `python3 工具/方案.py --图 %s` 自 体系总图 之析机出（今树即算·%s）；逐环所改之件逐件：部、谁跑、谁读、判。'
         '「谁读」与今析不合即 --验 ⚠（图已变·重出）。' % (W, time.strftime('%m-%d', time.gmtime())), '',
         '| 件 | 部 | 谁跑 | 谁读 | 判 |', '|---|---|---|---|---|']
    诸 = 所改之件(文)
    诸 += [k for k in (图之用之表(文) or {}) if re.search(r'\.(py|js|yml|json|md)$', k) and k not in 诸
           and os.path.basename(k) not in {os.path.basename(x) for x in 诸}]   # 旧表所列之余件（逐环未书其路者）亦重出
    for p in 诸:
        v = _图件(件, p)
        if v is None:
            L.append('| %s | — | （图中无此件：新立，入主後随图） | — | — |' % p)
            continue
        r = 行文(v, True)
        L.append('| %s | %s | %s | %s | %s |' % (p, _格(r[1]), _格(r[3]), _格(r[5]), _格(r[7])[:80]))
    return L


def _读者名(x):
    return re.sub(r'^(席|流|git钩)·', '', x)


def 图之用之警(文, 析=None):
    """→ [⚠]：表之「谁读」与今析不合（今析之读者不见於表、或表书读者而今析无）——只 ⚠（图已变·重出）。"""
    表 = 图之用之表(文) or {}
    if not 表:
        return []
    _, 件 = 析 or 图之析()
    警 = []
    for k, 行 in 表.items():
        v = _图件(件, k)
        if v is None:
            continue
        读 = 行.get('谁读', '')
        今 = sorted({_读者名(b) for _, b in v['读']})
        缺 = [x for x in 今 if x not in 读]
        if 缺:
            警.append('⚠ 图之用之谁读与今析不合：%s 今析之读者 %s 不在表（重出：python3 工具/方案.py --图 W）' % (k, '、'.join(缺[:6]) + ('等 %d' % len(缺) if len(缺) > 6 else '')))
        elif not 今 and 读 not in ('', '—', '-', '无'):
            警.append('⚠ 图之用之谁读与今析不合：%s 表书「%s」而今析无读者' % (k, 读[:30]))
    return 警


def 验(W, root=ROOT):
    p = os.path.join(root, 目录, '%s.md' % W)
    if not os.path.exists(p):
        return False, ['无方案：%s（先 `python3 工具/方案.py --模板 %s 题`，逐环确证了再开）' % (os.path.relpath(p, root), W)]
    文 = open(p, encoding='utf-8').read()
    坏 = 验文(文)
    if 要图(W):                         # 〔W912 环3〕居诸检之首（⛔与 W911 之缓存之算同处·免并之冲突）
        坏 += 图之用之坏(文)
    if _号(W) >= 坑之检之起:
        坏 += 坑之检之坏(文)
    if _号(W) >= 虫洞之择之起:
        坏 += 虫洞之择之坏(文)
    return not 坏, 坏


模板 = """# 方案·{W}·{题}

> 先设计、後实施（1009 作者令）：每一环都先确证它能做成——确证须引实据（费账之键、Run、试：命令及其果、自测 n/n、工具之档），⛔猜。
> 尚未确证者列入「未确证」并写其「试」；未确证有一条，即⛔开。

## 虫洞之择

- 候甲：（一法）——效：（…）；费：（…）；险：（…）；质：（…）
- 候乙：（另一法）——效：（…）；费：（…）；险：（…）；质：（…）
- 取：候（X）——由：（各方面何以最优：效最好、费最省、险最小、⛔伤书之质）

## 逐环

| 环 | 做什么 | 谁办 | 确证 | 时 | 费 | 败则 |
|---|---|---|---|---|---|---|
| 1 | （填） | 脚本：（器） | （实据） | （数 分） | $（数） | （败了怎么办） |

## 未确证

- （何事未确证）；试：（怎么小样实测）

## 合计

- 时：（数 分）；费：$（数）；据：（费账之键或试）

## 坑之检

- （逐坑写本法如何排除：`python3 工具/方法坑账.py --查`；凡改一把尺者，写「消费者：grep -rn '<函名>' 工具/ → 工具/…」）
"""


def 立模板(W, 题, root=ROOT):
    p = os.path.join(root, 目录, '%s.md' % W)
    if os.path.exists(p):
        print('⛔ 已在：%s（⛔覆）' % os.path.relpath(p, root)); return None
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(模板.format(W=W, 题=题))
    print('✓ 写 %s——逐环填实据；未确证者先试' % os.path.relpath(p, root))
    return p


def _图之自测(好):
    """〔W912 环3〕图之用之验之自测 → (过, 共)——自 自测 之首调之（其段⛔与他件之自测同处·免三方并之冲突）。"""
    ok = 共 = 0
    择 = '## 虫洞之择\n- 候甲：器自算——效：全；费：$0；险：低\n- 候乙：开席逐条——效：同；费：$12；质：同\n- 取：候甲——由：效同而费最省、险最小\n'
    # ★W912 环3（作者 1120「这不是每次都要用吗」）：W912 起之 W9xx 须「## 图之用」，逐环所改之件俱入其表（缺即坏）；W911 以下、W1xx 免；
    #   表之「谁读」与今析不合只 ⚠；--图 自体系总图之析机出（此注假析·⛔真生）；W912 本身合
    图文 = 好.replace('| 1 | 对拍 |', '| 1 | 改 工具/甲.py 与 设定/乙.json、工具/席/丙.js、.github/workflows/丁.yml（工具/<器>.py 占位⛔认） |')
    节图 = ('\n## 图之用\n| 件 | 部 | 谁跑 | 谁读 | 判 |\n|---|---|---|---|---|\n| 工具/甲.py | 长 | 全测·甲 | 引之者：乙器 | 用 |\n'
          '| 设定/乙.json | 长 | — | 引之者：甲 | 用 |\n| 丙.js | 心 | — | — | 用 |\n| `.github/workflows/丁.yml` | 觉 | GitHub | — | 用 |\n')
    检择 = '\n## 坑之检\n- ⑤ 等推用 推.py --等\n' + 择
    共 += 1; ok += 所改之件(图文) == ['工具/甲.py', '设定/乙.json', '工具/席/丙.js', '.github/workflows/丁.yml']   # 占位⛔认；表以路或档名认
    t3 = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(t3, 目录))
        w = lambda W, s: open(os.path.join(t3, 目录, W + '.md'), 'w', encoding='utf-8').write(s)
        w('W912', 图文 + 检择); w('W913', 图文 + 检择 + 节图.replace('| 设定/乙.json | 长 | — | 引之者：甲 | 用 |\n', ''))
        w('W914', 图文 + 检择 + 节图); w('W911', 图文 + 检择)
        w('W915', 好.replace('| 1 | 对拍 |', '| 1 | 兜底之令⛔改；巡.yml 之 cron 照旧（述之） |') + 检择)      # 逐环⛔书一件（全路）→ ⛔索其节（W911 自测之样即此式）
        g912, g913, g914, g911, g915 = (验(W, t3) for W in ('W912', 'W913', 'W914', 'W911', 'W915'))
    finally:
        shutil.rmtree(t3)
    共 += 1; ok += (g912[0] is False and any('无「## 图之用」' in x for x in g912[1]))                        # 缺节 → 坏
    共 += 1; ok += (g913[0] is False and g913[1] == ['图之用缺 设定/乙.json（python3 工具/方案.py --图 W 重出其节）'])   # 缺件 → 坏（唯缺者）
    共 += 1; ok += (g914[0] is True and g911[0] is True and not 要图('W911') and not 要图('W151') and not 要图('W1000') and 要图('W912'))   # 全 → 过；W911 以下、W1xx 免
    共 += 1; ok += (g915 == (True, []) and 所改之件(好) == [])                                           # 无件可图 → ⛔索其节（与 W911 之样并而⛔误坏）
    假件 = {'甲.py': {'读': {('引', '乙器'), ('引', '席·造章')}, '员': None}, '乙.json': {'读': set(), '员': None}}
    假行 = lambda v, 全=False: ['甲.py', '长', '职', '全测·甲', '每推', '引之者：乙器、席·造章', '—', '用（机判：有跑有读）', '工具/甲.py', '🟢〔—〕']
    出图 = 图之用之节('W914', 图文 + 节图, (假行, 假件))
    共 += 1; ok += ('| 工具/甲.py | 长 | 全测·甲 | 引之者：乙器、席·造章 | 用（机判：有跑有读） |' in 出图
                    and '| 工具/席/丙.js | — | （图中无此件：新立，入主後随图） | — | — |' in 出图 and 出图[0] == '## 图之用')
    警 = 图之用之警(图文 + 节图, (假行, 假件))
    共 += 1; ok += (len(警) == 2 and '工具/甲.py 今析之读者 造章 不在表' in 警[0] and '设定/乙.json 表书「引之者：甲」而今析无读者' in 警[1]
                    and 图之用之警(图文 + 节图.replace('引之者：乙器', '乙器、席·造章').replace('引之者：甲', '—'), (假行, 假件)) == [])   # 谁读不合只 ⚠
    共 += 1; ok += 验('W912')[0]                                                                        # W912 本身合（其图之用由 --图 机出）
    return ok, 共


def 自测():
    ok = 共 = 0
    好 = """# 方案·W9·测
## 逐环
| 环 | 做什么 | 谁办 | 确证 | 时 | 费 | 败则 |
|---|---|---|---|---|---|---|
| 1 | 对拍 | 脚本：工具/费审对拍.py | 试：python3 工具/费审对拍.py → 115 单位俱符，27 秒 | 1 分 | $0 | 不符即停，查明再续 |
| 2 | 五执笔 | 模型：创作，机器办不了 | 费账 wf_e7912fa3-a0c：执笔每席 $13—26 | 40 分 | $80 | 一席死即 resume |
## 未确证
- 无
## 合计
- 时：41 分；费：$80；据：费账 wf_e7912fa3-a0c
"""
    共 += 1; ok += (验文(好) == [])
    _过, _共 = _图之自测(好); ok += _过; 共 += _共                                                    # 〔W912 环3〕图之用
    共 += 1; ok += any('无实据' in x for x in 验文(好.replace('费账 wf_e7912fa3-a0c：执笔每席 $13—26', '大概能行')))      # 猜 → 红
    共 += 1; ok += any('谁办' in x for x in 验文(好.replace('模型：创作，机器办不了', '模型')))                     # 模型须写为何
    共 += 1; ok += any('败则' in x for x in 验文(好.replace('一席死即 resume', '—')))
    共 += 1; ok += any('$ 之数' in x for x in 验文(好.replace('| $80 |', '| 不知 |')))
    坏 = 验文(好.replace('- 无', '- 381 之料够否；试：python3 工具/章料.py 381'))
    共 += 1; ok += (any('尚有未确证' in x for x in 坏) and not any('无「试：」' in x for x in 坏))            # 有试仍⛔开
    共 += 1; ok += any('无「试：」' in x for x in 验文(好.replace('- 无', '- 381 之料够否')))
    t = tempfile.mkdtemp()
    try:
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            p = 立模板('W9', '测', t); q = 立模板('W9', '测', t)
        共 += 1; ok += (p is not None and q is None and 验('W9', t)[0] is False and 验('W8', t)[0] is False)     # 模板未填即红；无方案即红
    finally:
        shutil.rmtree(t)
    新 = 好.replace('# 方案·W9·测', '# 方案·W9·测（新法）', 1)
    共 += 1; ok += any('前定之验' in x for x in 验文(新))                       # 新法无前定之验即红
    新2 = 新 + '\n## 前定之验\n- 基线：W8 之实｜数：行家之分｜胜：≥+2｜不胜即退回旧法\n'
    共 += 1; ok += not any('前定之验' in x for x in 验文(新2))                  # 写足即过
    # ★1027（坑㉛㊱·#42）：W75 起之方案须「## 坑之检」；称改一把尺者须「消费者：grep …」且列其档；W74 以前免（史）
    t2 = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(t2, 目录))
        w = lambda W, s: open(os.path.join(t2, 目录, W + '.md'), 'w', encoding='utf-8').write(s)
        w('W74', 好); w('W75', 好)
        a74, a75 = 验('W74', t2), 验('W75', t2)
        检 = '\n## 坑之检\n- ⑤ 等推用 推.py --等；⑰ pipefail\n'
        w('W75', 好 + 检)
        b75 = 验('W75', t2)[0]
        尺 = 好.replace('| 1 | 对拍 |', '| 1 | 改取章之尺（章号之取） |')
        w('W76', 尺 + 检)
        c76 = 验('W76', t2)
        w('W76', 尺 + 检 + "- ㊱ 改尺：消费者：grep -rn '取章' 工具/ → 工具/封版.py、工具/段料.py\n")
        d76 = 验('W76', t2)[0]
        w('W77', 好.replace('| 1 | 对拍 |', '| 1 | 不改尺，只加一格 |') + 检)
        e77 = 验('W77', t2)[0]
    finally:
        shutil.rmtree(t2)
    共 += 1; ok += (a74[0] is True and a75[0] is False and any('坑之检' in x for x in a75[1]) and b75 is True)   # 回灌：W75 无坑之检即红；旧案免
    共 += 1; ok += (c76[0] is False and any('消费者' in x for x in c76[1]) and d76 is True and e77 is True)       # 改尺无消费者即红；「不改尺」⛔误拦
    print('方案·自测 %d/%d' % (ok, 共))
    择 = '## 虫洞之择\n- 候甲：器自算——效：全；费：$0；险：低\n- 候乙：开席逐条——效：同；费：$12；质：同\n- 取：候甲——由：效同而费最省、险最小\n'
    共 += 1; ok += (虫洞之择之坏(好 + 择) == [])                                                       # 二候、各比、取有由 → 过
    共 += 1; ok += any('无「## 虫洞之择」' in x for x in 虫洞之择之坏(好))                              # 无其节 → 红
    共 += 1; ok += any('只 1' in x for x in 虫洞之择之坏(好 + 择.replace('- 候乙：开席逐条——效：同；费：$12；质：同\n', '')))   # 只一候 → 红
    共 += 1; ok += any('无「- 取' in x for x in 虫洞之择之坏(好 + 择.replace('- 取：候甲——由：效同而费最省、险最小\n', '')))   # 无取 → 红
    共 += 1; ok += any('缺 费' in x for x in 虫洞之择之坏(好 + 择.replace('费：$12；', '')))                  # 候缺费之比 → 红
    共 += 1; ok += any('无其由' in x for x in 虫洞之择之坏(好 + 择.replace('——由：效同而费最省、险最小', '')))      # 取无由 → 红
    return ok == 共


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--自测']:
        sys.exit(0 if 自测() else 1)
    if a[:1] == ['--模板'] and len(a) == 3:
        sys.exit(0 if 立模板(a[1], a[2]) else 1)
    if a[:1] == ['--验'] and len(a) == 2:
        o, 坏 = 验(a[1])
        print('✓ 方案 %s：逐环俱有确证、时、费、败则；无未确证' % a[1] if o else '⛔ 方案 %s：\n  ' % a[1] + '\n  '.join(坏))
        if o and 要图(a[1]):                     # 〔W912 环3〕图之用之谁读与今析不合只 ⚠
            try:
                for x in 图之用之警(open(os.path.join(ROOT, 目录, a[1] + '.md'), encoding='utf-8').read()):
                    print('  ' + x)
            except Exception as e:
                print('  ⚠ 图之用之谁读未比（体系总图 之析不得：%s）' % str(e)[:80])
        sys.exit(0 if o else 1)
    if a[:1] == ['--图'] and len(a) == 2:        # 〔W912 环3〕印「## 图之用」之节（以供贴入）
        p = os.path.join(ROOT, 目录, a[1] + '.md')
        if not os.path.exists(p):
            print('⛔ 无方案：%s' % os.path.relpath(p, ROOT)); sys.exit(1)
        print('\n'.join(图之用之节(a[1], open(p, encoding='utf-8').read())))
        sys.exit(0)
    if a == ['--验全']:
        fs = sorted(glob.glob(os.path.join(ROOT, 目录, 'W*.md')))
        全坏, 析 = 0, None
        for f in fs:
            W = os.path.basename(f)[:-3]
            o, 坏 = 验(W)
            if not o:
                全坏 += 1; print('⛔ %s：%s' % (W, '；'.join(坏)[:300]))
            elif 要图(W):                        # 〔W912 环3〕图之用之谁读：只 ⚠（体系总图之析一回）
                try:
                    析 = 析 or 图之析()
                    for x in 图之用之警(open(f, encoding='utf-8').read(), 析):
                        print('⚠ %s：%s' % (W, x[2:]))
                except Exception as e:
                    print('⚠ %s：图之用之谁读未比（%s）' % (W, str(e)[:80]))
        print('方案：%d 份，不过 %d' % (len(fs), 全坏))
        sys.exit(0 if not 全坏 else 1)
    print(__doc__); sys.exit(2)
