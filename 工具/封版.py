#!/usr/bin/env python3
"""封版（1013 立·造式二代·设定/方法升级_造式二代.md §五之五）——封版诸件之跑器、核数、提交、备份，归脚本。

为何立：一代之案席与封版席两席（380：$19.65＋$31.88，来回 414 回）大半在跑器、核数、提交、备份——机器之活。
二代拆开（零 token 之检）：
  · 读懂了才写得出之档（回执之文、锁定行逐拍、创作记录、全书记忆、状态册、open_brief、下一章开镜卡）——记席（造章.js 之末席）；
  · 其余——存版对表、造式之实、锁定行之数、坑账之单、诸闸、第十一轮、读者可见之快格、医生、末章硬闸、提交、存底、推「章-N」、撤锁——本器。

用法：
  python3 工具/封版.py N --前        # 记席先跑：对表（正文≠末版即存一版）、造式之实、锁定行之数、坑账之单、约到期（N≥411）、前章回执与锁定行之样
  python3 工具/封版.py N --前 --红   # 复跑只印红：⛔ 项（新红／变）、较上回之变、上回红今已绿，末行「✓ 余 N 项俱绿」（上回之印存 .cache/封版前/；首跑全印）
  python3 工具/封版.py N --後        # 记席毕、--前 绿、复盘与交接已写：验记席之档俱在 → 同步（README、总站、人物册之阶段句随之）→ 诸闸（囤灰闸、
                                      #   质量三闸、席令之禁、圣经随裁、器物点名 N〔1027 左移之拦〕、第十一轮、读者可见之快格、读者可见之慢格〔1119 执行之审·治7〕、医生、末章硬闸）
                                      #   → 席记「封版」段（後之闸俱过方书·1118）→ 活态之报 → 提交（封版#N 一提交载本章之一切）→ 存底 → 推「章-N」（一章唯此一推）→ 撤锁（红即停、⛔提交）
  python3 工具/封版.py N --後 --试   # 演练（丝滑主义·改流程先演於真料）：取第N章封版之提交为底，於临时之副本以今之器重跑同步与诸闸
                                      #   （⛔提交、⛔推、⛔存底），同步之档逐字比於封版之提交、诸闸之判比於其实，果入 设定/演练账.json
  python3 工具/封版.py --自测         # 以已封版之 380 之真料核诸数（与其锁定行亲核之数逐个同）
  python3 工具/封版.py --回放慢格     # 〔1119 执行之审·治7〕读者之慢之真迹回放（手跑·一回之证）：472 封版之树 f743735c6 → 红（FS沉默闸）、其治 79ef08a55 → 绿
                                      #   ⛔入 --自测：各树以其自身之器跑（⛔验今器），恒同一果；二树各 11k 档、约廿五秒、省取之片懒取逾 1MB 之档——徒加阻推之闸之时与败源
次序之据：开轮六检於第十一轮之前跑（旧⑭「封版之章不得再跑十轮」1027 汰——其防移 续跑之守：已封之 N ⛔再派造章）。
一章之序（1027 A2·Variant S）：记席毕 → `--前 --红` 绿 → `复盘.py W … --简 --平台 $X` 与交接现状（写而⛔另提交）→ `--後`——
  封版#N 一提交载回执、记席诸档、复盘、交接；其末 `存底 --标` 推「章-N」即触 GitHub autopush（分片而闸、绿即并入主枝、果入 备份/报）；
  推成即本地泊於「章-N」（1117·法用#停钩空转：平台 Stop 钩⛔每回合报「未推」；--候主 之快进归主枝；泊不成照旧）；
  沙盒⛔跑全闸、⛔推主枝；跑毕主环 `python3 工具/接棒守.py --候主 N`（run_in_background、零 token：主枝含即快进返 0、坏报即返其红——
  红者照其行治、提交、`推.py`（交「治-<sha>」）；`推.py --直` 只作审计之兜底：报「拒」或 GitHub 停摆）。
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import os, sys, re, json, glob, time, shutil, hashlib, tempfile, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
施工表 = os.path.join('设定', '01_镇冢秘术_逐章施工与伏笔回收表.md')
总纲 = os.path.join('设定', '02_余章之势_总纲.md')
_坐 = re.sub(r'^(session_|cse_)', '', os.environ.get('CLAUDE_CODE_REMOTE_SESSION_ID', '').strip())   # 1027 执行之核：封版之提交之坐取本会话（旧写死总编辑之坐，法用#换会话 之坐异读之即空验）
尾 = 'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>' + ('\nClaude-Session: https://claude.ai/code/session_%s' % _坐 if _坐 else '')


# 〔1119 死规之审·gates14〕拔「五钩」：逐章逼答钩即坐实「每章须有钩」之框（违 1119·G1108-06）；与 小说检察官._receipt_ok 同拔（X83 一致之测）；余键⛔动
回执闸之键 = ('伏笔', '新锚', '病历', '清单', '原场', '到期账', '章魂', '生死检', '改动闸', '本章之失')   # 小说检察官._receipt_ok 於 N≥351 所索（记料【一】同印·X83）


def 正文档(n, root=ROOT):
    from 对账预筛 import 章号
    for f in glob.glob(os.path.join(root, '正文', '*.md')):
        if 章号(f) == n:
            return f
    return None


def 跑(a, root=ROOT, 限=900):
    t = time.time()
    try:
        r = subprocess.run([sys.executable] + a if a[0].endswith('.py') else a, cwd=root, capture_output=True, text=True, timeout=限)
        return r.returncode, r.stdout + r.stderr, time.time() - t
    except subprocess.TimeoutExpired:
        return 124, '（逾 %d 秒未毕）' % 限, time.time() - t


def 器(名):
    return os.path.join(ROOT, '工具', 名)


def 数(n, root=ROOT):
    """锁定行之机器之数（⛔凭空写一个数即是造数）。"""
    f = 正文档(n, root)
    if not f:
        return {'坏': '第%d章之正文不在' % n}
    文 = open(f, encoding='utf-8').read()
    L = 文.split('\n')
    亮 = next((i + 1 for i, l in enumerate(L) if '【本章亮点】' in l), None)
    白止 = (亮 - 1) if 亮 else len(L)
    while 白止 > 1 and not L[白止 - 1].strip():
        白止 -= 1
    星 = sum(1 for l in L[:白止] if l.strip() == '＊')
    import 净重对表
    d = {'正文': os.path.relpath(f, root), '白文': '1 至 %d 行' % 白止, '亮点行': 亮, '净重': 净重对表.净重(f),
         '＊': 星, '拍': 星 + 1, 'sha1': hashlib.sha1(文.encode('utf-8')).hexdigest()[:12]}
    台 = os.path.join(root, '版本', '第%d章' % n, '_台账.json')
    if os.path.exists(台):
        版们 = json.load(open(台, encoding='utf-8')).get('版本', [])
        if 版们:
            末 = 版们[-1]
            d['末版'] = 末.get('版')
            s = 末.get('soft')
            s = eval(s, {}) if isinstance(s, str) else (s or {})      # 台账之 soft 以 Python 字面存（跑轮所写）
            d['六数'] = '净重%s｜段数%s｜长段数%s｜嗅%s｜触%s｜四字串三现%s' % tuple(s.get(k, '?') for k in ('净重', '段数', '长段数', '嗅', '触', '四字串三现'))
            d['诸版'] = ['%s %s「%s」' % (v.get('版'), v.get('时', ''), str(v.get('说明', ''))[:40]) for v in 版们]
            末档 = os.path.join(root, '版本', '第%d章' % n, '%s.md' % 末.get('版'))
            d['与末版同'] = os.path.exists(末档) and open(末档, encoding='utf-8').read() == 文
    m = re.search(r'\|\s*%d\s*\|\s*([主暗]·\d+(?:—\d+)?)\s*\|' % n, open(os.path.join(root, 总纲), encoding='utf-8').read())   # 两栏排，整行逐栏认
    d['总纲'] = '| %d | %s |' % (n, m.group(1)) if m else None
    return d


_引式 = re.compile(            # ★W60 X37：骨记之「章:行」——全角半角冒号、区间（至／—／-，後端可复书其章）、本章（：行）、续前一引之章（、：行）
    r'(?<![\dA-Za-zＡ-Ｚａ-ｚ０-９_#/.\-])(\d{1,3})[:：](\d{1,4})(?:\s*(?:至|—|–|-|～|~)\s*(?:(\d{1,3})[:：])?(\d{1,4}))?'
    r'|(?<=[（(])[:：](\d{1,4})(?:\s*(?:至|—|–|-|～|~)\s*(\d{1,4}))?(?=\s*[）)、，,])'
    r'|(?<=、)[:：](\d{1,4})(?:\s*(?:至|—|–|-|～|~)\s*(\d{1,4}))?')
_原句式 = re.compile(r'[ \t]*[）)]?[ \t]*「([^」\n]+)」')       # 紧随其引之「原句」（「（：23）「……」」之式容一「）」）
_略 = re.compile(r'……|…|⋯+|\.\.\.|／')                        # 原句内之略与分行：逐段各核
_标 = '，。！？、；：,.!?;:…—「」『』“”‘’"\'（）()·｜|\\s'


def _净(s):
    """⛔比标点之引号与空白：骨记以「」引，白文之对白是“”，引中之引是『』。"""
    return re.sub(r'[\s「」『』“”‘’"\']', '', s)


def 骨引(骨, n):
    """骨记之诸引 → [{章, 起, 止, 句, 前文, 後文, 原}]。句＝紧随之「原句」（无则 None＝远引）；前文／後文＝其引所在小句之文（供远引之核）。
    ⛔认：字母之後之号（Ｄ6：164、W33:）、跨章之区间；「总纲：325」之类（冒号前无章号、亦非「（：」）非章之引。"""
    from 对账预筛 import 汉章行
    骨 = 汉章行(骨)                     # ★X84（1105）：骨记以汉字写章行（「四百一十二：五十三」）——器内换作数字再认（⛔改骨记）
    出 = []; 前章 = None
    for m in _引式.finditer(骨):
        if m.group(1):
            c, a = int(m.group(1)), int(m.group(2))
            if m.group(3) and int(m.group(3)) != c:
                前章 = None; continue
            b = int(m.group(4)) if m.group(4) else a
        elif m.group(5):
            c, a = n, int(m.group(5)); b = int(m.group(6)) if m.group(6) else a
        else:
            if 前章 is None:
                continue
            c, a = 前章, int(m.group(7)); b = int(m.group(8)) if m.group(8) else a
        前章 = c
        q = _原句式.match(骨, m.end())
        i = max(骨.rfind(x, 0, m.start()) for x in '｜|；;。\n')
        j = [k for k in (骨.find(x, m.end()) for x in '）)｜|；;。\n') if k >= 0]
        出.append({'章': c, '起': a, '止': max(a, b), '句': q.group(1) if q else None, '原': m.group(0),
                   '前文': 骨[i + 1:m.start()].rstrip(' \t（(')[-40:], '後文': 骨[m.end():min(j) if j else len(骨)][:40]})
    return 出


def 共串(甲, 乙, 下=4):
    """甲之一串（⛔跨标点）逐字在乙者，取其最长；短於「下」字者 ''。"""
    乙 = _净(乙); 最 = ''
    for 段 in re.split('[%s]+' % _标, 甲):
        for i in range(len(段)):
            j = i + max(下, len(最) + 1)
            while j <= len(段) and 段[i:j] in 乙:
                最 = 段[i:j]; j += 1
    return 最 if len(最) >= 下 else ''


def 核引(引, 白们):
    """一引 → (类, 合否, 注)。类：原句／远引／短（原句不足四字·不核）。白们：章 → 白文之行（行号与档同）。
    原句：全句逐段核（⛔旧式只核句首二十四字）——以略号与「／」切段，凡四字以上之段俱须逐字在所引之行·±1（区间则其起－1 至止＋1）；
    远引：骨记其小句之文与所引之行·±1 之最长逐字共串（四字以上方算），注即其串；无者注空，由印者印所引之行。"""
    L = 白们.get(引['章'])
    类 = '远引' if 引['句'] is None else '原句'
    if L is None:
        return 类, False, '所引之章不在'
    if 引['起'] > len(L):
        return 类, False, '行逾其白文（%d 行）' % len(L)
    lo, hi = max(1, 引['起'] - 1), min(len(L), 引['止'] + 1)
    窗 = '\n'.join(L[lo - 1:hi])
    if 类 == '远引':
        s = 共串(引['前文'] + '｜' + 引['後文'], 窗)
        return 类, bool(s), s
    段们 = [s for s in (_净(x) for x in _略.split(引['句'])) if len(re.sub('[%s]' % _标, '', s)) >= 4]
    if not 段们:
        return '短', True, ''
    缺 = [s for s in 段们 if s not in _净(窗)]
    if not 缺:
        return 类, True, ''
    实 = [k for k, l in enumerate(L, 1) if 缺[0] in _净(l)]
    return 类, False, ('实在 :%s' % '、:'.join(map(str, 实[:3]))) if 实 else '所引之章无此句'


def 骨引之核(骨, n, root=ROOT, 白们=None):
    """→ [(引, 类, 合, 注, 所引之章之白文行)]。白们缺省则只载所引诸章之白文（⛔全书）。"""
    引们 = 骨引(骨, n)
    if 白们 is None:
        import 章料
        白们 = {}
        for c in sorted({x['章'] for x in 引们}):
            f = 章料.章档(c, root)
            if f:
                t = open(f, encoding='utf-8').read(); i = t.find('【本章亮点】')
                白们[c] = (t[:i] if i >= 0 else t).split('\n')
    出 = []
    for x in 引们:
        类, 合, 注 = 核引(x, 白们)
        出.append((x, 类, 合, 注, 白们.get(x['章'])))
    return 出


def 骨引之印(核):
    """骨引之核 → 机械之证之①（一项；远引诸行以换行续之）。"""
    def 号(x):
        return '%d:%d' % (x['章'], x['起']) + ('—%d' % x['止'] if x['止'] > x['起'] else '')
    原 = [k for k in 核 if k[1] == '原句']; 短 = [k for k in 核 if k[1] == '短']; 远 = [k for k in 核 if k[1] == '远引']
    坏 = ['%s「%s」%s' % (号(x), x['句'][:20], 注) for x, _, 合, 注, _L in 原 if not 合]
    s = '①骨记引句（章:行「原句」·含区间、全角冒号、本章（：行））%d/%d 合｜不合 %d%s%s' % (
        len(原) - len(坏), len(原), len(坏), ('：' + '；'.join(坏[:30])) if 坏 else '（俱四字以上逐字在所引之章之行·±1）',
        '｜不足四字不核 %d' % len(短) if 短 else '')
    if 远:
        共 = [k for k in 远 if k[2]]; 余 = [k for k in 远 if not k[2]]
        s += '\n      ①之二·骨记远引（章:行 而无「原句」）%d 处：骨记之文四字以上逐字在所引之行·±1 者 %d/%d%s' % (
            len(远), len(共), len(远), ('（' + '、'.join('%s「%s」' % (号(x), 注) for x, _, _, 注, _L in 共[:40]) + '）') if 共 else '')
        if 余:
            s += '；余 %d 处印所引之行（记席照此判、⛔再 awk）：' % len(余)
            for x, _, _, 注, L in 余[:40]:
                if 注:
                    行 = '（%s）' % 注
                else:                    # 所引之行（区间则连其诸行）；骨记之文有三字以上落在其行·±1 者，截其近处，否则截行首
                    窗 = _净(''.join(L[max(1, x['起'] - 1) - 1:min(len(L), x['止'] + 1)]))
                    本 = _净(''.join(L[x['起'] - 1:x['止']]))
                    近 = 共串(x['前文'] + '｜' + x['後文'], 窗, 3)
                    # ★X91③（434）：旧截百字——426:95（340 字）被截、记席再 awk 一回；今所引之行全印（至 400 字，与 章料.引之原句 同界），
                    #   唯共串只落在 ±1 之邻行者印其近处之窗
                    if 近 and 近 not in 本:
                        p = max(0, 窗.find(近) - 20)
                        行 = '「%s」' % (('…' if p > 0 else '') + 窗[p:p + 300])
                    else:
                        行 = '「%s」' % (本[:400] + ('…（下略 %d 字）' % (len(本) - 400) if len(本) > 400 else ''))
                s += '\n        %s%s ← 骨「%s‖%s」' % (号(x), 行, x['前文'][-16:], x['後文'][:16])
    return s


def 对白之行(L):
    """白文之行们 → [(行号, 行)]：对白之行（坑⑩·机械之证③）；记落.py 之「‹器:对白›」同此一把尺。"""
    return [(k + 1, l) for k, l in enumerate(L) if '“' in l or re.search(r'「[^」]{1,40}」[，。！？]?(?:他|她|我|钱满|刘二|东头|老头)?说', l)]


def 机械之证(n, root=ROOT):
    """★1015 W33 之改（390 之试：记席 58 工具里翻查 32——坑账之答所须之据由模型逐条 grep）：
    据之可机算者器先算——①骨记引句逐条核於所引之章（坑㉕；★W60 X37：含区间、本章、远引——远引无原句者印所引之行）②卡之⛔字在白文之数（坑⑱）③对白之行（坑⑩）④日词（坑⑫）⑤数词之行（坑㉘）
    ⑥极短段之比：本章与同线前三章（坑账 P39；★1016 X06 之补——旧缺此项，391、393 记席每章自算）。
    ⛔判：只交据；犯没犯仍由记席判。"""
    import 章料
    f = 章料.章档(n, root)
    t = open(f, encoding='utf-8').read()
    i = t.find('【本章亮点】')
    白, 骨 = (t[:i], t[i:]) if i >= 0 else (t, '')
    L = 白.split('\n'); 出 = []
    # ①骨记之引（★W60 X37：逐条机核——旧式只认「章:行「≤40 字」」一式、只核句首 24 字，398 记席仍亲 awk 远引六处）
    出.append(骨引之印(骨引之核(骨, n, root)))
    # ②卡之⛔字
    卡 = os.path.join(root, '版本', '第%d章' % n, '_开镜卡.md')
    禁 = []
    if os.path.exists(卡):
        kt = open(卡, encoding='utf-8').read()
        禁 = sorted(set(re.findall(r'⛔\s*「([^」]{1,8})」', kt) + re.findall(r'「([^」]{1,8})」\s*⛔', kt)))
    出.append('②卡之⛔字在白文之数：' + ('｜'.join('「%s」%d' % (w, 白.count(w)) for w in 禁[:30]) or '（卡无⛔「字」之式）'))
    # ③对白之行
    对 = 对白之行(L)
    出.append('③对白之行 %d：%s' % (len(对), '、'.join(':%d' % k for k, _ in 对[:40])))
    # ④日词
    日 = [(k + 1, m) for k, l in enumerate(L) for m in re.findall(r'第[零〇一二三四五六七八九十百]+[天日]|昨天|前天|今天|明天|後半夜|天亮|天黑|晌午|後晌|日落', l)]
    出.append('④日词：%s' % ('、'.join(':%d%s' % (k, m) for k, m in 日[:40]) or '无'))
    # ⑤数词之行
    数 = [(k + 1, m) for k, l in enumerate(L) for m in re.findall(r'[零〇一二两三四五六七八九十百千]+(?:个|道|处|回|天|步|指|尺|丈|口|块|张|行|格|刻|时辰|下)', l) if not re.match(r'一[^十百千]', m)]   # 「一个」「一下」之类⛔列（噪）
    出.append('⑤数词 %d 处（先说後数之核）：%s' % (len(数), '、'.join(':%d%s' % (k, m) for k, m in 数[:40])))
    # ⑥极短段之比（P39）：本章与同线前三章，同一把尺（极短段()），旧→新排
    import 造式验
    前三 = 同线前三(n, lambda k: 造式验.线(k, root), lambda k: 章料.章档(k, root) is not None)
    def _比(k):
        短, 共 = 极短段(open(章料.章档(k, root), encoding='utf-8').read())
        return 短, 共, (100.0 * 短 / 共 if 共 else 0.0)
    列 = [(k,) + _比(k) for k in 前三 + [n]]
    率 = [r for *_, r in 列]
    出.append('⑥极短段（≤%d 字）之比｜同线(%s)前三章与本章：%s｜连四章上行：%s' % (
        极短段之限, 造式验.线(n, root) or '?', '→'.join('%d %d／%d＝%.1f%%' % x for x in 列),
        ('是' if all(a < b for a, b in zip(率, 率[1:])) else '否') if len(列) == 4 else '（同线前章不足三，判不出）'))
    return 出


极短段之限 = 15        # ★P39 之尺（382—393 记席同法：≤15 字为极短段）


def 极短段(文, 限=极短段之限):
    """(极短段数, 段数)。段之尺与 跑轮.score 之「段数」同（白文去题行、去空行、去「＊」、去空白）——⛔另造一把尺。"""
    import 跑轮
    段 = [re.sub(r'\s', '', x) for x in 跑轮.body_of(文).split('\n') if x.strip() and x.strip() != '＊']
    return sum(1 for x in 段 if len(x) <= 限), len(段)


def 同线前三(n, 线之, 在=lambda k: True, 远=24):
    """n 之同线（造式验.线）前三章，旧→新；线认不出则 []。"""
    l0 = 线之(n)
    if not l0:
        return []
    得 = []
    for k in range(n - 1, max(n - 远, 0), -1):
        if len(得) == 3:
            break
        if 线之(k) == l0 and 在(k):
            得.append(k)
    return 得[::-1]


def 慢检并起(n, root=ROOT, 隔=0.5):
    """★W60 X39（399 记席 flaws②：--前 逾 120 秒，记席之 Bash 转後台、候二回）——400 於副本实测改前 121.5 秒：
    检察官 --末章 79.9 秒、开轮六检 --静 39.0 秒（二者相继），余检合计约 2 秒。今此二检先并起於後台，余检照序跑；
    印之序照旧（至其位方 result()）。⛔删一检、⛔减其所查：命令一字不改，只改其起之时。
    隔：诸器一载 `_账` 即读改写 `_跑账.json` 一笔（无锁），同刻起则丢一笔——错开半秒起。
    → {'检察官': future→CompletedProcess（与旧之 subprocess.run 同）, '开轮六检': future→(rc, 印, 秒)（与旧之 跑() 同）}"""
    from concurrent.futures import ThreadPoolExecutor
    池 = ThreadPoolExecutor(max_workers=2)
    慢 = {'检察官': 池.submit(subprocess.run, [sys.executable, 器('小说检察官.py'), '--末章', str(n)], cwd=root, capture_output=True, text=True)}
    time.sleep(隔)
    慢['开轮六检'] = 池.submit(跑, [器('开轮六检.py'), str(n), '--静'], root)
    time.sleep(隔)
    池.shutdown(wait=False)          # 不候：二检照跑，至其位 result() 方候
    return 慢


def 前(n, root=ROOT):
    print('════ 封版·前（第%d章）════' % n)
    d = 数(n, root)
    if d.get('坏'):
        print('⛔ ' + d['坏']); return False
    if d.get('与末版同') is False:
        rc, out, _ = 跑([器('跑轮.py'), '--存', str(n), '造式二代·定稿：正文与末版对齐（封版.py --前）'], root)
        print('· 正文与末版不一：已存一版（rc=%d）' % rc)
        d = 数(n, root)
    慢 = 慢检并起(n, root)                                   # ★W60 X39：二慢检先并起於後台（存版之後：其读版本）；余检照序跑、照序印
    rc, out, _ = 跑([器('造式.py'), str(n)], root)
    print('· 造式之实：%s' % (out.strip().split('\n')[-1] if out.strip() else rc))
    print('· 锁定行之数（取此，⛔凭空写）：')
    for k in ('正文', '总纲', '白文', '亮点行', '净重', '六数', '＊', '拍', '末版', '与末版同', 'sha1'):
        print('    %s：%s' % (k, d.get(k)))
    for v in d.get('诸版', []):
        print('    版：' + v)
    rc, out, _ = 跑([器('坑账.py'), '--逐章', str(n)], root)
    print('· 坑账之单（逐条答进回执「坑账之答」）：\n' + '\n'.join('    ' + l for l in out.strip().split('\n')))
    try:
        print('· 坑账之机械之证（器先算·记席照此答、⛔再逐条 grep——W33 之治：390 记席翻查 32 回多在此）：\n' + '\n'.join('    ' + l for l in 机械之证(n, root)))
    except Exception as _e:
        print('· 坑账之机械之证：⛔算不出（%s）——记席照旧手查' % _e)
    try:                                                     # ★1013：开轮十六检——384 记席未写「承前之判」（⑮），封版·後 方红；今於 --前 即印其红
        rc6, out6, _ = 慢['开轮六检'].result()
        import 全测 as _全测
        余6 = _全测._六检之败(out6)
        print('· 开轮十六检：%s' % ('✓ 俱过' if not 余6 else '⛔ ' + '；'.join(余6)[:600] + '——记席须治（承前之判写进轮记，逐样点名落判：认／翻／搁下）'))
    except Exception as _e:
        print('· 开轮十六检：⛔判不出（%s）' % _e)
    try:                                                     # ★1106（425 实踩：大审 #29 限425 未裁，封版 --前 绿而 GitHub 推闸「负测·大审挂限」红）：大审之闸於 --前 即印
        _r = subprocess.run([sys.executable, 器('大审.py'), '--闸'], cwd=root, capture_output=True, text=True, timeout=120)
        _逾 = [l.strip() for l in _r.stdout.split('\n') if l.strip().startswith('⛔')]
        print('· 大审之闸：%s' % ('✓ 无逾限之挂' if not _逾 else '⛔ ' + '；'.join(_逾)[:500] + '——主环当场裁（已治／判驳／改限·⛔静静顺延）'))
    except Exception as _e:
        print('· 大审之闸：⛔判不出（%s）' % _e)
    try:                                                     # ★1017：回执闸（小说检察官._receipt_ok）——397 记席之回执缺「到期账」一词，封版·後之全测·快（检察官自测·末章硬闸）方红；今於 --前 即印所缺之键
        import 小说检察官 as _检
        _文 = ''.join(open(_f, encoding='utf-8').read() for _f in _检._receipt_files(n))
        _缺 = [k for k in 回执闸之键 if k not in _文]
        print('· 回执闸：%s' % ('✓ 键俱在' if _检._receipt_ok(n) else '⛔ 回执（设定/回执_*第%d章*.md）缺键：%s——记席照 396 回执之式补其节（到期账：本章动没动 设定/到期账.json、哨与限）' % (n, '、'.join(_缺) or '（档名不认本章）')))
    except Exception as _e:
        print('· 回执闸：⛔判不出（%s）' % _e)
    if os.path.exists(os.path.join(root, '版本', '第%d章' % n, '_器物.md')):     # ★1020：398 治 soft-1 删「本子」於拍5，器物册之「出=5」遂错——全测·快不含逐章回灌，推闸方红；左移於此
        r = subprocess.run([sys.executable, 器('器物点名.py'), str(n)], cwd=root, capture_output=True, text=True)
        _红 = [l.strip() for l in r.stdout.split('\n') if '⛔ ★' in l]
        print('· 器物册（器物点名 %d）：%s' % (n, ('⛔ ' + '｜'.join(_红[:3]) + '——改册之拍号照白文亲数') if (_红 or '⛔' in r.stdout) else '✓ 拍号俱对'))
    # ★1118 466 逮：记席漏立「## 四、续写第 N+1 章前的硬门槛」，至 --後 之医生（项目文档接线）方红——同一之判左移於 --前（一秒）
    try:
        _施 = open(os.path.join(root, '设定', '01_镇冢秘术_逐章施工与伏笔回收表.md'), encoding='utf-8').read()
        print('· 施工表下一章硬门槛：%s' % ('✓' if ('## 四、续写第 %d 章前的硬门槛' % (n + 1)) in _施 else '⛔ 缺「## 四、续写第 %d 章前的硬门槛」一节——记席照前章之节式补立（医生·项目文档接线同判）——治後再跑 --前' % (n + 1)))
    except Exception as _e:
        print('· 施工表下一章硬门槛：⛔判不出（%s）' % _e)
    主环 = []                                               # ★1024 省 token 之审 records 二·④：N≥411 越职三闸（囤灰闸、跑账、席令之禁）入「主环之职」一栏；质量三闸（含①之e 六问）留记席之栏
    for _名, _令 in (('囤灰闸', ['囤灰闸.py']), ('跑账', ['跑账.py']), ('圣经随裁', ['圣经随裁.py']),
                     ('质量三闸', ['质量三闸.py']), ('席令之禁', ['席令之禁.py'])):   # ★1023 坑㉟复踩：408 新立大审.js 缺律⑮⑳，至 --後 之全测·快（六分）方红——一秒之器左移於此   # ★1022 坑㊹：404 封毕而推闸之质量三闸①之c（一章一日）方红——与推闸同一器左移於 --前   # ★1020 坑㉟：400 封版三回——新器未接未跑、新裁未书圣经之随，至 --後 之全测·快（十分钟後）方红；此三闸各一秒，左移於此
        _r = subprocess.run([sys.executable, 器(_令[0])] + _令[1:], cwd=root, capture_output=True, text=True)
        _红 = [l.strip() for l in _r.stdout.split('\n') if l.strip().startswith('⛔')][:3]   # ⛔取行中之「⛔」：挂账之由文里亦有⛔字
        _行 = '· %s：%s' % (_名, '✓' if _r.returncode == 0 else '⛔ ' + ('；'.join(_红) or 'rc=%d' % _r.returncode)[:400] + '——治後再跑 --前')
        if n >= 分栏之始 and _名 in 主环之闸:
            主环.append('    ' + _行.replace('——治後再跑 --前', '——主环治'))
        else:
            print(_行)
    if n >= 分栏之始:          # ★1027 法用之守：已取之法本章真用上了没有（--前：记席之後方有之证免）——主环之职，--後 照拦
        _r = subprocess.run([sys.executable, 器('法用之守.py'), '--验', str(n), '--前'], cwd=root, capture_output=True, text=True)
        _红 = [l.strip() for l in _r.stdout.split('\n') if l.strip().startswith('⛔')][:3]
        主环.append('    · 法用之守：%s' % ('✓' if _r.returncode == 0 else '⛔ ' + ('；'.join(_红) or 'rc=%d' % _r.returncode)[:400] + '——主环治'))
    r = 慢['检察官'].result()   # ★1020：398 亮点 5+逗 至封版·後之全测·快（十一分钟後）方红——检察官之末章硬闸单跑左移於此（W60 X39：已於上并起）
    _病 = 末章之病(r.stdout) if r.returncode else []
    print('· 末章硬闸（检察官）：%s' % ('✓ 通过' + ('（第十一轮归 --後）' if r.returncode else '') if not _病 else '⛔ ' + '；'.join(_病)[:600] + '——治後再跑 --前'))
    try:                                                     # ★1013：六问（质量三闸①之e）——381 记席未答，封版之全测方红；今於 --前 即印
        import 质量三闸
        _名, _过, _语 = 质量三闸.gate1e(n)[0]
        print('· 六问：%s %s%s' % ('✓' if _过 else '⛔', _语, '' if _过 else '——记席须於轮记之首答六条（造章.js 记令 2之二）'))
    except Exception as _e:
        print('· 六问：⛔判不出（%s）' % _e)
    if n >= 分栏之始:          # ★1027 A2：约到期之实跑（正文自陈之约到期而未看）——旧唯一坐调之（已汰），全测只跑其负测；记席之栏（记席尚能答），--後 之读者之快格照拦
        _r = subprocess.run([sys.executable, 器('约到期.py'), '--闸'], cwd=root, capture_output=True, text=True)
        _红 = [l.strip() for l in _r.stdout.split('\n') if l.strip().startswith('⛔')][:3]
        print('· 约到期：%s' % ('✓ 无到期而未看之约' if _r.returncode == 0 else '⛔ ' + ('；'.join(_红) or 'rc=%d' % _r.returncode)[:400]
                                + '——记席治：到期之章让其物在手上再出现一回，或於轮记写「约-NNN·本章未兑：<由>」'))
    回 = sorted(glob.glob(os.path.join(root, '设定', '回执_*_第%d章封版席.md' % (n - 1))))
    print('· 前章回执之样：%s' % (os.path.relpath(回[-1], root) if 回 else '（无）'))
    t = open(os.path.join(root, 施工表), encoding='utf-8').read()
    样 = [l[:120] + '…' for l in t.split('\n') if l.startswith('| %d | 锁定 |' % (n - 1)) or l.startswith('| %d | 悬账 |' % (n - 1))]
    print('· 前章锁定行与悬账行之样（施工表）：\n' + '\n'.join('    ' + x for x in 样))
    if 主环:
        print('· 主环之职（记席⛔治；封版 --後 照拦）：\n' + '\n'.join(主环))
    return True


分栏之始 = 411                                   # ★N≤410 之 --前 之印一字不变
主环之闸 = ('囤灰闸', '跑账', '席令之禁')        # 越记席之职（409 回执 §十四·3 自注）；--後 之囤灰闸、全测·快照拦
_项式 = re.compile(r'^(    )?· ([^：]+)：[ \t]*(✓|⛔)')


def 前之项(印):
    """--前 之印 → {名: [栏, 态, 文]}：栏 席／主环；态 ✓／⛔／·（无态之印，文＝其块之全文，供较上回之变）。"""
    项, 块 = {}, None
    for l in 印.split('\n'):
        m = _项式.match(l)
        if m:
            项[m.group(2).strip()] = ['主环' if m.group(1) else '席', m.group(3), l.strip()]; 块 = None
        elif l.startswith('· '):
            块 = re.split('[：（]', l[2:], maxsplit=1)[0].strip(); 项[块] = ['席', '·', l]
        elif l.startswith('⛔ '):
            项[l[:24]] = ['席', '⛔', l.strip()]; 块 = None
        elif 块 and l.startswith(' '):
            项[块][2] += '\n' + l
    return 项


def _锁之数(文):
    return dict(re.findall(r'(?m)^    ([^：\n]+)：(.*)$', 文))


def 红印(n, 今, 上, 时=''):
    """--前 --红 之印：席栏之 ⛔（新红／变）、较上回之变、上回红今已绿、主环之职之红；末行「✓ 余 N 项俱绿」。"""
    出, 绿 = ['════ 封版·前·红（第%d章；较上回 %s）════' % (n, 时 or '?')], 0
    for 名, (栏, 态, 文) in 今.items():
        旧 = 上.get(名)
        if 态 == '✓':
            绿 += 1
        elif 态 == '⛔' and 栏 == '席':
            出.append(文 + ('' if 旧 and 旧[1] == '⛔' and 旧[2] == 文 else '（变）' if 旧 and 旧[1] == '⛔' else '（新红）'))
        elif 态 == '·' and 旧 and 旧[2] != 文:
            if 名 == '锁定行之数':
                a, b = _锁之数(旧[2]), _锁之数(文)
                出.append('· 变·锁定行之数：' + '；'.join('%s %s→%s' % (k, a.get(k, '（无）'), b.get(k, '（无）')) for k in b if a.get(k) != b.get(k)))
            else:
                出.append('· 变·%s（其印已异於上回；全印：python3 工具/封版.py %d --前）' % (名, n))
    已 = [名 for 名, x in 上.items() if x[1] == '⛔' and (今.get(名) or [0, '✓'])[1] != '⛔']
    if 已:
        出.append('· 上回红今已绿：' + '、'.join(已))
    环 = [x[2] for x in 今.values() if x[0] == '主环' and x[1] == '⛔']
    if 环:
        出.append('· 主环之职（记席⛔治；封版 --後 照拦）：\n' + '\n'.join('    ' + x for x in 环))
    出.append('✓ 余 %d 项俱绿' % 绿)
    return '\n'.join(出)


def 上回之档(n, root=ROOT):
    return os.path.join(root, '.cache', '封版前', '第%d章.json' % n)     # ⛔存 版本/（免 --後 提交、惹囤灰闸、档肿哨）


class _分流:
    """印之二路：存其文、且（显）照印於终端——--前 跑约二分，⛔候毕方印。"""
    def __init__(self, 显, 原):
        self.显, self.原, self.文 = 显, 原, []

    def write(self, x):
        self.文.append(x)
        if self.显:
            self.原.write(x)
        return len(x)

    def flush(self):
        self.原.flush()


def 前印(n, 红=False, root=ROOT):
    """--前（与 --前 --红）之跑口：印之同时存其项於 .cache；红且有上回者只印 红印()，无上回者全印（首跑）。"""
    档 = 上回之档(n, root)
    try:
        上 = json.load(open(档, encoding='utf-8'))
    except Exception:
        上 = None
    原 = sys.stdout
    流 = _分流(not (红 and 上), 原)
    sys.stdout = 流
    try:
        ok = 前(n, root)
    finally:
        sys.stdout = 原
    今 = 前之项(''.join(流.文))
    if 红 and 上:
        print(红印(n, 今, 上.get('项', {}), 上.get('时', '')))
    try:
        os.makedirs(os.path.dirname(档), exist_ok=True)
        json.dump({'时': time.strftime('%m-%d %H:%M:%S'), '项': 今}, open(档, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    except Exception as e:
        print('· 上回之印存不得（%s）——下回 --红 照全印' % e)
    return ok


def 记之缺(n, root=ROOT):
    t = open(os.path.join(root, 施工表), encoding='utf-8').read()
    项 = [('回执', bool(glob.glob(os.path.join(root, '设定', '回执_*_第%d章封版席.md' % n)))),
         ('锁定行', ('| %d | 锁定 |' % n) in t), ('悬账行', ('| %d | 悬账 |' % n) in t),
         ('创作记录', os.path.exists(os.path.join(root, '版本', '第%d章' % n, '_创作记录.md'))),
         ('全书记忆·章详记', os.path.exists(os.path.join(root, '设定', '全书记忆', '第%d章.md' % n))),
         ('下一章开镜卡', os.path.exists(os.path.join(root, '版本', '第%d章' % (n + 1), '_开镜卡.md'))),
         ('席记', os.path.exists(os.path.join(root, '版本', '第%d章' % n, '_席记.json')))]
    if n >= 分栏之始:          # ★1024 验席：记席留「‹器:键›」而未跑 记落.py 即交，器格成空壳入封——--後 拦之（N≤410 无此项）
        import 记落
        项 += [('占位未填·%s（跑 python3 工具/记落.py %d）' % (名, n), False) for 名, p in 记落.档们(n, root) + [('检察官', 记落.检察官)]
               if '‹器:' in (记落.读(p, root) or '')]
    return [k for k, ok in 项 if not ok]


def 可提交(n, 路们):
    """只收本章所及之处（⛔git add -A）：正文／本章与下一章之版本目录／设定／根之 .md 与 .html。"""
    # ★1013：记席按令改 工具/小说检察官.py 之 OPEN_BRIEF_CARD_SCHEMA[N+1]——旧只收 设定/ 等，此档永留未提交（381 实逮）
    #   ⛔1027：提示词系统之「--开拍 N+1」随十三轮之旧令汰（阶段之数⛔再改之），其档⛔收
    前缀 = ('正文/', '版本/第%d章/' % n, '版本/第%d章/' % (n + 1), '设定/', '工具/小说检察官.py',
          '阅读器/镇冢秘术_全本阅读器.html')        # ★1013：阅读器由本器同步，旧不收——381 实逮「不在本章所及之处」
    收 = [p for p in 路们 if p.startswith(前缀) or ('/' not in p and p.endswith(('.md', '.html')))]
    return 收, [p for p in 路们 if p not in 收]


def 末章之病(out):
    """检察官 --末章 之印 → 诸病（✗ 行之下诸条）；⛔「第十一轮未过」——其归 --後（399 --前 之假红）。"""
    L = out.split('\n')
    i = next((k for k, l in enumerate(L) if '✗' in l), None)
    if i is None:
        return ['（判不出：无 ✗ 行）']
    return [l.strip() for l in L[i + 1:] if l.strip() and not l.strip().startswith('第十一轮未过') and not l.strip().startswith('末章硬闸·')]


def 红行(out, 顶=15):
    """器之印中之红项（「✗」行、行首「⛔」而非 D6 之训者）——封版红时当面印，⛔只印末一行。"""
    出 = [l.strip() for l in out.split('\n') if l.strip() and ('✗' in l or l.strip().startswith('⛔')) and '永远的痛' not in l]
    return 出[:顶]


# 〔W908 环9·治8〕--试 之临时副本（clone --shared 本地之仓）无沙盒之活迹：_器之迹.jsonl（未踪）、origin 之 备份/报、章-*、巡应诸枝（本仓只有其 refs/remotes）——
#   法用之守 之证读之者於副本恒红（1120 实：473 之副本 ✓20 ⛔27、474 之副本 ✓20 ⛔26，俱此四类），--试 自 411 起止於 法用之守、其後诸闸（第十一轮、读者之快、读者之慢、医生、末章硬闸）恒不得演。
#   唯 --演：红行之因尽属此四类者只注（⚠·⛔计判）；余因（档含、废而未除、写者、完备、语截断……）照拦。真封（演=False）一字不变。
副本之缺 = (r'[^；\s（]+\.py(?: [^；（]*?)? 自本章之开（[^）]*）未跑(?:（迹[^）]*）)?',   # 法用之守.迹.查（证之「跑」俱 工具/ 之 .py）：副本无沙盒之器迹
          r'报/[^；\s]+ 无凭：备份/报 无此枝(?:（彼时）)?',            # 报之证：副本无 origin/备份/报
          r'origin 无 [^；\s]+(?: 之枝)?',                           # git 含／枝之证：副本无 origin 之枝
          r'未演（流程之法须真料演练方上）：演练账与 报/演 俱无其录')     # 验演：报/演 在 备份/报（副本无）
副本无活迹之语 = '副本无活迹（沙盒之器迹、origin 之 备份/报 与 章-*·巡应诸枝）'


def 副本之免(out):
    """〔W908 环9·治8〕法用之守 --验 之印 → (免, 余)：免＝其因尽属 副本之缺 之红行；余＝他红之行（照拦）。头行（「法用之守 --验」）不计。
    行式：「⛔ <id>（<据>）：因；因」「⛔ 待·<id>（限 N）：因——示」；不合其式之⛔行（完备、废而未除之类）俱入余。"""
    免, 余 = [], []
    for l in out.split('\n'):
        s = l.strip()
        if not s.startswith('⛔') or '法用之守 --验' in s:
            continue
        m = re.match(r'⛔ (待·)?[^（\s：]+（[^）]*）：(.+)$', s)
        剩 = (m.group(2).split('——')[0] if m.group(1) else m.group(2)) if m else s
        for p in 副本之缺:
            剩 = re.sub(p, '', 剩)
        (免 if m and not 剩.replace('；', '').strip() else 余).append(s)
    return 免, 余


def 後之闸(n, root=ROOT):
    """记席之档俱在之後、提交之前之序：→ [(名, 命令)]（红即停）。★1118：席记之「封版」段於此诸闸俱过之後方书（其凭）。
    ★1020 X21：⛔於此跳心跳 N+1——N+1 无席而锁在（空锁：自走判候、席在跑吗放行、全测之留字降黄；W53 验席所逮）。
      封版之活态之报撞断流之治在接力：其静自交棒之刻（本表第十一轮所产之 `_十一轮.json`）起算。
    ★1027 法用之守（N≥411）：已取之法本章无证即红、⛔提交（其验之末行入席记「法用」，下一章以之为前章已验之凭）。
    ★1027 A2（Variant S·flow／tools 二审之裁）：旧「全测·快」（405 实测 338 秒：跑轮负测 213、检察官自测 39、医生 38）→ 三闸俱拦：
      读者之快（全测 --快 --只 读者可见之快格·一秒余）、医生（检察官 --doctor：圣经之约、canon open_brief N+1、施工表、
      README 阶段与 CANON-ID、阅读器之同——记席与本器之同步所写）、末章硬闸（检察官 --末章 N）；医生与末章硬闸并起（後之并）。
      器之自测（跑轮负测、检察官自测……）归 GitHub autopush 之全闸一回（分等·器红入账）——⛔沙盒与 GitHub 同树二跑。
    ★1027 执行之核（线B·#44·坑㉞㉟㊹：左移之检只印不拦）：--前 所印之 质量三闸、席令之禁、圣经随裁、器物点名 N（各约一秒）
      於 --後 照拦（红即⛔提交）——旧只於 --前 印、记席若未治即封毕方於 GitHub 之闸红。器物点名唯本章有 _器物.md 方跑。
    〔1119 执行之审·治7〕读者之慢（全测 --只 全书检,书级体检,FS沉默闸·约廿余秒）：读者可见之慢格旧唯 GitHub 之全闸跑——
      416、449、451、452、471、472 六回俱封後方红（472：FS16 限471·治-79ef08a55 方入主枝）；今封前於沙盒跑、红即⛔提交。
      与 GitHub 同一组 chk_*（全测.诸项），⛔另写判；入後之并（与医生、末章硬闸并起·472 之演：读者之慢 22 秒、医生 7 秒，墙钟约增十五秒）。外声闸⛔入（其器恒 exit 0，入之拦不住）。
    〔W908 环9〕读者之慢一式取之（见 读者之慢之算：全测.读者可见之闸 − 负测·* − 全测.活态之格 − 已左移者 − 慢之豁免·各书其由）——
      旧三格之外添 抄袭闸、分量闸、亮点界、亮点在、净重对表、字数闸、含拍（章-471 分量闸封後方红之类）；数闸免（其负测改真仓之正文）。"""
    闸 = [('囤灰闸', [器('囤灰闸.py')])]
    if n >= 分栏之始:
        闸.append(('法用之守', [器('法用之守.py'), '--验', str(n)]))
    闸 += [(名, [器(档)] + 参 + (['--拦章', str(n)] if 名 == '全书记忆' else [])) for 名, 档, 参 in 左移之拦]   # ★1119 全书记忆 --拦章 N：缺、sha 格坏、稿无处可取凡章俱拦；残片唯本章拦，他章之残片只印（入全测 → 器红账）
    if os.path.exists(os.path.join(root, '版本', '第%d章' % n, '_器物.md')):
        闸.append(('器物点名', [器('器物点名.py'), str(n)]))
    return 闸 + [('第十一轮', [器('小说检察官.py'), '--十一轮', str(n)]),
                ('读者之快', [器('全测.py'), '--快', '--只', ','.join(读者之快)]),
                ('读者之慢', [器('全测.py'), '--只', ','.join(读者之慢 or 读者之慢之算())]),     # 〔1119 执行之审·治7〕後之并之首（最久者先起）；W908 环9 一式取之
                ('医生', [器('小说检察官.py'), '--doctor']), ('末章硬闸', [器('小说检察官.py'), '--末章', str(n)])]


左移之拦 = (('质量三闸', '质量三闸.py', []), ('席令之禁', '席令之禁.py', []), ('圣经随裁', '圣经随裁.py', []),   # 1027 #44：--前 印、--後 拦
         ('全书记忆', '全书记忆.py', []))   # ★X92（1109·435 限）：主环改正文後详记之 sha 不随（432 v02 入主枝、433 记席方逮）——--後 之瘦闸拦（0.1 秒）；治路：跑轮 --存 → 记落 N --重填


读者之快 = ('改单', '圣经引号', '坑账', '暂停令', '钩子挂载', '约到期闸')   # 全测·快之读者可见之格（俱在 全测.读者可见之闸）——红即拦
# 〔W908 环9·治7 之扩·⛔另立表〕读者之慢＝全测.读者可见之闸 − 负测·* − 全测.活态之格 − 已左移者（读者之快、左移之拦）− 慢之豁免——一式取之、⛔手列：
#   读者可见之闸添一非负测之格即自入封前（封前之闸与 GitHub 读者可见之闸同表：章-471 之分量闸、472 之 FS沉默闸 俱封後方红·Run 44516535483）；
#   序随 全测.诸项（⛔取集之序：str 之哈希每跑异）。红即拦（全测之 chk_* 同一·⛔另写判）。
#   回放（456—473 之封树十八·各以底之器与今之器跑，封前〔HEAD＝封之父、工作区＝封之树、席记 段.封版＝「待 封版.py」、工作流账＝父〕与封後各一）：
#     误红 0（前红而後绿者 0·依封後方生之档者无）；红者唯 471（全书检、分量闸）、472（FS沉默闸）——前後俱红、GitHub 亦红（真红·封前即拦）。
#   封前所增（474 之树三回之均）：後之并之墙钟 旧约 22 秒 → 约 31 秒（＋9 秒·零 token；读者之慢 31、医生 7、末章硬闸 0.2 并起）。
#   ⚠此式凡新入 读者可见之闸 之非负测格俱自入封前、无回放（如 W909 之并）：入闸之前先照上式回放 456 起之封树，误红（前红而後绿：其格读封後方生之档）即入 慢之豁免 并书由——⛔待写书之坐封时方见（误拦写书）。
慢之豁免 = {   # 名 → 由（⛔无由之免；自测钉其俱在 全测.读者可见之闸、俱⛔在封前之格）
    '外声闸': '其器恒 exit 0（全测.chk_outside_voice 只报不拦）——入之拦不住',
    '负测留字': '非 全测.诸项 之格：全测 main 跑毕之留字之查——--只 不认即恒「未认」而红',
    '数闸': ('其格并跑 负测_数闸，於真仓改旧章之正文再复原（负测_数闸.py:96-100）——与医生、末章硬闸并起即竞读其档；'
             '逾时被杀则所改之旧章留盘，随封版之提交入库（正文/ 在 可提交 之前缀）——伤书之质（质之铁律：不确即⛔入）；GitHub 之片各於一次性之树跑之、无此险'),
}


def 读者之慢之算(全=None):
    """〔W908 环9〕→ 读者之慢（tuple·序随 全测.诸项(非快)）：读者可见之闸 − 负测·* − 全测.活态之格 − 读者之快 − 左移之拦 − 慢之豁免。
    全 可注（自测之变异）。⛔手列。"""
    if 全 is None:
        import 全测 as 全
    已 = set(读者之快) | {x[0] for x in 左移之拦}
    return tuple(k for k, _ in 全.诸项(False) if k in 全.读者可见之闸 and not k.startswith('负测·')
                 and k not in 全.活态之格 and k not in 已 and k not in 慢之豁免)


try:
    读者之慢 = 读者之慢之算()   # 〔1119 执行之审·治7〕全测（非快）之读者可见之慢格——红即拦（W908 环9：一式取之）
except Exception:              # 全测之表读不得：本器之他用（--前、诸器之 import）照常；--後 之 後之闸 再算之即抛（⛔无闸而过）
    读者之慢 = ()
後之并 = ('读者之慢', '医生', '末章硬闸')      # 各载检察官约廿至三十秒：并起（〔1119 执行之审·治7〕读者之慢入之）
慢格之真迹 = (('f743735c641633bd0807a930a27cc6a750ad3c7c', 1),    # 〔1119 执行之审·治7〕自测之真迹回放：472 封版之树（GitHub 封後方红·FS16 限471）→ 红
            ('79ef08a55da2d54649a566cf3cc02e856b0d44b4', 0))    # 其治（治-79ef08a55·GitHub 绿而入主枝）→ 绿
活态之格 = ('接力', '跑账', '负测·自进化环')    # 全测并.活态 之余三（钩子挂载在 读者之快）：GitHub 之机读之皆空而假绿——封时於沙盒跑，只报、入器红账


def 後之存(n):
    """提交之後之序：→ [(名, 命令)]（红只报⚠）。末步撤锁（心跳.可收 守：心跳已属 N+1 者⛔清）。
    ★1027 A2：一章唯一推——`存底 --标 N`（章-N）；云端验（主枝未进即恒红·已删）、存底 --演（章-N 之克隆归 autopush 之 章-* 之取）、
      存底包（打了⛔送·接棒守 --候主 之非成之返方印）、跑账（--前 主环之职与活态之报已跑）俱去。"""
    return [('存底 --存', [器('存底.py'), '--存', '第%d章封版' % n]), ('存底 --标', [器('存底.py'), '--标', str(n)]),
            ('撤锁', [器('心跳.py'), '--收', str(n)])]


def 并起(诸, root=ROOT, 隔=0.5):
    """★1027 A2：医生与末章硬闸各载检察官约三十秒——并起（错开半秒：诸器一载 `_账` 即读改写 `_跑账.json`，无锁）。
    → {名: future→(rc, 印, 秒)}（与 跑() 同）。"""
    from concurrent.futures import ThreadPoolExecutor
    池 = ThreadPoolExecutor(max_workers=max(1, len(诸)))
    出 = {}
    for k, (名, a) in enumerate(诸):
        if k:
            time.sleep(隔)
        出[名] = 池.submit(跑, a, root)
    池.shutdown(wait=False)
    return 出


def 活态之报(n, root=ROOT):
    """★1027 A2：全测并.活态 读沙盒之现场（跑账、心跳、自进化环之脉、钩之挂载），GitHub 之机读之皆空而假绿
    （410 之 GitHub 之印：跑账「此刻无凭」作 ✓）——封时於沙盒跑其三：只报⚠、⛔拦；红入器红账（本地并云端·限三章治），
    绿者销其笔、余格之笔⛔动（全测._器红入账 之「跑过」：与 GitHub 之并判同一 器红之判，⛔另一份）。→ 红之名们"""
    d = tempfile.mkdtemp(prefix='封版活态_')
    try:
        出 = os.path.join(d, '果.json')
        rc, out, 秒 = 跑([器('全测.py'), '--只', ','.join(活态之格), '--出', 出], root)
        try:
            果 = json.load(open(出, encoding='utf-8')).get('果') or []
        except Exception:
            果 = []
    finally:
        shutil.rmtree(d, ignore_errors=True)
    已 = {x[0]: x for x in 果}
    红 = [k for k in 活态之格 if k not in 已 or not 已[k][1]]
    逾 = []
    try:
        import 全测
        逾 = 全测._器红入账(红, n, 活态之格)
    except Exception as e:
        print('  ⚠ 器红账未并（%s）' % e)
    print('  %s %-10s rc=%d %5.0fs  %s' % ('✓' if not 红 else '⚠', '活态之报', rc, 秒,
                                         '%s 俱绿' % '、'.join(活态之格) if not 红 else '器红（只报·入器红账限三章治）：' + '、'.join(红)))
    for k in 红:
        print('      ⚠ %s：%s' % (k, str((已.get(k) or [k, False, '未跑出果'])[2])[:150]))
    if 逾:
        print('      ⛔ 器红逾限：%s——已逾三章之限，先治（X55）' % '、'.join(逾))
    return 红


def 封毕之语(n):
    """封毕之下一步（1027 坑51·A2）：章-N 已触 GitHub autopush（一章唯此一推）——主环只候（零 token），⛔直推主枝、⛔沙盒再跑全闸。"""
    return ('✓ 封版毕（封版#%d 一提交、「章-%d」一推）。下一步（主环）：python3 工具/接棒守.py --候主 %d（run_in_background；零 token——'
            '「章-%d」已触 GitHub autopush，分片而闸、绿即并入主枝；坏报即早返其红：红者照其行治、提交、推.py 交治枝；逾限印 workflow_dispatch 之兜底）'
            % (n, n, n, n))


def 阶段之数(n, root=ROOT):
    """★X53·1021：README 阶段句随封版自改（零 token；旧由记席／主环手改，401 漏之即红於全测·快）。
    ⛔1027：提示词系统（十三轮之旧令，无一席读之）之「--开拍 N+1」⛔再改——其检（检察官医生之提示词系统一支）同日汰。
    ★1027 执行之核（线B·#60）：总站、人物册之「现状」一栏（「已写 1—N 章」）同法自改（旧停在 379·各站之细待 W11 一次重写，⛔追）。"""
    改 = []
    站式, 站新 = r'已写 <b>1—\d+ 章</b>（初稿号）；\d+ 起待写', '已写 <b>1—%d 章</b>（初稿号）；%d 起待写' % (n, n + 1)
    for 档, 式, 新 in (('README.md', r'第 1—\d+ 章已经同步封版；第 \d+ 章开写前', '第 1—%d 章已经同步封版；第 %d 章开写前' % (n, n + 1)),
                     ('镇冢秘术_总站.html', 站式, 站新), ('人物册_总纲_九站.html', 站式, 站新)):
        fp = os.path.join(root, 档)
        if not os.path.exists(fp):
            continue
        t = open(fp, encoding='utf-8').read()
        t2 = re.sub(式, 新, t, count=1)
        if t2 != t:
            open(fp, 'w', encoding='utf-8').write(t2); 改.append(档)
    return 改


def 後(n, 演=False, root=ROOT):
    if 演 and not os.path.exists(os.path.join(root, 演之记)):
        print('⛔ --演 只於 --试 所立之临时副本里跑（%s 不在）——⛔在真仓同步而不提交' % 演之记); return False
    print('════ 封版·後（第%d章）%s════' % (n, '·演（临时之副本：⛔席记、⛔提交、⛔推）' if 演 else ''))
    缺 = 记之缺(n, root)
    if 缺:
        print('⛔ 记席之档未齐：%s——回记席补（⛔本器代写）' % '、'.join(缺)); return False
    print('  ✓ 阶段之数    %s' % ('、'.join(阶段之数(n, root)) or '已是 %d／%d' % (n, n + 1)))
    步 = [('净重对表 --补', [器('净重对表.py'), '--补'], False), ('同步全本阅读器', [器('同步全本阅读器.py')], False),
         ('全书记忆随', [器('全书记忆.py'), '--随'], False),   # ★1024 实踩（410）：亮点添注而白文未动，详记之 sha 器随（零 token）
         ('剧情链', [器('剧情链.py')], False),          # ★1015 作者令：每章精读之详记串成从头到尾之链，封版即重生、随提交上 GitHub
         ('剧情全图', [器('剧情全图.py')], False),      # ★1119 W907 作者令「一眼……定位哪里有问题、哪里可升级」（法用#剧情全图）：诸源并一图（脊、开环、漏、升）——剧情链之後重生；写者唯一（唯此步与人手重跑）
         ('人物链', [器('人物链.py'), '--并记'], False),   # ★1015 作者议：每人从头到尾之链与每两人之关系——自记席之「在场之人」零 token 重并（虹吸）
         ('进化树随', [器('进化树.py'), '--随'], False),   # ★1119 作者令「进化路线·进化树……保存在 GitHub 的主线」（法用#进化树）：谱随三账——唯封版重写（写者唯一·⛔总编辑之坐与写书之坐两边各写而并冲突）；--验 绿即⛔动
         ('器之迹', [器('囤灰闸.py'), '--迹', str(n), '--写'], False),   # ★1015 作者议：每章从头到尾用了哪些器、每器之表现（败、慢、重跑）——自 _器之迹.jsonl 零 token
         ('体系总图', [器('体系总图.py')], False)]   # 〔1119·W909·法用#体系总图〕一件一行之体系总图（部、职、谁跑、谁读、末真用、用之审之判）——封版 --後 与总编辑之 --随治 重写（两写之并由 账并 之生成之图一支·W912）；居器之迹之後：末真用之窗含本章之迹，⛔封後即旧
    步 += [('回执对账', [器('回执对账.py')], True), ('开轮六检', [器('开轮六检.py'), str(n)], True),
          ('第零轮开镜庭', [器('第零轮开镜庭.py')], True), ('造式之实', [器('造式.py'), str(n)], True)]
    for 名, a, 必 in 步:
        rc, out, 秒 = 跑(a, root)
        末 = [l for l in out.split('\n') if l.strip()][-1:] or ['']
        print('  %s %-10s rc=%d %5.0fs  %s' % ('✓' if rc == 0 else '⛔', 名, rc, 秒, 末[0].strip()[:150]))
        if 必 and rc != 0:
            print('⛔ 停：%s 红——⛔提交；照其印治（记席之档或交总编辑）' % 名); return False
    闸, 并 = 後之闸(n, root), {}
    for i, (名, a) in enumerate(闸):
        if 名 in 後之并 and 名 not in 并:          # ★1027 A2：医生与末章硬闸至其位方并起（第十一轮之後：末章硬闸须其凭）；〔1119 执行之审·治7〕今读者之慢为其首、三者同起
            并.update(并起([x for x in 闸[i:] if x[0] in 後之并], root))
        rc, out, 秒 = 并[名].result() if 名 in 并 else 跑(a, root)
        末 = [l for l in out.split('\n') if l.strip()][-1:] or ['']
        免, 余 = 副本之免(out) if 演 and 名 == '法用之守' and rc != 0 else ([], [])   # 〔W908 环9·治8〕唯 --演：其红尽属 副本之缺 方免
        免 = [] if 余 else 免
        print('  %s %-10s rc=%d %5.0fs  %s' % ('✓' if rc == 0 else '⚠' if 免 else '⛔', 名, rc, 秒, 末[0].strip()[:150]))
        if 免:
            print('      ⚠ %s：%d 条只注（⛔计判）——首：%s' % (副本无活迹之语, len(免), 免[0][:100]))
        elif rc != 0:
            for l in 红行(out):      # ★1020 398 封版：红而只印末一行，须另跑方知何项——红则当面印其诸红项
                print('      ' + l)
            print('⛔ 停：%s 红——⛔提交' % 名); return False
        if 名 == '法用之守' and not 演:      # ★1027：其验入席记（随本章之提交上云；下一章之法用之守以此为前章已验之凭）
            _p = os.path.join(root, '版本', '第%d章' % n, '_席记.json')
            _j = json.load(open(_p, encoding='utf-8'))
            _j['法用'] = 末[0].strip()[:200]
            json.dump(_j, open(_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # ★1118 总编辑复核「负测·封版之凭」→改①：席记之「封版」段移於後之闸俱过之後方书（旧在诸闸之前：闸红而其段已书、记席之占「待 封版.py」先被覆）——
    #   其段即「诸闸真过」之凭（接力.有回执、十一轮哨 N≥368 兼认之），随封版#N 一提交；其文一字未改（新旧二器所书同）
    #   ⚠其副：囤灰闸丙验席记诸段俱在（含「封版」·囤灰闸.py:406）——旧器先书而掩其缺，今⛔先书：席记缺「封版」之键（记落未跑）即红「丙·第N章席记缺段：封版」；治＝重跑 记落（造章.js:428 记席之令、记落.席记之落 书「待 封版.py」之占），⛔手书 段.封版
    if not 演:
        p = os.path.join(root, '版本', '第%d章' % n, '_席记.json')
        j = json.load(open(p, encoding='utf-8'))
        j.setdefault('段', {})['封版'] = ('封版.py：净重对表补、阅读器同步、回执对账、开轮六检、开镜庭、造式之实、囤灰闸、第十一轮、读者可见之快格与慢格、医生、末章硬闸俱过；'   # 〔1119 执行之审·治7〕慢格（W908 环9：读者之慢之算 一式取之）
                                       '提交（复盘、交接同载）、存底、推章-%d（全闸交 GitHub autopush）、撤锁（%s）' % (n, time.strftime('%Y-%m-%d', time.gmtime())))
        json.dump(j, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    活态之报(n, root)
    if 演:
        print('✓ 演毕：诸闸俱过（⛔席记、⛔提交、⛔推）'); return True
    st = subprocess.run(['git', '-c', 'core.quotepath=off', 'status', '--porcelain', '-uall'], cwd=root, capture_output=True, text=True).stdout
    路们 = [l[3:].strip().strip('"') for l in st.split('\n') if l.strip()]
    收, 弃 = 可提交(n, 路们)
    if 弃:
        print('  · 不在本章所及之处、⛔提交：%s' % '、'.join(弃))
    件 = 章之件标成(n, root)          # ★X86（1105·425 还账）：本章之 W 於封版 --後 即标已成（其账随封版#N 一提交）——⛔待下坐之开补
    if 件 and '设定/工作流账.json' not in 收:
        收.append('设定/工作流账.json')
    名 = re.sub(r'^.*?第.+?章_?', '', os.path.basename(正文档(n, root) or ''))[:-3]
    subprocess.run(['git', 'add', '--'] + 收, cwd=root, check=True)
    # ★1013：说明须标「封版#N」——改单闸认之为「新章封版之追记（係添不係改）」；缺之则推时改单红（381 实逮）
    msg = ('第%d章《%s》封版（造式二代·封版#%d）：诸闸、第十一轮、读者可见之快格与慢格、医生、末章硬闸俱过（全闸交 GitHub autopush）——'   # 〔1119 执行之审·治7〕
           '记席之档（回执、锁定行、创作记录、全书记忆、状态册、open_brief、第%d章开镜卡）、复盘、交接\n\n%s' % (n, 名, n, n + 1, 尾))
    r = subprocess.run(['git', 'commit', '-q', '-m', msg], cwd=root, capture_output=True, text=True)
    print('  %s 提交 %s' % ('✓' if r.returncode == 0 else '⛔', subprocess.run(['git', 'log', '--oneline', '-1'], cwd=root, capture_output=True, text=True).stdout.strip()[:100]))
    if r.returncode != 0:
        print(r.stdout + r.stderr); return False
    标败 = None
    for 名, a in 後之存(n):
        rc, out, 秒 = 跑(a, root)
        末 = [l for l in out.split('\n') if l.strip()][-1:] or ['']
        print('  %s %-8s rc=%d %5.0fs  %s' % ('✓' if rc == 0 else '⚠', 名, rc, 秒, 末[0].strip()[:150]))
        if 名 == '存底 --标' and rc != 0:
            标败 = 末[0].strip()[:150]
    if 标败 is not None:   # ★1027 A2 验：一章唯此一推——败而仍印「封版毕」，主环 --候主 白候九十分（无章-N 即无 autopush、无报），逾限之 workflow_dispatch 亦无其枝
        print(标推未成之语(n, 标败)); return False
    print(泊章之语(n, root))   # ★1117（GitHub 化之审·I·法用#停钩空转）：章-N 已在云端 → 本地泊於「章-N」，候主之快进归主枝；败即照旧（只报⚠）
    print(封毕之语(n))
    return True


def 章之件标成(n, root=ROOT):
    """X86：工作流账中名起「第N章」之件（一章一 W）未成者 → 工作流账.标(已成)（其自核照旧；拒即⚠、⛔拦封——下坐之开仍补）。回所标之 id 或 None。"""
    try:
        import 工作流账 as 账
        p = os.path.join(root, 账.账档)
        件们 = [x for x in json.load(open(p, encoding='utf-8'))['件'] if str(x.get('名', '')).startswith('第%d章' % n)]
        if not 件们 or 件们[-1].get('状态') == '已成':
            return None
        i = 件们[-1]['id']
        if 账.标(i, '已成', root):
            print('  ✓ 工作流账    %s 已成（随封版#%d 之提交·X86）' % (i, n)); return i
        print('  ⚠ 工作流账    %s 拒标已成（照其由治；下坐之开仍补）' % i)
    except Exception as e:
        print('  ⚠ 工作流账    未标：%s' % str(e)[:120])
    return None


def 泊章之语(n, root=ROOT):
    """★1117（GitHub 化之审·I·法用#停钩空转）：「章-N」推成 → 本地泊於「章-N」（推报.泊）。平台 Stop 钩以 origin/<当前枝> 量「未推」——
    封後本地主枝超 origin 主枝至 autopush 并之，每回合之末其钩报未推、空转二回；泊後其量 0（真未推之提交照报）；--候主 之快进归主枝。
    ⛔抛、⛔拦（泊不成即照旧·只印 ⚠）。→ 印之行"""
    try:
        import 推报
        ok, 语 = 推报.泊('章-%d' % int(n), root)
    except Exception as e:
        ok, 语 = False, '泊不成（照旧）：%s' % str(e)[:120]
    return '  %s %-8s %s' % ('✓' if ok else '⚠', '泊', 语.lstrip('✓·⚠ '))


def 标推未成之语(n, 由=''):
    """封版之提交已成而「章-N」未推上（1027 A2 验：一章唯此一推，败即当场红、⛔候主）。"""
    return ('⛔ 封版#%d 之提交已成而「章-%d」未推上（%s）——autopush 未触、⛔候主：先 `python3 工具/存底.py --标 %d`'
            '（HEAD 即封版#%d 之提交；或 `python3 工具/自进化环.py` 之 L0 缺碑自补），成後 `python3 工具/接棒守.py --候主 %d`'
            % (n, n, 由 or '推败', n, n, n))


# ═══ 演练（1027 A2·丝滑主义：改流程之器先演於真料、⛔径上线）═══
演之记 = '.封版之演'      # --试 所立临时副本之记（其文＝底之提交）；--演 见之方跑——⛔在真仓同步而不提交
纯同步之档 = ('README.md', '镇冢秘术_总站.html', '人物册_总纲_九站.html', '阅读器/镇冢秘术_全本阅读器.html',
            '设定/全书记忆/剧情链.md', '设定/全书记忆/剧情全图.md', '设定/全书记忆/人物链/')   # 唯本器之同步所写（⛔记席所写）：演时复其前之样，令同步真重生之
活迹之档 = ('版本/第%d章/_器之迹.md',)   # 记沙盒当时之器迹（_器之迹.jsonl 与「前章封版→本章封」之窗·W922 环2）——⛔可重放，只注不比
时戳之凭 = ('_十一轮.json', '_总核.json')   # 第十一轮重跑即新其「时」与「流」（跑者之号·跑轮._stream_id）——余键须同（左眼、右眼、软项、版数……）
跑者之键 = ('时', '流')
器生之档 = ('设定/进化链.md', '设定/进化树.md', '设定/体系总图.md', '设定/执行清单.md')   # 〔W921 环7〕执行清单 与 体系总图 同为其写步所生（清单()）——只注其摘   # 1119：进化树之谱带「截至 HEAD」，副本之 HEAD 异即变——只注其摘   # 进化链.py 自盘上诸器重写（活态之报之 负测·自进化环 → L3）：随今之器（叠器）而变，⛔同步之档——只注其摘   # 〔W909〕体系总图自今之器（叠器）与诸章之迹（活迹）重生——只注其摘
章之料档 = {'工具/小说检察官.py': r'(?ms)^OPEN_BRIEF_CARD_SCHEMA = \{\n.*?^\}\n'}   # 器档而载章之料（记席所写之块）：叠今之器时码随今、其块随底
演练账 = os.path.join('设定', '演练账.json')


_定库之变 = ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_COMMON_DIR', 'GIT_OBJECT_DIRECTORY', 'GIT_ALTERNATE_OBJECT_DIRECTORIES')


def _g(a, root, 字=True, **k):
    """⛔承外之 GIT_DIR 诸变（钩中跑自测即带之）——库只由 root 定（同 推报._git）。"""
    e = {x: v for x, v in os.environ.items() if x not in _定库之变}
    return subprocess.run(['git', '-c', 'core.quotepath=off'] + a, cwd=root, capture_output=True, text=字, env=e, **k)


def 封之笔(n, root=ROOT, 范=None):
    """第 n 章封版之提交——其信带「（造式二代·封版#n）」「（封版#n）」「（封版#n·改单#…）」之类（⛔误认 #n0、⛔认「封版#n 之後」之笔）。
    范：所寻之引们（默 HEAD 之史、无则 --all）。无即 None。
    （封版之演、自进化环 L0 缺碑、自走 本树已封、接棒守 存底之封 同此一把尺——⛔各写一份）"""
    式 = re.compile(r'[（·]封版#%d[）·]' % int(n))
    for 引 in ([list(范)] if 范 else [['HEAD'], ['--all']]):
        r = _g(['log', '--format=%H%x09%s', '-F', '--grep=封版#%d' % int(n)] + 引, root)
        for l in (r.stdout or '').split('\n'):
            h, _, s = l.partition('\t')
            if h and 式.search(s):
                return h
    return None


def 叠器(root, 仓, 底):
    """今之器（工具／.claude／.github：已提交、未提交、新增、已删）叠於副本→ 所叠之路们。
    章之料档（器档而载章之料，如检察官之 OPEN_BRIEF_CARD_SCHEMA）：码随今之器、其块随底（1027 合流之演：旧式整档留底，
    底之检察官犹调已汰之器——开轮六检之 _cold_done、提示词系统之档——末章硬闸、医生假红）；两边俱寻不着其块即⛔叠（整档留底）。"""
    改 = _g(['diff', '--name-only', 底, '--', '工具', '.claude', '.github'], root).stdout.split('\n')
    新 = _g(['ls-files', '--others', '--exclude-standard', '--', '工具', '.claude', '.github'], root).stdout.split('\n')
    叠 = []
    for p in sorted(set(x.strip() for x in 改 + 新 if x.strip())):
        源, 去 = os.path.join(root, p), os.path.join(仓, p)
        if p in 章之料档:
            式 = re.compile(章之料档[p])
            try:
                今, 旧 = open(源, encoding='utf-8').read(), open(去, encoding='utf-8').read()
            except OSError:
                continue
            m今, m旧 = 式.search(今), 式.search(旧)
            if not (m今 and m旧):
                continue
            open(去, 'w', encoding='utf-8').write(今[:m今.start()] + m旧.group(0) + 今[m今.end():])
            叠.append(p)
            continue
        if os.path.exists(源):
            os.makedirs(os.path.dirname(去), exist_ok=True)
            shutil.copy2(源, 去)
        elif os.path.exists(去):
            os.remove(去)
        叠.append(p)
    return 叠


def 复同步(仓, 底):
    """底（封版之提交）所改之纯同步之档复其前（底^）之样——同步须真重生之，⛔因已在而空过。→ 所复之路们"""
    前, 复 = 底 + '^', []
    for p in [x.strip() for x in _g(['diff', '--name-only', 前, 底], 仓).stdout.split('\n') if x.strip()]:
        if p in 纯同步之档 or any(q.endswith('/') and p.startswith(q) for q in 纯同步之档):
            if _g(['cat-file', '-e', '%s:%s' % (前, p)], 仓).returncode == 0:
                _g(['checkout', 前, '--', p], 仓)
            elif os.path.exists(os.path.join(仓, p)):
                os.remove(os.path.join(仓, p))
            复.append(p)
    return 复


def _块(root, 版, p):
    r = _g(['show', '%s:%s' % (版, p)], root, 字=False)
    return r.stdout if r.returncode == 0 else None


def 演之比(仓, 底, n, 叠, root=ROOT):
    """副本跑毕 → (差, 注)：凡异於底之档（叠器与演之记除外）——活迹只注；十一轮之凭唯「时」新者注；余俱入差，
    并寻真仓之史里底之後此档之他版，逐字同者注其「後治」（例：410 之详记 sha 封後方由坑㊾之治随之）。"""
    差, 注 = [], []
    变 = [x for x in _g(['diff', '--name-only', 底], 仓).stdout.split('\n') if x.strip()]
    新 = [x for x in _g(['ls-files', '--others', '--exclude-standard'], 仓).stdout.split('\n') if x.strip()]
    活 = [x % n for x in 活迹之档]

    def 摘(p):          # 所异之行（至多四行·各截百字）——账里自明其异在何处
        L = _g(['diff', '-U0', 底, '--', p], 仓).stdout.split('\n')
        return [l[:100] for l in L if l.startswith(('+', '-')) and not l.startswith(('+++', '---'))][:4]
    for p in sorted(set(变 + 新)):
        if p in 叠 or p == 演之记:
            continue
        if p in 活:
            注.append({'档': p, '因': '活迹：记沙盒当时之器迹（_器之迹.jsonl 与前章封版至本章封之窗），⛔可重放——只注不比'}); continue
        if os.path.basename(p) in 时戳之凭 and p in 变:
            try:
                甲 = json.loads(_块(仓, 底, p).decode('utf-8')); 乙 = json.load(open(os.path.join(仓, p), encoding='utf-8'))
                if {k: v for k, v in 甲.items() if k not in 跑者之键} == {k: v for k, v in 乙.items() if k not in 跑者之键}:
                    注.append({'档': p, '因': '第十一轮之凭：唯「时」「流」（跑之时、跑者之号）新——重跑即新，余键俱同'}); continue
            except Exception:
                pass
        if p in 器生之档:
            注.append({'档': p, '因': '器生：进化链、进化树、体系总图（并其执行清单）自盘上诸器（叠今之器）与迹重写——随叠器而变，非同步之档', '摘': 摘(p)}); continue
        今 = open(os.path.join(仓, p), 'rb').read() if os.path.exists(os.path.join(仓, p)) else None
        後治 = ''
        for h in _g(['log', '--format=%H', '%s..HEAD' % 底, '--', p], root).stdout.split():
            if 今 is not None and _块(root, h, p) == 今:
                後治 = '%s %s' % (h[:12], _g(['log', '-1', '--format=%s', h], root).stdout.strip()[:80]); break
        d = {'档': p, '何': ('与封版之提交不同' if p in 变 else '封版之提交无此档') if 今 is not None else '副本里无之'}
        if 後治:
            d['後治'] = '与其後之笔逐字同：' + 後治
        if p in 变:
            d['摘'] = 摘(p)
        差.append(d)
    return 差, 注


_判行 = re.compile(r'^\s+(✓|⛔|⚠)\s+(\S+(?: --\S+)?)\s+rc=(-?\d+)')   # 名可带一参（「净重对表 --补」）


def 诸闸之判(印):
    """--後 之印 → {名: ✓／⛔／⚠}（同步、诸检、诸闸、活态之报之行）。"""
    return {m.group(2): m.group(1) for m in (_判行.match(l) for l in 印.split('\n')) if m}


def 写演练账(录, root=ROOT):
    p = os.path.join(root, 演练账)
    try:
        账 = json.load(open(p, encoding='utf-8'))
        账 = 账 if isinstance(账, list) else []
    except Exception:
        账 = []
    账.append(录)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(账, f, ensure_ascii=False, indent=1)
        f.write('\n')


def 演练(n, root=ROOT, 记=True):
    """--後 --试：取第 n 章封版之提交为底，立临时之副本（clone --shared，己之 config：钩子挂载之自愈⛔动真仓）、叠今之器、
    复纯同步之档於其前，於副本里跑 `封版.py n --後 --演`（同步、诸检、诸闸、活态之报；⛔席记、⛔提交、⛔推、⛔存底），
    比同步之档於底（逐字）、比诸闸之判於其实（底在＝其时诸闸俱过）。果入 设定/演练账.json（id、何、料、底、果、差、注、闸、判、秒、时）。"""
    t0 = time.time()
    print('════ 封版·後·试（第%d章·演於真料）════' % n)
    底 = 封之笔(n, root)
    if not 底:
        print('⛔ 第%d章封版之提交（造式二代·封版#%d）寻不着——⛔演' % (n, n)); return False
    目 = tempfile.mkdtemp(prefix='封版演_')
    仓 = os.path.join(目, '仓')
    try:
        r = _g(['clone', '-q', '--shared', '--no-checkout', root, 仓], 目)
        if r.returncode == 0:
            r = _g(['checkout', '-q', '--detach', 底], 仓)
        if r.returncode != 0:
            print('⛔ 副本立不成：%s' % (r.stderr or r.stdout).strip()[:200]); return False
        叠 = 叠器(root, 仓, 底)
        复 = 复同步(仓, 底)
        open(os.path.join(仓, 演之记), 'w').write(底 + '\n')
        print('  · 底 %s｜叠今之器 %d 档｜纯同步之档复其前 %d：%s' % (底[:12], len(叠), len(复), '、'.join(复) or '无'))
        p = subprocess.run([sys.executable, os.path.join(仓, '工具', '封版.py'), str(n), '--後', '--演'], cwd=仓,
                           capture_output=True, text=True, timeout=3600)
        印 = p.stdout + p.stderr
        print('\n'.join('  │ ' + l for l in 印.rstrip().split('\n')))
        闸 = 诸闸之判(印)
        差, 注 = 演之比(仓, 底, n, 叠, root)
    finally:
        shutil.rmtree(目, ignore_errors=True)
    if 闸.get('活态之报') == '⚠':
        _活红 = [l.strip()[1:].strip()[:60] for l in 印.split('\n') if l.strip().startswith('⚠ ') and ' rc=' not in l
                and 副本无活迹之语 not in l]     # 〔W908 环9〕法用之守之免行另注（下）
        注.append({'档': '（活态之报）', '因': '活态之格读沙盒之现场（存底枝、心跳、跑账、自进化环之脉）——临时之副本无之而红，只报（⛔计判）：'
                   + '｜'.join(_活红)[:300]})
    if 闸.get('法用之守') == '⚠':      # 〔W908 环9·治8〕其红尽属 副本之缺（後 之 --演 判之）：只注；余证（档含、废、写者、完备）照判
        注.append({'档': '（法用之守）', '因': '法用之守之活迹诸证：%s——只注（⛔计判）：' % 副本无活迹之语
                   + '｜'.join(l.strip()[:80] for l in 印.split('\n') if 副本无活迹之语 in l)[:300]})
    演判 = '过' if p.returncode == 0 and 闸 and all(v != '⛔' for v in 闸.values()) else '拦'
    果 = '同' if (not 差 and 演判 == '过') else '异'
    # 结：异之性——唯「後治」之异（副本与封版之提交异、而与其後真仓所落之治逐字同：今之序於封时即治其旧红）与「未解之异」分说
    结 = ('同：同步之档逐字同、诸闸之判同' if 果 == '同' else
          '唯後治之异：%s 异於封版之提交而与其後之治逐字同（今之序於封时即治其旧红）；诸闸之判同（过）' % '、'.join(d['档'] for d in 差)
          if 演判 == '过' and all(d.get('後治') for d in 差) else
          '未解之异：%s；诸闸之判 演%s／实过' % ('、'.join(d['档'] for d in 差 if not d.get('後治')) or '（无）', 演判))
    录 = {'id': '封版後演·%d·%s' % (n, time.strftime('%Y%m%dT%H%M', time.gmtime())),
          '何': '封版 --後 之新闸（1027 A2·Variant S：读者之快、医生、末章硬闸代全测·快；後之存去云端验、存底 --演、存底包、跑账）於真料重放',
          '料': '第%d章' % n, '底': 底[:12], '果': 果, '结': 结, '差': 差, '注': 注, '复': 复, '闸': 闸,
          '判': {'实': '过（封版之提交在＝其时诸闸俱过）', '演': 演判}, '秒': int(time.time() - t0),
          '时': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    for d in 差:
        print('  ⛔ 差：%s（%s）%s' % (d['档'], d['何'], ('｜' + d['後治']) if d.get('後治') else ''))
    for d in 注:
        print('  · 注：%s——%s' % (d['档'], d['因']))
    print('  %s 演练：果「%s」｜诸闸之判 演%s／实过｜同步之档异 %d｜%d 秒' % ('✓' if 果 == '同' else '⛔', 果, 演判, len(差), 录['秒']))
    print('  · 结：' + 结)
    if 记:
        写演练账(录, root)
        print('  · 已入 %s（id %s）' % (演练账, 录['id']))
    return 果 == '同'


def _封之笔之局():
    """演练诸器之局（临时之二仓·⛔钉真仓之史：浅克隆亦通）：封之笔认「封版#9」⛔误认「封版#90」；复同步复纯同步之档於底^；
    演之比：叠器⛔比、活迹只注、十一轮之凭唯时新只注、余入差（其後之笔逐字同者注後治）、新增之档入差；
    叠器：删者删、改者叠；章之料档码随今、其块随底。"""
    d = tempfile.mkdtemp(prefix='封版演局_')
    env = dict({k: v for k, v in os.environ.items() if not k.startswith('GIT_')}, GIT_CONFIG_GLOBAL=os.devnull,
               GIT_AUTHOR_NAME='t', GIT_AUTHOR_EMAIL='t@t', GIT_COMMITTER_NAME='t', GIT_COMMITTER_EMAIL='t@t')
    阅 = '阅读器/镇冢秘术_全本阅读器.html'

    def 写(根, 档们):
        for p, t in 档们.items():
            os.makedirs(os.path.dirname(os.path.join(根, p)), exist_ok=True)
            open(os.path.join(根, p), 'w', encoding='utf-8').write(t)

    def 提(根, 档们, 信):
        写(根, 档们)
        subprocess.run(['git', 'add', '-A'], cwd=根, env=env, capture_output=True)
        subprocess.run(['git', '-c', 'commit.gpgsign=false', 'commit', '-q', '-m', 信], cwd=根, env=env, capture_output=True)
        return subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=根, env=env, capture_output=True, text=True).stdout.strip()
    try:
        源, 仓 = os.path.join(d, '源'), os.path.join(d, '仓')
        subprocess.run(['git', 'init', '-q', 源], env=env, capture_output=True)
        旧式 = 提(源, {阅: '旧', '设定/s.md': '甲', '工具/q.py': 'x', '设定/进化链.md': '链1'}, '第8章《丙》封版（封版#8·改单#G1）：旧式之信')
        底 = 提(源, {阅: '新', '版本/第9章/_十一轮.json': '{"时": "1", "流": "S1", "左眼": "过"}', '版本/第9章/_器之迹.md': '迹1',
                     '版本/第9章/_总核.json': '{"时": "1", "版数": 5}'},
               '第9章《甲》封版（造式二代·封版#9）：诸闸')
        提(源, {'设定/u.md': '戊'}, '封版#9 之後：回修案之格')
        後 = 提(源, {'设定/s.md': '乙'}, '後治：s')
        提(源, {'设定/t.md': '丙'}, '第90章《乙》封版（造式二代·封版#90）：诸闸')
        subprocess.run(['git', 'clone', '-q', 源, 仓], env=env, capture_output=True)
        subprocess.run(['git', 'checkout', '-q', '--detach', 底], cwd=仓, env=env, capture_output=True)
        复 = 复同步(仓, 底)
        复了 = open(os.path.join(仓, 阅), encoding='utf-8').read() == '旧'
        写(仓, {阅: '新', '版本/第9章/_十一轮.json': '{"时": "2", "流": "S2", "左眼": "过"}', '版本/第9章/_器之迹.md': '迹2',
               '版本/第9章/_总核.json': '{"时": "2", "版数": 6}',
               '设定/s.md': '乙', '设定/新.md': '丁', '工具/q.py': 'y', '设定/进化链.md': '链2'})
        差, 注 = 演之比(仓, 底, 9, ['工具/q.py'], 源)
        # 叠器：删者删、改者叠；章之料档（检察官）码随今、OPEN_BRIEF_CARD_SCHEMA 之块随底（回灌：整档留底即旧码调已汰之器）
        叠源, 叠仓 = os.path.join(d, '叠源'), os.path.join(d, '叠仓')
        subprocess.run(['git', 'init', '-q', 叠源], env=env, capture_output=True)
        叠底 = 提(叠源, {'工具/小说检察官.py': "import 旧器\nOPEN_BRIEF_CARD_SCHEMA = {\n    9: '底之卡',\n}\nX = 1\n", '工具/汰.py': 'x', '工具/留.py': '1'}, 'c')
        subprocess.run(['git', 'clone', '-q', 叠源, 叠仓], env=env, capture_output=True)
        os.remove(os.path.join(叠源, '工具', '汰.py'))
        写(叠源, {'工具/小说检察官.py': "import 新器\nOPEN_BRIEF_CARD_SCHEMA = {\n    9: '底之卡',\n    10: '後之卡',\n}\nX = 2\n", '工具/留.py': '2'})
        叠 = 叠器(叠源, 叠仓, 叠底)
        叠了 = (sorted(叠) == ['工具/小说检察官.py', '工具/汰.py', '工具/留.py'] and not os.path.exists(os.path.join(叠仓, '工具', '汰.py'))
               and open(os.path.join(叠仓, '工具', '留.py')).read() == '2'
               and open(os.path.join(叠仓, '工具', '小说检察官.py'), encoding='utf-8').read()
               == "import 新器\nOPEN_BRIEF_CARD_SCHEMA = {\n    9: '底之卡',\n}\nX = 2\n")
        return (叠了 and 封之笔(9, 源) == 底 and 封之笔(90, 源) not in (None, 底) and 封之笔(8, 源) == 旧式 and 封之笔(7, 源) is None
                and 封之笔(9, 源, ['HEAD~4']) is None and 封之笔(9, 源, ['HEAD~3']) == 底
                and 复 == [阅] and 复了 and [x['档'] for x in 注] == ['版本/第9章/_十一轮.json', '版本/第9章/_器之迹.md', '设定/进化链.md']
                and 注[2]['摘'] == ['-链1', '+链2'] and 差[1].get('摘') == ['-甲', '+乙']
                and [(x['档'], x['何']) for x in 差] == [('版本/第9章/_总核.json', '与封版之提交不同'), ('设定/s.md', '与封版之提交不同'), ('设定/新.md', '封版之提交无此档')]
                and 差[1].get('後治', '').startswith('与其後之笔逐字同：' + 後[:12]) and '後治' not in 差[2] and '後治' not in 差[0])
    except Exception:
        return False
    finally:
        shutil.rmtree(d, ignore_errors=True)


_慢格行 = re.compile(r'^\s+(✓|✗)\s+(\S+)\s')    # 全测.只跑 之每格一行（「  ✓ 名   语」）


def 慢格之回放(真迹=慢格之真迹, root=ROOT, 限=600):
    """〔1119 执行之审·治7〕「读者之慢」之真迹回放（自测之格）：每底立临时之 worktree（detach 於底；⛔clone --shared——
    GitHub 之片係省取〔partial clone〕，史之大档须由其 promisor 懒取，独 worktree 共其库与 config 方取得），
    以 後之闸 所生之「读者之慢」之命令（器之路改根於其树）於其树里跑——器即底之树之器（⛔叠今之器：史之树一字不移，
    回放永可复，⛔随今器之漂而诬红）；诸底并起（各约廿余秒）。→ {底: (rc, {格: ✓／✗}, 印末)}；树立不成 → (None, {}, 由)。
    〔1119 执行之审·复核〕⛔入 --自测（负测·封版 在 全测.读者可见之闸·阻推）：各树以其自身之器跑，⛔验今之器，其果恒同（一回之证即足）；
    而每跑立二树（各 11,529 档／288MB）、约廿五秒（旧 0.75 秒）、省取之片（gate.yml blob:limit=1m）懒取逾 1MB 之档、动真库之 .git/worktrees——
    徒加阻推之闸之时与败源。今唯手跑 `封版.py --回放慢格`；--自测 留静验（argv、後之并、全表之名）与 Barrier(3) 之并起之验。"""
    from concurrent.futures import ThreadPoolExecutor
    命 = dict(後之闸(472, '/无此根')).get('读者之慢')
    if not 命:
        return {底: (None, {}, '後之闸无「读者之慢」之格') for 底, _ in 真迹}
    e = {x: v for x, v in os.environ.items() if x not in _定库之变}
    目 = tempfile.mkdtemp(prefix='封版慢格_')

    def 一(底):
        树 = os.path.join(目, 底[:12])
        r = _g(['worktree', 'add', '-q', '--detach', 树, 底], root)
        if r.returncode != 0:
            return None, {}, '树立不成：%s' % (r.stderr or r.stdout).strip()[:200]
        a = [os.path.join(树, '工具', x[len(器('')):]) if x.startswith(器('')) else x for x in 命]
        try:
            p = subprocess.run([sys.executable] + a, cwd=树, capture_output=True, text=True, timeout=限, env=e)
            rc, 印 = p.returncode, p.stdout + p.stderr
        except subprocess.TimeoutExpired:
            rc, 印 = 124, '（逾 %d 秒未毕）' % 限
        return rc, {m.group(2): m.group(1) for m in (_慢格行.match(l) for l in 印.split('\n')) if m}, 印.strip()[-300:]
    try:
        with ThreadPoolExecutor(max_workers=max(1, len(真迹))) as 池:
            return dict(zip([底 for 底, _ in 真迹], 池.map(一, [底 for 底, _ in 真迹])))
    finally:
        剪 = [_g(['worktree', 'remove', '--force', os.path.join(目, 底[:12])], root).returncode for 底, _ in 真迹]
        shutil.rmtree(目, ignore_errors=True)
        if any(剪):          # 未立或删不成者：其记随目之去而剪（⛔留残树於 .git/worktrees）
            _g(['worktree', 'prune'], root)


def 自测():
    ok = 共 = 0
    d = 数(380)
    # 据 380 锁定行亲核之数（施工表 | 380 | 锁定 |）：白文 1 至 107 行、亮点 109、净重与六数（照锁定行现取）、末版、「＊」4 处（五拍）、与末版逐字同
    共 += 1; ok += (d.get('白文') == '1 至 107 行' and d.get('亮点行') == 109)
    # ★1020：净重与六数⛔钉快照（2572）——还账施改白文（380·v05，1020）後锁定行由 净重对表 --补 重量为 2,559，旧格遂红於快测；
    #   今照其注之本义「与其锁定行亲核之数逐个同」：取施工表 380 锁定行之六数比之（正文改而锁定行未补 → 仍红）
    _锁 = re.search(r'净重([\d,]+)｜段数\d+｜长段数\d+｜嗅\d+｜触\d+｜四字串三现\d+',
                   next((l for l in open(os.path.join(ROOT, 施工表), encoding='utf-8') if l.startswith('| 380 | 锁定 |')), ''))
    共 += 1; ok += (_锁 is not None and d.get('净重') == int(_锁.group(1).replace(',', '')) and re.fullmatch(r'v\d\d', d.get('末版') or '') is not None
                   and d.get('六数') == _锁.group(0).replace(',', ''))   # ★1015：末版⛔钉 v03（还账施改骨记即存新版——坑二十八之家）
    共 += 1; ok += (d.get('＊') == 4 and d.get('拍') == 5 and re.fullmatch(r'[0-9a-f]{12}', d.get('sha1', '')) is not None and d.get('与末版同') is True)   # ★sha1 ⛔钉快照：白文之数（行、净重、拍）不随骨记之改而变，sha1 随之变
    共 += 1; ok += (d.get('总纲') == '| 380 | 主·148 |')
    _证 = 机械之证(390)                       # ★1015 W33 之改：据 390 记席手查之果（回执 §六：骨记引句俱合、对白 8 行皆钱满 :15…:125）
    共 += 1; ok += (len(_证) == 6 and '不合 0' in _证[0] and _证[2].startswith('③对白之行 8：:15、:99'))
    # ★W60 X37：骨记之引逐条机核——造局於字串（⛔钉盘上会长之数）：全角冒号、区间（至／略号分段）、逾四十字之原句、
    #   本章（：行）、续引（、：行）、Ｄ6／总纲之号⛔认、跨章区间⛔认、不足四字不核、±1 之界、章不在、行逾白文、远引四字之共与印行
    _长 = '天地玄黄宇宙洪荒日月盈昃辰宿列张寒来暑往秋收冬藏闰余成岁律吕调阳云腾致雨露结为霜金生丽水玉出昆冈'
    _错 = _长[:24] + '错字错字'                 # 句首二十四字俱对、其尾错
    _白们 = {12: ['子丑寅卯辰', '甲乙丙丁戊', '“一二三四五，”他说。', '己庚辛壬癸', '', _长],
            13: ['戌亥甲子乙丑丙寅', '问话，尾巴没有往上走。', '上头一张是复印的悬赏。'], 900: ['# 第九百章', '本章之一句话在此。']}
    _骨 = ('【本章亮点】\na（12：3「一二三四五，」）。b 12:1「己庚辛壬癸」。c 12：2至4「甲乙丙丁戊……己庚辛壬癸」。d 12:6「%s」。e 12:6「%s」。'
          'f 拍一（：2）「本章之一句话在此。」。g Ｄ6：2「本章之一句话在此」、总纲：2「本章之一句话在此」。h 13:1「子丑」。'
          'i （13：2 尾巴没有往上走之翻）。j 背冲街坐（13：3 悬赏在身）。k 12：2至13：3。l 12：1、：4「己庚辛壬癸」。'
          'm 14:1「此章不在其书」。n 12:99「甲乙丙丁戊」。') % (_长, _错)
    _核 = 骨引之核(_骨, 900, 白们=_白们)
    _印 = 骨引之印(_核)
    共 += 1; ok += ([(x['章'], x['起'], x['止'], 类, 合) for x, 类, 合, _, _ in _核] == [
        (12, 3, 3, '原句', True), (12, 1, 1, '原句', False), (12, 2, 4, '原句', True), (12, 6, 6, '原句', True), (12, 6, 6, '原句', False),
        (900, 2, 2, '原句', True), (13, 1, 1, '短', True), (13, 2, 2, '远引', True), (13, 3, 3, '远引', False), (12, 1, 1, '远引', False),
        (12, 4, 4, '原句', True), (14, 1, 1, '原句', False), (12, 99, 99, '原句', False)]
        and _印.startswith('①骨记引句（章:行「原句」·含区间、全角冒号、本章（：行））5/9 合｜不合 4：12:1「己庚辛壬癸」实在 :4；')
        and '12:6「天地玄黄宇宙洪荒日月盈昃辰宿列张寒来暑往」所引之章无此句' in _印 and '14:1「此章不在其书」所引之章不在' in _印
        and '12:99「甲乙丙丁戊」行逾其白文（6 行）' in _印 and '｜不足四字不核 1' in _印
        and '①之二·骨记远引（章:行 而无「原句」）3 处：骨记之文四字以上逐字在所引之行·±1 者 1/3（13:2「尾巴没有往上走」）；余 2 处' in _印
        and '\n        13:3「上头一张是复印的悬赏。」 ← 骨「j 背冲街坐‖ 悬赏在身」' in _印)
    # ★X43③：±1 之界之内亦钉（旧只测外界 :1→:4 差三）——差一（上下）合、差二⛔；区间之止＋1、起－1 合，止＋2 ⛔；远引同窗
    _界 = 骨引之核('【本章亮点】a 12:3「己庚辛壬癸」。b 12:5「己庚辛壬癸」。c 12:2「己庚辛壬癸」。d 12:6「己庚辛壬癸」。'
                  'e 12:2至3「己庚辛壬癸」。f 12:5至6「甲乙丙丁戊」。g 12:2至3「天地玄黄宇宙」。h （12：5 己庚辛壬癸之翻）。i （12：6 己庚辛壬癸之翻）。',
                  900, 白们=_白们)
    共 += 1; ok += ([(x['起'], x['止'], 类, 合) for x, 类, 合, _, _ in _界] == [
        (3, 3, '原句', True), (5, 5, '原句', True), (2, 2, '原句', False), (6, 6, '原句', False),
        (2, 3, '原句', True), (5, 6, '原句', False), (2, 3, '原句', False), (5, 5, '远引', True), (6, 6, '远引', False)])
    # 回灌：旧式（一式之正则＋人物链.核句 只核句首 24 字）——认Ｄ6 为章、漏区间／逾四十字／本章／续引，且放过 e 之错尾
    import 人物链
    _旧 = [(a, b) for a, b, _ in re.findall(r'(\d{1,3})[:：](\d{1,4})(?:[—–-]\d+)?\s*「([^」]{4,40})」', _骨)]
    共 += 1; ok += (_旧 == [('12', '3'), ('12', '1'), ('12', '6'), ('6', '2'), ('14', '1'), ('12', '99')]
                   and 人物链.核句(12, _错, '6', 文='\n'.join(_白们[12])) == (True, 6))
    # 真局（瑕疵总账 X37 所举：398 记席亲 awk 之远引 272:509、388:49）——器今自核、自印其行
    _证398 = 机械之证(398)[0]
    共 += 1; ok += ('272:509「尾巴没有往上走」' in _证398 and re.search(r'\n        388:49「[^」]*悬赏[^」]*」 ← 骨「', _证398) is not None
                   and '不合 0' in _证398 and '不合 0' in 机械之证(400)[0])
    # ★X91①③：432 骨记之汉数连引⛔误析（旧印 390:422、422:424）；远引之行⛔截百字（422:45 之末句全印）
    _证432 = 机械之证(432)[0]
    共 += 1; ok += ('390:422' not in _证432 and '422:424' not in _证432 and '响得比那一回空' in _证432)
    # ★X100①：续列之章号⛔析作前引之行（449 骨记「四百零三：三十五、四百四十一、四百四十五」旧析 403:441、403:445）
    共 += 1; ok += ([(d['章'], d['起']) for d in 骨引('收四百零三：三十五、四百四十一、四百四十五之日子', 449)] == [(403, 35)]
                   and [(d['章'], d['起']) for d in 骨引('四百一十三：五、七、十一', 449)] == [(413, 5), (413, 7), (413, 11)])
    # ★X92：全书记忆入左移之拦（--前 印、--後 拦）
    共 += 1; ok += (('全书记忆', '全书记忆.py', []) in 左移之拦 and any(x[0] == "全书记忆" for x in 後之闸(434)))
    # ★1119 总编辑复核「全书记忆」→改：--後 之全书记忆闸带 --拦章 N（他章之残片⛔拦本章之封；缺、格坏照拦）
    共 += 1; ok += (dict(後之闸(434))['全书记忆'][0].endswith('全书记忆.py') and dict(後之闸(434))['全书记忆'][1:] == ['--拦章', '434']
                   and dict(後之闸(434))['质量三闸'][1:] == [])
    # ★1016 X06：⑥极短段之比——造局於字串（⛔钉盘上会长之数）：≤15 字为极短，「＊」与题行不算段、空白不算字
    _文 = '# 第九百章 某\n\n短。\n\n＊\n\n' + '长' * 16 + '\n\n' + '一二三四五六七 八九十一二三四五\n\n【本章亮点】\n短\n'
    _线 = lambda k: '主' if k % 2 == 0 else '暗'
    共 += 1; ok += (极短段(_文) == (2, 3) and 极短段('') == (0, 0)
                   and 同线前三(391, _线) == [385, 387, 389] and 同线前三(391, _线, lambda k: k != 387) == [383, 385, 389]
                   and 同线前三(391, lambda k: None) == [] and 同线前三(3, _线) == [1]
                   and _证[5].startswith('⑥极短段（≤15 字）之比｜同线(主)前三章与本章：') and _证[5].count('→') == 3
                   and re.search(r'→390 \d+／\d+＝\d+\.\d%｜连四章上行：[是否]$', _证[5]) is not None)
    收, 弃 = 可提交(381, ['正文/a.md', '版本/第381章/x', '版本/第382章/_开镜卡.md', '设定/y.json', 'README.md', '工具/z.py', '版本/第379章/v.md'])
    共 += 1; ok += (弃 == ['工具/z.py', '版本/第379章/v.md'] and len(收) == 5)
    共 += 1; ok += (记之缺(380) == [] and '下一章开镜卡' not in 记之缺(380))
    # ★1024 验席：N≥411 之占位未填 --後 拦（施工表留 ‹器:sha1›）；N≤410 照旧不认
    import tempfile as _tf0, shutil as _sh0
    _目0 = _tf0.mkdtemp(prefix='封版占_')
    try:
        os.makedirs(os.path.join(_目0, os.path.dirname(施工表)))
        open(os.path.join(_目0, 施工表), 'w', encoding='utf-8').write('| 410 | 锁定 | ‹器:sha1› |\n| 411 | 锁定 | ‹器:sha1› |\n')
        共 += 1; ok += (any(x.startswith('占位未填·施工表') for x in 记之缺(411, _目0)) and not any(x.startswith('占位未填') for x in 记之缺(410, _目0)))
    finally:
        _sh0.rmtree(_目0, ignore_errors=True)
    # ★1020 X21（W53 验席之治法 a）：①⛔跳 N+1（空锁）、撤锁为提交後之末步；後() 真走此两表（⛔内联另一份——验席之七）；
    #   ②封版之全测⛔撞断流：接力之静自交棒（_十一轮.json）起算；③撤 N 之锁⛔清 N+1 之心跳（取本地与远端之新者——验席之十）。
    #   回灌：旧表（心跳 N+1 於全测前、⛔撤锁）、後() 内联旧表、接力只看下一章之新动、可收不比新旧——各即红。
    #   （接力、心跳二器之自测不在全测，借此格入快测）
    _体 = open(__file__, encoding='utf-8').read().split('\ndef 後(')[1].split('\ndef ')[0]
    # ★1027 A2（Variant S·坑㊹㊾之格）：後之闸 ＝ 囤灰闸、第十一轮、读者之快、医生、末章硬闸——旧「全测·快」（338 秒，九成係器之自测）去。
    #   其守之意不变：记席与本器於 --前 之後所写之档（同步诸档、检察官之 schema、圣经之锚、亮点之注），医生（圣经之约、open_brief N+1、
    #   施工表、README 阶段、阅读器之同）、末章硬闸、读者可见之快格（改单、圣经引号、坑账、暂停令、钩子挂载、约到期闸）仍於提交之前拦——
    #   ⛔候 GitHub 之全闸於提交之後方逮（彼时 章-N 已不可改，治须治枝再一闸）；器之自测归 GitHub autopush 之全闸一回（⛔同树二跑）。
    #   後之存：一章唯一推（存底 --标·章-N）；云端验、存底 --演、存底包、跑账去。
    #   回灌：旧表（含「全测·快」）、去医生或末章硬闸、读者之快缺一格或含非读者可见之格、後之存复旧——各即红。
    _闸 = 後之闸(400, '/无此根')
    _闸d = dict(_闸)
    import 全测 as _全, 全测并 as _并
    _快表, _全表 = dict(_全.诸项(True)), dict(_全.诸项(False))
    共 += 1; ok += ([x[0] for x in _闸] == ['囤灰闸', '质量三闸', '席令之禁', '圣经随裁', '全书记忆', '第十一轮', '读者之快', '读者之慢', '医生', '末章硬闸']
                   and _闸d['读者之快'][1:] == ['--快', '--只', '改单,圣经引号,坑账,暂停令,钩子挂载,约到期闸']
                   and _闸d['医生'][1:] == ['--doctor'] and _闸d['末章硬闸'][1:] == ['--末章', '400'] and set(後之并) <= set(x[0] for x in _闸)
                   and all(k in _快表 and k in _全.读者可见之闸 for k in 读者之快) and '跑轮负测' not in _快表 and '跑轮负测' in _全表
                   and set(活态之格) | {'钩子挂载'} == set(_并.活态) and all(k in _全表 for k in 活态之格)
                   and not any('心跳.py' in x for _, a in _闸 for x in a)
                   and [x[0] for x in 後之存(400)] == ['存底 --存', '存底 --标', '撤锁']
                   and 後之存(400)[-1] == ('撤锁', [器('心跳.py'), '--收', '400'])
                   and '闸, 并 = 後之闸(n, root), {}' in _体 and 'in 後之存(n):' in _体 and '活态之报(n, root)' in _体
                   and _体.index('活态之报(n, root)') < _体.index("'commit', '-q'")
                   # ★1027 A2 验：章-N 一推败 → 当场 ⛔、返非零、⛔印「封版毕」（回灌：旧之只印 ⚠ 而续印封毕之语即红）
                   and "if 名 == '存底 --标' and rc != 0:" in _体 and 'print(标推未成之语(n, 标败)); return False' in _体
                   and _体.index('标推未成之语(n, 标败)') < _体.index('print(封毕之语(n))')
                   and '存底.py --标 411' in 标推未成之语(411, 'x') and '--候主 411' in 标推未成之语(411) and '封版毕' not in 标推未成之语(411))
    # 〔1119 执行之审·治7〕读者之慢：後之闸之一格（全测 --只 三慢格·⛔--快：快表无之即俱「未认」恒红）、後之并之首（第十一轮之後·与医生、末章硬闸三并），
    #   三格俱在 全测.诸项(非快) 与 全测.读者可见之闸（与 GitHub 同一组 chk_*·⛔另写判）、⛔外声闸（恒 exit 0）、⛔与读者之快重；
    #   真迹回放（各底之树原样·⛔叠今之器）：472 封版之树 f743735c6 → rc 1、FS沉默闸 ✗（GitHub 封後方红之 FS16 限471）、全书检与书级体检 ✓；
    #   其治 79ef08a55（GitHub 绿而入主枝）→ rc 0、三格俱 ✓（⛔误拦）。
    #   回灌：去此格、去其一名、加 --快、出後之并（串跑）、并起不三并、472 之树转绿、治之树转红 → 各即红。
    import threading as _th7
    _栅7, _原跑7 = _th7.Barrier(3, timeout=5), globals()['跑']

    def _假跑7(a, root=ROOT, 限=900):
        try:
            _栅7.wait()
        except _th7.BrokenBarrierError:
            return 1, '相继', 0
        return 0, '', 0.1
    try:
        globals()['跑'] = _假跑7
        _f7 = 并起([x for x in _闸 if x[0] in 後之并], ROOT, 隔=0.05)
        _rr7 = [_f7[k].result() if k in _f7 else None for k in ('读者之慢', '医生', '末章硬闸')]
    finally:
        globals()['跑'] = _原跑7
    _名7 = [x[0] for x in _闸]
    (_红底, _红rc), (_绿底, _绿rc) = 慢格之真迹
    # 〔1119 执行之审·复核〕真迹回放移出 --自测（见 慢格之回放 之注）：手跑 `封版.py --回放慢格`（1119 证：f743735c6 → rc 1·FS沉默闸 ✗；79ef08a55 → rc 0）；
    #   此处只验其接线：命取 後之闸 之「读者之慢」（⛔另拟）、--回放慢格 之支调之而以 慢格之真迹 判
    src = open(os.path.abspath(__file__), encoding='utf-8').read()
    _回体 = src.split('def 慢格之回放(')[1].split('\ndef ')[0] if 'def 慢格之回放(' in src else ''
    _主7 = src.split("\nif __name__ == '__main__':")[1] if "\nif __name__ == '__main__':" in src else ''
    _过7 = (_闸d.get('读者之慢') == [器('全测.py'), '--只', ','.join(读者之慢)] and set(後之并) == {'读者之慢', '医生', '末章硬闸'}
           and [k for k in _名7 if k in 後之并] == ['读者之慢', '医生', '末章硬闸'] and _名7.index('第十一轮') < _名7.index('读者之慢')
           and all(k in _全表 and k not in _快表 and k in _全.读者可见之闸 and k not in 读者之快 for k in 读者之慢) and '外声闸' not in 读者之慢
           and _rr7 == [(0, '', 0.1)] * 3 and (_红rc, _绿rc) == (1, 0) and len(_红底) == len(_绿底) == 40
           and "dict(後之闸(472, '/无此根')).get('读者之慢')" in _回体 and "a == ['--回放慢格']" in _主7 and '慢格之回放()' in _主7
           and ('= 慢格' + '之回放(') not in src.split('\ndef 自测(')[1].split("\nif __name__ == '__main__':")[0])   # --自测 ⛔调回放（⛔立树）
    if not _过7:
        print('  ✗ 读者之慢（治7）：并 %s' % (_rr7,))
    共 += 1; ok += _过7
    # 〔W908 环9〕读者之慢一式取之（⛔手列、⛔另立表）：封前之格（读者之快、读者之慢、左移之拦）∪ 全测.活态之格 ∪ 慢之豁免 ⊇ 读者可见之非负测格；
    #   豁免俱在读者可见之闸、俱书由、俱⛔在封前之格；读者之慢 ⊇ 治7 之三格、俱在 全测.诸项(非快)（⛔「未认」）、序随诸项；
    #   变异（伪全测）：读者可见之闸添一非负测之格 → 自入；添负测·*、活态之格、已左移者 → ⛔入；载时全测读不得（读者之慢空）→ 後之闸再算、全测坏即抛（⛔无闸而过）。
    #   回灌：手列旧三格、豁免无由或陈（不在读者可见之闸）、去一读者可见之非负测格而⛔书免 → 各即红。
    import types as _ty9
    _前格9 = set(读者之快) | set(读者之慢) | {x[0] for x in 左移之拦}
    _非负9 = {k for k in _全.读者可见之闸 if not k.startswith('负测·')}
    _伪9 = _ty9.SimpleNamespace(诸项=lambda q: list(_全.诸项(q)) + [('伪慢格', None), ('负测·伪', None), ('伪活', None), ('伪左', None)],
                               读者可见之闸=set(_全.读者可见之闸) | {'伪慢格', '负测·伪', '伪活', '伪左'}, 活态之格=tuple(_全.活态之格) + ('伪活',))
    _原快9 = 读者之快
    try:
        globals()['读者之快'] = 读者之快 + ('伪左',)
        _算伪9 = 读者之慢之算(_伪9)
    finally:
        globals()['读者之快'] = _原快9
    _原慢9 = 读者之慢
    try:
        globals()['读者之慢'] = ()          # 载时全测读不得之局：後之闸 再算（⛔「--只」空而过）
        _补9 = dict(後之闸(400, '/无此根')).get('读者之慢')
    finally:
        globals()['读者之慢'] = _原慢9
    try:
        读者之慢之算(_ty9.SimpleNamespace())
        _抛9 = False
    except Exception:
        _抛9 = True
    _过9 = (_非负9 <= _前格9 | set(_全.活态之格) | set(慢之豁免) and set(慢之豁免) <= _全.读者可见之闸
           and all(isinstance(v, str) and len(v) >= 12 for v in 慢之豁免.values()) and not (set(慢之豁免) & _前格9)
           and {'全书检', '书级体检', 'FS沉默闸'} <= set(读者之慢) and all(k in _全表 for k in 读者之慢)
           and 读者之慢 == 读者之慢之算() and [k for k, _ in _全.诸项(False) if k in 读者之慢] == list(读者之慢)
           and _算伪9 == 读者之慢 + ('伪慢格',) and _抛9 and _补9 == [器('全测.py'), '--只', ','.join(读者之慢)]
           and "\n读者之慢 = ('" not in src and '    读者之慢 = 读者之慢之算()' in src
           and "','.join(读者之慢 or 读者之慢之算())" in src.split('\ndef 後之闸(')[1].split('\ndef ')[0])
    if not _过9:
        print('  ✗ 读者之慢之算（W908 环9）：前格 ∪ 免 缺 %s；算 %s' % (sorted(_非负9 - _前格9 - set(_全.活态之格) - set(慢之豁免)), 读者之慢))
    共 += 1; ok += _过9
    # ★1117（GitHub 化之审·I·法用#停钩空转）：章-N 推成（标败为 None）方泊、泊在封毕之语前；泊不成（无远端之临时库）只印 ⚠、⛔抛；
    #   真推之泊（临时裸库）：泊於「章-N」、平台 Stop 钩之量 0（推报.钩之未推）——回灌：泊在标败之判前、泊章之语抛、⛔泊即红
    _无 = tempfile.mkdtemp(prefix='封版泊_')
    subprocess.run(['git', 'init', '-q', _无], capture_output=True)
    _泊印 = 泊章之语(411, _无)
    shutil.rmtree(_无, ignore_errors=True)
    _泊真 = False
    _库 = tempfile.mkdtemp(prefix='封版泊_')
    try:
        import 推报 as _报
        _裸, _沙, _ = _报.演泊之库(_库, '章-411')        # 临时之裸库（推报 之演·写者册 演）：主枝一笔、「章-411」已推而未并
        _前钩 = _报.钩之未推(_沙)
        _真印 = 泊章之语(411, _沙)
        _泊真 = (_前钩 == 1 and _真印.lstrip().startswith('✓ 泊') and _报.钩之未推(_沙) == 0
                 and subprocess.run(['git', 'symbolic-ref', '--short', 'HEAD'], cwd=_沙, capture_output=True, text=True).stdout.strip() == '章-411')
    except Exception as _x:
        print('  ✗ 泊之真推 崩：%s' % _x)
    finally:
        shutil.rmtree(_库, ignore_errors=True)
    共 += 1; ok += ('print(泊章之语(n, root))' in _体 and _体.index('print(标推未成之语(n, 标败)); return False') < _体.index('print(泊章之语(n, root))')
                   < _体.index('print(封毕之语(n))') and _泊印.lstrip().startswith('⚠ 泊') and _泊真)
    # ★1027 A2：--演 只於 --试 所立之副本里跑（无演之记即止，⛔在真仓同步而不提交）；诸闸之判自其印取；医生与末章硬闸并起
    import io as _io0, contextlib as _cl0
    _目1 = tempfile.mkdtemp(prefix='封版演记_')
    try:
        with _cl0.redirect_stdout(_io0.StringIO()) as _o1:
            _r1 = 後(400, 演=True, root=_目1)
    finally:
        shutil.rmtree(_目1, ignore_errors=True)
    # 并否以栅（二者俱至方过；相继即首者候五秒而栅破）判、⛔以墙钟（GitHub 之机忙时秒数抖，读者可见之格⛔可抖·1027 丝滑）
    import threading as _th1
    _记1, _原跑1, _栅1 = [], globals()['跑'], _th1.Barrier(2, timeout=5)

    def _假跑1(a, root=ROOT, 限=900):
        _记1.append((time.time(), a[-1]))
        try:
            _栅1.wait()
        except _th1.BrokenBarrierError:
            return 1, '相继', 0
        return 0, '', 0.3
    try:
        globals()['跑'] = _假跑1
        _f1 = 并起([('医生', ['x', '--doctor']), ('末章硬闸', ['x', '410'])], ROOT, 隔=0.05)
        _rr1 = [_f1[k].result() for k in ('医生', '末章硬闸')]
    finally:
        globals()['跑'] = _原跑1
    共 += 1; ok += (_r1 is False and '⛔ --演 只於 --试' in _o1.getvalue() and '阶段之数' not in _o1.getvalue()
                   and _rr1 == [(0, '', 0.3)] * 2 and len(_记1) == 2
                   and 诸闸之判('  ✓ 囤灰闸     rc=0     1s  ✓\n  ⛔ 医生       rc=1    37s  ERROR=1\n  ⚠ 活态之报   rc=1     4s  x\nx  ✓ 甲 rc=0\n  ✓ 净重对表 --补   rc=0     0s  共改 0 行。')
                   == {'囤灰闸': '✓', '医生': '⛔', '活态之报': '⚠', '净重对表 --补': '✓'}
                   and _封之笔之局())
    # 〔W908 环9·治8〕--试 之副本无活迹：法用之守 之红尽属 副本之缺（器迹未跑、备份/报 无枝、origin 无枝、报/演 俱无）→ 唯 --演 只注（⚠·续走其後诸闸）；
    #   余因（档含、废而未除、语截断）照拦；真封（演=False）同印即⛔停（一字不变）。样取 473 之副本之实印（1120：✓20 ⛔27 俱此四类）。
    #   回灌：去「演」之限（真封亦免）、免而不续、余因亦免、头行入判、演练⛔注其免 → 各即红。
    _样9 = ('⛔ 推闸交GitHub（§八.2）：报/推/章-472.json 无凭：备份/报 无此枝\n'
           '⛔ 主枝并进（§三.3）：origin 无 章-472；接棒守.py --候主 472 自本章之开（11-19T15:02）未跑\n'
           '⛔ 段案之带为准（设定/瑕疵总账.md X）：造式验.py 473 --料 自本章之开（11-19T15:02）未跑\n'
           '⛔ 演练之流（§八.21）：origin 无 备份/报 之枝；未演（流程之法须真料演练方上）：演练账与 报/演 俱无其录\n'
           '⛔ 云巡（§三.5）：origin 无 备份/巡应 之枝；origin 无 备份/巡印 之枝\n'
           '⚠ 待·探缓存分档（限 411）：到限而证只验串在（纸证·E4）——补行为之证\n'
           '⛔ 法用之守 --验 473：应验 47 法（✓20 ⛔27 ⚠0）｜完备 ✓')
    _余样9 = ('⛔ 封版瘦闸（§八.19）：工具/封版.py 无 \'读者之慢\'；origin 无 章-472\n'
             '⛔ 废而未除：甲（废於 1119）1 处：工具/x.py\n'
             '⛔ 自走默印（§八.8）：自走.py 自本章之开（11-19T15:02）未')       # 末行：语截断（法用之守 之 语[:200]）
    _免9, _余9 = 副本之免(_样9)
    _免9b, _余9b = 副本之免(_样9 + '\n' + _余样9)
    _原9, _法印9, _果9 = {k: globals()[k] for k in ('跑', '记之缺', '阶段之数', '活态之报')}, [_样9], []

    def _假跑9(a, root=ROOT, 限=900):
        return (1, _法印9[0], 0.1) if a[0].endswith('法用之守.py') else (0, '✓', 0.1)
    _目9 = tempfile.mkdtemp(prefix='封版副免_')
    try:
        open(os.path.join(_目9, 演之记), 'w').write('x\n')
        globals().update(跑=_假跑9, 记之缺=lambda n, root=ROOT: [], 阶段之数=lambda n, root=ROOT: [], 活态之报=lambda n, root=ROOT: [])
        for _演9, _印9 in ((True, _样9), (True, _样9 + '\n' + _余样9), (False, _样9)):
            _法印9[0], _o9 = _印9, _io0.StringIO()
            try:
                with _cl0.redirect_stdout(_o9):
                    _r9 = 後(411, 演=_演9, root=_目9)
            except Exception as _x9:      # 真封而误免即走至席记之写（临时之根无之）——崩即红
                _r9 = '崩：%s' % str(_x9)[:60]
            _v9 = _o9.getvalue()
            _果9.append((_r9, 诸闸之判(_v9).get('法用之守'), '演毕' in _v9, 副本无活迹之语 in _v9, '⛔ 停：法用之守 红' in _v9, '读者之慢' in 诸闸之判(_v9)))
    finally:
        globals().update(_原9)
        shutil.rmtree(_目9, ignore_errors=True)
    _演体9 = src.split('\ndef 演练(')[1].split('\ndef ')[0]
    _过9b = (len(_免9) == 5 and _余9 == [] and len(_免9b) == 5 and len(_余9b) == 3
            and _果9 == [(True, '⚠', True, True, False, True), (False, '⛔', False, False, True, False), (False, '⛔', False, False, True, False)]
            and "if 闸.get('法用之守') == '⚠':" in _演体9 and '副本无活迹之语 in l' in _演体9 and '副本无活迹之语 not in l' in _演体9)
    if not _过9b:
        print('  ✗ --试 之副本免活迹（W908 环9·治8）：免 %d 余 %s；後 %s' % (len(_免9), _余9b, _果9))
    共 += 1; ok += _过9b
    # ★1027 A2（合流：同功一处）：活态之报之器红只并所跑之三格（红入、首见留；绿销）——他格之笔⛔动（回灌：⛔跑过即误销「他格」）；
    #   判借 全测.器红之判（GitHub 之并判同用），⛔另写一份并账
    _账2, _逾2 = _全.器红之判(['跑账', '负测·自进化环'], 410,
                             {'他格': {'首见': 400, '限': 403}, '跑账': {'首见': 405, '限': 408}, '接力': {'首见': 409, '限': 412}}, 活态之格)
    _误2, _ = _全.器红之判(['跑账'], 410, {'他格': {'首见': 400, '限': 403}})
    共 += 1; ok += (_逾2 == ['跑账'] and set(_账2) == {'他格', '跑账', '负测·自进化环'} and _账2['跑账']['首见'] == 405
                   and _账2['负测·自进化环'] == {'首见': 410, '末见': 410, '限': 413} and '他格' not in _误2
                   and '全测._器红入账(红, n, 活态之格)' in open(__file__, encoding='utf-8').read().split('\ndef 活态之报(')[1].split('\ndef ')[0])
    try:
        import 接力 as _接, 心跳 as _跳
        _t = 1e9
        _封 = dict(印=False, now=_t, 末=400, 回执=True, 动=_t - 68 * 60, 跳=(False, None, None), 停=(False, ''))
        共 += 1; ok += (_接.查(交=_t - 120, **_封)[0] == [] and _接.查(交=_t - 68 * 60, **_封)[0] != []
                       and _跳.可收(400, [{'章': 401, '时': 2}, {'章': None, '时': 1}])[0] is False
                       and _跳.可收(400, [{'章': 401, '时': 1}, {'章': None, '毕': 400, '时': 2}])[0] is True)
    except Exception:
        共 += 1
    # ★1027 坑51：封毕之下一步係 接棒守 --候主 N（後台·零 token），⛔推.py（沙盒直推抢先、GitHub 之推恒败）；後() 只经 封毕之语 印之
    _毕 = 封毕之语(411)
    共 += 1; ok += ('python3 工具/接棒守.py --候主 411' in _毕 and '推.py（' not in _毕 and 'print(封毕之语(n))' in _体
                   and 'python3 工具/推.py（後台）' not in open(__file__, encoding='utf-8').read().split('def 自测')[0])
    共 += 1; ok += 红行('x\n  ✗ 负测·甲  坏\n⛔⛔ 永远的痛·D6\n  ✓ 乙\n⛔ 停') == ['✗ 负测·甲  坏', '⛔ 停']   # ★1020：红则印诸红项、⛔D6 之训
    _印 = '  ✗第9章《甲》:\n      第十一轮未过:未见 x\n  末章硬闸·第9章：失败'
    共 += 1; ok += 末章之病(_印) == [] and 末章之病(_印.replace('      第十一轮', '      5+逗:甲\n      第十一轮')) == ['5+逗:甲']   # ★1020：--前 免第十一轮（其归 --後）、余病照报
    # ★W60 X39：--前 之二慢检并起——①二检之命令与旧一字不差（检察官 --末章 N 以 subprocess.run、开轮六检 N --静 以 跑）；
    #   ②并起：二检俱至一栅方过（相继即首者候五秒而栅破、返非零）——⛔以墙钟判（GitHub 之机忙时抖·1027 丝滑）；③前() 只经 慢检并起 起此二检（⛔另跑一回、⛔删一检）
    import subprocess as _sp, threading as _th
    _记, _栅 = [], _th.Barrier(2, timeout=5)
    _原run, _原跑 = _sp.run, globals()['跑']

    def _过栅():
        try:
            _栅.wait(); return 0
        except _th.BrokenBarrierError:
            return 1

    def _假run(a, **k):
        _记.append(('run', a[1:], k.get('cwd'))); return _sp.CompletedProcess(a, _过栅(), '', '')

    def _假跑(a, root=ROOT, 限=900):
        _记.append(('跑', a, root)); return _过栅(), '', 0.4
    try:
        _sp.run = _假run; globals()['跑'] = _假跑
        _慢 = 慢检并起(400, ROOT, 隔=0.05)
        _r1, _r2 = _慢['检察官'].result(), _慢['开轮六检'].result()
    finally:
        _sp.run = _原run; globals()['跑'] = _原跑
    _前体 = open(__file__, encoding='utf-8').read().split('\ndef 前(')[1].split('\ndef ')[0]
    共 += 1; ok += (sorted(_记) == sorted([('run', [器('小说检察官.py'), '--末章', '400'], ROOT), ('跑', [器('开轮六检.py'), '400', '--静'], ROOT)])
                   and _r1.returncode == 0 and _r2[0] == 0
                   and "慢['开轮六检'].result()" in _前体 and "慢['检察官'].result()" in _前体 and _前体.count('慢检并起(') == 1
                   and '开轮六检.py' not in _前体 and '小说检察官.py' not in _前体)
    _前 = open(os.path.abspath(__file__), encoding='utf-8').read().split('def 自测')[0]
    共 += 1; ok += ("('质量三闸', ['质量三闸.py'])" in _前)        # ★1022 坑㊹：--前 跑与推闸同一之质量三闸（一章一日等）
    共 += 1; ok += ("('席令之禁', ['席令之禁.py'])" in _前)        # ★1023 坑㉟复踩：--前 跑席令之禁（新席缺律⑮⑳）
    # 〔W909〕体系总图之步：居 进化树随、器之迹 之後（末真用之窗含本章之迹），不拦（必＝False）；其产入器生之档（演练只注其摘）
    _步位 = {a: i for i, (a, _) in enumerate(re.findall(r"\('([^']+)', \[器\('([^']+)'\)", _前.split('\ndef 後(')[1].split('\ndef ')[0]))}
    共 += 1; ok += ("('体系总图', [器('体系总图.py')], False)" in _前 and _步位.get('体系总图', -1) > _步位.get('器之迹', 99) > _步位.get('进化树随', 99)
                   and '设定/体系总图.md' in 器生之档 and '设定/执行清单.md' in 器生之档)   # 〔W921 环7〕清单同生於体系总图之写步
    # ★1027 A2：约到期之实跑入 --前（N≥411·记席之栏，其项名可为 --红 所认）；--後 之读者之快以 约到期闸 照拦
    共 += 1; ok += ("器('约到期.py'), '--闸']" in _前体 and _前体.index('# ★1027 A2：约到期') > _前体.index("_名, _过, _语 = 质量三闸.gate1e(n)[0]")
                   and 前之项('· 约到期：⛔ ⛔欠约 约-001：第291章拍139立「甲」——记席治\n')['约到期'][:2] == ['席', '⛔'] and '约到期闸' in 读者之快)
    共 += 1; ok += ("('全书记忆随', [器('全书记忆.py'), '--随']" in _前 and _前.index('全书记忆随') < _前.index("('剧情链', [器('剧情链.py')]"))   # ★1024 坑㊾：--後 先随详记之 sha、後生剧情链
    # ★1119 W907：剧情全图 於剧情链之後重生（其⑤取总览③、站取剧情链.站们）；其档入纯同步之档（演时复其前、令同步真重生）
    共 += 1; ok += (_前.index("('剧情链', [器('剧情链.py')]") < _前.index("('剧情全图', [器('剧情全图.py')]") < _前.index("('人物链', [器('人物链.py')")
                   and '设定/全书记忆/剧情全图.md' in 纯同步之档)
    # ★1027 执行之核（#44）：--前 所印之 质量三闸、席令之禁、圣经随裁、器物点名 N 於 --後 照拦（器物点名唯有 _器物.md 之章）；
    #   （#60）阶段之数并改 总站、人物册之「已写 1—N 章」（回灌：旧之 README 一档之表 → 站之现状停在 379 即红）
    _器物有 = os.path.exists(os.path.join(ROOT, '版本', '第410章', '_器物.md'))
    _410 = dict(後之闸(410))
    共 += 1; ok += ((not _器物有 or _410.get('器物点名', [None, None])[1:] == ['410'])
                   and '器物点名' not in dict(後之闸(410, '/无此根'))
                   and all(_410[k][0].endswith(k + '.py') for k in ('质量三闸', '席令之禁', '圣经随裁')))
    import tempfile as _tf6, shutil as _sh6
    _站 = _tf6.mkdtemp(prefix='封版站_')
    try:
        _行 = '<span>已写 <b>1—379 章</b>（初稿号）；380 起待写。本页下文……</span>'
        open(os.path.join(_站, 'README.md'), 'w', encoding='utf-8').write('第 1—409 章已经同步封版；第 410 章开写前\n')
        open(os.path.join(_站, '镇冢秘术_总站.html'), 'w', encoding='utf-8').write(_行)
        open(os.path.join(_站, '人物册_总纲_九站.html'), 'w', encoding='utf-8').write(_行)
        _改1 = 阶段之数(410, _站)
        _改2 = 阶段之数(410, _站)
        _站文 = open(os.path.join(_站, '镇冢秘术_总站.html'), encoding='utf-8').read()
    finally:
        _sh6.rmtree(_站, ignore_errors=True)
    共 += 1; ok += (sorted(_改1) == ['README.md', '人物册_总纲_九站.html', '镇冢秘术_总站.html'] and _改2 == []
                   and '已写 <b>1—410 章</b>（初稿号）；411 起待写' in _站文 and '镇冢秘术_总站.html' in 纯同步之档)
    # ★1024 省 token 之审 records 二：--前 --红 与「主环之职」之栏
    #   ①分栏只走 N≥411、只移三闸（质量三闸＝六问之所出，留记席栏）；N≤410 之印照旧（print(_行) 一路）；--後 之囤灰闸照拦
    共 += 1; ok += (分栏之始 == 411 and 主环之闸 == ('囤灰闸', '跑账', '席令之禁') and 'if n >= 分栏之始 and _名 in 主环之闸' in _前体
                   and "闸 = [('囤灰闸', [器('囤灰闸.py')])]" in _前)
    # ★1027 法用之守：--前 於 N≥411 带 --前 跑之、入主环之职栏；--後 之闸 N≥411 含之（红即停、⛔提交）而 N≤410 无之；其验之末行入席记「法用」
    共 += 1; ok += ([x[0] for x in 後之闸(411, '/无此根')] == ['囤灰闸', '法用之守', '质量三闸', '席令之禁', '圣经随裁', '全书记忆', '第十一轮', '读者之快', '读者之慢', '医生', '末章硬闸']
                   and 後之闸(411, '/无此根')[1][1][1:] == ['--验', '411']
                   and [x[0] for x in 後之闸(410, '/无此根')] == ['囤灰闸', '质量三闸', '席令之禁', '圣经随裁', '全书记忆', '第十一轮', '读者之快', '读者之慢', '医生', '末章硬闸']
                   and "if n >= 分栏之始:          # ★1027 法用之守" in _前体 and "'法用之守.py'), '--验', str(n), '--前']" in _前体
                   and "主环.append('    · 法用之守：" in _前体 and "_j['法用'] = 末[0]" in _体
                   and 前之项('· 主环之职（记席⛔治；封版 --後 照拦）：\n    · 法用之守：⛔ 甲——主环治\n')['法用之守'][:2] == ['主环', '⛔'])
    _上 = ('· 造式之实：✓ 二代\n· 锁定行之数（取此，⛔凭空写）：\n    净重：3004\n    sha1：aaaaaaaaaaaa\n'
          '· 坑账之机械之证（器先算·记席照此答、⛔再逐条 grep）：\n    ①甲\n· 开轮十六检：⛔ ⑮未答——记席须治\n'
          '· 回执闸：⛔ 回执缺键：到期账——记席照式补\n· 六问：✓ 已答\n· 器物册（器物点名 411）：✓ 拍号俱对\n'
          '· 主环之职（记席⛔治；封版 --後 照拦）：\n    · 囤灰闸：✓\n    · 跑账：⛔ 甲器从没跑过——主环治\n    · 席令之禁：✓\n')
    _今 = (_上.replace('⛔ ⑮未答——记席须治', '✓ 俱过').replace('回执缺键：到期账', '回执缺键：病历').replace('aaaaaaaaaaaa', 'bbbbbbbbbbbb')
           .replace('    ①甲\n', '    ①乙\n') + '· 末章硬闸（检察官）：⛔ 5+逗:甲——治後再跑 --前\n')
    _项上, _项今 = 前之项(_上), 前之项(_今)
    _印 = 红印(411, _项今, _项上, '10-24 00:00:00')
    _L = _印.split('\n')
    共 += 1; ok += (_项上['跑账'][:2] == ['主环', '⛔'] and _项上['开轮十六检'][:2] == ['席', '⛔'] and _项上['锁定行之数'][1] == '·'
                   and '· 回执闸：⛔ 回执缺键：病历——记席照式补（变）' in _L and '· 末章硬闸（检察官）：⛔ 5+逗:甲——治後再跑 --前（新红）' in _L
                   and '· 上回红今已绿：开轮十六检' in _L and '· 变·锁定行之数：sha1 aaaaaaaaaaaa→bbbbbbbbbbbb' in _L
                   and any(l.startswith('· 变·坑账之机械之证') for l in _L) and '    · 跑账：⛔ 甲器从没跑过——主环治' in _L
                   and _L[-1] == '✓ 余 6 项俱绿' and not any('造式之实' in l or '六问' in l or '器物册' in l for l in _L))
    # ②前印：上回之印存 .cache（⛔版本/）；首跑全印、其後 --红 只印红；同印再跑 → 只余末行与题
    import tempfile as _tf, io as _io
    _目 = _tf.mkdtemp(prefix='封版红_')
    _原前 = globals()['前']
    try:
        globals()['前'] = lambda n, root=ROOT: (print(_上, end=''), True)[1]
        _o1 = _io.StringIO(); _s.stdout, _原 = _o1, _s.stdout
        try:
            _r1 = 前印(411, True, _目); _r2 = 前印(411, True, _目)
        finally:
            _s.stdout = _原
        _存 = 上回之档(411, _目)
        共 += 1; ok += (_r1 and _r2 and _o1.getvalue().startswith(_上) and _o1.getvalue().count('════ 封版·前·红') == 1
                       and _o1.getvalue().rstrip().endswith('✓ 余 5 项俱绿') and os.path.exists(_存)
                       and '/.cache/封版前/' in _存.replace(os.sep, '/') and '版本' not in os.path.relpath(_存, _目))
    finally:
        globals()['前'] = _原前
        import shutil as _sh; _sh.rmtree(_目, ignore_errors=True)
    import inspect as _ins
    # ★X83（1105）：回执闸之键一表——与小说检察官._receipt_ok 所索者同（多一少一俱红）
    import 小说检察官 as _检k
    _源k = _ins.getsource(_检k._receipt_ok)
    共 += 1; ok += (set(re.findall(r"'([^'\s]{2,4})' in tx", _源k)) == set(回执闸之键))
    # 〔1119 死规之审·gates14〕验新裁：无「五钩」之回执过闸；守牙仍红——缺「伏笔」或「到期账」之回执照拦
    import tempfile as _tfk, shutil as _shk
    _rt = _tfk.mkdtemp(); _rp = os.path.join(_rt, '回执.md'); _原rf = _检k._receipt_files
    _检k._receipt_files = lambda n: [_rp]
    try:
        open(_rp, 'w', encoding='utf-8').write('第473章 ' + '、'.join(回执闸之键)); _过 = _检k._receipt_ok(473)
        open(_rp, 'w', encoding='utf-8').write('第473章 五钩 ' + '、'.join(k for k in 回执闸之键 if k != '伏笔')); _拦1 = not _检k._receipt_ok(473)
        open(_rp, 'w', encoding='utf-8').write('第473章 五钩 ' + '、'.join(k for k in 回执闸之键 if k != '到期账')); _拦2 = not _检k._receipt_ok(473)
    finally:
        _检k._receipt_files = _原rf; _shk.rmtree(_rt, ignore_errors=True)
    共 += 1; ok += ('五钩' not in 回执闸之键 and _过 and _拦1 and _拦2)
    # ★X84（1105）：骨引认汉字之章行（420 骨记之真形）
    _汉引 = 骨引('是四百一十二：五十三「那一截空」，取四百一十三：五、七', 420)
    共 += 1; ok += ([(x['章'], x['起'], x['句']) for x in _汉引] == [(412, 53, '那一截空'), (413, 5, None), (413, 7, None)])
    # ★X86（1105）：章之件标成——名起「第N章」之未成件即标（桩 标）；已成、无件、名不起其章者⛔动；⛔拦封（标拒仍回 None）
    import tempfile as _tf, 工作流账 as _账
    _t = _tf.mkdtemp(); os.makedirs(os.path.join(_t, '设定'))
    json.dump({'件': [{'id': 'W8', '名': '第8章（甲）', '状态': '已成'}, {'id': 'W9', '名': '第9章（乙）', '状态': '进行'},
                      {'id': 'W10', '名': '剧情庭·第9章之段', '状态': '进行'}]}, open(os.path.join(_t, _账.账档), 'w', encoding='utf-8'))
    _原标, _标们 = _账.标, []
    _账.标 = lambda i, 态, root=None: (_标们.append((i, 态)) or i != 'W9x')
    _o2 = _io.StringIO(); _s.stdout, _原 = _o2, _s.stdout
    try:
        _k = (章之件标成(9, _t), 章之件标成(8, _t), 章之件标成(7, _t))
    finally:
        _s.stdout = _原; _账.标 = _原标; _sh.rmtree(_t, ignore_errors=True)
    共 += 1; ok += (_k == ('W9', None, None) and _标们 == [('W9', '已成')])
    _段後 = open(__file__, encoding='utf-8').read().split('\ndef 後(')[1].split('\ndef ')[0]
    共 += 1; ok += ('章之件标成(n, root)' in _段後 and _段後.index('章之件标成(n, root)') < _段後.index("'git', 'commit'"))
    print('封版·自测 %d/%d%s' % (ok, 共, ' 全通' if ok == 共 else ' 未过'))
    return ok == 共


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--自测']:
        sys.exit(0 if 自测() else 1)
    if a == ['--回放慢格']:           # 〔1119 执行之审·治7·复核〕读者之慢之真迹回放（手跑·一回之证·⛔入 --自测）
        _果 = 慢格之回放()
        _合 = True
        for _底, _期 in 慢格之真迹:
            _rc, _格, _末 = _果.get(_底) or (None, {}, '')
            _是 = _rc == _期 and bool(_格) and ((_期 == 0) == all(v == '✓' for v in _格.values()))
            _合 = _合 and _是
            print('%s %s → rc %s（期 %d）：%s%s' % ('✓' if _是 else '⛔', _底[:9], _rc, _期, '、'.join('%s %s' % kv for kv in _格.items()) or '—',
                                                  '' if _是 else '｜' + str(_末)[-200:]))
        sys.exit(0 if _合 else 1)
    if len(a) >= 2 and a[0].isdigit() and a[1] in ('--前', '--後'):
        n = int(a[0])
        sys.exit(0 if (前印(n, '--红' in a) if a[1] == '--前' else 演练(n) if '--试' in a else 後(n, '--演' in a)) else 1)
    print(__doc__); sys.exit(2)
