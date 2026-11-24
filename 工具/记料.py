#!/usr/bin/env python3
"""记料（1015 立·W33）——零 token：把记席九件事要翻的诸账之相关段一次汇成一档，记席一回读毕、⛔逐档翻找。

为何立：W24／W27／W31 三份复盘皆点「记席居诸席之首」（386 $5.26／45 回→387 $5.64／51 回→388 $6.09／63 回）；
  1015 量 388 记席之 63 回：取证与翻账 26、跑器 14、其他 14、写 6、读 3——四成回数花在逐份翻找
  「前章回执之式、施工表 N-1 之锁定行与悬账、全书记忆五档之相关段、轮记与行家评、圣经之锚、检察官之行、下一章之段案与总纲」，
  每翻一回重读整份上下文（坑㉚ 之同类：席以零碎之活办多档）。执笔有章料（一档汇齐），记席无——本器即记席之章料。
⛔限：只汇、⛔判；所汇皆逐字抄自盘上之档（章:行可查）；封版.py N --前 之印⛔汇（其有存版之副作用，记席自跑）。

★1020 W53·X15（记席之费在读：392 记席 $4.73；394 长章之记料 161KB 逾 150KB 拦封版，瘦後余量仅 5KB——料随章长与在场人数而涨）之结构之治：
  ①节之界：十二节各有其界（`界`），逾界即截於行界、印其所略与全文之路；Σ界＋诸题 < 限——记料之长与章长、在场人数脱钩（自测以「八倍之章、全册之人」回灌钉之）。
  ②各节之用（据 397 记席之席记「料缺」与 397 封版对全书记忆四档之 diff）：
     去其不用——用法首六十行（读者调取之法）→§五规矩、§六之式（记席照之写第N章.md，旧反不汇）｜总览首十四行（一页之要、按站，记席不改）→今站一块与锚行｜
       前章创作记录首三十行→每节首二行｜前章席记（令已给其式）｜轮记首十行→轮记、行家评之目（带行号；记席本须全读）、构思之档｜
       悬线钉 N—N+3 之整行（一行一二千字）→钉 N、N+1 之处各摘其旁。
     留而改之——同线前章之白文（冷眼轮所冷读者即此章，392—397 回执俱书「记料十节逐字汇入」）加行号（旧无行号，冷眼轮、承前之判引 章:行 另 grep）。
     补其所缺——前章回执每节首三行（旧只首四十行，§四以下另 sed）｜施工表本章硬门槛整节（旧只其头三行）｜open_brief 全块（旧截四千）｜
       检察官 OPEN_BRIEF_CARD_SCHEMA 之行（旧式「^ N:」认不着四格缩进，向来空）｜在场之人（旧以 str(别称) 拆，list 之称全认不着、暗线之「她」恒零——395、397 五、十一两节空）｜
       全书记忆四档之锚行｜state_canon 一卡之式｜大师进化账末三行。
  ③所引之档之「#」行一律加「〉」——旧式引回执、轮记之「## 八·…」与记料自家之「## 八·…」同形，记席按节找料即撞错节；记料自家之节作「## 【八】…」。
  ④（独立验席所逮·【九】之界与段案之取相撞）段案之取止於任一「## 」（旧连附一、附二取入：399 之【九】16KB 截去总纲、余章 400 之行）；
     多源之节锚行短行在前、式样长档殿後（【四】【八】【九】），逾界之注只列被截诸片之源（旧只一源，注指错档）；【八】锚行⛔重印。

★1020 X36（398 记席 flaws③、399 记席另报：四样料外另 sed／grep）之补——各补入其最近之节之尾，⛔新立节（仍十二节）：
  ①【七】诸构思之「## 满分之问」全段（399 记席：甲、己、庚三份另 sed）——三种写法与其比在前、拍表殿後（截自尾起，先截拍表；带行号）；
  ②【二】同镜前章之「| N | 悬账 |」行（398 记席：上一同镜章之悬账另翻）——其章与【十】同取 _承前之章（开镜庭之尺·X43⑧：
     旧自家 _同镜 以六十章窗另判，遇镜未钉之章越过去取远章，与【十】分岔；今一尺）（X34：399 黎东来镜之同镜前章係 389，⛔397）；
     同镜取不着者照旧取同线；同镜即 N-1 者其行已在上、⛔重印；
  ③【八】本章卡与下一章卡里「圣经:NNNN」（连「、:NNNN」「—NNNN」）所指之行——锚行、前章之条已印者⛔重印；
  ④【五】【十一】卡·问九之二所列之人（399 记席：管章的人只以纸到场，【五】只认白文、状态册与人物.md 另 grep）——
     收「- **名**」之头与注里之称（「不回」「⛔在场」之句⛔收）与白文出现之人之并；册无其人者列其名。
  界：补殿旧体之後，旧体先截於其旧界——旧节之所收一字不让；补之额取诸节未用之界（池＝Σ界−Σ旧体之实），依 补序 分，各补又有其顶（补界）；
     全档 ≤ Σ界＋头 ＜ 限——头注之总界不动（自测压测量之）。逾额即截、印其所略与其源（「（本节逾界·补额」）。
  驳席所逮（1020）：①构思作「② ## 满分之问」「② 满分之问」者（386—397 十八份，圈号起行）旧认不着、印「无满分之问之节」→ _满分之段 兼认；
     ③「`圣经：7408`／`:8161`」之续引（334、335、353 之卡）旧只认首号→兼认「／」与反引号；自测补「镜：我」之归一（396→394）。

★1021 W60·X42（400 记席 flaws②：【九】余章之行漏收 401——余章:66 末「401 暗 她循牌纹到同一条街」接在 400 之行末；卡所须之前章白文另 awk）：
  ①【九】余章总案之条以「N 主／N 暗」（连「419／421／423 暗」「430—434 主」）在行内认、一条归一章（⛔只认行首「- N 」；旧之行首仍认）——
     条之起：行首之「- 」（连缩进之子条）或句读（。！？；〕」』）｜）之後；「主线」「暗线」⛔认；本章与下一章之条俱汇（记席核本章、立下一章之卡）。
  ②【十】之补：本章卡、下一章卡、open_brief 所引之远章「章:行」「章:行—行」以 章料.引之原句 展其原句（⛔另造一法；只留章之引——总纲、余章总案之行【九】已汇）；
     【十】白文已全收（未逾界）之章只列其号；越章长之行⛔展、⛔崩；无同线前章白文而有远引者【十】仍立（注其由）。补序 十 在 七 前（先短後长）。
     ★X43⑧：换镜之章（同镜前章非同线前章）【十】并附同线前章之末五段（带行号·开轮⑮所比之收句之骨）——旧⛔附，记席另 sed -n 读。
  W60 席四之驳所留二病（1021）：
  ③【十】之选章与开镜庭接钩同尺（_承前之章：import 第零轮开镜庭 之 _同镜之前，⛔另抄一把）——换镜之暗线章取同镜之前
     （401 沈鸢镜→397，⛔同线之 399 黎东来镜；399→389）；主线照取同线（400→398、398→396，其料一字不变）；
     import 败、线／镜未定、_同镜之前 返 None 者照旧取同线，【十】节首印一行「承前取同线·镜未定之由」。
     ⚠开轮⑮仍比同线前章——换镜之章其同线前章之末五段附於【十】之尾（X43⑧）；全文要之者 sed -n 读。
  ④自测⑳㉑改以造局（注入之串、tempdir 之盘）测行中之认、行首之认、401 独行与接在 400 行末；真档只余「401 之料含 401 之条」一格冒烟
     （余章总案将由 401 段剧情庭改写——⛔钉行号与字面）；补 lookahead 之格（「。390 主线」⛔切）与远源三路（本章卡、下一章卡、open_brief）各一格。

用法：
  python3 工具/记料.py N          # → 版本/第N章/_记料.md
  python3 工具/记料.py --自测
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import os, sys, re, glob, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
表 = os.path.join('设定', '01_镇冢秘术_逐章施工与伏笔回收表.md')
记 = os.path.join('设定', '全书记忆')
册档 = os.path.join('设定', '人物状态册.json')
限 = 150 * 1024
# ★1020 X15·节之界（字节）：Σ 145,500＋诸题与逾界之注（≤ 头之界，自测压测量之）＜ 限 153,600——结构上逾不了
#   验席所逮後调：九 16000→20000（W54 段案一章之节至 15KB：398 之节＋余章 398 之行＝17.7KB）｜
#   十 14000→15000（近百章同线白文带行号之顶 360 之 13038，旧余 7%）｜三 4000→3500（385—399 之顶 2694）
界 = {'一': 13000, '二': 17000, '三': 3500, '四': 18000, '五': 6000, '六': 12000,
      '七': 4000, '八': 14000, '九': 20000, '十': 15000, '十一': 17000, '十二': 6000}
头之界 = 6000
# ★1020 X36·补之顶（字节）：补不入 Σ界——其额取诸节未用之界（池＝Σ界−Σ旧体之实，依 补序 先短後长），故全档仍 ≤ Σ界＋头＜限。
#   顶据其实：七 满分之问 385—399 之顶 399 七份 35.1KB（三种写法 10.0KB＋拍表 25.2KB）｜二 悬账行一行之顶 317 之 9.0KB
#   （385—399 之顶 394 之 5.2KB；363、365 之 7—8KB 行逾 6000 即整行截去——截於行界）｜八 卡引圣经 0—3 行（1722 一行 1.6KB）｜
#   五、十一 卡·问九之二所列而白文未见者 0—2 人
#   ★1021 X42·十 卡与 open_brief 所引远章之原句（章料.引之原句）：399 之 13.1KB、400 之 13.2KB、401 之 9.5KB
补界 = {'一': 4500, '八': 6000, '二': 9500, '五': 3000, '十一': 5000, '十': 14000, '七': 45000}
补序 = ('一', '八', '二', '五', '十一', '十', '七')


def 读(p, root=ROOT):
    p = os.path.join(root, p)
    if not os.path.exists(p):
        return ''
    b = open(p, 'rb').read()
    try:
        return b.decode('utf-8')
    except UnicodeDecodeError as e:
        # ★X116（469）：467 之 _轮记.md 被某席之落档截在字节、末字残——旧以 utf-8 读之即崩、记席手去残字节方续。
        #   残在档尾（≤3 字节之不全之字）：轮记之档就地去残、印一行；余处之坏照 replace 读（⛔崩）。
        if e.start >= len(b) - 3 and e.reason == 'unexpected end of data':
            t = b[:e.start].decode('utf-8')
            if os.path.basename(p) == '_轮记.md':
                open(p, 'wb').write(b[:e.start])
                sys.stderr.write('⚠ X116 %s 档尾残 %d 字节（截於字节）——已就地去残；其末节或缺尾，记席照实记\n' % (p, len(b) - e.start))
            return t
        return b.decode('utf-8', errors='replace')


def 行们(文, 式, 上=0, 下=0, 最多=None):
    """文里合式之行（连上下文），带行号。"""
    L = 文.split('\n'); 出 = []; 已 = set()
    for i, l in enumerate(L):
        if re.search(式, l):
            for k in range(max(0, i - 上), min(len(L), i + 下 + 1)):
                if k not in 已:
                    已.add(k); 出.append('%d｜%s' % (k + 1, L[k]))
            if 最多 and len(出) >= 最多:
                break
    return '\n'.join(出)


def 引(t):
    """★1020 X15③：所引之档之「#」行加「〉」——⛔与记料自家之节同形。"""
    return '\n'.join(('〉' + l) if l.startswith('#') else l for l in (t or '').split('\n'))


def _截(片们, k):
    """★1020 X36（自 节 析出，旧节与补同尺）：片们 [(源, 片)] 依序以空行相接；逾 k 字节截於行界 →
    (留, 略)；略 = None 或 (下略之行数, 下略之字节, [被截诸片之源])。"""
    片们 = [(s, (t or '').strip()) for s, t in 片们 if (t or '').strip()]
    体 = '\n\n'.join(t for _, t in 片们)
    if len(体.encode()) <= k:
        return 体, None
    留 = 体.encode()[:k].decode('utf-8', 'ignore')
    if '\n' in 留:
        留 = 留[:留.rfind('\n')]
    略 = 体[len(留):].strip('\n')
    略源, 止 = [], -2
    for s, t in 片们:
        止 += 2 + len(t)
        if 止 > len(留) and s and s not in 略源:
            略源.append(s)
    return 留, (略.count('\n') + 1, len(略.encode()), 略源)


def _片们(体, 源=''):
    return [(源, 体)] if not isinstance(体, list) else 体


def 节(号, 标, 体, 源='', 补=None, 补额=0):
    """★1020 X15①：一节一界——逾界截於行界，印其所略与所略之源（缺者 sed -n 补）。
    体：str（一源，源即其档）或 [(源, 片)]（多源之节：片依序以空行相接；注只列被截诸片之源——
    X15 验席逮：旧只收一源，【九】截在总纲、余章总案而注写段案，记席照注 sed 找不回）。
    多源之节，式样与长档殿後、锚行与短行在前——截自尾起，先截者须是全文最易补者。
    ★1020 X36：补 [(源, 片)] 殿旧体（与其逾界之注）之後，自截於 补额——旧体之截只看旧界，补⛔挤旧。"""
    k = 界[号]
    体, 略 = _截(_片们(体, 源), k)
    体 = 体 or '（无）'
    if 略:
        体 += '\n（本节逾界 %d 字节：下略 %d 行、%d 字节%s——缺者 sed -n 补）' % (
            k, 略[0], 略[1], ('；所略之源 ' + '、'.join(略[2])) if 略[2] else '')
    if 补:
        补体, 补略 = _截(补, 补额)
        if 补体:
            体 += '\n\n' + 补体
        if 补略:
            体 += '\n（本节逾界·补额 %d 字节：补下略 %d 行、%d 字节%s——缺者 sed -n 补）' % (
                补额, 补略[0], 补略[1], ('；所略之源 ' + '、'.join(补略[2])) if 补略[2] else '')
    return '\n## 【%s】%s\n\n%s\n' % (号, 标, 体)


def _用(号, 体, 源=''):
    """旧体截於其界後之实（字节·不计逾界之注）——补之池 ＝ Σ界 − Σ此。"""
    return len(_截(_片们(体, 源), 界[号])[0].encode())


def 段(文, 头式, 起=0):
    """文里（自第 起 行·0 起）首个合「头式」之「#」行起之一段（至下一个同级以上之「#」行止），带行号。"""
    L = 文.split('\n')
    for i, l in enumerate(L):
        if i >= 起 and l.startswith('#') and re.search(头式, l):
            级 = len(l) - len(l.lstrip('#'))
            j = i + 1
            while j < len(L) and not (L[j].startswith('#') and len(L[j]) - len(L[j].lstrip('#')) <= 级):
                j += 1
            return '\n'.join('%d｜%s' % (k + 1, L[k]) for k in range(i, j)).rstrip()
    return ''


def 块(文, i):
    """文之第 i 行（0 起）起之一块「- **…」（至下一个顶格之「- 」或「#」止），带行号。"""
    L = 文.split('\n')
    j = i + 1
    while j < len(L) and not L[j].startswith(('- ', '#')):
        j += 1
    return '\n'.join('%d｜%s' % (k + 1, L[k]) for k in range(i, j)).rstrip()


def _号段(号们):
    """[9924, 9925, 9926, 9930] → '9924—9926、9930'。"""
    出 = []
    for x in sorted(set(号们)):
        if 出 and x == 出[-1][1] + 1:
            出[-1][1] = x
        else:
            出.append([x, x])
    return '、'.join(('%d' % a) if a == b else '%d—%d' % (a, b) for a, b in 出)


def 截(s, k):
    s = str(s)
    return s if len(s) <= k else s[:k] + '…（下略 %d 字）' % (len(s) - k)


def 行截(t, k=300):
    """式样与锚行之每行截 k 字（记席改其档须先 Read 其行——此只给式与行号，⛔整行抄两回）。"""
    return '\n'.join(截(l, k) for l in (t or '').split('\n'))


def 章白(n, root=ROOT):
    import 章料
    f = 章料.章档(n, root)
    if not f:
        return '', ''
    t = open(f, encoding='utf-8').read()
    return f, t.split('【本章亮点】')[0]


def _白行(n, root=ROOT):
    """(档之相对路, [(行号, 行)])——第 n 章白文（【本章亮点】之前）之非空行，行号即整档之行（与 awk NR 同）。"""
    import 章料
    f = 章料.章档(n, root)
    if not f:
        return '?', []
    L = open(f, encoding='utf-8').read().split('【本章亮点】')[0].split('\n')
    return os.path.relpath(f, root), [(i + 1, l) for i, l in enumerate(L) if l.strip()]


def _节首(t, k):
    """★1016（393 封版逮：记料 156KB 逾 150KB；X15 记席之费在读）：前章之档只作式样——每「## 」节留首 k 行，余印其数。"""
    出, 节行 = [], 0
    for l in t.split('\n'):
        if l.startswith('## '):
            if 节行 > k:
                出.append('（本节下略 %d 行）' % (节行 - k))
            出.append(l); 节行 = 0; continue
        节行 += 1
        if 节行 <= k:
            出.append(l)
    if 节行 > k:
        出.append('（本节下略 %d 行）' % (节行 - k))
    return '\n'.join(出)


# ── 在场之人（★1020 X15：旧以 str(别称) 拆——别称是 list，拆出「['她（…）'」，名表之称全认不着；暗线之「她」恒零）──
_泛 = re.compile(r'^(?:一个|那个|这个|那|这)?(?:人|女人|男人|汉子|孩子|老人|后生|姑娘)$')


def _称们(v):
    """名与别称：去括注、拆「甲/乙」、二字以上。"""
    al = v.get('别称') or []
    if isinstance(al, str):
        al = re.split(r'[、，,]', al)
    出 = []
    for x in [v.get('名') or ''] + list(al):
        x = re.sub(r'（[^）]*）|\([^)]*\)', '', str(x)).strip()
        出 += [y.strip() for y in re.split(r'[／/]', x) if len(y.strip()) >= 2]
    return 出


def _镜(白):
    """三值（与 看官._线 同尺）：主（我≥3/千）｜她｜他。"""
    w = len(re.sub(r'\s', '', 白)) or 1
    if 白.count('我') / w * 1000 >= 3:
        return '主'
    return '她' if 白.count('她') >= 白.count('他') else '他'


def 在场(白, N, 册):
    """[(名, 所见之称, 册行)]：①别称注「主线第一人称」「暗线章通篇只作『她』」者，其镜之章必在场；
    ②名（去括注、非泛称）见於白文；③别称（三字以上、非泛称）见於白文且末见章在三十章内。
    （1020 量 385—397：以「N态」为真——旧 认中 31／漏 23／误 0，今 认中 44／漏 10／误 1。）"""
    if not 白:
        return []
    镜 = _镜(白)
    出 = []
    for v in (册.get('人物') or [] if isinstance(册, dict) else []):
        if not isinstance(v, dict):
            continue
        注们 = []
        for x in (v.get('别称') if isinstance(v.get('别称'), list) else []):
            m = re.search(r'（([^）]*)）', str(x))
            if m:
                注们.append(m.group(1))
        称们 = _称们(v)
        if any(('第一人称' in z and 镜 == '主') or ('通篇' in z and '她' in z and 镜 == '她') for z in 注们):
            出.append((v.get('名'), ['（%s之镜·通篇）' % 镜], v)); continue
        if 称们 and not _泛.match(称们[0]) and 称们[0] in 白:
            出.append((v.get('名'), [称们[0]], v)); continue
        m = re.match(r'\d+', str(v.get('末见章') or ''))
        近 = bool(m) and int(m.group()) >= N - 30
        中 = [x for x in 称们[1:] if len(x) >= 3 and not _泛.match(x) and x in 白]
        if 近 and 中:
            出.append((v.get('名'), 中, v))
    return 出


def _册之区(名, root=ROOT):
    """人物状态册.json 里此人之行区（起—止，1 起）。"""
    L = 读(册档, root).split('\n')
    头 = [i for i, l in enumerate(L) if re.match(r'^   "名": ', l)]
    for k, i in enumerate(头):
        if L[i].strip().rstrip(',') == '"名": %s' % json.dumps(名, ensure_ascii=False):
            止 = (头[k + 1] - 2) if k + 1 < len(头) else len(L)
            return i, 止
    return None


def _册行(v):
    """去旧态、留末一态（截五百字）；余串截二百字、列只留末二条（前略之数印出）——全行看其区。"""
    态 = sorted([x for x in v if re.match(r'\d+态$', x)], key=lambda x: int(re.match(r'\d+', x).group()))
    出 = {}
    for k, x in v.items():
        if re.match(r'\d+态$', k) and k not in 态[-1:]:
            continue
        if isinstance(x, list):
            出[k] = (['（前 %d 条略）' % (len(x) - 2)] if len(x) > 2 else []) + [截(y, 120) for y in x[-2:]]
        elif isinstance(x, str):
            出[k] = 截(x, 500 if re.match(r'\d+态$', k) else 200)
        else:
            出[k] = x
    出['（旧态）'] = '、'.join(态[:-1][-6:]) + ('等 %d 态' % len(态[:-1]) if len(态) > 7 else '')
    return json.dumps(出, ensure_ascii=False)


def _段案(n, root=ROOT):
    """第 n 章之段案之节 → (档之相对路, 节文, [段头与附录诸节之目 :起—止])——取至任一「## 」止。
    ★1020 X15 验席：旧式止於「## 数」，各段案档末一章连其後「## 附一·落账」「## 附二·…」一并取入（400 之节取成 16KB）。"""
    for p in sorted(glob.glob(os.path.join(root, '设定', '段案', '*.md'))):
        if os.path.basename(p).startswith('_'):
            continue
        L = open(p, encoding='utf-8').read().split('\n')
        末 = len(L) - (1 if L and L[-1] == '' else 0)
        头 = [i for i, l in enumerate(L) if l.startswith('## ')]
        for k, i in enumerate(头):
            if re.match(r'## %d\s*$' % n, L[i]):
                止 = 头 + [末]
                目 = ['段头 :1—%d' % 头[0]] + ['%s :%d—%d' % (L[a][3:].strip(), a + 1, 止[q + 1])
                                               for q, a in enumerate(头) if not re.match(r'## \d+\s*$', L[a])]
                return os.path.relpath(p, root), '\n'.join(L[i:止[k + 1]]).strip(), 目
    return '', '', []


# ★1118 总编辑复核「悬念哨→改」（改其供⛔改其判）：悬念哨之第二路只认回执之严式，而旧⛔一器教记席书之（461—467 四笔实落而失记·主环三回手补）
悬之令 = '如本章正文实落其拍，骨记（或回执）须书一行：SUS-X·本章复提：<拍号或逐字 ≥8 字>；未落者⛔书（⛔凭段案代正文）'


def _段案之悬(n, root=ROOT):
    """第 n 章段案之节（_段案 之取·至任一「## 」止）内提 SUS-A／SUS-B／SUS-C 之行 → (档之相对路, [(整档之行号, 行)])——逐字；无则 ('', [])。"""
    源, 文, _ = _段案(n, root)
    if not 文:
        return '', []
    L = open(os.path.join(root, 源), encoding='utf-8').read().split('\n')
    起 = next(i for i, l in enumerate(L) if re.match(r'## %d\s*$' % n, l))
    return 源, [(起 + 1 + j, l) for j, l in enumerate(文.split('\n')) if re.search(r'SUS-[ABC]', l)]


# ── ★1020 X36 之补 ──
def _满分之段(文):
    """一份构思之「满分之问」段（带行号）。★1020 X36 驳席逮：386—397 十八份构思作「② ## 满分之问」「② 满分之问」
    （圈号起行、非「#」行——造章令「② 一节「## 满分之问」」照抄），段 认不着，旧印「无满分之问之节」而实有；
    圈号起者止於下一圈号行或「#」行。"""
    s = 段(文, r'满分之问')
    if s:
        return s
    L = 文.split('\n')
    起 = next((i for i, l in enumerate(L) if re.match(r'^[①-⑳]\s*(?:#+\s*)?满分之问', l)), None)
    if 起 is None:
        return ''
    止 = next((j for j in range(起 + 1, len(L)) if re.match(r'^(?:#|[①-⑳])', L[j])), len(L))
    return '\n'.join('%d｜%s' % (k + 1, L[k]) for k in range(起, 止)).rstrip()


def _满分之问(构思, root=ROOT, 表只=None):
    """诸构思之「满分之问」全段（带行号）→ [(源, 片)]：三种写法与其比在前（每份一片），拍表（「|」起之行）殿後——截自尾起先截拍表。
    ★X97（446）表只：只此诸档附拍表（胜稿）；嫁大进之稿只给三种写法与其比（所嫁之拍行家评「## 大进」已载）。"""
    文们, 表们 = [], []
    干 = '甲乙丙丁戊己庚辛壬癸'
    for p in sorted(构思, key=lambda p: (干.find((re.search(r'起草_(.)_构思', p) or [None, ''])[1]) % 99, p)):
        rp = os.path.relpath(p, root)
        s = _满分之段(open(p, encoding='utf-8', errors='replace').read())
        if not s:
            文们.append((rp, '〔%s：无「满分之问」之节〕' % rp)); continue
        L = s.split('\n')
        表 = [l for l in L if l.split('｜', 1)[-1].startswith('|')]
        文 = [l for l in L if l not in 表]
        头 = '〔%s:%s—%s·满分之问%s〕\n' % (rp, L[0].split('｜')[0], L[-1].split('｜')[0], '（拍表 %d 行殿後）' % len(表) if 表 else '')
        文们.append((rp, 头 + 行截('\n'.join(文), 800)))
        if 表 and (表只 is None or p in 表只):
            表们.append((rp, '〔%s·满分之问之拍表〕\n' % rp + 行截('\n'.join(表), 800)))
    return 文们 + 表们


def _胜嫁之构思(构思, 章目, N, root=ROOT, 只胜=False):
    """★X95②：胜稿与嫁大进之稿之构思档。蒙号＝稿号[(干序+N) % 宽]（造章.js 蒙号）；行家评认不出胜稿即原样返。"""
    t = 读(os.path.join(章目, '_行家评.md'), root)
    def 节(h):
        m = re.search(r'^## %s.*?$(.*?)(?=^## |\Z)' % h, t, re.M | re.S)
        return m.group(1) if m else ''
    号 = '一二三四五六七'
    胜 = re.search('稿([%s])' % 号, 节('名次'))
    if not 胜:
        return 构思
    要 = {胜.group(1)} | (set() if 只胜 else set(re.findall('稿([%s])' % 号, 节('大进'))))
    干 = '甲乙丙丁戊己庚'
    宽 = len(构思)
    出 = [p for p in 构思 if (re.search(r'起草_(.)_构思', p) or [None, ''])[1] in 干
          and 号[(干.find(re.search(r'起草_(.)_构思', p)[1]) + N) % 宽] in 要]
    return 出 or 构思


def _轮记之审(p, root=ROOT, 末回=False):
    """★X91③：轮记中「## …盲读…」「## …逻辑审…」之节全文（带行号；至下一「## 」止）→ [(源, 片)]；无者 []。
    ★X97（446）末回=True：同类（盲读／逻辑审）有後回者，前回只留判行（soft／hard／读误／粗体之判·各截 200），全文注 sed -n——
    445 记席之料【七】二回逻辑审全节约 17KB、後回已复验前回之治。"""
    t = 读(p, root)
    if not t:
        return []
    L = t.split('\n'); 出 = []
    头们 = [i for i, l in enumerate(L) if l.startswith('## ')] + [len(L)]
    节们 = [(a, b) for a, b in zip(头们, 头们[1:]) if re.search('盲读|逻辑审', L[a])]
    类 = lambda a: '盲读' if '盲读' in L[a] else '逻辑审'
    for k, (a, b) in enumerate(节们):
        前 = 末回 and any(类(a2) == 类(a) for a2, _ in 节们[k + 1:])
        if 前:
            判 = [(i, l) for i, l in enumerate(L[a + 1:b], a + 1)
                  if re.match(r'\s*[-*]?\s*(\*\*|soft|hard|HARD|SOFT|读误|致命|结论|判)', l)]
            出.append((p, '〔补·%s:%d—%d·%s（前回·只留判行；全文 sed -n %d,%dp）〕\n' % (p, a + 1, b, L[a][3:].strip(), a + 1, b) +
                       '\n'.join('%d｜%s' % (i + 1, 截(l, 200)) for i, l in 判)))
        else:
            出.append((p, '〔补·%s:%d—%d·%s〕\n' % (p, a + 1, b, L[a][3:].strip()) +
                       '\n'.join('%d｜%s' % (i + 1, 截(l, 600)) for i, l in enumerate(L[a:b], a) if l.strip())))
    return 出


def _圣经之引(t):
    """「圣经：1950、:2644」「圣经：12—14」→ [1950, 2644, 12, 13, 14]（去重、依序；一段至多展八行）。
    ★1020 X36 驳席：334、335、353 之卡作「`圣经：7408`／`:8161`」（斜杠、反引号相隔）——旧只认首号；段尾小於段首（「:1950—52」）旧整段丢，今只取段首。"""
    号 = []
    for m in re.finditer(r'圣经[:：](\d+)(?:[—–-](\d+))?((?:`?\s*[、，,／/]\s*`?[:：]\d+(?:[—–-]\d+)?)*)', t or ''):
        for a, b in [(m.group(1), m.group(2))] + re.findall(r'[:：](\d+)(?:[—–-](\d+))?', m.group(3)):
            a = int(a)
            号 += list(range(a, min(int(b) if b and int(b) >= a else a, a + 7) + 1))
    return list(dict.fromkeys(号))


_不收 = re.compile(r'不回|⛔在场|不在场')


def _卡之人(卡, 册, 已):
    """卡·问九之二所列之人 → ([(名, [所见之称], 册之人)], [册无其人之头])：
    「- **名**」之头只认其名；注（他行）以「；。」分句，句含「不回」「⛔在场」者⛔收（399：录入的那个、接线的永不回）；已（白文所认之名）⛔重。"""
    L = (卡 or '').split('\n')
    起 = next((i for i, l in enumerate(L) if l.startswith('#') and '问九之二' in l), None)
    if 起 is None:
        return [], []
    止 = next((j for j in range(起 + 1, len(L)) if L[j].startswith(('#', '---'))), len(L))
    头们, 句们 = [], []
    for l in L[起 + 1:止]:
        m = re.match(r'^- \*\*([^*]+)\*\*', l)
        if m:
            头们.append(re.sub(r'（[^）]*）|\([^)]*\)', '', m.group(1)).strip())
        elif l.strip() and not l.startswith('>'):
            句们 += [s for s in re.split(r'[；;。]', l) if s.strip() and not _不收.search(s)]
    出, 中头 = [], set()
    for v in (册.get('人物') or [] if isinstance(册, dict) else []):
        if not isinstance(v, dict):
            continue
        称们 = [x for x in _称们(v) if not _泛.match(x)]
        中 = [h for h in 头们 if any(x == h or x in h for x in 称们)]
        中头.update(中)
        中 += [x for x in 称们 if any(x in s for s in 句们) and x not in 中]
        if 中 and v.get('名') not in 已:
            出.append((v.get('名'), 中, v))
    return 出, [h for h in 头们 if h not in 中头]


# ── ★1021 X42 ──
# 余章总案之条头：行首之「- 」（连缩进之子条）或句读之後之「N 主／N 暗」（「419／421／423 暗」「430—434 主」）；「主线」「暗线」⛔认
_条头 = re.compile(r'(?:^\s*-\s*|(?<=[。！？；〕」』）)｜|])\s*)(\d{2,3}(?:[／/]\d{2,3})*(?:[—–]\d{2,3})?)\s*(?:主|暗)(?=[\s·「『（(★*〔：:]|$)')
_旧头 = re.compile(r'^- (\d+) ')      # 旧式（行首「- N 」）照认——⛔坏


def _章们(s):
    """「419／421／423」→ [419, 421, 423]；「430—434」→ [430…434]（一段至多三十章）。"""
    出 = []
    for x in re.split(r'[／/]', s):
        ab = re.split(r'[—–]', x)
        a = int(ab[0])
        b = int(ab[1]) if len(ab) > 1 and ab[1] and a <= int(ab[1]) <= a + 30 else a
        出 += range(a, b + 1)
    return 出


def _余章之条(案, n):
    """余章总案里第 n 章之条 → [(行号, 片, 行中起否, 其行下接他章否)]：一行里诸条头（行首与行中）切其行，一条归一章——
    ★1021 X42：旧只认行首「- N 」，400 之行末之「401 暗 她循牌纹到同一条街」漏收；行首之条其行下接他章者，止於他章之头。"""
    出 = []
    for i, l in enumerate((案 or '').split('\n'), 1):
        头 = {}
        m = _旧头.match(l)
        if m:
            头[0] = [int(m.group(1))]
        for m in _条头.finditer(l):
            起 = 0 if l[:m.start(1)].strip() in ('', '-') else m.start(1)
            头[起] = _章们(m.group(1))
        位 = sorted(头)
        for k, a in enumerate(位):
            if n in 头[a]:
                b = 位[k + 1] if k + 1 < len(位) else len(l)
                出.append((i, l[a:b].rstrip(), a > 0, b < len(l)))
    return 出


def _远引(文, root=ROOT, 全收=()):
    """★1021 X42②：卡与 open_brief 所引之远章「章:行」「章:行—行」→ 原句——照 章料.引之原句（⛔另造一法：越章长之行⛔展、
    一段至多三十行、逾 30KB 即止）；只留章之引（总纲、余章总案、D3、D6 之行⛔——【九】已汇或不属白文）；全收之章只列其号。"""
    import 章料
    return [x for x in 章料.引之原句(文 or '', root, 略章=set(全收))
            if re.match(r'- \d', x) or x.startswith(('- 见前文白文', '（所引尚有'))]


def _承前之章(N, 卡, root=ROOT, 庭=None):
    """★1021 W60·X42 驳席①：【十】之承前章与开镜庭之接钩同一把尺——import 第零轮开镜庭 之 _同镜之前（⛔另抄一把）。
    旧只取同线：401（沈鸢镜）取 399（黎东来镜），而其卡之钩实接同镜之 397（W60 席二）。
    线、镜、表俱取开镜庭之器（_线表 总纲丁表、_镜之表 锁定行「镜：」、_镜之正、_答——与其 _接钩之前 同序：卡「本章之镜」起头之名先、锁定行次之）：
      开镜庭判本章暗线、其镜认得着、同镜有前者取同镜之前；主线（同镜即同线）照取同线、⛔印由；
      import 败、本章之线或镜未定、或 _同镜之前 返 None（线／镜未钉之暗线章即止、同镜无前）者照旧取同线，回其由——料中印一行「承前取同线·镜未定之由」。
    同线照旧以 造式验.线（十二章内）。庭：测时注入之替身（⛔读盘）。
    → (章或 None, '同镜'／'同线', 镜或 None, 镜未定之由或 None, 同线之章或 None)。"""
    import 造式验
    本线 = 造式验.线(N, root)
    同线 = next((k for k in range(N - 1, N - 13, -1) if 本线 and 造式验.线(k, root) == 本线), None)
    镜 = None
    try:
        if 庭 is None:
            import 第零轮开镜庭 as 庭
        线 = 庭._线表()
        if 线.get(N) != '暗':
            return 同线, '同线', None, (None if 线.get(N) == '主' or 本线 != '暗' else '本章之线开镜庭认不着（总纲丁表未钉）'), 同线
        镜表 = 庭._镜之表()
        镜 = 庭._镜之正(庭._答(卡 or '', '本章之镜')) or 镜表.get(N)
        if not 镜:
            return 同线, '同线', None, '本章之镜认不着（卡之「本章之镜」须以其名起头；锁定行亦无）', 同线
        k, 由 = 庭._同镜之前(N, 镜, 线, 镜表)
    except Exception as e:
        return 同线, '同线', 镜, 'import 第零轮开镜庭 或其器败（%s：%s）' % (type(e).__name__, e), 同线
    if k:
        return k, '同镜', 镜, None, 同线
    return 同线, '同线', 镜, '%s镜·%s' % (镜, 由 or '_同镜之前 返 None'), 同线


def 近三之向形(T, N):
    """★X100④（450 封前）：近三章锁定行之「本章之向｜形｜品」——记席写本章之向形须避同（449 记席另翻施工表）。N≤449 ⛔出（旧料一字不动）。"""
    if N < 450:
        return ''
    出 = []
    for n in range(N - 3, N):
        m = re.search(r'^\| %d \| 锁定 \|.*?(本章之向[：:][^*\n]*)' % n, T, re.M)
        出.append('- %d：%s' % (n, m.group(1).strip() if m else '（锁定行无「本章之向」）'))
    # ★1113 X103①：窗义明书（452 记席「近三章」之窗含否本章未明）——下一章卡之窗含本章与下一章；--立 之卡已带机器所报之向形
    return ('\n\n〔近三章之向｜形｜品（本章之向、形须与之相异或书其由）。下一章（%d）之卡：⑲窗＝%d—%d（含其章）三章⛔同向；'
            '⑰窗＝%d—%d（含其章）同形≤3；本章 %d 之向形取本章卡；`--立 %d` 已印机器所报〕\n' % (N + 1, N - 1, N + 1, N - 3, N + 1, N, N + 1)
            + '\n'.join(出))


# ── ★1118 器红三治·根病一（a9e5cc5ee：461、462 详记缺「## 一句之要」→ 章料·剧情链红）──
今站之底 = 2          # 今站块逾额时⛔略之末几章之行（记席「添本章一行」之式样）
今之末之底 = 400      # 「全书今之末」一行逾额时至少留其首几字（记席改其首二条）
_站章行 = re.compile(r'^\d+｜- \*\*(?:主线|暗线)·\d')


def _余额(k, 片们):
    """多源之节之界 k 减去 片们 [(源, 片)] 所占（与 _截 同尺：各片 strip、片间空行二字节）——余者即首片之额。"""
    return k - sum(len(t.strip().encode()) + 2 for _, t in 片们 if (t or '').strip())


def _总览之片(总览, 今站, 额全, 额必):
    """【四】首片（总览·题、「全书今之末」、今站一块、索引末三行）→ str。
    旧：此片无额，今站块每章一行（E8 451—480 每行 ≈560B；462 之片 15.1KB），【四】截自尾起——先截前章之记，次截用法 §六之式；
    461、462 记席未见「## 一句之要」之式而漏写（a9e5cc5ee 手补）。
    今：片 ≤ 额全（余三片俱全收之额）即与旧式一字不差；逾者——
      ①今站块之章行（「- **主线·N」「- **暗线·N」）自旧而新逐行略去、末 今站之底 行⛔略，至 ≤ 额全；略处印一行其行段与 sed -n；
      ②仍逾 额必（人物锚行、用法 §五§六 二片外之全额；前章之记·式样让之）者，「全书今之末」一行截其尾（⛔少於 今之末之底 字）；
      ③仍逾者片截於 额必（截於行界、印其略）——用法 §五§六 之全收由此在结构上钉死，⛔再随今站之长而丢。"""
    V = 总览.split('\n')
    题们 = 行们(总览, r'^# |全书今之末', 0, 0, 3).split('\n')
    站 = 段(总览, r'^### E\d', 今站).split('\n') if 今站 >= 0 else []
    尾 = '\n'.join('%d｜%s' % (i + 1, l) for i, l in list(enumerate(V))[-3:])

    def 成(题们, 站):
        return ('〔总览·题、「全书今之末」、今站一块（记席改其「线与日」「读者之所欠」、添本章一行）、索引末三行〕\n' +
                '\n'.join(题们) + '\n' + (引(行截('\n'.join(站), 200)) if 今站 >= 0 else '（总览无站块）') + '\n' + 尾)

    def 长(t):
        return len(t.strip().encode())
    片 = 成(题们, 站)
    if 长(片) <= 额全:
        return 片
    # ①
    章 = [k for k, l in enumerate(站) if _站章行.match(l)]
    可略 = 章[:-今站之底] if len(章) > 今站之底 else []
    for m in range(1, len(可略) + 1):
        略 = set(可略[:m])
        号 = [int(站[k].split('｜', 1)[0]) for k in 可略[:m]]
        注 = '（今站块旧章之行 :%s 共 %d 行略（★1118·【四】逾额：末 %d 章之行为添行之式样；用法 §六之式恒全收）——全行 sed -n %d,%dp %s）' % (
            _号段(号), m, 今站之底, min(号), max(号), os.path.join(记, '总览.md'))
        站略 = [l for k, l in enumerate(站) if k not in 略]
        站略.insert(可略[0], 注)
        片 = 成(题们, 站略)
        if 长(片) <= 额全:
            return 片
    if 长(片) <= 额必:
        return 片
    # ②
    i = next((k for k, l in enumerate(题们) if '全书今之末' in l), None)
    if i is not None:
        末 = 题们[i]
        n = len(末)
        while 长(片) > 额必 and n > 今之末之底:
            n = max(今之末之底, n - max(50, (长(片) - 额必) // 3 + 20))
            题们 = 题们[:i] + [截(末, n) + '（全行 sed -n %s 读）' % 末.split('｜', 1)[0]] + 题们[i + 1:]
            片 = 成(题们, 站略 if 可略 else 站)
    if 长(片) <= 额必:
        return 片
    # ③
    留, 略 = _截([('', 片)], max(0, 额必 - 300))
    return 留 + '\n（总览之片逾额 %d 字节：下略 %d 行、%d 字节——全文 sed -n 读 %s）' % (额必, 略[0], 略[1], os.path.join(记, '总览.md'))


def 汇(N, root=ROOT):
    f, 白 = 章白(N, root)
    出 = ['# 记料·第%d章（零 token 所汇·工具/记料.py）' % N, '',
          '> 记席之九件事所要翻的诸账，於此一档；逐字抄自盘上（章:行可查）。⛔再逐档翻找——缺者方以 `sed -n` 补，并记其缺（交主环补器）。'
          '封版.py %d --前 之印⛔在此（其有存版之副作用），记席自跑。' % N,
          '> 节作「## 【一】」至「## 【十二】」，各有其界（逾界者印其所略与全文之路）；所引之档之「#」行皆加「〉」（原档无此符）。'
          '「〔补·…〕」起者係 X36、X42 之补（殿其节之尾，额取诸节未用之界）。']
    if N >= 411:                     # ★1024 省 token 之审 records 一·第一步：纯机械之格归 记落.py（N≤410 之料一字不变）
        try:
            import 大审
            号们 = '、'.join('#%s' % x[0] for x in 大审.限於(N + 1)) or '（零笔）'
        except Exception as _e:
            号们 = '（算不出：%s）' % _e
        出.append('> ★器格（N≥411·`工具/记落.py`）：诸档之纯机械之格⛔手抄，写占位「‹器:键›」——键：回执之数（回执 §一首三条）｜终稿（创作记录 §五首条）｜'
                  'sha1｜六数｜净重｜白文止｜亮点行｜星｜拍｜星行｜拍界｜末版｜诸版｜台账版数｜总纲｜总纲行｜日号｜极短段｜对白｜章料KB｜记料KB｜大审笔数｜大审之笔｜'
                  '大审#号（开镜卡问七一笔一键：%s）；圣经事件链之题与旧锚〔已销〕、总览之题与「写至」、检察官 schema 行、席记「封版」段器直落（⛔手改）。'
                  '写毕跑 `python3 工具/记落.py %d`；值与 diff 先看 `--试`。' % (号们, N))
    # ★1020 X36：诸节先记其料、末了一并成节——补之额要等诸节旧体之实量毕方知
    诸, 补们 = [], {}
    卡档 = [os.path.join('版本', '第%d章' % n, '_开镜卡.md') for n in (N, N + 1)]
    卡, 下卡 = 读(卡档[0], root), 读(卡档[1], root)
    # 一、前章回执之式
    前回 = sorted(glob.glob(os.path.join(root, '设定', '回执_*_第%d章封版席.md' % (N - 1))))
    _骨 = sorted(glob.glob(os.path.join(root, '设定', '回执_*_第%d章封版席.md' % N)))
    if N >= 460 and 前回 and _骨:          # ★X109（1117）：回执之骨已由 记落 --骨 立——⛔再印前章回执之式（骨即其式）
        诸.append(('一', '回执之骨（X109·`记落.py %d --骨` 已立 %s：节目、键、§一 器格俱在）——⛔Write 回执全档；只以 Edit 并发把诸「‹判›」换作判语（每条 ≤60 字·凭写 章:行），本章特有之节（本章之失、交总编辑）照实书条；前章回执 %s 要其式者 sed -n 其节'
                   % (N, os.path.relpath(_骨[-1], root), os.path.relpath(前回[-1], root)), '', os.path.relpath(_骨[-1], root)))
    elif 前回:
        p = os.path.relpath(前回[-1], root)
        import 封版 as _封                    # ★X83（1105）：回执闸之键与封版 --前 一表（418 记席多回补键）
        诸.append(('一', '前章回执之式（%s：每节首三行；全文照此式写）｜回执闸之键（俱须在·小说检察官._receipt_ok）：%s'
                   % (p, '、'.join(_封.回执闸之键)), 引(行截(_节首(open(前回[-1], encoding='utf-8').read(), 3), 400)), p))
        # ★1113 X101②（452 记席费审：回五另 grep 前章回执之键行 $0.43、回七拟回执思逾万 token）：N≥453 回执闸诸键之行印出（各截 120 字）——键之写式一眼即得
        if N >= 453:
            _键行 = [l[:120] for l in open(前回[-1], encoding='utf-8').read().split('\n')
                     if re.match(r'^- \*\*(%s)\*\*' % '|'.join(map(re.escape, _封.回执闸之键)), l)]
            if _键行:
                补们['一'] = ('；补：回执闸诸键之行（前章回执·各截 120 字·X101②）',
                             [(p, '〔补·回执闸诸键之行（%s）〕\n' % p + '\n'.join(_键行))])
    # ★1118 总编辑复核「悬念哨→改」：本章段案之节内提 SUS-A／B／C 之行逐字（带整档行号）并第二路之严式，殿【一】之补（补序首·额取补界一）；节内无者⛔印
    悬源, 悬行 = _段案之悬(N, root)
    if 悬行:
        悬片 = (悬源, '〔补·本章（%d）段案所排之悬念拍（%s「## %d」节内提 SUS-A／SUS-B／SUS-C 之行·逐字）〕\n%s\n' % (N, 悬源, N, 悬之令)
              + '\n'.join('%d｜%s' % (i, 引(l)) for i, l in 悬行))
        标一, 片一 = 补们.get('一', ('；补：', []))
        补们['一'] = (标一 + ('、' if 片一 else '') + '本章段案所排之 SUS 拍与第二路之严式（悬念哨）', 片一 + [悬片])
    # 二、施工表
    T = 读(表, root)
    诸.append(('二', '施工表：N-1 之锁定行与悬账（式样）、本章之硬门槛（整节；下一章之节立於其上）',
                行们(T, r'^\| %d \| (锁定|悬账) \|' % (N - 1)) + '\n\n' + 行截(段(T, r'^## 四、续写第 %d 章前的硬门槛' % N), 400)
                + 近三之向形(T, N), 表))
    # ★1020 X36②：同镜前章之悬账行（同镜即 N-1 者其行已在上）；★X43⑧：其章与【十】同取 _承前之章（开镜庭之尺·⛔自家 _同镜 之六十章窗）
    同, 承由, 承镜, 未定, 同线 = _承前之章(N, 卡, root)
    镜前, 镜, 镜由 = 同, 承镜, 承由
    if 镜前 and 镜前 != N - 1:
        悬 = 行们(T, r'^\| %d \| 悬账 \|' % 镜前)
        补们['二'] = ('；补：%s前章（%d）之悬账行' % (镜由, 镜前), [(表, '〔补·%s前章（第%d章%s）之悬账行（%s）〕\n' % (
            镜由, 镜前, ('·镜：%s' if 镜由 == '同镜' else '·本章之镜 %s 无同镜之前') % 镜 if 镜 else '', 表) +   # 驳席：同线者旧注「·镜：霍钧」读如 389 之镜
            (悬 or '（施工表无「| %d | 悬账 |」之行）' % 镜前))])
    # 三、创作记录（式样）
    创 = os.path.join('版本', '第%d章' % (N - 1), '_创作记录.md')
    诸.append(('三', '前章创作记录（%s：每节首二行·式样；席记之式见令）' % 创, 引(_节首(读(创, root), 2)), 创))
    # 四、全书记忆
    用法 = 读(os.path.join(记, '用法.md'), root)
    U = 用法.split('\n')
    起 = next((i for i, l in enumerate(U) if l.startswith('## 五、')), 0)
    止 = next((i for i in range(起 + 1, len(U)) if U[i].startswith('## 七、')), len(U))
    前章记 = 读(os.path.join(记, '第%d章.md' % (N - 1)), root)
    总览 = 读(os.path.join(记, '总览.md'), root)
    V = 总览.split('\n')
    今站 = max([i for i, l in enumerate(V) if re.match(r'^### E\d', l)] or [-1])
    人物 = 读(os.path.join(记, '人物.md'), root)
    # ★1020 X15 验席：锚行在前，§五§六（有行号，截则 sed -n 起,止p）次之，前章之记（式样）殿後——截自尾起只截式样
    # ★1118（a9e5cc5ee 根病一）：总览之片自有其额（_总览之片）——今站块逐章长，旧截自尾起先截前章之记、次截用法 §六之式（461、462 详记缺「## 一句之要」）；
    #   今逾额者先略今站块之旧章行、次截「全书今之末」之尾、末了片截於其额——人物锚行与用法 §五§六 二片恒全收
    人片 = (os.path.join(记, '人物.md'),
          '〔人物.md·题与今之行止（全档 %d 行；在场之人之节见【五】）〕\n' % len(人物.split('\n')) + 行截(行们(人物, r'^# |^> 今之行止', 0, 0, 3)))
    用片 = (os.path.join(记, '用法.md'), '〔用法.md:%d—%d〕\n' % (起 + 1, 止) + 引('\n'.join(U[起:止])))
    前片 = (os.path.join(记, '第%d章.md' % (N - 1)),
          '〔第%d章.md·式样（每节首二行；式以上之 §六 为准；全文照 `设定/全书记忆/第%d章.md`）〕\n' % (N - 1, N - 1) + 引(行截(_节首(前章记, 2), 200)))
    诸.append(('四', '全书记忆：总览与人物之锚行、用法 §五规矩与 §六之式、前章之记（每节首二行·式样）', [
        (os.path.join(记, '总览.md'), _总览之片(总览, 今站, _余额(界['四'], [人片, 用片, 前片]), _余额(界['四'], [人片, 用片]))),
        人片, 用片, 前片]))
    # 五、在场之人：人物.md 之节首与末一「之变」
    册 = {}
    try:
        册 = json.load(open(os.path.join(root, 册档), encoding='utf-8'))
    except Exception:
        pass
    人们 = 在场(白, N, 册)

    def 人节(名, 题):
        名0 = re.sub(r'（[^）]*）', '', 名 or '')
        节体 = 段(人物, r'^### .*%s' % re.escape(名0)) if 名0 else ''
        行 = 节体.split('\n') if 节体 else []
        变 = [l for l in 行 if re.match(r'\d+｜- \*\*\d+', l)]
        return [题, '\n'.join([引(x) for x in 行[:1]] + [截(x, 400) for x in 变[-1:]]) or '（人物.md 无其节）']
    体 = []
    for 名, 中, v in 人们:
        体 += 人节(名, '### %s（白文所见之称：%s｜末见章 %s）' % (名, '、'.join(中), v.get('末见章')))
    诸.append(('五', '本章白文里出现之人（人物.md 之节首与末一「之变」·式样；状态册之行见【十一】）——须添「%d态」者' % N, '\n'.join(体), os.path.join(记, '人物.md')))
    # ★1020 X36④：卡·问九之二所列而白文未见之人（只以纸、以手到场者——399 管章的人）；册无其人者列其名
    卡人, 卡无册 = _卡之人(卡, 册, {x[0] for x in 人们})
    if 卡人 or 卡无册:
        体 = ['〔补·卡·问九之二所列而白文未见之人（%s）〕' % 卡档[0]]
        for 名, 中, v in 卡人:
            体 += 人节(名, '### %s（卡·问九之二所列之称：%s｜末见章 %s）' % (名, '、'.join(中), v.get('末见章')))
        if 卡无册:
            体.append('〔卡·问九之二所列而状态册无其人：%s〕' % '、'.join(卡无册))
        补们['五'] = ('；补：卡·问九之二所列之人', [(卡档[0], '\n'.join(体))])
    # 六、物件、悬线
    物件 = 读(os.path.join(记, '物件.md'), root)
    悬线 = 读(os.path.join(记, '悬线.md'), root)
    W = 物件.split('\n')
    末物 = max([i for i, l in enumerate(W) if re.match(r'^- \*\*\d+ 之物', l)] or [-1])
    S = 悬线.split('\n')
    所结 = max([i for i, l in enumerate(S) if re.match(r'^- \*\*.*所结所开', l)] or [-1])
    号 = re.compile(r'(?<!\d)(%d|%d)(?!\d)' % (N, N + 1))
    条, 摘 = [], []
    for i, l in enumerate(S):
        if i == 所结 or not 号.search(l):
            continue
        if re.match(r'^- \*\*(%d|%d)（' % (N, N + 1), l):
            条.append('%d｜%s' % (i + 1, 截(l, 400)))
            continue
        窗, 末 = [], -1
        for m in 号.finditer(l):
            a, b = max(m.start() - 40, 末 + 1), min(len(l), m.end() + 24)
            if a < b:
                窗.append(l[a:b]); 末 = b
        摘.append('%d｜%s…%s…%s' % (i + 1, l[:24], '…'.join(窗[:2]), '（另 %d 处）' % (len(窗) - 2) if len(窗) > 2 else ''))
    诸.append(('六', '物件之末一块（式样；新块添於档末）、悬线：末一「所结所开」（式样）、钉 %d、%d 之条与其旁' % (N, N + 1),
                '〔物件.md·题与末一块〕\n' + 行们(物件, r'^# ', 0, 0, 1) + '\n' + (行截(块(物件, 末物), 200) if 末物 >= 0 else '（无）') +
                '\n\n〔悬线.md·题与末一「所结所开」〕\n' + 行们(悬线, r'^# ', 0, 0, 1) + '\n' + ('%d｜%s' % (所结 + 1, 截(S[所结], 600)) if 所结 >= 0 else '（无）') +
                '\n\n〔悬线.md·「%d（」「%d（」之条〕\n' % (N, N + 1) + ('\n'.join(条) or '（无）') +
                '\n\n〔悬线.md·提及 %d、%d 之行（摘其旁；全行 sed -n 读）〕\n' % (N, N + 1) + ('\n'.join(摘) or '（无）'), os.path.join(记, '悬线.md')))
    # 七、轮记、行家评、构思之目（记席本须全读——此只给目与行号）
    def 目(p):
        t = 读(p, root)
        if not t:
            return '〔%s：无〕' % p
        return '〔%s·%d 字节·%d 行〕\n' % (p, len(t.encode()), t.count('\n') + 1) + '\n'.join(
            '%d｜〉%s' % (i + 1, 截(l, 80)) for i, l in enumerate(t.split('\n')) if l.startswith('#'))
    章目 = os.path.join('版本', '第%d章' % N)
    构思 = sorted(glob.glob(os.path.join(root, 章目, '起草_*_构思.md')))
    诸.append(('七', '本章轮记、行家评之目（行号）与诸构思之档——创作记录据之（全读）', [
        (os.path.join(章目, '_轮记.md'), 目(os.path.join(章目, '_轮记.md'))),
        (os.path.join(章目, '_行家评.md'), 目(os.path.join(章目, '_行家评.md')) + '\n\n〔行家评·名次〕\n' +
         行们(读(os.path.join(章目, '_行家评.md'), root), r'^#+ *名次|^\d+\. *稿|名次', 0, 2, 20)),
        (os.path.join(章目, '起草_*_构思.md'), '〔构思〕\n' +
         ('\n'.join('%s（%d 字节）' % (os.path.relpath(p, root), os.path.getsize(p)) for p in 构思) or '（无）'))]))
    # ★1020 X36①：诸构思之「满分之问」全段（三种写法与其比在前、拍表殿後）
    # ★X91③（434）：轮记之盲读、逻辑审全节先列（记席据之写回执§四、创作记录——旧只给目，432 记席多一回读 13—95 行）
    轮 = _轮记之审(os.path.join(章目, '_轮记.md'), root, 末回=N >= 446)
    # ★X95②（440）：满分之问只给胜稿与嫁大进之稿之构思（行家评「## 名次」首稿＋「## 大进」所引之稿；蒙号照造章.js 之轮转）——
    #   余稿只列档名（〔构思〕已列）；认不出者照旧全给（⛔缺料）
    取 = _胜嫁之构思(构思, 章目, N, root) if (构思 and N >= 440) else 构思
    # ★X97（446）：拍表只附胜稿之构思（嫁稿之拍行家评「## 大进」已载）——445【七】拍表三份约 7KB
    胜们 = _胜嫁之构思(构思, 章目, N, root, 只胜=True) if (构思 and N >= 446) else None
    满 = _满分之问(取, root, 表只=胜们 if 胜们 and len(胜们) < len(取) else None) if 取 else []
    if 满:
        满[0] = (满[0][0], '〔补·诸构思之「满分之问」全段（%d 份%s；三种写法与其比在前，拍表殿後——截自尾起先截拍表）〕\n' % (
            len(取), '·只胜稿与嫁大进之稿（X95）：余 %d 份只列档名，要时 sed -n' % (len(构思) - len(取)) if len(取) < len(构思) else '') + 满[0][1])
    if 轮 or 满:
        补们['七'] = ('；补：' + '、'.join(x for x, y in (('轮记之盲读与逻辑审全节', 轮), ('诸构思之「满分之问」全段', 满)) if y), 轮 + 满)
    # 八、圣经之锚、检察官之行、open_brief
    圣 = 读(os.path.join('设定', '00_镇冢秘术_唯一总圣经.md'), root)
    检 = 读(os.path.join('工具', '小说检察官.py'), root)
    try:
        canon = json.load(open(os.path.join(root, '设定', 'canon事实库.json'), encoding='utf-8'))
        ob = canon.get('open_brief') if isinstance(canon, dict) else None
    except Exception:
        canon, ob = {}, None
    圣档 = os.path.join('设定', '00_镇冢秘术_唯一总圣经.md')
    锚 = 行们(圣, r'^## 十一、已写 1—|第 (%d|%d) 章必须从' % (N, N + 1), 0, 2, 12)
    # ★1020 X15 验席：前章之条含本章之锚（398 之 9924—9926 印两回·赘 762 字节）——锚行已印者⛔重印、注其号；
    #   open_brief（记席逐栏重写）在前，前章之条（式样）殿後——截自尾起只截式样
    已印 = {l.split('｜', 1)[0] for l in 锚.split('\n') if '｜' in l}
    条 = [l for l in 段(圣, r'^### 第 %d 章《' % (N - 1)).split('\n') if l]
    重 = [int(l.split('｜', 1)[0]) for l in 条 if l.split('｜', 1)[0] in 已印]
    条文 = 截(引(行截('\n'.join(l for l in 条 if l.split('｜', 1)[0] not in 已印), 300)), 1500)
    诸.append(('八', '圣经之锚与事件链之题、检察官 OPEN_BRIEF_CARD_SCHEMA 本章与下一章之行、open_brief（全块）、前章之条（式样）', [
        (圣档, 行截(锚, 400)),
        (os.path.join('工具', '小说检察官.py'), '〔检察官·OPEN_BRIEF_CARD_SCHEMA〕\n' +
         (行截(行们(检, r'^\s+(%d|%d):\s*\(' % (N, N + 1), 1, 0, 6), 600) or '（无本章与下一章之行）')),
        (os.path.join('设定', 'canon事实库.json'), '〔open_brief〕\n' + (json.dumps(ob, ensure_ascii=False, indent=1) if ob else '（open_brief 不在）')),
        (圣档, '〔圣经·第 %d 章之条（式样%s）〕\n' % (N - 1, '；:%s 即上之锚行，⛔重印' % _号段(重) if 重 else '') + 条文)]))
    # ★1020 X36③：本章卡与下一章卡里「圣经:NNNN」所指之行——上已印者（锚行、前章之条）⛔重印、注其号
    已见 = 已印 | set(re.findall(r'^(\d+)｜', 条文, re.M))
    引们 = [(p, _圣经之引(t)) for p, t in zip(卡档, (卡, 下卡)) if t]
    号们 = list(dict.fromkeys(k for _, ks in 引们 for k in ks))[:24]
    if 号们:
        G = 圣.split('\n')
        新 = [k for k in 号们 if str(k) not in 已见 and 0 < k <= len(G)]
        补们['八'] = ('；补：卡所引圣经之行', [(圣档, '〔补·卡所引圣经之行（%s%s）〕\n' % (
            '；'.join('%s 引 :%s' % (p, _号段(ks)) for p, ks in 引们 if ks),
            '；:%s 已见上，⛔重印' % _号段([k for k in 号们 if str(k) in 已见]) if len(新) < len(号们) else '') +
            (行截('\n'.join('%d｜%s' % (k, G[k - 1]) for k in 新), 400) or '（所引之行俱已见上或逾档末）'))])
    # 九、下一章：总纲、余章总案之短行在前，段案之节殿後（★1020 X15 验席：旧段案在前，一逾界先丢的是总纲、余章总案之行）
    段源, 段文, 段目 = _段案(N + 1, root)
    纲档, 案档 = os.path.join('设定', '02_余章之势_总纲.md'), os.path.join('设定', '剧情庭题', '余章总案.md')
    纲, 案 = 读(纲档, root), 读(案档, root)
    A = 案.split('\n')
    二起 = next((i for i, l in enumerate(A) if l.startswith('## 二、')), None)
    二止 = next((i for i in range((二起 or 0) + 1, len(A)) if A[i].startswith('## ')), len(A)) if 二起 is not None else None
    # ★1021 X42①：余章之条以「N 主／N 暗」在行内认、一条归一章（旧 r'^- N ' 只认行首——余章:66 末之 401 漏收）；本章与下一章之条俱汇
    条文 = '\n'.join('%d｜%s%s%s' % (i, '…' if 中 else '', 片, '…' if 续 else '')
                   for n in (N, N + 1) for i, 片, 中, 续 in _余章之条(案, n)[:6])
    诸.append(('九', '下一章（%d）：总纲之行、余章总案本章与下一章之条、段案之节；开镜卡以「python3 工具/第零轮开镜庭.py --立 %d」起' % (N + 1, N + 1), [
        (纲档, '〔总纲·%d、%d 之行〕\n' % (N + 1, N + 2) + (行们(纲, r'\| *(%d|%d) *\|' % (N + 1, N + 2), 0, 0, 6) or '（无）')),
        (案档, '〔余章总案·§四 %d（本章）、%d 之条（行中之「N 主／N 暗」亦认、一条归一章：「…」起者係行中之条，「…」止者其行下接他章之条）%s〕\n' % (
            N, N + 1, '' if 二起 is None else '；§二解歧之裁在 :%d—%d（sed -n 读）' % (二起 + 1, 二止)) +
         (条文 or '（无）')),
        (段源, ('〔%s·%d 之节；段头与附录不汇（sed -n 读）：%s〕\n' % (段源, N + 1, '｜'.join(段目)) + 引(段文)) if 段文 else '（段案无其节）')]))
    # 十、同线前章之白文（带行号）——冷眼轮之冷读、承前之判（开轮⑮比其末五段之骨）；极短段之比已归 封版 --前 ⑥
    # ★1021 W60·X42 驳席①：选章与开镜庭之接钩同尺（_承前之章：import 其 _同镜之前）——换镜之暗线章取同镜之前（401→397、399→389）；
    #   主线照取同线（400→398、398→396，其节一字不变）；同镜取不着者照旧取同线，节首印一行「承前取同线·镜未定之由」
    注 = ('〔承前取同线·镜未定之由：%s〕' % 未定) if 未定 else ''
    十, 剪 = None, False
    if 同 and 同 != N - 1:
        p同, L同 = _白行(同, root)
        换 = 承由 == '同镜' and 同 != 同线           # 同镜前章非同线前章（换镜之暗线章）
        # ★1119 X117（473 起）：记占 470—472 均 6.7% 逾 5.5%——【十】只留前章末五段（承前之判只须收句之骨；冷眼轮 1027 已汰），全文 sed -n 读
        剪 = N >= 473 and len(L同) > 5
        体十 = (注 + '\n' if 注 else '') + ('〔%s·末五段（X117·473 起只留收句之骨；余 %d 段、全文 sed -n 读）〕\n' % (p同, len(L同) - 5)
                                           if 剪 else '〔%s〕\n' % p同) + '\n'.join('%d｜%s' % x for x in (L同[-5:] if 剪 else L同))
        if 换 and 同线:                            # ★X43⑧：换镜之章并附同线前章之末五段（开轮⑮所比之收句之骨）——旧⛔附、记席另 sed
            # ★1103 W78 驳之取舍（主环裁）：附段（约 1.3KB）入【十】之旧体，补之池随之减——换镜之章（399、401、407 之类）【七】拍表之补或下略 1—3 行（其注照印、缺者 sed -n）；
            #   二者俱省一回 sed，而附段係开轮⑮之比所必须、拍表之略有注可补——取附段。
            p线, L线 = _白行(同线, root)
            体十 = [(p同, 体十), (p线, '〔同线前章·%s 之末五段（开轮⑮所比；全文 sed -n 读）〕\n' % p线 + '\n'.join('%d｜%s' % x for x in L线[-5:]))]
        十 = ('十', (('同镜前章（第%d章·%s镜——与开镜庭接钩同尺；同线前章係第%s章，开轮⑮所比，其末五段附於节尾）' % (同, 承镜, 同线 or '?'))
                     if 换 else ('同线前章（第%d章·亦同镜·%s镜）' % (同, 承镜)) if 承由 == '同镜' else '同线前章（第%d章）' % 同) +
              '之白文（行号即整档之行）——冷眼轮之冷读、承前之判%s、收句之骨' % ('' if 换 else '（开轮⑮）'),
              体十, p同)
    # ★1021 X42②：本章卡、下一章卡、open_brief 所引之远章「章:行」「章:行—行」之原句（章料.引之原句）——【十】白文全收（未逾界）之章只列其号
    远源 = [(p, t) for p, t in zip(卡档, (卡, 下卡)) if t] + \
        ([(os.path.join('设定', 'canon事实库.json') + '·open_brief', json.dumps(ob, ensure_ascii=False, indent=1))] if ob else [])
    全收 = {同} if 十 and not 剪 and _截(_片们(十[2], 十[3]), 界['十'])[1] is None else set()   # X117：剪後非全收，远引照展
    远 = _远引('\n'.join(t for _, t in 远源), root, 全收) if 远源 else []
    if (远 or 注) and not 十:      # 镜未定之由无白文可附者，【十】仍立以印其由
        十 = ('十', '%s前章之白文（%s——不汇）' % (承由, ('%s前章即第%d章' % (承由, 同)) if 同 else '十二章内无同线之章'), 注, '')
    if 远:
        补们['十'] = ('；补：卡所引远章之原句', [('、'.join(p for p, _ in 远源), '〔补·卡所引远章之原句（%s 所引之「章:行」；工具/章料.py 引之原句之法）〕\n' % (
            '、'.join(p for p, _ in 远源)) + '\n'.join(远))])
    if 十:
        诸.append(十)
    # 十一、人物状态册之行
    def 册之行(人):
        出 = []
        for 名, 中, v in 人:
            区 = _册之区(v.get('名'), root)
            出.append('〔%s%s〕%s' % (v.get('名'), '·%s:%d—%d' % (册档, 区[0] + 1, 区[1]) if 区 else '', _册行(v)))
        return 出
    行 = 册之行(人们)
    if 卡人:    # ★1020 X36④：卡·问九之二所列而白文未见之人之册行
        补们['十一'] = ('；补：卡·问九之二所列之人', [(册档, '〔补·卡·问九之二所列而白文未见之人（%s）〕\n' % 卡档[0] + '\n'.join(册之行(卡人)))])
    if 行 or 卡人:
        诸.append(('十一', '人物状态册之行（在场之人；留末一态、列留末二条——添「%d态」照此式；全行看其区）' % N, '\n'.join(行), 册档))
    # 十二、canon 卡名与一卡之式、大师进化账之末
    try:
        卡们 = [c for c in ((canon or {}).get('state_canon') or []) if isinstance(c, dict)]
    except Exception:
        卡们 = []
    名们 = [x for _, 中, v in 人们 for x in [re.sub(r'（[^）]*）', '', v.get('名') or '')] + 中 if len(x) >= 2 and not x.startswith('（')]
    近 = [c.get('what', '') for c in 卡们 if (isinstance(c.get('from'), int) and c['from'] >= N - 15) or any(x in str(c.get('what', '')) for x in 名们)]
    式卡 = max(卡们, key=lambda c: c.get('from') if isinstance(c.get('from'), int) else -1) if 卡们 else None
    进 = 读(os.path.join('设定', '大师进化账.md'), root).rstrip('\n').split('\n')
    诸.append(('十二', 'canon state_canon 卡名（近十五章所立、或提在场之人者；open_brief 之 required_state_cards 照此择）、一卡之式、大师进化账末三行', [
        (os.path.join('设定', 'canon事实库.json'), '\n'.join('- ' + x for x in 近[-60:]) + '\n\n〔state_canon·末立之一卡（式样）〕\n' +
         (截(json.dumps(式卡, ensure_ascii=False), 500) if 式卡 else '（无）')),
        (os.path.join('设定', '大师进化账.md'), '〔设定/大师进化账.md·末三行（式样；教训追加於档末）〕\n' +
         '\n'.join('%d｜%s' % (len(进) - 2 + k, 截(l, 200)) for k, l in enumerate(进[-3:])))]))
    # ★1020 X36·成节：补之池＝Σ界−Σ旧体之实（截於其旧界後），依 补序 先短後长分之，各⛔逾其补界——全档 ≤ Σ界＋头
    诸 = [x + ('',) * (4 - len(x)) for x in 诸]       # 多源之节无「源」一格
    池 = sum(界.values()) - sum(_用(号, 体, 源) for 号, _, 体, 源 in 诸)
    额 = {}
    for 号 in 补序:
        if 号 in 补们 and any(号 == x[0] for x in 诸):
            额[号] = max(0, min(补界[号], 池))
            池 -= len(_截(补们[号][1], 额[号])[0].encode())
    出 += [节(号, 标 + (补们[号][0] if 号 in 额 else ''), 体, 源, 补们[号][1] if 号 in 额 else None, 额.get(号, 0))
          for 号, 标, 体, 源 in 诸]
    return '\n'.join(出)


def 自测():
    ok = 共 = 0
    共 += 1; ok += 行们('a\nb 12\nc', r'12', 1, 1) == '1｜a\n2｜b 12\n3｜c'
    共 += 1; ok += 节('三', '', '') == '\n## 【三】\n\n（无）\n'
    t = 汇(388)
    共 += 1; ok += all(k in t for k in ('【一】前章回执之式', '| 387 | 锁定 |', '【四】全书记忆', '【五】本章白文里出现之人', '【九】下一章（389）'))
    共 += 1; ok += ('### 刘二' in t or '### 钱满' in t)                  # 在场之人认得出（册之式 1015 自测逮：旧当作 dict）
    # ★1016（393 封版逮）：量限不钉 388——其料取自日增之账（总览、物件、状态册），钉旧章则账一长即红（二十八之家）；量今之末章
    末 = max([int(m.group(1)) for f in glob.glob(os.path.join(ROOT, '版本', '第*章')) for m in [re.search(r'第(\d+)章$', f)] if m and 章白(int(m.group(1)))[0]] or [388])
    t末 = 汇(末)
    共 += 1; ok += len(t末.encode()) <= 限
    # ★1113 X101②：N≥453 【一】补回执闸诸键之行（前章回执·「- **键**」之式）；452 ⛔补
    共 += 1; ok += (lambda f: (not f) or (lambda t: '〔补·回执闸诸键之行' in t and '- **伏笔**' in t)(汇(453)))(
        glob.glob(os.path.join(ROOT, '设定', '回执_*_第452章封版席.md'))) and '〔补·回执闸诸键之行' not in 汇(452)
    # ── ★1020 W53·X15 之格 ──
    # ⑥节之界：逾界即截、印其略；Σ界＋诸题之界 < 限（结构上逾不了——旧无界，394 161KB）
    大 = 节('一', '甲', '\n'.join('行%05d' % i for i in range(5000)), 'x.md')
    共 += 1; ok += (len(大.encode()) <= 界['一'] + 300 and '逾界' in 大 and 'x.md' in 大 and sum(界.values()) + 头之界 < 限)
    # ⑦回灌旧病（料随章长与在场人数而涨）：八倍之章、全册之人俱在场——记料仍 ≤ 限（旧式量之 ≫150KB）
    _册 = json.load(open(os.path.join(ROOT, 册档), encoding='utf-8'))
    _诸名 = '、'.join(re.sub(r'（[^）]*）', '', v.get('名') or '') for v in _册.get('人物') or [])
    _f, _白 = 章白(末)
    _旧章白, _旧白行 = globals()['章白'], globals()['_白行']
    _p, _L = _白行(末)
    try:
        globals()['章白'] = lambda n, root=ROOT: (_f, (_白 + _诸名 + '\n') * 8)
        globals()['_白行'] = lambda n, root=ROOT: (_p, _L * 8)
        胀文 = 汇(末)
        胀 = len(胀文.encode())
    finally:
        globals()['章白'], globals()['_白行'] = _旧章白, _旧白行

    def _头(t):
        """诸节之体以外之字节：档头、节题、逾界之注（结构之界里「头之界」所管者）。"""
        n, 入 = 0, False
        for l in t.split('\n'):
            入 = 入 or l.startswith('## 【')
            if not 入 or l.startswith(('## 【', '（本节逾界')):
                n += len(l.encode()) + 1
        return n
    # ★1020 X15 验席（头之界只是自测里一个常数，码里不强制）：压测之档头、节题、逾界之注实量 ≤ 头之界，则 Σ界＋头之界 < 限 方成其证
    共 += 1; ok += 胀 <= 限 and _头(胀文) <= 头之界 and 胀 <= sum(界.values()) + 头之界
    # ⑧回灌旧病（暗线·她之镜之章无一人在场）：397 之「她」须认作沈鸢（旧以 str(别称) 拆，395、397 五、十一两节空）
    _, 白397 = 章白(397)
    共 += 1; ok += ('沈鸢' in [x[0] for x in 在场(白397, 397, _册)] and '霍钧' not in [x[0] for x in 在场(白397, 397, _册)])
    # ⑨回灌旧病（引档之节撞记料之节）：记料里「## 」起之行唯自家之「## 【」
    共 += 1; ok += all(l.startswith('## 【') for l in t末.split('\n') if l.startswith('## '))
    # ⑩回灌旧病（检察官之行恒空：旧式「^ N:」认不着四格缩进）：末章之记料须带 OPEN_BRIEF_CARD_SCHEMA 本章之行
    共 += 1; ok += bool(re.search(r'\d+｜\s+%d:\s*\(' % 末, t末))
    # ── ★1020 X15·独立验席所逮（【九】之界与段案之取相撞、逾界之注指错档、【八】锚行印两回）之格 ──
    # ⑪回灌旧病（段案之取连附录）：段案档末一章之後之「## 附一·落账」⛔取入（旧式止於「## 数」，400 之节取成 16KB）；附录入目、带行号
    import tempfile, shutil
    _d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(_d, '设定', '段案'))
        open(os.path.join(_d, '设定', '段案', '1-2.md'), 'w', encoding='utf-8').write(
            '# 段案·1—2\n> 律\n## 1\n- 一\n## 2\n- 二\n## 附一·落账\n| 甲 |\n')
        _源, _文, _目 = _段案(2, _d)
    finally:
        shutil.rmtree(_d, ignore_errors=True)
    共 += 1; ok += (_源 == os.path.join('设定', '段案', '1-2.md') and _文 == '## 2\n- 二' and _目 == ['段头 :1—2', '附一·落账 :7—8']
                    and all(not re.search(r'^## (?!%d\s*$)' % n, _段案(n)[1], re.M) for n in range(末 - 15, 末 + 4)))
    # ⑫回灌旧病（逾界之注指错档）：多源之节，注只列被截诸片之源——截在尾片者⛔列前片；截入前片者两源俱列
    _短, _长 = '322｜| 398 | 主·157 |', '\n'.join('段%05d' % i for i in range(4000))
    _甲 = 节('九', '', [('纲.md', _短), ('段.md', _长)])
    _乙 = 节('九', '', [('段.md', _长), ('纲.md', _短)])
    共 += 1; ok += (_短 in _甲 and '所略之源 段.md——' in _甲 and '纲.md' not in _甲.split('（本节逾界')[1]
                    and '所略之源 段.md、纲.md' in _乙)
    # ⑬回灌旧病（总纲、余章总案之行被段案挤掉）：【九】总纲、余章总案在前，段案之节殿後；段案之节⛔带附录
    _九 = t末.split('## 【九】')[1].split('\n## 【')[0] if '## 【九】' in t末 else ''
    _位 = [_九.find(x) for x in ('〔总纲·', '〔余章总案·', '之节；段头与附录不汇')]
    共 += 1; ok += (0 <= _位[0] < _位[1] and (_位[2] < 0 or _位[1] < _位[2]) and '〉## 附' not in _九
                    and (('（本节逾界' not in _九) or re.search(r'所略之源 设定/段案/[^、—]+——', _九) is not None))
    # ⑭回灌旧病（【八】锚行印两回：398 前章之条含 9924—9926）：圣经之行号於【八】只现一回
    def _八号(t):
        八 = t.split('## 【八】')[1].split('\n## 【')[0]
        锚, 条 = 八.split('〔检察官')[0], (八.split('〔圣经·第')[1] if '〔圣经·第' in 八 else '')
        return re.findall(r'^(\d+)｜', 锚, re.M), re.findall(r'^(\d+)｜', 条, re.M)
    t398 = 汇(398)
    _锚号, _条号 = _八号(t398)
    共 += 1; ok += bool(_锚号) and not set(_锚号) & set(_条号) and len(_锚号) == len(set(_锚号))
    # ── ★1020 X36 之格（四样各一格，并补之池一格）；钉已封之 399（七份构思、黎东来镜、卡引圣经：1950、:2644、管章的人只以纸到场）──
    t399 = t末 if 末 == 399 else 汇(399)

    def _节(t, k):
        return t.split('## 【%s】' % k)[1].split('\n## 【')[0] if '## 【%s】' % k in t else ''
    _T = 读(表)
    _卡399 = 读(os.path.join('版本', '第399章', '_开镜卡.md'))
    # ⑮回灌旧病（满分之问只列档名，399 记席甲、己、庚另 sed）：七份之「## 满分之问」头行带其行号俱在【七】之补；三种写法俱在拍表之前；
    #   拍表或全在、或其略注明其源（池不足时先截拍表）
    _七 = _节(t399, '七')
    _构 = sorted(glob.glob(os.path.join(ROOT, '版本', '第399章', '起草_*_构思.md')))
    _头行 = []
    for p in _构:
        L = open(p, encoding='utf-8').read().split('\n')
        i = next((i for i, l in enumerate(L) if l.startswith('#') and '满分之问' in l), None)
        _头行.append('%d｜%s' % (i + 1, L[i]) if i is not None else None)
    _补位 = _七.find('〔补·诸构思')
    _表位 = [_七.find('·满分之问之拍表〕')] + [_七.find(h) for h in _头行 if h]
    #   ★1020 X36 驳席：圈号起之「② ## 满分之问」「② 满分之问」（386—397 十八份；397 甲、戊）须认得、止於「③」行之前
    _圈 = [_满分之段(open(os.path.join(ROOT, '版本', '第397章', '起草_%s_构思.md' % g), encoding='utf-8').read()) for g in '甲戊']
    共 += 1; ok += (len(_构) == 7 and all(_头行) and 0 <= _补位 < min(_表位[1:])
                    and (max(_表位[1:]) < _表位[0] or (_表位[0] < 0 and '（本节逾界·补额' in _七))   # 驳席：拍表全截（账长池瘦）亦合其注，⛔红
                    and ('（本节逾界·补额' not in _七 or re.search(r'补额.*所略之源 版本/第399章/起草_._构思\.md', _七) is not None)
                    and _满分之段('# 题\n① 甲\n② 满分之问\n- 写法甲\n③ 乙') == '3｜② 满分之问\n4｜- 写法甲'
                    and _圈[0].startswith('7｜② ## 满分之问') and _圈[1].startswith('4｜② 满分之问')
                    and not any(re.search(r'^\d+｜③', x, re.M) for x in _圈))
    # ⑯回灌旧病（同镜前章之悬账另翻）：399 黎东来镜之同镜前章係 389（⛔同线 397）、395 她之镜越 389 黎东来、391／393 霍钧取 387；
    #   本章锁定行未立（记席跑记料之时）则取卡之「本章之镜」；同镜无前（391 霍钧首见）照旧取同线；【二】之补带 389 之悬账行
    #   ★X43⑧：【二】与【十】同取 _承前之章（开镜庭之尺；自家 _同镜·六十章窗已删——⛔两尺并存）
    共 += 1; ok += (_承前之章(399, _卡399)[:3] == (389, '同镜', '黎东来') and _承前之章(399, '- **本章之镜**：黎东来（第三人称）\n')[:2] == (389, '同镜')
                    and _承前之章(395, '')[0] == 387 and _承前之章(391, '')[1] == '同线'
                    and _承前之章(396, '')[0] == 394       # 驳席：锁定行「镜：我」须归一作苏衍（⛔跳去 374 之「我」）
                    and '_同镜' not in globals()
                    and re.search(r'^\d+｜\| 389 \| 悬账 \|', _节(t399, '二'), re.M) is not None
                    and re.search(r'^\d+｜\| 396 \| 悬账 \|', _节(t398, '二'), re.M) is not None)
    # ⑰回灌旧病（卡所引圣经行料外另查）：「圣经：1950、:2644」「圣经：12—14」之认；399 之【八】印 1950、2644 各一回，【八】之行号⛔重
    _八 = _节(t399, '八')
    _八号们 = re.findall(r'^(\d+)｜', _八.split('〔检察官')[0] + '\n' + _八.split('〔圣经·第')[-1], re.M)
    _经 = '圣经' + ':'   # ★1020：拆字以免圣经引号之闸认作在役之引
    共 += 1; ok += (_圣经之引(_经 + '1950、:2644；`圣经：12—14`，圣经七·9') == [1950, 2644, 12, 13, 14]
                    and _圣经之引('`' + _经 + '7408`／`:8161`；`' + _经 + '8496`／`施工表:305`；' + _经 + '1950—52') == [7408, 8161, 8496, 1950]
                    and '\n1950｜' in _八 and '\n2644｜' in _八 and len(_八号们) == len(set(_八号们)))
    # ⑱回灌旧病（只以纸到场之人不在【五】）：管章的人（399 卡·问九之二之注）入【五】【十一】之补；「永不回」之句⛔收（录入的那个）；白文之人仍在补前
    _五, _十一 = _节(t399, '五'), _节(t399, '十一')
    _卡人, _无册 = _卡之人('## 问九之二\n- **甲某**｜在场\n- **乙某**（不出场）｜x\n  - 注：丙某只以纸到场；丁某永不回\n---\n- **戊某**',
                         {'人物': [{'名': n} for n in ('甲某', '乙某', '丙某', '丁某', '戊某')]}, {'甲某'})
    共 += 1; ok += ('### 管章的人（卡·问九之二所列' in _五 and '录入的那个' not in _五 and '〔管章的人·' in _十一
                    and -1 < _五.find('### 黎东来') < _五.find('〔补·卡') and [x[0] for x in _卡人] == ['乙某', '丙某'] and _无册 == [])
    # ⑲补之池：旧体先截於其旧界、一字不让补；补殿其後、截於补额而注其源；399、398 之记料 ≤ Σ界＋头之界
    _旧 = 节('九', '', [('纲.md', _短), ('段.md', _长)])
    _新 = 节('九', '', [('纲.md', _短), ('段.md', _长)], 补=[('补.md', '\n'.join('补%04d' % i for i in range(900)))], 补额=2000)
    共 += 1; ok += (_新.startswith(_旧.rstrip('\n')) and '补0000' in _新 and '补0899' not in _新
                    and re.search(r'（本节逾界·补额 2000 字节：补下略 \d+ 行.*所略之源 补\.md——', _新) is not None
                    and max(len(t399.encode()), len(t398.encode())) <= sum(界.values()) + 头之界)
    # ── ★1021 X42 之格（W60 席四驳後：⑳㉑改以造局测——余章总案将由 401 段剧情庭改写，⛔钉真档之行号与字面；真档只余㉗一格冒烟）──
    _接 = '## 四\n- 400 主 天亮甲。401 暗 她乙\n- 402 主 丙'       # 401 接在 400 之行末（旧余章:66 之形）
    _独 = '## 四\n- 400 主 天亮甲\n- 401 暗 她乙\n- 402 主 丙'      # 401 独成一行
    # ⑳回灌旧病（「401 暗」接在 400 之行末，【九】旧印「（无）」）：行中之「N 主／N 暗」（连「419／421／423 暗」「430—434 主」）认得、
    #   一条归一章；401 独行与接在 400 行末俱认
    共 += 1; ok += (_余章之条(_接, 401) == [(2, '401 暗 她乙', True, False)]
                    and _余章之条(_独, 401) == [(3, '- 401 暗 她乙', False, False)]
                    and _余章之条('- 400 主 甲。〔据〕401 暗 乙。', 401) == [(1, '401 暗 乙。', True, False)]
                    and _余章之条('x。419／421／423 暗 丙｜y。430—434 主 丁', 421) == [(1, '419／421／423 暗 丙｜y。', True, True)]
                    and [x[1] for x in _余章之条('x。430—434 主 丁', 432)] == ['430—434 主 丁'])
    # ㉑行首之认⛔坏：行首之条照认（连旧式无主暗之「- N 」、缩进之子条）、止於同行他章之头；无句读之引⛔切
    共 += 1; ok += (_余章之条(_接, 400) == [(2, '- 400 主 天亮甲。', False, True)]
                    and _余章之条(_独, 400) == [(2, '- 400 主 天亮甲', False, False)]
                    and _余章之条('- 402 照旧式\n  - 443 暗 子条', 402) == [(1, '- 402 照旧式', False, False)]
                    and _余章之条('- 402 照旧式\n  - 443 暗 子条', 443) == [(2, '  - 443 暗 子条', False, False)]
                    and _余章之条('- 400 主 与 390 主线同；照 391 暗之数，与 392 主·154 同一天', 400) == [
                        (1, '- 400 主 与 390 主线同；照 391 暗之数，与 392 主·154 同一天', False, False)]
                    and _余章之条('- 400 主 与 390 主线同；照 391 暗之数', 390) == [])
    # ㉑之二（驳席：_条头 之 lookahead 旧无一格咬得住——上格「与 390 主线」无句读在前，删 lookahead 亦绿）：
    #   句读之後之「N 主线」「N 暗线」⛔切（删 lookahead 即红）；「N 暗：」照切
    _防 = '- 400 主 甲。390 主线之事；391 暗线之数〕392 暗：乙'
    共 += 1; ok += (_余章之条(_防, 390) == [] and _余章之条(_防, 391) == []
                    and _余章之条(_防, 400) == [(1, '- 400 主 甲。390 主线之事；391 暗线之数〕', False, True)]
                    and _余章之条(_防, 392) == [(1, '392 暗：乙', True, False)])
    # ── 造局之盘（tempdir）：一〇一—一〇六 六章（单暗双主）、总纲、余章总案、二卡、open_brief——汇 之接线以造局测；
    #    开镜庭之线表、镜表以替身注入（_同镜之前、_镜之正、_答 用其真者——⛔另抄一把）──
    import types
    import 第零轮开镜庭 as _庭
    _局 = tempfile.mkdtemp()
    _假线 = {k: '暗' if k % 2 else '主' for k in range(101, 107)}

    def _写(p, t):
        p = os.path.join(_局, p)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8').write(t)

    def _假庭(镜表):
        return types.SimpleNamespace(_线表=lambda: dict(_假线), _镜之表=lambda: dict(镜表),
                                     _镜之正=_庭._镜之正, _答=_庭._答, _同镜之前=_庭._同镜之前)
    _真承 = _承前之章

    def _局汇(n, 镜表):
        globals()['_承前之章'] = lambda N, 卡, root=ROOT, 庭=None: _真承(N, 卡, root, _假庭(镜表))
        try:
            return 汇(n, _局)
        finally:
            globals()['_承前之章'] = _真承
    try:
        for k in range(101, 107):
            _写(os.path.join('正文', '镇冢秘术_第一百零%s章_局.md' % '一二三四五六'[k - 101]),
                '\n'.join('章%d行%d' % (k, i) for i in range(1, 7)) + '\n【本章亮点】\n- 亮')
        _写(os.path.join('设定', '02_余章之势_总纲.md'), '\n'.join('| %d | %s·1 |' % (k, _假线[k]) for k in range(101, 107)))
        _写(表, ''.join('| %d | 锁定 | 《局》%s |\n| %d | 悬账 | 局悬%d |\n' % (k, '**镜：沈鸢**' if k == 101 else '', k, k) for k in range(101, 107)))
        _写(os.path.join('版本', '第105章', '_开镜卡.md'), '## 问二·本章之镜\n- **本章之镜**：沈鸢（白文只作「她」）\n- 接钩：照 102:2，又 101:2\n')
        _写(os.path.join('版本', '第106章', '_开镜卡.md'), '- 钩：照 102:3\n')
        _写(os.path.join('设定', 'canon事实库.json'), json.dumps({'open_brief': {'钩': '照 102:4'}}, ensure_ascii=False))
        _九们 = []
        for _案 in (_接, _独):
            _写(os.path.join('设定', '剧情庭题', '余章总案.md'), _案.replace('400', '104').replace('401', '105').replace('402', '106'))
            _九们.append(_节(_局汇(104, {}), '九'))
        _汇105 = _局汇(105, {101: '沈鸢', 103: '黎东来'}); _十, _二 = _节(_汇105, '十'), _节(_汇105, '二')
        _汇105未 = _局汇(105, {101: '沈鸢'}); _十未, _二未 = _节(_汇105未, '十'), _节(_汇105未, '二')
        _十空 = _节(_局汇(101, {}), '十')
        _卡105 = 读(os.path.join('版本', '第105章', '_开镜卡.md'), _局)
        _败 = _真承(105, _卡105, _局, types.SimpleNamespace())          # 庭之器缺
        _旧模 = sys.modules.get('第零轮开镜庭')
        sys.modules['第零轮开镜庭'] = None                                  # import 第零轮开镜庭 即败
        try:
            _败2 = _真承(105, _卡105, _局)
        finally:
            sys.modules['第零轮开镜庭'] = _旧模
        _主 = _真承(104, '', _局, _假庭({}))
        # ㉚之局（★1118 悬念哨→改）：段案 101-106 之「## 105」节有 SUS 之行、「## 104」节无；段头与「## 106」之 SUS 行⛔入 105 之补——前汇俱毕方写（⛔扰上之诸局）
        _写(os.path.join('设定', '段案', '101-106.md'), '# 段案 101—106（局）\n> - **悬念哨三账**：SUS-A 段头之行\n'
            '## 104\n- 种：无悬\n- 物之动：拍一·甲\n'
            '## 105\n- 种：收「册」——SUS-C 复提：那一沓贴其外\n- 守：二线律\n- 物之动：**拍一**：那一沓贴在判词外头（SUS-C）；拍二·SUS-A 页头落日\n'
            '## 106\n- 种：SUS-B 柄窝\n')
        for k in (103, 104):
            _写(os.path.join('设定', '回执_20260101_第%d章封版席.md' % k), '# 回执·%d（局）\n\n## 一·数\n- 甲\n' % k)
        _一105, _一104 = [_局汇(n, {}).split('\n## 【一】')[1].split('\n## 【')[0] for n in (105, 104)]   # 档头之注亦含「## 【一】」——⛔用 _节
    finally:
        shutil.rmtree(_局, ignore_errors=True)
    # ㉚★1118 总编辑复核「悬念哨→改」（改其供⛔改其判）：本章段案之节内提 SUS-A／B／C 之行逐字（带整档行号）并第二路之严式殿【一】之补；
    #   段头、他章之节之 SUS 行⛔入；节内无者⛔印（【一】照立）——旧码⛔一字教记席书「SUS-X·本章复提」（461—467 四笔实落而失记）
    共 += 1; ok += ('〔补·本章（105）段案所排之悬念拍（设定/段案/101-106.md「## 105」' in _一105
                    and '\n如本章正文实落其拍，骨记（或回执）须书一行：SUS-X·本章复提：<拍号或逐字 ≥8 字>；未落者⛔书（⛔凭段案代正文）\n' in _一105
                    and '\n7｜- 种：收「册」——SUS-C 复提：那一沓贴其外\n' in _一105
                    and '\n9｜- 物之动：**拍一**：那一沓贴在判词外头（SUS-C）；拍二·SUS-A 页头落日' in _一105
                    and all(k not in _一105 for k in ('8｜- 守', 'SUS-A 段头', 'SUS-B 柄窝'))
                    and '本章段案所排之 SUS 拍' in _一105.split('\n')[0])
    共 += 1; ok += (_一104.startswith('前章回执之式') and all(k not in _一104 for k in ('本章复提', '段案所排', 'SUS')))
    # ⑳之二（造局·汇之接线）：【九】汇本章与下一章之条——下一章（105）接在本章（104）之行末者（「…」起）、独行者俱入本章之料
    共 += 1; ok += ('\n2｜- 104 主 天亮甲。…\n' in _九们[0] and '\n2｜…105 暗 她乙\n' in _九们[0] + '\n'
                    and '\n2｜- 104 主 天亮甲\n' in _九们[1] and '\n3｜- 105 暗 她乙\n' in _九们[1] + '\n')
    # ㉒之二（驳席：远源三路旧只本章卡一路有格）——造局各引一处主线 102 之行（⛔承前之章，与其选章无涉；删一路即红）：本章卡｜下一章卡｜open_brief
    共 += 1; ok += '\n- 102:2　章102行2' in _十
    共 += 1; ok += '\n- 102:3　章102行3' in _十
    共 += 1; ok += '\n- 102:4　章102行4' in _十
    # ㉔（驳席①·造局）承前之章与开镜庭接钩同尺：暗线换镜者取同镜之前（105 沈鸢镜→101，⛔同线之 103 黎东来镜），
    #   其白文全收、卡引 101 只列其号；主线照取同线、⛔印由
    共 += 1; ok += (_十.startswith('同镜前章（第101章·沈鸢镜') and '同线前章係第103章' in _十.split('\n')[0]
                    and '\n1｜章101行1' in _十 and '承前取同线' not in _十
                    and re.search(r'见前文白文.*101:2', _十) is not None and '\n- 101:2' not in _十
                    and _主 == (102, '同线', None, None, 102))
    # ㉔之二（X43⑧·造局）一尺：【二】之补与【十】同章——同镜取得 101 者【二】补 101 之悬账；103 之镜未钉（庭止於 103·⛔越过去取 101）
    #   者【二】补同线 103 之悬账（旧自家 _同镜 以六十章窗越过 103 取 101，与【十】分岔）；换镜之【十】附同线前章（103）之末五段
    共 += 1; ok += ('局悬101' in _二 and '同镜前章（第101章' in _二 and '局悬103' not in _二
                    and '局悬103' in _二未 and '同线前章（第103章' in _二未 and '局悬101' not in _二未
                    and '〔同线前章·正文/镇冢秘术_第一百零三章_局.md 之末五段' in _十
                    and all('\n%d｜章103行%d' % (i, i) in _十 for i in range(2, 7)) and '\n1｜章103行1' not in _十
                    and '同线前章·' not in _十未)
    # ㉕（驳席①·造局）同镜取不着即照旧取同线、料中印一行「承前取同线·镜未定之由」：_同镜之前 返 None（103 之镜未钉·⛔跨过去猜）｜
    #   本章之镜认不着（无白文可附者【十】仍立以印其由）｜庭之器缺｜import 第零轮开镜庭 败
    共 += 1; ok += (_十未.startswith('同线前章（第103章）') and '\n〔承前取同线·镜未定之由：沈鸢镜·第103章之镜锁定行未钉〕\n' in _十未
                    and '\n1｜章103行1' in _十未
                    and '〔承前取同线·镜未定之由：本章之镜认不着' in _十空
                    and _败[:3] == (103, '同线', None) and '第零轮开镜庭' in (_败[3] or '')
                    and _败2[:2] == (103, '同线') and 'Error' in (_败2[3] or '') and '第零轮开镜庭' in (_败2[3] or ''))
    # ── 真档 ──
    t401 = t末 if 末 == 401 else 汇(401)
    _卡 = {n: 读(os.path.join('版本', '第%d章' % n, '_开镜卡.md')) for n in range(385, 402)}
    # ㉖（驳席①·真档之证）401→397（沈鸢镜·⛔同线之 399 黎东来镜）、399→389（黎东来镜）；主线 400→398、398→396 不变（⛔印由）；
    #   385—401 诸章之取与开镜庭 _接钩之前 一一相合（同镜之前有者同、无者回落同线）——两处之尺一分岔即红
    _合 = []
    for n in range(385, 402):
        if _卡[n]:
            _k庭, _k料 = _庭._接钩之前(n, _卡[n])[0], _承前之章(n, _卡[n])
            _合.append(_k料[0] == _k庭 and _k料[1] == '同镜' if _k庭 else _k料[1] == '同线')
    共 += 1; ok += (_承前之章(401, _卡[401])[:2] == (397, '同镜') and _承前之章(399, _卡[399])[:2] == (389, '同镜')
                    and _承前之章(400, _卡[400])[:4] == (398, '同线', None, None) and _承前之章(398, _卡[398])[:4] == (396, '同线', None, None)
                    and len(_合) >= 15 and all(_合)
                    and _节(t401, '十').startswith('同镜前章（第397章·沈鸢镜') and _节(t398, '十').startswith('同线前章（第396章）')
                    and '承前取同线' not in _节(t398, '十'))
    # ㉗真档之冒烟（⛔钉行号、⛔钉字面）：401 之料【九】含余章总案 401 之诸条（条自真档现认）
    _401 = _余章之条(读(os.path.join('设定', '剧情庭题', '余章总案.md')), 401)
    共 += 1; ok += bool(_401) and all(('\n%d｜%s%s' % (i, '…' if 中 else '', 片)) in _节(t401, '九') for i, 片, 中, _ in _401[:6])
    # ㉒远引汇入（400 记席另 awk 383:93—103、395:87、397:91）：卡、open_brief 所引之远章「章:行」「章:行—行」照 章料.引之原句 展於【十】之补；
    #   【十】白文已全收之章（401 之同镜前章 397）只列其号；401 之卡所引之章引（非全收、行在章内且非空）俱在【十】（逾补额者其注列源）
    import 章料
    _f395 = 章料.章档(395); _L395 = open(_f395, encoding='utf-8').read().split('\n')
    _远 = _远引('照 395:87、383:93—103，又 399:115、总纲:1、D3:1', ROOT, {399})
    _十401 = _节(t401, '十')
    _该, _收 = [], []
    for m in 章料._引式.finditer(_卡[401]):
        if m.group(1).isdigit() and 章料.章档(int(m.group(1))):
            if int(m.group(1)) == 397:
                _收.append(m.group(0)); continue
            _Lk = open(章料.章档(int(m.group(1))), encoding='utf-8').read().split('\n')
            if 1 <= int(m.group(2)) <= len(_Lk) and _Lk[int(m.group(2)) - 1].strip():
                _该.append(m.group(0))
    共 += 1; ok += (len(_远) == 3 and _远[0] == '- 395:87　' + _L395[86].strip()[:400] and _远[1].startswith('- 383:93—103\n  93｜')
                    and '见前文白文' in _远[2] and '399:115' in _远[2] and not any('总纲' in x or 'D3' in x for x in _远)
                    and '〔补·卡所引远章之原句' in _十401 and _该 and _收
                    and (all(('\n- %s' % k) in _十401 for k in _该)          # 卡日後添引而逾补额者：注须列其源（⛔无声而丢）
                         or re.search(r'（本节逾界·补额.*所略之源 版本/第401章/_开镜卡\.md', _十401) is not None)
                    and (re.search(r'见前文白文.*397:', _十401) is not None or '（本节逾界·补额' in _十401)   # ★1023 406 封版逮：open_brief 日长、补额溢则此注随略（略注已列其源）
                    and '\n- 397:' not in _十401)
    # ㉓引越章长⛔崩：行号逾章长⛔展、行段逾章末截於章末（且一段至多三十行）、无其章⛔展；t401 ≤ 限
    _n400 = len(open(章料.章档(400), encoding='utf-8').read().split('\n'))
    _越 = _远引('400:%d、400:%d—%d、400:5—9999、9999:3、999:1' % (_n400 + 5, _n400 - 2, _n400 + 40), ROOT)
    _号 = [int(x) for x in re.findall(r'^\s+(\d+)｜', '\n'.join(_越), re.M)]
    共 += 1; ok += (not any(x.startswith('- 400:%d　' % (_n400 + 5)) for x in _越) and not any('9999:3' in x or '999:1' in x for x in _越)
                    and any(x.startswith('- 400:5—9999\n  5｜') for x in _越) and _号 and max(_号) <= _n400
                    and all(x <= 5 + 29 for x in _号 if x < _n400 - 2) and len(t401.encode()) <= 限)
    # ㉔★1024 器格之注：N≥411 方立（N≤410 之料一字不变）；其注点 记落.py 与大审诸号、⛔逾头之界
    共 += 1; ok += (('★器格' in t末) == (末 >= 411) and ('★器格' not in t399) and _头(t末) <= 头之界
                    and ('`python3 工具/记落.py %d`' % 末 in t末 if 末 >= 411 else True))
    # ㉕★X91③：轮记之盲读、逻辑审全节入【七】之补（432 记席多读一回 13—95 行）；无轮记者 []
    _轮 = _轮记之审(os.path.join('版本', '第433章', '_轮记.md'))
    共 += 1; ok += (len(_轮) == 2 and '盲读' in _轮[0][1] and '逻辑审' in _轮[1][1] and '读误之判' in _轮[1][1]
                    and _轮记之审(os.path.join('版本', '第9999章', '_轮记.md')) == [])
    # ㉖★X95②：胜稿与嫁大进之稿之构思——钉 439（稿三胜＝丁、大进嫁稿二＝丙；蒙号轮转 (干序+N)%宽）；行家评无名次者原样返
    _目 = os.path.join('版本', '第439章')
    _c = sorted(glob.glob(os.path.join(ROOT, _目, '起草_*_构思.md')))
    共 += 1; ok += ([os.path.basename(x) for x in _胜嫁之构思(_c, _目, 439)] == ['起草_丁_构思.md', '起草_丙_构思.md']
                   and _胜嫁之构思(_c, os.path.join('版本', '无此章'), 439) == _c) if len(_c) == 5 else 0
    # ㉗★X97（446）：前回之审只留判行、拍表只附胜稿——钉 445（逻辑审二回、盲读二回；稿二胜＝乙）
    _轮5 = _轮记之审(os.path.join('版本', '第445章', '_轮记.md'), 末回=True)
    _c5 = sorted(glob.glob(os.path.join(ROOT, '版本', '第445章', '起草_*_构思.md')))
    _取5 = _胜嫁之构思(_c5, os.path.join('版本', '第445章'), 445); _胜5 = _胜嫁之构思(_c5, os.path.join('版本', '第445章'), 445, 只胜=True)
    _满5 = _满分之问(_取5, 表只=_胜5)
    共 += 1; ok += (len(_轮5) == 4 and sum('前回' in x[1].split('\n')[0] for x in _轮5) == 2
                    and sum(len(x[1].encode()) for x in _轮5) < sum(len(x[1].encode()) for x in _轮记之审(os.path.join('版本', '第445章', '_轮记.md'))) * 0.75
                    and len(_胜5) == 1 and sum('拍表〕' in x[1] for x in _满5) == 1) if len(_c5) == 5 else 0
    # ㉘★X100④（450）：近三章之向形——造局於字串（⛔钉盘上会长之表）：N≥450 出三行、缺者注之；N≤449 ⛔出
    _T = '| 447 | 锁定 | 甲｜**本章之向：往内｜形：记账｜品：暗**｜**式：x**\n| 449 | 锁定 | 乙｜**本章之向：往外｜形：取信｜品：暗**\n'
    _向 = 近三之向形(_T, 450)
    共 += 1; ok += ('- 447：本章之向：往内｜形：记账｜品：暗' in _向 and '- 448：（锁定行无「本章之向」）' in _向
                    and '- 449：本章之向：往外｜形：取信｜品：暗' in _向 and 近三之向形(_T, 449) == '')
    # ㉙★1118（a9e5cc5ee 根病一：【四】截自尾起，E8 今站块逐章长，先截前章之记、次截用法 §六之式——461、462 记席未见「## 一句之要」而漏写，
    #   章料·剧情链红）：造局三样（今站块六十章｜并「全书今之末」二万字｜并索引末行三万字）——用法 §五§六（连「## 一句之要」）、人物锚行恒全收；
    #   ①今站块只略旧章之行（末二章之行、线与日、读者之所欠、题、索引末三行⛔略；略处印其行段与 sed -n），前章之记·式样仍在；
    #   ②「全书今之末」截其尾而留其首；③片截於其额而注其路；未逾者（三章之站）一字不略、无略注
    _局4 = tempfile.mkdtemp()

    def _造4(站数, 末字, 索末):
        _记4 = os.path.join(_局4, 记)
        os.makedirs(_记4, exist_ok=True)
        open(os.path.join(_记4, '用法.md'), 'w', encoding='utf-8').write(
            '# 用法\n## 五、⛔规矩\n1. 规矩甲\n## 六、逐章详记之式\n```\n# 第N章《章名》\n## 发生了什么\n## 读之得\n## 一句之要\n```\n- 写毕自核\n## 七、诸裁\n- 裁\n')
        站行 = ['- **%s·%d（局）**：%s' % ('暗线' if k % 2 else '主线', k, '甲' * 300) for k in range(511 - 站数, 511)]
        open(os.path.join(_记4, '总览.md'), 'w', encoding='utf-8').write(
            '# 全书记忆·总览（至第 510 章）\n\n**全书今之末**：' + '乙' * 末字 + '\n## ② 按站\n### E8 局（写至 510）\n- **线与日**：丙\n' +
            '\n'.join(站行) + '\n- **E8 读者之所欠（至 510）**：丁\n\n### 此後\n## ③ 逐章索引\n| 509 | 戊 |\n| 510 | ' + '己' * 索末 + ' |\n')
        open(os.path.join(_记4, '人物.md'), 'w', encoding='utf-8').write('# 人物\n> 今之行止（局）：庚\n')
        open(os.path.join(_记4, '第510章.md'), 'w', encoding='utf-8').write('# 第510章\n## 发生了什么\n1. 辛\n## 一句之要\n壬\n')
        globals()['_承前之章'] = lambda N, 卡, root=ROOT, 庭=None: (None, '同线', None, None, None)
        try:
            return _节(汇(511, _局4), '四')
        finally:
            globals()['_承前之章'] = _真承
    try:
        _四们 = [_造4(*x) for x in ((3, 100, 1), (60, 1000, 1), (60, 20000, 1), (60, 1000, 30000))]
    finally:
        shutil.rmtree(_局4, ignore_errors=True)
    _用 = ['〔用法.md:2—11〕\n〉## 五、⛔规矩\n1. 规矩甲\n〉## 六、逐章详记之式', '〉## 一句之要\n```\n- 写毕自核', '〔人物.md·', '今之行止（局）：庚']
    共 += 1; ok += (all(all(k in x for k in _用) for x in _四们)
                    and all(len(x.split('\n', 1)[1].split('\n（本节逾界')[0].strip().encode()) <= 界['四'] for x in _四们)
                    and all('- **%s·%d（局）**' % ('暗线' if k % 2 else '主线', k) in _四们[0] for k in (508, 509, 510))   # 未逾：三章之行俱在、无略注、前章之记全收
                    and '今站块旧章之行' not in _四们[0] and '（本节逾界' not in _四们[0] and '〉## 一句之要\n壬' in _四们[0])
    共 += 1; ok += ('今站块旧章之行 :' in _四们[1] and re.search(r'全行 sed -n \d+,\d+p 设定/全书记忆/总览\.md', _四们[1]) is not None
                    and all(k in _四们[1] for k in ('- **主线·510（局）**', '- **暗线·509（局）**', '**线与日**：丙', '读者之所欠（至 510）', '# 全书记忆·总览', '| 509 | 戊 |'))
                    and '- **暗线·451（局）**' not in _四们[1] and '〔第510章.md·式样' in _四们[1]
                    and '（全行 sed -n' not in _四们[1].split('**全书今之末**')[1].split('\n')[0])
    共 += 1; ok += ('（全行 sed -n 3 读）' in _四们[2] and '乙' * 今之末之底 in _四们[2] and '乙' * 20000 not in _四们[2]
                    and '- **主线·510（局）**' in _四们[2] and '读者之所欠（至 510）' in _四们[2])
    共 += 1; ok += ('（总览之片逾额' in _四们[3] and '己' * 30000 not in _四们[3])
    # ★X116（469）：轮记截於字节、末字残——读之⛔崩、就地去残；非轮记者只读⛔写
    import tempfile as _tf
    _局X = _tf.mkdtemp()
    try:
        _pX = os.path.join(_局X, '_轮记.md'); _qX = os.path.join(_局X, '_料.md')
        for _f in (_pX, _qX):
            open(_f, 'wb').write('## 节\n甲乙…'.encode()[:-1])
        _tX = 读(_pX, _局X); _uX = 读(_qX, _局X)
        共 += 1; ok += (_tX == '## 节\n甲乙' and open(_pX, 'rb').read() == '## 节\n甲乙'.encode()
                        and _uX == '## 节\n甲乙' and len(open(_qX, 'rb').read()) == len('## 节\n甲乙…'.encode()) - 1)
    finally:
        shutil.rmtree(_局X, ignore_errors=True)
    print('记料·自测 %d/%d（%d 之记料 %d 字节；八倍之章、全册在场 %d 字节·头 %d；399 %d 字节；限 %d）' % (
        ok, 共, 末, len(t末.encode()), 胀, _头(胀文), len(t399.encode()), 限))
    return ok == 共


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--自测']:
        sys.exit(0 if 自测() else 1)
    if len(a) == 1 and a[0].isdigit():
        N = int(a[0])
        if N >= 460:                       # ★X109：先立回执之骨（已有回执即⛔覆）
            import 记落 as _记落
            _bp = _记落.骨(N)
            if _bp:
                print('✓ 回执之骨：%s' % _bp)
        t = 汇(N)
        p = os.path.join(ROOT, '版本', '第%d章' % N, '_记料.md')
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8').write(t)
        b = len(t.encode())
        print('✓ 写 %s（%d KB）%s' % (os.path.relpath(p, ROOT), b // 1024, '' if b <= 限 else '　⛔逾 150KB（坑③）'))
        sys.exit(0 if b <= 限 else 1)
    print(__doc__); sys.exit(2)
