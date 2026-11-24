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
  ## 坑之检          （1027 起·W75 起之方案须有：逐坑写本法如何排除——坑㉛㊱）
  - ⑤ 等推用 推.py --等；⑰ pipefail；㊱ 改尺：消费者：grep -rn '<函名>' 工具/ → 工具/甲.py、工具/乙.py
    凡称改一把尺（取章、取镜、取线、计数之法……）者，须有「消费者：grep …」一行并列其档（坑㊱：一义跨器而漏其消费者）。
  ## 虫洞之择      （W910 起：候 ≥2、各比效费险质、取有由；〔1120 W911 环2·坑61〕W913 起之 W9xx（W912 环7 起）：本节恰一行
                    「- 兜底之隔：不改」或「- 兜底之隔：改——缓存之算：每唤冷 $…、暖 $…；日 $…」（式定、器验：缺、二行、位误、带尾、缺价 → 坏；
                    「改」而本节他行⛔书「缓存」→ 坏）——兜底之隔＝总编辑之坐常态两唤之最大隔（缓存一时之档：逾一时即冷、每唤约十倍）。
                    其真另以二守兜之：自测之跨器之钉（独算 接棒守.兜底之令 常态之隔 <60）、接棒守 --巡 之冷唤之察。旧之以正则猜文已删）
  ## 预审          （〔1120 W911 环6·坑65〕W913 起之 W9xx（W912 环7 起）：施前独立之攻——预审者 Run（费账之键·名「W·预审」·席 ≥2）、
                    审之指、逐险「- 险（环N｜取）：…｜防：…」（覆盖模型之环、改 工具/、.github/、设定/ 之环与取；防带锚；⛔未防）、判；
                    --开 深验其 Run 之档（本机），--裁 复验（开後改环者亦验）。序：方案 → 预审 Run → 费审 --记 → 本节 → --开 → 施）

用法：
  python3 工具/方案.py --模板 W19 题      # 写 设定/方案/W19.md 之模板（已在则⛔覆）
  python3 工具/方案.py --验 W19           # 验一份；不过 rc=1
  python3 工具/方案.py --验全             # 验 设定/方案/ 下诸份（入全测）
  python3 工具/方案.py --预审之指 W913     # 印审之指（「## 预审」之「- 审之指：」书之）
  python3 工具/方案.py --预审 W913 <Run>   # 印「## 预审」之稿：自其 Run 之 result 机出险行（施者填环与防、书判）
  python3 工具/方案.py --自测
工作流账 `--开 W` 先验 设定/方案/W.md（守新律者另深验其预审之 Run）——不过即拒开；`--裁 W`（W9xx 守新律者）复验之。
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import os, sys, re, glob, json, time, tempfile, shutil

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


# ── 〔1120 W911 重造 环2·环6〕新律：兜底之隔之声明、施前之预审（坑61 复踩·坑65）──
#   旧之「缓存之算」以正则猜自由之文（言改唤隔否）——三回补正则（wf_7d40b1f3-558、wf_b5d6ff53-915、wf_89eac13d-6ad）俱以一漏换一误，已删：
#   自由之文⛔可机猜。今：方案自书一行之声明（式定、器验其式），其真另以二守兜之——①本器自测之跨器之钉（独算 接棒守.兜底之令 常态之隔 <60·
#   钉与表⛔同器：改之须动二器）；②接棒守 --巡 之冷唤之察（转录之尾：隔逾一时而缓存读≈0 即印「本唤冷」）；并施前之预审（攻者 ≥2·Run 可验）。
新律之起 = 913
新律之续 = {'W912': 7}     # 号 <913 而本律入主後续增其环者：其逐环有环号 ≥ 此者即照新律（W912 二轮·环7—9）；W1xx 恒免


def 总编辑之件(W, 起):
    """新律之界（与 W912「要图」共一判·坑53：要图(W) ≡ 总编辑之件(W, 图之用之起)）：W9xx（总编辑之件）且号 ≥ 起。
    写书之件 W1xx、W1000 起恒免（⛔拖累写书）；号非 W\\d+（W913b、w913）→ False——工作流账 --开 另拒其新件（⛔以怪号逃律）。"""
    return re.fullmatch(r'W9\d\d', str(W)) is not None and _号(W) >= 起


def _环们(文):
    """逐环之数据行 → [(环号 int｜None, 谁办, 做什么, 败则)]（表头、分隔、栏数不合者⛔入）。"""
    出 = []
    for l in (节(文, '逐环') or '').split('\n'):
        l = l.strip()
        if not l.startswith('|') or re.fullmatch(r'\|[\s\-:|]+\|', l):
            continue
        c = [x.strip() for x in l.strip('|').split('|')]
        if len(c) != len(列) or c == 列:
            continue
        m = re.match(r'\d+', c[0])
        出.append((int(m.group(0)) if m else None, c[2], c[1], c[6]))
    return 出


def 守新律(W, 文):
    """W 之方案须守新律（声明、预审）否：总编辑之件(W, 新律之起)；或 新律之续 所列之件而其逐环有续增之环（W912 环7 起）。"""
    if 总编辑之件(W, 新律之起):
        return True
    起环 = 新律之续.get(str(W))
    return 起环 is not None and any(n is not None and n >= 起环 for n, _, _, _ in _环们(文))


def _行与节(文):
    """→ [(节名, 行)]：去代码块（``` 之间）与引文（> 起）之行；节名取所在「## 」之头（档首 ''）。"""
    出, 名, 码 = [], '', False
    for l in 文.split('\n'):
        s = l.strip()
        if s.startswith('```'):
            码 = not 码
            continue
        if 码 or s.startswith('>'):
            continue
        if l.startswith('## '):
            名 = l[3:].strip()
            continue
        出.append((名, s))
    return 出


# 兜底之隔＝总编辑之坐常态（非暂停）两唤之最大隔（接棒守.兜底之隔分·今 30）。属「改」者：改 接棒守.兜底之令 之表（号、cron、开否）、
#   update_trigger／create_trigger／delete_trigger 之令、暂停解停之序（暂停令.守书之诸参）、降级复常之令（兜底之改 之出）、所唤之会话；
#   ⛔属：云巡之 唤之隔分（同局二十分一唤之节流·别义）、降级之二十分及其持续（降级之隔短於常态）。名⛔用「唤之隔」（与 唤之隔分 撞）。
声明式 = re.compile(r'(?:-\s*)?兜底之隔\s*[:：]\s*(?:不改|改——缓存之算：(?P<算>.+?))\s*。?')
_声明候 = re.compile(r'^(?:-\s*)?(兜底之隔|唤之隔)\s*[:：]')


def 兜底之隔之坏(文):
    """→ [坏]（W911 环2）：全档（去代码块、引文）恰一行「- 兜底之隔：不改」或「- 兜底之隔：改——缓存之算：每唤冷 $…、暖 $…；日 $…」，
    居「## 虫洞之择」（与候、取同节）；行首许「- 」、冒号全半角俱认；值以 fullmatch 判（「不改」⛔带尾——尾可藏改；先判「不改」）；
    「改」须同行各书冷、暖、日之 $ 数（三数异处·一数⛔充二），且虫洞之择（去此行）须书「缓存」——所取之候之费须用冷价，交预审。"""
    诸 = [(n, s) for n, s in _行与节(文) if _声明候.match(s)]
    旧 = [s for _, s in 诸 if _声明候.match(s).group(1) == '唤之隔']
    if 旧:
        return ['声明之名已改：「%s」→「兜底之隔」（唤之隔分＝20 係云巡之节流·别义）' % 旧[0][:30]]
    if not 诸:
        return ['缺兜底之隔之声明：「## 虫洞之择」须恰一行「- 兜底之隔：不改」或「- 兜底之隔：改——缓存之算：每唤冷 $…、暖 $…；日 $…」'
                '（引文、代码块、表中之字⛔算）']
    if len(诸) > 1:
        return ['兜底之隔之声明 %d 行（须恰一行）：%s' % (len(诸), '／'.join(s[:24] for _, s in 诸))]
    n, s = 诸[0]
    if not n.startswith('虫洞之择'):
        return ['兜底之隔之声明位误：在「## %s」，须在「## 虫洞之择」（与候、取同节）' % (n or '（档首）')]
    m = 声明式.fullmatch(s)
    if not m:
        return ['兜底之隔之声明式不合：「%s」——「不改」⛔带尾；改则「改——缓存之算：每唤冷 $…、暖 $…；日 $…」' % s[:40]]
    if m.group('算') is None:
        return []
    算 = m.group('算')
    位 = {k: {x.start(1) for x in re.finditer(k + r'[^；;|｜冷暖]{0,12}?(\$)\s*\d', 算)} for k in ('冷', '暖', '日')}
    坏 = []
    if not any(len({a, b, c}) == 3 for a in 位['冷'] for b in 位['暖'] for c in 位['日']):
        缺 = [k for k in ('冷', '暖', '日') if not 位[k]]
        坏.append('兜底之隔「改」之缓存之算须同行各书 每唤冷 $…、暖 $…、日 $…（三数异处）%s——只算暖价即坑61'
                 % ('：缺 %s' % '、'.join(缺) if 缺 else ''))
    if '缓存' not in '\n'.join(x for nn, x in _行与节(文) if nn.startswith('虫洞之择') and x != s):
        坏.append('兜底之隔「改」而虫洞之择（去声明之行）⛔书「缓存」——候与取须算缓存之冷暖（坑61）')
    return 坏


def _cron之刻(c):
    """cron 之分、时二栏 → 一日之刻（分）之集（*、*/n、a-b、a-b/n、a,b）——独写（⛔借 接棒守 之 兜底之分／自测之算：钉与表⛔同器）。"""
    def 栏(f, 顶):
        诸 = set()
        for p in f.split(','):
            基, _, 步 = p.partition('/')
            if 基 == '*':
                lo, hi = 0, 顶 - 1
            elif '-' in 基:
                lo, hi = (int(x) for x in 基.split('-'))
            else:
                lo = int(基)
                hi = 顶 - 1 if 步 else lo
            诸.update(range(lo, hi + 1, int(步 or 1)))
        return 诸
    分, 时 = c.split()[:2]
    return {h * 60 + m for h in 栏(时, 24) for m in 栏(分, 60)}


def 常态之隔(令):
    """令：(名, 号, 常之 cron, 降之 cron, 常开否) 之表 → (常态两唤之最大隔〔分·跨日〕, 一日之刻数)；无常开者 → (1440, 0)。"""
    日 = [False] * 1440
    for _, _, 常, _, 开 in 令:
        if 开:
            for t in _cron之刻(常):
                日[t] = True
    刻 = [i for i, x in enumerate(日) if x]
    if not 刻:
        return 1440, 0
    return max((刻[(i + 1) % len(刻)] - 刻[i]) % 1440 or 1440 for i in range(len(刻))), len(刻)


# 预审（W911 环6·坑65「方案之核心之断未经预审即施工」）：W913 起之总编辑之件，方案须「## 预审」一节——
#   - 预审者：wf_…（或 子席:agent-…；可数键·席名⛔算）      - 审之指：<八位>（`--预审之指 W`：取行、兜底之隔之声明与逐环之 做什么／败则 之 sha1）
#   - 险（环N｜取）：<险>｜防：<防>（逐险一行·`--预审 W <Run>` 自 Run 之 result 机出险文，施者只填环与防）      - 判：可施｜判：须改→已改 环N
#   险须点环号或「取」（「* 险」「- 风险」之行亦认·式不合即坏）；凡「模型」之环、做什么书 工具/、.github/、设定/ 之环、与「取」各须一险点之（覆盖）；
#   防须实（以 无／未／尚未／待／⛔防／todo／不及 起即空；⛔—／略／後补／暂缓／不防）且带锚：
#   工具/…、自测、格：、「环N 改…」或「驳：<由>」；「未防」唯居防段之首（或一行之首）方作未防；二判相违即坏。浅验（--验·GitHub 可跑）：预审者之键在 设定/费账.json、
#   名以「W·预审」起、席之和 ≥2；深验（--开·本机）：其 Run 之档 completed、脚本含本方案之路、起时早於开、result 有险、Run 出险之数 ≤ 节之险行、攻者判「须改」则节判⛔「可施」。
#   深验以脚本含「方案/W.md」判所审——预审之 Run 须书其方案之路於提示；通用之脚本以 args 拼路者，须於提示另书其路（全文）。
#   序（唯一）：方案 → 预审 Run（args: {W, 预审: true}·续跑之守⑤许之）→ `费审.py --记 <Run> "W·预审"` → `--预审 W <Run>` 补节、填防 → --开 → 施；
#   开後改其核心（审之指异）→ --验 即坏、工作流账 --裁 拒——复审（新 Run）而後更其指。误红则修其式，⛔降（⛔退为只验节在）。
_键式 = r'wf_[0-9a-f]{8}-[0-9a-f]{3}|子席:agent-[0-9a-f]+(?:\.jsonl)?'
_险式 = re.compile(r'^-\s*险\s*[（(]([^）)\n]*)[）)]\s*[:：]\s*(.*)$')
_点式 = re.compile(r'\s*(?:(?:环\s*\d+[①-⑳]*|取)\s*(?:[、,，/／]\s*|$))+')
_防分 = re.compile(r'[｜|]\s*防\s*[:：]')
_防空 = re.compile(r'^(?:(?:—+|-+|－+|略)\s*[。.]?$|无|未|尚未|待|後补|后补|暂缓|不防|不及|⛔\s*防|(?i:todo))')   # 以否定之辞起即空（「无自测」「尚未防」⛔借锚）
_防锚 = re.compile(r'工具/\S|自测|格\s*[:：]|环\s*\d+[①-⑳]*\s*改|驳\s*[:：]\s*\S{4,}')
_判式 = re.compile(r'-\s*判\s*[:：]\s*(?:可施|须改\s*(?:→|->)\s*已改\s*((?:环\s*\d+[①-⑳]*\s*[、,，]?\s*)+))\s*。?')


def 预审之指(文):
    """→ 方案之核心之指（sha1 前八位）：虫洞之择之「- 取」行与兜底之隔之声明行、逐环之 环｜做什么｜败则——预审之後改之即异（须复审）。"""
    import hashlib
    取 = [s for n, s in _行与节(文) if n.startswith('虫洞之择') and (re.match(r'-\s*取\s*[:：]', s) or _声明候.match(s))]
    环 = ['%s｜%s｜%s' % (n, 做, 败) for n, _, 做, 败 in _环们(文)]
    return hashlib.sha1('\n'.join(取 + 环).encode('utf-8')).hexdigest()[:8]


def _预审者(文):
    m = re.search(r'^-\s*预审者\s*[:：](.*)$', 节(文, '预审') or '', re.M)
    return (m.group(1), re.findall(_键式, m.group(1))) if m else ('', [])


def 预审之式之坏(文):
    """→ [坏]：「## 预审」之式（见上）——缺节、无 Run、险之行式、防之空与锚、未防、覆盖、判、审之指。⛔读费账（浅验见 预审之账之坏）。"""
    节文 = 节(文, '预审')
    if 节文 is None or not 节文.strip():
        return ['无「## 预审」一节（W%d 起·坑65：方案 → 预审 Run〔args: {W, 预审: true}·攻者 ≥2〕→ 费审 --记 <Run> "W·预审" → 本节 → --开）' % 新律之起]
    坏 = []
    if not _预审者(文)[1]:
        坏.append('预审无 Run：须「- 预审者：wf_…」（费账之键·或 子席:agent-…；席名⛔算）')
    环表 = _环们(文)
    有环 = {n for n, _, _, _ in 环表 if n is not None}
    险数, 所点 = 0, set()
    for l in (x.strip() for x in 节文.split('\n')):
        if not l.startswith(('-', '*')):
            continue
        体 = re.sub(r'^[-*]\s*', '', l)
        if 体.startswith('未防'):
            坏.append('预审有未防：「%s」——未防即⛔开' % 体[:30])
            continue
        if not 体.startswith(('险', '风险')):             # 「* 险」「- 风险」亦认作险行——式不合即坏（⛔静过）
            continue
        m = _险式.match(l)
        if not m or not _点式.fullmatch(m.group(1)):
            坏.append('险之行式不合：「%s」——须「- 险（环N｜取）：…｜防：…」（险须点环号或「取」）' % 体[:30])
            continue
        点 = {('环%s' % x) if x else '取' for x in re.findall(r'环\s*(\d+)|取', m.group(1))}
        for x in sorted(点 - {'取'} - {'环%d' % n for n in 有环}):
            坏.append('险点 %s 而逐环无之：「%s」' % (x, 体[:30]))
        d = _防分.search(m.group(2))
        if not d:
            坏.append('险之行缺「｜防：」：「%s」' % 体[:30])
            continue
        险文, 防 = m.group(2)[:d.start()].strip(), m.group(2)[d.end():].strip()
        if not 险文:
            坏.append('险之行无险文：「%s」' % 体[:30])
        if 防.startswith('未防'):
            坏.append('预审有未防：「%s」——未防即⛔开' % 体[:30])
        elif not 防 or _防空.match(防):
            坏.append('防空：「%s」——防须实（⛔以 无／未／尚未／待／⛔防／todo／不及 起，⛔—／略／後补／暂缓／不防）' % 体[:30])
        elif not _防锚.search(防):
            坏.append('防无锚：「%s」——须点 工具/…、自测、格：、「环N 改…」或「驳：<由>」' % 体[:30])
        险数 += 1
        所点 |= 点
    if not 险数:
        坏.append('预审无一险之行（「- 险（环N｜取）：…｜防：…」）——书而未攻⛔算预审')
    须 = {'环%d' % n for n, 谁, 做, _ in 环表 if n is not None and (谁.startswith('模型') or any(p in 做 for p in ('工具/', '.github/', '设定/')))} | {'取'}
    未 = sorted(须 - 所点, key=lambda x: (x == '取', int(x[1:]) if x != '取' else 0))
    if 险数 and 未:
        坏.append('预审未攻：%s（凡「模型」之环、做什么书 工具/、.github/、设定/ 之环与「取」须各有一险点之）' % '、'.join(未))
    判们 = [l.strip() for l in 节文.split('\n') if re.match(r'\s*-\s*判\s*[:：]', l)]
    if not 判们:
        坏.append('预审无「- 判：可施」或「- 判：须改→已改 环N」')
    种 = set()
    for l in 判们:
        m = _判式.fullmatch(l)
        if not m:
            坏.append('判之式不合：「%s」——「判：可施」或「判：须改→已改 环N」' % l[:30])
        else:
            种.add(m.group(1) is None)
            for x in re.findall(r'环\s*(\d+)', m.group(1) or ''):
                if int(x) not in 有环:
                    坏.append('判点 环%s 而逐环无之' % x)
    if len(种) > 1:
        坏.append('二判相违：「可施」与「须改→已改」并书——判唯一')
    指 = re.search(r'^-\s*审之指\s*[:：]\s*([0-9a-f]{8})\b', 节文, re.M)
    今指 = 预审之指(文)
    if not 指:
        坏.append('预审缺「- 审之指：%s」（python3 工具/方案.py --预审之指 W）' % 今指)
    elif 指.group(1) != 今指:
        坏.append('方案之核心（取、兜底之隔之声明、逐环之做什么／败则）改於预审之後（审之指 %s ≠ 今 %s）——复审（新 Run）而後更其指' % (指.group(1), 今指))
    return 坏


def 预审之账之坏(文, W, root=ROOT):
    """→ [坏]（浅验·GitHub 可跑）：预审者之诸键俱在 设定/费账.json、其名以「W·预审」起（他件之 Run ⛔借）、席之和 ≥2（二攻者）。"""
    _, 键们 = _预审者(文)
    if not 键们:
        return []                      # 无 Run 之坏由 预审之式之坏 出
    try:
        表 = {r.get('键'): r for r in json.load(open(os.path.join(root, '设定', '费账.json'), encoding='utf-8'))['行']}
    except Exception as e:
        return ['费账读不出（%s）——预审之 Run 无从验' % e]
    坏, 席 = [], 0
    for k in 键们:
        r = 表.get(k) or 表.get(k + '.jsonl')
        if r is None:
            坏.append('预审之 Run %s 不在费账——先 `python3 工具/费审.py --记 %s "%s·预审"`' % (k, k, W))
            continue
        if not str(r.get('名', '')).startswith('%s·预审' % W):
            坏.append('预审之 Run %s 之费账名「%s」非「%s·预审」起（他件之 Run ⛔借）' % (k, r.get('名'), W))
        席 += int(r.get('席') or 0)
    if not 坏 and 席 < 2:
        坏.append('预审之席 %d（须 ≥2：二攻者各攻）' % 席)
    return 坏


def _诸Run之根():
    return os.environ.get('ZM_WORKFLOWS_ROOT') or os.path.expanduser('~/.claude/projects')   # 环境之注只供自测


def _险判(x, 险们=None, 判们=None):
    """Run 之 result → ([诸险之 risk], [攻者之 verdict 之文])——预审之稿 与 深验 共用（坑53）。"""
    险们, 判们 = ([] if 险们 is None else 险们), ([] if 判们 is None else 判们)
    if isinstance(x, dict):
        if 'risk' in x:
            险们.append(x['risk'])
        if isinstance(x.get('verdict'), str):
            判们.append(x['verdict'])
        for v in x.values():
            _险判(v, 险们, 判们)
    elif isinstance(x, list):
        for v in x:
            _险判(v, 险们, 判们)
    return 险们, 判们


def _Run之档(k, 根=None):
    根 = 根 or _诸Run之根()
    if k.startswith('wf_'):
        fs = glob.glob(os.path.join(根, '*', '*', 'workflows', k + '.json')) + glob.glob(os.path.join(根, '*', 'workflows', k + '.json'))
    else:
        名 = k.split(':', 1)[1]
        fs = glob.glob(os.path.join(根, '*', '*', 'subagents', 名 if 名.endswith('.jsonl') else 名 + '.jsonl'))
    return fs[0] if fs else None


def 预审之深验(W, root=ROOT, 今=None):
    """→ (坏, 警)（工作流账 --开 所调·本机）：预审者之诸键，其 Run 之档（~/.claude/projects/*/*/workflows/<Run>.json；子席则 subagents/<agent>.jsonl）
    俱在——wf_：status＝completed、脚本（script 或 scriptPath）含「方案/W.md」、startTime 早於开、result 有险（risk·空或他式即坏）、
    诸 Run 出险之数 ≤ 节之险行、攻者之判（verdict）含「须改」则节之判⛔「可施」；
    子席：转录含「方案/W.md」、首时早於开。读不得 → 坏（拒开）。预审者之行书「云坐」者（Run 不在本机）→ 只浅验、印 ⚠。"""
    文 = open(os.path.join(root, 目录, '%s.md' % W), encoding='utf-8').read()
    原, 键们 = _预审者(文)
    if not 键们:
        return ['预审无 Run'], []
    if '云坐' in 原:
        return [], ['⚠ %s 之预审书「云坐」（本机无其 Run 之档）——只浅验（费账之键、名、席）' % W]
    今秒 = 今.timestamp() if 今 else time.time()
    路名 = '方案/%s.md' % W
    节文 = 节(文, '预审') or ''
    节险 = sum(1 for l in 节文.split('\n') if _险式.match(l.strip()))
    坏, 险, 须改 = [], 0, False
    for k in 键们:
        p = _Run之档(k)
        if not p:
            坏.append('预审之 Run %s 之档本机不在——拒开（云坐跑者於预审者之行书「云坐」·只浅验）' % k)
            continue
        try:
            if k.startswith('wf_'):
                d = json.load(open(p, encoding='utf-8'))
                sc = str(d.get('script') or '')
                if not sc and d.get('scriptPath'):
                    sc = open(d['scriptPath'], encoding='utf-8').read()
                起 = (d.get('startTime') or 0) / 1000
                if d.get('status') != 'completed':
                    坏.append('预审之 Run %s 之状「%s」非 completed' % (k, d.get('status')))
                险们, 判们 = _险判(d.get('result'))
                if not 险们:
                    坏.append('预审之 Run %s 之 result 无险（空、或非 {risk} 之式）——攻者之险须可机读' % k)
                险 += len(险们)
                须改 = 须改 or any(re.search(r'(?<![无不毋])须改', v) for v in 判们)
            else:
                with open(p, encoding='utf-8', errors='replace') as f:
                    sc = f.read(64 * 1024 * 1024)
                m = re.search(r'"timestamp"\s*:\s*"([^"]+)"', sc)
                import datetime as _d
                起 = _d.datetime.fromisoformat(m.group(1).replace('Z', '+00:00')).timestamp() if m else 0
        except Exception as e:
            坏.append('预审之 Run %s 之档读不出（%s）' % (k, str(e)[:60]))
            continue
        if 路名 not in sc:
            坏.append('预审之 Run %s 之脚本／转录⛔含 设定/%s（所审非此方案）' % (k, 路名))
        if not 起 or 起 >= 今秒:
            坏.append('预审之 Run %s 之起时不早於开' % k)
    if 险 > 节险:
        坏.append('预审之 Run 出险 %d 而本节只 %d 行——攻者之险须俱入节（python3 工具/方案.py --预审 %s <Run> 机出其行）' % (险, 节险, W))
    if 须改 and re.search(r'^\s*-\s*判\s*[:：]\s*可施', 节文, re.M):
        坏.append('攻者判「须改」而本节之判「可施」——须「判：须改→已改 环N」（⛔匿攻者之判）')
    return 坏, []


def 预审之稿(W, k, root=ROOT):
    """→ 「## 预审」之稿（行）：自 Run 之 result 机出诸险（risk）与攻者之判（verdict）——施者只填环与防、书判（未填之行 --验 即坏）。"""
    p = _Run之档(k)
    if not p or not k.startswith('wf_'):
        raise ValueError('Run %s 之档本机不在（或非 wf_）' % k)
    d = json.load(open(p, encoding='utf-8'))
    险们, 判们 = _险判(d.get('result'))
    险们 = [re.sub(r'\s+', ' ', str(r)).replace('｜', '／').replace('|', '／') for r in 险们]
    判们 = [re.sub(r'\s+', ' ', v)[:80] for v in 判们]
    文 = open(os.path.join(root, 目录, '%s.md' % W), encoding='utf-8').read()
    return (['## 预审', '', '- 预审者：%s（攻者 %d·席之和见费账）' % (k, d.get('agentCount') or 0), '- 审之指：%s' % 预审之指(文)]
            + ['- 险（环?）：%s｜防：（填：工具/…、自测、格：、「环N 改…」或「驳：<由>」）' % r for r in 险们]
            + ['- 判：（攻者之判：%s——填「可施」或「须改→已改 环N」）' % '；'.join(判们)])


def 开前之验(W, root=ROOT, 今=None):
    """工作流账 --开 所调 → (过否, 坏, 警)：验(W)；守新律之件加 预审之深验（本机读其 Run 之档）。"""
    o, 坏 = 验(W, root)
    if not o:
        return False, 坏, []
    文 = open(os.path.join(root, 目录, '%s.md' % W), encoding='utf-8').read()
    if not 守新律(W, 文):
        return True, [], []
    深, 警 = 预审之深验(W, root, 今)
    return not 深, 深, 警


def _号(W):
    m = re.fullmatch(r'W(\d+)', str(W))
    return int(m.group(1)) if m else 0


def 验(W, root=ROOT):
    p = os.path.join(root, 目录, '%s.md' % W)
    if not os.path.exists(p):
        return False, ['无方案：%s（先 `python3 工具/方案.py --模板 %s 题`，逐环确证了再开）' % (os.path.relpath(p, root), W)]
    文 = open(p, encoding='utf-8').read()
    坏 = 验文(文)
    if re.fullmatch(r'W0\d+', str(W)):                # 〔W911 补〕前导零（W0913）：新律以号定界、总编辑之件 判 False 即逃律——⛔免，验即坏（--开 随之拒）
        坏.append('号「%s」带前导零（W0913 之类即逃新律之界）——去其零再立方案' % W)
    if _号(W) >= 坑之检之起:
        坏 += 坑之检之坏(文)
    if _号(W) >= 虫洞之择之起:
        坏 += 虫洞之择之坏(文)
    if 守新律(W, 文):                    # 〔W911 环2·环6〕W913 起之总编辑之件（W912 环7 起）：声明与预审（浅验·费账）
        坏 += 兜底之隔之坏(文) + 预审之式之坏(文) + 预审之账之坏(文, W, root)
    return not 坏, 坏


模板 = """# 方案·{W}·{题}

> 先设计、後实施（1009 作者令）：每一环都先确证它能做成——确证须引实据（费账之键、Run、试：命令及其果、自测 n/n、工具之档），⛔猜。
> 尚未确证者列入「未确证」并写其「试」；未确证有一条，即⛔开。

## 虫洞之择

- 候甲：（一法）——效：（…）；费：（…）；险：（…）；质：（…）
- 候乙：（另一法）——效：（…）；费：（…）；险：（…）；质：（…）
- 取：候（X）——由：（各方面何以最优：效最好、费最省、险最小、⛔伤书之质）
- 兜底之隔：（W913 起之 W9xx 必书一行，二择一：「不改」〔⛔带尾〕｜「改——缓存之算：每唤冷 $…、暖 $…；日 $…」〔改兜底之令之表、*_trigger 之令、暂停解停或降级复常之令、所唤之会话者〕）

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

## 预审

> W913 起之 W9xx（坑65）：开前之序——本方案成 → 预审 Run（args: {{W: "{W}", 预审: true}}·攻者 ≥2·只读）→ `python3 工具/费审.py --记 <Run> "{W}·预审"`
> → `python3 工具/方案.py --预审 {W} <Run>` 机出险行、逐险填环与防、书判 → `python3 工具/工作流账.py --开 {W} …`（深验其 Run 之档）→ 施。开後改取、兜底之隔或逐环即须复审。
> 预审之 Run 须书本方案之路（设定/方案/{W}.md）於提示——深验以其脚本含此路判之；通用之脚本以 args 拼路者，须於提示另书其路（全文），否则拒开。
- 预审者：（wf_…）
- 审之指：（python3 工具/方案.py --预审之指 {W}）
- 险（环N｜取）：（攻者之险）｜防：（工具/…、自测、格：、「环N 改…」或「驳：<由>」）
- 判：（可施｜须改→已改 环N）
"""


def 立模板(W, 题, root=ROOT):
    p = os.path.join(root, 目录, '%s.md' % W)
    if os.path.exists(p):
        print('⛔ 已在：%s（⛔覆）' % os.path.relpath(p, root)); return None
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(模板.format(W=W, 题=题))
    print('✓ 写 %s——逐环填实据；未确证者先试' % os.path.relpath(p, root))
    return p


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
    择 = '## 虫洞之择\n- 候甲：器自算——效：全；费：$0；险：低\n- 候乙：开席逐条——效：同；费：$12；质：同\n- 取：候甲——由：效同而费最省、险最小\n'
    共 += 1; ok += (虫洞之择之坏(好 + 择) == [])                                                       # 二候、各比、取有由 → 过
    共 += 1; ok += any('无「## 虫洞之择」' in x for x in 虫洞之择之坏(好))                              # 无其节 → 红
    共 += 1; ok += any('只 1' in x for x in 虫洞之择之坏(好 + 择.replace('- 候乙：开席逐条——效：同；费：$12；质：同\n', '')))   # 只一候 → 红
    共 += 1; ok += any('无「- 取' in x for x in 虫洞之择之坏(好 + 择.replace('- 取：候甲——由：效同而费最省、险最小\n', '')))   # 无取 → 红
    共 += 1; ok += any('缺 费' in x for x in 虫洞之择之坏(好 + 择.replace('费：$12；', '')))                  # 候缺费之比 → 红
    共 += 1; ok += any('无其由' in x for x in 虫洞之择之坏(好 + 择.replace('——由：效同而费最省、险最小', '')))      # 取无由 → 红
    # ★1120 W911 重造 环2·环6（坑61 复踩·坑65）：旧「缓存之算」之正则（以文猜改唤隔）已删——改为自书之声明（兜底之隔）与施前之预审。
    #   钉逐一直测本律之函（⛔断 验()[0] is True 於 W≥913：W912「图之用」之律入主则其案须兼备——故 W913 之正例兼书「## 图之用」之节）。
    新钉 = []

    def 钉(名, f):
        try:
            v = bool(f())
        except Exception as e:
            v, 名 = False, 名 + '（崩：%s）' % str(e)[:80]
        新钉.append((名, v))
    图节 = '\n## 图之用\n| 件 | 部 | 谁跑 | 谁读 | 判 |\n|---|---|---|---|---|\n'
    声 = '- 兜底之隔：不改\n'
    改声 = '- 兜底之隔：改——缓存之算：每唤冷 $3.3、暖 $0.27；日约 $26\n'
    冷择 = 择.replace('费：$12；', '费：缓存一时之档·隔逾一时即冷 $12；')                      # 候书缓存之冷暖（改者须）
    底 = lambda W='W9', 声行=声, 择文=择: 好.replace('# 方案·W9·测', '# 方案·%s·测' % W) + 检 + 择文 + 声行     # 好＋坑之检＋虫洞之择（末行声明）
    审 = lambda 文, 险们=('- 险（环2）：五执笔之费估低｜防：自测 3/3 钉其界', '- 险（取）：候甲之费未算冷唤｜防：驳：候甲⛔改唤隔，冷暖同档'), \
        者='wf_0000aaaa-001', 判='- 判：可施', 指=None: (
        '\n## 预审\n- 预审者：%s（攻者二）\n- 审之指：%s\n%s\n%s\n' % (者, 指 or 预审之指(文), '\n'.join(险们), 判))
    全 = lambda W='W913', **k: 底(W) + 审(底(W), **k) + 图节
    隔坏 = lambda 文: 兜底之隔之坏(文)
    有 = lambda 坏, 字: any(字 in x for x in 坏)
    # 一、声明之式（预审·声明之律 险1—3 之①—⑩）
    钉('声明·缺行 → 坏', lambda: 有(隔坏(底(声行='')), '缺兜底之隔之声明'))
    钉('声明·「- 兜底之隔：不改」→ 过', lambda: 隔坏(底()) == [])
    钉('声明·半角冒号、无「- 」→ 过', lambda: 隔坏(底(声行='兜底之隔: 不改\n')) == [])
    钉('声明·「不改」带尾（尾可藏改）→ 坏', lambda: 有(隔坏(底(声行='- 兜底之隔：不改（兜底之令改每三时）\n')), '式不合'))
    钉('声明·二行相反 → 坏', lambda: 有(隔坏(底(声行=声 + '- 兜底之隔：改——缓存之算：无\n')), '2 行'))
    钉('声明·只在引文 → 缺', lambda: 有(隔坏(底(声行='> 兜底之隔：不改｜改——…\n')), '缺兜底之隔之声明'))
    钉('声明·只在代码块 → 缺', lambda: 有(隔坏(底(声行='```\n- 兜底之隔：不改\n```\n')), '缺兜底之隔之声明'))
    钉('声明·只在逐环之格 → 缺', lambda: 有(隔坏(底(声行='').replace('| 1 | 对拍 |', '| 1 | 对拍（兜底之隔：不改） |')), '缺兜底之隔之声明'))
    钉('声明·置於「## 未确证」→ 坏而明言位误', lambda: 有(隔坏(底(声行='').replace('## 未确证\n- 无', '## 未确证\n- 无\n- 兜底之隔：不改')), '位误'))
    钉('声明·旧名「唤之隔」（与 唤之隔分＝20 撞）→ 坏', lambda: 有(隔坏(底(声行='- 唤之隔：不改\n')), '名已改'))
    钉('声明·模板之占位 → 坏（⛔以不改为默）', lambda: 有(隔坏(模板.format(W='W913', 题='测')), '式不合'))
    # 二、「改」之枝（险2：同行各书冷、暖、日之 $ 数；虫洞之择去此行须书缓存——留旧钉②）
    钉('改·冷暖日俱书、候书缓存 → 过', lambda: 隔坏(底(声行=改声, 择文=冷择)) == [])
    钉('改·「缓存之算：冷暖俱算」无价 → 坏', lambda: 有(隔坏(底(声行='- 兜底之隔：改——缓存之算：冷暖俱算\n', 择文=冷择)), '三数异处'))
    钉('改·只书暖价（冷暖同档）→ 坏', lambda: 有(隔坏(底(声行='- 兜底之隔：改——缓存之算：暖 $0.09（冷暖同档）；日 $4\n', 择文=冷择)), '缺 冷'))
    钉('改·冷暖俱书而无日之数 → 坏', lambda: 有(隔坏(底(声行='- 兜底之隔：改——缓存之算：冷 $3.3、暖 $0.27\n', 择文=冷择)), '缺 日'))
    钉('改·一数充二（「冷唤日约 $26」）→ 坏', lambda: 有(隔坏(底(声行='- 兜底之隔：改——缓存之算：冷唤日约 $26、暖 $0.27\n', 择文=冷择)), '三数异处'))
    钉('改·「改」而虫洞之择（去声明）无「缓存」→ 坏', lambda: 有(隔坏(底(声行=改声)), '⛔书「缓存」'))
    钉('改·「改」而无「——缓存之算：」→ 坏', lambda: 有(隔坏(底(声行='- 兜底之隔：改每三时\n', 择文=冷择)), '式不合'))
    # 三、号之界（险8·与 W912「要图」共一判）：W9xx 且 ≥913；W912 环7 起；W1xx、W1000、怪号免——经 验(W, tmp)（即 --开 之路）
    def _界():
        t = tempfile.mkdtemp()
        try:
            os.makedirs(os.path.join(t, 目录))
            for W, s in (('W913', 底('W913', 声行='')), ('W910', 底('W910', 声行='')), ('W151', 底('W151', 声行='')),
                         ('W912', 底('W912', 声行='')), ('W914', 全('W914'))):
                open(os.path.join(t, 目录, W + '.md'), 'w', encoding='utf-8').write(s)
            json.dump({'行': [{'键': 'wf_0000aaaa-001', '名': 'W914·预审', '席': 2}]}, open(os.path.join(t, '设定', '费账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
            r = {W: 验(W, t) for W in ('W913', 'W910', 'W151', 'W912', 'W914')}
            行2 = '| 2 | 五执笔 | 模型：创作，机器办不了 | 费账 wf_e7912fa3-a0c：执笔每席 $13—26 | 40 分 | $80 | 一席死即 resume |'
            open(os.path.join(t, 目录, 'W912.md'), 'w', encoding='utf-8').write(
                底('W912', 声行='').replace(行2, 行2 + '\n| 7 | 版之鲜 | 模型：续增之环 | 自测 1/1 | 1 分 | $1 | 退 |'))
            r['W912环7'] = 验('W912', t)
            return r
        finally:
            shutil.rmtree(t)
    钉('界·W913 缺声明与预审 → 坏（经 验(W, tmp)）', lambda: 有(_界()['W913'][1], '兜底之隔') and 有(_界()['W913'][1], '预审'))
    钉('界·W910、W151、W912（环1—6）→ 免', lambda: not any(有(_界()[W][1], '兜底之隔') or 有(_界()[W][1], '预审') for W in ('W910', 'W151', 'W912')))
    钉('界·W912 续增环7 → 照新律', lambda: 有(_界()['W912环7'][1], '兜底之隔'))
    钉('界·W914 声明与预审俱全 → 无其坏', lambda: not any('兜底之隔' in x or '预审' in x for x in _界()['W914'][1]))
    钉('界·总编辑之件：W9xx 且 ≥起；W1000、W913b、w913 免', lambda: 总编辑之件('W913', 913) and 总编辑之件('W999', 913) and not 总编辑之件('W912', 913)
       and not 总编辑之件('W1000', 913) and not 总编辑之件('W913b', 913) and not 总编辑之件('w913', 913) and not 总编辑之件('W151', 913))
    # 四、W911 本行自验（号虽免、式须自验）：真档之声明与预审之式
    W911文 = lambda: open(os.path.join(ROOT, 目录, 'W911.md'), encoding='utf-8').read()
    钉('W911·真档之声明过', lambda: 兜底之隔之坏(W911文()) == [])
    钉('W911·真档之预审之式过（过渡：预审与施同 Run·号 <913 免费账与深验）', lambda: 预审之式之坏(W911文()) == [])
    # 五、跨器之钉（险6·钉与表⛔同器）：独算 接棒守.兜底之令 常态之隔 <60、开者一日 ≥24 刻
    钉('跨器·常态之隔之算（甲:27＋乙:57 → 30；*/3 → 180；九至十七时 → 960；俱停 → 1440）', lambda: 常态之隔([('甲', 't', '27 * * * *', '27 * * * *', True), ('乙', 't', '57 * * * *', '47 * * * *', True)]) == (30, 48)
       and 常态之隔([('甲', 't', '27 */3 * * *', '27 * * * *', True)])[0] == 180 and 常态之隔([('甲', 't', '0 9-17 * * *', '0 * * * *', True)])[0] == 960
       and 常态之隔([('甲', 't', '27 * * * *', '27 * * * *', False)]) == (1440, 0) and 常态之隔([('甲', 't', '0,30 0-23/2 * * *', '0 * * * *', True)])[0] == 90)
    def _跨器():
        import 接棒守
        隔, 刻 = 常态之隔(接棒守.兜底之令)
        return 隔 < 60 and 刻 >= 24
    钉('跨器·接棒守.兜底之令 常态之隔 <60 且一日 ≥24 刻（坑61：隔逾一时缓存恒冷）', _跨器)
    # 六、预审之式（预审之律 险1—2·5）
    式坏 = lambda 文: 预审之式之坏(文)
    钉('预审·缺节 → 坏', lambda: 有(式坏(底('W913')), '无「## 预审」'))
    钉('预审·无 Run（席名⛔算）→ 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 者='二攻者（声明之律、预审之律）')), '无 Run'))
    钉('预审·防段「未防」（虽带锚）→ 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 险们=('- 险（环2）：x｜防：未防——自测待补', '- 险（取）：y｜防：自测钉之'))), '预审有未防'))
    钉('预审·「- 未防：…」之行 → 坏', lambda: 有(式坏(全().replace('- 判：可施', '- 未防：环2 之费\n- 判：可施')), '预审有未防'))
    钉('预审·防为 无／—／待後补 → 坏', lambda: all(有(式坏(底('W913') + 审(底('W913'), 险们=('- 险（环2）：x｜防：%s' % d, '- 险（取）：y｜防：自测钉之'))), '防空')
                                          for d in ('无', '—', '待後补', '暂缓')))
    钉('预审·缺「｜防：」段 → 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 险们=('- 险（环2）：x', '- 险（取）：y｜防：自测钉之'))), '缺「｜防：」'))
    钉('预审·防无锚 → 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 险们=('- 险（环2）：x｜防：多加小心', '- 险（取）：y｜防：自测钉之'))), '防无锚'))
    钉('预审·零险 → 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 险们=())), '无一险'))
    钉('预审·险未点环号、所点非环非取 → 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 险们=('- 险：x｜防：自测钉之', '- 险（取）：y｜防：自测钉之'))), '险之行式不合')
       and 有(式坏(底('W913') + 审(底('W913'), 险们=('- 险（环2、某）：x｜防：自测钉之', '- 险（取）：y｜防：自测钉之'))), '险之行式不合'))
    钉('预审·险点逐环所无之环 → 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 险们=('- 险（环2、环9）：x｜防：自测钉之', '- 险（取）：y｜防：自测钉之'))), '环9'))
    钉('预审·模型之环未攻 → 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 险们=('- 险（取）：y｜防：自测钉之',))), '未攻'))
    钉('预审·「取」未攻 → 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 险们=('- 险（环2）：x｜防：自测钉之',))), '未攻'))
    钉('预审·无「判：」→ 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 判='')), '判'))
    钉('预审·判之式不合（「判：大概可」）→ 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 判='- 判：大概可')), '判'))
    钉('预审·审之指不合（预审後改逐环）→ 坏', lambda: 有(式坏(全().replace('| 2 | 五执笔 |', '| 2 | 七执笔 |')), '复审'))
    钉('预审·全者 → 过；险文述旧之「未防」、半角之竖与冒号、「判：须改→已改 环2」→ 过', lambda: 式坏(全()) == []
       and 式坏(底('W913') + 审(底('W913'), 险们=('- 险（环2）：首稿未防之漏复现|防:自测钉之', '- 险（取）：y｜防：格：方案'), 判='- 判：须改→已改 环2')) == [])
    # 〔W911 补·复验③④〕防以否定之辞起、「* 险」「- 风险」之行、二判相违；审之指含声明；覆盖认 .github/、设定/
    钉('预审·防以否定之辞起（无自测／尚未防／⛔防／todo／TODO／不及／未及）→ 坏', lambda: all(有(式坏(底('W913') + 审(底('W913'), 险们=('- 险（环2）：x｜防：%s' % d, '- 险（取）：y｜防：自测钉之'))), '防空')
       for d in ('无自测', '尚未防，自测待补', '⛔防（自测不及）', 'todo 工具/x', 'TODO 自测', 'ToDo 自测', '不及：自测', '未及：自测')))
    钉('预审·「* 险」「- 风险」「* 风险」起之行亦为险行（式不合即坏·⛔静过）', lambda: all(有(式坏(底('W913') + 审(底('W913'), 险们=(
        '- 险（环2）：x｜防：自测钉之', '- 险（取）：y｜防：自测钉之', '%s（环2）：z｜防：未防' % h))), '险之行式不合') for h in ('* 险', '- 风险', '* 风险')))
    钉('预审·二判相违（「可施」与「须改→已改」并书）→ 坏', lambda: 有(式坏(底('W913') + 审(底('W913'), 判='- 判：可施\n- 判：须改→已改 环2')), '相违'))
    钉('预审·审之指含兜底之隔之声明（预审後改「不改」为「改」→ 复审）', lambda: 有(式坏(全().replace(声, 改声)), '复审'))
    钉('预审·覆盖认 做什么书 .github/、设定/ 之环（人之环亦然）→ 未攻即坏', lambda: all(有(式坏((lambda 文: 文 + 审(文))(底('W913').replace(
        '## 未确证', '| 3 | 改 %s | 人：总编辑 | 试：python3 工具/方案.py --自测 → 1/1 | 1 分 | $0 | 退回旧版 |\n## 未确证' % p, 1))), '未攻：环3')
        for p in ('.github/workflows/巡.yml', '设定/执行之制.md')))
    # 七、预审之账（浅验·费账）：键在、名「W·预审」起、席之和 ≥2
    def _账(行们, 文=None):
        t = tempfile.mkdtemp()
        try:
            os.makedirs(os.path.join(t, '设定'))
            json.dump({'行': 行们}, open(os.path.join(t, '设定', '费账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
            return 预审之账之坏(文 or 全(), 'W913', t)
        finally:
            shutil.rmtree(t)
    钉('预审之账·键不在费账 → 坏', lambda: 有(_账([]), '不在费账'))
    钉('预审之账·他件之 Run（名「W911·巡之钟」）→ 坏', lambda: 有(_账([{'键': 'wf_0000aaaa-001', '名': 'W911·巡之钟', '席': 14}]), '非「W913·预审」'))
    钉('预审之账·席 1 → 坏', lambda: 有(_账([{'键': 'wf_0000aaaa-001', '名': 'W913·预审', '席': 1}]), '≥2'))
    钉('预审之账·「W913·预审」席 2 → 过；子席二键各一席 → 过', lambda: _账([{'键': 'wf_0000aaaa-001', '名': 'W913·预审', '席': 2}]) == []
       and _账([{'键': '子席:agent-a01.jsonl', '名': 'W913·预审·甲', '席': 1}, {'键': '子席:agent-a02.jsonl', '名': 'W913·预审·乙', '席': 1}],
              全(者='子席:agent-a01、子席:agent-a02')) == [])
    # 八、预审之深验（--开·本机读 Run 之档）与 工作流账 --开／--裁 之拦（临时之方案、临时之账、临时之 Run 之档）
    import datetime as _d, contextlib as _cl, io as _io
    今 = _d.datetime.now(_d.timezone.utc)
    def _场(文们, Run=None, 费=None):
        t = tempfile.mkdtemp()
        os.makedirs(os.path.join(t, 目录)); os.makedirs(os.path.join(t, 'R', 'p', 's', 'workflows'))
        for W, s in 文们.items():
            open(os.path.join(t, 目录, W + '.md'), 'w', encoding='utf-8').write(s)
        json.dump({'宗旨': '测', '件': []}, open(os.path.join(t, '设定', '工作流账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        json.dump({'行': 费 if 费 is not None else [{'键': 'wf_0000aaaa-001', '名': 'W913·预审', '席': 2, '美元': 1}]},
                  open(os.path.join(t, '设定', '费账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        if Run is not None:
            json.dump(Run, open(os.path.join(t, 'R', 'p', 's', 'workflows', 'wf_0000aaaa-001.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        return t
    好Run = {'status': 'completed', 'script': "const P = WT + '/设定/方案/W913.md'", 'startTime': int((今.timestamp() - 3600) * 1000),
             'result': {'atks': [{'risks': [{'risk': '甲'}, {'risk': '乙'}], 'verdict': '可施'}]}}
    须改果 = {'atks': [{'risks': [{'risk': '甲'}, {'risk': '乙'}], 'verdict': '须改，改後可施'}]}
    def _于场(文们, Run, f, 费=None):
        t = _场(文们, Run, 费)
        旧 = os.environ.get('ZM_WORKFLOWS_ROOT')
        os.environ['ZM_WORKFLOWS_ROOT'] = os.path.join(t, 'R')
        try:
            return f(t)
        finally:
            os.environ.pop('ZM_WORKFLOWS_ROOT') if 旧 is None else os.environ.__setitem__('ZM_WORKFLOWS_ROOT', 旧)
            shutil.rmtree(t)
    _深 = lambda Run, 文=None: _于场({'W913': 文 or 全()}, Run, lambda t: 预审之深验('W913', t, 今))
    钉('深验·全 → 过', lambda: _深(好Run) == ([], []))
    钉('深验·Run 之档本机不在 → 坏（拒开）', lambda: 有(_深(None)[0], '本机不在'))
    钉('深验·状 running → 坏', lambda: 有(_深(dict(好Run, status='running'))[0], 'completed'))
    钉('深验·脚本⛔含本方案之路（借 Run）→ 坏', lambda: 有(_深(dict(好Run, script='W911.md'))[0], '所审非此方案'))
    钉('深验·起时不早於开 → 坏', lambda: 有(_深(dict(好Run, startTime=int((今.timestamp() + 60) * 1000)))[0], '起时'))
    钉('深验·Run 出险三而节只二 → 坏', lambda: 有(_深(dict(好Run, result={'risks': [{'risk': 1}, {'risk': 2}, {'risk': 3}]}))[0], '俱入节'))
    钉('深验·攻者判「须改」而节判「可施」→ 坏；节判「须改→已改 环2」→ 过；攻者判「无须改」⛔算须改', lambda: 有(_深(dict(好Run, result=须改果))[0], '须改')
       and _深(dict(好Run, result=须改果), 全(判='- 判：须改→已改 环2')) == ([], [])
       and all(_深(dict(好Run, result={'atks': [dict(须改果['atks'][0], verdict='可施，%s' % v)]})) == ([], []) for v in ('无须改', '不须改', '毋须改')))
    _二费 = [{'键': 'wf_0000aaaa-001', '名': 'W913·预审', '席': 2, '美元': 1}, {'键': 'wf_0000bbbb-002', '名': 'W913·预审', '席': 2, '美元': 1}]
    def _二Run(t):
        json.dump(好Run, open(os.path.join(t, 'R', 'p', 's', 'workflows', 'wf_0000bbbb-002.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        return 预审之深验('W913', t, 今)
    钉('深验·二 Run：前「须改」後「可施」而节判「可施」→ 坏（⛔只取末 Run）', lambda: 有(_于场({'W913': 全(者='wf_0000aaaa-001、wf_0000bbbb-002')}, dict(好Run, result=须改果), _二Run, _二费)[0], '须改'))
    钉('深验·Run 之 result 无险（空、{}、字串之列）→ 坏', lambda: all(有(_深(dict(好Run, result=r))[0], '无险')
       for r in (None, {}, {'risks': ['甲', '乙']}, {'atks': [{'risks': '甲；乙', 'verdict': '可施'}]})))
    钉('深验·云坐 → 只浅验而印 ⚠', lambda: _深(None, 全(者='wf_0000aaaa-001（云坐）'))[0] == [] and 有(_深(None, 全(者='wf_0000aaaa-001（云坐）'))[1], '云坐'))
    def _子席(t, 有路=True):
        d = os.path.join(t, 'R', 'p', 's', 'subagents'); os.makedirs(d)
        open(os.path.join(d, 'agent-a01.jsonl'), 'w', encoding='utf-8').write(
            json.dumps({'timestamp': (今 - _d.timedelta(hours=1)).isoformat(), 'message': {'content': '攻 设定/方案/W913.md' if 有路 else '攻 W911'}}, ensure_ascii=False) + '\n')
        return 预审之深验('W913', t, 今)[0]
    子文 = lambda: 全(者='子席:agent-a01')
    钉('深验·子席之转录含本方案之路 → 过；⛔含 → 坏', lambda: _于场({'W913': 子文()}, None, _子席) == []
       and 有(_于场({'W913': 子文()}, None, lambda t: _子席(t, False)), '所审非此方案'))
    钉('稿·--预审 W <Run> 自 result 机出诸险，未填环与防即坏（逐险行俱坏、判亦坏）', lambda: (lambda L: sum(1 for x in L if x.startswith('- 险')) == 2
       and sum(1 for x in 式坏(底('W913') + '\n' + '\n'.join(L) + '\n') if x.startswith('险之行式不合')) == 2
       and 有(式坏(底('W913') + '\n' + '\n'.join(L) + '\n'), '判之式不合'))(_于场({'W913': 底('W913')}, 好Run, lambda t: 预审之稿('W913', 'wf_0000aaaa-001', t))))
    def _开(文们, Run, W='W913', 改后=None):
        def f(t):
            import 工作流账 as _账器
            o = _io.StringIO()
            with _cl.redirect_stdout(o):
                r = _账器.开(W, 2, '停', '换', '挡路：测；坑之检：无新坑；零token之检：须模型', '约 1 时、$100', t, 今)
                c = None
                if 改后 is not None:
                    open(os.path.join(t, 目录, W + '.md'), 'w', encoding='utf-8').write(改后)
                    c = _账器.裁(W, '续', '续一回之由', 1, t, 今)
            return r, c, o.getvalue()
        return _于场(文们, Run, f)
    钉('开·无预审之 W913 → 拒开', lambda: _开({'W913': 底('W913') + 图节}, 好Run)[0] is False and '预审' in _开({'W913': 底('W913') + 图节}, 好Run)[2])
    钉('开·预审全而 Run 之档本机不在 → 拒开（深验）', lambda: _开({'W913': 全()}, None)[0] is False and '本机不在' in _开({'W913': 全()}, None)[2])
    钉('开·声明、预审、费账、Run 之档俱全 → 开', lambda: _开({'W913': 全()}, 好Run)[0] is True)
    钉('开·怪号之新件（W913b）→ 拒开', lambda: _开({'W913b': 全('W913b')}, 好Run, 'W913b')[0] is False)
    钉('开·前导零之号（W0913）→ 拒开；⛔免（验之亦坏）', lambda: _开({'W0913': 全('W0913')}, 好Run, 'W0913')[0] is False
       and _于场({'W0913': 底('W0913', 声行='')}, None, lambda t: 验('W0913', t))[0] is False)
    钉('裁·开後改逐环而审之指⛔更 → 裁拒（开後改环者亦验）', lambda: _开({'W913': 全()}, 好Run, 改后=全().replace('| 2 | 五执笔 |', '| 2 | 七执笔 |'))[1] is False)
    钉('裁·方案未改 → 裁许', lambda: _开({'W913': 全()}, 好Run, 改后=全())[1] is True)
    # 九、模板：声明与预审之占位俱⛔过（⛔以默值过闸）
    钉('模板·有「## 预审」与声明之占位，验之俱坏', lambda: '## 预审' in 模板 and 预审之式之坏(模板.format(W='W913', 题='测')) != [])
    for 名, v in 新钉:
        共 += 1; ok += v
        if not v:
            print('  ✗ ' + 名)
    print('方案·自测 %d/%d' % (ok, 共))
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
        sys.exit(0 if o else 1)
    if a[:1] == ['--预审之指'] and len(a) == 2:      # 〔W911 环6〕审之指：取行、兜底之隔之声明与逐环之 做什么／败则 之 sha1 前八位
        print(预审之指(open(os.path.join(ROOT, 目录, a[1] + '.md'), encoding='utf-8').read()))
        sys.exit(0)
    if a[:1] == ['--预审'] and len(a) == 3:          # 〔W911 环6〕「## 预审」之稿：自 Run 之 result 机出险行（施者只填环与防、书判）
        try:
            print('\n'.join(预审之稿(a[1], a[2])))
        except Exception as e:
            print('⛔ 预审之稿不得：%s' % e); sys.exit(1)
        sys.exit(0)
    if a == ['--验全']:
        fs = sorted(glob.glob(os.path.join(ROOT, 目录, 'W*.md')))
        全坏 = 0
        for f in fs:
            W = os.path.basename(f)[:-3]
            o, 坏 = 验(W)
            if not o:
                全坏 += 1; print('⛔ %s：%s' % (W, '；'.join(坏)[:300]))
        print('方案：%d 份，不过 %d' % (len(fs), 全坏))
        sys.exit(0 if not 全坏 else 1)
    print(__doc__); sys.exit(2)
