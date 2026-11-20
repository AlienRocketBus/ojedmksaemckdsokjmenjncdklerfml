#!/usr/bin/env python3
"""章料（1008 立·虫洞之律：机器能找的⛔让模型找）——零 token 汇一章之料，席只读此一档。

为何立：380 造式实测，三魂各席动手 57—146 回、取回 250—550KB，在圣经、canon、施工表、前文里自己搜；
每一回都把越来越长的上下文重发一遍——时与 token 花在「找」上（坑之账②④）。本器把「找」做完：
  开镜卡与预令（全）｜施工表「续写第 N 章前的硬门槛」｜余章总案之解歧之裁与本章前後之拍、本章之种｜
  前两章白文（全）｜开镜卡里点到之人之状态（取最新一章之态）｜涉本章之 canon 卡（有界之卡在前）｜
  悬线里钉在本章之行｜大师进化账末十五条（1015 自三十减：390 之料 130KB 逾限，末十五条为今仍活之教，旧者已入法）｜叫绝之拍库「十条手艺」。
席之令：先读 `版本/第N章/_料.md`；料外只许 grep 核一处、上下三行；⛔自己搜料。
★1027 X58（410 选、审诸席：_料.md 约 4.9 万 token 逾单回 Read 之限、须分两回读）——拆二档：
  `_料.md`＝卡与令（开镜卡、段案、预令、所引原句、内部名、硬门槛、余章总案、人物之态、全员之账、canon、十条手艺）；
  `_料_前文.md`＝前文白文与账（前两章白文、随身物之末位、悬线、进化账）。_料.md 首节点明彼档；执笔、合稿、记席并读，选、审先读卡与令。
  （全员之账留卡与令：稿差.py 之窄席料摘读之·坑㊱ 之消费者。）

用法：
  python3 工具/章料.py N [出档]  → 写 版本/第N章/_料.md 与 _料_前文.md（或 出档 与 出档去 .md 加 _前文.md），印各节之大小
  python3 工具/章料.py --稿引 <稿>...  → 诸稿【本章亮点】所引之章:行汇展（X62·选、合、审诸席⛔awk 补查）
  python3 工具/章料.py --自测
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import os, sys, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from 对账预筛 import 章号, 汉章行  # 汉字章号 → int；汉字之章行 → 数字（X84）


def 读(p):
    p = os.path.join(ROOT, p) if not os.path.isabs(p) else p
    return open(p, encoding='utf-8').read() if os.path.exists(p) else ''


def 章档(n, root=ROOT):
    for f in glob.glob(os.path.join(root, '正文', '*.md')):
        if 章号(f) == n:
            return f
    return None


def 节(文, 头, 止=r'^## '):
    """取以「头」起之一节（至下一个同级之头止）。"""
    m = re.search(r'^' + re.escape(头) + r'.*$', 文, re.M)
    if not m:
        return ''
    rest = 文[m.end():]
    e = re.search(止, rest, re.M)
    return 文[m.start(): m.end() + (e.start() if e else len(rest))].strip()


def 本章之行(文, n, 邻=1):
    """总案、悬线里提到本章（及前後一章）之行。"""
    pat = re.compile(r'(?<!\d)(' + '|'.join(str(k) for k in range(n - 邻, n + 邻 + 1)) + r')(?!\d)')
    return [l for l in 文.split('\n') if pat.search(l)]


def _汉限(s, n):
    """截至第 n 个汉字（「字」照 还账.py ⑥字顶之计：数汉字，标点、数码不计）；逾则截而缀「…」。
    ★1020：复原之由 340 字符而汉字 179——照字符截 300 即把裁文令添之「⛔白文互对（圣经:9869）」截掉半句，故数汉字。"""
    k = 0
    for i, c in enumerate(s):
        if '一' <= c <= '鿿':
            k += 1
            if k > n:
                return s[:i] + '…'
    return s


def 去器表(卡):
    """★1020 398 之料 123128 字节逾限：卡之「起草之日之器表」係记席立卡之日跑器之凭（开镜庭全功率闸所验，卡档原样不动），
    执笔用不着——入料时去其表（只去表，表上下之文照收）。"""
    return re.sub(r'\*\*起草之日之器表\*\*[^\n]*\n\n(?:\|[^\n]*\n)+\n?', '', 卡)


def 人物(卡文, 册, 本线=None):
    """★1015：异线之人（本线係主而其人係暗线，或反之）只收身份一行——二线不通消息，执笔⛔须其知与末态（390 之料 122KB 逾限之治；与 1013「异线之章只收白文」同律）；「两线」之人照收全。"""
    出 = []
    for p in 册.get('人物', []):
        名 = p.get('名', '')
        称 = [名] + [re.split(r'[（(]', a)[0] for a in p.get('别称', []) if a]
        if not any(c and len(c) >= 2 and c in 卡文 for c in 称):
            continue
        态键 = sorted([k for k in p if re.fullmatch(r'\d+态', k)], key=lambda k: int(k[:-1]))
        线 = str(p.get('线', ''))
        if 本线 and 线 in ('主线', '暗线') and not 线.startswith(本线):
            出.append('### %s（%s·末见 %s·异线之人：只其身份）\n- 身份：%s' % (名, p.get('生死', ''), p.get('末见章', ''), str(p.get('身份', ''))[:300]))
            continue
        行 = ['### %s（%s·末见 %s）' % (名, p.get('生死', ''), p.get('末见章', '')),
             '- 身份：' + str(p.get('身份', ''))[:600],
             '- 知：' + '；'.join(p.get('知', []))[:600],
             '- 不知：' + '；'.join(p.get('不知', []))[:400]]
        if str(p.get('复原之由') or '').strip():   # ★1020 大审397·#45：非态之键「复原之由」须到执笔眼里（只印末一态则漏）——一行，≤300 字
            行.append('- 复原之由：' + _汉限(str(p['复原之由']).strip(), 300))
        if 态键:
            行.append('- %s：%s' % (态键[-1], str(p[态键[-1]])[:900]))
        出.append('\n'.join(行))
    return 出


def 全员(册):
    """★1009 坑⑬：料包须含「已定之细」——全员生死、末见、线、最新之态（一人一行）；开镜卡点到者另有全卡。"""
    出 = []
    for p in 册.get('人物', []):
        态键 = sorted([k for k in p if re.fullmatch(r'\d+态', k)], key=lambda k: int(k[:-1]))
        亡 = ('亡於 %s' % p.get('亡於章')) if p.get('亡於章') not in (None, '', 'None') else ''
        态 = ('｜%s：%s' % (态键[-1], str(p[态键[-1]])[:140])) if 态键 else ''
        出.append('- %s｜%s%s｜末见 %s｜%s%s' % (p.get('名', ''), p.get('生死', ''), ('·' + 亡) if 亡 else '',
                                            p.get('末见章', ''), p.get('线', ''), 态))
    return 出


限料 = 120 * 1024   # ★1009 坑③：档要短——章料逾此即红（380 实 102KB）


def canon卡(卡文, 库, n, 限=24000):
    有界, 名中 = [], []
    for f in 库.get('facts', []):
        if f.get('level') not in ('ERROR', 'WARN'):
            continue
        only = f.get('only_ch') or []
        frm = f.get('from_ch')
        if (only and n in only) or (frm and frm >= n - 10 and frm <= n):
            有界.append(f)
            continue
        idn = re.sub(r'^F\d+_', '', f.get('id', ''))
        if any(w and len(w) >= 2 and w in 卡文 for w in re.split(r'[与之和、]', idn)):
            名中.append(f)
    出, 计 = [], 0
    for f in 有界 + 名中:
        s = '- **%s**（%s）：%s' % (f['id'], f.get('level'), f.get('note', '')[:900])
        if 计 + len(s) > 限:
            出.append('- ……（另 %d 卡未列，限 %d 字）' % (len(有界) + len(名中) - len(出), 限)); break
        出.append(s); 计 += len(s)
    return 出


def 段案行(n, root=ROOT):
    """1013：设定/段案/<a>-<b>.md 之「## n」一节（重、魂路、叫绝之拍、种、知之变、物之动、日、收（旧名钩））；无则空。
    〔1119 死规之审·gates1/docs3〕「钩」改「收（可无）」：整节照印，⛔分其项。"""
    for f in sorted(glob.glob(os.path.join(root, '设定', '段案', '[0-9]*-[0-9]*.md'))):
        t = open(f, encoding='utf-8').read()
        m = re.search(r'^## %d\s*$(.*?)(?=^## |\Z)' % n, t, re.M | re.S)
        if m:
            return '（%s）\n%s' % (os.path.relpath(f, root), m.group(1).strip())
    return ''



# ★1119 X119（469：卡判暗线常章带 2,300—3,100、段案定 2,900—3,300——五执笔照卡写、四稿俱 2,300 余，合後低段案约 455）：
#   本章之带唯段案「字数：a—b」为准——自走之派令、承.py 以之传 args.带，造章.js（N≥471）执笔令【厚】照之；造式验 --料 见卡带不一即红
带式 = re.compile(r'(\d,\d{3})\s*[—\-～~]+\s*(\d,\d{3})')


def 段案之带(n, root=ROOT):
    """→ 'a—b'（段案本章一节「字数：a—b」，千分位逗号）；无则空。"""
    m = re.search(r'字数[：:]\s*\**\s*(?:[^\d\n]{0,8})?(\d,\d{3})\s*[—\-～~]+\s*(\d,\d{3})', 段案行(n, root))
    return '%s—%s' % m.groups() if m else ''

# ★1015（391 诸席「此法之缺」七席同报：卡令「照 268 原句」而料只展单行；D3:76、D6 T44、余章总案:54 俱不展——七席各自 awk 整章，费七回）
_设档 = {'总纲': os.path.join('设定', '02_余章之势_总纲.md'),
        '余章总案': os.path.join('设定', '剧情庭题', '余章总案.md'),
        'D3': os.path.join('设定', '剧情庭题', 'D3_真拦之敌_主案.md'),
        'D6': os.path.join('设定', '剧情庭题', 'D6_床上那人_六审主案.md')}
_引式 = re.compile(r'(?<![\d:A-Za-z])(总纲|余章总案|D3|D6|\d{3})(?:\.md)?(?:\s*主案)?\s*[:：]\s*(\d{1,4})(?:\s*[—\-～~]\s*[:：]?(\d{1,4}))?(?!\d)')
# ★X62（1027）：诸稿【本章亮点】之引另认二式——章号一至三位（「73：165」）、行段以「至」连（「404：99至105」）；卡与段案之引照 _引式（⛔动）
_稿引式 = re.compile(r'(?<![\d:A-Za-z])(?<!拍库)(?<!拍库 )(总纲|余章总案|D3|D6|[1-9]\d{0,2})(?:\.md)?(?:\s*主案)?\s*[:：]\s*(\d{1,4})(?:\s*[—\-～~至]\s*[:：]?(\d{1,4}))?(?!\d)')
# ★X132（479·477 共病之一根：段案引 471:35「他的骨头里，来了一句话。」而其句在 :37——诸席读作他句）：单行之引而其行以冒号、或「一句话／一句／说／道／问／喊」收者，其下文係所引之实
_引下式 = re.compile(r'([：:]|(?:一句话|一句|一声|说|道|问|喊|念|写着)[。，,]?)[」』"]?$')
_行式 = re.compile(r'(?<![A-Za-z])(D3|D6)\s*(?:主案\s*)?([RWT]\d{1,3})(?!\d)')


def 引之原句(文, root=ROOT, 限=80, 段限=30, 字限=30 * 1024, 略章=(), 式=None):
    """1013（坑⑬复踩之治）：开镜卡、段案、预令所引之「章:行」（如 380:69）与「总纲:行」逐一展开为原句。
    ⛔其由：381 之料只带章号不带原句（318:33、327:29 之掰口等），五稿三稿各撞坏一处已定之细（掰口写反、空钉、床位）。
    行号逾其章之行数者（如 380:2572 是净重，不是行）⛔展；空行⛔展。
    ★1015：①行段「268:61—77」整段展（每段至多 30 行）；②「D3:76」「D3 主案:76」「D6:75」「余章总案:54」认其档；
    ③「D6 T44」「D3 W7」认主案表中以其号起之行；④展出逾 30KB 即止（照实印所舍）。
    ★X43（1027·W60 驳席）：略章之认移於行号之验後——旧序先查略章、後查章长，卡中净重「397:2440」（397 為略章）即认作章引、列入「见前文白文」；
    今行号逾其章之行数者，略章亦⛔列。式：所用之引式（缺省 _引式；诸稿之亮点用 _稿引式）。"""
    出, 见, 档 = [], set(), {}
    大 = 0
    略 = []                                   # ★1016：前文白文已全收（带行号）之章⛔重展，只列其号

    def 行们(f):
        if f not in 档:
            档[f] = open(f, encoding='utf-8').read().split('\n')
        return 档[f]
    for m in (式 or _引式).finditer(文):
        k = m.group(0)
        if k in 见:
            continue
        见.add(k)
        名 = m.group(1)
        f = os.path.join(root, _设档[名]) if 名 in _设档 else 章档(int(名), root)
        if not f or not os.path.exists(f):
            continue
        L = 行们(f)
        i = int(m.group(2)); j = int(m.group(3)) if m.group(3) else i
        if not (1 <= i <= len(L)):           # ★X43：先验行号（净重「397:2440」⛔认），後查略章
            continue
        if 名.isdigit() and int(名) in 略章:
            略.append(k); continue
        if j < i or j - i >= 段限:
            j = i + 段限 - 1 if j >= i else i
        if i == j and _引下式.search(L[i - 1].strip()):   # ★X132（479）：单行引而其行引出下文（「来了一句话。」「说：」）——连展至下一非空行
            j = next((x for x in range(i + 1, min(len(L), i + 4) + 1) if L[x - 1].strip()), i)
        if (f, i, j) in 见:                    # 「D3:76」「D3 主案:76」同一处只展一回
            continue
        见.add((f, i, j))
        块 = ['- %s　%s' % (k, L[i - 1].strip()[:400])] if i == j else \
             ['- %s' % k] + ['  %d｜%s' % (x, L[x - 1].strip()[:400]) for x in range(i, min(j, len(L)) + 1) if L[x - 1].strip()]
        if i == j and not L[i - 1].strip():
            continue
        b = len('\n'.join(块).encode())
        if 大 + b > 字限 or len(出) >= 限:
            出.append('（所引尚有未展者——逾 %d KB 之限；要者照其号 awk 一处）' % (字限 // 1024)); break
        出.append('\n'.join(块)); 大 += b
    for m in _行式.finditer(文):
        k = '%s %s' % (m.group(1), m.group(2))
        if k in 见:
            continue
        见.add(k)
        f = os.path.join(root, _设档[m.group(1)])
        if not os.path.exists(f):
            continue
        for x, l in enumerate(行们(f), 1):
            if re.match(r'^\|?\s*\**%s\**\s*[|｜：:　 ]' % m.group(2), l.strip()):
                b = len(l.encode())
                if 大 + b <= 字限:
                    出.append('- %s（%s:%d）　%s' % (k, m.group(1), x, l.strip()[:600])); 大 += b
                break
    if 略:
        出.append('- 见前文白文（料中已全收、行首带号，⛔重展）：%s' % '、'.join(略))
    return 出


def 稿之引(路们, root=ROOT, 字限=24 * 1024):
    """★X62（1027·410 选席七回、审席十回之料外补查·1024_W71 行家 flaws①—④）：诸稿【本章亮点】所引之「章:行」由器汇展——零 token，
    选、合、审诸席照此印引原场、核致命之据，⛔awk 补查。先列各稿所引之号（⛔认【本章亮点】以前之白文），後展原句（诸稿同引者只展一回）。"""
    出, 合 = [], []
    for p in 路们:
        t = 读(p) if os.path.exists(p) else ''
        名 = os.path.basename(p)
        if '【本章亮点】' not in t:
            出.append('- %s：%s' % (名, '缺档' if not t else '无【本章亮点】')); continue
        亮 = 汉章行(t[t.index('【本章亮点】'):])     # ★X84（1105）：汉字之章行（「四百一十二：五十三」）器内换作数字再认
        号 = list(dict.fromkeys(m.group(0) for m in _稿引式.finditer(亮)))
        出.append('- %s：%s' % (名, '、'.join(号) if 号 else '无章:行之引'))
        合.append(亮)
    展 = 引之原句('\n'.join(合), root, 限=200, 字限=字限, 式=_稿引式) if 合 else []
    return ['〔诸稿所引〕'] + 出 + ['〔原场（章:行 逐一展开；行号逾其章者⛔展）〕'] + (展 or ['- 无'])


def _他章已接(l, n):
    """悬线里「- **386（主·…）**〔1014 已接写…〕」一类：他章之接写之记，提及本章号而非钉於本章。"""
    m = re.match(r'\s*-\s*\*\*(\d{3})（', l)
    return bool(m and int(m.group(1)) != n and '已接写' in l)


def _号行(t):
    """★1015（392 二席报：前文白文不带行号，引一处须另跑 awk）——非空行前加「行号｜」，空行照留。"""
    return '\n'.join(('%d｜%s' % (i, l)) if l.strip() else l for i, l in enumerate(t.split('\n'), 1))


def 内部名(文, root=ROOT):
    """1015（391 五席同报：卡用「点户」「档柜」「贺兰」，正文 0 见——各席各译）：卡、段案里 2—4 字之「名」，正文全书 0 见者。"""
    名们 = sorted(set(re.findall(r'「([\u4e00-\u9fff]{2,4})」', 文)))
    if not 名们:
        return []
    白 = ''.join(open(f, encoding='utf-8').read() for f in glob.glob(os.path.join(root, '正文', '*.md')))
    return [x for x in 名们 if x not in 白]


def 物之末位(文, 物文, n=10 ** 6, 限=8000):
    """★X48（1022·405）：物之末位（零 token·全书记忆/物件.md）——执笔⛔凭记性放物：
    ① 主、暗二线各取 n 前最近一章之「- **N 之物（主线／暗线…）**」块（每物末位逐条在内）；
    ② 「### 名」之要物，卡、段案、预令点到者取其「今」一行。"""
    出 = []
    块 = {}
    for m in re.finditer(r'^- \*\*(\d+) 之物（([主暗])线[^\n]*\n((?:  .*\n?)*)', 物文, re.M):
        k = int(m.group(1))
        if k < n and k > 块.get(m.group(2), (0,))[0]:
            块[m.group(2)] = (k, m.group(0).rstrip())
    for 线 in sorted(块, key=lambda x: -块[x][0]):
        出.extend(_汉限(l, 120) for l in 块[线][1].split('\n'))
    for m in re.finditer(r'^### (.+?)\n(.*?)(?=^#{2,3} |\Z)', 物文, re.M | re.S):
        头, 体 = m.group(1).strip(), m.group(2)
        名 = [re.sub(r'（[^）]*）', '', x).strip('「」 ') for x in re.split(r'[＝、与]', 头)]
        名 = [x.split('之')[-1] for x in 名 if x]
        今 = re.search(r'^- \*\*今\*\*：(.*)$', 体, re.M)
        if 今 and any(len(x) >= 2 and x in 文 for x in 名):
            出.append('- **%s**：%s' % (头, _汉限(今.group(1).strip(), 200)))
    while 出 and len('\n'.join(出).encode()) > 限:
        出.pop()
    return 出


前文之节 = ('前文·', '随身物之末位', '悬线·', '大师进化账·')   # ★X58：「前文白文与账」一档之节（余俱入卡与令）


def 属前文(名):
    return 名.startswith(前文之节)


def 前文之档(出):
    """_料.md → _料_前文.md（出档 x.md → x_前文.md）。"""
    return (出[:-3] if 出.endswith('.md') else 出) + '_前文.md'


# ★X127（1120·475 段案「签收夹（埋於268）」268 无其句、三执笔 grep 落空）：段案「收「键」（埋於 N）」逐条 grep 第 N 章正文，
#   键之实字二字组（去虚字）零见即「种之原场缺」，入料首、交主环先改段案（标设计之称而前文另有其句者亦印——主环核即过）
_种虚 = set('之的那一了这个上下又他她我你')


def 种之原场缺(案行, root=ROOT):
    出 = []
    for 键, n in re.findall(r'收[「“]([^」”]{1,30})[」”][（(]埋於\s*(\d+)[）)]', 案行):
        f = 章档(int(n), root)
        if not f:
            continue
        文 = 读(f)
        汉 = re.findall(r'[一-鿿]+', 键)
        对 = {s[i:i + 2] for s in 汉 for i in range(len(s) - 1) if not (set(s[i:i + 2]) & _种虚)}
        对 = 对 or {c for s in 汉 for c in s if c not in _种虚}
        if 对 and not any(p in 文 for p in 对):
            出.append('- 收「%s」（埋於 %s）：第%s章正文零见其字——原场缺或在他章，主环先核改段案' % (键, n, n))
    return 出


def 汇(n, root=ROOT, 出=None):
    d = os.path.join(root, '版本', '第%d章' % n)
    卡 = 读(os.path.join(d, '_开镜卡.md'))
    if not 卡:
        raise SystemExit('⛔ 无开镜卡：版本/第%d章/_开镜卡.md' % n)
    预 = 读(os.path.join(d, '_总编辑预令.md'))
    施 = 读(os.path.join(root, '设定', '01_镇冢秘术_逐章施工与伏笔回收表.md'))
    案 = 读(os.path.join(root, '设定', '剧情庭题', '余章总案.md'))
    悬 = 读(os.path.join(root, '设定', '全书记忆', '悬线.md'))
    进 = 读(os.path.join(root, '设定', '大师进化账.md'))
    拍 = 读(os.path.join(root, '设定', '叫绝之拍库.md'))
    册 = json.loads(读(os.path.join(root, '设定', '人物状态册.json')) or '{}')
    库 = json.loads(读(os.path.join(root, '设定', 'canon事实库.json')) or '{}')
    段 = []
    案行 = 段案行(n, root)
    缺种 = 种之原场缺(案行, root) if 案行 else []
    if 缺种:                                    # ★X127：入料首
        段.append(('⛔ 种之原场缺（段案「埋於 N」而第 N 章零见·X127）', '\n'.join(缺种)))
    段.append(('开镜卡', 去器表(卡)))
    if 案行:
        # 〔1119 死规之审·gates1/prompts2/docs3〕标改：收处降为参考、⛔照抄段案之句为末句（426、430、468 末句即段案之钩逐字）；即刻生效（473—480 旧段案之「钩」由此标降为参考）
        #   〔1119 总章心诀5·退回〕叫绝之拍回「照此」：无一伤录记执笔照段案之拍造而伤（骨刻意、皮自在）
        段.append(('段案·本章之行（事、叫绝之拍、种、知之变、物之动、日——照此；收处係参考，执笔可更好；⛔照抄段案之句为末句）', 案行))
        try:                                    # ★1113 X105：段案头之「⛔「X」字」执笔只见本章一节而不见头（453「潮」字之漏）——同印其列（造式验同一把·禁字致命）
            import 造式验
            禁 = 造式验.段案之禁字(n, root)
            if 禁:
                段.append(('段案所禁之字（白文一字⛔出，造式验致命）', '、'.join('「%s」' % z for z in 禁)))
        except Exception:
            pass
    if 预:
        段.append(('总编辑预令', 预))
    引 = 引之原句(卡 + '\n' + 案行 + '\n' + 预, root, 略章={k for k in (n - 1, n - 2) if 章档(k, root)})
    if 引:
        段.append(('开镜卡、段案所引之原句（章:行 逐一展开——写已定之细只照此，⛔凭章号猜）', '\n'.join(引)))
    内 = 内部名(卡 + '\n' + 案行, root)
    if 内:
        段.append(('卡之内部名（正文全书 0 见——设计之称或新物；白文⛔照搬：照卡中「白文作」，无则译成在场之人口里、眼里之称，诸稿各自译，合稿统一）', '、'.join(内)))
    门 = 节(施, '## 四、续写第 %d 章前的硬门槛' % n)
    if 门:
        段.append(('施工表·续写本章前之硬门槛', 门))
    if 案:
        if not 案行:                            # ★1015：段案係「据余章总案 §二解歧之裁」所立（只汇只验）——有段案之章⛔重收 §二（392 料 6KB）
            段.append(('余章总案·解歧之裁', 节(案, '## 二、')))
        if 案行:                                # ★1015（392 料 132KB）：段案已据余章总案立本章之行（且随裁同改）——总案只留「下一章」之行，供埋种；本章与前一章⛔重收
            本行 = set(本章之行(案, n, 0)) | set(本章之行(案, n - 1, 0))
            段.append(('余章总案·下一章之行（%d；本章之设计见段案）' % (n + 1), '\n'.join(l for l in 本章之行(案, n + 1, 0) if l not in 本行)))
            if n >= 477:                        # ★1120 477 共病（四稿把「骨里那一句」落今时）：余章总案:240 之露句之守、489 之「前两回」点到本章而料只汇 n+1 之行——汇总案中点到本章号之他行（每行 ≤600 字、共 ≤8KB）
                已 = set(l for l in 本章之行(案, n + 1, 0) if l not in 本行)
                点 = [l.strip()[:600] for l in 案.split('\n') if re.search(r'(?<!\d)%d(?!\d)' % n, l) and l not in 已 and l.strip()]
                if 点:
                    段.append(('余章总案·点到本章之他行（後章所倚、诸守——本章须为之立锚；⛔越段案之设计）', _汉限('\n'.join(点), 8 * 1024 // 3) if len('\n'.join(点).encode()) > 8 * 1024 else '\n'.join(点)))
        else:
            段.append(('余章总案·本章前後之行（%d±1）' % n, '\n'.join(本章之行(案, n))))
    import 造式验
    本线 = 造式验.线(n, root)
    for k in (n - 1, n - 2):
        f = 章档(k, root)
        if f:
            t = open(f, encoding='utf-8').read()
            if 本线 and 造式验.线(k, root) and 造式验.线(k, root) != 本线 and '【本章亮点】' in t:
                # ★1013：异线之章只收白文（其骨记係另一线之种与物，二线不通消息；384 之料 130KB 逾限，此节省 11KB）；同线之章照收全（物之去向在其骨记）
                段.append(('前文·第%d章白文（异线·只白文；行首为行号，引作「%d:行」）' % (k, k), _号行(t[:t.index('【本章亮点】')].rstrip())))
            else:
                段.append(('前文·第%d章白文（全；行首为行号，引作「%d:行」）' % (k, k), _号行(t)))
    物 = 物之末位(卡 + '\n' + 案行 + '\n' + 预, 读(os.path.join(root, '设定', '全书记忆', '物件.md')), n)
    if 物:
        段.append(('随身物之末位（卡、段案点到之物·全书记忆/物件.md 之「今」——物在谁手、何处，照此放）', '\n'.join(物)))
    人 = 人物(卡 + 预, 册, 本线)
    if 人:
        段.append(('人物之态（开镜卡点到者）', '\n\n'.join(人)))
    全 = 全员(册)
    if 全:
        段.append(('全员之账（生死、末见、线、最新之态）', '\n'.join(全)))
    c = canon卡(卡 + 预, 库, n)
    if c:
        段.append(('canon 卡（有界在前，名中在後）', '\n'.join(c)))
    悬行 = [l for l in 本章之行(悬, n, 0) if not _他章已接(l, n)]   # ★1016（394 料 122KB）：他章已接写之记（史，非钉本章之悬）⛔收
    if 悬行:
        段.append(('悬线·钉在本章之行', '\n'.join(悬行)))
    教 = [l for l in 进.split('\n') if l.startswith('- ')][-15:]
    if 教:
        段.append(('大师进化账·末十五条', '\n'.join(教)))
    手 = 节(拍, '## 十条手艺') or 节(拍, '## 十')
    if 手:
        段.append(('叫绝之拍库·十条手艺', 手))
    出 = 出 or os.path.join(d, '_料.md')
    出前 = 前文之档(出)
    卡段 = [(名, x) for 名, x in 段 if not 属前文(名)]
    前段 = [(名, x) for 名, x in 段 if 属前文(名)]
    相 = os.path.relpath(出前, root) if os.path.abspath(出前).startswith(os.path.abspath(root) + os.sep) else 出前
    文 = ['# 第%d章·章料·卡与令（工具/章料.py 零 token 汇；席只读此二档，料外只许 grep 核一处、上下三行）\n' % n,
         '## 〔本料二档（X58·1027 拆）〕\n\n本档＝卡与令。**前文白文与账**（%s）在 `%s`——执笔、合稿、记席并读之（Read·allow_large）；选、审诸席先读本档，须前文时再读彼档。\n'
         % ('、'.join(名.split('（')[0] for 名, _ in 前段) or '无', 相)]
    for 名, x in 卡段:
        文.append('## 〔%s〕\n\n%s\n' % (名, x.strip()))
    前文 = ['# 第%d章·章料·前文白文与账（工具/章料.py 零 token 汇；卡与令在 _料.md）\n' % n]
    for 名, x in 前段:
        前文.append('## 〔%s〕\n\n%s\n' % (名, x.strip()))
    open(出, 'w', encoding='utf-8').write('\n'.join(文))
    open(出前, 'w', encoding='utf-8').write('\n'.join(前文))
    for 名, x in 段:
        print('  %s %-28s %6d 字节' % ('前' if 属前文(名) else '卡', 名, len(x.encode())))
    大, 大前 = os.path.getsize(出), os.path.getsize(出前)
    print('✓ 写 %s（卡与令 %d KB）、%s（前文白文与账 %d KB）' % (os.path.relpath(出, root), 大 // 1024, os.path.relpath(出前, root), 大前 // 1024))
    坏 = [(名, k) for 名, k in ((os.path.basename(出), 大), (os.path.basename(出前), 大前)) if k > 限料]
    if 坏:
        print('⛔ 章料 %s 逾限 %d KB（坑③：档要短——每席每回都背它）：先瘦开镜卡与预令，⛔删全员之账与 canon'
              % ('、'.join('%s %d KB' % (名, k // 1024) for 名, k in 坏), 限料 // 1024))
        return None
    return 出


def 自测():
    ok = 共 = 0
    共 += 1; ok += 本章之行('a 380 b\nc 3801 d\ne 379 f\ng 12', 380) == ['a 380 b', 'e 379 f']
    文 = '# t\n## 一、甲\nx\n## 二、乙\ny\nz\n## 三、丙\nw'
    共 += 1; ok += 节(文, '## 二、') == '## 二、乙\ny\nz'
    册 = {'人物': [{'名': '老头', '别称': ['樗里闩（终局方许）'], '生死': '存', '知': ['甲'], '不知': [], '379态': '新', '377态': '旧'}]}
    r = 人物('老头站着', 册)
    共 += 1; ok += (len(r) == 1 and '379态：新' in r[0])
    库 = {'facts': [{'id': 'F1_老头之眼', 'level': 'ERROR', 'note': 'n1'}, {'id': 'F2_别的', 'level': 'ERROR', 'note': 'n2', 'only_ch': [380]},
                    {'id': 'F3_无关', 'level': 'ERROR', 'note': 'n3'}, {'id': 'F4_债词', 'level': 'FYI', 'note': 'n4', 'only_ch': [380]}]}
    c = canon卡('老头站着', 库, 380)
    共 += 1; ok += (len(c) == 2 and 'F2_别的' in c[0] and 'F1_老头之眼' in c[1])
    _人 = 人物('乙丙在卡上', {'人物': [{'名': '乙丙', '生死': '存', '末见章': 380, '线': '暗线', '身份': '暗线之人', '知': ['秘'], '380态': '态'}]}, '主')
    共 += 1; ok += len(_人) == 1 and '异线之人' in _人[0] and '秘' not in _人[0]          # 主线之章：暗线之人只其身份
    _人2 = 人物('乙丙在卡上', {'人物': [{'名': '乙丙', '生死': '存', '末见章': 380, '线': '暗线', '身份': '暗线之人', '知': ['秘'], '380态': '态'}]}, '暗')
    共 += 1; ok += '秘' in _人2[0]                                                         # 同线照收全
    # ★1020 大审397·#45：非态之键「复原之由」印一行（≤300 字·数汉字）；无此键⛔印；异线之人⛔印
    _复 = 人物('老头站着', {'人物': [{'名': '老头', '生死': '存', '知': [], '复原之由': '由在白文三笔；⛔年。', '396态': '末'}]})
    共 += 1; ok += ('\n- 复原之由：由在白文三笔；⛔年。\n- 396态：末' in _复[0]) and '复原之由' not in r[0]
    _长 = 人物('老头站着', {'人物': [{'名': '老头', '生死': '存', '复原之由': '甲，' * 400}]})[0].split('- 复原之由：')[1].split('\n')[0]
    共 += 1; ok += len(re.findall(r'[一-鿿]', _长)) == 300 and _长.endswith('…') and _汉限('甲，乙', 300) == '甲，乙'
    共 += 1; ok += '复原之由' not in 人物('乙丙在卡上', {'人物': [{'名': '乙丙', '线': '暗线', '身份': '暗', '复原之由': '由'}]}, '主')[0]
    _真 = json.load(open(os.path.join(ROOT, '设定', '人物状态册.json'), encoding='utf-8'))
    _老 = [x for x in 人物('老头', _真, '主') if x.startswith('### 老头')]
    _真由 = [p for p in _真['人物'] if p.get('名') == '老头'][0].get('复原之由', '')
    共 += 1; ok += bool(_老) and ('- 复原之由：' + _汉限(_真由, 300)) in _老[0] and len(re.findall(r'[一-鿿]', _汉限(_真由, 300))) <= 300   # 真册：老头条印得出
    全 = 全员({'人物': [{'名': '甲', '生死': '亡', '亡於章': 300, '末见章': 300, '线': '主线', '299态': '旧', '300态': '倒'},
                        {'名': '乙', '生死': '存', '亡於章': None, '末见章': 380, '线': '暗线'}]})
    共 += 1; ok += (len(全) == 2 and '亡於 300' in 全[0] and '300态：倒' in 全[0] and '亡於' not in 全[1])
    共 += 1; ok += (限料 == 120 * 1024)
    _物 = 物之末位('他摸本子', '### 合玉（半）\n- **今**：领口\n### 苏衍之本子（甲）\n- **首见**：1\n- **今**：怀里\n## 七\n- **9 之物（暗线·甲）**：\n  - **勺**：罐口\n- **11 之物（暗线·乙）**：\n  - **勺**：缸边\n- **10 之物（主线·丙）**：\n  - **灯**：案上\n', 11)
    共 += 1; ok += _物 == ['- **10 之物（主线·丙）**：', '  - **灯**：案上', '- **9 之物（暗线·甲）**：', '  - **勺**：罐口', '- **苏衍之本子（甲）**：怀里']   # X48：二线各取 n 前最近一块＋点到之要物
    共 += 1; ok += 去器表('甲\n\n**起草之日之器表**（亲跑）：\n\n| 命令 | 其印 |\n|---|---|\n| a | b |\n\n**本章不许写的三样**') == '甲\n\n**本章不许写的三样**'
    共 += 1; ok += ('魂路：翻个儿｜物证｜不说' in 段案行(386) and 段案行(999) == '')
    _f = 章档(380); _行 = open(_f, encoding='utf-8').read().split('\n') if _f else ['']
    _引 = 引之原句('见 380:1 又 380:1，又 380:2572（净重）、总纲:1、9380:1', ROOT)
    共 += 1; ok += (len(_引) == 2 and _引[0] == '- 380:1　' + _行[0].strip()[:400] and _引[1].startswith('- 总纲:1　'))
    _段 = 引之原句('照 380:1—3、380:5—1（倒段只展首行）', ROOT)                             # ★1015 行段整展、倒段只首行
    共 += 1; ok += (len(_段) == 2 and _段[0].startswith('- 380:1—3\n  1｜') and _段[1].startswith('- 380:5—1　'))
    _x = 引之原句('段案引 471:35', ROOT)                                                      # ★X132：引出下文之行连展至其句
    共 += 1; ok += (len(_x) == 1 and _x[0].startswith('- 471:35\n  35｜') and '37｜' in _x[0] and '一村人' in _x[0])
    _d = 引之原句('D3:1、D3 主案:1、余章总案.md:1、D6 T44', ROOT)                                # 设档之认、主案表之号
    共 += 1; ok += (len(_d) == 3 and any(x.startswith('- D6 T44（D6:') for x in _d) and _d[1].startswith('- 余章总案.md:1'))
    _略 = 引之原句('380:1 与 381:2', ROOT, 略章={381})
    共 += 1; ok += (len(_略) == 2 and _略[0].startswith('- 380:1') and '381:2' in _略[1] and '见前文白文' in _略[1])   # 前文已收之章⛔重展
    # ★X43（1027）：略章之卡中净重「397:2440」⛔认作章引（旧序先查略章——回灌即红）；略章之真行照列
    _净 = 引之原句('净重 380:2572、380:1', ROOT, 略章={380})
    共 += 1; ok += (_净 == ['- 见前文白文（料中已全收、行首带号，⛔重展）：380:1'])
    # ★X62（1027）：诸稿亮点之引汇展——只认【本章亮点】以後；二位章号、「至」连之行段；诸稿同引只展一回；缺档照印
    import tempfile as _tf2
    _dd = _tf2.mkdtemp()
    _a, _b = os.path.join(_dd, '起草_稿一.md'), os.path.join(_dd, '起草_稿二.md')
    open(_a, 'w', encoding='utf-8').write('白文 380:3\n【本章亮点】\n接380：1，又 380:2—3；净重 380:2572\n')
    open(_b, 'w', encoding='utf-8').write('白文\n【本章亮点】\n握380：1\n')
    _g = 稿之引([_a, _b, os.path.join(_dd, '起草_稿三.md')], ROOT)
    共 += 1; ok += (_g[1] == '- 起草_稿一.md：380：1、380:2—3、380:2572' and _g[2] == '- 起草_稿二.md：380：1' and _g[3] == '- 起草_稿三.md：缺档'
                   and sum(x.startswith('- 380：1　') for x in _g) == 1 and any(x.startswith('- 380:2—3\n') for x in _g) and not any('380:3' in x for x in _g))
    _c = os.path.join(_dd, '起草_稿四.md')
    open(_c, 'w', encoding='utf-8').write('【本章亮点】\n握73：1至2\n')
    共 += 1; ok += (not 章档(73)) or 稿之引([_c], ROOT)[-1].startswith('- 73：1至2\n  1｜')        # 二位章号、「至」之段
    共 += 1; ok += (_他章已接('- **386（主·一）**〔1014 已接写〕：…394…', 394) and not _他章已接('- **394（主·一）**〔已接写〕', 394) and not _他章已接('- 钉 394：某物', 394))
    共 += 1; ok += (内部名('「老头」「七七七七」「那盏灯」') == ['七七七七'] or 内部名('「老头」「七七七七」') == ['七七七七'])   # 正文 0 见者
    import tempfile as _tf, io as _io, contextlib as _cl
    _o = os.path.join(_tf.mkdtemp(), 'x.md')
    with _cl.redirect_stdout(_io.StringIO()):
        汇(384, ROOT, _o)
    _卡 = open(_o, encoding='utf-8').read()
    _x = open(前文之档(_o), encoding='utf-8').read()
    共 += 1; ok += ('前文·第383章白文（异线·只白文' in _x and '前文·第382章白文（全' in _x and '\n1｜' in _x)   # 异线只白文、同线照全；行首带号
    # ★X58（1027）：拆二档——前文白文与账⛔在卡与令；卡与令首节点明彼档；全员之账留卡与令（稿差之消费者）；回灌：旧之一档之式此判即红
    共 += 1; ok += ('〔前文·' not in _卡 and '〔随身物之末位' not in _卡 and '〔悬线·' not in _卡 and '〔大师进化账·' not in _卡 and '〔开镜卡〕' in _卡 and '〔全员之账' in _卡
                   and '〔本料二档' in _卡.split('## 〔开镜卡〕')[0] and os.path.basename(前文之档(_o)) in _卡 and '〔开镜卡〕' not in _x)
    共 += 1; ok += (前文之档('/a/_料.md') == '/a/_料_前文.md' and 属前文('前文·第3章白文') and not 属前文('全员之账（生死）'))
    # 〔1119 死规之审·gates1/prompts2〕段案之标：收处係参考、⛔照抄段案之句为末句（叫绝之拍照此·总章心诀5 退回）；旧标「执笔照此造」⛔再出（稿差以「〔段案·本章之行」为首认之，首⛔变）
    共 += 1; ok += ('〔段案·本章之行（事、叫绝之拍、种、知之变、物之动、日——照此；收处係参考，执笔可更好；⛔照抄段案之句为末句）〕' in _卡 and '执笔照此造' not in _卡)
    # ★X127：段案之种原场核——268 无「签收夹」即印；在者⛔印
    共 += 1; ok += (len(种之原场缺('收「签收夹」（埋於 268）；收「骨头里」（埋於 471）', ROOT)) == 1)
    print('章料·自测 %d/%d' % (ok, 共))
    return ok == 共


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--自测']:
        sys.exit(0 if 自测() else 1)
    if a[:1] == ['--稿引'] and len(a) > 1:   # ★X62：诸稿亮点所引之原场（选之先跑、合、审）
        print('\n'.join(稿之引(a[1:])))
        sys.exit(0)
    if len(a) not in (1, 2) or not a[0].isdigit():
        print(__doc__); sys.exit(2)
    sys.exit(0 if 汇(int(a[0]), 出=a[1] if len(a) == 2 else None) else 1)
