# -*- coding: utf-8 -*-
"""棘轮预检 · 2026-09-01 立（LAW-289C·令§十一机化）
　病：改文之後直接 --存版，棘轮闸事後才报回退，遂须 --补存 补一版。
　　　289 第5轮（补身撞「是哪一样」）、第6轮（承前撞「馊压过甜」）连犯二回。
　法：**不另造一把尺**——直接 import 跑轮.score 与其 RATCHET_MIN/MAX，
　　　读同一份 _台账.json 算同一个「历来最优」；
　　　★故此器所报，与 --存版 之棘轮闸逐字同源，不会出现「预检绿而存版红」。
　用：python3 工具/棘轮预检.py N      ← 落盘之後、--存版 之前跑
　　　rc=0 放行｜rc=1 会回退｜rc=2 无此章
〔1119 死规之审·gates21〕RATCHET_MAX（嗅／沈鸢不降）与 RATCHET_V01（四感不低於起草）之退 → 入 drift（⚠·只报），⛔入 worse（⛔·rc 1）：
　其係改稿之内容底线，只逼补偿之笔（跑轮:244-249·289）；沈鸢之名之棘轮更与暗线称谓之约相抵。RATCHET_MIN（四字串三现、顿悟起手）防复防癖，照旧硬。
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import io, os, re, sys, json, glob

根 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(根, '工具'))
from 跑轮 import score, body_of, RATCHET_MIN, RATCHET_MAX, RATCHET_V01  # noqa: E402

CN = {'零':0,'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9}


def _号(s):
    m = re.search(r'第([零一二三四五六七八九十百]+)章', s)
    if not m:
        return None
    t = m.group(1)
    if t.startswith('十'):
        t = '一' + t
    n = cur = 0
    for ch in t:
        if ch == '百':
            n += (cur or 1) * 100; cur = 0
        elif ch == '十':
            n += (cur or 1) * 10; cur = 0
        else:
            cur = CN[ch]
    return n + cur


def 正文路径(n):
    for p in sorted(glob.glob(os.path.join(根, '正文', '*.md'))):
        if _号(os.path.basename(p)) == n:
            return p
    return None


def 起草版(n):
    """台账首个有 soft 之版——RATCHET_V01 之底（2026-09-02立）。"""
    f = os.path.join(根, '版本', '第%d章' % n, '_台账.json')
    if not os.path.exists(f):
        return {}
    for r in json.load(io.open(f, encoding='utf-8')).get('版本', []):
        sf = r.get('soft') or {}
        if sf:
            return sf
    return {}


def 末版(n):
    """台账里最後一个有 soft 的版——★2026-09-05 立·丙㉑之治。
    ★其立之由（拿账说）：原式只有「历来最优」一个底，而那个底取的是 min／max **跨全部版本**，
    ★★而 四字串三现／顿悟起手 都是**绝对计数**，随净重长；台账里第一版总是最短的那一版，
    ★★★遂使「历来最优」永远等於「起草那一版」。实测：有台账之章 193，旧式判红 158（82%）。
    ★★★★一道在成书上红八成的闸，拦不住任何东西——它只是每次都喊。
    　故改：**⛔ 只对末版**（这一笔是不是我刚才写坏的），历来最优降为 ⚠（累计漂移，供人判）。
    ★★2026-09-05 再改·同一处第二病：**台账里记的数是存版当天那把尺量的**，
    　而此器拿今天这把尺量当前正文——两把尺比一个数。实测（见 --自测②）：
    　有末版档之章 193，台账所记与今日之尺重算不符者 31 章（16%），全在「顿悟起手」一项上。
    　故末版之数**不读台账，改自 版本/第N章/v*.md 末档当场重算**：同一把尺，两边才比得。
    　台账只在末档不存时兜底（并在印出时标明其数出自台账）。"""
    vs = sorted(glob.glob(os.path.join(根, '版本', '第%d章' % n, 'v*.md')))
    if vs:
        _h, sf = score(io.open(vs[-1], encoding='utf-8').read())
        return sf, os.path.basename(vs[-1])[:-3]
    f = os.path.join(根, '版本', '第%d章' % n, '_台账.json')
    if not os.path.exists(f):
        return {}, None
    led = json.load(io.open(f, encoding='utf-8'))
    for r in reversed(led.get('版本', [])):
        sf = r.get('soft') or {}
        if sf:
            return sf, (r.get('版') or '?') + '·台账'
    return {}, None


def 最优(n):
    """与跑轮存版处逐行同式：只认台账里已记之 soft，缺键者不参与。"""
    f = os.path.join(根, '版本', '第%d章' % n, '_台账.json')
    if not os.path.exists(f):
        return {}
    led = json.load(io.open(f, encoding='utf-8'))
    best = {}
    for r in led.get('版本', []):
        sf = r.get('soft') or {}
        for k in RATCHET_MIN:
            if k in sf:
                best[k] = min(best.get(k, sf[k]), sf[k])
        for k in RATCHET_MAX:
            if k in sf:
                best[k] = max(best.get(k, sf[k]), sf[k])
        if '净重' in sf:
            best['净重'] = max(best.get('净重', sf['净重']), sf['净重'])
    return best


def 三现串(txt):
    b = body_of(txt)
    seen = {}
    for i in range(len(b) - 3):
        k = b[i:i + 4]
        if re.match(r'^[一-龥]{4}$', k):
            seen[k] = seen.get(k, 0) + 1
    return {k for k, v in seen.items() if v >= 3}


_感式 = {'嗅': r'味|气味|鼻|闻', '听': r'听|响|声|叫|吠',
        '触': r'凉|温|烫|硬|软|摸|按|贴', '视': r'灯|光|看|眼|见'}


def _四感删证(n, txt, 项):
    """★★★★★2026-09-05·305第8、9两轮所立（欠-305A之治·§十一③机化）。
    ★其红在哪一行（二组数·§六①）：
      · **305第8轮**：删拍71（「昨天那个十一是针听的…」——一处转述），器报「听 14→13」；
      · **305第9轮**：紧拍72（「一把说硬，一把说一响」——同一对尺之三陈），器报「听／触」又降。
      ★★二回所减者俱非一次真的感觉，是一句转述**；而器只印「听 14→13」，
        不印那一句是什么——**於是「所减者是不是一次真感觉」这一问，全靠人自己记得去问。**
    ★★★故此块只做一件事：**把「本轮删掉而含此感之字」的句子逐句摆出来**，判仍归人。
    ★★★★它认哪几样（§六④）：**四感四项，本书同类共四样**（嗅／听／触／视，与 RATCHET_V01 同源）；
      ★它认不着的两样：①改写而非整句删者（其残句仍在，不入此表）；②**「那一句算不算一次真感觉」——那一判器不下，人下。**"""
    vs = sorted(glob.glob(os.path.join(根, '版本', '第%d章' % n, 'v*.md')))
    if not vs:
        return []
    旧 = body_of(io.open(vs[-1], encoding='utf-8').read())
    新 = body_of(txt)
    切 = lambda t: [x for x in re.split(r'[。！？\n]', t) if x.strip()]
    有 = set(切(新))
    式 = _感式.get(项)
    if not 式:
        return []
    return [x.strip() for x in 切(旧)
            if x.strip() and x not in 有 and re.search(式, x)]


def _拆出章(n):
    """本章有没有一个「自它拆出」的章（施工表 M 行自注「（N拆出）」）。
    ★立此一问之由（2026-09-05·丙㉑之三）：RATCHET_V01 之「不得低於起草」比的是绝对句数，
    ★★而拆过章的源章，其感官之句并没有被抽掉——它们搬到隔壁那一章去了。
    ★★★故此处不豁免整章，只豁免**查得实的那一部分**：把「本轮删去而含此感之句」逐句拿到
    　　　拆出之章的正文里找，找得着的才算「搬走了」。找不着的照旧算回退。"""
    f = os.path.join(根, '设定', '01_镇冢秘术_逐章施工与伏笔回收表.md')
    if not os.path.exists(f):
        return None
    for ln in io.open(f, encoding='utf-8'):
        m = re.match(r'\|\s*(\d+)\s*\|', ln)
        m2 = re.search(r'（(\d+)拆出）', ln)
        if m and m2 and int(m2.group(1)) == n:
            return int(m.group(1))
    return None


def _搬走几句(n, 句):
    """那些删去的句，有几句能在「自本章拆出」的那一章正文里找着。"""
    m = _拆出章(n)
    if not m or not 句:
        return 0, 0, m
    p = 正文路径(m)
    if not p:
        return 0, len(句), m
    体 = body_of(io.open(p, encoding='utf-8').read())
    体 = re.sub(r'[\s「」“”‘’（）()【】：:；;，,。．、？！?!*★·—…]', '', 体)
    n有 = 0
    for x in 句:
        g = re.sub(r'[\s「」“”‘’（）()【】：:；;，,。．、？！?!*★·—…]', '', x)
        if len(g) >= 6 and g[:12] in 体:
            n有 += 1
    return n有, len(句), m


def _末版係拆章前(n, 档=None):
    """末档是不是「拆章以前」的那一版——是则它与当前正文根本不是同一段文，逐项比无意义。
    ★其判（不猜，去盘上数）：本章若有一个自它拆出的章 m，
    　把末档正文切句，数其中有多少句**今天已不在本章、却在第 m 章正文里**。
    　≥8 句即判「末档係拆章前之版」（111 之 v11 数得 40 余句）。
    ★★判成之後，与末版比的那些回退一律降作 ⚠ 并写明其由：句没有少，是搬到隔壁去了。"""
    m = _拆出章(n)
    if not m:
        return 0, None
    vs = sorted(glob.glob(os.path.join(根, '版本', '第%d章' % n, 'v*.md')))
    p2, p3 = 正文路径(n), 正文路径(m)
    if not vs or not p2 or not p3:
        return 0, None
    剥 = lambda t: re.sub(r'[\s「」“”‘’（）()【】：:；;，,。．、？！?!*★·—…]', '', t)
    切 = lambda t: [x for x in re.split(r'[。！？\n]', body_of(t)) if len(剥(x)) >= 8]
    本 = 剥(body_of(io.open(p2, encoding='utf-8').read()))
    邻 = 剥(body_of(io.open(p3, encoding='utf-8').read()))
    n搬 = 0
    for x in 切(io.open(档 or vs[-1], encoding='utf-8').read()):
        g = 剥(x)
        if g[:12] not in 本 and g[:12] in 邻:
            n搬 += 1
    return n搬, m


def 跑(n, 报=True):
    """★2026-09-05 改（丙㉑之治）：⛔ 之底由「历来最优」改为「末版」，历来最优降为 ⚠。

    ★改之由，拿账说：
      · 四字串三现／顿悟起手 都是**绝对计数**，随净重长；台账里第一版总是最短的那一版，
        故「历来最优＝min 跨全部版本」永远等於「起草那一版之数」。
      · 实测（`python3 工具/棘轮预检.py --全书`）：有台账之章 193，
        旧式（vs 历来最优）判红 158 章 82%；改密度亦无救（162 章 84%）；
        新式（vs 末版）判红 39 章 20%，且所红者尽是末版之後本坐动过手的章。
      · 一道在成书上红八成的闸，拦不住任何东西——它只是每次都喊。而 --存版 那一头本来就只 ⚠ 不拦，
        是此器把同一个数印成了 ⛔ 与「处方：先改回」，那句话在一件已封版的章上不可执行。
    ★所以新式问的是那个答得出的问题：**我刚才这一笔，把这一章写坏了吗**（当前 vs 末版）；
      而「累计漂移」（当前 vs 历来最优）照印，只是降作 ⚠，并把那个最优版的净重一并印出来，
      让人一眼看得出它是不是长短之故。
    ★★§六④ 它认哪几样：RATCHET_MIN 二样（四字串三现·顿悟起手）、RATCHET_MAX 二样（嗅·沈鸢）、
      RATCHET_V01 四样（嗅听触视·不得低於起草）——本书同类之尺共八样，此器认全八样，未新造一把。
    """
    p = 正文路径(n)
    if not p:
        if 报:
            print('⛔ 第%d章之正文不在' % n)
        return 2
    txt = io.open(p, encoding='utf-8').read()
    _hard, soft = score(txt)
    末, 末号 = 末版(n)
    best = 最优(n)
    n搬, 邻章 = _末版係拆章前(n)
    末前拆 = n搬 >= 8
    worse = []          # ⛔：与末版比之回退（这一笔写坏的）
    drift = []          # ⚠：与历来最优比之漂移（累计，可为长短之故）
    拆退 = []           # ⚠：末档係拆章前之版，逐项比无意义
    for k in RATCHET_MIN:
        if k in 末 and soft[k] > 末[k]:
            (拆退 if 末前拆 else worse).append((k, 末[k], soft[k], '升'))
        elif k in best and soft[k] > best[k]:
            drift.append((k, best[k], soft[k], '升'))
    for k in RATCHET_MAX:
        if k in 末 and soft[k] < 末[k]:
            # 〔1119 死规之审·gates21〕嗅／沈鸢之降（对末版）入 drift（⚠），⛔入 worse：内容之底只逼补偿之笔（289）
            (拆退 if 末前拆 else drift).append((k, 末[k], soft[k], '降·对末版'))
        elif k in best and soft[k] < best[k]:
            drift.append((k, best[k], soft[k], '降'))
    v01 = 起草版(n)
    搬 = []
    for k in RATCHET_V01:
        if k in v01 and k in soft and soft[k] < v01[k]:
            句 = _四感删证(n, txt, k)
            有, 共, m = _搬走几句(n, 句)
            if m and 共 and 有 * 2 >= 共:
                搬.append((k, v01[k], soft[k], 有, 共, m))
            else:
                drift.append((k, v01[k], soft[k], '低於起草'))   # 〔1119 死规之审·gates21〕四感低於起草入 drift（⚠），⛔入 worse
    if 报:
        print('════ 棘轮预检 · 第%d章 ════' % n)
        if not 末 and not best:
            print('  ℹ 台账无版可比（新章），棘轮无底，放行。')
            return 0
        if 末:
            print('  末版（%s·净重 %s）：' % (末号 or '?', 末.get('净重', '?'))
                  + '｜'.join('%s %s' % (k, 末[k]) for k in sorted(末) if k != '净重'))
        print('  当前正文（净重 %s）：' % soft.get('净重')
              + '｜'.join('%s %s' % (k, soft[k]) for k in sorted(末 or best) if k != '净重'))
        if soft.get('嗅') == 0:
            # ★2026-09-05·机制总审（八路·覆盖之缺审第11条·P35 嗅零复发3）：无一闸在嗅==0时出声；今此处出一声（报而不拦）。
            print('  ⚠ 嗅零（P35·复发3）：本章嗅之密度为零——起草只顾一样感官；159/160/161 三章连零之旧病。')
        for k, a, b, d in 拆退:
            print('  ⚠ %s %d→%d(%s)——**末档係拆章前之版**：末档里有 %d 句今天不在本章而在第%d章'
                  '（第%d章係自本章拆出），两边不是同一段文，逐项比无意义，不拦。'
                  % (k, a, b, d, n搬, 邻章, 邻章))
        for k, a, b, 有, 共, m in 搬:
            print('  ⚠ %s %d→%d(低於起草)——**其降係拆章**：本轮删去而含「%s」之句 %d 条里，'
                  '有 %d 条在第%d章正文里（第%d章係自本章拆出）。句没有少，只是搬到隔壁去了，不拦。'
                  % (k, a, b, k, 共, 有, m, m))
        for k, a, b, d in drift:
            if d in ('降·对末版', '低於起草'):
                # 〔1119 死规之审·gates21〕内容之底（嗅／沈鸢／四感）之退只印 ⚠ 並其删证；判其降伤不伤文，归人（此行⛔带「⛔」字：起草闸.红行 见⛔即红）
                句 = _四感删证(n, txt, k) if k in _感式 else []
                print('  ⚠ 内容之底（只报·〔1119·gates21〕）：%s %d→%d(%s)%s——判其降伤不伤文归人；勿为补数而补字'
                      % (k, a, b, d, ('｜本轮删去而含「%s」之句 %d 条：' % (k, len(句))
                                      + '｜'.join('「%s」' % x[:34] for x in 句[:3])) if 句 else ''))
                continue
            print('  ⚠ 漂移（对历来最优·非本笔之责）：%s %d→%d(%s)　★历来最优之净重 %s，当前 %s——'
                  '两版长短不同则绝对计数本不可比，此行只作参考，不拦。'
                  % (k, a, b, d, best.get('净重', '?'), soft.get('净重', '?')))
        if not worse:
            print('  ✓ 与末版比无回退；此刻存版，棘轮不会报回退。')
            if any(d in ('降·对末版', '低於起草') for _k, _a, _b, d in drift):
                # 〔1119 死规之审·gates21〕✓ 只及 RATCHET_MIN（防复防癖）；上列内容之底之 ⚠ 照旧在，只报不拦
                print('    （此 ✓ 只及 %s；上列「内容之底」之 ⚠ 只报不拦。）' % '／'.join(RATCHET_MIN))
            if 末前拆:
                print('    （末档係拆章前之版，故上列诸项只作参考。本章之棘轮须待下一次存版方能重立底。）')
        for k, a, b, d in worse:
            extra = ''
            if k in _感式:
                句 = _四感删证(n, txt, k)
                if 句:
                    extra = ('｜本轮删去而含「%s」之句 %d 条：' % (k, len(句))
                             + '｜'.join('「%s」' % x[:34] for x in 句[:3]))
                    if len(句) > 3:
                        extra += '｜…'
                else:
                    extra = '｜本轮无整句删去而含此感者——**故其降係改写所致，须逐处自看**'
            if k == '四字串三现':
                vs = sorted(glob.glob(os.path.join(根, '版本', '第%d章' % n, 'v*.md')))
                if vs:
                    新 = 三现串(txt) - 三现串(io.open(vs[-1], encoding='utf-8').read())
                    if 新:
                        extra = '｜所增之串：' + '、'.join(sorted(新))
                    else:
                        extra = '｜与末版之档比指不出新串——**须逐处自看**'
            print('  ⛔ %s %d→%d(%s)%s' % (k, a, b, d, extra))
        if worse:
            print('  处方：先改回再 --存版。')
            print('  ★而其常犯之形有二：①补身之字落在旧物上，旧物之名已在章中（289第5轮）；')
            print('    ②承前之句引原场之词，而那词本章已用过两回（289第6轮）。')
    return 1 if worse else 0


def 全书(报=True, 止=None):
    """把新旧两式在全书上各跑一遍，把两个数并排印出来——§一⑥：数旁边要有印它的命令。
    止：只算章号 ＜止 之章（自测①用 旧式之窗——见 自测）。"""
    ns = []
    for f in sorted(glob.glob(os.path.join(根, '版本', '第*章', '_台账.json'))):
        m = re.search(r'第(\d+)章', f)
        if m and (止 is None or int(m.group(1)) < 止):
            ns.append(int(m.group(1)))
    有 = 新红 = 旧红 = 0
    新单 = []
    for n in ns:
        p = 正文路径(n)
        if not p:
            continue
        末, _ = 末版(n)
        best = 最优(n)
        if not 末 and not best:
            continue
        有 += 1
        _h, soft = score(io.open(p, encoding='utf-8').read())
        n搬, _邻 = _末版係拆章前(n)
        if n搬 < 8 and any(k in 末 and soft[k] > 末[k] for k in RATCHET_MIN):   # 〔1119 死规之审·gates21〕新式之⛔只数 RATCHET_MIN（MAX 之降今只 ⚠）
            新红 += 1
            新单.append(n)
        if (any(k in best and soft[k] > best[k] for k in RATCHET_MIN)
                or any(k in best and soft[k] < best[k] for k in RATCHET_MAX)):
            旧红 += 1
    if 报:
        print('════ 棘轮预检 · 全书 ════')
        print('  有台账之章 %d' % 有)
        print('  旧式（⛔对历来最优）判红 %d 章（%.0f%%）' % (旧红, 100.0 * 旧红 / max(1, 有)))
        print('  新式（⛔对末版）　判红 %d 章（%.0f%%）' % (新红, 100.0 * 新红 / max(1, 有)))
        print('  新式所红：' + '、'.join(str(x) for x in 新单))
    return 有, 旧红, 新红, 新单


旧式之窗 = 306   # 与自测②同窗（range(200, 306)）


def 自测():
    R = []
    # 〔489·器红逾限之治〕①所证係史：旧式（对历来最优）在其所行之窗（＜306，与②同窗·本器 0901 立时之局）红过半。
    #   旧以全书为分母——此後之章俱照新式写、旧式几不红（306—489 之 184 章旧红 27），分母年年涨而①自 485 转假红。
    #   ⛔删此格、⛔降其界：窗内之数照旧当场算（今 198 章旧红 162），新式之⛔於全书照旧由 --全书 印、③⑤ 照验。
    有, 旧红, 新红, 新单 = 全书(报=False, 止=旧式之窗)
    R.append(('①旧式之窗（＜%d）旧式红过半而新式不过半（旧 %d／新 %d／共 %d）' % (旧式之窗, 旧红, 新红, 有),
              旧红 > 有 * 0.5 and 新红 < 有 * 0.5))
    # ②未动过手之章（当前与末版之档逐字同）须绿
    绿 = None
    for n in range(200, 306):
        vs = sorted(glob.glob(os.path.join(根, '版本', '第%d章' % n, 'v*.md')))
        p = 正文路径(n)
        if not vs or not p:
            continue
        if body_of(io.open(vs[-1], encoding='utf-8').read()) == body_of(io.open(p, encoding='utf-8').read()):
            绿 = n
            break
    R.append(('②与末版之档逐字同之章（第%s章）判绿' % 绿, 绿 is not None and 跑(绿, 报=False) == 0))
    # ③造一个真回退：塞进一个重复四字串，须⛔且指得出名
    import tempfile
    n3 = 绿
    ok3 = False
    if n3:
        p3 = 正文路径(n3)
        原 = io.open(p3, encoding='utf-8').read()
        try:
            塞 = '\n他把那块石头放下。他把那块石头放下。他把那块石头放下。\n'
            io.open(p3, 'w', encoding='utf-8').write(原.replace('\n\n【本章亮点】', 塞 + '\n【本章亮点】', 1))
            ok3 = 跑(n3, 报=False) == 1
        finally:
            io.open(p3, 'w', encoding='utf-8').write(原)
    R.append(('③塞入一个三现之四字串，新式须⛔（第%s章·跑後原样写回）' % n3, ok3))
    # ④两器同源：不另造尺
    import 跑轮 as _pl
    R.append(('④与跑轮同源·未另造一把尺', score is _pl.score and RATCHET_MIN is _pl.RATCHET_MIN))
    # ⑤两把尺之证：台账所记之数与今日之尺重算不符者几章（故末版之数须自档重算，不读台账）
    不符 = 0
    共档 = 0
    for f in sorted(glob.glob(os.path.join(根, '版本', '第*章', '_台账.json'))):
        mm = re.search(r'第(\d+)章', f)
        if not mm:
            continue
        nn = int(mm.group(1))
        vv = sorted(glob.glob(os.path.join(根, '版本', '第%d章' % nn, 'v*.md')))
        if not vv:
            continue
        led = json.load(io.open(f, encoding='utf-8')).get('版本', [])
        lastled = next((r['soft'] for r in reversed(led) if r.get('soft')), None)
        if not lastled:
            continue
        共档 += 1
        _hh, sc = score(io.open(vv[-1], encoding='utf-8').read())
        if any(k in lastled and sc.get(k) != lastled[k] for k in ('四字串三现', '顿悟起手', '嗅', '沈鸢')):
            不符 += 1
    R.append(('⑤台账之数与今日之尺重算不符者 %d／%d 章——故末版之数自档重算而不读台账' % (不符, 共档),
              不符 > 0))
    # ⑥拆章之豁免不许滥发：111 之拆章前之版（v11·≥8句在112）认得出，而 200 无拆出章故不豁免
    #   ★1027 合流：D1 落（改单#G1027-02）为 111 存了拆章後之 v12，末档已非拆章前——⛔钉「末档」，改钉 111 之 v11 之真档
    _v11 = os.path.join(根, '版本', '第111章', 'v11.md')
    R.append(('⑥拆章豁免只发给真拆过的（111 之 v11 认得出、200 不发）',
              os.path.exists(_v11) and _末版係拆章前(111, _v11)[0] >= 8 and _末版係拆章前(200)[0] == 0))
    # ⑦豁免不吞真回退：拿一个无拆出章之章塞入三现串，照旧⛔（即③之章）
    R.append(('⑦豁免不吞真回退（③之章无拆出章）', _拆出章(绿) is None))
    for 名, ok in R:
        print(('  ✓ ' if ok else '  ⛔ ') + 名)
    print('  自测 %d/%d' % (sum(1 for _, o in R if o), len(R)))
    return all(o for _, o in R)


# ★★★★★DEBT-298A（298第12轮立·限307·於307封版之序结清；1027 自 十轮精进.py 移此——十轮精进汰）
#   ★其伤：棘轮之「四字三现」认的是四字之窗，不是词——一句五个字的重出算两处，六个字的算三处。
#   ★★旧式照旧管棘轮之判（一行不动）；此认词之变式只供 `--项 四字三现·认词` 另报一数，供人裁。
#   ★★★其法：以最长可合并之串为身——凡四字之窗出现≥3次者，向左右各试长一字，长出之串仍≥3次即顶掉短的；
#     末了去掉「已被别的串整个含住」者。**一句只算一处，不论它有几个字。**
def rep3_by_word(body, 门=3):
    """四字三现·认词：把重叠之窗合成最长之串，一句只算一处。返回 (处数, [串…])。"""
    seen = {}
    for i in range(len(body) - 3):
        k = body[i:i + 4]
        if re.match(r'^[\u4e00-\u9fa5]{4}$', k):
            seen[k] = seen.get(k, 0) + 1
    cand = {k for k, v in seen.items() if v >= 门}
    grown = set()
    for k in cand:
        cur = k
        while True:
            better = None
            for ch in {body[m.end():m.end() + 1] for m in re.finditer(re.escape(cur), body)}:      # 向右长一字
                if ch and re.match(r'^[\u4e00-\u9fa5]$', ch) and body.count(cur + ch) >= 门:
                    better = cur + ch
                    break
            if better is None:
                for ch in {body[max(m.start() - 1, 0):m.start()] for m in re.finditer(re.escape(cur), body)}:   # 向左长一字
                    if ch and re.match(r'^[\u4e00-\u9fa5]$', ch) and body.count(ch + cur) >= 门:
                        better = ch + cur
                        break
            if better is None or better == cur:
                break
            cur = better
        grown.add(cur)
    最长 = sorted(grown, key=len, reverse=True)      # 去被别的串整个含住者
    留 = []
    for x in 最长:
        if not any(x in y and x != y for y in 留):
            留.append(x)
    return len(留), sorted(留)


if __name__ == '__main__':
    if '--自测' in sys.argv:
        sys.exit(0 if 自测() else 1)
    if '--全书' in sys.argv:
        全书(); sys.exit(0)
    a = [x for x in sys.argv[1:] if not x.startswith('-')]
    # ★★★★★DEBT-298A（298第12轮立·限307·於307封版之序结清）之口：
    #   `python3 工具/棘轮预检.py N --项 四字三现·认词`
    #   ★旧式（四字之窗）照旧管棘轮之判，一行不动；此口只另报一个认词之数，供人裁。
    #   ★★其由见本档 `rep3_by_word` 之注（1027 自 十轮精进.py 移此）。
    if '--项' in sys.argv:
        i = sys.argv.index('--项')
        项 = sys.argv[i + 1] if len(sys.argv) > i + 1 else ''
        if 项 != '四字三现·认词':
            print('⛔本口只认「四字三现·认词」一项（DEBT-298A 所立）'); sys.exit(2)
        if not a:
            print('用法：python3 工具/棘轮预检.py N --项 四字三现·认词'); sys.exit(2)
        n = int(a[0])
        import glob as _g
        vs = sorted(_g.glob(os.path.join(根, '版本', '第%d章' % n, 'v*.md')))
        src = vs[-1] if vs else None
        f = (src or 正文路径(n))
        if not f:
            print('⛔第%d章之文取不着' % n); sys.exit(2)
        txt = io.open(f, encoding='utf-8').read()
        body = body_of(txt)
        _h, sf = score(txt)
        cnt, strs = rep3_by_word(body)
        print('════ 四字三现·认词 · 第%d章 ════' % n)
        print('  其文：%s' % os.path.basename(f))
        print('  旧式（四字之窗·棘轮所judge者）：%d' % sf.get('四字串三现', -1))
        print('  新式（认词·以最长可合并之串为身）：%d' % cnt)
        print('  ── 逐串（新式）──')
        for x in strs:
            print('   · %s（%d 次）' % (x, body.count(x)))
        print('  ★二式之差 %d：一句五个字的重出，旧式算两处；六个字的算三处——'
              '句子越长它被罚得越重，而它其实只重了一回。' % (sf.get('四字串三现', 0) - cnt))
        sys.exit(0)
    if not a:
        print('用法：python3 工具/棘轮预检.py N｜--全书｜--自测｜N --项 四字三现·认词'); sys.exit(2)
    sys.exit(跑(int(a[0])))
