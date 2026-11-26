#!/usr/bin/env python3
"""造式验（1013 立·造式二代·设定/方法升级_造式二代.md §五、§九）——诸机闸一次跑完，零 token。

为何立：一代之机闸、抄袭之关、厚之关三席以模型去跑十几个器（380 机闸一席 $9、抄袭与厚之关另席），
而「跑器、看 rc、印红处」是机器之活（零 token 等效之检）。今合稿席只跑本器一回，红了只治红处。

两类（其判据逐器实测过——1013 以已封版之 380 试跑，十七器俱绿、各器红时之形查过源码）：
  致命之器（⛔绿不许交）：起草闸（rc）｜硬闸（JSON 计数有 >0 即红）｜抄袭闸（rc）｜崩坏闸（rc）｜检察官之封版门（ERROR>0 即红·N≥420·X80）｜
                         厚（净重取 工具/净重对表.py 之尺；带底：总纲本章之行 主 2500／暗 2300；
                            ★1020 X40·401 起：`分量闸.须厚` 判「非厚不可」之章，净重 <2,900 亦红；
                            〔1119 死规之审·gates6〕N≥473：唯净重 <2,000 铁底致命，带底与须厚只印 ⚠）
  报之器（红即印其末行，治或写明其由）：棘轮预检、字数闸、数闸、含拍、亮点对表、亮点界、亮点在、息日链、日差哨、器物点名、外事尺 --度、比带、咬合哨
  （「对位」查诸器之位、非本章之事，单跑约 94 秒——在全测，⛔入本器。）

用法：
  python3 工具/造式验.py N           # 跑毕印逐器一行；致命之器有红 rc=1
  python3 工具/造式验.py N --json    # 另印 JSON
  python3 工具/造式验.py N --料      # 只验料全：开镜卡、章料（≤120KB）、前两章正文；★401 起须厚之章段案「字数」之带不及 2,900 即红
                                     #   〔1119 死规之审·gates6〕N≥473：须厚之带只印 ⚠
  python3 工具/造式验.py --自测
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import os, sys, re, json, glob, time, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
致命 = [('起草闸', '{N}', 'rc'), ('硬闸', '{N}', '硬'), ('抄袭闸', '{N}', 'rc'), ('崩坏闸', '{N}', 'rc')]
# ★1104 X80（418 今:57「打那三处过」触 F007_打介词：五稿、行家、合稿、造式验俱未逮，至记席回执闸方露·记席多花六回）：
#   N≥420 起检察官之封版门（canon 之 F 条 ERROR）入致命之器——合稿时即逮；N≤419 旧行不变
察起 = 420
报 = [('棘轮预检', '{N}'), ('字数闸', '{N}'), ('数闸', '{N}'), ('含拍', '{N}'), ('亮点对表', '{N}'), ('亮点界', '{N}'),
     ('亮点在', '{N}'), ('息日链', ''), ('日差哨', ''), ('器物点名', '{N}'), ('外事尺', '--度 {N}'), ('比带', '{N}'),
     ('咬合哨', ''), ('质量三闸', '--一日 {N}')]   # ★1105 质量三闸①之c 合稿即见（424 至记席方报）；★1014：381—385 无一章报咬合，推时方红（坑㉖）——合稿时即见
带底 = {'主': 2500, '暗': 2300}
# ★1020 X40（瑕疵总账·裁_1020_推闸二红_399封版後）：`分量闸.须厚` 判「非厚不可」之章，399 只写进开镜卡、⛔入闸——
#   执笔七席照段案之带「2,300—2,900」写成 2303—2461，末稿 2580，分量闸·暗线之厚红於推闸（又一道只在事後说话的闸）。
#   ★故 401 起两验俱在落笔之前或合稿之时说话：①合稿之验（厚）：须厚之章净重 <暗厚 即⛔红；
#   ②--料 之验：须厚之章，段案本章「字数」之带不及暗厚即⛔红（其判在 段案验.须厚之带红·与 段案验 同一把）。
#   ⛔N≤400 之判一格未动（须厚起 401）；⛔另造一把判：须厚之判直取 分量闸.须厚（与推闸同尺）。
须厚起 = 401
# 〔1119 死规之审·gates6/prompts9/docs7〕作者唯一之底 2000（0722·圣经:106-107；0817·施工表:4684）：N≥473「厚」唯 <铁底 致命，带底／须厚只印 ⚠；N<473 照旧（坑㉚）
_死规审自 = 473
铁底 = 2000
# ★1113 X105（453:7「潮了一小块」：段案 451-460 头⛔「潮」字，五稿、行家、逻辑审俱未逮，记席方见）：
#   N≥455 起读本章所在段案之头（首「## NNN」之前）与本章一节之「⛔「X」字」之列，本章白文命中即致命红（合稿时即见）
禁字起 = 455
骨引起 = 465     # ★X113（465 封前）：骨记之引号逾所引章白文之末行即红（462 骨记「454:131」而 454 止於 117 行·记席手核方逮）
_禁字式 = re.compile(r'⛔「([^」]{1,4})」字')
# ★1120 禁字之免（设定/裁_1120_480段案之正.md ②·总编辑之裁：480 拍一温玉一处免「玉」，⛔删段之禁）：
#   段案本章一节书「禁字之免「X」N处」——X 须是本章所禁之字；本章白文（【本章亮点】以前）许命中 ≤N 行，逾限则其字白文诸行俱红；骨记照红。
#   ⛔读头（头之免即一段十章俱免）；其号「禁字之免」独有（「避免「X」字」之属⛔认）；⛔书作「⛔「X」字（…免）」（_禁字式 反读成禁）。
#   造式验（合稿之致命）、章料（执笔之料）、剧情全图（将到之撞）同用此一把（坑㊱）。
_免式 = re.compile(r'禁字之免「([^」]{1,4})」(\d+|[一二两三四五六七八九十])处')
_汉数 = {'一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}


def _段案之节(n, root=ROOT):
    """→ (头, 本章一节之文)；无本章之节 → None。"""
    for f in sorted(glob.glob(os.path.join(root, '设定', '段案', '[0-9]*-[0-9]*.md'))):
        t = open(f, encoding='utf-8').read()
        m = re.search(r'^## %d\s*$(.*?)(?=^## |\Z)' % n, t, re.M | re.S)
        if m:
            return re.split(r'^## \d+\s*$', t, maxsplit=1, flags=re.M)[0], m.group(1)
    return None


def 段案之禁字(n, root=ROOT):
    """→ [字]：本章所在段案之头与本章一节所列「⛔「X」字」（去重、依次）。★1120：有免之字照列（其免另取 段案之免）。"""
    s = _段案之节(n, root)
    return list(dict.fromkeys(_禁字式.findall(s[0] + '\n' + s[1]))) if s else []


def 免之析(节文, 禁=None):
    """纯判 → {字: 限}：一章之节所书「禁字之免「X」N处」；禁（其章所禁之字）给则只留所禁者。"""
    出 = {}
    for z, k in _免式.findall(节文 or ''):
        if 禁 is None or z in 禁:
            出[z] = int(k) if k.isdigit() else _汉数[k]
    return 出


def 段案之免(n, root=ROOT):
    """→ {字: 限}：本章一节（⛔头）之「禁字之免「X」N处」，只认本章所禁之字。"""
    s = _段案之节(n, root)
    return 免之析(s[1], _禁字式.findall(s[0] + '\n' + s[1])) if s else {}


# ★1117 X107（454:15「沟里有雪，没过脚面」：同线前三章白文「雪」字俱 0（只霜），一过杆子即没脚面之雪——五稿、行家、合稿俱未逮，唯逻辑审 soft-1 见）：
#   N≥457 起报之器「天候」：本章白文新出之天候字（雪、霜、雨、冰），同线前三章白文俱 0 者，其首见之段须带承接之相（早先、存着、化、冻）一处，否即报
天候起 = 457
首末起 = 473    # ★大审470 #23（473 封前）：章首、章末连章同式即红——469:5「…没有了。」470:5「…没有指头了。」；467、468、470 三回收在「睡着」，旧器只查一章之末、俱漏
_首族 = {'没有…了': r'没有[^，。！？]{0,6}了[。！]?$', '不见了': r'不见了[。！]?$', '还…着': r'还[^，。！？]{0,6}着[。！]?$',
        '空着': r'空着[。！]?$', '…了一下': r'了一[下声回遍]'}
_虚字 = set('了的那这一个两下上是而在把就也又还都得地么呢吗吧他她我你们不没')
_首末之频 = {}


def _首末段(n, root=ROOT):
    """(首段之首句, 末段)——白文之非空、非题之段。"""
    L = [l.strip() for l in (章白文(n, root) or '').split('\n') if l.strip()]
    L = [l for l in L if not l.startswith(('《', '＊', '*', '#')) and not re.match(r'^第\S+章', l)]
    if not L:
        return '', ''
    return re.split(r'(?<=[。！？])', L[0])[0], L[-1]


def _二字(s):
    s = re.sub(r'[^一-鿿]', '', s)
    return {s[i:i + 2] for i in range(len(s) - 1)} - {b for b in (s[i:i + 2] for i in range(len(s) - 1)) if set(b) & _虚字}


def _末之频(n, root=ROOT):
    """全书 1..n-1 章末段之二字文档频（缓存）——常见之词⛔算撞。"""
    if n not in _首末之频:
        import collections
        c, k = collections.Counter(), 0
        for m in range(1, n):
            末 = _首末段(m, root)[1]
            if 末:
                c.update(_二字(末)); k += 1
        _首末之频[n] = (c, k)
    return _首末之频[n]


def 首末之红(n, root=ROOT, 首=None, 末=None):
    """→ [要]：①首句与前一章首句同一句模（_首族）；②末段一实词二字串（全书章末频 ≤3%）在前三章之末段里 ≥2 回同见。"""
    中 = []
    a, z = _首末段(n, root)
    a, z = 首 if 首 is not None else a, 末 if 末 is not None else z
    pa = _首末段(n - 1, root)[0]
    for k, p in _首族.items():
        if a and pa and re.search(p, a) and re.search(p, pa):
            中.append('章首同式「%s」：本章「%s」｜%d「%s」——换一个起法' % (k, a, n - 1, pa))
    c, tot = _末之频(n, root)
    for b in sorted(_二字(z)):
        if tot and c[b] / tot > 0.03:
            continue
        见 = [m for m in (n - 1, n - 2, n - 3) if b in _二字(_首末段(m, root)[1])]
        if len(见) >= 2:
            中.append('章末同式「%s」：本章末段与 %s 之末段俱有——连章收在同一样上，换一个收法' % (b, '、'.join(map(str, 见))))
    return 中
天候字 = ['雪', '霜', '雨', '冰']
承相 = ['早先', '存着', '化', '冻']
_天候之伪 = ['冰凉', '冰冷', '冰窖']           # 言凉非言天，⛔算


def 章白文(n, root=ROOT):
    f = 正文档(n, root)
    if not f:
        return None
    t = open(f, encoding='utf-8').read()
    i = t.find('【本章亮点】')
    return t[:i] if i >= 0 else t


def _天候数(t, z):
    for w in _天候之伪:
        if z in w:
            t = t.replace(w, '')
    return t.count(z)


def 天候之红(白文, 前文表):
    """纯判：→ [(字, 行号, 段首)]：本章有、前文表（同线前三章之白文）俱 0、而首见之段无承接之相者。"""
    出 = []
    行 = 白文.split('\n')
    for z in 天候字:
        if not _天候数(白文, z) or any(_天候数(p or '', z) for p in 前文表):
            continue
        for i, ln in enumerate(行, 1):
            if _天候数(ln, z):
                if not any(c in ln for c in 承相):
                    出.append((z, i, ln[:24]))
                break
    return 出


def 同线前章(n, 几=3, root=ROOT):
    l, 出, k = 线(n, root), [], n - 1
    while l and k > 0 and len(出) < 几 and n - k <= 30:
        if 线(k, root) == l:
            出.append(k)
        k -= 1
    return 出


def 禁字之红(白文, 字表, 免=None):
    """纯判：→ [(字, 行号, 句)]，白文命中段案所禁之字者。
    ★1120 免（段案之免 → {字: 限}）：其字在白文（【本章亮点】以前）命中 ≤限 行者，此数行⛔入；逾限则其字白文诸行俱入（印全）；骨记照入。"""
    出 = []
    行们 = 白文.split('\n')
    for i, ln in enumerate(行们, 1):
        for z in 字表:
            if z in ln:
                k = ln.find(z)
                出.append((z, i, ln[max(0, k - 12):k + 12]))
    if 免:
        骨 = next((i for i, ln in enumerate(行们, 1) if '【本章亮点】' in ln), len(行们) + 1)
        for z, 限 in 免.items():
            白 = [x for x in 出 if x[0] == z and x[1] < 骨]
            if len(白) <= 限:
                出 = [x for x in 出 if x not in 白]
    return 出


def 须厚之料():
    """→ (净重, 线表)：自 分量闸 现取（与推闸同尺）。其「ℹ台账与正文不合」一行吞之（每跑必印·非本器之事），⛔行照印。"""
    import io, contextlib, 分量闸
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        w = 分量闸.诸章之净重()
    for l in buf.getvalue().split('\n'):
        if l.strip().startswith('⛔'):
            print(l)
    return w, 分量闸._线之表()


def 须厚之判(n, 净重=None, 线表=None):
    """→ (须, 语)：须 ∈ True／False／None。★None＝未可判：本章之前尚有暗线之章未写（窗未定·如段案一回立十章，
    401 未写而判 403）——⛔拿未写之章当薄章去判（那是一道假红）；待其前诸章写毕，--料 与 自走之派令於开派之时再判。
    ⛔N<须厚起 者不判（N≤400 之令与判⛔动）。"""
    import 分量闸
    if n < 须厚起:
        return False, '★第%d章 <%d，须厚之闸不及（N≤400 之令与判⛔动）' % (n, 须厚起)
    if 净重 is None or 线表 is None:
        _w, _L = 须厚之料()
        净重 = _w if 净重 is None else 净重
        线表 = _L if 线表 is None else 线表
    末写 = max(净重) if 净重 else 0
    未写 = sorted(x for x, l in 线表.items() if l == '暗' and 末写 < x < n)
    if 线表.get(n) == '暗' and 未写:
        return None, ('★第%d章之须厚未可判：其前暗线 %s 尚未写（窗未定）——待其前诸章写毕，'
                      'python3 工具/造式验.py %d --料 与 自走.py 之派令於开派之时再判'
                      % (n, '／'.join(str(x) for x in 未写), n))
    return 分量闸.须厚(n, 净重, 线表)


def 须厚之红(n, w, 须):
    """合稿之验：→ (红, 语)。须厚之章（n≥须厚起、须 is True）净重 <暗厚 即红；其语照 分量闸 之「治在事之择」。"""
    import 分量闸
    if n < 须厚起 or 须 is not True:
        return False, ''
    if n >= _死规审自:   # 〔1119 死规之审·gates6〕须厚之红改印注（⚠·⛔致命）：唯一硬线＝2000 铁底
        return False, ('须厚（只报）：%s净重 %d %s %d%s' % (('✓', w, '≥', 分量闸.暗厚, '') if w >= 分量闸.暗厚 else
                       ('⚠', w, '＜', 分量闸.暗厚, '——此窗暗线近五篇皆薄；其事若担得起更厚可厚，不为字数凑（1119 死规之审）')))
    if w >= 分量闸.暗厚:
        return False, '须厚（分量闸·须厚）：✓净重 %d ≥ %d' % (w, 分量闸.暗厚)
    return True, ('须厚（分量闸·须厚）：⛔净重 %d ＜ %d——本章係这一窗暗线最後一篇能交此账者；'
                  '⛔其治在事之择（换一件更大的事），不在字数（⛔添字、⛔撒感官以凑数）；合稿治不得即交总编辑（⛔认其量）'
                  % (w, 分量闸.暗厚))


def 骨引之红(骨, n, root=ROOT, 白们=None):
    """★X113：骨记（【本章亮点】起）诸引 → 行号逾所引章白文而无据者 [「章:行」…]。旧只於封版 --前 之机械之证印、⛔判红。
    逾白文而落於彼章骨记之行者（如 456「据450：145第一百八十三天」引 450 骨记之日账）：骨记引处之文与彼行·±1 有四字以上逐字之共串即认、否则红
    （462 v01「不紧，也不慢，回 454:131」——原句之回响落在 454 骨记、无四字之共·须红）；逾全档末行者恒红。"""
    import 封版, 章料
    出 = []
    for x, 类, 合, 注, L in 封版.骨引之核(骨, n, root, 白们):
        if 合 or not 注.startswith('行逾其白文'):
            continue
        f = 章料.章档(x['章'], root)
        全 = open(f, encoding='utf-8').read().split('\n') if f else []
        if x['起'] <= len(全) and 封版.共串(x['前文'] + '｜' + x['後文'], '\n'.join(全[max(1, x['起'] - 1) - 1:min(len(全), x['止'] + 1)])):
            continue
        出.append('%d:%d %s%s' % (x['章'], x['起'], 注, '·落其骨记而无四字之共' if x['起'] <= len(全) else '·逾全档'))
    return 出


def 正文档(n, root=ROOT):
    from 对账预筛 import 章号
    for f in glob.glob(os.path.join(root, '正文', '*.md')):
        if 章号(f) == n:
            return f
    return None


def 净重(路):
    """⛔另造一把尺（1013 实踩：自写之尺於 380 得 2581，仓之尺 2572）——直取 工具/净重对表.py 之 净重（与检察官同尺）。"""
    import 净重对表
    return 净重对表.净重(路)


def 线(n, root=ROOT):
    t = open(os.path.join(root, '设定', '02_余章之势_总纲.md'), encoding='utf-8').read()
    m = re.search(r'\|\s*%d\s*\|\s*(主|暗)·\d+(?:—\d+)?\s*\|' % n, t)      # ★总纲两栏排（左 381、右 404）——整行逐栏认（1013 实踩：只认左栏，右栏之章认不出）
    return m.group(1) if m else None


def 跑(器, 参, n):
    a = [sys.executable, os.path.join(ROOT, '工具', 器 + '.py')] + 参.format(N=n).split()
    t = time.time()
    try:
        r = subprocess.run(a, cwd=ROOT, capture_output=True, text=True, timeout=300)
        out, rc = (r.stdout + r.stderr), r.returncode
    except subprocess.TimeoutExpired:
        out, rc = '（逾 300 秒未毕）', 124
    末 = [l for l in out.split('\n') if l.strip()]
    return rc, out, (末[-1].strip() if 末 else ''), time.time() - t


def 硬之红(out):
    try:
        d = json.loads(out[out.index('{'):out.rindex('}') + 1])
        return {k: v for k, v in d.items() if isinstance(v, (int, float)) and v > 0}
    except Exception:
        return {'硬闸之印读不出': 1}


# ★1016·X02（393 合稿席为找红处多跑三回工具）：器红时总表只印其末行——起草闸印训语「③写完先跑本器甲层」、
#   硬闸只印计数、不印句，且「五逗句」扫全档连骨记，与「亮点段五逗」把同一句计两回（393 报 3＋3 实 3 句）。
#   今器红时於其行下另印「要」：起草闸甲层红之项、硬闸非零诸格之句（首二十字、至多五句）、余器之⛔行。
#   ⛔判红之准一格未动——以下只管「印什么」，红不红仍由 rc／硬之红 定。
def _句段(t):
    """t 之句（与 硬闸.硬项 同切：句末 。！？…）→ [(起, 止)]。"""
    段, s = [], 0
    for m in re.finditer(r'(?<=[。！？…])', t):
        if m.start() > s:
            段.append((s, m.start())); s = m.start()
    if s < len(t):
        段.append((s, len(t)))
    return 段


def _句之首(t, 起, 止, 锚=None):
    """句之首二十字。句起自锚（红处，缺则句中首个「，」）所在之行首、止於锚所在之行末——句切只认 。！？…，
    章题、「---」、【本章亮点】、上段末之 ” 会粘在句前，段末无句号者（章题、“走—”）又会把下一段粘在句後，⛔印作一句。
    ★W53·X20：旧式去尽空白（连换行）再取二十字，章题与下一行之正文粘作一串（「#第九百九十九章雪他走了。」）。"""
    if 锚 is None:
        锚 = t.find('，', 起, 止)
        锚 = 起 if 锚 < 0 else 锚
    起 = max(起, t.rfind('\n', 0, 锚) + 1)
    行末 = t.find('\n', 锚)
    止 = 止 if 行末 < 0 else min(止, 行末)
    return '%d行「%s」' % (t.count('\n', 0, 起) + 1, t[起:止].strip().lstrip('」”’』）)、，；：').lstrip()[:20])


# ★W53·X20：亮点段之格（只数骨记）→ 其所并入之全档之格（数全档，骨记在内）——同一句⛔印两回。
并入 = {'亮点段破折': ('破折',), '亮点段半角': ('半角逗', '半角引号')}


def 硬之要(txt, h=None, 至多=5):
    """txt：全档之文；h：硬闸诸格之数（缺则自算）。返 (末, 要)——末为一行之计，要为逐格之句。
    五逗句与亮点段五逗⛔重计：五逗句分白文／骨记二数，骨记之句即亮点段五逗，不另列。"""
    import 硬闸
    if h is None:
        h = {k: v for k, v in 硬闸.硬项(txt).items() if v}
    body, hl = 硬闸.拆(txt)
    prose = txt.split('【本章亮点】')[0]
    偏 = {'全': (txt, 0), '白': (body, len(prose) - len(body)),
          '亮': (hl, txt.find('【本章亮点】') if hl else len(txt))}
    禁 = '|'.join(re.escape(w) for w in sorted(硬闸.永禁词(), key=len, reverse=True)) or r'(?!)'
    定 = {'破折': ('全', '—'), '半角逗': ('全', ','), '半角冒': ('全', ':'), '半角引号': ('全', '"'),
         '半角问': ('全', r'\?'), '半角叹': ('全', '!'), '半角分': ('全', ';'), '半角撇': ('全', "'"),
         '英文': ('全', '[A-Za-z]'), '章号入正文': ('白', r'(?:[一二三四五六七八九十百零〇]+|\d+)章'),
         '禁抖': ('白', '[抖颤]'), '永禁词': ('白', 禁), '叠词粘连': ('白', 硬闸.叠词式.pattern),
         '段间空行病': ('白', r'[。！？”＊]\n(?!\n)[^\n]'),
         '亮点段破折': ('亮', '—'), '亮点段半角': ('亮', '[,"]'), '亮点段永禁': ('亮', 禁)}
    句 = _句段(txt)
    界 = txt.find('【本章亮点】') if hl else len(txt)

    def 所在(pos):
        for a, b in 句:
            if a <= pos < b:
                return (a, b)
        return (pos, pos + 20)

    def 列(spans):
        出, 见 = [], set()
        for sp in spans:
            if sp not in 见:
                见.add(sp); 出.append(sp)
        return 出

    末, 要 = [], []
    for k, v in h.items():
        if k == '亮点段五逗' and '五逗句' in h:
            continue                                   # 并入五逗句之骨记数，⛔重计
        if any(p in h for p in 并入.get(k, ())):
            continue                                   # ★W53·X20：亮点段破折／半角之句已在全档之格（骨记·），⛔重印
        if k == '五逗句' or k == '亮点段五逗':
            五 = [sp for sp in 句 if txt[sp[0]:sp[1]].count('，') >= 5]
            白 = [sp for sp in 五 if sp[1] <= 界]
            骨 = [sp for sp in 五 if sp[1] > 界]
            if k == '五逗句':
                注 = '五逗句 %d 句（白文 %d｜骨记 %d%s）' % (v, len(白), len(骨),
                       '；骨记之句即「亮点段五逗 %d」，同句不重计' % h['亮点段五逗'] if h.get('亮点段五逗') else '')
                spans = 白 + 骨
            else:
                注, spans = '亮点段五逗 %d 句' % v, 骨
            末.append(注)
            要.append('%s：%s' % (注.split('（')[0], '；'.join(('骨记·' if sp[1] > 界 else '') + _句之首(txt, *sp)
                                                         for sp in spans[:至多]) or '（句定不着，跑 硬闸.py N 自看）'))
            continue
        if k not in 定:
            末.append('%s %s' % (k, v))
            要.append('%s：（此格无句之定位，跑 硬闸.py N 自看）' % k); continue
        域, 式 = 定[k]
        t, o = 偏[域]
        锚, 骨数 = {}, 0
        for m in re.finditer(式, t):
            锚.setdefault(所在(o + m.start()), o + m.start())
            骨数 += (o + m.start()) >= 界
        亮 = [x for x, ps in 并入.items() if k in ps and h.get(x)]
        末.append('%s %s（白文 %d｜骨记 %d；骨记之数已在「%s %d」，同句不重计）' % (k, v, v - 骨数, 骨数, 亮[0], h[亮[0]])
                  if 亮 and 骨数 else '%s %s' % (k, v))
        spans = 列(锚)
        要.append('%s：%s' % (k, '；'.join(('骨记·' if 锚[sp] >= 界 else '') + _句之首(txt, sp[0], sp[1], 锚[sp])
                                           for sp in spans[:至多]) or '（句定不着）')
                  + ('（另 %d 句未列）' % (len(spans) - 至多) if len(spans) > 至多 else ''))
    return '、'.join(末), 要


def 红之要(器, out, 末):
    """器红时其行下另印之要（硬闸另由 硬之要 出）。起草闸：甲层⛔之项；余器：⛔行（去末行，至多三条）。"""
    行 = [l.strip() for l in out.split('\n') if l.strip()]
    if 器 == '起草闸':
        甲 = out.split('── 乙层')[0]
        红 = [l.strip() for l in 甲.split('\n') if l.strip().startswith('⛔')]
        if 红:
            return ['甲层红 %d 项：%s' % (len(红), '、'.join(l[1:].strip().split('：')[0] for l in 红))] + \
                   [l[:160] for l in 红]
        return ['甲层无⛔行而 rc≠0——其印之末三行：'] + [l[:160] for l in 行[-3:]]
    from 起草闸 import 红行                            # ★W53·X20：⛔行止於冒号者并其下要紧之句（与起草闸甲层同一法）
    红 = [l[:160] for l in 红行(out) if l != 末.strip()]
    return 红[:3]


def 察之判(out, n):
    """检察官之印 → (红, 末, 要)：封版门 ERROR>0 或读不出即红；要取本章 ✗ 之行（至多五）。"""
    m = re.search(r'封版门:ERROR=(\d+)', out)
    # ★1110 W109（430—439 每章合稿必撞之误拦）：「回执未交」「第十一轮未过」二项係封版席与封版 --後 之产出，
    #   合稿之时恒未有——只记「待封版」、⛔计致命；余之 ERROR 照红（封版门本身仍於 封版 --後 全计）
    待封 = len(re.findall(r'(?m)^\s+(?:回执未交|第十一轮未过):', out))
    红 = (m is None) or int(m.group(1)) - 待封 > 0
    末 = ('ERROR=%s' % m.group(1) + ('（其中待封版 %d）' % 待封 if 待封 else '')) if m else '封版门之印读不出'
    要 = [l.strip()[:160] for l in out.split('\n') if re.match(r'\s*✗第%d章 \[' % n, l)][:5] if 红 else []
    return 红, 末, 要


def 验(n, root=ROOT):
    出 = []
    for 器, 参, 判 in 致命:
        rc, out, 末, 秒 = 跑(器, 参, n)
        要 = []
        if 判 == '硬':
            h = 硬之红(out)
            红 = bool(h) or rc != 0
            末 = '、'.join('%s %s' % kv for kv in h.items()) if h else '诸格俱零'
            f = 正文档(n, root)
            if h and f and '硬闸之印读不出' not in h:
                try:
                    末, 要 = 硬之要(open(f, encoding='utf-8').read(), h)
                except Exception as e:                       # 只是印法，⛔因之改红绿
                    要 = ['（定句时出错：%s）' % e]
        else:
            红 = rc != 0
            if 红:
                要 = 红之要(器, out, 末)
        出.append(dict(器=器, 类='致命', 红=红, rc=rc, 秒=round(秒, 1), 末=末, 要=要))
    if n >= 察起:
        rc, out, 末, 秒 = 跑('小说检察官', '{N}', n)
        红, 末, 要 = 察之判(out, n)
        出.append(dict(器='检察官', 类='致命', 红=红, rc=rc, 秒=round(秒, 1), 末=末, 要=要))
    f = 正文档(n, root)
    if not f:
        出.append(dict(器='厚', 类='致命', 红=True, rc=1, 秒=0, 末='第%d章之正文不在 正文/' % n))
    else:
        w, l = 净重(f), 线(n, root)
        底 = 带底.get(l)
        须, 须语 = 须厚之判(n) if n >= 须厚起 else (False, '')     # ★1020 X40：N≤400 一字不判
        厚红, 厚语 = 须厚之红(n, w, 须)
        # 〔1119 死规之审·gates6〕N≥473：唯 <2000 铁底致命；带底只作信号（印 ⚠）；总纲无本章之行照红（非字数之额）
        _新 = n >= _死规审自
        出.append(dict(器='厚', 类='致命', 红=((底 is None or w < 铁底) if _新 else (底 is None or w < 底 or 厚红)), rc=0, 秒=0,
                      末='净重 %d｜%s线带底 %s' % (w, l or '?', 底 if 底 else '（总纲无本章之行）')
                      + ('｜⚠低於带底（只报）' if _新 and 底 and w < 底 else '') + ('｜⛔低於铁底 %d' % 铁底 if _新 and w < 铁底 else '')
                      + ('｜' + 厚语 if 厚语 else ''),
                      **({'要': [x.strip().replace('**', '') for x in 须语.split('\n') if x.strip()]} if 厚红 else {})))
        # ★1020 X40·驳席：「要」只於须厚之红时添——N≤400 之厚一行（含 --json）与改前逐字同
        if n >= 禁字起:
            字表 = 段案之禁字(n, root)
            免 = 段案之免(n, root)                     # ★1120 禁字之免：本章一节所许之处（只报其实，逾限即红）
            文 = open(f, encoding='utf-8').read()
            中 = 禁字之红(文, 字表, 免)
            免语 = ''.join('｜免「%s」≤%d 处（白文实 %s）' % (z, k, '、'.join(':%d' % x[1] for x in 禁字之红(文.split('【本章亮点】')[0], [z])) or '0')
                          for z, k in 免.items())
            出.append(dict(器='禁字', 类='致命', 红=bool(中), rc=0, 秒=0,
                          末=('段案所禁「%s」' % '、'.join(字表) if 字表 else '段案无「⛔「X」字」之列') + 免语 + ('｜命中 %d 处' % len(中) if 中 else '｜零命中'),
                          要=['「%s」 :%d  …%s…' % x for x in 中[:8]]))
        if n >= 骨引起:
            t = open(f, encoding='utf-8').read(); i = t.find('【本章亮点】')
            中 = 骨引之红(t[i:], n, root) if i >= 0 else []
            出.append(dict(器='骨引', 类='致命', 红=bool(中), rc=0, 秒=0,
                          末=('骨记之引号逾所引章白文 %d 处——合稿席当场改其号' % len(中)) if 中 else '骨记之引号俱在所引章白文之内',
                          要=中[:10]))
        if n >= 首末起:
            中 = 首末之红(n, root)
            出.append(dict(器='首末', 类='致命', 红=bool(中), rc=0, 秒=0,
                          末=('章首章末连章同式 %d 处——合稿席当场改其句' % len(中)) if 中 else '章首、章末与前章不同式', 要=中[:6]))
        if n >= 天候起:
            前 = 同线前章(n, root=root)
            中 = 天候之红(章白文(n, root) or '', [章白文(k, root) for k in 前])
            出.append(dict(器='天候', 类='报', 红=bool(中), rc=0, 秒=0,
                          末='同线前章 %s' % ('、'.join(map(str, 前)) or '无') + ('｜新出而无承接之相 %d 字' % len(中) if 中 else '｜续'),
                          要=['「%s」 :%d  %s…——前三章俱无，首见之段须带早先／存着／化／冻一处' % x for x in 中]))
    for 器, 参 in 报:
        rc, out, 末, 秒 = 跑(器, 参, n)
        出.append(dict(器=器, 类='报', 红=rc != 0, rc=rc, 秒=round(秒, 1), 末=末[:200],
                      要=红之要(器, out, 末) if rc != 0 else []))
    return 出


def 照整章(卡):
    """卡里「照 NNN」「NNN 之腔／原句」而全卡无「NNN:行」者 → [NNN]。"""
    提 = set(re.findall(r'照\s*(\d{3})(?![\d:：])(?!\s*卡)', 卡))   # ★444：「照 447 卡」係照某章之卡、非照其白文（未写之章无白文可点） | set(re.findall(r'(?<![\d:：])(\d{3})\s*(?:之腔|原句|的原句|的腔)', 卡))
    return sorted(x for x in 提 if not re.search(r'(?<!\d)%s\s*[:：]\s*\d' % x, 卡))


def 前文之缺(d, n):
    """★1027 X58：章料拆二档——_料.md 点明 _料_前文.md 者，彼档须在、⛔逾 120KB；旧之一档（未点明）照旧。→ [坏]"""
    p, 前 = os.path.join(d, '_料.md'), os.path.join(d, '_料_前文.md')
    if not os.path.exists(p) or '_料_前文.md' not in open(p, encoding='utf-8').read()[:1200]:
        return []
    if not os.path.exists(前):
        return ['章料之前文白文与账（_料_前文.md）不在（先跑 python3 工具/章料.py %d）' % n]
    if os.path.getsize(前) > 120 * 1024:
        return ['章料·前文 %d KB 逾 120KB（坑③）' % (os.path.getsize(前) // 1024)]
    return []


def 料律之缺(d, root=ROOT):
    """★1027 复核所逮（坑㊱·一义跨器而漏其消费者）：章料拆二档，而 `工具/席/造章.js` 之料律仍写「_料.md（…前两章白文全文…悬线、进化账）
    ——一次读毕；料外只许 grep 核一处」——席照令即⛔读 _料_前文.md（前两章白文、悬线）。料已拆（_料.md 点明彼档）而造章.js 未点名彼档 → [坏]。"""
    p = os.path.join(d, '_料.md')
    if not os.path.exists(p) or '_料_前文.md' not in open(p, encoding='utf-8').read()[:1200]:
        return []
    try:
        js = open(os.path.join(root, '工具', '席', '造章.js'), encoding='utf-8').read()
    except OSError:
        return []
    if '_料_前文.md' in js:
        return []
    return ['章料已拆二档而 工具/席/造章.js 之料律未点名 _料_前文.md（席照「只读 _料.md、料外只许 grep 核一处」即⛔读前两章白文与悬线）——於 N≥411 之料律点名彼档（坑㊱）']


def 料全(n, root=ROOT):
    坏 = []
    d = os.path.join(root, '版本', '第%d章' % n)
    if not os.path.exists(os.path.join(d, '_开镜卡.md')):
        坏.append('无开镜卡')
    p = os.path.join(d, '_料.md')
    if not os.path.exists(p):
        坏.append('无章料（先跑 python3 工具/章料.py %d）' % n)
    elif os.path.getsize(p) > 120 * 1024:
        坏.append('章料 %d KB 逾 120KB（坑③）' % (os.path.getsize(p) // 1024))
    坏 += 前文之缺(d, n) + 料律之缺(d, root)
    for k in (n - 1, n - 2):
        if not 正文档(k, root):
            坏.append('第%d章正文不在' % k)
    卡 = open(os.path.join(d, '_开镜卡.md'), encoding='utf-8').read() if os.path.exists(os.path.join(d, '_开镜卡.md')) else ''
    整章 = 照整章(卡)
    if 整章:                                  # ★1015（391 七席同报：卡令「照 268 原句」而无行号，七席各 awk 整章）
        坏.append('开镜卡令照 %s 之原句／之腔而未点其行——点作「%s:a—b」，章料即自展' % ('、'.join(整章), 整章[0]))
    try:                                      # ★1016 左移（396 封版逮：⑲ 只在封版时跑，卡定同向而章已写成）：动笔前即验本章之卡之向
        import 开轮六检 as _开
        for 名, ok, msg in _开.check19(n):
            if not ok:
                # 〔1119 死规之审·gates18·复核〕N≥473 ⑲ 只印 ⚠、⛔入坏：与 开轮六检._软报 同判（372 卡「⛔不许再往前，此向係被逼而择」、
                #   大审_至第377章:67 判 372／373 静场为最可能弃书处）——派令前硬拦即把开轮之软化吃掉；N<473 照旧（坑㉚）
                if n >= _死规审自:
                    print('  ⚠开轮⑲（只报·1119 死规之审）：%s' % msg[:120])
                else:
                    坏.append('开轮⑲：%s' % msg[:120])
    except Exception as e:
        坏.append('开轮⑲ 跑不起：%s' % e)
    import 剧情庭之关                          # ★1015 左移（W43 逮：391 写毕封版时方红）：动笔前，本段须已有剧情庭之势
    坏 += 剧情庭之关.查(root, 章=n)
    if n >= 须厚起:                            # ★1020 X40：须厚之章，段案「字数」之带不及暗厚即红（动笔前说话·⛔N≤400）
        import 章料
        坏 += 料之须厚(n, *须厚之判(n), 章料.段案行(n, root))
    if n >= 带一起:                            # ★1119 X119：本章之带唯段案为准——段案无带、卡之本章带与之不一即红
        import 章料
        坏 += 料之带(n, 章料.段案之带(n, root), 卡)
    if n >= 物缺起:                            # ★1126 X155（488：段案点「老头那盏灯」而物件.md 唯「### 灯」一字无今——料无其位，三稿令老头自出其灯）
        import 章料
        坏 += 料之物缺(章料.段案行(n, root), 卡, open(os.path.join(root, '设定', '全书记忆', '物件.md'), encoding='utf-8').read(), n)
    if n >= 钉起:                              # ★1126 X158／X159（489 悬线二笔、490 裁「像」钉於本章而卡零列——五六稿零兑）
        坏 += 料之钉(卡, 钉之条(n, root))
    return 坏


钉起 = 494


def 钉之条_纯(n, 悬文, 裁们):
    """★1126 X158／X159：纯判 → [(名, 源)]。①悬线档点到本章之行（他章已接写之记⛔收），以「｜〕；。」分段，段中本章号独立
    （⛔「N:行」之引）且带「→」或「再收」者，取「（→」前之名（2—14 字、⛔「N之…」）；②裁档（{档名: 文}）之行带「→N」或「钉於 N」者，其名＝「档名:行」。"""
    import re as _re
    import 章料
    号 = _re.compile(r'(?<![\d:：])%d(?![\d:])' % n)
    出, 见 = [], set()
    for i, l in enumerate(悬文.split('\n'), 1):
        if not 号.search(l) or 章料._他章已接(l, n):
            continue
        for 段 in _re.split(r'[｜〕；。]', l):
            if not 号.search(段) or ('→' not in 段 and '再收' not in 段):
                continue
            名 = _re.split(r'[（(→]', 段)[0].split('：')[-1].split('〔')[-1]
            名 = _re.sub(r'[*「」\s]', '', 名)
            if 2 <= len(名) <= 14 and len(_re.findall(r'[\u4e00-\u9fff]', 名)) >= 2 and not _re.match(r'\d+(之|再)', 名) and 名 not in 见:
                见.add(名); 出.append((名, '悬线:%d' % i))
    for 档, 文 in sorted(裁们.items()):
        for i, l in enumerate(文.split('\n'), 1):
            if _re.search(r'(?:→|钉於)\s*%d(?!\d)' % n, l):
                出.append(('%s:%d' % (档, i), '%s:%d' % (档, i)))
    return 出


def 钉之条(n, root=ROOT):
    悬 = os.path.join(root, '设定', '全书记忆', '悬线.md')
    裁们 = {os.path.basename(f)[:-3]: open(f, encoding='utf-8').read() for f in glob.glob(os.path.join(root, '设定', '裁_*.md'))}
    return 钉之条_纯(n, open(悬, encoding='utf-8').read() if os.path.exists(悬) else '', 裁们)


def 料之钉(卡, 条们):
    """★1126 X158／X159：纯判 → [坏]。钉本章之条（悬线、裁档）逐条须在开镜卡一行里点其名并落「治／改挂 NNN／销／弃」——缺即红
    （卡之「## 钉本章之账」一节；如「到期之账」之逐条）。"""
    import re as _re
    落 = _re.compile(r'治|改挂\s*\d{3}|销|弃')
    行们 = 卡.split('\n')
    缺 = [名 for 名, 源 in 条们 if not any(名 in 行 and 落.search(行) for 行 in 行们)]
    return ['钉本章之条开镜卡未逐条落「治／改挂 N／销」：%s——卡立「## 钉本章之账」逐条落（X158）' % '、'.join(缺)] if 缺 else []


物缺起 = 492


def 料之物缺(案, 卡, 物文, n):
    """★1126 X155：纯判 → [坏]。段案「物之迹／物之计」逐件（｜分、取首逗前之名）；其名为物件.md「### 」要物之名（或其一部）者，
    章料.物之末位（卡＋段案）所出须见其名——取不到即红（名一字、缺「- **今**：」行，或末章之块未列）。非要物（身体之部、未立题者）⛔判。"""
    import 章料
    import re as _re
    出 = '\n'.join(章料.物之末位(卡 + '\n' + 案, 物文, n))
    名们 = set()
    for m in _re.finditer(r'^### (.+?)$', 物文, _re.M):
        for x in _re.split(r'[＝、与]', m.group(1)):
            x = _re.sub(r'（[^）]*）', '', x).strip('「」 ')
            if x:
                名们.add(x.split('之')[-1])
    坏 = []
    for 段 in _re.findall(r'物之[迹计][：:](.*)', 案.replace('*', '')):
        for 件 in _re.split(r'[｜|]', 段):
            名 = _re.split(r'[，,（(：:→]', _re.sub(r'[*\s]', '', 件), maxsplit=1)[0]
            if not 名 or not any(名 == x or 名 in x or x in 名 for x in 名们 if x):
                continue
            if 名 not in 出:
                坏.append('段案物之迹点「%s」而章料物之末位取不到——物件.md 立其题（名 ≥2 字）并书「- **今**：」行（X155）' % 名)
    return 坏


带一起 = 471


def 料之带(n, 段带, 卡):
    """★1119 X119（469：卡「本章…照暗线常章带 2,300—3,100」、段案 2,900—3,300——五执笔照卡写、四稿俱 2,300 余）：纯判 → [坏]。
    段案本章无「字数：a—b」即红；卡中言「本章」之行所书之带（d,ddd—d,ddd）与段案之带不一即红（通则之行——无「本章」字者——⛔判）。"""
    if n < 带一起:
        return []
    if not 段带:
        return ['段案第%d章无「字数：a—b」——本章之带唯段案为准（X119），先补' % n]
    import 章料
    坏 = []
    for i, 行 in enumerate(卡.split('\n'), 1):
        if '本章' not in 行:
            continue
        for a, b in 章料.带式.findall(行):
            if '%s—%s' % (a, b) != 段带:
                坏.append('开镜卡:%d 本章之带 %s—%s 与段案 %s 不一——卡随段案改（X119）' % (i, a, b, 段带))
    return 坏


def 料之须厚(n, 须, 须语, 节文):
    """--料 之须厚一验（纯判·自测以字串跑）：→ [坏]。须厚之章，段案本章「字数」之带不及暗厚即红（其判 段案验.须厚之带红·同一把）；
    未可判者（其前暗线有未写之章）亦红——开派之时其前诸章当已写毕，仍未可判即料不全。⛔N<须厚起 者不判。"""
    if n < 须厚起:
        return []
    if n >= _死规审自:   # 〔1119 死规之审·gates6/docs7〕--料 之须厚只印 ⚠、⛔入坏（唯一硬线＝2000 铁底）
        if 须 is True:
            import 段案验
            红 = 段案验.须厚之带红(n, 节文)
            if 红:
                print('  ⚠%s（只报·1119 死规之审）' % 红.lstrip('⛔'))
        elif 须 is None:
            print('  ⚠%s（只报·1119 死规之审）' % 须语.lstrip('★'))
        return []
    if 须 is True:
        import 段案验
        红 = 段案验.须厚之带红(n, 节文)
        return [红] if 红 else []
    if 须 is None:
        return [须语.lstrip('★')]
    return []


def 自测():
    ok = 共 = 0
    f = 正文档(380)
    import 净重对表
    共 += 1; ok += (f is not None and 净重(f) == 净重对表.净重(f))                 # 一把尺
    共 += 1; ok += (硬之红('{\n "破折": 0,\n "英文": 2\n}') == {'英文': 2} and 硬之红('乱') == {'硬闸之印读不出': 1})
    # X80（1104）：检察官封版门 ERROR>0 即红（418:57 F007 之回灌）、=0 绿、读不出红
    _察 = '  ✗第418章 [F007_打介词]行57: …我打那三处过。…\n  封版门:ERROR=1(须0) REVIEW=6(人工裁定)'
    共 += 1; ok += (察之判(_察, 418)[0] and len(察之判(_察, 418)[2]) == 1 and 察之判('  封版门:ERROR=0(须0)', 420) == (False, 'ERROR=0', [])
                  and 察之判('乱', 420)[0] and 察起 == 420)
    _待 = '  ✗第439章《一格》:\n      第十一轮未过:未见 …\n      回执未交:当章…\n  封版门:ERROR=2(须0) REVIEW=7(人工裁定)'
    共 += 1; ok += (not 察之判(_待, 439)[0] and 察之判(_待.replace('ERROR=2', 'ERROR=3'), 439)[0])   # ★1110 W109：待封版二项⛔计致命、余者照红
    共 += 1; ok += all(os.path.exists(os.path.join(ROOT, '工具', x[0] + '.py')) for x in 致命 + 报)
    共 += 1; ok += (线(381) == '暗' and 线(380) == '主' and 线(404) == '主' and 线(405) == '暗' and 线(999) is None)   # 右栏之章亦认
    共 += 1; ok += (照整章('点户照 268 原句，腔照 211') == ['211', '268'] and 照整章('照 268 原句（268:61—77）') == [] and 照整章('照 447 卡，卡未定取挪晚') == [])
    import tempfile as _tf9                   # ★1027 X58：二档之料——点明彼档而彼档缺即红；彼档在、旧之一档 → 不红
    with _tf9.TemporaryDirectory() as _d9:
        open(os.path.join(_d9, '_料.md'), 'w', encoding='utf-8').write('# 料\n## 〔本料二档〕\n前文在 `版本/第9章/_料_前文.md`\n')
        _缺9 = 前文之缺(_d9, 9)
        open(os.path.join(_d9, '_料_前文.md'), 'w', encoding='utf-8').write('# 前文\n')
        _在9 = 前文之缺(_d9, 9)
        open(os.path.join(_d9, '_料.md'), 'w', encoding='utf-8').write('# 料（旧之一档）\n')
        os.remove(os.path.join(_d9, '_料_前文.md'))
        _旧9 = 前文之缺(_d9, 9)
    共 += 1; ok += (len(_缺9) == 1 and '_料_前文.md' in _缺9[0] and _在9 == [] and _旧9 == [])
    # ★1027 复核补（坑㊱）：料已拆而造章.js 之料律未点名 _料_前文.md → 红；点名 → 过；旧之一档 → ⛔验（放行之反例）
    with _tf9.TemporaryDirectory() as _r9:
        _章9 = os.path.join(_r9, '版本', '第9章'); os.makedirs(_章9); os.makedirs(os.path.join(_r9, '工具', '席'))
        open(os.path.join(_章9, '_料.md'), 'w', encoding='utf-8').write('# 料\n## 〔本料二档〕\n前文在 `版本/第9章/_料_前文.md`\n')
        _js = os.path.join(_r9, '工具', '席', '造章.js')
        open(_js, 'w', encoding='utf-8').write('const 料律 = `${章目}/_料.md（前两章白文全文）——一次读毕；料外只许 grep 核一处`')
        _律缺 = 料律之缺(_章9, _r9)
        open(_js, 'a', encoding='utf-8').write('\nconst 前料 = `${章目}/_料_前文.md`')
        _律在 = 料律之缺(_章9, _r9)
        open(os.path.join(_章9, '_料.md'), 'w', encoding='utf-8').write('# 料（旧之一档）\n')
        open(_js, 'w', encoding='utf-8').write('x')
        _律旧 = 料律之缺(_章9, _r9)
    共 += 1; ok += (len(_律缺) == 1 and '造章.js' in _律缺[0] and _律在 == [] and _律旧 == [])
    # ★X02：红处之要——五逗不重计、硬闸印句、起草闸印甲层红项（造局以字串，⛔钉盘上之数）
    文 = ('# 第九百九十九章 试\n\n甲，乙，丙，丁，戊，己。他说——好。\n平常一句。\n\n---\n\n'
          '【本章亮点】\n\n①子，丑，寅，卯，辰，巳。②平。')
    import 硬闸
    h = {k: v for k, v in 硬闸.硬项(文).items() if v}
    末, 要 = 硬之要(文, h)
    共 += 1; ok += (h.get('五逗句') == 2 and h.get('亮点段五逗') == 1          # 硬闸自身仍计两回（判准未动）
                   and '白文 1｜骨记 1' in 末 and '亮点段五逗 1」，同句不重计' in 末
                   and not any(y.startswith('亮点段五逗') for y in 要)
                   and any(y.startswith('五逗句') and '3行「甲，乙，丙' in y and '骨记·' in y and '骨记·10行「①子，丑，寅' in y for y in 要)
                   and any(y.startswith('破折') and '「他说——好。」' in y for y in 要)
                   and any(y.startswith('段间空行病') for y in 要))
    共 += 1; ok += (硬之要('# 第九百九十九章 试\n\n他说：「走。」——好。\n')[1] == ['破折：3行「——好。」'])   # 句首之」⛔印
    多 = '# 第九百九十九章 试\n\n' + ''.join('句%d——。' % i for i in range(7))
    _, 要7 = 硬之要(多)
    共 += 1; ok += (len(要7) == 1 and 要7[0].count('「') == 5 and '另 2 句未列' in 要7[0])   # 至多五句
    起 = ('── 甲层·机器判得死的（红即拦）──\n  ✓ 亮点对表：✓ 零\n  ⛔ 含拍：⛔ 并段旧拍未删\n'
          '  ⛔ 硬闸·本章：{\'破折\': 1}\n\n── 乙层\n  ⛔ 乙层之⛔不算\n    ③写完先跑本器甲层，再交别人看')
    r = 红之要('起草闸', 起, '③写完先跑本器甲层，再交别人看')
    共 += 1; ok += (r[0] == '甲层红 2 项：含拍、硬闸·本章' and len(r) == 3 and not any('乙层' in y for y in r))
    # ★W53·X20 三病（造局以字串）：①亮点段破折／半角之句⛔与全档之格重印；②余器⛔行止於冒号者并其下要紧之句；
    #   ③章题与下一行、段末无句号之段与下一段⛔粘作一句。
    末20, 要20 = 硬之要('# 第九百九十九章 试\n\n甲乙。\n\n---\n\n【本章亮点】\n\n①子——丑,寅"卯。②平。')
    共 += 1; ok += (not any(y.startswith('亮点段') for y in 要20) and not any(x.startswith('亮点段') for x in 末20.split('、'))
                   and '破折：骨记·9行「①子——丑' in 要20[0] and '破折 2（白文 0｜骨记 2；骨记之数已在「亮点段破折 2」' in 末20)
    共 += 1; ok += (红之要('数闸', '  ⛔ 不符 2 处：\n     甲.md 行3 标5 实4 ｜某某\n末行', '末行')
                   == ['⛔ 不符 2 处：甲.md 行3 标5 实4 ｜某某'])
    共 += 1; ok += (_句之首('# 第九百九十九章 雪\n他走了。', 0, 17) == '1行「# 第九百九十九章 雪」'
                   and 硬之要('# 第九百九十九章 雪\n\n“走—”\n他说着就去了。')[1][0] == '破折：3行「“走—”」')
    # ★1020 X40：须厚入闸（造局以字串与假表，⛔钉盘上之数；⛔N≤400 一格不判）
    import 分量闸
    L = {393: '暗', 395: '暗', 397: '暗', 399: '暗', 400: '主', 401: '暗', 402: '主', 403: '暗'}
    薄 = {393: 2492, 395: 2408, 397: 2440, 399: 2580}
    共 += 1; ok += (须厚之判(401, 薄, L)[0] is True                                   # 前四篇暗线皆薄→非厚不可
                   and 须厚之判(403, 薄, L)[0] is None                                  # 401 未写·窗未定→未可判（⛔假红）
                   and 须厚之判(402, 薄, L)[0] is False                                 # 主线不受
                   and 须厚之判(401, {**薄, 399: 2900}, L)[0] is False            # 一篇已厚→不须
                   and 须厚之判(399, {391: 2580, 393: 2492, 395: 2408, 397: 2440}, L)[0] is False   # ⛔N≤400 不判
                   and 分量闸.须厚(399, {391: 2580, 393: 2492, 395: 2408, 397: 2440}, {**L, 391: '暗'})[0] is True)  # ★回灌：399 本须厚，旧无一闸
    共 += 1; ok += (须厚之红(401, 2899, True)[0] and '治在事之择' in 须厚之红(401, 2899, True)[1]
                   and 须厚之红(401, 2900, True)[0] is False and '✓' in 须厚之红(401, 2900, True)[1]
                   and 须厚之红(400, 2000, True) == (False, '')                        # ⛔N≤400
                   and 须厚之红(401, 2000, False) == (False, '') and 须厚之红(401, 2000, None) == (False, '')
                   and 须厚之红(401, 2580, True)[0])                                    # ★回灌：399 之末稿 2580 在 401 须红
    _带 = lambda x: '（设定/段案/401-410.md）\n- 重：中\n- 守：⛔凑字；字数：%s。' % x
    # ★1119 X119：卡之本章带与段案不一即红（回灌 469 之卡句）；同即绿；通则之行（无「本章」）⛔判；段案无带红；N≤470 ⛔判
    _卡469 = '- 常章 2,500—3,500｜暗线常章带 ＝ 2,300 — 3,100\n- 465 已 ≥2,900，本章不是那一篇，照暗线常章带 2,300—3,100，⛔凑。'
    共 += 1; ok += (len(料之带(471, '2,900—3,300', _卡469)) == 1 and 料之带(471, '2,300—3,100', _卡469) == []
                    and len(料之带(471, '', '')) == 1 and 料之带(470, '2,900—3,300', _卡469) == [] and 料之带(470, '', '') == [])
    _物 = '### 灯\n- **老头之铜皮马灯**：2\n### 那盏灯（後段）\n- **今**：锹柄上\n'                  # ★X155 回灌 488：「### 灯」一字无今即红
    共 += 1; ok += (len(料之物缺('- 物之动：**物之计**：灯→随匣进坑｜左掌，座上', '', _物.split('### 那盏灯')[0], 488)) == 1
                   and 料之物缺('- 物之动：**物之计**：那盏灯→锹柄上｜左掌，座上', '', _物, 492) == []
                   and 料之物缺('- 物之动：无', '', _物, 492) == [])
    共 += 1; ok += (len(料之须厚(401, True, '', _带('暗线常章 2,300—2,900'))) == 1                 # ★回灌：399 段案之带
                   and len(料之须厚(401, True, '', _带('2,300—2,800'))) == 1                          # 带之顶 <2,900
                   and 料之须厚(401, True, '', _带('暗线须厚 2,900—3,100')) == []
                   and 料之须厚(400, True, '', _带('2,300—2,900')) == []                              # ⛔N≤400
                   and 料之须厚(401, False, '', _带('2,300—2,900')) == []
                   and 料之须厚(401, None, '★未可判', '') == ['未可判']
                   and len(料之须厚(401, True, '', '')) == 1)                                        # 段案无本章之节
    # ★1020 X40·驳席补：上三格只验纯判——删 验() 之「or 厚红」或 料全() 之须厚一段，三格照绿（假绿）；
    #   此格桩其重器（⛔真跑诸闸、⛔钉盘上之数），验其接口：401 合稿之厚一行红、--料 红；400 两路一字不及
    g = globals()
    _原 = {k: g[k] for k in ('跑', '正文档', '净重', '线', '须厚之判')}
    import 章料 as _章料, 剧情庭之关 as _剧, 开轮六检 as _开
    _旧 = (_章料.段案行, _剧.查, _开.check19)
    try:
        g['跑'] = lambda 器, 参, n: (0, '{}', '诸格俱零', 0)
        g['正文档'] = lambda n, root=ROOT: '/桩'
        g['净重'] = lambda 路: 2601
        g['线'] = lambda n, root=ROOT: '暗'
        g['须厚之判'] = lambda n, *a: (True, '⛔**第%d章非厚不可**：桩' % n)
        _章料.段案行 = lambda n, root=ROOT: '（设定/段案/401-410.md）\n- 守：字数：暗线常章 2,300—2,900。'
        _剧.查 = lambda root=ROOT, 章=None: []
        _开.check19 = lambda cur: []
        a401, a400 = [[x for x in 验(k) if x['器'] == '厚'][0] for k in (401, 400)]
        b401, b400 = [[x for x in 料全(k) if '须厚' in x] for k in (401, 400)]
    finally:
        g.update(_原)
        _章料.段案行, _剧.查, _开.check19 = _旧
    共 += 1; ok += (a401['红'] and '治在事之择' in a401['末'] and a401.get('要') == ['⛔第401章非厚不可：桩']
                   and not a400['红'] and '须厚' not in a400['末'] and '要' not in a400
                   and len(b401) == 1 and '之底 ＜2900' in b401[0] and b400 == [])
    # 〔1119 死规之审·gates6〕N≥473：须厚之红→注；料之须厚只印 ⚠；N<473 照旧（原验「红」者今验「⚠ 而不红」，并验守牙仍红）
    #   〔1119 退回·更胜从前之筛〕gates7（段案无带即红）无硬证其更胜→退回原样：480 照旧红（下格验之；自走.py 之拦派同退·两器同判）
    #   〔1119 死规之审·gates18·复核〕⑲ 骨之方向：有 E1（版本/第372章/_开镜卡.md:30 被逼择向、大审_至第377章:67）→ 与 开轮六检._软报 同判：
    #     N≥473 只印 ⚠、⛔入坏；N<473 照旧红（下格验之）
    import io as _io19, contextlib as _cl19
    _印19 = _io19.StringIO()
    with _cl19.redirect_stdout(_印19):
        _须473 = 料之须厚(480, True, '', _带('2,300—2,800'))
        _未473 = 料之须厚(480, None, '★未可判', '')
    共 += 1; ok += (须厚之红(480, 2899, True)[0] is False and '⚠' in 须厚之红(480, 2899, True)[1]
                   and '✓' in 须厚之红(480, 2900, True)[1] and 须厚之红(472, 2899, True)[0] is True        # N<473 照旧红
                   and _须473 == [] and _未473 == [] and '⚠第480章须厚' in _印19.getvalue() and '⚠未可判' in _印19.getvalue()
                   and len(料之须厚(472, True, '', _带('2,300—2,800'))) == 1)                              # N<473 照旧红
    _原19 = {k: g[k] for k in ('跑', '正文档', '净重', '线', '须厚之判', '禁字起', '骨引起', '天候起', '首末起')}
    _旧19 = (_章料.段案行, _章料.段案之带, _剧.查, _开.check19)
    _印19b = _io19.StringIO()
    try:
        g['跑'] = lambda 器, 参, n: (0, '{}', '诸格俱零', 0)
        g['正文档'] = lambda n, root=ROOT: '/桩'
        g['线'] = lambda n, root=ROOT: '暗'
        g['须厚之判'] = lambda n, *a: (True, '⚠第%d章：桩' % n)
        g['禁字起'] = g['骨引起'] = g['天候起'] = g['首末起'] = 10 ** 9    # 桩其重器（⛔读盘上之白文）；★W908 环1：首末起（473 立）漏桩，480 读 '/桩' 而崩
        _章料.段案行 = lambda n, root=ROOT: '（设定/段案/471-480.md）\n- 守：字数：2,300—2,800。'
        _章料.段案之带 = lambda n, root=ROOT: ''
        _剧.查 = lambda root=ROOT, 章=None: []
        _开.check19 = lambda cur: [('⑲·骨之方向', False, '近三章皆朝往内（桩）')]
        g['净重'] = lambda 路: 2601
        a480 = [x for x in 验(480) if x['器'] == '厚'][0]
        a472 = [x for x in 验(472) if x['器'] == '厚'][0]
        g['净重'] = lambda 路: 2200
        a480薄 = [x for x in 验(480) if x['器'] == '厚'][0]
        a472薄 = [x for x in 验(472) if x['器'] == '厚'][0]
        g['净重'] = lambda 路: 1999
        a480铁 = [x for x in 验(480) if x['器'] == '厚'][0]
        with _cl19.redirect_stdout(_印19b):
            b480 = 料全(480)
        b472 = 料全(472)
    finally:
        g.update(_原19)
        _章料.段案行, _章料.段案之带, _剧.查, _开.check19 = _旧19
    共 += 1; ok += (not a480['红'] and '⚠低於带底' not in a480['末'] and '须厚（只报）：⚠净重 2601' in a480['末']   # 2601 ≥ 暗带底 2300：只注须厚
                   and a472['红']                                                                                # N<473 照旧：须厚之红仍致命
                   and not a480薄['红'] and '⚠低於带底（只报）' in a480薄['末'] and a472薄['红']               # 2200 <暗带底 2300：473 起只 ⚠，472 照旧红
                   and a480铁['红'] and '⛔低於铁底 2000' in a480铁['末'] and '⚠低於带底' in a480铁['末']         # 守牙：<2000 致命
                   and not any('须厚' in x for x in b480)                                                        # 须厚只 ⚠（gates6）
                   and any('字数：a—b' in x for x in b480)                                                      # 〔1119 退回〕段案无带 480 照旧红
                   and not any('开轮⑲' in x for x in b480) and '⚠开轮⑲（只报' in _印19b.getvalue()             # 〔1119·gates18·复核〕⑲ 473 起只 ⚠
                   and any('开轮⑲' in x for x in b472) and any('字数：a—b' in x for x in b472))                 # N<473 ⑲ 照旧红
    # X105（1113）：段案头之禁字——453 v01「潮了一小块」回灌须红、改「湿」须绿；451-460 之列读得出「潮」
    共 += 1; ok += (禁字之红('鞋帮潮了一小块。\n她没动。', ['潮']) == [('潮', 1, '鞋帮潮了一小块。')]
                   and 禁字之红('鞋帮湿了一小块。', ['潮']) == [] and 禁字之红('潮', []) == []
                   and '潮' in 段案之禁字(455) and 段案之禁字(9999) == [])
    # ★1120 禁字之免（设定/裁_1120_480段案之正.md ②·总编辑之裁）：段案本章一节书「禁字之免「X」N处」——其字白文许命中 ≤N 行，
    #   逾限则其字白文诸行俱红（印全）；骨记照红；免只读本章一节（头之免⛔及他章）、只免所禁之字；「避免「X」字」之属⛔认；他字之禁不变；
    #   ⛔删段之禁：段案之禁字 照旧含其字（章料印其免、执笔见之）
    def _崩之(f):
        try:
            return f()
        except Exception as e:
            print('  ✗禁字之免之钉崩：%s %s' % (type(e).__name__, e))
            return None
    import tempfile as _tf20
    with _tf20.TemporaryDirectory() as _r20:
        os.makedirs(os.path.join(_r20, '设定', '段案'))
        open(os.path.join(_r20, '设定', '段案', '901-910.md'), 'w', encoding='utf-8').write(
            '# 段案·901—910\n\n> **本段之禁字**：⛔「玉」字、⛔「潮」字。禁字之免「潮」一处（头之免⛔及他章）\n\n'
            '## 909\n- 守：⛔「霍钧」字。避免「潮」字一处。\n\n'
            '## 910\n- 物之动：拍一温玉。\n- 守：禁字之免「玉」一处（拍一）；禁字之免「秦」一处（未禁之字⛔免）；⛔与两半、合同句。\n')
        _免20 = _崩之(lambda: (段案之免(910, _r20), 段案之免(909, _r20), 段案之禁字(910, _r20), 段案之禁字(909, _r20)))
    共 += 1; ok += (_免20 == ({'玉': 1}, {}, ['玉', '潮'], ['玉', '潮', '霍钧']))
    _白一 = '右手伸进领口，攥着玉。\n天亮了。\n\n---\n\n【本章亮点】\n①拍一。'
    共 += 1; ok += bool(_崩之(lambda: 禁字之红(_白一, ['玉', '潮'], {'玉': 1}) == []                                  # 白文一行：免
                              and [x[1] for x in 禁字之红('攥着玉。\n玉还温着。\n', ['玉'], {'玉': 1})] == [1, 2]         # 逾限：其字白文诸行俱红
                              and [x[1] for x in 禁字之红('攥着玉。\n\n【本章亮点】\n①拍一温玉。', ['玉'], {'玉': 1})] == [4]   # 骨记照红
                              and [x[0] for x in 禁字之红('攥着玉。\n鞋帮潮了。', ['玉', '潮'], {'玉': 1})] == ['潮']     # 他字之禁不变
                              and len(禁字之红(_白一, ['玉'])) == 1 and len(禁字之红(_白一, ['玉'], {})) == 1))          # 无免照旧红
    # 真段案：480 拍一免「玉」一处；471—479 无免；禁表照旧含「玉」（⛔删段之禁）
    共 += 1; ok += bool(_崩之(lambda: 段案之免(480) == {'玉': 1} and all(段案之免(k) == {} for k in range(471, 480))
                              and all('玉' in 段案之禁字(k) for k in range(471, 481)) and 段案之免(9999) == {}))
    # 接口：验() 之禁字一格以 段案之免 计（桩其重器·⛔真跑诸闸；白文以临时档）——480 白文一处玉绿、两处红；479 一处红
    with _tf20.TemporaryDirectory() as _d20:
        _一, _二 = os.path.join(_d20, '一.md'), os.path.join(_d20, '二.md')
        open(_一, 'w', encoding='utf-8').write('# 第四百八十章 试\n\n右手伸进领口，攥着玉。\n天亮了。\n')
        open(_二, 'w', encoding='utf-8').write('# 第四百八十章 试\n\n攥着玉。\n玉还温着。\n')
        _原20 = {k: g[k] for k in ('跑', '正文档', '净重', '线', '须厚之判', '骨引起', '天候起', '首末起')}
        _当20 = {}
        try:
            g['跑'] = lambda 器, 参, n: (0, '{}', '诸格俱零', 0)
            g['正文档'] = lambda n, root=ROOT: _当20['f']
            g['净重'] = lambda 路: 2601
            g['线'] = lambda n, root=ROOT: '主'
            g['须厚之判'] = lambda n, *a: (False, '')
            g['骨引起'] = g['天候起'] = g['首末起'] = 10 ** 9

            def _禁格(k, f):
                _当20['f'] = f
                return [x for x in 验(k) if x['器'] == '禁字'][0]
            _格20 = _崩之(lambda: (_禁格(480, _一), _禁格(480, _二), _禁格(479, _一)))
        finally:
            g.update(_原20)
    共 += 1; ok += bool(_格20 and not _格20[0]['红'] and '免「玉」' in _格20[0]['末'] and _格20[1]['红']
                        and len(_格20[1]['要']) == 2 and _格20[2]['红'])
    # X107（1117）：天候之续——454 v01「沟里有雪，没过脚面」须红、v02「存着早先落的雪…冻了一层壳」须绿（同线前三章 452、450、448 白文无雪）
    def _段白(p):
        t = open(os.path.join(ROOT, '版本', '第454章', p), encoding='utf-8').read()
        i = t.find('【本章亮点】')
        return t[:i] if i >= 0 else t
    前454 = [章白文(k) for k in 同线前章(454)]
    r1, r2 = 天候之红(_段白('v01.md'), 前454), 天候之红(_段白('v02.md'), 前454)
    共 += 1; ok += (len(同线前章(454)) == 3 and [x[0] for x in r1] == ['雪'] and r2 == []
                   and 天候之红('手冰凉。', ['']) == [] and 天候之红('下雨了。', ['雨']) == [])
    # X113（465）：骨记引号逾白文——462 v01「454:131」回灌须红（454 白文 117 行）、v02 改「454:111」须绿
    def _骨(p):
        t = open(os.path.join(ROOT, '版本', '第462章', p), encoding='utf-8').read()
        return t[t.find('【本章亮点】'):]
    共 += 1; ok += (骨引之红(_骨('v01.md'), 462) == ['454:131 行逾其白文（117 行）·落其骨记而无四字之共'] and 骨引之红(_骨('v02.md'), 462) == []
                   and 骨引之红(open(正文档(456), encoding='utf-8').read().split('【本章亮点】', 1)[1], 456) == []   # 456 引 450 骨记之日账·认
                   and 骨引之红('【本章亮点】据450：999云云。', 456) == ['450:999 行逾其白文（143 行）·逾全档'] and 骨引起 == 465)
    # ★大审470 #23：章首同式（470 之首 vs 469 之首）、章末同式（睡着连三回）
    共 += 1; ok += (any('没有…了' in x for x in 首末之红(470)) and not any('章首' in x for x in 首末之红(472)))
    _旧 = _首末段.__globals__['_首末段']; _假 = {467: ('', '他睡着了，攥本子那只手松了半边。'), 468: ('', '我睡着以前，她的指头还搁在那一行上。')}
    globals()['_首末段'] = lambda m, root=ROOT: _假.get(m) or _旧(m, root)    # 回灌 468:113 改前之末
    try:
        共 += 1; ok += any('睡着' in x for x in 首末之红(470, 末='後半夜，我坐着睡着了。', 首=''))
    finally:
        globals()['_首末段'] = _旧
    共 += 1; ok += (_二字('了那一') == set() and 首末起 == 473)
    # ★X158／X159 回灌 489：悬线钉本章之二笔、裁「→490」而卡零列即红；卡逐条落「治／改挂」即绿；「N:行」之引⛔作钉
    _悬 = '- **E8·483 所结所开**〔仍挂〕475 板子上那只拇指之主（→485·485 零兑，改钉 489）｜那张纸（→507）｜旧引（489:12→後章）'
    _条 = 钉之条_纯(489, _悬, {'裁_甲': '一行\n「像」→490\n'})
    共 += 1; ok += ([x[0] for x in _条] == ['475板子上那只拇指之主'] and 钉之条_纯(490, _悬, {'裁_甲': '一行\n「像」→490\n'})[-1][0] == '裁_甲:2'
                   and len(料之钉('## 问八\n- 无', _条)) == 1 and 料之钉('## 钉本章之账\n- 475板子上那只拇指之主｜改挂 499', _条) == []
                   and len(料之钉('- 475板子上那只拇指之主（只提名不落）', _条)) == 1 and 钉起 == 494)
    print('造式验·自测 %d/%d' % (ok, 共))
    return ok == 共


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--自测']:
        sys.exit(0 if 自测() else 1)
    if not a or not a[0].isdigit():
        print(__doc__); sys.exit(2)
    n = int(a[0])
    if '--料' in a:
        坏 = 料全(n)
        print('✓ 第%d章之料全' % n if not 坏 else '⛔ 第%d章之料不全：%s' % (n, '；'.join(坏)))
        sys.exit(0 if not 坏 else 1)
    r = 验(n)
    for x in r:
        print('  %s %-6s %-5s %5.1fs  %s' % ('⛔' if x['红'] else '✓', x['器'], '（致命）' if x['类'] == '致命' else '', x['秒'], x['末']))
        for y in x.get('要') or []:
            print('        ↳ %s' % y)
    红致 = [x['器'] for x in r if x['红'] and x['类'] == '致命']
    红报 = [x['器'] for x in r if x['红'] and x['类'] == '报']
    print('造式验·第%d章：致命之器%s｜报之器%s' % (n, '俱绿' if not 红致 else '有红（%s）——⛔交' % '、'.join(红致),
                                         '俱绿' if not 红报 else '有红（%s）——治或写明其由' % '、'.join(红报)))
    if '--json' in a:
        print(json.dumps(r, ensure_ascii=False))
    sys.exit(1 if 红致 else 0)
