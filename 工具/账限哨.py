#!/usr/bin/env python3
"""账限哨（1021 立·作者问「为什么到现在还是我自己发现之後告诉你，你才发现」）。

为何立：瑕疵总账诸条皆写了「限」（如「401 段前」「407 大审前」），而⛔一器读之——限到不到，全凭主环记得；
复盘之「B＋C 之候」写了七回、行了二回，亦无一处催。本哨零 token：读 设定/瑕疵总账.md 之未治诸行，取其限之章号，
与下一章比——到期即「欠」，自走.py 照「到期账」之欠一并印、⛔起笔；工作流账.py 会话开头亦印。
限之式：「NNN 段前／段开镜前／开镜前／前」→ 下一章 ≥ NNN 即到；「NNN 封版前／记席前／大审前」→ 下一章 > NNN 即到
（其活可於 NNN 一章之内办；大审前：NNN 所终之十章大审於 NNN 封後方开·407 账限误拦之治）；裸「NNN」作「NNN 前」（1027·X57 之「408」旧不判）。
1027 执行之审 #10 #14 #15 #20 #72 之改（作者令「已定之决……须全部执行起来」）：
  ①延须带新数之限：「延至 NNN<式>：<由>」（由四字以上），判以新限；一条至多一延——第二延即⛔（再延是把账搬个地方放着）；
    新限至多原限之後二十章（两段）——逾即⛔（「延至 999」形同无期）；
    旧式「延：<由>」无数，作未延、照原限拦（旧式之延 1021—1024 一挂再挂，X17 挂至全书写完）。
  ②未治之节，限栏取不出章号者即⛔（「W11 各该节」之无期之口）——唯明写「无限：<由>」者免。
  ③（1106 进化主义「缺陷一见即治、坚决不拖」）未延之条，原限至远下一章後十章（一段）——限远即⛔；须候某情者写「无限：<由>」。
用法：
  python3 工具/账限哨.py          # 印到期与将到（三章内）之条；有到期 rc=1
  python3 工具/账限哨.py --自测
  python3 工具/账限哨.py --撞号        # 〔W919〕列本账之号撞（一号二行）与跨枝之撞（同号异条·origin/主 ∪ 在飞之 章-*／治-*）；有撞 rc 1
  python3 工具/账限哨.py --新号        # 〔W919〕取新号：origin/主 ∪ 章-*／治-* 诸账之最大号（fetch 限十五秒）＋余三（跨在飞诸章可立之号）
  python3 工具/账限哨.py --号 X132     # 〔W919〕列本号之诸行、「原号 X132」之行、工具之活引（改号只改其注·史之引⛔动）
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import os, sys, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_式 = r'(段开镜前|段前|开镜前|大审前|封版前|记席前|前)'
限式 = re.compile(r'(?<!\d)(\d{3})(?!\d)\s*' + _式)
裸式 = re.compile(r'^\s*(\d{3})(?!\d)')                     # 裸 NNN（限栏之首）→「NNN 前」
延至式 = re.compile(r'延至\s*(\d{3})(?!\d)\s*' + _式 + r'?\s*[：:]\s*([^）)|]*)')
旧延式 = re.compile(r'(?<![至无])延[：:]')                     # 无数之延（旧式）
延上 = 20                                                      # ★一延至多两段（二十章）——无上则「延至 999」即无期之口
远上 = 10                                                      # ★1106 进化主义：原限至远一段（十章）——立账即排进下一段之内，⛔远挂
无限式 = re.compile(r'无限[：:]\s*(?:\S\s*){4,}')


def _限(格):
    """限栏 → (章, 式) 或 (None, '')：先认带式者（延至之段去之），次认栏首之裸 NNN。"""
    原 = 延至式.sub('', 格)
    k = 限式.search(原)
    if k:
        return int(k.group(1)), k.group(2)
    k = 裸式.match(原)
    if k:
        return int(k.group(1)), '前'
    return None, ''


承式 = re.compile(r'承\s*(X\d+(?:\s*[、，,]\s*X\d+)*)')         # 〔执行之制·治11〕换号不重计延：题或源书「承 X<旧号>」


def _全行(文):
    """X 号 → 其行之格（全账诸节俱取·已治亦取：换号之旧条多已移已治）；号重者取首见。"""
    d = {}
    for l in 文.split('\n'):
        if re.match(r'\|\s*X\d+\s*\|', l):
            格 = [c.strip() for c in l.strip().strip('|').split('|')]
            d.setdefault(格[0], (格, l))
    return d


def 承之链(号, 文, 全=None, 见=None):
    """→ (承之号[]（递归·⛔环）, 合延)：每一承即一延（换号＝把账搬个号放着），并合旧条自身之延（新式＋旧式）。"""
    全 = 全 if 全 is not None else _全行(文)
    见 = 见 if 见 is not None else {号}
    格, l = 全.get(号, ([号, '', ''], ''))
    链, 延 = [], 0
    for 段 in 承式.findall(' '.join(格[1:3])):
        for k in re.findall(r'X\d+', 段):
            if k in 见:
                continue
            见.add(k)
            链.append(k)
            延 += 1
            if k in 全:
                kl = 全[k][1]
                延 += len(延至式.findall(kl)) + len(旧延式.findall(kl))
                子链, 子延 = 承之链(k, 文, 全, 见)
                链 += 子链
                延 += 子延
    return 链, 延


def 同类之窗(链, 文, 全=None):
    """承之链诸条之题中所见之章号（三位）→ (起, 止)｜None：印「同类连 N 章逾」（只印·配额⛔拦书·总章:58）。"""
    全 = 全 if 全 is not None else _全行(文)
    数 = [int(x) for k in 链 if k in 全 for x in re.findall(r'(?<!\d)([34]\d\d)(?!\d)', 全[k][0][1])]
    return (min(数), max(数)) if 数 else None


def 诸条(文):
    """返 [(号, 题, 限章, 限式, 延, 病)]——只取「## 未治」一节之 X 行。
    延：已依新限（「延至 NNN：由」）判者为 True；病：'' 或 ⛔之由（无章号／二延／延至无由）——有病者即到期。"""
    # ★复核所逮（1027）：旧只读「## 未治」一节——X 行挪进他节（「## 挂起」「## 候」之类）即出哨之眼、无期而逃；今凡非「## 已治…」之节俱读
    行们 = []
    for 节 in re.split(r'^## ', 文, flags=re.M)[1:]:
        题, _, 体 = 节.partition('\n')
        if not 题.startswith('已治'):
            行们 += 体.split('\n')
    out = []
    全 = _全行(文)
    for l in 行们:
        if not re.match(r'\|\s*X\d+\s*\|', l):
            continue
        格 = [c.strip() for c in l.strip().strip('|').split('|')]
        号, 题, 限 = 格[0], 格[1][:40], 格[-1]
        章, 式 = _限(限)
        新 = 延至式.findall(l)
        旧 = 旧延式.findall(l)
        链, 承延 = 承之链(号, 文, 全) if 承式.search(' '.join(格[1:3])) else ([], 0)
        延, 病 = False, ''
        if len(新) + len(旧) + 承延 >= 2:
            病 = '延逾一回（新式 %d、旧式 %d%s）——一条至多一延，再延即⛔：治之，或写「弃：由」移已治' % (
                len(新), len(旧), '、承 %s 合延 %d·换号不重计（执行之制·治11）' % ('、'.join(链), 承延) if 链 else '')
        elif 承延 and not 新:
            延 = True                                    # 承一旧号＝已延一回（⛔再延）
        elif 新:
            n, s, 由 = 新[0]
            if len(re.sub(r'\s', '', 由)) < 4:
                病 = '「延至 %s」无由（须四字以上）' % n
            elif 章 is not None and int(n) - 章 > 延上:
                病 = '「延至 %s」逾原限 %d 之後 %d 章——一延至多两段（%d 章）：「延至 999」形同无期（1027 复核所逮）' % (n, 章, 延上, 延上)
            else:
                章, 式, 延 = int(n), (s or '前'), True
        if not 病 and 章 is None and not 无限式.search(限):
            病 = '限栏取不出章号（「%s」）——须写数限，或「无限：<由>」' % 限[:24]
        out.append((号, 题, 章, 式, 延, 病))
    return out


def 判(下, 文):
    """返 (到期, 将到)：到期 [(号, 题, 章, 式, 延, 病)]（有病者恒到期）；将到为三章内者。"""
    到, 将 = [], []
    for x in 诸条(文):
        号, 题, 章, 式, 延, 病 = x
        if 病:
            到.append(x)
            continue
        if 章 is None:
            continue
        if not 延 and 章 - 下 > 远上:   # ★1106 进化主义「缺陷一见即治、坚决不拖」：原限至远一段——限远即⛔（须等某情者写「无限：<由>」）
            到.append((号, 题, 章, 式, 延, '限远逾一段（限 %d·下一章 %d·至远 %d 章）——缺陷一见即治⛔拖；须候某情者写「无限：<由>」' % (章, 下, 远上)))
            continue
        到期 = (下 > 章) if 式 in ('封版前', '记席前', '大审前') else (下 >= 章)
        if 到期:
            到.append(x)
        elif 章 - 下 <= 3:
            将.append(x)
    return 到, 将


def 末章(root=ROOT):
    try:
        import 自走
        return 自走.末章()
    except Exception:
        return 0


哨账之拦起 = 486          # 〔执行之制·治14〕下一章 483—485 只报（三章），486 起入到期而拦（段序之守照旧拦派）
哨承式 = re.compile(r'承\s*费哨')
哨之顶 = 3               # 「无估」「无由之非写」各累三即到期


def 哨红未入账(root=ROOT, 文=None, 两段=None, 无估无由=None):
    """〔执行之制·治14（律⑲·1124·482 主环收批）〕→ [由]：费哨（治3 之真尺）连两段红、「无估」累三、「无由之非写」累三——
    瑕疵总账未治之节无「承 费哨」之 X（带限、带治）者，各为一条「哨红未入账」。账限哨只读⛔写（⛔令器写瑕疵总账：添写者）。
    两段、无估无由 可注（自测）。"""
    if 文 is None:
        try:
            文 = open(os.path.join(root, '设定', '瑕疵总账.md'), encoding='utf-8').read()
        except Exception:
            文 = ''
    行们 = []
    for 节 in re.split(r'^## ', 文, flags=re.M)[1:]:
        题, _, 体 = 节.partition('\n')
        if not 题.startswith('已治'):
            行们 += [l for l in 体.split('\n') if re.match(r'\|\s*X\d+\s*\|', l)]
    if any(哨承式.search(l) for l in 行们):
        return []
    try:
        import 费哨
        段 = 两段 if 两段 is not None else 费哨.两段(root)
        估, 由 = 无估无由 if 无估无由 is not None else 费哨.无估无由(root)
    except Exception as e:
        return ['费哨读不得（%s）——缺即印缺' % str(e)[:40]]
    出 = []
    if len(段) >= 2 and 段[0] and 段[1] and 段[0][0] and 段[1][0]:
        出.append('费哨连两段红（写书之占 今 %.0f%%、前段 %.0f%%·界 70%%）' % (段[0][1] * 100, 段[1][1] * 100))
    if len(估) >= 哨之顶:
        出.append('无估之件累 %d（$%.0f）' % (len(估), sum(x[2] for x in 估)))
    if len(由) >= 哨之顶:
        出.append('无由之非写累 %d（$%.0f）' % (len(由), sum(x[2] for x in 由)))
    return 出


def 同类之印(文):
    """〔执行之制·治11〕未治之条承旧号者 → 「同类连 N 章逾：前治 X<旧> 无效」（只印⛔拦：配额之证⛔改红·总章:58「钱已花，勿以配额拦书」）。"""
    L, 全 = [], _全行(文)
    for 号, 题, 章, 式, 延, 病 in 诸条(文):
        格 = 全.get(号, ([号, '', ''], ''))[0]
        if not 承式.search(' '.join(格[1:3])):
            continue
        链, _ = 承之链(号, 文, 全)
        窗 = 同类之窗([号] + 链, 文, 全)
        L.append('   · %s 承 %s：同类连 %s 章逾%s：前治 %s 无效（换号合计其延·执行之制·治11）' % (
            号, '、'.join(链), (窗[1] - 窗[0] + 1) if 窗 else '?', '（%d—%d）' % 窗 if 窗 else '', '、'.join(链)))
    return L


def 印(root=ROOT, 下=None):
    try:
        文 = open(os.path.join(root, '设定', '瑕疵总账.md'), encoding='utf-8').read()
    except Exception as e:
        return False, ['账限哨：瑕疵总账读不得（%s）' % e]
    下 = 下 or 末章(root) + 1
    到, 将 = 判(下, 文)
    哨 = 哨红未入账(root, 文)
    if 哨 and 下 >= 哨账之拦起:
        到 = 到 + [('哨', '哨红未入账：费哨', None, '', False, '；'.join(哨) + '——瑕疵总账无「承 费哨」之 X：总编辑写一条 X（带限、带治）方消（执行之制·治14·律⑲）')]
    L = ['%s 账限哨：下一章 %d——瑕疵总账到期 %d 条（其中延至新限者 %d）、三章内将到 %d 条' % ('⛔' if 到 else '✓', 下, len(到), sum(1 for x in 到 if x[4]), len(将))]
    for 号, 题, 章, 式, 延, 病 in 到:
        if 病:
            L.append('   ⛔ %s %s：%s' % (号, 病, 题))
        else:
            L.append('   ⛔ %s 限 %d %s%s：%s' % (号, 章, 式, '（已延一回·⛔再延）' if 延 else '', 题))
    for 号, 题, 章, 式, 延, 病 in 将:
        L.append('   · %s 限 %d %s：%s' % (号, 章, 式, 题))
    L += 同类之印(文)
    if 哨 and 下 < 哨账之拦起:
        L.append('   ⚠ 哨红未入账：费哨——%s；瑕疵总账无「承 费哨」之 X（写一条 X 带限、带治方消·只报至下一章 %d·%d 起拦·执行之制·治14）'
                 % ('；'.join(哨), 哨账之拦起 - 1, 哨账之拦起))
    if 到:
        L.append('   治法：先治而移「已治」（带提交），或写「弃：<由>」移已治；未延过者可写一回「延至 NNN<式>：<由>」（须新数限，到期照拦）。')
    try:                                 # 〔W919 环14〕号撞只印 ⚠（⛔拦派）
        for 号, 行们 in sorted(号撞(文).items(), key=lambda x: int(x[0][1:])):
            L.append('   ⚠ 号撞 %s：设定/瑕疵总账.md:%s——改号：`python3 工具/账限哨.py --新号` 取号、活引多者留号（⛔拦派）' % (号, '、:'.join(map(str, 行们))))
    except Exception as e:
        L.append('   ⚠ 号撞之判崩：%s' % e)
    return bool(到), L


# ── 〔W919 环14〕号撞：二坐（章之坐、总编辑之坐）各自其派时之树取「末号＋1」而立 X，并入即撞（X132、X134、X145）——
#   号撞(文) 只报（印 ⚠·⛔拦派）；号於入主之时以 --新号 取（并 origin/主 与在飞之 章-*／治-* 诸账·留余三）；改号照「活引多者留号」，
#   被改者行首书「〔原号 Xn·号撞（二坐同取）·W919 改号〕」（⛔书「承 X」：承式即计延）；推.py 速检之 新号之撞 与 --新号 同取其集（号之集·一函）。
号行式 = re.compile(r'^\|\s*(X\d+)\s*\|')
号余 = 3                  # 跨在飞诸章可立之号（486—489 之章坐各或立一号）
号之取限 = 15             # fetch 之限（秒）
号之枝数 = 40             # 章-*／治-* 取其近者（committerdate）——旧者已并入主枝


def 号撞(文):
    """→ {号: [行号…]}：一号见二行以上者（全账诸节俱计；引块「>」之行⛔计）。"""
    d = {}
    for i, l in enumerate((文 or '').split('\n'), 1):
        m = 号行式.match(l)
        if m:
            d.setdefault(m.group(1), []).append(i)
    return {k: v for k, v in d.items() if len(v) > 1}


def 条之首(l):
    """X 行 → 其「缺」栏之首十六字（去行首「〔…〕」之注、空白）——跨枝比同号是否同条（条移已治、行内改其尾⛔异）。"""
    格 = [c.strip() for c in l.strip().strip('|').split('|')]
    缺 = 格[1] if len(格) > 1 else ''
    缺 = re.sub(r'^〔[^〕]*〕', '', 缺)
    return re.sub(r'\s', '', 缺)[:16]


def 号表(文):
    """→ {号: [条之首…]}（全账诸节）。"""
    d = {}
    for l in (文 or '').split('\n'):
        m = 号行式.match(l)
        if m:
            d.setdefault(m.group(1), []).append(条之首(l))
    return d


def _git(root, *a, 限=10):
    import subprocess
    return subprocess.run(['git', '-c', 'core.quotepath=off'] + list(a), cwd=root, capture_output=True, text=True, timeout=限)


def 号之集(root=ROOT, 取=True, 枝=None):
    """→ (集, 取败)：集 = {ref: {号: [条之首…]}}——origin/主 ∪ 近 号之枝数 个 origin 之 章-*／治-*（未并入主枝者·在飞）（--新号 与 推.py 速检 新号之撞 同取·坑53）。
    取：先 fetch（限 号之取限 秒）；败即用本地之 refs、取败 True。崩只返其所得。"""
    import subprocess
    枝 = 枝 or 'claude/the-novel-review-4dtuit'
    取败 = False
    if 取:
        try:
            r = _git(root, 'fetch', '-q', '--no-tags', 'origin', '+refs/heads/%s:refs/remotes/origin/%s' % (枝, 枝),
                     '+refs/heads/章-*:refs/remotes/origin/章-*', '+refs/heads/治-*:refs/remotes/origin/治-*', 限=号之取限)
            取败 = r.returncode != 0
        except Exception:
            取败 = True
    集 = {}
    try:
        诸 = ['refs/remotes/origin/' + 枝] + [x for x in _git(root, 'for-each-ref', '--sort=-committerdate', '--count=%d' % 号之枝数, '--format=%(refname)',
                                                         'refs/remotes/origin/章-*', 'refs/remotes/origin/治-*').stdout.split('\n') if x.strip()]
        for i, ref in enumerate(诸):
            if i and _git(root, 'merge-base', '--is-ancestor', ref, 诸[0]).returncode == 0:
                continue                 # 已并入主枝者（其号已入主账·旧撞已改）⛔计——只计主枝与在飞之枝
            t = _git(root, 'show', '%s:设定/瑕疵总账.md' % ref)
            if t.returncode == 0:
                集[ref] = 号表(t.stdout)
    except Exception:
        取败 = True
    return 集, 取败


def 末号(集, *文们):
    数 = [int(k[1:]) for 表 in 集.values() for k in 表] + [int(m) for 文 in 文们 for m in re.findall(r'(?m)^\|\s*X(\d+)\s*\|', 文 or '')]
    return max(数) if 数 else 0


def 新号(集, *文们, 余=号余):
    """→ 'Xn'：诸账之最大号＋1＋余（留余三：在飞诸章自其派时之树取「末号＋1」，⛔与之复撞）。"""
    return 'X%d' % (末号(集, *文们) + 1 + 余)


def 跨枝之撞(文, 集):
    """→ [(号, 本条之首, ref, 彼条之首)]：本账之号（本账只一行者）於他枝之账异条（同号异条＝二坐同取）。"""
    本 = 号表(文)
    出 = []
    for 号, 首们 in sorted(本.items(), key=lambda x: int(x[0][1:])):
        if len(首们) != 1:
            continue
        for ref, 表 in 集.items():
            彼们 = 表.get(号, [])
            if 首们[0] in 彼们:
                continue                 # 彼枝亦有本条（其余之同号者係本账已改号之旧撞·⛔重报）
            for 彼 in 彼们:
                if 彼 and 首们[0] and 彼 != 首们[0]:
                    出.append((号, 首们[0], ref, 彼))
    return 出


def 撞号之印(root=ROOT, 取=True, 文=None, 集=None):
    """→ (有撞, [行])：本账之号撞（一号二行）与跨枝之撞。"""
    文 = 文 if 文 is not None else open(os.path.join(root, '设定', '瑕疵总账.md'), encoding='utf-8').read()
    L, 撞 = [], 号撞(文)
    for 号, 行们 in sorted(撞.items(), key=lambda x: int(x[0][1:])):
        L.append('   ⚠ 号撞 %s：设定/瑕疵总账.md:%s（%s）' % (号, '、:'.join(map(str, 行们)), '｜'.join(号表(文)[号])))
    取败 = False
    if 集 is None:
        集, 取败 = 号之集(root, 取)
    跨 = 跨枝之撞(文, 集)
    for 号, 本, ref, 彼 in 跨:
        L.append('   ⚠ 跨枝之撞 %s：本账「%s」｜%s「%s」' % (号, 本, ref.replace('refs/remotes/', ''), 彼))
    if 取败:
        L.append('   ⚠ fetch 不成（限 %d 秒）——跨枝之撞以本地之 refs 判' % 号之取限)
    return bool(撞 or 跨), L


def 号之引(号, root=ROOT, 文=None):
    """→ [行]：本号之诸行、「原号 Xn」之行（设定/瑕疵总账.md）、工具之活引（工具/*.py、工具/席/*.js）。"""
    文 = 文 if 文 is not None else open(os.path.join(root, '设定', '瑕疵总账.md'), encoding='utf-8').read()
    L = []
    式 = re.compile(r'(?<![\dA-Za-z])%s(?!\d)' % re.escape(号))
    for i, l in enumerate(文.split('\n'), 1):
        m = 号行式.match(l)
        if (m and m.group(1) == 号) or ('原号 %s' % 号) in l and 式.search(l):
            L.append('  设定/瑕疵总账.md:%d　%s' % (i, l[:90]))
    for f in sorted(glob.glob(os.path.join(root, '工具', '*.py')) + glob.glob(os.path.join(root, '工具', '席', '*.js'))):
        try:
            for i, l in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
                if 式.search(l):
                    L.append('  %s:%d　%s' % (os.path.relpath(f, root), i, l.strip()[:90]))
        except Exception:
            continue
    return L


def 自测():
    r = []
    def T(名, 条):
        r.append((名, bool(条)))
        print(('  ✓ ' if 条 else '  ✗ ') + 名)
    文 = '''# 账
## 未治
| 号 | 题 | 源 | 治 | 限 |
|---|---|---|---|---|
| X1 | 甲病 | s | t | 401 段开镜前（某裁） |
| X2 | 乙病 | s | t | 401 封版前 |
| X3 | 丙病 | s | t | W11 各该节 |
| X4 | 丁病 | s | t | 403 段前 |
| X5 | 戊病 | s | t | 401 段前（延：W59 落後即治，候其干跑） |
| X6 | 己病 | s | t | 410 前 |
| X19 | 申病 | s | t | 420 前 |
| X7 | 庚病 | s | t | 401 大审前 |
| X8 | 辛病 | s | t | 408 |
| X9 | 壬病 | s | t | 无限：全书写完之後之二稿，与章无涉 |
| X10 | 癸病 | s | t | 401 段前（延至 420 段前：某器之改随 411 段剧情庭顺治） |
| X11 | 子病 | s | t | 401 段前（延至 404 段前：先候一章）（延至 420 段前：再候） |
| X12 | 丑病 | s | 治（延：甲由甚长） | 401 段前（延至 420 段前：又延一回之由） |
| X13 | 寅病 | s | t | 401 段前（延至 420 段前：） |
| X14 | 卯病 | s | t | 410 段前（延：旧式之由甚长） |
| X17 | 午病 | s | t | 401 段前（延至 999 段前：一个够长之由） |
| X18 | 未病 | s | t | 401 段前（延至 421 段前：恰两段之由） |
> | X98 | 引之旧账（引块：转引他档之印） | s | t | 380 段前 |
## 挂起（他节）
| X15 | 辰病 | s | t | W11 各该节 |
| X16 | 巳病 | s | t | 401 段前 |
## 已治
| Y1 | 旧 | s | t | 300 前 |
| X99 | 旧之无限 | s | t | W11 各该节 |
'''
    到, 将 = 判(401, 文)
    号到 = [x[0] for x in 到]
    病 = {x[0]: x[5] for x in 诸条(文)}
    T('①「401 段开镜前」下一章 401 即到', 'X1' in 号到)
    T('②「401 封版前」下一章 401 未到（可於 401 之内办）', 'X2' not in 号到)
    T('③「401 封版前」下一章 402 即到', 'X2' in [x[0] for x in 判(402, 文)[0]])
    T('④（1027 改）限栏取不出章号（「W11 各该节」）→ 即⛔（旧式不判·无期之口）', 'X3' in 号到 and '取不出章号' in 病['X3'])
    T('④之二 写「无限：<由>」者免（放行之反例）', 'X9' not in 号到 and not 病['X9'])
    T('⑤三章内将到', 'X4' in [x[0] for x in 将])
    T('⑥（1027 改）旧式「延：<由>」无数 → 作未延、照拦（旧式只报⚠）', 'X5' in 号到 and not [x for x in 到 if x[0] == 'X5'][0][4])
    T('⑥之二 旧式之延而原限未到 → 不拦（放行之反例）', 'X14' not in 号到 and not 病['X14'])
    T('⑦已治之节不读（其无期者亦不判）', 'Y1' not in 号到 and 'X99' not in 号到)
    T('⑦之二（复核补）X 行挪进「## 挂起」之类他节 → 照未治判（⛔挪节而逃）：无期者⛔、到期者⛔', 'X15' in 号到 and '取不出章号' in 病['X15'] and 'X16' in 号到)
    T('⑩「401 大审前」下一章 401 未到、402 即到（大审於 401 封後开）', 'X7' not in 号到 and 'X7' in [x[0] for x in 判(402, 文)[0]])
    T('⑧远者（一段之内）不报', 'X6' not in 号到 and 'X6' not in [x[0] for x in 将])
    T('⑧之二（1106 进化主义）原限远逾一段（420 之於 401）→ 即⛔（⛔远挂）；已延者照延上判（X10 不因此红）', 'X19' in 号到 and '限远逾一段' in [x[5] for x in 到 if x[0] == 'X19'][0]
      and 'X10' not in 号到)
    T('⑪裸「408」作「408 前」：下一章 408 即到、407 未到（旧式不判·X57 之漏）',
      'X8' in [x[0] for x in 判(408, 文)[0]] and 'X8' not in [x[0] for x in 判(407, 文)[0]] and 'X8' in [x[0] for x in 判(407, 文)[1]])
    T('⑫「延至 420 段前：由」→ 判以新限：401 不拦、420 即到且标已延', 'X10' not in 号到
      and [x for x in 判(420, 文)[0] if x[0] == 'X10'][0][4] is True)
    T('⑬二延（两回「延至」，或新旧各一）→ 即⛔，不论限到否', 'X11' in [x[0] for x in 判(380, 文)[0]] and 'X12' in [x[0] for x in 判(380, 文)[0]]
      and '一条至多一延' in 病['X11'] and '一条至多一延' in 病['X12'])
    T('⑭「延至 420 段前：」无由 → ⛔（延须有由）', 'X13' in 号到 and '无由' in 病['X13'])
    T('⑭之二「延至 999」逾原限二十章 → ⛔（无期之口）；恰二十章（401→421）→ 放', 'X17' in 号到 and '逾原限' in 病['X17']
      and 'X18' not in 号到 and not 病['X18'])
    T('⑭之三 引块（行首「>」）之 X 行⛔算活账（机制体检账 65：器把引文读成活挂账）——真账只在表里', 'X98' not in 号到 and 'X98' not in 病)
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, '设定'))
        open(os.path.join(d, '设定', '瑕疵总账.md'), 'w', encoding='utf-8').write(文)
        拦, L = 印(d, 401)
        T('⑨印：有到期即拦，并印治法（「延至 NNN」之式）', 拦 and L[0].startswith('⛔') and any('延至 NNN' in x for x in L))
        open(os.path.join(d, '设定', '瑕疵总账.md'), 'w', encoding='utf-8').write(
            '## 未治\n| X1 | 甲 | s | t | 430 段前 |\n| X2 | 乙 | s | t | 无限：全书写完後之二稿 |\n## 已治\n')
        拦, L = 印(d, 421)
        T('⑨之二 印：俱未到 → 放（✓）', not 拦 and L[0].startswith('✓'))
    # ⑮回灌旧树：db52f247 之瑕疵总账（X41「W11 各该节」、X57「408」、X43／X50 旧式之延）——新判须红其四，旧判只红 X17 等
    try:
        import subprocess
        旧 = subprocess.run(['git', 'show', 'db52f247:设定/瑕疵总账.md'], cwd=ROOT, capture_output=True, text=True)
        if 旧.returncode == 0:
            旧到 = [x[0] for x in 判(411, 旧.stdout)[0]]
            T('⑮回灌旧树（db52f247）：X41（W11 无期）、X57（裸 408）、X43、X50（旧式之延）俱⛔', all(k in 旧到 for k in ('X41', 'X57', 'X43', 'X50')))
        else:
            print('  · ⑮旧树不在（浅克隆）——略')
    except Exception as e:
        print('  · ⑮回灌略：%s' % e)
    # ⑯〔执行之制·治11〕换号不重计延：承旧号者合计其延
    文承 = ('## 未治\n| X30 | 记占又逾（478） | 复盘；承 X20 | t | 490 前 |\n| X31 | 他病承 X21（470） | s | t | 490 前 |\n'
           '| X32 | 承 X22 而自延 | s | t | 401 前（延至 420 前：候其器之落） |\n'
           '## 已治\n| X20 | 记占逾（463） | 承 X10、X11 | 已治 | 470 前 |\n| X21 | 旧（455） | s | 已治 | 470 前 |\n| X22 | 旧 | s | 已治 | 400 前 |\n'
           '| X10 | 记占逾（455） | s | 已治 | 460 前 |\n| X11 | 记占逾（460） | s | 已治 | 462 前 |\n')
    病承 = {x[0]: x[5] for x in 诸条(文承)}
    延承 = {x[0]: x[4] for x in 诸条(文承)}
    T('⑯ 承链合延：X30 承 X20（承 X10、X11）→ 合延 3 ⛔再延（换号不重计）', '承 X20、X10、X11 合延 3' in 病承['X30'])
    T('⑯之二 只承一旧号（未延）→ 作已延一回、限未到不拦', not 病承['X31'] and 延承['X31'] is True and 'X31' not in [x[0] for x in 判(483, 文承)[0]])
    T('⑯之三 承一号而自延一回 → 合二 ⛔', '一条至多一延' in 病承['X32'])
    T('⑯之四 同类之印：「同类连 N 章逾：前治 … 无效」只印', any('X30 承' in x and '同类连 24 章逾' in x for x in 同类之印(文承)))
    try:                                                     # ⑰回灌 a6c9f7a04（执行之审之 HEAD）之瑕疵总账：X117 补书「承 X112、X109」→ 计已延二、判红
        import subprocess
        旧 = subprocess.run(['git', 'show', 'a6c9f7a04:设定/瑕疵总账.md'], cwd=ROOT, capture_output=True, text=True)
        if 旧.returncode == 0 and re.search(r'^\| X117 \|', 旧.stdout, re.M):
            灌 = re.sub(r'^(\| X117 \|[^|]*)\|', lambda m: m.group(1) + '（承 X112、X109）|', 旧.stdout, count=1, flags=re.M)
            病灌 = {x[0]: x[5] for x in 诸条(灌)}
            T('⑰回灌 a6c9f7a04：X117 承 X112、X109 → 合延二、判红（旧只印「已延一回」）',
              'X117' in 病灌 and '合延 2' in 病灌['X117'] and 'X117' in [x[0] for x in 判(474, 灌)[0]])
        else:
            print('  · ⑰旧树不在（浅克隆）——略')
    except Exception as e:
        print('  · ⑰回灌略：%s' % e)
    # ⑱〔执行之制·治14〕哨红未入账：费哨连两段红、无估累三、无由累三 → 印；添「X1xx 承 费哨…限 480」→ 消
    _账14 = '## 未治\n| X1 | 甲 | s | t | 490 前 |\n## 已治\n| X2 | 旧 | 承 费哨 | 已治 | 470 前 |\n'
    _哨 = 哨红未入账(文=_账14, 两段=[(True, 0.48), (True, 0.36)], 无估无由=([('a', '', 1.0)] * 3, [('b', '', 2.0)] * 2))
    T('⑱ 哨红未入账：连两段红、无估累三 → 印二条（无由累二 ⛔印；已治之「承 费哨」⛔销）',
      len(_哨) == 2 and '连两段红' in _哨[0] and '无估之件累 3' in _哨[1])
    T('⑱之二 只一段红 → ⛔印', not 哨红未入账(文=_账14, 两段=[(True, 0.48), (False, 0.8)], 无估无由=([], [])))
    _账14b = _账14.replace('## 已治', '| X140 | 费之占连两段逾界 | 承 费哨 | 治 | 480 前 |\n## 已治')
    T('⑱之三 添「X140 承 费哨…限 480」→ 消', not 哨红未入账(文=_账14b, 两段=[(True, 0.48), (True, 0.36)], 无估无由=([('a', '', 1.0)] * 3, [])))
    import tempfile as _tf
    with _tf.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, '设定'))
        open(os.path.join(d, '设定', '瑕疵总账.md'), 'w', encoding='utf-8').write(_账14)
        import 费哨 as _哨器
        _旧两段, _旧无 = _哨器.两段, _哨器.无估无由
        _哨器.两段 = lambda root=None, 件=10, 行=None: [(True, 0.48), (True, 0.36)]
        _哨器.无估无由 = lambda root=None, 行=None: ([], [])
        try:
            拦a, La = 印(d, 哨账之拦起 - 1)
            拦b, Lb = 印(d, 哨账之拦起)
        finally:
            _哨器.两段, _哨器.无估无由 = _旧两段, _旧无
        T('⑱之四 先只报三章：下一章 %d 只印 ⚠（⛔拦）、%d 起入到期而拦' % (哨账之拦起 - 1, 哨账之拦起),
          not 拦a and any('哨红未入账' in x and '⚠' in x for x in La) and 拦b and any('哨红未入账' in x for x in Lb))
    # ⑲〔W919 环14〕号撞：一号二行（诸节俱计、引块⛔计）→ 撞；印只 ⚠ ⛔拦；新号＝诸账之末号＋1＋余三；跨枝同号异条 → 撞（同条移已治、行首〔原号〕之注 ⛔异）；
    #   号之集：主枝 ∪ 在飞之 章-*／治-*（已并入主枝者⛔计）；--号 列本号、「原号」之行与工具之活引
    _账19 = ('## 未治\n| 号 | 缺 | 源 | 主 | 限 |\n|---|---|---|---|---|\n| X5 | 甲之病甚长甚长甚长 | s | t | 490 前 |\n| X7 | 乙之病 | s | t | 490 前 |\n'
            '> | X5 | 引块之行 | s | t | 490 前 |\n## 已治（1015）\n| X7 | 丙之病 | s | 已治 |\n| X9 | 〔原号 X5·号撞（二坐同取）·W919 改号〕丁之病 | s | 已治 |\n')
    T('⑲ 号撞：X7 一号二行（未治、已治各一）→ 撞；引块之 X5 ⛔计', 号撞(_账19) == {'X7': [5, 8]})
    T('⑲之二 新号＝末号＋1＋余三；集之号亦计', 新号({}, _账19) == 'X13' and 新号({'r': {'X20': ['x']}}, _账19) == 'X24' and 号余 == 3)
    T('⑲之三 条之首去行首〔原号〕之注；跨枝：同号异条 → 撞、同条（移已治亦同）→ 静、本账重号者⛔重计',
      条之首('| X9 | 〔原号 X5·号撞〕丁之病 | s |') == '丁之病' and 跨枝之撞(_账19, {'refs/remotes/origin/章-9': {'X5': ['他坐之条'], 'X9': ['丁之病']}})
      == [('X5', '甲之病甚长甚长甚长', 'refs/remotes/origin/章-9', '他坐之条')] and 跨枝之撞(_账19, {'r': {'X5': ['甲之病甚长甚长甚长'], 'X7': ['他']}}) == []
      and 跨枝之撞(_账19, {'refs/remotes/origin/主': {'X5': ['甲之病甚长甚长甚长', '丁之病']}}) == [])     # 主枝尚有旧撞（本账已改号）⛔重报
    import tempfile as _tf19, subprocess as _sp19
    with _tf19.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, '设定'))
        open(os.path.join(d, '设定', '瑕疵总账.md'), 'w', encoding='utf-8').write(_账19)
        _拦19, _L19 = 印(d, 480)
        _有19, _撞L = 撞号之印(d, 文=_账19, 集={})
        T('⑲之四 印：号撞只 ⚠（⛔拦·到期照判）；--撞号 有撞即有', not _拦19 and any('⚠ 号撞 X7' in x and '⛔拦派' in x for x in _L19) and _有19
          and any('号撞 X7' in x for x in _撞L) and 撞号之印(d, 文=_账19.replace('| X7 | 丙之病', '| X8 | 丙之病'), 集={})[0] is False)
        _e19 = dict({k: v for k, v in os.environ.items() if not k.startswith('GIT_')}, GIT_CONFIG_GLOBAL=os.devnull, GIT_AUTHOR_NAME='t',
                    GIT_AUTHOR_EMAIL='t@t', GIT_COMMITTER_NAME='t', GIT_COMMITTER_EMAIL='t@t')
        _g = lambda *a: _sp19.run(['git'] + list(a), cwd=d, capture_output=True, text=True, env=_e19)
        _g('init', '-q'); _g('add', '-A'); _g('commit', '-qm', 'a')
        _g('update-ref', 'refs/remotes/origin/主', 'HEAD'); _g('update-ref', 'refs/remotes/origin/章-1', 'HEAD')
        open(os.path.join(d, '设定', '瑕疵总账.md'), 'w', encoding='utf-8').write(_账19 + '| X11 | 在飞之条 | s | 已治 |\n')
        _g('commit', '-qam', 'b'); _g('update-ref', 'refs/remotes/origin/治-abc', 'HEAD')
        _集19, _败19 = 号之集(d, 取=False, 枝='主')
        T('⑲之五 号之集（⛔取）：主枝 ∪ 在飞之 治-*；已并入主枝之 章-* ⛔计；末号随在飞之号',
          set(_集19) == {'refs/remotes/origin/主', 'refs/remotes/origin/治-abc'} and not _败19 and 'X11' in _集19['refs/remotes/origin/治-abc']
          and 新号(_集19) == 'X15')
        os.makedirs(os.path.join(d, '工具'))
        open(os.path.join(d, '工具', 'a.py'), 'w', encoding='utf-8').write('# ★X5（某治）\n# X51 ⛔\n')
        _引19 = 号之引('X5', d, _账19)
        T('⑲之六 --号：本号之行、「原号 X5」之行、工具之活引（X51 ⛔混）', len(_引19) == 3 and any(':4　| X5' in x for x in _引19)
          and any(':9　' in x for x in _引19) and any('a.py:1' in x for x in _引19) and not any('a.py:2' in x for x in _引19))
    _主19 = open(os.path.abspath(__file__), encoding='utf-8').read().split("if __name__ == '__main__':")[-1]
    T('⑲之七 --新号 fetch 不成即⛔出号（rc 2）；--撞号 有撞 rc 1', "sys.exit(2)" in _主19.split("'--新号'")[1].split("'--号'")[0]
      and 'sys.exit(1 if 有 else 0)' in _主19)
    ok = sum(v for _, v in r)
    print('账限哨·自测 %d/%d%s' % (ok, len(r), ' 全通' if ok == len(r) else ' 未过'))
    return ok == len(r)


if __name__ == '__main__':
    if '--自测' in sys.argv[1:]:
        sys.exit(0 if 自测() else 1)
    if sys.argv[1:] == ['--撞号']:
        有, L = 撞号之印()
        print(('⛔ 号撞：\n' if 有 else '✓ 号撞 0\n') + '\n'.join(L))
        sys.exit(1 if 有 else 0)
    if sys.argv[1:] == ['--新号']:
        _集, _败 = 号之集()
        _本 = open(os.path.join(ROOT, '设定', '瑕疵总账.md'), encoding='utf-8').read()
        if _败:
            print('⛔ fetch 不成（限 %d 秒）——号取不得：⛔改号（入主时取不得即只入器、号撞照印 ⚠）' % 号之取限)
            sys.exit(2)
        print('%s（诸账之末号 X%d·origin/主 ∪ 近 %d 个 章-*／治-*；留余 %d）' % (新号(_集, _本), 末号(_集, _本), 号之枝数, 号余))
        sys.exit(0)
    if len(sys.argv) == 3 and sys.argv[1] == '--号' and re.fullmatch(r'X\d+', sys.argv[2]):
        print('\n'.join(号之引(sys.argv[2])) or '（无）')
        sys.exit(0)
    拦, L = 印()
    print('\n'.join(L))
    sys.exit(1 if 拦 else 0)
