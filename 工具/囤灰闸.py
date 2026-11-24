#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""囤灰闸——**造了没人用的器、席、机制，一个也不许留在仓里**。

【其立之由（2026-09-08·作者令）】
  作者说：「本来你做这个东西是非常厉害，能够去帮助写出中国第一的小说，
  然而你却很多东西却没有用起来，这是很可怕的一件事儿。」
  ★这话点的是本仓一个真病：**一百一十八个器、四张席、三十条坑，没有一样机制在查「它有没有被调用」。**
  全测查的是「跑过的器绿不绿」，从不查「该跑的器跑没跑」——**造出来搁着的，全测一声不吭。**

【它认哪几样，本书同类共几样（令§六④）】
  甲·器之囤灰：认 `工具/*.py` **全部 118 样**（本书同类即此 118 样，无遗）。
     判法：自诸真跑口（全测／起草闸／大审／书级体检／跑轮／自走／封版／接棒守；1027 汰一坐、回修、十轮精进、一章到底——其器俱删）
     并 `工具/席/*.js` 与 git 钩子起，**逐层展开引用闭包**；闭包之外者即囤灰。
  乙·席之囤灰：认 `工具/席/*.js` **全部**（当场 glob）。判法（1020 X29 改·见 `席之判`）：派令之文（`造章.js`、`自走.py`）以
     `scriptPath:'工具/席/<名>'` 调者即有路（⛔只提其名、注行不算）；余者须在 `工具/席/用法.md`「诸席之位与末用」表有其行
     （其位·末用·限），末用 ≤ 末章、限 ≤ 末用＋30 且未到——⛔「用法.md 或派令之文里提到其名」不算有位。
  丙·章之未走全席：认**第 起用章 及其後**之章（今起用章＝306）。判法：`版本/第N章/_席记.json` 须在，
     且八段（定位／三魂／起草／机闸／读席／修席／极限／案席）逐段有记。
     ★**丙只管新章**：306 以前之章不是这套机制写的，拿它去判是假红（令§十三②）。

【挂账】确有其由而暂不接的，写进 `设定/囤灰挂账.md`，一样一行，**须写明其由与其限（到哪一章之前接上）**。
  挂了账仍印黄，只是不判红——**挂账是欠条，不是赦免**。

【普查（1027·执行之审 #55 #103）】跑得着不等於有用：候修（假红多、慢、败多）、候退（唯自测一路；其名见於「废」而活引寡）、
  档之囤灰（顶层 设定/*.md 无活引、无 glob 之族、末提交逾三十日）——**只报不拦**，候者交大审之器审与总编辑之裁。

用法：
    python3 工具/囤灰闸.py            # 全查
    python3 工具/囤灰闸.py --普查      # 候修／候退／档之囤灰（只报）
    python3 工具/囤灰闸.py --自测      # 负测
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import os
import re
import sys
import glob
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
起用章 = 306


def 诸段():
    """★★2026-09-09·作者令「确保这些机制能运营起来」之下所改·**本闸自己就是那一件生锈的**：
      本闸立日（0908）把八段写死在码里；同日本坐把 `一章.js` 由八段扩到十一段
      （加三庭·五庭·封版），**而本闸照旧只查八段——新造的三段，当天就没人守了。**
    ★**其病之形，正是作者所指的那一样**：「不断更新去修改机制……到最后都同归没有运营」。
    ★★**故改：段名不写在本闸里，当场自 `工具/席/一章.js` 之 meta.phases 读**——
      **流水线加一段，本闸下一次跑就认得它；再也生不出这种锈。**
    ★★★读不着即判红（不许「读不着就放行」——那等於把闸关了）。"""
    # ★1017 淘汰之律（X28）：一章.js 已彻删——一代之段冻存於 造式.py（只供复核已封之旧章）
    m = _造式模()
    return list(m.一代之段) if m is not None else None
def _造式模():
    try:
        import importlib.util as _u
        _sp = _u.spec_from_file_location('_zaoshi_dust', os.path.join(os.path.dirname(os.path.abspath(__file__)), '造式.py'))
        _m = _u.module_from_spec(_sp)
        _sp.loader.exec_module(_m)
        return _m
    except Exception:
        return None


def _造式(n):
    """本章是不是造式之章（`版本/第N章/_式.md`·判在 工具/造式.py）。读不出判据而挂着 `_式.md` 者亦认作造式——
    其段读不出即红，⛔不许借此退回常式之段。"""
    if not os.path.exists(os.path.join(ROOT, '版本', '第%d章' % n, '_式.md')):
        return False
    m = _造式模()
    return True if m is None else m.是造式(n, ROOT)


def _造式之段(n=None):
    """n 给出者：二代之章（_式.md 书「造式二代」）读 造章.js 之段（1013），一代之章读 一章.js。"""
    m = _造式模()
    return m.造式之段(ROOT, n) if m is not None else None


真跑口 = ['工具/全测.py', '工具/起草闸.py', '工具/大审.py', '工具/书级体检.py', '工具/跑轮.py',
          '工具/自走.py', '工具/封版.py', '工具/接棒守.py']      # ★1027：一坐、回修、十轮精进 随十三轮汰；添流之三口


def _读(p):
    try:
        with open(os.path.join(ROOT, p), encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception:
        return ''


_汉 = '零一二三四五六七八九'


def _汉数(n):
    """章号转汉字（与本书档名同式：第二百七十三章）。"""
    if n < 10:
        return _汉[n]
    if n < 20:
        return '十' + (_汉[n % 10] if n % 10 else '')
    if n < 100:
        return _汉[n // 10] + '十' + (_汉[n % 10] if n % 10 else '')
    s = _汉[n // 100] + '百'
    r = n % 100
    if r == 0:
        return s
    if r < 10:
        return s + '零' + _汉[r]
    return s + _汉數_十(r)


def _汉數_十(r):
    return ('十' if r < 20 else _汉[r // 10] + '十') + (_汉[r % 10] if r % 10 else '')


def 正文在(n):
    return bool(glob.glob(os.path.join(ROOT, '正文', '*第%s章_*.md' % _汉数(n))))


def _汉转数(s):
    """★「三百一十」「三百九十七」「四十」→ 整数（只认零〇一至九、十、百、千）。"""
    值 = {'零': 0, '〇': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    位 = {'十': 10, '百': 100, '千': 1000}
    总, 数 = 0, 0
    for c in s:
        if c in 值:
            数 = 值[c]
        elif c in 位:
            总 += (数 or 1) * 位[c]
            数 = 0
        else:
            return None
    return 总 + 数


def 末章():
    """★盘上正文之末章——逐档读其名之章号取最大（⛔借 正文在()：其 _汉数 把 310—319 写作「三百十」，认不得「三百一十」）。"""
    诸 = [_汉转数(m.group(1)) for f in glob.glob(os.path.join(ROOT, '正文', '*.md'))
          for m in [re.search(r'第([零〇一二两三四五六七八九十百千]+)章', os.path.basename(f))] if m]
    return max([x for x in 诸 if x] or [0])


def 席表(用法):
    """★`工具/席/用法.md`「诸席之位与末用」表 → {席名: (其位, 末用, 限章或 None)}。限之格无章号（如「—（自走派）」）返 None——
    只派令之席许如此；余席限为 None 即红（见 席之判·1020 X29）。"""
    出 = {}
    for l in 用法.split('\n'):
        m = re.match(r'\s*\|\s*`?([^|`\s]+\.js)`?\s*\|([^|]*)\|([^|]*)\|([^|]*)\|', l)
        if m:
            限 = re.search(r'\d+', m.group(4))
            出[m.group(1)] = (m.group(2).strip(), m.group(3).strip(), int(限.group()) if 限 else None)
    return 出


def _串终(文, i):
    """单引、双引之串（自 i 之引号起）→ 其终之後一位；⛔跨行（失步之害只到行尾）。"""
    q, j, n = 文[i], i + 1, len(文)
    while j < n and 文[j] != q and 文[j] != '\n':
        j += 2 if 文[j] == '\\' else 1
    return j + 1 if j < n and 文[j] == q else j


def _模终(文, i):
    """JS 模板之串（i 在开头反引号之後）→ 其终之後一位；`${…}` 里之码（含嵌套之模板）照括号深浅走过。"""
    n = len(文)
    while i < n:
        if 文[i] == '\\':
            i += 2
        elif 文[i] == '`':
            return i + 1
        elif 文.startswith('${', i):
            i, 深 = i + 2, 0
            while i < n:
                c = 文[i]
                if c in '"\'':
                    i = _串终(文, i)
                    continue
                if c == '`':
                    i = _模终(文, i + 1)
                    continue
                if c == '{':
                    深 += 1
                elif c == '}':
                    if 深 == 0:
                        break
                    深 -= 1
                i += 1
            i += 1
        else:
            i += 1
    return n


def _去注(文, 语=None):
    """★W60·X33⑥：剔注，留码与串——整行注与**行尾注**、**`/* */` 块注**、**Python 之 docstring**（行首起之三引号串）。
    语＝'py'：`#` 注、三引号串；'js'：`//`、`/* */` 注、反引号模板（`${}` 嵌套）、正则之字面；None（片段）：二家俱认。
    ⛔串里之 `#`、`//`、`/*`（如 `'工具/席/*.js'`、所印命令行尾之 `# …`）不作注——派令本在串里（`L.append("  Workflow({scriptPath:…})")`）。
    单引、双引之串⛔跨行：引号失步之害只到行尾。"""
    py, js = 语 in ('py', None), 语 in ('js', None)
    出, i, n, 前 = [], 0, len(文), ''
    while i < n:
        c = 文[i]
        if py and 文.startswith(('"""', "\'\'\'"), i):
            j = 文.find(文[i:i + 3], i + 3)
            j = n if j < 0 else j + 3
            if 文[文.rfind('\n', 0, i) + 1:i].strip().lower().strip('rbuf'):
                出.append(文[i:j])                                  # 码中之三引号串（赋值、传参）：留
            else:
                出.append('\n' * 文.count('\n', i, j))           # 行首之三引号串＝docstring：剔（留行数）
            i, 前 = j, '"'
        elif c in '"\'':
            j = _串终(文, i)
            出.append(文[i:j])
            i, 前 = j, c
        elif js and c == '`':
            j = _模终(文, i + 1)
            出.append(文[i:j])
            i, 前 = j, c
        elif (py and c == '#') or (js and 文.startswith('//', i)):
            j = 文.find('\n', i)
            i = n if j < 0 else j
        elif js and 文.startswith('/*', i):
            j = 文.find('*/', i + 2)
            j = n if j < 0 else j + 2
            出.append('\n' * 文.count('\n', i, j))
            i = j
        elif js and c == '/' and 前 in '(,=:[!&|?{};':
            m = re.compile(r'/(?:\\.|\[(?:\\.|[^\]\\\n])*\]|[^/\\\n\[])+/[a-z]*').match(文, i)   # 正则之字面：其中之引号、// ⛔认
            j = m.end() if m else i + 1
            出.append(文[i:j])
            i, 前 = j, '/'
        else:
            出.append(c)
            if not c.isspace():
                前 = c
            i += 1
    return ''.join(出)


def 派令之席(派令之文):
    """★派令之文里**真被调**之席名集（1020 X29 再治）：只认 `scriptPath:'工具/席/<名>.js'`（容一个反斜杠转义——
    与 `自走.py` ⑬之八 `_死席` 同一把尺），且**注不算**：整行注、行尾注、`/* */` 块注、docstring（W60·X33⑥·见 `_去注`）；
    **子目录之派令**（`工具/席/_旧/X.js`）不算顶层之 X.js 有路（旧取 basename 而混同·W60·X33⑥）。
    ⛔只提其名（「一代在 工具/席/一章.js」之注、自测之串 `工具/席/救章.js`）不是派令——旧式子串之判凭此把已彻删之席判作有路。
    派令之文：一串（片段·二家之注俱认），或诸档之列——其项为串，或 (档名, 文)（照其扩展名定 py／js，逐档剔注）。"""
    return {p[len('工具/席/'):] for p in 派令之路(派令之文) if '/' not in p[len('工具/席/'):]}


def 派令之路(派令之文):
    """★X43⑤：派令之文里真被调之席之**全路**集（'工具/席/X.js'、子目录者 '工具/席/_旧/Y.js' 亦在）——派令之席（顶层之名）与
    `自走.py` ⑬之八 `_死席`（盘上不在之路）同出此一尺（⛔两抄：旧 _死席 自抄一正则而不剔注，注里之 scriptPath 亦算派令）。"""
    诸 = [派令之文] if isinstance(派令之文, str) else list(派令之文)
    出 = set()
    for x in 诸:
        名, 文 = x if isinstance(x, tuple) else ('', x)
        语 = 'py' if 名.endswith('.py') else 'js' if 名.endswith('.js') else None
        出 |= {'工具/席/' + p for p in re.findall(r"scriptPath:\\?'工具/席/([^'\\]+\.js)", _去注(文, 语))}
    return 出


def _派令之档():
    """派令之文＝造章.js、自走.py——逐档带名（照扩展名剔其家之注）。"""
    return [(p, _读(p)) for p in ('工具/席/造章.js', '工具/自走.py')]


def 席之判(席们, 派令之文, 用法, 末):
    """★乙·席之囤灰（1020 X29 改）→ [(席, 其由)]。
    ⛔旧式：席名「在 造章.js 或 用法.md 里出现」即算有位——**一代五席（读席／案席／连贯席／一路／救章）
      其调者早删、二代一回未派，只凭 用法.md 里一段旧说明，多留了十几章，本闸一声不吭**（1017 X29 之普查方逮）。
    ★今：①派令之文（造章.js、自走.py）以 `scriptPath:'工具/席/<名>'` 调者即有路（见 派令之席；⛔只提其名、注行不算）；
      ②余者须在「诸席之位与末用」表有其行（其位·末用·限），且**限系於末用**：末用格以章号起、末用 ≤ 末章、
        限写章号且 ≤ 末用＋30（⛔手填远限、⛔「—」充限）；③末章 ≥ 限 → 红：接上（改其位、更其末用与限），或彻删（铁律④⑤）。"""
    表 = 席表(用法)
    派 = 派令之席(派令之文)
    出 = []
    for s in 席们:
        if s in 派:
            continue
        if s not in 表:
            出.append((s, '无派令之路（造章.js、自走.py 无 scriptPath 调之），亦不在 用法.md「诸席之位与末用」表——'
                          '补其行（其位·末用·限），或彻删。'))
            continue
        末用 = re.match(r'\s*(\d+)', 表[s][1])
        限 = 表[s][2]
        if 末用 is None or 限 is None:
            出.append((s, '无派令之路，而表行之%s无章号（末用「%s」）——末用须以章号起、限＝末用＋30 写章号（⛔「—」只许派令之席）。'
                          % ('末用' if 末用 is None else '限', 表[s][1])))
        elif int(末用.group(1)) > 末:
            出.append((s, '无派令之路，末用 %s 在末章 %d 之後——末用须是真用之章。' % (末用.group(1), 末)))
        elif 限 > int(末用.group(1)) + 30:
            出.append((s, '无派令之路，限 %d 逾 末用 %s＋30——限系於末用（⛔手填远限）。' % (限, 末用.group(1))))
        elif 末 >= 限:
            出.append((s, '无派令之路，末用 %s，限 %d 已到（末章 %d）——三十章未用：接上（改其位、更其末用与限），或彻删（铁律④⑤·X29）。'
                          % (表[s][1], 限, 末)))
    return 出


def _挂账():
    """返 {名: 其由}。挂账须一行写全：`· 名 —— 其由（限：…）`。"""
    out = {}
    for line in _读('设定/囤灰挂账.md').split('\n'):
        m = re.match(r'\s*[·*-]\s*(\S+?)\s*(?:——|--)\s*(.+)', line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def 器之闭包(runners=None):
    """自真跑口逐层展开引用闭包，返 (跑得着集, 器全集)。"""
    tools = [os.path.basename(f) for f in glob.glob(os.path.join(ROOT, '工具', '*.py'))]
    起 = list(真跑口 if runners is None else runners)
    if runners is None:
        # ★席与钩子只在「全查」时算真跑口；负测明给 runners 时不许再添，
        #   否则闭包永远展得开，那一格就是死的（§二十八·活数钉成常数）。
        起 += [os.path.relpath(f, ROOT) for f in glob.glob(os.path.join(ROOT, '工具', '席', '*.js'))]
        起 += [os.path.relpath(f, ROOT) for f in glob.glob(os.path.join(ROOT, '工具', 'githooks', '*'))]
        # ★2026-09-16 补·**`.claude/settings.json` 之钩亦係真跑口**：
        #   ⛔**其实**：`工具/席在跑吗.py` 自 0915 立起即被本闸与 `对位.py` 判作孤器，
        #     三章之案席逐章报「⛔不为它绿而改器一行」——**那一条戒是对的，而这一处不是「为它绿」**：
        #     **那只器真有人跑**，其跑口逐字在 `.claude/settings.json` 第10行之 Stop 钩
        #     （`cd /home/user/the-novel && python3 工具/席在跑吗.py`），**每一回合收尾时真跑一遍**。
        #   ★**本闸本已认 `工具/githooks/*`（git 之钩）为真跑口**——
        #     **`.claude` 之钩与它是同一类东西，只是挂在另一个壳上**；**认前者不认後者，是本闸漏了一处，不是那只器囤了灰。**
        #   ⛔**而其限不许放宽半分**：**只添这一个档作起点，一个新豁免也没有开**；
        #     **凡一件器在诸跑口、诸席、二钩之内一处也提不着者，照旧红**（自测⑥钉死）。
        起 += [f for f in ['.claude/settings.json'] if os.path.isfile(os.path.join(ROOT, f))]
    起 = [p for p in 起 if os.path.isfile(os.path.join(ROOT, p))]
    reach = set(os.path.basename(p) for p in 起 if p.endswith('.py'))
    work = list(起)
    while work:
        s = _读(work.pop())
        for t in tools:
            if t in s and t not in reach:
                reach.add(t)
                work.append('工具/' + t)
    return reach, set(tools)


def 查(印=True):
    """返 (红条列, 黄条列)。"""
    红, 黄 = [], []
    账 = _挂账()

    # 甲·器
    reach, tools = 器之闭包()
    灰 = sorted(tools - reach)
    for t in 灰:
        (黄 if t in 账 else 红).append(
            '甲·器囤灰：工具/%s 自诸真跑口展不到——造了没人跑。%s' %
            (t, ('已挂账：' + 账[t]) if t in 账 else '接进某个跑口，或写进 设定/囤灰挂账.md'))

    # 乙·席（1020 X29：派令之路＝造章.js、自走.py 之 scriptPath；余者须在 用法.md「诸席之位与末用」表有行、限系於末用且未到——见 席之判）
    席们 = sorted(os.path.basename(f) for f in glob.glob(os.path.join(ROOT, '工具', '席', '*.js')))
    for s, 语 in 席之判(席们, _派令之档(), _读('工具/席/用法.md'), 末章()):
        (黄 if s in 账 else 红).append('乙·席囤灰：工具/席/%s %s%s' % (
            s, 语, ('　已挂账：' + 账[s]) if s in 账 else ''))

    # 乙之二·席之 schema 键须尽是 ASCII
    # ★其立之由（0908·本坐亲犯）：`一章.js` 之 schema 用了中文键，工作流一起手即
    #   `400 input_schema.properties: Property keys should match pattern '^[a-zA-Z0-9_.-]{1,64}$'`，
    #   **六个 agent 全崩、一章未写**。这是一条判得死的（正则一跑即知），故做成闸。
    for f in sorted(glob.glob(os.path.join(ROOT, '工具', '席', '*.js'))):
        文 = _读(os.path.relpath(f, ROOT))
        坏 = sorted(set(re.findall(r'([^\x00-\x7F][^\s:]*)\s*:\s*\{\s*type:', 文)))
        if 坏:
            红.append('乙之二·%s 之 schema 键非 ASCII：%s——工作流会当场 400，一个 agent 也起不来。'
                      % (os.path.basename(f), '／'.join(坏[:6])))

    # 丙·章
    for d in sorted(glob.glob(os.path.join(ROOT, '版本', '第*章'))):
        m = re.search(r'第(\d+)章', os.path.basename(d))
        if not m or int(m.group(1)) < 起用章:
            continue
        n = int(m.group(1))
        # ★丙只判「正文已在」之章：开了镜卡而未起草者不是囤灰，判它是假红（令§十三②）。
        if not 正文在(n):
            continue
        p = os.path.join(d, '_席记.json')
        if not os.path.isfile(p):
            红.append('丙·第%d章无 _席记.json——这一章没走八席（起用章＝%d）。' % (n, 起用章))
            continue
        try:
            j = json.load(open(p, encoding='utf-8'))
        except Exception as e:
            红.append('丙·第%d章 _席记.json 读不动：%s' % (n, e))
            continue
        # ★2026-10-08·造式之章（`版本/第N章/_式.md`·判在 `工具/造式.py`）：⛔无三庭／五庭／读席／修席／极限诸段，
        #   其席记照**造式之段**验（当场自 `一章.js` 之 `const 造式之段` 读——与 meta.phases 同律：段名不写死在本闸）。
        #   ⛔非豁免：造式之段一段不许缺；读不出造式之段即红（不许读不出就放行）。
        if _造式(n):
            段 = _造式之段(n)
            if not 段:
                红.append('丙·第%d章係造式之章，而读不出其席档（一章.js／造章.js）之 const 造式之段——**段名之源断了**（一代之段冻存於 造式.py）。' % n)
                continue
        else:
            段 = 诸段()
        if not 段:
            红.append('丙·读不出冻存之一代之段（造式.py）——**段名之源断了，本闸整条丙路即成空转**。')
            continue
        缺 = [x for x in 段 if x not in (j.get('段') or {})]
        if 缺:
            红.append('丙·第%d章席记缺段：%s' % (n, '／'.join(缺)))

    if 印:
        print('════ 囤灰闸 ════')
        print('  甲·器 %d 样，跑得着 %d，囤灰 %d' % (len(tools), len(reach), len(灰)))
        print('  乙·席 %d 张（派令之路 %d 张，余照 用法.md 之表）' % (
            len(席们), len(set(席们) & 派令之席(_派令之档()))))
        新章 = [d for d in glob.glob(os.path.join(ROOT, '版本', '第*章'))
                if re.search(r'第(\d+)章', os.path.basename(d))
                and int(re.search(r'第(\d+)章', os.path.basename(d)).group(1)) >= 起用章]
        print('  丙·起用章 %d 及其後之章 %d 部' % (起用章, len(新章)))
        for x in 黄:
            print('  ⚠ ' + x)
        for x in 红:
            print('  ⛔ ' + x)
        print('  ✓ 无囤灰。' if not 红 else '  ⛔ 囤灰 %d 件。' % len(红))
    return 红, 黄


# ═══ 负测（令§六③：改闸必同日负测，且须旧式回灌） ═══
def 自测():
    """★负测之要：每一格都要**咬得住一个真的旧局**，不许拿常数钉死（§二十八）。"""
    global ROOT   # ⑫ 一格须换仓根作局（跑毕复位）
    ok, bad = 0, []

    def T(name, cond, note=''):
        nonlocal ok
        if cond:
            ok += 1
        else:
            bad.append(name + ('（%s）' % note if note else ''))

    # ①今日之局：全查须绿（这一格是活的——仓里真有囤灰它就红）
    红, _ = 查(印=False)
    T('①今局无囤灰', not 红, '；'.join(红[:3]))

    # ②旧式回灌·器：把真跑口砍成一个**叶器**（字数闸——它谁也不引），闭包须当场塌下来。
    # ★这一格两头皆活（§二十八：不许把活数钉成常数）：
    #   拿「全跑口之闭包」减「叶器之闭包」，其差须 ≥50——两个数都是当场算的，
    #   日后添器减器它自己跟着走，钉不死也洗不白。
    # ★★为什么不拿「跑轮.py」当叶器：跑轮.py 的头注里提了全测.py，闭包一层就展满了（实测囤灰 0）——
    #   **那样这一格就是死的，而它会天天印绿**。这一处是本器立日亲手逮出来的，记此备忘。
    reach全, tools全 = 器之闭包()
    reach叶, tools叶 = 器之闭包(runners=['工具/字数闸.py'])
    差 = len(reach全) - len(reach叶)
    T('②叶器闭包须比全跑口闭包小 ≥50（今：%d − %d）' % (len(reach全), len(reach叶)), 差 >= 50,
      '实差 %d' % 差)

    # ③器之全集须＝工具/*.py 之数（防它悄悄只认一部分）
    真数 = len(glob.glob(os.path.join(ROOT, '工具', '*.py')))
    T('③器全集＝工具/*.py 之数 %d' % 真数, len(tools全) == 真数, '实认 %d' % len(tools全))

    # ④挂账须读得出（拿一行假账灌进去验其正则）
    m = re.match(r'\s*[·*-]\s*(\S+?)\s*(?:——|--)\s*(.+)', '· 某器.py —— 其由（限：第 999 章前接上）')
    # ⑦★2026-09-16 立：**`.claude/settings.json` 之钩係真跑口，而真孤器照旧红**
    #   ⛔其所由来：`工具/席在跑吗.py` 三章被判孤器，而它真有人跑——
    #   其跑口在 `.claude/settings.json` 第10行之 Stop 钩，**每一回合收尾时真跑一遍**；
    #   本闸本已认 `工具/githooks/*`，**`.claude` 之钩与它同类，只是挂在另一个壳上**。
    _reach7, _tools7 = 器之闭包()
    T('⑦席在跑吗.py 今自 .claude 之钩展得着', '席在跑吗.py' in _reach7)
    # ⑦之二⛔**而一个谁也没提过的器照旧展不着**——**只添一个起点，一个豁免也没有开**
    # ⛔**其名须当场拼出来，不许在本档里写成一个整串**：
    #   ⭑本坐头一版把那个样器之名整串写在此处（连注里那一处也算），**而本档自己就在闭包之内**——
    #   **那一串一写下去，样器当场就「被人提过」了，於是本格自己把自己证伪。**
    #   ★**与 `chk_wuzha` 之假红同族**：**器自己的文字，也是它所量的那一片盘的一部分。**
    _名 = '_负测' + '孤器' + '样.py'
    _样 = os.path.join(ROOT, '工具', _名)
    try:
        with open(_样, 'w', encoding='utf-8') as _f:
            _f.write('# 无人提及之器\n')
        _r7, _t7 = 器之闭包()
        T('⑦之二 真孤器照旧展不着（只添起点，未开豁免）', _名 not in _r7)
    finally:
        if os.path.exists(_样):
            os.remove(_样)
    # ⑦之三⛔**其起点须係一个真在盘上的档**（不在即不添，免得凭空多一个起点）
    _src7 = open(os.path.join(ROOT, '工具', '囤灰闸.py'), encoding='utf-8').read()
    T('⑦之三 其起点带 os.path.isfile 之验', "'.claude/settings.json'] if os.path.isfile" in _src7)

    T('④挂账一行读得出', bool(m) and m.group(1) == '某器.py')

    # ⑤丙只管起用章及其後（拿一个旧章号验其不判）
    T('⑤起用章之界在 306', 起用章 == 306)

    # ⑥段名须当场自 一章.js 读出，且其数须与 js 里 title: 之数相同（防只读到前几个）
    段 = 诸段()
    _m = _造式模()
    T('⑥段名读得出（今 %s 段）' % (len(段) if 段 else '读不出'), bool(段) and len(段) >= 8,
      str(段))
    T('⑥之二 段名与冻存之一代之段同（造式.py·X28）', bool(段) and _m is not None and 段 == list(_m.一代之段))
    # ⑥之三·**这一格是本闸生锈那一回的负测**：若把段名钉回旧式八段，
    #   而 js 已是十一段，则「钉死」之式认不出新加的三段——须当场看得出其差。
    旧八 = ['定位', '三魂', '起草', '机闸', '读席', '修席', '极限', '案席']
    T('⑥之三 今之段数已多於旧钉之八段（钉死即生锈之凭）',
      bool(段) and len(段) > len(旧八), '今 %s' % (len(段) if 段 else '?'))

    # ⑦席之全集非空（防 glob 写错路而一律绿）
    T('⑦席读得着', os.path.join(ROOT, '工具', '席', '造章.js') in glob.glob(os.path.join(ROOT, '工具', '席', '*.js')))   # ★409 囤灰四席彻删：⛔以份数为底

    # ⑧旧式回灌·席：拿一个派令之文与 用法.md 俱无之席名，须判红（1020 X29：真调 席之判，⛔只验「字不在档里」）
    _派 = _读('工具/席/造章.js') + _读('工具/自走.py')
    _用 = _读('工具/席/用法.md')
    T('⑧未挂之席须判红', [x[0] for x in 席之判(['无此席.js'], _派, _用, 末章())] == ['无此席.js'])
    # ⑧之四【X29 回灌旧病】旧 用法.md 之式——只一段说明提到其名（0908 之「读席」节逐字）、表里无行：
    #   旧式（名在 用法.md 即算有位）判绿，一代五席即凭此多留十几章；今须判红。
    _旧用 = ('## 一·`读席.js` —— 只读白文，判落到拍号（**不改一字**）\n'
            "用法：`Workflow({scriptPath:'工具/席/读席.js', args:[184,188,191]})`\n")
    T('⑧之四 X29 回灌：只在 用法.md 说明里提其名、表里无行者须红（旧式判绿）',
      '读席.js' in _旧用 and [x[0] for x in 席之判(['读席.js'], _派, _旧用, 397)] == ['读席.js'])
    # ⑧之五 限到即红、未到不红（限＝末用＋30）
    _表 = '| 席 | 其位 | 末用 | 限 |\n|---|---|---|---|\n| 某席.js | 无派令之路 | 379（某事） | 409 |\n'
    T('⑧之五 无派令之路者限到（末章≥限）即红、未到不红',
      len(席之判(['某席.js'], '', _表, 409)) == 1 and 席之判(['某席.js'], '', _表, 408) == [])
    # ⑧之六 派令之文里以 scriptPath 调者有路，不须表行（转义之式 \' 亦认）
    T('⑧之六 自走所派之席（scriptPath，含 \\\' 转义之式）不须表行',
      席之判(['大审.js'], "Workflow({scriptPath:'工具/席/大审.js'", '', 9999) == []
      and 席之判(['剧情庭.js'], "L.append('  Workflow({scriptPath:\\'工具/席/剧情庭.js\\', args:{}})')", '', 9999) == [])
    # ⑧之七 今仓之表读得出（无派令之路之席逐张有行、各带限）；造章.js 由 自走 之 scriptPath 认得（⛔再特判其名）
    _实 = 席表(_用)
    _今派 = 派令之席(_派)
    _无路 = [s for s in sorted(os.path.basename(f) for f in glob.glob(os.path.join(ROOT, '工具', '席', '*.js')))
            if s not in _今派]
    T('⑧之七 今仓无派令之路之席（%d 张）逐张在表、各带限；造章／大审／剧情庭 认作派令' % len(_无路),
      all(s in _实 and _实[s][2] for s in _无路)   # ★409 囤灰四席彻删後无路之席可为零（其判由 ⑧之五、⑧之十 之样本守）
      and {'造章.js', '大审.js', '剧情庭.js'} <= _今派, str(_无路) + '｜派 ' + str(sorted(_今派)))
    # ⑧之九【X29 再治·回灌旧病】旧式「名在派令之文即有路」（子串之判）：已彻删之 救章.js（自走 ⑬之八 自测之串）、
    #   一章.js（造章.js 之注、自走之说明）复立於盘，旧判绿；今须红。另以注、串、注行之 scriptPath 各灌一回。
    #   ★今之派令之文之後，另接 1020 盘上二行之逐字（造章.js:14 之注、自走 ⑬之八 之串）——他日其行改去，本格不假红。
    _旧判 = lambda s, 派: s in 派
    _派9 = (_派 + '\n// ═══ 造式二代（1013 依 设定/方法升级_造式二代.md 立；一代在 工具/席/一章.js，留作退路——⛔往一章.js 添式）═══\n'
           + '    _旧行 = "L.append(\'     Workflow({scriptPath:\\\\\'工具/席/救章.js\\\\\', args:{章:%d}})\' % 末)"\n')
    T('⑧之九 X29 回灌：救章.js、一章.js 只凭注与串提其名——旧式判绿，今须红',
      _旧判('救章.js', _派9) and _旧判('一章.js', _派9)
      and [x[0] for x in 席之判(['救章.js', '一章.js'], _派, _用, 末章())] == ['救章.js', '一章.js']
      and [x[0] for x in 席之判(['救章.js', '一章.js'], _派9, _用, 末章())] == ['救章.js', '一章.js'])
    T('⑧之九之二 注里、串里只提其名者红；注行里之 scriptPath 亦红；码行之 scriptPath 绿',
      席之判(['某席.js'], '// 一代在 工具/席/某席.js，留作退路\n', '', 1) != []
      and 席之判(['某席.js'], "_旧 = '工具/席/某席.js'\n", '', 1) != []
      and 席之判(['某席.js'], "    # Workflow({scriptPath:'工具/席/某席.js'})\n", '', 1) != []
      and 席之判(['某席.js'], "    L.append(\"Workflow({scriptPath:'工具/席/某席.js'})\")\n", '', 1) == [])
    # ⑧之十【X29 再治】限系於末用：手填远限（999）、「—」充限、末用逾末章、末用无章号——俱红；限＝末用＋30 而未到者绿
    _行 = lambda 末用, 限: '| 某席.js | x | %s | %s |\n' % (末用, 限)
    T('⑧之十 限系於末用：远限、「—」、末用逾末章、末用无章号俱红；合律且未到者绿',
      席之判(['某席.js'], '', _行('379', '999'), 500) != []
      and 席之判(['某席.js'], '', _行('379', '—（自走派）'), 500) != []
      and 席之判(['某席.js'], '', _行('600', '630'), 500) != []
      and 席之判(['某席.js'], '', _行('立後未用', '409'), 400) != []
      and 席之判(['某席.js'], '', _行('379（某事）', '409'), 400) == []
      and 席之判(['某席.js'], '', _行('390', '400'), 399) == [])
    # ⑧之十一【W60·X33⑥·W53 验席之攻（scratchpad W53验_G5/r2/攻.py）逐式回灌】行尾注（# 与 //）、docstring 内、
    #   JS 块注内、子目录之派令——旧判（只滤整行注、取 basename）俱绿；今须红。
    _攻 = {'行尾 # 注': "foo()  # Workflow({scriptPath:'工具/席/X.js'})\n",
          '行尾 // 注': "foo();  // Workflow({scriptPath:'工具/席/X.js'})\n",
          'docstring 内': '"""\n  说明：旧时 Workflow({scriptPath:\'工具/席/X.js\'})\n"""\n',
          '块注内': "/*\n Workflow({scriptPath:'工具/席/X.js'})\n*/\n",
          '子目录': "Workflow({scriptPath:'工具/席/_旧/X.js'})\n"}
    _旧派 = lambda 文: set(os.path.basename(p) for p in re.findall(
        r"scriptPath:\\?'(工具/席/[^'\\]+\.js)", '\n'.join(l for l in 文.split('\n') if not l.lstrip().startswith(('#', '//')))))
    T('⑧之十一 行尾注、docstring、块注、子目录之派令——旧判俱绿，今俱红',
      all('X.js' in _旧派(v) for v in _攻.values())
      and [k for k, v in _攻.items() if 席之判(['X.js'], v, '', 1) == []] == [],
      '今判绿者：%s' % [k for k, v in _攻.items() if 席之判(['X.js'], v, '', 1) == []])
    # ⑧之十一之二 不放松：串里之 # 、//、/*（所印命令之行尾注、glob 之 '工具/席/*.js'）⛔作注而吞掉其後之真派令；
    #   块注、docstring 之後之码行照认；模板嵌套（`${…`…`…}`）与正则之字面不使引号失步；逐档带名（py／js）与片段同判
    _真 = ("    _诸 = glob.glob('工具/席/*.js')   # 席之全集\n"
           "    L.append(\"  Workflow({scriptPath:'%s'})   # 承.py 所写之包裹\" % p)\n"
           "    L.append(\"  Workflow({scriptPath:'工具/席/甲席.js', args:{}})   # 每章\")\n"
           '    """说明：Workflow({scriptPath:\'工具/席/丁席.js\'})"""\n'
           "    L.append('  Workflow({scriptPath:\\'工具/席/乙席.js\\', args:{}})')\n")
    _js = ("const 令 = `${N >= 398 ? `【落笔】# 一节 // 非注 ${x.名}` : ''}` + 'a'   // 行尾之注\n"
           "const 正 = /'\"`/.test(s) || /\\/\\//.test(s)\n"
           "/* 块注 Workflow({scriptPath:'工具/席/丁席.js'}) */\n"
           "Workflow({scriptPath:'工具/席/丙席.js', args:{}})\n")
    T('⑧之十一之二 串里之 #／//／/* ⛔吞真派令；docstring、块注照剔；模板嵌套与正则不失步；逐档与片段同判',
      派令之席(_真) == {'甲席.js', '乙席.js'} and 派令之席([('x.py', _真)]) == {'甲席.js', '乙席.js'}
      and 派令之席([('x.js', _js)]) == {'丙席.js'} and 派令之席(_js) == {'丙席.js'}
      and 派令之席(_派令之档()) == 派令之席(_派),
      '%s｜%s｜%s' % (sorted(派令之席(_真)), sorted(派令之席([('x.js', _js)])), sorted(派令之席(_js))))
    # ⑧之八 末章读得出（限之判赖之）：认得「三百一十」（⛔「三百十」），且今末章 ≥ 起用章
    T('⑧之八 末章读得出（今 %d）、「三百一十」认作 310' % 末章(),
      末章() >= 起用章 and _汉转数('三百一十') == 310 and _汉转数('三百九十七') == 397)

    # ⑧之二·旧式回灌·schema 键：拿一段中文键之 schema 灌进正则，须逮出
    坏 = re.findall(r'([^\x00-\x7F][^\s:]*)\s*:\s*\{\s*type:', '  锁定行: { type: \'string\' },')
    T('⑧之二 中文 schema 键逮得出', 坏 == ['锁定行'], '实逮 %s' % 坏)

    # ⑧之三·今日之席无中文 schema 键（活格：真有就红）
    T('⑧之三 今日诸席之 schema 键尽是 ASCII',
      not any('schema 键非 ASCII' in x for x in 查(印=False)[0]))

    # ⑨正文在()须认得出真章（拿三个真章号验；认不出则丙整条是死的）
    T('⑨正文在()认得出 273／305／1', 正文在(273) and 正文在(305) and 正文在(1))

    # ⑩旧式回灌·丙：本仓今有「版本/第306章」而无正文，丙不许判它红
    T('⑩无正文之新章不判红',
      not any('第306章无 _席记' in x for x in 查(印=False)[0]) or 正文在(306))

    # ⑪★2026-10-08·造式之章：其席记照造式之段验（当场自 一章.js 读），常式之章照 meta.phases 验——两头皆活
    _zs = _造式之段()
    T('⑪造式之段读得出（今 %s）' % ('、'.join(_zs) if _zs else '读不出'), bool(_zs) and len(_zs) >= 6)
    T('⑪之二 造式之段与冻存之一代造式之段同', bool(_zs) and _m is not None and _zs == list(_m.一代造式之段))
    T('⑪之三 造式之段不含审改诸段（三庭／五庭／修席／极限）',
      bool(_zs) and not any(x in _zs for x in ('三庭', '五庭', '修席', '极限')))
    _R0 = ROOT
    import tempfile as _tf, shutil as _sh
    _t = _tf.mkdtemp(prefix='囤灰_造式_')
    try:
        for _sub in ('工具/席', '正文'):
            os.makedirs(os.path.join(_t, _sub))
        _d = os.path.join(_t, '版本', '第400章')
        os.makedirs(_d)
        open(os.path.join(_t, '正文', '镇冢秘术_第四百章_测.md'), 'w', encoding='utf-8').write('测\n')
        ROOT = _t
        def _丙红():
            return [x for x in 查(印=False)[0] if x.startswith('丙·第400章')]
        # 造式之章：席记照造式之段写齐 → 丙不红
        open(os.path.join(_d, '_式.md'), 'w', encoding='utf-8').write('式：虫洞（造式·1008）\n')
        json.dump({'章': 400, '段': {k: 'x' for k in (_zs or [])}}, open(os.path.join(_d, '_席记.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        T('⑫造式之章席记照造式之段写齐者，丙不红', not _丙红(), '；'.join(_丙红()))
        # 造式之章缺「验」一段 → 红（⛔非豁免）
        json.dump({'章': 400, '段': {k: 'x' for k in (_zs or []) if k != '验'}}, open(os.path.join(_d, '_席记.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        T('⑫之二 造式之章缺「验」一段者红', any('验' in x for x in _丙红()))
        # 同一份造式之席记而无 _式.md → 照 meta.phases 验，缺三庭等即红（不挂牌不许用造式之段）
        json.dump({'章': 400, '段': {k: 'x' for k in (_zs or [])}}, open(os.path.join(_d, '_席记.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        os.remove(os.path.join(_d, '_式.md'))
        T('⑫之三 无 _式.md 者照常式之段验（缺三庭即红）', any('三庭' in x for x in _丙红()))
    finally:
        ROOT = _R0
        _sh.rmtree(_t, ignore_errors=True)

    # ⑬ 器之迹（1015）：窗内之跑、败、重跑认得出，窗外⛔入
    import json as _j
    _行 = [_j.dumps({'t': '2026-10-15T01:00:0%d' % i, '器': '甲.py', '参': ['389'], '秒': 2, 'rc': (1 if i == 0 else 0)}) for i in range(3)]
    _行.append(_j.dumps({'t': '2026-10-16T01:00:00', '器': '乙.py', '参': [], '秒': 1, 'rc': 0}))
    _计 = 迹('2026-10-15T00:00:00', '2026-10-15T23:00:00', 行们=_行)
    if _计.get('甲.py', {}).get('跑') == 3 and _计['甲.py']['败'] == 1 and _计['甲.py'].get('重跑') and '乙.py' not in _计:
        ok += 1
    else:
        bad.append('⑬器之迹之窗、败、重跑')
    for _名, _合 in _普查之测():          # ⑭—⑯ 普查（1027·#55 #103）
        T(_名, _合)
    print('── 负测·囤灰闸 %d/%d %s ──' % (ok, ok + len(bad), '全通' if not bad else '｜未过：' + '；'.join(bad)))
    return not bad


def 迹窗(n, root=None):
    """第 N 章之器之全程之窗：自 版本/第N章/_料.md 之立（章之料成即章起）至本章封版之提交（未封即今）。→ (始 ISO, 至 ISO)"""
    import subprocess, time as _t
    root = root or ROOT
    料 = os.path.join(root, '版本', '第%d章' % n, '_料.md')
    始 = _t.strftime('%Y-%m-%dT%H:%M:%S', _t.gmtime(os.path.getmtime(料))) if os.path.exists(料) else '0000'
    r = subprocess.run(['git', 'log', '-1', '--format=%cI', '--grep', '第%d章《' % n, '--grep', '封版', '--all-match'],
                       cwd=root, capture_output=True, text=True)
    至 = '9999'
    if r.stdout.strip():
        import datetime
        至 = datetime.datetime.fromisoformat(r.stdout.strip()).astimezone(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
    return 始, 至


def 迹(始, 至, root=None, 行们=None):
    """_器之迹.jsonl 里 始—至 之诸跑 → 每器：跑、败（rc 非 0／None）、总秒、最长、同参重跑（同器同参 ≥3 回＝摩擦之疑）"""
    import json as _j
    root = root or ROOT
    if 行们 is None:
        p = os.path.join(root, '_器之迹.jsonl')
        行们 = open(p, encoding='utf-8').read().split('\n') if os.path.exists(p) else []
    计 = {}; 参计 = {}
    for l in 行们:
        try:
            e = _j.loads(l)
        except Exception:
            continue
        if not (始 <= e.get('t', '') <= 至):
            continue
        x = 计.setdefault(e['器'], {'跑': 0, '败': 0, '秒': 0.0, '最长': 0.0, '败例': []})
        x['跑'] += 1; x['秒'] += e.get('秒') or 0; x['最长'] = max(x['最长'], e.get('秒') or 0)
        if e.get('rc') not in (0, None):
            x['败'] += 1
            if len(x['败例']) < 3:
                x['败例'].append('%s %s rc=%s' % (e['t'][11:16], ' '.join(e.get('参') or []), e.get('rc')))
        k = (e['器'], tuple(e.get('参') or []))
        参计[k] = 参计.get(k, 0) + 1
        if e['器'] == '段序之守.py' and str((e.get('参') or [''])[0]).startswith('报：'):   # 〔W921 环4⑥〕过渡之报（rc 0）随章入库
            x.setdefault('报', []).append('%s %s' % (e['t'][5:16].replace('T', ' '), str(e['参'][0])[:200]))
    for (器, 参), c in 参计.items():
        if c >= 3:
            计[器].setdefault('重跑', []).append('%s ×%d' % (' '.join(参) or '（无参）', c))
    return 计


def 迹报(n, 计, 始, 至):
    行 = ['# 器之迹·第%d章（零 token·工具/囤灰闸.py --迹 %d）' % (n, n), '',
         '> 本章从料成到封版（%s — %s，UTC）所跑之器与其表现。败＝退出码非 0（闸之红亦算——须分辨真红、假红）；'
         '重跑＝同器同参 ≥3 回（摩擦之疑：其印不明、或闸反复红）。供复盘与每回大审之器之审。' % (始, 至), '',
         '| 器 | 跑 | 败 | 总秒 | 最长 | 重跑 | 败例 |', '|---|---|---|---|---|---|---|']
    for 器, x in sorted(计.items(), key=lambda kv: (-kv[1]['败'], -kv[1]['秒'])):
        行.append('| %s | %d | %d | %.1f | %.1f | %s | %s |' % (器, x['跑'], x['败'], x['秒'], x['最长'],
                  '；'.join(x.get('重跑', [])), '；'.join(x['败例'])))
    if not 计:
        行.append('| （窗内无迹——_器之迹.jsonl 自 1015 03:20 起记） | | | | | | |')
    报 = [y for x in 计.values() for y in x.get('报', [])]
    if 报:                                       # 〔W921 环4⑥〕段序之守之过渡之报：接棒守 --巡 每巡印末三封之报；三章俱无方转拦
        行 += ['', '## 段序之守之报（W921·甲之验之过渡·rc 0）', ''] + ['- %s' % y for y in 报[:12]]
    return '\n'.join(行) + '\n'


# ═══ 普查（1027·执行之审 #55 #103：「跑得着」不等於「有用」——候修、候退、档之囤灰；只报不拦） ═══
# ★其由：默跑只证跑得着（甲·器 215 样，跑得着 215，囤灰 0），从未判「跑得着而无用」——起草庭之对质、检察官七令俱跑得着而无用，闸照绿。
#   虫洞法典:37、全测之注早书 `--普查`，而器里无此一支（只书无行）。今立之：
#   候修：假红多（_器之账.json 红史）、慢（秒均 ≥ 慢之界；无账则读 设定/全测均秒.json）、败多（_器之迹.jsonl rc 非 0 过半）；
#   候退：①唯自测一路——诸活档（工具/*.py、席 js、钩、.claude、.github，⛔注）引其名者唯 全测 之「--自测」之调（负测_* 本即测，⛔列）；
#         ②其名见於法用册「废」之名而活引 ≤ 2 档（所对质之流程已废，余用待核）；
#   档之囤灰：顶层 设定/*.md，⛔有 glob 读者之族（回执_*、裁_*、冷轮_* 等，当场自器码取其前缀），活档（器、总章、README、圣经、canon）
#         无一字面之引，且末提交逾三十日 → 候汰（canon 旧稿汰前先查圣经是否已收其义；删後入法用册「废」·无档）。
#   ⛔拦：普查只报——候者交大审之器审与总编辑之裁（一席审一席驳），⛔自删。
慢之界 = 30.0          # 秒均 ≥ 此 → 候修·慢
红多之界 = 0.5         # 红／跑 ≥ 此（跑 ≥3）→ 候修·红多
灰之日 = 30            # 档之末提交逾此日 → 档之囤灰


def _活档(root):
    """→ [(相对路, 去注之文)]：工具/*.py、席 js、githooks、.claude/settings.json、.github/workflows。"""
    出 = []
    for g in ('工具/*.py', '工具/席/*.js', '工具/githooks/*', '.github/workflows/*.yml'):
        for f in sorted(glob.glob(os.path.join(root, g))):
            rel = os.path.relpath(f, root).replace(os.sep, '/')
            try:
                文 = open(f, encoding='utf-8', errors='ignore').read()
            except Exception:
                continue
            语 = 'py' if f.endswith('.py') else 'js' if f.endswith('.js') else None
            出.append((rel, _去注(文, 语) if 语 else 文))
    for f in ('.claude/settings.json',):
        if os.path.isfile(os.path.join(root, f)):
            出.append((f, open(os.path.join(root, f), encoding='utf-8', errors='ignore').read()))
    return 出


def _只自测(行们, 名):
    """全测 之文中提 名 之行，俱係「--自测」之调（run(…, ['工具/名', '--自测']) 或 _自测之项(…, '工具/名')）否。"""
    诸 = [l for l in 行们 if 名 in l]
    return bool(诸) and all('--自测' in l or '_自测之项(' in l for l in 诸)


def 候退(root=None, 册=None):
    """→ [(器, 由)]"""
    root = root or ROOT
    活 = _活档(root)
    册 = 册 if 册 is not None else (json.load(open(os.path.join(root, '设定', '法用册.json'), encoding='utf-8'))
                                    if os.path.isfile(os.path.join(root, '设定', '法用册.json')) else {})
    废名 = ['%s %s' % (x.get('名', ''), x.get('id', '')) for x in 册.get('废') or []]
    出 = []
    for f in sorted(glob.glob(os.path.join(root, '工具', '*.py'))):
        名 = os.path.basename(f)
        干 = 名[:-3]
        if 名.startswith(('负测_', '_')) or 名 in ('全测.py', '囤灰闸.py'):
            continue
        式 = re.compile(r'%s|\bimport %s\b|\bfrom %s import' % (re.escape(名), re.escape(干), re.escape(干)))
        引 = [rel for rel, 文 in 活 if rel != '工具/' + 名 and 式.search(文)]
        if 引 == ['工具/全测.py'] and _只自测(dict(活)['工具/全测.py'].split('\n'), 名):
            出.append((名, '唯自测一路：活档引之者只 全测 之「--自测」——其本职一回未跑（造了只验不用）'))
            continue
        废 = [x for x in 废名 if 名 in x]
        if 废 and len(引) <= 2:
            出.append((名, '其名见於法用册「废」（%s）而活引只 %d 档（%s）——所对质之流程已废，余用待核' % (废[0][:40], len(引), '、'.join(引) or '无')))
    return 出


def 候修(root=None, 账=None, 均秒=None, 迹行=None):
    """→ [(名, 由)]：_器之账.json（各格之跑、红、秒均）；无账则 设定/全测均秒.json 只判慢；_器之迹.jsonl 之败多。"""
    root = root or ROOT
    if 账 is None:
        p = os.path.join(root, '_器之账.json')
        try:
            账 = json.load(open(p, encoding='utf-8')) if os.path.isfile(p) else {}
        except Exception:
            账 = {}
    if 均秒 is None and not 账:
        p = os.path.join(root, '设定', '全测均秒.json')
        try:
            均秒 = json.load(open(p, encoding='utf-8')) if os.path.isfile(p) else {}
        except Exception:
            均秒 = {}
    出 = []
    for 名, x in sorted((账 or {}).items()):
        if not isinstance(x, dict):
            continue
        跑, 红 = x.get('跑') or 0, x.get('红') or 0
        if 跑 >= 3 and 红 / 跑 >= 红多之界:
            出.append((名, '红多（红 %d／跑 %d）——真红即治其物，假红即治其器' % (红, 跑)))
        if (x.get('秒均') or 0) >= 慢之界:
            出.append((名, '慢（秒均 %.1f）——零 token 而慢者先问能否移 GitHub 或缩其域' % x['秒均']))
    for 名, 秒 in sorted((均秒 or {}).items()):
        if isinstance(秒, (int, float)) and 秒 >= 慢之界:
            出.append((名, '慢（种秒 %.1f）' % 秒))
    if 迹行 is None:
        p = os.path.join(root, '_器之迹.jsonl')
        迹行 = open(p, encoding='utf-8', errors='ignore').read().split('\n') if os.path.isfile(p) else []
    计 = 迹('0000', '9999', root=root, 行们=迹行)
    for 器, x in sorted(计.items()):
        if x['跑'] >= 5 and x['败'] * 2 > x['跑']:
            出.append((器, '败多（迹：败 %d／跑 %d）——%s' % (x['败'], x['跑'], '；'.join(x['败例'][:2]))))
    return 出


def _glob前缀(活):
    """诸活器码中带「*」之串 → 其档名之前缀（≥2 字）：'回执_*第%d章*.md' → '回执_'。并 startswith('…') 之前缀。"""
    出 = set()
    for _, 文 in 活:
        for s in re.findall(r"['\"]([^'\"\n]{0,80}\*[^'\"\n]{0,40})['\"]", 文):
            前 = s.split('*')[0].split('/')[-1]
            if len(前) >= 2:
                出.add(前)
        for s in re.findall(r"startswith\(\s*\(?\s*['\"]([^'\"\n]{2,40})['\"]", 文):
            出.add(s.split('/')[-1])
    return {x for x in 出 if x}


def 档之囤灰(root=None, 今=None, 日=None, 末改=None):
    """→ [(档, 由)]：顶层 设定/*.md 之候汰。末改：{档: 末提交之 epoch}（自测注之；默一回 git log 取之）。"""
    import subprocess, time as _t
    root = root or ROOT
    今 = 今 or _t.time()
    日 = 灰之日 if 日 is None else 日
    活 = _活档(root)
    前缀 = _glob前缀(活)
    他 = []
    for f in ('00_总章.md', 'README.md', '设定/00_镇冢秘术_唯一总圣经.md', '设定/canon事实库.json'):
        try:
            他.append(open(os.path.join(root, f), encoding='utf-8', errors='ignore').read())
        except Exception:
            pass
    全文 = '\n'.join([文 for _, 文 in 活] + 他)
    if 末改 is None:
        末改 = {}
        r = subprocess.run(['git', '-c', 'core.quotepath=off', 'log', '--format=@%ct', '--name-only', '--', '设定/'],
                           cwd=root, capture_output=True, text=True)
        t = None
        for l in r.stdout.split('\n'):
            if l.startswith('@'):
                t = int(l[1:])
            elif l.strip() and l not in 末改 and t is not None:
                末改[l] = t
    出 = []
    for f in sorted(glob.glob(os.path.join(root, '设定', '*.md'))):
        rel = os.path.relpath(f, root).replace(os.sep, '/')
        名 = os.path.basename(f)
        if any(名.startswith(p) for p in 前缀):
            continue
        干 = 名[:-3]
        if 名 in 全文 or (len(干) >= 6 and 干 in 全文):
            continue
        t = 末改.get(rel)
        if t is None or (今 - t) < 日 * 86400:
            continue
        出.append((rel, '活档无一字面之引、无 glob 之族，末提交距今 %d 日' % int((今 - t) // 86400)))
    return 出


def 普查(root=None, 印=True):
    """→ {'候修': [...], '候退': [...], '档之囤灰': [...]}；只报不拦。"""
    果 = {'候修': 候修(root), '候退': 候退(root), '档之囤灰': 档之囤灰(root)}
    if 印:
        print('════ 囤灰闸 --普查（只报·⛔拦；候者交大审之器审与总编辑之裁） ════')
        for k, 顶 in (('候修', 30), ('候退', 30), ('档之囤灰', 25)):
            print('  %s %d%s' % (k, len(果[k]), '（列其首 %d）' % 顶 if len(果[k]) > 顶 else ''))
            for 名, 由 in 果[k][:顶]:
                print('    · %s —— %s' % (名, 由))
    return 果


def _普查之测():
    """→ [(名, 合否)]：普查之三路，各以坏例证其真红、以反例证其⛔误拦（假仓·git 真提交带日）。"""
    import tempfile, shutil, subprocess, time as _t
    R = []
    t = tempfile.mkdtemp(prefix='囤灰_普查_')
    try:
        def 写(p, s):
            os.makedirs(os.path.dirname(os.path.join(t, p)) or t, exist_ok=True)
            open(os.path.join(t, p), 'w', encoding='utf-8').write(s)
        写('工具/全测.py', "def chk_a():\n    out = run('负测·甲', ['工具/甲.py', '--自测'])\n"
                         "def chk_b():\n    return _自测之项('负测·丙', '工具/负测_丙.py')\n"
                         "def chk_c():\n    out = run('乙', ['工具/乙.py'])\n"
                         "def chk_d():\n    out = run('丁', ['工具/丁.py', '--自测'])\n")
        写('工具/甲.py', '# 只供自测\n')
        写('工具/乙.py', '# 全测真跑其本职\n')
        写('工具/丁.py', '# 自走亦调之\n')
        写('工具/负测_丙.py', '# 测也\n')
        写('工具/戊.py', '# 其流程已废\n')
        写('工具/自走.py', "import subprocess\nsubprocess.run(['python3', '工具/丁.py'])\n# 甲.py 只在注里提\n"
                         "G = glob.glob(os.path.join(ROOT, '设定', '回执_*.md'))\n")
        写('工具/己.py', "P = '设定/引之档.md'\n")
        写('设定/法用册.json', json.dumps({'废': [{'id': '旧流', '名': '旧流（工具/戊.py 之对质）'}]}, ensure_ascii=False))
        for p in ('设定/旧档.md', '设定/新档.md', '设定/引之档.md', '设定/回执_0901_第9章.md'):
            写(p, '文\n')
        g = lambda *a, **k: subprocess.run(['git'] + list(a), cwd=t, capture_output=True, text=True, **k)
        g('init', '-q')
        for k, v in (('user.name', 't'), ('user.email', 't@t'), ('commit.gpgsign', 'false')):
            g('config', k, v)
        今 = int(_t.time())
        def 提(档们, 前日):
            g('add', '--', *档们)
            env = dict(os.environ, GIT_AUTHOR_DATE='@%d +0000' % (今 - 前日 * 86400), GIT_COMMITTER_DATE='@%d +0000' % (今 - 前日 * 86400))
            g('commit', '-q', '-m', 'x', env=env)
        提(['工具', '设定/法用册.json', '设定/旧档.md', '设定/引之档.md', '设定/回执_0901_第9章.md'], 40)
        提(['设定/新档.md'], 2)
        退 = dict(候退(t))
        R.append(('⑭普查·候退：唯自测一路者（甲）入列；注里之提⛔算活引', '甲.py' in 退 and '唯自测' in 退['甲.py']))
        R.append(('⑭之二 放行：全测真跑其本职者（乙）、他器亦调者（丁）、负测_*（丙）俱⛔列',
                  not any(k in 退 for k in ('乙.py', '丁.py', '负测_丙.py'))))
        R.append(('⑭之三 其名见於「废」而活引 ≤2 者（戊）入列', '戊.py' in 退 and '废' in 退['戊.py']))
        修 = dict(候修(t, 账={'快格': {'跑': 5, '红': 0, '秒均': 1.0}, '红格': {'跑': 4, '红': 3, '秒均': 2.0},
                                 '慢格': {'跑': 3, '红': 0, '秒均': 45.0}, '少跑': {'跑': 2, '红': 2, '秒均': 1.0}},
                         迹行=[json.dumps({'t': '2026-10-2%dT00:00:00' % i, '器': '败器.py', '参': [], '秒': 1, 'rc': 1 if i < 4 else 0})
                              for i in range(6)]))
        R.append(('⑮普查·候修：红多（3／4）、慢（45 秒）、败多（迹 4／6）俱入列', '红格' in 修 and '慢格' in 修 and '败器.py' in 修))
        R.append(('⑮之二 放行：常格、跑不足三回者⛔列', '快格' not in 修 and '少跑' not in 修))
        灰 = dict(档之囤灰(t, 今=今))
        R.append(('⑯档之囤灰：无引而逾三十日者（旧档）入列', '设定/旧档.md' in 灰))
        R.append(('⑯之二 放行：新改（2 日）、器字面引之、glob 之族（回执_*）俱⛔列',
                  not any(k in 灰 for k in ('设定/新档.md', '设定/引之档.md', '设定/回执_0901_第9章.md'))))
    finally:
        shutil.rmtree(t, ignore_errors=True)
    真 = dict(档之囤灰())
    R.append(('⑯之三 真仓：档之囤灰可算（%d 份）、器所读之 瑕疵总账 ⛔在其列' % len(真), '设定/瑕疵总账.md' not in 真))
    return R


if __name__ == '__main__':
    if '--自测' in sys.argv:
        sys.exit(0 if 自测() else 1)
    if '--普查' in sys.argv:            # 1027·#55 #103：只报不拦
        普查()
        sys.exit(0)
    if '--迹' in sys.argv:
        _n = int(sys.argv[sys.argv.index('--迹') + 1])
        _始, _至 = 迹窗(_n)
        _报 = 迹报(_n, 迹(_始, _至), _始, _至)
        if '--写' in sys.argv:
            _p = os.path.join(ROOT, '版本', '第%d章' % _n, '_器之迹.md')
            os.makedirs(os.path.dirname(_p), exist_ok=True)
            open(_p, 'w', encoding='utf-8').write(_报); print('✓ 写 %s' % os.path.relpath(_p, ROOT))
        else:
            print(_报)
        sys.exit(0)
    红, _ = 查()
    sys.exit(1 if 红 else 0)
