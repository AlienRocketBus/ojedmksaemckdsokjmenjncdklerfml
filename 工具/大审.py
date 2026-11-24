# -*- coding: utf-8 -*-
"""大审闸（2026-09-02·作者令所立）

★**作者令（逐字）**：「**这个小说应该平均10章就应该从头到尾我们来进行一个剧情和质量
  等等各个方面严格把控，看看有没有达到一个最高等级**……**站在普通读者的视角，站在一个
  最顶尖小说家的视角，站在一个评委的视角，站在一个编辑的视角，站在一个普通小说爱好者
  的这么一个视角**……**不要说只有一个小说家，你可以用好几个小说家。**」

★★**而立此闸之前，先把「为什么现有的看官五席不够」写死在这里**（2026-09-02 九席审读之实）：
  ①**五席之输入是同一样东西**——`白文(n)` 的字符流加一张手写动词表加对它的计数；
    ★**四席吃同一份输入，於是四席是同一次测量的四个样本，不是四只眼**；
    ★★**唯一产出过真发现的是连读客（289/291开篇重出），而它正是唯一输入不同的那一席（多章）**。
  ②**必响之器不携带信息**：小说家（`if len(分)<3` 强制交三拍）与评论员（七项对中位，
    低者即「弱」，54章里52章出得了负）——**一个从不判谁不过的庭不是庭，而一个必然要响的器，
    响的时候不携带任何信息**。
  ③**回路没闭**：账 105 笔、93 笔未清（88.6%），`记账()` 无去重（今已焊），
    **只有产方没有收方**；**往一个消费端已饱和的系统里加生产端，加出来的只有积压**。
★★★**故此闸之律有三，缺一即不许开审**：
  · **甲·一席要占位，须说得出「它看得见而现有各席都看不见的那一样是什么」**
    （连读客说得出：多章；第二个小说家说不出）；
  · **乙·不强制出负，强制留痕**——**一席被逼着说「我在拍47停了一下，因为X」，
    这句话不论是不是伤都是信息；「非删三拍不可」不是**；
  · **丙·每一笔判须落到拍号或逐字引用之原句**，且须逐笔落「治／驳／挂」，不许只挂。

★★★★**而此器不读小说，也不判小说**——**它只管一件事：到十章了没有，上一次大审在不在，
  其席够不够，其判有没有人收。** ★**真读的那一步只有人（或替人真读的第三方）做得了**，
  器不许替它签字（`看官.py` 自陈之限：「这只眼仍是我，故它是半只眼……逮不出心里动不动」）。

用法：
    python3 工具/大审.py            ← 报：距上次大审几章、该不该开、上次之判清了没有
    python3 工具/大审.py --闸        ← 只出判（供全测调用）
    python3 工具/大审.py --立 293    ← 造一份大审之册（其模在下）
    python3 工具/大审.py --包 398 407 ← 瘦式·零 token 先行：诸器之红＋十章白文＋已付之盲读、逻辑审 → 设定/_草/大审407/包.md
    python3 工具/大审.py --录 <runId> ← 瘦式·录册归器（X27）：自 journal 排册之一、二、三节，⛔一席抄档
    python3 工具/大审.py --自测      ← 零先计红之钉（470 包回放）、诸摘、增之顶、器事之分流（W908 环8）；--闸 亦跑之
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
每 = 10                      # ★作者令：平均十章一回
段齐起 = 410                 # ★1023 作者令「设计十章→写十章→审十章」：自 410 起大审与段同界（段＝381 起每十章，段末＝410、420……）


def 到期(末, 上):
    """→ 该审至之章（段末）或 None。410 起：末以前（含）最近之段末未审即到期（审 上+1—段末；⛔段中开审）；
    其前照旧「距上一回满十章」。旧逢 7 而审（387、397、407），与段错开三章——审出之病下一段之造读不到。"""
    if 末 >= 段齐起:
        应 = 380 + (末 - 380) // 10 * 10
        return 应 if 应 >= 段齐起 and 应 > 上 else None
    return 末 if 末 - 上 >= 每 else None
册目 = os.path.join(ROOT, '设定')

# ★席之表：其名·其所独见（甲律：说不出「独见」者不许占位）
# ★1023 瘦式（X51·裁_1021_省律 九）：十二席并作四席一裁——诸旧席之问俱并入其一，⛔丢问：
#   连读客←生客·冷起手、生客·三章空降、连读客、评委、类型读者、弃卷席；小说家←白描、繁复、结构、编辑；
#   逻辑闭环←立得住、主线、悬念账、复述（并孤钩之兑删）；人物←人物之审六席（读人物链＋十章）；裁←录册之判。
#   所废：二十余席各读十章（W50 约 $75）、录册一席抄档（$21）、驳席重读、认声盲测（去名之器 X25 随之去）。
席表 = [
    ('连读客', '十章连读之读者之眼——拖、腻、弃卷、钩；并冷起手、半路进来、评委、类型读者之问：唯一看得见「同一个意思说了几遍」与「读到第几拍合书」'),
    ('小说家', '白描、繁复、结构、编辑四路合一——独见「意思已尽而字还在」「看着克制其实是空」「哪一章是多的」「信息负担」'),
    ('逻辑闭环', '立得住、主线、悬念账、复述——对圣经、canon、全书记忆：独见「凑出来的因」「线丢」「开了几个结了几个」'),
    ('人物', '诸人合一席，读人物链（全程而薄）与十章——独见「人前後不一、智之降、关系之断」'),
    ('裁', '只读四席之报与上册逾限之笔，⛔重读十章——逐笔落裁，出口归造'),
]


def _末章():
    ns = []
    for f in os.listdir(os.path.join(ROOT, '正文')):
        m = re.search(r'第([零〇一二三四五六七八九十百]+)章', f)
        if not m:
            continue
        s, t, n = m.group(1), 0, 0
        d = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
             '六': 6, '七': 7, '八': 8, '九': 9}
        for ch in s:
            if ch in d:
                n = d[ch]
            elif ch == '十':
                t += (n or 1) * 10
                n = 0
            elif ch == '百':
                t += (n or 1) * 100
                n = 0
        ns.append(t + n)
    return max(ns) if ns else 0


def 空模子(路):
    """★2026-09-13 立：一份只造了没填过的册，不算一回大审。

    ⛔其事：`大审_至第313章.md` 与 `大审_至第323章.md` 二档皆 42 行、
    通篇 `第%d—%d章`、裁定表只一行「⛔待裁」——**是 `--立` 造出来的空模子**，
    而 319—327 九章之开镜卡与悬账逐章照抄「**大审停在第313章，已欠十五章**」，
    ★**实则 `大审_至第324章.md` 248 行、裁定表逐行有裁，大审真正停在 324。**
    ⛔**一句错的现况，抄了九章。**（机制体检账 ㊧）

    ★其判只两问，皆字面可数：**模子之记号还在**（`%d` 未被换掉）
    **或 裁定表一笔裁也没有**。
    """
    try:
        t = io.open(路, encoding='utf-8', errors='replace').read()
    except Exception:
        return True
    if '%d' in t:
        return True
    _sec = t.split('## 三·')[-1].split('\n## ')[0] if '## 三·' in t else ''
    for x in _sec.splitlines():
        if x.strip().startswith('|') and ('已治' in x or '判驳' in x
                                          or '判不治' in x or '已挂' in x):
            return False
    return True


def 诸册(含空=False):
    out = []
    for f in sorted(os.listdir(册目)):
        m = re.match(r'大审_至第(\d+)章\.md$', f)
        if m:
            路 = os.path.join(册目, f)
            if not 含空 and 空模子(路):
                continue
            out.append((int(m.group(1)), 路))
    return sorted(out)


def 账():
    末 = _末章()
    cs = 诸册()
    上 = cs[-1][0] if cs else 0
    距 = 末 - 上
    判 = []
    止 = 到期(末, 上)
    if 止:
        判.append('⛔大审到期（审 %d—%d；距上次 %d 章·410 起与段同界）——**该开一回大审**：'
                  '★其席须≥5且各说得出其「独见」；★★其判须逐笔落拍号；'
                  '★★★跑 python3 工具/大审.py --立 %d 造其册。' % (上 + 1, 止, 距, 止))
    # ★上一册之判有没有人收（丙律）
    if cs:
        t = io.open(cs[-1][1], encoding='utf-8', errors='replace').read()
        # ★【立闸当日即修】初版数的是§二里九席之原话（`· ⛔` 起手者，22条），
        #   ★★而§三之职正是把那些原话**并**成可裁之笔（今为9笔）——
        #     **拿并前之数去比并後之数，它永远差着**；
        #   ★★★故改数§三那张裁定表之行：**逐行须有一裁**（已治／判驳／判不治／已挂）。
        #   ★★★★而「已挂」须带其限（限N）方算一裁——**挂而无限，是把账搬个地方放着**。
        _sec = t.split('## 三·')[-1].split('\n## ')[0] if '## 三·' in t else ''
        _rows = [x for x in _sec.splitlines()
                 if x.strip().startswith('|') and x.count('|') >= 5
                 and not re.match(r'^\s*\|[\s\-:|]+\|\s*$', x)
                 and '判（席·题）' not in x]
        挂 = len(_rows)
        # ★★★★★2026-09-23·限359（本坐填「至第357章」一册时所逮）：**补两样真判之名。**
        #   ⛔**旧式只认四样**（已治／判驳／判不治／已挂＋限），**而一庭之上真会出的判不止四样**：
        #     ①**「半治·半驳」**——**一判之中取其半、驳其半**（如编辑席既指对了那一拍係第六次「空着」，
        #       而其「移末拍」之议会断掉四章之倒数）；②**「留痕·不裁」**——**一席自书「无致命之判」**，
        #       **其身无可裁，而⛔它须入册**（坑㉗所要的正是这一样：交白卷而说得出何以白）。
        #   ★**旧式之下，这两样各算一行「没人收」**，**於是本器逼着填册的人把它们改写成假的「已治」或「判驳」**——
        #     ⛔**一道闸若逼着人为过它而改判，那道闸就是在教人说谎**（④之五之律）。
        #   ⛔**而其口开得极窄**：**只认这两个整词，⛔不认单独一个「治」「驳」「挂」字**
        #     （⛔否则「⛔待裁」之模子里那一行也会被「裁」字放过去·同日负测④在守）。
        收 = len([x for x in _rows
                  if ('已治' in x or '判驳' in x or '判不治' in x
                      or '半治' in x or '留痕·不裁' in x
                      or ('已挂' in x and re.search(r'限\s*\d+', x)))])
        if 挂 and 收 < 挂:
            判.append('⛔上一册（至第%d章）裁定表 %d 行，而落了裁者只 %d 行——'
                      '**只有产方没有收方，账一成噪声，真的那几笔就没人看了**；'
                      '★而「已挂」须带其限方算一裁。'
                      % (cs[-1][0], 挂, 收))
        elif not 挂:
            判.append('⛔上一册（至第%d章）无裁定表——**逐席之判须并成可裁之笔**（丙律）。'
                      % cs[-1][0])
        # ★★★★★★2026-09-13 补第三问（本器自己欠的那一样）：
        #   ⛔**册上自书「『挂』不是把裁推开：它带着限，到期不裁即是逾期，器会报」**
        #   ——**而本器从来没有数过那个限到没到**：**它只问「已挂带没带一个数」。**
        #   ★**即一句写在册上的话，盘上没有一只手兑它**（本册 ㊚ 之同骨：**账断了一头**）；
        #   ★★**而这一路比那一路更难见**：**它不是报错了，是它从头到尾没在看。**
        #   ⛔**故补此问：凡「已挂·限N」而末章已过 N 者，当场报逾期。**
        # ⛔**立日即自栽一回**：头一版拿整行去找「限N」并取其最小
        #   ——**而一笔之「其由」那一格里常引着别的限**（0913 第11笔引 FS 之旧限 309），
        #   **於是它把别人的旧限当成了这一笔的限，当场报了一个假逾期。**
        #   ★**其治**：**一笔之限只认「已挂」所在那一格**（裁之格），⛔**其由之格一个数也不取**。
        # ★1119（W907 复核·同功两处）：逾之读归 限於 → 三之行（一析：裁之格取其限、「〔原：…〕」⛔取、三栏之旧笔表与「改挂」俱认）
        逾 = [(号, lim) for 号, lim, _ in 限於(末)]
        if 逾:
            判.append('⛔上一册（至第%d章）之「已挂」逾限 %d 笔（今为第%d章）：%s'
                      '——**挂带着限，到期不裁即是逾期**；'
                      '★**其裁须当场下或当面改限，⛔不许静静顺延。**'
                      % (cs[-1][0], len(逾), 末,
                         '、'.join('第%s笔(限%d)' % (i, l) for i, l in 逾)))
    return 末, 上, 距, 判


def 限於(n):
    """★1016（394 逮：393 记席照 大问表 之印填 394 卡问七，⛔见大审册「已挂·限394」之 #23——开镜卡漏、封版必逾）：
    上一册§三里「已挂」之笔其限 ≤ n 者 → [(号, 限, 其裁格之文)]。
    ★1119（W907 复核·同功两处）：逐行之读归 三之行（一析）——旧读只认五管以上之行、字面「已挂」，
      於是 录() 所写之「上册逾限之笔·当面裁」三栏之表（四管）、「改挂·限N」俱⛔见，开镜卡问七与下一回之旧笔⛔及。"""
    cs = 诸册()
    if not cs:
        return []
    t = io.open(cs[-1][1], encoding='utf-8', errors='replace').read()
    return [(r['号'], r['限'], re.sub(r'\s+', ' ', r['裁']).strip())    # ★1020：⛔截二百字（399 卡问七抄得半句）——卡须逐字抄其全裁
            for r in 三之行(t) if r['类'] == '已挂' and r['限'] is not None and r['限'] <= n]


_裁之词 = ('待裁', '判不治', '半治', '改挂', '已挂', '已治', '判驳', '留痕')
_隔式 = re.compile(r'^\s*\|[\s\-:|]+\|\s*$')


def _去原(s):
    """裁格去其「〔原：…〕」（可嵌：387 之「〔原：**旧期**（…〔原：…〕）〕」）——原裁係旧，⛔作今裁。"""
    出, 深 = [], 0
    i = 0
    while i < len(s):
        if 深 == 0 and s.startswith('〔原', i):
            深 = 1
            i += 2
            continue
        if 深:
            深 += {'〔': 1, '〕': -1}.get(s[i], 0)
        else:
            出.append(s[i])
        i += 1
    return ''.join(出)


def 裁之类(裁):
    """裁格 → (类, 限)。类取首见之词（「待裁」作他、「改挂」作已挂）；而首见非挂、「〔原：…〕」之外仍书「已挂／改挂…限N」者作已挂——
    397 #11「**半治**——删…；**已挂·限 W11 之 391 节（器上·限407）**」、#72「已治之部照记；…三处已挂·…·限417」：所挂之余⛔丢。
    限＝类为已挂者，「〔原：…〕」之外「限N」之最小（⛔取其由之格；无数者 None＝限非数）。"""
    净 = _去原(裁 or '')
    位 = sorted((净.find(w), w) for w in _裁之词 if w in 净)
    类 = 位[0][1] if 位 else '他'
    类 = {'待裁': '他', '改挂': '已挂'}.get(类, 类)
    if 类 not in ('已挂', '他') and re.search(r'(?:已挂|改挂)[^；;。|]{0,40}?限\s*\d', 净):
        类 = '已挂'
    ms = re.findall(r'限\s*(\d+)', 净) if 类 == '已挂' else []
    return 类, (min(int(y) for y in ms) if ms else None)


def 三之行(t):
    """★1119（W907 判者②·细④：剧情全图另写之§三之析并入本器·⛔同功两处）册之文 → §三裁定表逐行
    [{'号', '类', '判', '据', '裁', '限', '行'}]——限於、账、诸挂、剧情全图 俱读此一析。
    表头每表重取（其下一行係「|---|」者为头：337 首表「合｜撞上它的席｜其事」、407／410 次表「旧号｜裁｜其由」；
    表中插「>」之注而续者⛔作新表，续用前头）；无「裁」栏之表跳过（337「合」、324「刀」）。
    栏以表头定（判／据／裁／其由之首字；无判栏者判取其由）；类、限见 裁之类；行＝档之行（1 起）。"""
    L = (t or '').split('\n')
    出, 在, 头 = [], False, None
    for i, l in enumerate(L):
        if l.startswith('## '):
            在, 头 = l.startswith('## 三'), None
            continue
        if not (在 and l.startswith('|')) or _隔式.match(l):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if i + 1 < len(L) and _隔式.match(L[i + 1]):
            头 = c
            continue
        k = next((j for j, x in enumerate(头 or []) if x.startswith('裁')), None)
        if k is None:
            continue
        p = next((j for j, x in enumerate(头) if x.startswith('判')), None)
        q = next((j for j, x in enumerate(头) if x.startswith('据')), None)
        由 = next((j for j, x in enumerate(头) if x.startswith('其由')), None)
        p = p if p is not None else 由
        裁 = c[k] if k < len(c) else ''
        类, 限 = 裁之类(裁)
        出.append({'号': c[0], '类': 类, '判': c[p] if p is not None and p < len(c) else '',
                  '据': c[q] if q is not None and q < len(c) else '', '裁': 裁, '限': 限, '行': i + 1})
    return 出


def 诸挂(末=None):
    """★1119（W907 判者②：大审440 #1—12「已挂·限451」十一笔无人看）诸册§三之「已挂」而无人收者 →
    [{'至', '档', '号', '限', '裁', '判', '据', '行', '下册', '旧笔不及', '收於'}]，照册、号排。
    旧笔之隙：限於(b) 只读上一册——册 V 之笔限 > 其下一册之至者，下一册之旧笔不及（彼时未到限），再下一册又不读 V，⛔无人看。
    又（W907 复核）：1119 前之 限於 只读五管以上、字面「已挂」之行——三栏之旧笔表（407 次表「前册#11…限417」十四笔）、
      「改挂·限N」（410:114）其下一册之包⛔见；故此等行限虽 ≤ 下一册之至，亦作不及（⛔假定下一册已见）。
    所出：末册之「已挂」（限於 管之，照出）；前诸册之「已挂」而旧笔不及或限非数（None）者，
    後诸册§三未提其号（「大审V #号」「至第V章…#号」，或下一册之「前册#号」）、本册别行亦未已裁其号（「前册#N」之笔：
    410 #18「旧笔前册#16 到期未兑｜已治·414」）方出——提者即「收於」该册（⛔猜其裁）。
    末：只出 限 ≤ 末 者与限非数者（None＝俱出）。"""
    cs = 诸册()
    文 = {至: io.open(路, encoding='utf-8', errors='replace').read() for 至, 路 in cs}

    def 三节(t):
        m = re.search(r'(?ms)^## 三.*?(?=^## |\Z)', t)
        return m.group(0) if m else ''
    出 = []
    for i, (至, 路) in enumerate(cs):
        下 = cs[i + 1][0] if i + 1 < len(cs) else None
        L = 文[至].split('\n')
        行们 = 三之行(文[至])
        for r in 行们:
            if r['类'] != '已挂':
                continue
            原 = L[r['行'] - 1]
            旧见 = 原.count('|') >= 5 and '已挂' in 原              # 1119 前 限於 之二门（史之实：下一册之包係旧读所出）
            不及 = 下 is not None and (r['限'] is None or r['限'] > 下 or not 旧见)
            if 下 is not None and not 不及:
                continue                                    # 下一册之旧笔（或账之逾限）已见之
            if 末 is not None and r['限'] is not None and r['限'] > 末:
                continue
            号 = re.escape(re.sub(r'[*\s]', '', r['号']))
            收 = [w for w, _ in cs[i + 1:] if re.search(r'(?:大审\s*%d|至第\s*%d\s*章)[^#|\n]{0,8}#\s*%s(?!\d)' % (至, 至, 号), 三节(文[w]))]
            if not 收 and 下 is not None and re.search(r'前册\s*#\s*%s(?!\d)' % 号, 三节(文[下])):
                收 = [下]
            if not 收 and 号.startswith('前册') and any(
                    x is not r and x['类'] in ('已治', '判驳', '判不治', '半治') and re.search(号 + r'(?!\d)', x['判'] + x['据'] + x['裁'])
                    for x in 行们):
                收 = [至]
            if 收 and 下 is not None:
                continue
            出.append(dict(r, 至=至, 档=os.path.relpath(路, ROOT), 下册=下, 旧笔不及=不及, 收於=收[0] if 收 else None))
    return 出


def 号之名(至, 号):
    """「大审V #号」；号係次表之「前册#N」者书「大审V 前册#N」（⛔「#前册#N」）。"""
    号 = re.sub(r'\*', '', str(号)).strip()
    return '大审%d %s' % (至, 号) if 号.startswith('前册') else '大审%d #%s' % (至, 号)


def 立(n):
    p = os.path.join(册目, '大审_至第%d章.md' % n)
    if os.path.exists(p):
        print('★已在：%s' % p)
        return p
    lo = max(1, n - 每 + 1)
    io.open(p, 'w', encoding='utf-8').write(
        ('# 大审 · 至第%d章（第%d—%d章）\n\n' % (n, lo, n)) +  # ★0925 逮：此行原无 % 代入，册首印出「%d」字样
        '> **★作者令**：「平均10章就应该从头到尾进行一个剧情和质量各个方面严格把控。」\n'
        '> **★★而此册之律三**（`工具/大审.py` 头所载）：\n'
        '> **甲**·一席要占位，须说得出「它看得见而现有各席都看不见的那一样是什么」；\n'
        '> **乙**·不强制出负，**强制留痕**；\n'
        '> **丙**·每一笔判须落到拍号或逐字引用之原句，且须逐笔落「治／驳／挂」。\n\n'
        '## 一·本回之席（其名｜其独见｜其所读）\n\n'
        '| 席 | 其独见（甲律·说不出者不许占位） | 所读 |\n|---|---|---|\n'
        + ''.join('| %s | %s | 〔第N—N章〕 |\n' % (a, b) for a, b in 席表) +
        '\n## 二·逐席之判（乙律·留痕；丙律·落拍号）\n\n'
        '〔逐席一节，每节：其所答之全文＋其致命之判（题／据／何以要命／拟治）〕\n\n'
        '## 三·逐笔裁定（丙律·不许只挂）\n\n'
        '| # | 判（席·题） | 据（章·拍·原句） | 裁 | 其由 |\n|---|---|---|---|---|\n'
        '| 1 | | | ⛔待裁／已治／判驳／已挂 | |\n\n'
        '## 四·本回之数（器出，非估）\n\n'
        '〔净重之趋／约到期／大问表逾期之样／看官账未清之数〕\n\n'   # ★1027：站账随一坐之群汰，其数⛔再索
        '## 五·本回之得（一句话）\n\n'
        '〔**这十章合起来，是「慢而深」还是「原地打转」**〕\n')
    print('★大审之册已立：%s' % p)
    print('★★而它须由真读的席来填——**器不许替它签字**。')
    return p


def 印(只闸=False):
    末, 上, 距, 判 = 账()
    if not 只闸:
        print('\n════ 大审 · 以第%d章计 ════' % 末)
        print('  【其律】平均 %d 章一回，从头到尾，逐席真读。' % 每)
        print('  上次大审：%s｜距今 %d 章' % (('至第%d章' % 上) if 上 else '**从来没有过**', 距))
        print('  ── 席之表（%d 席·各须说得出其独见）──' % len(席表))
        for a, b in 席表:
            print('   · %-14s %s' % (a, b))
        print('  ★而此器不读小说、不判小说——它只管「到十章了没有、席够不够、判有没有人收」。')
    else:
        # ★2026-09-05·机制总审：只闸之式原一字不印即为绿——全测之 hook 索器自印之头（§一⑤），故只闸亦印一行头。
        print('════ 大审 · 以第%d章计（只闸）════ 上次%s｜距今 %d 章' % (末, ('至第%d章' % 上) if 上 else '无', 距))
    for x in 判:
        print('  ' + x)
    if not 判:
        print('  ✓不到期，或上一册之判已逐笔落裁。')
    return 判



def _汉(n):
    d = '零一二三四五六七八九'
    if n < 10:
        return d[n]
    if n < 20:
        return '十' + (d[n % 10] if n % 10 else '')
    if n < 100:
        return d[n // 10] + '十' + (d[n % 10] if n % 10 else '')
    h, r = n // 100, n % 100
    if r == 0:
        return d[h] + '百'
    if r < 10:
        return d[h] + '百零' + d[r]
    return d[h] + '百' + d[r // 10] + '十' + (d[r % 10] if r % 10 else '')


def 章档(n):
    for f in sorted(os.listdir(os.path.join(ROOT, '正文'))):
        if ('_第%s章_' % _汉(n)) in f:
            return os.path.join(ROOT, '正文', f)
    return None


def 白文(n):
    p = 章档(n)
    if not p:
        return None
    out = []
    for i, l in enumerate(io.open(p, encoding='utf-8', errors='replace').read().split('\n'), 1):
        if '【本章亮点】' in l:
            break
        out.append('%d\t%s' % (i, l))
    return '\n'.join(out)


def _节(t, 题, 末=True):
    """轮记中题含 题 之 ## 节（末＝取末一回）。"""
    ps = re.split(r'(?m)^(?=## )', t)
    hs = [x for x in ps if x.startswith('## ') and 题 in x.split('\n', 1)[0]]
    return (hs[-1] if 末 else hs[0]).strip() if hs else ''


包目 = lambda b: os.path.join(ROOT, '设定', '_草', '大审%d' % b)
零先之器 = [('抄袭闸', ['抄袭闸.py', '--段']), ('刻意之疲', ['刻意之疲.py']), ('悬念哨', ['悬念哨.py']),
          ('线限哨', ['线限哨.py']), ('清偿章哨', ['清偿章哨.py'])]

# ★W908 环8（1119·用之审）：零先之器之⛔行，须带其所指方计红——账号（SUS-B-磨窝、CHAR-282A）、「限 N」、「第N章」
#   （抄袭闸之红以章为指，⛔漏）；头注之⛔（「⛔本器只报不拦」「⛔不许专开一拍」）⛔计。旧守 '只报不拦' not in x[:6]，
#   而 x 带行首之空、守不着：大审470 包悬念哨「红 3 行」真者 1、线限哨「红 1 行」真者 0。⚠✗红 之行照旧。
_所指 = re.compile(r'(?<![A-Za-z])[A-Z]{2,}-[0-9A-Za-z一-龥]|限\s*\d|第\s*\d+\s*章')


def 计红(x):
    """零先之器之一行计红否（纯判）。"""
    if not re.search(r'⛔|⚠|✗|红', x) or '只报不拦' in x[:6]:
        return False
    return '⛔' not in x or bool(_所指.search(x))


# ★W908 环8：半用之器接入——外声闸、改记（常令:43 之读路）入包：读者可见之旁证（出声几句；封後改了哪几行——已付之
#   盲读、逻辑审判於改前），四席用之。窗界哨之未答（裁八「改入大审包之报（不拦）」）、处方旗哨、末十章 _器之迹.md 之
#   rc≠0 係器之事：其报只印 --包 之出，与段末囤灰普查同块（主环读之、当段裁）；⛔入 包.md——1027 之裁「四席⛔读器之事」，
#   入则四席各读约 1KB 而⛔用，主环不读包、裁席不读包（W908 验·坑6／坑52）。增之顶 3KB（包与主环之出合计；守瘦式 ≤$25）：
#   逾即自价最低者删，删者留一行之指。⛔入章料、开镜卡：外声之静是戏，⛔成配额。
增顶 = 3 * 1024


def _跑器(令, 时=300):
    import subprocess
    try:
        r = subprocess.run(['python3', os.path.join(ROOT, '工具', 令[0])] + 令[1:], cwd=ROOT,
                           capture_output=True, text=True, timeout=时)
        return (r.stdout or '') + (r.stderr or '')
    except Exception as e:
        return '（跑不成：%s）' % e


def 外声之摘(o, a, b):
    """外声闸之印（其表：章 出声句 出声字 别人问他 句）→ a—b 出声几句几字、最长连零（只报）。"""
    行 = {}
    for x in o.splitlines():
        m = re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)[ \t]*(.*)$', x)
        if m and a <= int(m.group(1)) <= b:
            行[int(m.group(1))] = (int(m.group(2)), int(m.group(3)), m.group(5).strip())
    if not 行:
        return ['- **外声闸**：（未得 %d—%d 之数：%s）' % (a, b, (o.strip().splitlines() or ['无印'])[-1][:60])]
    长 = 今 = 0
    for n in range(a, b + 1):
        今 = 今 + 1 if n in 行 and 行[n][0] == 0 else 0
        长 = max(长, 今)
    引 = '；'.join('%d「%s」' % (n, re.sub(r'[「」“”]', '', v[2].split('｜')[0])[:12])
                  for n, v in sorted(行.items()) if v[0] and v[2])
    判 = [x.strip() for x in o.splitlines() if re.match(r'\s*[⛔⚠] 逾', x)][:1]
    return ['- **外声闸**（只报·静是戏，⛔配额）：%d—%d 出声 %d 句 %d 字%s｜最长连零 %d 章%s' % (
        a, b, sum(v[0] for v in 行.values()), sum(v[1] for v in 行.values()),
        ('（%s）' % 引[:120]) if 引 else '', 长, ('｜' + 判[0][:40]) if 判 else '')]


def 改记之摘(印们):
    """{章: `改记.py --章 N` 之印} → 封後改正文之摘：同一提交并一行（章:行）。封版之笔及其前（稿之成）⛔录。"""
    提 = {}
    for n in sorted(印们):
        块 = re.split(r'(?m)^■ ', 印们[n])[1:]                       # 新者在前
        封 = [i for i, k in enumerate(块) if re.search(r'第%d章《[^》\n]*》封版' % n, k.split('\n', 1)[0])]
        if not 封:                                                  # 无封版之笔：正文之最旧一笔即其成
            封 = [i for i, k in enumerate(块) if '· 正文/' in k] or [0]
        封 = 封[-1]                                                 # 首封（重封前之改亦录）
        for k in 块[:封]:
            头, _, 身 = k.partition('\n')
            m = re.search(r'(?m)· 正文/.*?行：(.+)$', 身)
            if not m:
                continue
            时, 号, 说 = (头.split('｜', 2) + ['', ''])[:3]
            提.setdefault(号, [时, 说, []])[2].append('%d:%s' % (n, m.group(1).strip()[:40]))
    if not 提:
        return ['- **改记**：封後正文无改。']
    序 = sorted(提.items(), key=lambda kv: kv[1][0], reverse=True)
    L = ['- **改记·封後改正文**（`改记.py --章 N`；已付之盲读、逻辑审判於改前）：%d 笔' % len(序)]
    L += ['    %s %s「%s」→ %s' % (v[0][5:10], 号, v[1][:28], '｜'.join(v[2]))[:300] for 号, v in 序[:6]]
    return L


def 窗界之摘(rows, txt):
    """窗界哨.扫() 之行与窗界账之文 → 未答之摘（以 窗界哨.对档 判答否，⛔另立其式）。"""
    import 窗界哨
    未 = [r for r in rows if not 窗界哨.对档(txt, [r])[0]]
    L = ['- **窗界哨**（裁八：未答者入大审之报、⛔拦）：缺界之窗 %d、答过 %d、未答 %d%s' % (
        len(rows), len(rows) - len(未), len(未), '' if 未 else ' ✓')]
    L += ['    `%s` 行%d·缺%s' % (r[5][:70], r[1], r[4]) for r in 未[:8]]
    return L


def 处方旗之摘(o):
    m = re.search(r'处方里点名之旗 (\d+) 处', o)
    红 = [x.strip() for x in o.splitlines() if re.match(r'\s*⛔ 工具/', x)]
    if 红:
        return ['- **处方旗哨**：红 %d 行（旗不认即照默认路走）' % len(红)] + ['    ' + x[:160] for x in 红[:6]]
    return ['- **处方旗哨**：%s' % (('✓（处方之旗 %s 处，器俱认）' % m.group(1)) if m
                                  else '（未得其数：%s）' % (o.strip().splitlines() or ['无印'])[-1][:60])]


def 器之迹之摘(a, b, root=None):
    """a—b 之 版本/第N章/_器之迹.md 之 rc≠0 行 → 一摘：败多者八，例中器自坏（exc）者尽列。闸之红亦计败，真假由主环分。
    与囤灰普查之「候修·败多」（_器之迹.jsonl 全史）係一信两窗：主环之块以此紧接其上，⛔另处再报（坑53）。"""
    聚, 缺 = {}, []
    for n in range(a, b + 1):
        p = os.path.join(root or ROOT, '版本', '第%d章' % n, '_器之迹.md')
        if not os.path.exists(p):
            缺.append(n)
            continue
        for l in io.open(p, encoding='utf-8', errors='replace'):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if len(c) < 7 or not (c[1].isdigit() and c[2].isdigit()) or int(c[2]) == 0:
                continue
            x = 聚.setdefault(re.sub(r'\.(py|js)$', '', c[0]), {'跑': 0, '败': 0, '章': 0, '异': []})
            x['跑'] += int(c[1])
            x['败'] += int(c[2])
            x['章'] += 1
            x['异'] += re.findall(r'rc=exc:(\w+)', '|'.join(c[6:]))
    if not 聚:
        return ['- **器之迹·败**：%d—%d 无 rc≠0 之行%s' % (a, b, ('（缺迹：%s）' % '、'.join(map(str, 缺))) if 缺 else '')]
    序 = sorted(聚.items(), key=lambda kv: (-kv[1]['败'], kv[0]))
    L = ['- **器之迹·败**（本段 %d—%d 之 `_器之迹.md` rc≠0；全史之败多即下普查「候修」；闸之红亦计，真假由主环分）：器 %d、败 %d' % (
        a, b, len(聚), sum(v['败'] for v in 聚.values()))]
    L.append('    败多：' + '、'.join('%s %d/%d（%d 章）' % (k, v['败'], v['跑'], v['章']) for k, v in 序[:8]))
    异 = {}
    for k, v in 序:
        for e in v['异']:
            异.setdefault(e, [])
            if k not in 异[e]:
                异[e].append(k)
    if 异:
        L.append('    例中器自坏：' + '；'.join('%s（%s）' % (e, '、'.join(ks[:4])) for e, ks in sorted(异.items())))
    if 缺:
        L.append('    缺迹：' + '、'.join(map(str, 缺)))
    return L


def 字节(行们):
    return len(('\n'.join(行们) + '\n').encode('utf-8')) if 行们 else 0


def 限增(块们, 顶=增顶):
    """块们：[(名, 行们, 指)]，前者价高 → (留之行们, 省之名们)。总字节逾顶即自末删，删者代以一行之指。"""
    块们 = [list(x) for x in 块们]
    省 = []
    for x in reversed(块们):
        if sum(字节(y[1]) for y in 块们) <= 顶:
            break
        x[1] = ['- **%s**：逾增之顶（%dB）而省——主环自跑 %s' % (x[0], 顶, x[2])]
        省.append(x[0])
    return 块们, 省


def 排(外, 改, 窗, 旗, 迹, 顶=增顶):
    """诸摘 → (入包之行们, 印主环之行们, 省之名们)。价序 外声、改记、窗界、处方旗、器之迹（逾顶自末删）；
    器之迹居器事之末，主环之块里紧接囤灰普查之「候修」。"""
    块们, 省 = 限增([('外声闸', 外, '`外声闸.py`'), ('改记', 改, '`改记.py --章 N`'), ('窗界哨', 窗, '`窗界哨.py`'),
                    ('处方旗哨', 旗, '`处方旗哨.py`'), ('器之迹', 迹, '`囤灰闸.py --迹 N`')], 顶)
    return 块们[0][1] + 块们[1][1], 块们[2][1] + 块们[3][1] + 块们[4][1], 省


# 〔执行之制·治15（1124·482 主环收批）〕普查必裁：段末之普查写入 设定/囤灰普查.md（每段一节·本器唯一写者），总编辑对每候书判
#   「删：由／修：由／留：由／假候：由」（如 记落.py「410 rc=2」係自测故意期望 rc 2 → 假候）；同一候连两段无判 → 其行标「（前段亦无判）」，
#   法用#囤灰普查随段 之证（下段首验）见之即红。⛔改他行之判（已判者照留·重跑只添新候）。
普查档 = os.path.join('设定', '囤灰普查.md')
普查之首 = ('# 囤灰普查（段末 `大审.py --包` 自写·本器唯一写者；执行之制·治15「普查必裁」）\n\n'
          '> 每段一节；每候一行，总编辑於「｜判：」後书「删：由」「修：由」「留：由」或「假候：由」（⛔空）。同一候连两段无判，'
          '器於其行标「（前段亦无判）」——法用#囤灰普查随段 下段首验见之即红。器只添节、添新候、标连两段，⛔改已书之判。\n')
_普候式 = re.compile(r'(?m)^- (候修|候退|档之囤灰) · (.+?) —— (.*?)(（前段亦无判）)?｜判：(.*)$')


def 普查之候(普文):
    """囤灰闸 --普查 之印 → [(类, 名, 由)]（「  候修 N」之下「    · 名 —— 由」）。"""
    出, 类 = [], None
    for l in (普文 or '').split('\n'):
        m = re.match(r'^\s{2}(候修|候退|档之囤灰)\s+\d+', l)
        if m:
            类 = m.group(1)
            continue
        m = re.match(r'^\s{4}· (.+?) —— (.*)$', l)
        if m and 类:
            出.append((类, m.group(1).strip(), m.group(2).strip()))
    return 出


def 普查之节(旧, a, b, 候们):
    """旧（设定/囤灰普查.md 之全文·或空）、本段 a—b、候们 → 新全文。本段之节已在：已有之行照留（其判⛔动）、只添新候；
    前段（a-10—b-10）之节中无判之候、本段又见而本段亦无判 → 标「（前段亦无判）」。"""
    旧 = 旧 or 普查之首
    节们 = re.split(r'(?m)^(?=## )', 旧)
    首, 节们 = 节们[0], 节们[1:]
    键 = lambda a_, b_: '## %d—%d' % (a_, b_)
    前节 = next((x for x in 节们 if x.startswith(键(a - 10, b - 10))), '')
    前无判 = {(m.group(1), m.group(2)) for m in _普候式.finditer(前节) if not m.group(5).strip()}
    本 = next((x for x in 节们 if x.startswith(键(a, b))), None)
    旧行 = {(m.group(1), m.group(2)): m for m in _普候式.finditer(本 or '')}
    行们 = []
    for 类, 名, 由 in 候们:
        m = 旧行.pop((类, 名), None)
        判 = m.group(5).strip() if m else ''
        标 = '（前段亦无判）' if not 判 and (类, 名) in 前无判 else ''
        行们.append('- %s · %s —— %s%s｜判：%s' % (类, 名, (m.group(3) if m else 由), 标, 判))
    for (类, 名), m in 旧行.items():          # 旧候本回不见（已删、已修）→ 照留其行（判在则判在；无判而去者⛔标）
        行们.append(m.group(0))
    新节 = '%s（段末普查·候 %d·判 %d）\n\n%s\n' % (键(a, b), len(行们), sum(1 for l in 行们 if l.split('｜判：', 1)[1].strip()),
                                         '\n'.join(行们) if 行们 else '（无候）')
    if 本 is None:
        节们.append(新节 + '\n')
    else:
        节们 = [新节 + '\n' if x is 本 else x for x in 节们]
    节们.sort(key=lambda x: int(re.match(r'## (\d+)', x).group(1)) if re.match(r'## (\d+)', x) else 0)
    return 首.rstrip('\n') + '\n\n' + '\n\n'.join(x.rstrip('\n') for x in 节们) + '\n'


def 写普查(a, b, 普文, root=None):
    """把普查之印写入 设定/囤灰普查.md 之本段之节（本器唯一写者）→ (候数, 未判数, 连两段无判数)。"""
    p = os.path.join(root or ROOT, 普查档)
    try:
        旧 = io.open(p, encoding='utf-8').read()
    except OSError:
        旧 = ''
    新 = 普查之节(旧, a, b, 普查之候(普文))
    io.open(p, 'w', encoding='utf-8').write(新)
    节 = next((x for x in re.split(r'(?m)^(?=## )', 新) if x.startswith('## %d—%d' % (a, b))), '')
    ms = list(_普候式.finditer(节))
    return len(ms), sum(1 for m in ms if not m.group(5).strip()), sum(1 for m in ms if m.group(4) and not m.group(5).strip())


def 主环之块(器事, 普查):
    """--包 之出之末块（只主环读：四席⛔读、⛔入包）：器之事在前，囤灰普查在後——器之迹（本段）紧接普查之「候修」（全史）。"""
    return '\n'.join(['── 主环·段末器之事与囤灰普查（零 token·只报；候者当段裁：删、修或留由）──'] + 器事
                     + [(普查 or '').strip() or '（普查无出）'])


def 接入(a, b):
    """→ (入包之行们, 印主环之行们, 省之名们)。"""
    外 = 外声之摘(_跑器(['外声闸.py', str(max(_末章(), b) - a + 1)]), a, b)
    改 = 改记之摘({n: _跑器(['改记.py', '--章', str(n)], 120) for n in range(a, b + 1)})
    try:
        import 窗界哨
        zh = os.path.join(ROOT, '设定', '窗界账.md')
        窗 = 窗界之摘(窗界哨.扫(), io.open(zh, encoding='utf-8', errors='replace').read() if os.path.exists(zh) else '')
    except Exception as e:
        窗 = ['- **窗界哨**：（跑不成：%s）' % str(e)[:80]]
    return 排(外, 改, 窗, 处方旗之摘(_跑器(['处方旗哨.py'])), 器之迹之摘(a, b))


def 包(a, b):
    """★1023 X51·瘦式之一「零 token 先行」与之三「虹吸」：诸器先跑、其红汇一页；十章白文（带行号）与各章已付之盲读、
    逻辑审之读误之判同入一包——诸席一读即得，⛔各自重找。→ 设定/_草/大审B/包.md"""
    import subprocess
    os.makedirs(包目(b), exist_ok=True)
    L = ['# 大审之包 · 第%d—%d章（零 token 所汇·诸席同读此一档）\n' % (a, b),
         '## 甲·器之红（零 token 先行：机械之病已由器逮，⛔再劳你找；你只判其中读者可见者）\n']
    for 名, 令 in 零先之器:
        a_ = ['python3', os.path.join(ROOT, '工具', 令[0])] + 令[1:] + ([str(a), str(b)] if 令[-1] == '--段' else [])
        try:
            r = subprocess.run(a_, cwd=ROOT, capture_output=True, text=True, timeout=300)
            o = (r.stdout or '') + (r.stderr or '')
        except Exception as e:
            o = '（跑不成：%s）' % e
        红 = [x for x in o.splitlines() if 计红(x)]
        L.append('- **%s**：%s' % (名, ('红 %d 行' % len(红)) if 红 else '✓'))
        L += ['    ' + x.strip()[:240] for x in 红[:12]]
        # ★1118 总编辑复核·刻意之疲 改（0ad2fad7c）：只照镜之器（恒绿）以「镜·」起之行照录——镜给大审之通读者，⛔算红
        L += ['    ' + x.strip()[:240] for x in o.splitlines() if x.strip().startswith('镜·') and x not in 红][:4]
    for n in range(a, b + 1):
        try:
            r = subprocess.run(['python3', os.path.join(ROOT, '工具', '整句复述哨.py'), str(n)], cwd=ROOT,
                               capture_output=True, text=True, timeout=120)
            o = r.stdout or ''
        except Exception:
            o = ''
        if '本章无一句' not in o and o.strip():
            L.append('- **整句复述哨·%d**：' % n)
            L += ['    ' + x.strip()[:240] for x in o.splitlines()[2:10] if x.strip()]
    try:
        旁, 器事, 省 = 接入(a, b)   # ★W908 环8：半用之器接入（合顶 3KB）；旁证入包、器之事只印主环；败⛔碍包之成
    except Exception as e:
        旁, 器事, 省 = [], ['- **半用之器接入**：（跑不成：%s）' % str(e)[:80]], []
    L += 旁
    # ★1119（W907 用之审·作者「做出来的东西都执行和用起来」）：全书之图（剧情全图·零 token·封版 --後 重生）之「一眼」入包——
    #   诸席先见全书之脊、未闭之环、漏之热、可升之位，⛔各翻散账；一章之全 `python3 工具/剧情全图.py --章 N`、一线 `--线 词`
    图 = os.path.join(ROOT, '设定', '全书记忆', '剧情全图.md')
    if os.path.exists(图):
        m = re.search(r'(?ms)^## 一眼\n(.*?)(?=^## |\Z)', io.open(图, encoding='utf-8', errors='replace').read())
        if m:
            L += ['\n## 甲之三·全书之图（`设定/全书记忆/剧情全图.md`「一眼」逐字；②开环、③漏、④升之全条见其档；'
                  '一章 `python3 工具/剧情全图.py --章 N`、一线 `--线 词`）\n', m.group(1).strip(), '']
    L.append('\n## 乙·十章白文（带原行号；引句一律「章:行」）与各章已付之盲读、逻辑审之末判\n')
    缺 = []
    for n in range(a, b + 1):
        t = 白文(n)
        if t is None:
            缺.append(n)
            continue
        L.append('### 第%d章 · %s\n' % (n, os.path.basename(章档(n))))
        L.append(t)
        rp = os.path.join(ROOT, '版本', '第%d章' % n, '_轮记.md')
        if os.path.exists(rp):
            rt = io.open(rp, encoding='utf-8', errors='replace').read()
            盲 = _节(rt, '盲读')
            审 = _节(rt, '逻辑审')
            误 = ''
            if 审:
                m = re.search(r'(?ms)^### 读误之判.*', 审)
                误 = m.group(0) if m else ''
            if 盲:
                L.append('\n#### 第%d章·已付之盲读（末回）\n%s' % (n, 盲[:3000]))
            if 误:
                L.append('\n#### 第%d章·已付之逻辑审·读误之判（末回）\n%s' % (n, 误[:1500]))
        L.append('')
    if 缺:
        raise SystemExit('⛔包缺章：%s' % 缺)
    p = os.path.join(包目(b), '包.md')
    io.open(p, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    # 上册「已挂」限 ≤b 之笔（逐字·裁席当面裁之，⛔静静顺延）
    旧 = 限於(b)
    # ★1119（W907 判者②）前诸册之「已挂」而旧笔不及者（限 > 其下一册之至：下一册时未到限、再下一册又只读上一册——大审440 十一笔「限451」实证）
    #   照 诸挂(b) 补入（限非数者⛔入：其裁待人）；裁席照「大审V #号」逐笔当面裁
    末册 = (诸册() or [(None, None)])[-1][0]
    try:
        隙 = [x for x in 诸挂(b) if x['至'] != 末册 and x['限'] is not None]
    except Exception as e:                       # 诸挂析不得⛔崩包：照旧只出上册之笔，并印其由
        print('⚠ 诸挂析不得（%s）——旧笔只取上册' % str(e)[:80])
        隙 = []
    io.open(os.path.join(包目(b), '旧笔.md'), 'w', encoding='utf-8').write(
        '# 上册「已挂」限 ≤%d 之笔（%d 笔·逐字自上册三节）\n\n' % (b, len(旧)) + '\n\n'.join(
            '- %s 限%d｜%s' % (('前册之' + 号) if 号.lstrip('*').startswith('前册') else ('前册#' + 号), l, c) for 号, l, c in 旧) + '\n'
        + (('\n## 前诸册「已挂」而旧笔不及之笔（%d 笔·限 ≤%d·逐字自其册三节；裁时书「大审V #号」）\n\n' % (len(隙), b)
            + '\n\n'.join('- %s 限%d｜%s' % (号之名(x['至'], x['号']), x['限'], re.sub(r'\s+', ' ', x['裁'])) for x in 隙) + '\n') if 隙 else ''))
    print('★上册逾限之笔：%d 笔%s → %s' % (len(旧), ('；前诸册旧笔不及 %d 笔' % len(隙)) if 隙 else '',
                                     os.path.relpath(os.path.join(包目(b), '旧笔.md'), ROOT)))
    print('★大审之包：%s（%d 字）' % (os.path.relpath(p, ROOT), sum(len(x) for x in L)))
    print('★半用之器接入：包增 %dB、主环之出 %dB（合顶 %dB）%s' % (字节(旁), 字节(器事), 增顶,
                                                              ('；逾顶而省：' + '、'.join(省)) if 省 else ''))
    return p, 器事


def 连带(引):
    """★1023 X46：改一处先知其伤谁——引中「N:L」之原句取其≥6字之段，grep 全书正文他处同段 → 连带之单（零 token）。"""
    out = []
    for n, l in re.findall(r'(\d{1,3})[:：](\d+)', 引 or ''):
        p = 章档(int(n))
        if not p:
            continue
        ls = io.open(p, encoding='utf-8', errors='replace').read().split('\n')
        if not (0 < int(l) <= len(ls)):
            continue
        句 = ls[int(l) - 1]
        段 = [x for x in re.split(r'[，。；：？！、“”「」\s]+', 句) if len(x) >= 6][:3]
        for x in 段:
            hit = []
            for f in sorted(os.listdir(os.path.join(ROOT, '正文'))):
                fp = os.path.join(ROOT, '正文', f)
                for i, y in enumerate(io.open(fp, encoding='utf-8', errors='replace').read().split('\n'), 1):
                    if x in y and not (fp == p and i == int(l)):
                        m = re.search(r'第([零一二三四五六七八九十百]+)章', f)
                        hit.append('%s:%d' % (m.group(1) if m else f, i))
            if hit:
                out.append('%s:%s「%s」亦见 %s' % (n, l, x, '、'.join(hit[:8]) + ('…' if len(hit) > 8 else '')))
    return out


def 裁之文(x, b):
    """裁席之一行 → 册三节「裁」格之文。★1024 实踩（408—410 册）：裁席把还账之限写成 408（包之首章），录成「已挂·限408」，
    册一成即逾限、推闸全红——限⛔早於本册之下一章：≤b 者一律正为 b+1（还账本义即限下一章）。"""
    裁 = str(x.get('ruling', ''))
    限 = x.get('limit')
    try:
        限 = max(int(限), b + 1) if 限 not in (None, '') else None
    except (TypeError, ValueError):
        pass
    if 裁 == '已挂' and 限:
        裁 = '已挂·限%s' % 限
    elif 裁 == '还账':   # 已写章之读者可见致命：一单器施（还账.py），限下一章
        裁 = '已挂·限%s（还账·器施）' % (限 or b + 1)
    return 裁


拍库 = os.path.join(ROOT, '设定', '叫绝之拍库.md')


def 入库(裁果, a, b, 库=None):
    """★1027（执行之审 #99·法用#拍库随段）：裁席之 beats 录入拍库「## 第{a}段」之节（在「已定未写之标杆」之前；已有其节⛔重录），
    → 册之行；无 beats 者册写「本段无入库之拍：<由>」——裁席未交其由则书「未交」（⛔代填：421 起法用之守即红，主环面裁）。"""
    库 = 库 or 拍库
    bs = [x for x in (裁果.get('beats') or []) if isinstance(x, dict) and str(x.get('quote', '')).strip()]
    if not bs:
        由 = str(裁果.get('no_beats_reason') or '').strip()
        return ['本段无入库之拍：%s' % 由] if len(re.sub(r'\s', '', 由)) >= 4 else ['本段之拍入库：未交（裁席既无 beats、亦无四字以上之由）']
    行 = ['- %s%s「%s」——%s' % (x.get('ch', ''), (':' + str(x['beat'])) if x.get('beat') else '',
                               str(x['quote']).replace('\n', ' '), str(x.get('why', '')).replace('\n', ' ')) for x in bs]
    题 = '## 第%d段（%d—%d·大审入库）' % (a, a, b)
    try:
        文 = io.open(库, encoding='utf-8').read()
    except OSError:
        文 = ''
    if 题 not in 文:
        块 = '%s\n\n%s\n\n' % (题, '\n'.join(行))
        k = 文.find('## 已定未写之标杆')
        k = 文.rfind('---', 0, k) if k >= 0 else -1
        文 = (文[:k] + 块 + 文[k:]) if k >= 0 else (文.rstrip('\n') + '\n\n' + 块)
        io.open(库, 'w', encoding='utf-8').write(文)
    return ['入拍库 %d 拍（`设定/叫绝之拍库.md`「第%d段」）：' % (len(bs), a)] + 行


def 录(run, a=None, b=None):
    """★1023 X27：自 workflow 之 journal 排册之一、二节（逐席之判）与三节（裁席之裁）——⛔一席抄档（W50 录册一席 $20.96）。"""
    import glob
    import json
    js = glob.glob(os.path.expanduser('~/.claude/projects/*/*/subagents/workflows/%s/journal.jsonl' % run))
    if not js:
        raise SystemExit('⛔无此 run 之 journal：%s' % run)
    行 = []
    for l in io.open(js[0], encoding='utf-8', errors='replace'):
        try:
            行.append(json.loads(l))
        except ValueError:
            pass
    标 = {d.get('key'): d.get('label', '') for d in 行 if d.get('type') == 'started'}
    果 = {}
    for d in 行:
        if d.get('type') == 'result':
            r = d.get('result')
            if isinstance(r, str):
                try:
                    r = json.loads(r)
                except ValueError:
                    pass
            果[标.get(d.get('key'), '')] = r
    席果 = {k.split('·', 1)[1]: v for k, v in 果.items() if k.startswith('大审·')}
    裁果 = 果.get('裁') or {}
    if not b:
        b = int(裁果.get('to') or 0) or _末章()
    a = a or b - 每 + 1
    p = os.path.join(册目, '大审_至第%d章.md' % b)
    L = ['# 大审 · 至第%d章（第%d—%d章）\n' % (b, a, b),
         '> 瘦式（X51·裁_1021_省律 九）：零 token 先行（`设定/_草/大审%d/包.md` 甲）＋四席一裁；本册一、二、三节由 `大审.py --录 %s` 自 journal 排出，⛔一席抄档。\n' % (b, run),
         '> 律三：甲·独见｜乙·不强制出负，强制留痕｜丙·每笔落拍号或原句、逐笔落裁。\n',
         '## 一·本回之席（其名｜其独见｜其所读）\n', '| 席 | 其独见 | 所读 |', '|---|---|---|']
    for 名, 独 in 席表:
        r = 席果.get(名) if 名 != '裁' else 裁果
        读 = (r or {}).get('read', '未交') if isinstance(r, dict) else '未交'
        L.append('| %s | %s | %s |' % (名, 独, str(读).replace('|', '／').replace('\n', ' ')))
    L.append('\n## 二·逐席之判（乙律·留痕；丙律·落拍号）\n')
    for 名, _ in 席表[:-1]:
        r = 席果.get(名)
        L.append('### %s\n' % 名)
        if not isinstance(r, dict):
            L.append('未交。\n')
            continue
        fs = r.get('findings') or []
        if not fs:
            L.append('本席无致命之判：%s\n' % r.get('no_fatal_note', ''))
        for i, f in enumerate(fs, 1):
            L.append('%d. 〔%s〕%s:%s「%s」——%s｜拟治：%s' % (i, f.get('severity', ''), f.get('ch', ''), f.get('beat', ''),
                                                       str(f.get('quote', '')).replace('\n', ' '), f.get('issue', ''), f.get('fix', '')))
        if r.get('summary'):
            L.append('\n总：%s' % r['summary'])
        if r.get('hooks'):
            L.append('\n孤钩：' + '；'.join('%s→%s %s %s' % (h.get('id'), h.get('verdict'), h.get('chapter', ''), h.get('form', '')) for h in r['hooks']))
        L.append('')
    L += ['## 三·逐笔裁定（丙律·不许只挂）\n', '| # | 判（席·题） | 据（章·拍·原句） | 裁 | 其由 | 连带（器·X46） |', '|---|---|---|---|---|---|']
    for i, x in enumerate(裁果.get('rows') or [], 1):
        裁 = 裁之文(x, b)
        if x.get('to_segment'):
            裁 += '（入段案·%s）' % x['to_segment']
        带 = '；'.join(连带(x.get('evidence', ''))[:4]) if x.get('repay') else ''
        L.append('| %d | %s | %s | %s | %s | %s |' % (i, *(str(v).replace('|', '／').replace('\n', ' ') for v in (
            x.get('judgment', ''), x.get('evidence', ''), 裁, x.get('reason', ''), 带))))
    cs = 裁果.get('carried') or []
    if cs:
        L += ['\n### 上册逾限之笔·当面裁\n', '| 旧号 | 裁 | 其由 |', '|---|---|---|']
        for x in cs:
            裁 = str(x.get('ruling', ''))
            if '已挂' in 裁 and x.get('limit') and '限' not in 裁:
                裁 += '·限%s' % x['limit']
            L.append('| 前册#%s | %s | %s |' % (str(x.get('old_no', '')).replace('前册#', ''), 裁, str(x.get('reason', '')).replace('|', '／').replace('\n', ' ')))
    L += ['\n## 四·本回之数（器出，非估）\n', '见 `设定/_草/大审%d/包.md` 甲节（零 token 先行诸器之红）。\n' % b,
          '## 五·本回之得（一句话）\n', str(裁果.get('verdict_line', '〔裁席未交〕')) + '\n',
          '## 六·出口归造（入下一段之剧情庭题与段案）\n'] + ['- %s' % x for x in (裁果.get('to_next_segment') or [])]
    L += ['\n## 七·叫绝之拍入库（法用#拍库随段）\n'] + 入库(裁果, a, b)
    io.open(p, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('★大审之册已录：%s（席 %d、裁 %d 行、旧笔 %d）' % (os.path.relpath(p, ROOT), len(席果), len(裁果.get('rows') or []), len(cs)))
    return p


# ★W908 环8：计红之钉（纯判·⛔读盘）——大审470 包甲节之原行回放，并真红不漏。自测② 用之；--闸 跑整个 自测()（见下）。
_四七零 = [('悬念哨', '  ⛔ SUS-B-磨窝       末见第462章｜已隔 8 章（限 3）', True),
         ('悬念哨', '  ⛔**不许专开一拍去提、不许把它答死、不许用同一句式**；', False),
         ('悬念哨', '  ⛔**而「这一章没位子」不是由**：没位子即改挂到走得到的那一章，当场写明。', False),
         ('线限哨', '  ── ⛔本器只报不拦：改一笔账之限是一庭的事 ──', False),
         ('清偿章哨', '  ⚠CHAR-282A（其章 285）：了结而无清偿章｜**旧账·只报不拦**', True),
         ('清偿章哨', '  ⚠DEBT-297E（其章 307）：了结而无清偿章｜**旧账·只报不拦**', True),
         ('清偿章哨', '  ⚠CHAR-309A（其章 313）：了结而无清偿章｜**旧账·只报不拦**', True),
         ('清偿章哨', '  ⚠CHAR-317A（其章 319）：了结而无清偿章｜**旧账·只报不拦**', True)]
_真红 = ['  ⛔ 第461章 12.0%',                                              # 抄袭闸 --段
        '  ⛔ PLOT-301：限 470 ＝ 甲线，而本笔係 乙线——那一章碰它即破线。',   # 线限哨
        '  ⛔CHAR-470A（其章 470）：了结而无清偿章',                          # 清偿章哨之新账
        '  ⚠ SUS-B-磨窝      末见第462章｜已隔 8 章（逾 3·只报）']            # 悬念哨今式


def _钉():
    """→ 坏者之述（空即全过）。"""
    坏 = ['470包%s「%s」' % ('漏真红' if 期 else '误计', x.strip()[:16]) for _, x, 期 in _四七零 if 计红(x) != 期]
    坏 += ['漏真红「%s」' % x.strip()[:16] for x in _真红 if not 计红(x)]
    数 = {}
    for 名, x, _ in _四七零:
        数[名] = 数.get(名, 0) + 计红(x)
    if 数 != {'悬念哨': 1, '线限哨': 0, '清偿章哨': 4}:
        坏.append('470包之数 %s≠悬念哨 1、线限哨 0、清偿章哨 4' % 数)
    return 坏


def 自测(印=True):
    """→ 坏者之名（空即全过）。纯判＋tempdir（⑧⑬），⛔读真盘之态、⛔跑他器（⑬ 只起一空跑之 python3）。
    ★--闸 亦跑之（全测·大审闸、封版 --前）：W908 验——旧只钉计红，诸摘与限增、器事之分流无一闸跑之。"""
    import contextlib
    import shutil
    import tempfile
    R = []
    旧 = lambda x: bool(re.search(r'⛔|⚠|✗|红', x)) and '只报不拦' not in x[:6]
    旧数 = {}
    for 名, x, _ in _四七零:
        旧数[名] = 旧数.get(名, 0) + 旧(x)
    R.append(('①旧式回放 470 包：悬念哨 3、线限哨 1、清偿章哨 4（误计之证）',
              旧数 == {'悬念哨': 3, '线限哨': 1, '清偿章哨': 4}))
    R.append(('②新式：悬念哨 1、线限哨 0、清偿章哨 4；真红（第N章、账号、限 N、⚠）⛔漏', not _钉()))
    o = ('════ 外声闸 · 只报不拦 ════\n  章      出声句      出声字      别人问他      \n'
         '  9      1        3        0          剩一站。\n  10     0        0        0          \n'
         '  11     0        0        0          \n  12     2        6        1          「还有几站？」｜明早。\n'
         '  13     0        0        0          \n  ── 末尾连续出声为零：1 章 ──\n  ✓ 未逾五章。\n'
         '     1—99章 2933｜100—199章 2473\n')
    外 = 外声之摘(o, 10, 13)
    R.append(('③外声之摘：只取 a—b（2 句 6 字、最长连零 2、引 12「还有几站？」）',
              len(外) == 1 and '出声 2 句 6 字' in 外[0] and '最长连零 2 章' in 外[0] and '12「还有几站？」' in 外[0]
              and '剩一站' not in 外[0]))
    印们 = {10: '■ 2026-11-19 11:46｜aaa1111｜治章-12 推闸（改单#X）\n   · 正文/书_第十章_甲.md　+1／−1　行：15\n'
                '■ 2026-11-19 05:43｜bbb2222｜大审 1—10 还账\n   · 版本/第10章/v02.md　+9／−0　行：1—9\n'
                '   · 正文/书_第十章_甲.md　+2／−2　行：15、59\n'
                '■ 2026-11-19 04:54｜ccc3333｜第10章《甲》封版（造式二代）\n   · 正文/书_第十章_甲.md　+157／−0　行：1—157\n'
                '■ 2026-11-19 01:59｜ddd4444｜开第10章：方案\n   · 版本/第10章/_料.md　+325／−0　行：1—325\n',
           9: '■ 2026-11-19 05:43｜bbb2222｜大审 1—10 还账\n   · 正文/书_第九章_乙.md　+1／−1　行：25\n'
              '■ 2026-11-18 05:43｜eee5555｜第9章《乙》封版（造式二代）\n   · 正文/书_第九章_乙.md　+2／−2　行：127、131\n'
              '■ 2026-11-18 05:22｜fff6666｜第9章《乙》稿（存底·封版前）\n   · 正文/书_第九章_乙.md　+147／−0　行：1—147\n',
           8: '■ 2026-11-17 09:00｜ggg7777｜还账 8\n   · 正文/书_第八章_丙.md　+1／−1　行：3\n'
              '■ 2026-11-17 05:00｜hhh8888｜旧式之成\n   · 正文/书_第八章_丙.md　+99／−0　行：1—99\n'}
    改 = '\n'.join(改记之摘(印们))
    R.append(('④改记之摘：封後之笔同提交并一行（bbb2222→9:25｜10:15、59），封版及其前、版本之档⛔录；无封版者以正文之成为界',
              '3 笔' in 改 and 'bbb2222' in 改 and '9:25｜10:15、59' in 改 and 'aaa1111' in 改 and '8:3' in 改
              and not any(k in 改 for k in ('ccc3333', 'eee5555', 'fff6666', 'hhh8888', '1—9'))))
    R.append(('⑤改记之摘：无封後之改即一行', 改记之摘({7: '■ 2026-11-17 05:00｜iii9999｜第7章《丁》封版\n   · 正文/书_第七章_丁.md　+9／−0　行：1—9\n'})
              == ['- **改记**：封後正文无改。']))
    甲窗, 乙窗 = '甲.py ‖ [' + '^。]{0,8} ‖ #1', '乙.py ‖ [' + '^x]{0,6} ‖ #1'   # ⛔写死其形：窗界哨扫本档即认作真窗（当场拼出）
    rows = [('甲.py', 10, '。', 8, '换行', 甲窗), ('乙.py', 20, 'x', 6, '。＋换行', 乙窗)]
    窗 = 窗界之摘(rows, '| ✅ 判对 | `%s` | 只在一行 |\n' % 甲窗)
    R.append(('⑥窗界之摘：以 窗界哨.对档 判，答过者⛔列、未答者列其名与行', '答过 1、未答 1' in 窗[0] and len(窗) == 2
              and '乙.py' in 窗[1] and '行20' in 窗[1]))
    旗 = 处方旗之摘('════ 处方旗哨 ════\n  处方里点名之旗 7 处｜⛔其器一字未提者 1 处\n  ⛔ 工具/甲器.py 之 --假旗 ← 见於 设定/令.md\n')
    R.append(('⑦处方旗之摘：总数之行（带⛔）⛔计红，真红列之；全绿一行',
              旗[0].endswith('红 1 行（旗不认即照默认路走）') and len(旗) == 2 and '--假旗' in 旗[1]
              and 处方旗之摘('  处方里点名之旗 7 处｜⛔其器一字未提者 0 处\n  ✓ 处方里点名的旗，器器皆认得。\n')
              == ['- **处方旗哨**：✓（处方之旗 7 处，器俱认）']))
    tmp = tempfile.mkdtemp(prefix='大审自测_')
    try:
        os.makedirs(os.path.join(tmp, '版本', '第10章'))
        io.open(os.path.join(tmp, '版本', '第10章', '_器之迹.md'), 'w', encoding='utf-8').write(
            '# 器之迹·第10章\n\n| 器 | 跑 | 败 | 总秒 | 最长 | 重跑 | 败例 |\n|---|---|---|---|---|---|---|\n'
            '| 甲闸.py | 5 | 4 | 1.0 | 0.5 | （无参） ×3 | 01:00  rc=1；01:02  rc=1 |\n'
            '| 乙器.py | 3 | 1 | 0.1 | 0.1 |  | 02:00 --help rc=exc:BrokenPipeError |\n'
            '| 丙器.py | 9 | 0 | 0.1 | 0.1 |  |  |\n')
        迹 = '\n'.join(器之迹之摘(9, 10, tmp))
        R.append(('⑧器之迹之摘：只取 rc≠0 之行（败 0 者⛔录），exc 尽列，缺迹之章列之',
                  '器 2、败 5' in 迹 and '甲闸 4/5（1 章）' in 迹 and 'BrokenPipeError（乙器）' in 迹
                  and '丙器' not in 迹 and '缺迹：9' in 迹))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    大 = ['- 行' + '字' * 60] * 40
    块们, 省 = 限增([('高', ['- 高'], 'x'), ('中', 大, 'y'), ('低', 大, 'z')], 3072)
    R.append(('⑨限增：逾 3KB 即自价最低者删、代以一行之指；价高者留',
              省 == ['低', '中'] and 块们[0][1] == ['- 高'] and '逾增之顶' in 块们[2][1][0]
              and sum(len(('\n'.join(x[1]) + '\n').encode('utf-8')) for x in 块们) <= 3072))
    块们, 省 = 限增([('高', ['- 高'], 'x'), ('低', ['- 低'], 'z')], 3072)
    R.append(('⑩限增：未逾顶即一字不删', 省 == [] and 块们[1][1] == ['- 低']))
    旁, 器事, 省 = 排(['- 外'], ['- 改'], ['- 窗'], ['- 旗'], ['- 迹'])
    R.append(('⑪排：外声、改记入包；窗界、处方旗、器之迹只印主环（器之迹居末）', 旁 == ['- 外', '- 改']
              and 器事 == ['- 窗', '- 旗', '- 迹'] and 省 == []))
    块 = 主环之块(器事, '════ 囤灰闸 --普查 ════\n  候修 1\n    · 甲 —— 败多\n').split('\n')
    R.append(('⑫主环之块：器之事与普查同块，器之迹（本段）紧接普查之「候修」（全史）',
              块[0].startswith('── 主环·') and 块[1:4] == ['- 窗', '- 旗', '- 迹'] and 块[4].startswith('════ 囤灰闸')
              and 块[5] == '  候修 1' and 主环之块([], '').endswith('（普查无出）')))
    # ⑭〔执行之制·治15〕普查必裁：入档、重跑留判只添新候、连两段无判即标（回灌 470 之普查无判 → 480 之节标之）
    _普 = '════ 囤灰闸 --普查 ════\n  候修 2\n    · 记落.py —— 410 rc=2\n    · 甲.py —— 慢\n  候退 1\n    · 乙.py —— 唯自测\n  档之囤灰 0\n'
    _候 = 普查之候(_普)
    _f1 = 普查之节('', 461, 470, _候)
    _f2 = _f1.replace('- 候修 · 记落.py —— 410 rc=2｜判：', '- 候修 · 记落.py —— 410 rc=2｜判：假候：自测故意期望 rc 2')
    _f3 = 普查之节(_f2, 461, 470, _候 + [('档之囤灰', '设定/丙.md', '无引')])
    _f4 = 普查之节(_f3, 471, 480, _候)
    R.append(('⑭普查之节：入档每候一行带「｜判：」；重跑本段留已书之判、只添新候；下段之节於前段无判而又见之候标「（前段亦无判）」，已判者⛔标',
              _候 == [('候修', '记落.py', '410 rc=2'), ('候修', '甲.py', '慢'), ('候退', '乙.py', '唯自测')]
              and _f1.count('｜判：\n') == 3 and '## 461—470（段末普查·候 3·判 0）' in _f1
              and '判：假候：自测故意期望 rc 2' in _f3 and '设定/丙.md' in _f3 and '候 4·判 1' in _f3
              and '- 候修 · 甲.py —— 慢（前段亦无判）｜判：' in _f4 and '记落.py —— 410 rc=2｜判：' in _f4
              and '记落.py —— 410 rc=2（前段亦无判）' not in _f4 and _f4.index('## 461—470') < _f4.index('## 471—480')))
    g, 旧g = globals(), {}
    tmp = tempfile.mkdtemp(prefix='大审自测包_')
    try:                                                    # ⑬ 包() 之实写：桩其诸源，看 包.md 与其回
        for k, v in (('ROOT', tmp), ('零先之器', []), ('接入', lambda a, b: (['- 旁证之桩'], ['- 器事之桩'], [])),
                     ('章档', lambda n: os.path.join(tmp, '正文', '书_桩.md')), ('白文', lambda n: '1\t桩'),
                     ('限於', lambda n: [])):
            旧g[k] = g[k]
            g[k] = v
        with contextlib.redirect_stdout(io.StringIO()):
            回 = 包(1, 1)
        文 = io.open(os.path.join(tmp, '设定', '_草', '大审1', '包.md'), encoding='utf-8').read()
        R.append(('⑬包()：旁证入 包.md，器之事⛔入（1027 之裁·四席⛔读）而回给 --包 印主环',
                  '旁证之桩' in 文 and '器事之桩' not in 文 and 回[1] == ['- 器事之桩']))
    except (Exception, SystemExit) as e:
        R.append(('⑬包()之实写：跑不成（%s）' % str(e)[:60], False))
    finally:
        g.update(旧g)
        shutil.rmtree(tmp, ignore_errors=True)
    if 印:
        for 名, ok in R:
            print(('  ✓ ' if ok else '  ⛔ ') + 名)
        print('大审·自测 %d/%d' % (sum(1 for _, ok in R if ok), len(R)))
    return [名 for 名, ok in R if not ok]


def 普查入档(a, b, 普):
    try:
        n, 未, 连 = 写普查(a, b, 普)
        print('%s 囤灰普查入档：%s 之「## %d—%d」候 %d、未判 %d%s——总编辑当段逐候书「删／修／留：由」或「假候：由」（执行之制·治15）'
              % ('⛔' if 连 else ('⚠' if 未 else '✓'), 普查档, a, b, n, 未, '、连两段无判 %d（下段首验即红）' % 连 if 连 else ''))
    except Exception as e:
        print('⚠ 囤灰普查入档不成：%s' % e)


if __name__ == '__main__':
    if '--自测' in sys.argv:
        raise SystemExit(1 if 自测() else 0)
    if '--限' in sys.argv:                 # 开镜卡问七：python3 工具/大审.py --限 N → 上一册「已挂」限 ≤N 之笔
        n = int(sys.argv[sys.argv.index('--限') + 1])
        r = 限於(n)
        print('── 大审「已挂」限 ≤%d 之笔（开镜卡问七须逐笔抄上；到其限须裁：已治／改限带由）──' % n)
        for 号, l, c in r:
            print('  #%s 限%d｜%s' % (号, l, c))
        print('  （零笔）' if not r else '  共 %d 笔' % len(r))
        raise SystemExit(0)
    if '--包' in sys.argv:
        i = sys.argv.index('--包')
        _, 器事 = 包(int(sys.argv[i + 1]), int(sys.argv[i + 2]))
        # ★1027（执行之审 #55 #103·线 D 之遗）：段末一回之囤灰普查——只印主环（⛔入包：四席⛔读器之事），候退、档之囤灰由总编辑当段裁（删、修或留由）
        # ★W908 环8：器之事（窗界哨之未答、处方旗哨、本段器之迹）同印此块（主环之块），⛔入包
        import subprocess
        try:
            r = subprocess.run(['python3', os.path.join(ROOT, '工具', '囤灰闸.py'), '--普查'], cwd=ROOT, capture_output=True, text=True, timeout=120)
            普 = r.stdout or r.stderr or '（无出）'
        except Exception as e:
            普 = '⚠ 囤灰普查跑不成：%s' % e
        print(主环之块(器事, 普))
        普查入档(int(sys.argv[i + 1]), int(sys.argv[i + 2]), 普)
        raise SystemExit(0)
    if '--普查' in sys.argv:              # 〔执行之制·治15〕补写本段之节（段末 --包 已跑而节未立者）：python3 工具/大审.py --普查 471 480
        i = sys.argv.index('--普查')
        import subprocess
        r = subprocess.run(['python3', os.path.join(ROOT, '工具', '囤灰闸.py'), '--普查'], cwd=ROOT, capture_output=True, text=True, timeout=120)
        print(r.stdout or r.stderr)
        普查入档(int(sys.argv[i + 1]), int(sys.argv[i + 2]), r.stdout or '')
        raise SystemExit(0)
    if '--录' in sys.argv:
        录(sys.argv[sys.argv.index('--录') + 1])
        raise SystemExit(0)
    if '--立' in sys.argv:
        raise SystemExit(0 if 立(int(sys.argv[sys.argv.index('--立') + 1])) else 2)
    判 = 印('--闸' in sys.argv)
    坏 = 自测(印=False) if '--闸' in sys.argv else []      # ★W908 环8：整个自测随闸（纯判＋tempdir，约 0.1 秒），坏即器红
    for x in 坏:
        print('  ⛔ 大审·自测坏（器之事·⛔关本章；器红账限三章治 工具/大审.py）：%s——--自测 详之' % x[:60])
    raise SystemExit(1 if 判 or 坏 else 0)
