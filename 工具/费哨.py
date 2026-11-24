#!/usr/bin/env python3
"""费哨（1021 立·作者问「七成的 token 竟然没有用来写书……为什么都耗费了这么多 token，你都没有做出一个及时的措施」）。

为何立：诸复盘只比「同类之上回」——每件都比上回同类省，而非写书之件越开越多，没有一处看全局之钱落在哪。
本哨零 token：读 设定/费账.json（费审.py --记／--记主 所写），按件分「写书」（一章、造剧情）与「非写书」，
看末 N 件（默认 10 件，以 W 号计）写书之占；⛔低於七成即红（裁_1021_省律 三之1「七三之律」）。
〔1119 执行之审·治3(a)〕尺正：末 N 件按费账之行序取（⛔按 W 号之数排——旧 W901—W904 恒占末十）；其间无 W 号之行
  （名空之 wf_、大审、「总编辑之坐·<日>」之主环行……）各以其「键」自为一件、以名判类，无名归非写书（旧跳过之：1117 起 $377.49 不计）。
  「主会话:」之行係一会话全程之总、与主环之切片重，仍⛔重加。量之源缺即印「缺」，⛔印 0%、⛔判合（根丙）。
跑口：工作流账.py 印（每回会话开头先跑）之首行；工作流账 --开 一件非写书之件而哨红者拒开，
      除非有效之据写明「挡路：」（挡下一章之料或闸）或「读者可见：」（读者读得到之病）及其由。
用法：
  python3 工具/费哨.py            # 印末十件之占；红则 rc=1
  python3 工具/费哨.py --件 20    # 看末二十件
  python3 工具/费哨.py --章       # 开章之检（自走.py 每回首印之）：末五章之费、资源配置比（造≥75%｜主环≤5%·取 法用之守.章量）
    〔1119 执行之审·治3(b)、治4(e)〕末五章按章号取（旧之式只认「造式／二代」、不认「W146·第472章」，停在 420—427、466）；
    主环行缺印「缺」；末三章之量源（工作流账之件＝--开 之果、费账之主环行）缺即印——只印、⛔拦。
  ★1027 执行之审 #64 #80（同功两处即废劣者）：配置比旧读 journal（容器一换即失，失即印 0%·每会话假⛔），与 法用之守 之量两算——
    今只调 法用之守.章量（费账＋复盘「按类」之造，随仓而存）；数无即印「算不得」，⛔印 0%。
  python3 工具/费哨.py --跑 <Run> <估$>   # 跑中之费对估：逾 1.5 倍即⛔立停
  python3 工具/费哨.py --自测
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import os, sys, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
界 = 0.70
写书类 = ('一章', '造剧情')
写书词 = re.compile(r'造式|二代|第\d+章|剧情庭|段案|余章总案|造剧情')
例外式 = re.compile(r'(挡路|读者可见)[：:]\s*(?:\S\s*){4,}')   # 由须四字以上（空白不计）


def 类表(root=ROOT):
    """W 号 → 复盘所书之类（「- 类：一章（…）」取括号前）。"""
    表 = {}
    for p in glob.glob(os.path.join(root, '设定', '复盘', '*.md')):
        m = re.search(r'_(W\d+)_', os.path.basename(p))
        if not m:
            continue
        try:
            t = open(p, encoding='utf-8').read()
        except Exception:
            continue
        k = re.search(r'^- 类：\s*([^（(\n]+)', t, re.M)
        if k:
            表[m.group(1)] = k.group(1).strip()
    return 表


def 判类(名, 表):
    """返（W 号或 None, 是否写书）。"""
    m = re.match(r'(W\d+)', 名 or '')
    w = m.group(1) if m else None
    if w and w in 表:
        return w, 表[w] in 写书类
    return w, bool(写书词.search(名 or ''))


def 算(行, 表, 件=10):
    """行：费账之行（追加之序）；计 wf_、子席:、主环: 三种（主会话: 係其总，⛔重加）。返 (写, 非, 诸件[(号或键, 件)…·按行序])。
    〔1119 执行之审·治3(a)〕有 W 号者以号合为一件；无 W 号者（名空之 wf_、大审、「总编辑之坐·<日>」之主环行）以其「键」自为一件、
    以名判类（无名归非写书·旧 :67 跳过之）。末段按费账行序（⛔按 W 号之数排·旧 :71 令 W901—W904 恒占末十）：
    取末「件」个 W 件；其前一个 W 件之末行为界，界後诸件（含无号者）俱计——末段仍约一段之跨，⛔因无号之件多而缩。"""
    按件 = {}
    for i, r in enumerate(行):
        键 = str(r.get('键', ''))
        if 键.startswith('主会话'):
            continue
        w, 写 = 判类(r.get('名', ''), 表)
        a = 按件.get(w or 键)
        if a is None:
            a = 按件[w or 键] = {'名': r.get('名', ''), '美元': 0.0, '写': 写, '号': bool(w), '末': i}
        a['美元'] += float(r.get('美元') or 0)
        a['末'] = i
    序 = sorted(按件, key=lambda k: 按件[k]['末'])
    号 = [k for k in 序 if 按件[k]['号']]
    界行 = 按件[号[-件 - 1]]['末'] if 件 >= 0 and len(号) > 件 else -1
    末 = [k for k in 序 if 按件[k]['末'] > 界行]
    写 = sum(按件[k]['美元'] for k in 末 if 按件[k]['写'])
    非 = sum(按件[k]['美元'] for k in 末 if not 按件[k]['写'])
    return 写, 非, [(k, 按件[k]) for k in 末]


def 判(root=ROOT, 件=10):
    """返 (红否, 一行之述, 诸件)。"""
    try:
        行 = json.load(open(os.path.join(root, '设定', '费账.json'), encoding='utf-8'))['行']
    except Exception as e:
        return False, '费哨：缺——费账读不得（%s）；⛔印 0%%，只报不拦' % e, []
    写, 非, 诸 = 算(行, 类表(root), 件)
    共 = 写 + 非
    if 共 <= 0:
        return False, '费哨：缺——末 %d 件无费可计（⛔印 0%%）' % 件, 诸
    占 = 写 / 共
    红 = 占 < 界
    号 = [k for k, x in 诸 if x['号']]
    无号 = [x for _, x in 诸 if not x['号']]
    述 = '%s 费哨：末 %d 件（%s—%s·按费账之序）并其间无 W 号之件 %d（$%.0f）写书 $%.0f／非写书 $%.0f——写书之占 %.0f%%（界 ≥%.0f%%·裁_1021_省律）%s' % (
        '⛔' if 红 else '✓', len(号), 号[0] if 号 else '', 号[-1] if 号 else '', len(无号), sum(x['美元'] for x in 无号),
        写, 非, 占 * 100, 界 * 100, '：非写书之件只许「挡路：」「读者可见：」二种方开' if 红 else '')
    return 红, 述, 诸


def 许开(名, 有效之据, root=ROOT):
    """工作流账 --开 所调：返 (许否, 由)。写书之件恒许；非写书之件於哨红时须带例外之由。"""
    _, 写 = 判类(名, 类表(root))
    if 写:
        return True, ''
    红, 述, _ = 判(root)
    if not 红:
        return True, ''
    if 例外式.search(有效之据 or ''):
        return True, '费哨红而有例外之由：' + 例外式.search(有效之据).group(0)
    return False, 述 + '——此件非写书，有效之据须写「挡路：<挡哪一章之料或闸>」或「读者可见：<哪一处之病>」'


配额 = (('造', 0.75, '≥'), ('验', 0.15, '≤'), ('记', 0.05, '≤'), ('主环', 0.05, '≤'), ('余', 0.0, '≤'))   # ★1021 作者令「按最完美之资源配置比」：钱先给造剧情


def 配置之量(n, root=ROOT):
    """★1027：第 n 章之资源配置比 → ({类: 占}, 缺之由)。取 法用之守.章量（费账＋复盘「按类」之造·一处算）；⛔读 journal。
    只有其数者入（造、主环）；章量无（费账无其章）→ ({}, 由)；有费而复盘无「按类」之造 → 只主环、由书其缺。"""
    try:
        import 法用之守
        q = 法用之守.章量(n, root)
    except Exception as e:
        return {}, '法用之守.章量 读不得（%s）' % e
    if not q:
        return {}, '费账无第%d章之行' % n
    占 = {}
    if q.get('造占') is not None:
        占['造'] = q['造占']
    # 〔1119 执行之审·治3·缺即印缺〕章量 无主环行亦给 主环占 0.0（458—472 复盘「无起时」而主环行不记）——0 係缺、⛔係合：无其行即不入、书其缺
    if q.get('主环占') is not None and 有主环行(n, root):
        占['主环'] = q['主环占']
    缺 = '；'.join(([] if '造' in 占 else ['复盘无「按类」之造']) +
                  ([] if '主环' in 占 else ['主环缺（费账无第%d章之主环行·复盘无起时）' % n]))
    return 占, 缺


def 有主环行(n, root=ROOT, 行=None):
    """〔1119 执行之审·治3〕费账有第 n 章之「主环:」行否（认章同 法用之守.章量）。读不得 → None（缺）。"""
    if 行 is None:
        try:
            行 = json.load(open(os.path.join(root, '设定', '费账.json'), encoding='utf-8'))['行']
        except Exception:
            return None
    for r in 行:
        m = re.match(r'(W\d+)·第?(\d{3})(?:章|造式)', str(r.get('名', '')))
        if m and int(m.group(2)) == n and str(r.get('键', '')).startswith('主环'):
            return True
    return False


def 配置之判(占):
    """占：{类: 金或占}——只判其有数之类（⛔缺类当 0）。→ (坏[], 述)。"""
    _和 = sum(v for v in 占.values() if v is not None)
    共 = _和 if _和 > 1.0001 else 1.0           # 金（美元）则以其和为分母；占（章量之 0—1）则照用
    坏 = []
    for k, 额, 向 in 配额:
        if 占.get(k) is None:
            continue
        x = 占[k] / 共
        if (向 == '≥' and x < 额) or (向 == '≤' and x > 额 + 1e-9):
            坏.append('%s %.0f%%（配额 %s%.0f%%）' % (k, x * 100, 向, 额 * 100))
    述 = '｜'.join('%s %.0f%%' % (k, 占[k] / 共 * 100) for k, _, _ in 配额 if 占.get(k) is not None)
    return 坏, 述


def 两段(root=ROOT, 件=10, 行=None):
    """〔执行之制·治14（1124·482 主环收批）〕费哨（治3 之真尺）今段与前段之判 → [(红否, 占), (红否, 占)｜None]：
    前段＝今段之界行（末「件」个 W 件之前一件之末行）以前之账再以同尺算——连两段红即账限哨之「哨红未入账：费哨」。"""
    if 行 is None:
        try:
            行 = json.load(open(os.path.join(root, '设定', '费账.json'), encoding='utf-8'))['行']
        except Exception:
            return []
    表 = 类表(root)
    出 = []
    for _ in range(2):
        写, 非, 诸 = 算(行, 表, 件)
        共 = 写 + 非
        if 共 <= 0 or not 诸:
            出.append(None); break
        出.append((写 / 共 < 界, round(写 / 共, 3)))
        末 = {}                                           # 前段：今段之界行（同 算 之界）以前之账
        for i, r in enumerate(行):
            if not str(r.get('键', '')).startswith('主会话'):
                w = 判类(r.get('名', ''), 表)[0]
                if w:
                    末[w] = i
        号 = sorted(末, key=末.get)
        if len(号) <= 件:
            出.append(None); break
        行 = 行[:末[号[-件 - 1]] + 1]
    return (出 + [None])[:2]


def 无估无由(root=ROOT, 行=None):
    """〔执行之制·治13(c)、治14（1124·482 主环收批）〕费账「估：无」之行（费审 --记 所标）、「无由」之行（非写而费哨红、名无挡路／读者可见）
    → (无估[(键, 名, 美元)], 无由[(键, 名, 美元)])。账限哨 治14 读之（各累三即「哨红未入账」之到期）。"""
    if 行 is None:
        try:
            行 = json.load(open(os.path.join(root, '设定', '费账.json'), encoding='utf-8'))['行']
        except Exception:
            return [], []
    无估 = [(r.get('键'), r.get('名', ''), float(r.get('美元') or 0)) for r in 行 if r.get('估') == '无']
    无由 = [(r.get('键'), r.get('名', ''), float(r.get('美元') or 0)) for r in 行 if r.get('无由')]
    return 无估, 无由


def 无估之印(root=ROOT):
    a, b = 无估无由(root)
    return '%s 无估之件 %d（$%.0f）、无由之非写 %d（$%.0f）——各累三即入账限哨之到期（哨红未入账·执行之制 治13(c)、治14）' % (
        '⚠' if a or b else '✓', len(a), sum(x[2] for x in a), len(b), sum(x[2] for x in b))


def 跑中(rid, 估):
    """★1021 作者令「方法过於耗即立刻停止」：一 Run 跑中之费（费审·零 token）对其估——逾 1.5 倍即⛔停。返 (逾否, 述)。"""
    import 费审
    d = 费审.找目录(rid)
    if not d:
        return False, '跑中：缺——无此 Run 之目录（%s）；⛔当 $0' % rid   # 〔1119 执行之审·治3·缺即印缺〕
    金 = sum(x['金'] for x in 费审.审(d))
    逾 = 金 > 1.5 * float(估)
    return 逾, '%s 跑中 %s：已花 $%.2f／估 $%.2f（%.1f 倍）%s' % ('⛔' if 逾 else '✓', rid, 金, float(估), 金 / max(0.01, float(估)),
                                                          '——逾 1.5 倍：立停（TaskStop），除非余一席而停之即废已付者，须一句写由' if 逾 else '')


def 量之源(诸章, 章费, root=ROOT):
    """〔1119 执行之审·治4(e)〕末三章之量源一行（只印·⛔拦）：工作流账之件（--开 之果：有其 W、或名起「第N章」，且有「起」）、
    费账之主环行（复盘／--记主 之果）。旧 458—472 十五章无件 → 复盘无起时 → 主环行不记、逾估之验空，而无一器言之。
    取证於仓中之账（随 git 而同），⛔取 _器之迹（各容器各一份；主环行由复盘以函记、⛔留 `--记主` 之迹——以迹判即恒误红）。"""
    if not 诸章:
        return '量之源：缺（费账无章之行）'
    try:
        件们 = json.load(open(os.path.join(root, '设定', '工作流账.json'), encoding='utf-8'))['件']
    except Exception as e:
        件们 = None
        件述 = '件 缺（工作流账读不得：%s）' % str(e)[:40]
    if 件们 is not None:
        无件 = [n for n in 诸章 if not any(x.get('起') and (x.get('id') == 章费[n]['W'] or str(x.get('名', '')).startswith('第%d章' % n))
                                          for x in 件们)]
        件述 = '工作流账之件 %d/%d%s' % (len(诸章) - len(无件), len(诸章),
                                     '（缺 %s）' % '、'.join('%d %s' % (n, 章费[n]['W']) for n in 无件) if 无件 else '')
    无主 = [n for n in 诸章 if not 章费[n]['有主']]
    主述 = '主环行 %d/%d' % (len(诸章) - len(无主), len(诸章))
    够 = len(诸章) >= 3                                   # 不足三章⛔言「逾三章」
    俱缺 = 够 and 件们 is not None and len(无件) == len(诸章)
    主俱缺 = 够 and len(无主) == len(诸章)
    号 = '⛔' if 俱缺 or 主俱缺 else ('⚠' if 无主 or 件们 is None or 无件 else '✓')
    语 = ('——逾三章无件：`工作流账.py --开` 未行或落空（→复盘无起时→主环行、逾估之验俱空·治4）' if 俱缺 else
          '——逾三章主环行俱缺（复盘无起时）' if 主俱缺 else '')
    return '%s 量之源（末三章 %s）：%s｜%s%s' % (号, '、'.join(str(n) for n in 诸章), 件述, 主述, 语)


def 章检(root=ROOT):
    """★1021 作者令「每一章只要一开始就看看原来的方法还行不行……一想能想出来，⛔过度消耗」：零 token 印数行——
    末五章之费与其势、主环之占、写书之占、账限之欠，并三问（章末简式复盘照答）。返 [行]。"""
    L = ['── 开章之检（零 token·省律）──']
    try:
        行 = json.load(open(os.path.join(root, '设定', '费账.json'), encoding='utf-8'))['行']
        源缺 = ''
    except Exception as e:
        行, 源缺 = [], '费账读不得（%s）' % e
    表 = 类表(root)
    章费 = {}
    for r in 行:
        键 = str(r.get('键', ''))
        if 键.startswith('主会话'):
            continue
        名 = r.get('名', '') or ''
        w, 写 = 判类(名, 表)
        # 〔1119 执行之审·治3(b)〕旧式 第?\d{3}章?造式|二代 不认「W146·第472章」——末五章停在 420—427、466 已六章；今认章同 :182，按章号取末五
        m = re.search(r'第?(\d{3})(?:章|造式|二代)', 名)
        if not w or not m:
            continue
        a = 章费.setdefault(int(m.group(1)), {'W': w, '席': 0.0, '主': 0.0, '有主': False})
        if 键.startswith('主环'):
            a['主'] += float(r.get('美元') or 0); a['有主'] = True
        else:
            a['席'] += float(r.get('美元') or 0)
    末 = sorted(章费)[-5:]
    if not 末:
        L.append('  末五章：缺（%s）——⛔印 0' % (源缺 or '费账无章之行'))
    else:
        # 〔1119 执行之审·治3·缺即印缺〕无主环行之章印「主环 缺」——⛔印 0%（旧 466 印「主环 0%」，实係复盘无起时而不记）
        L.append('  末五章：' + '｜'.join('第%d章 $%.0f（主环 %s）' % (n, 章费[n]['席'] + 章费[n]['主'],
                 ('%.0f%%' % (100 * 章费[n]['主'] / max(0.01, 章费[n]['席'] + 章费[n]['主']))) if 章费[n]['有主'] else '缺') for n in 末))
        均 = sum(章费[n]['席'] + 章费[n]['主'] for n in 末) / len(末)
        缺主 = [n for n in 末 if not 章费[n]['有主']]
        L.append('  每章均 $%.0f；的 ≤$30、主环 ≤$5（裁_1021_省律）%s' % (均, '——主环缺 %d 章（其主环不在均内）' % len(缺主) if 缺主 else ''))
        上 = 末[-1]
        占, 缺 = 配置之量(上, root)
        if not 占:
            L.append('  资源配置比（第%d章）：算不得（%s）——⛔印 0%%' % (上, 缺))
        else:
            坏, 述 = 配置之判(占)
            L.append('  资源配置比（第%d章·法用之守.章量）：%s%s——%s' % (上, 述, '（%s）' % 缺 if 缺 else '',
                     '⛔失配：' + '；'.join(坏) if 坏 else ('⚠只判其有数者、缺者⛔判合' if 缺 else '✓合配额')))
        L.append('  ' + 量之源(末[-3:], 章费, root))
    L.append('  ' + 判(root)[1])
    L.append('  ' + 无估之印(root))
    try:
        import 账限哨
        L.append('  ' + 账限哨.印(root)[1][0])
    except Exception:
        pass
    L.append('  三问（章末 `复盘.py W 题 runs --简 --平台 $X` 一句一答）：法行否｜最贵之席值否｜进化（入账 X 号或已行或无）')
    return L


def 自测():
    r = []
    def T(名, 条):
        r.append((名, bool(条)))
        print(('  ✓ ' if 条 else '  ✗ ') + 名)
    表 = {'W1': '一章', 'W2': '治器设计', 'W3': '造剧情', 'W4': '核验'}
    行 = [{'键': 'wf_a', '名': 'W1·写', '美元': 30}, {'键': '主环:x', '名': 'W1·写', '美元': 10},
          {'键': 'wf_b', '名': 'W2·器', '美元': 50}, {'键': 'wf_c', '名': 'W3·段', '美元': 20},
          {'键': '主会话:z', '名': 'W1·写', '美元': 999}, {'键': 'wf_d', '名': 'W4·审', '美元': 10}]
    写, 非, 诸 = 算(行, 表, 10)
    T('①写书＝一章＋造剧情（30+10+20）', 写 == 60)
    T('②非写书＝治器＋核验（50+10）', 非 == 60)
    T('③主会话之行⛔重加', all(x[1]['美元'] < 999 for x in 诸))
    写2, 非2, 诸2 = 算(行, 表, 2)
    T('④末 N 件按费账行序取（末二件 W3、W4；此局行序同号序）', [w for w, _ in 诸2] == ['W3', 'W4'] and 写2 == 20 and 非2 == 10)
    # 〔1119 执行之审·治3(a)〕④之二 守牙：号大而行早之件（W901 记於 W3 之前）⛔占末段——旧按 W 号之数排，W901—W904 恒占末十
    _行4 = 行[:2] + [{'键': 'wf_9', '名': 'W901·器', '美元': 70}] + 行[2:]
    T('④之二 号大而行早（W901 在 W2 之前记）→ 末二件仍 W3、W4，W901⛔入（旧按号排则恒占末段）',
      [w for w, _ in 算(_行4, 表, 2)[2]] == ['W3', 'W4'] and 'W901' in [w for w, _ in 算(_行4, 表, 9)[2]])
    T('⑤无复盘之件以名判：「W9·第401章造式」写书', 判类('W9·第401章造式', 表)[1] is True)
    T('⑥无复盘之件以名判：「W9·D1之备」非写书', 判类('W9·D1之备', 表)[1] is False)
    T('⑦例外之由须四字以上', 例外式.search('挡路：401 之料缺此') and not 例外式.search('挡路：无'))
    # ⑧许开：以 tempdir 造一局红账
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, '设定', '复盘'))
        json.dump({'行': [{'键': 'wf_a', '名': 'W1·器', '美元': 90}, {'键': 'wf_b', '名': 'W2·第9章造式', '美元': 10}]},
                  open(os.path.join(d, '设定', '费账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        红, 述, _ = 判(d)
        T('⑧写书 10%＜七成即红', 红)
        T('⑨哨红：非写书之件无例外拒开', 许开('W3·治器三批', '据', d)[0] is False)
        T('⑩哨红：非写书之件带「挡路：」许开', 许开('W3·治器三批', '挡路：401 之料缺远引', d)[0] is True)
        T('⑪哨红：写书之件恒许', 许开('W3·第10章造式', '', d)[0] is True)
    坏, _ = 配置之判({'造': 80, '验': 10, '记': 5, '主环': 5, '余': 0})
    T('⑫配置合额：造 80%、验 10%、记 5%、主环 5%', not 坏)
    坏, _ = 配置之判({'造': 50, '验': 10, '记': 5, '主环': 35, '余': 0})
    T('⑬配置失额：主环 35%、造 50% 俱报', len(坏) == 2 and any('主环' in x for x in 坏) and any('造' in x for x in 坏))
    # ⑭⑮1027 执行之审 #64 #80：配置比只取 法用之守.章量（⛔读 journal）；本机无 journal、复盘无按类 → 「算不得」或只印主环，⛔印 0%
    坏, 述 = 配置之判({'造': 0.695, '主环': 0.033})
    T('⑭占式（章量）：造 70% 失配、主环 3% 合；缺类（验、记、余）⛔当 0 而报', 坏 == ['造 70%（配额 ≥75%）'] and 述 == '造 70%｜主环 3%')
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, '设定', '复盘'))
        json.dump({'行': [{'键': 'wf_x', '名': 'W9·第409章造式', '美元': 60}, {'键': '主环:x', '名': 'W9·第409章造式', '美元': 3}]},
                  open(os.path.join(d, '设定', '费账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        L = 章检(d)
        配 = [x for x in L if '资源配置比' in x]
        T('⑮本机无 journal、复盘无「按类」：只印主环之占并书其缺，⛔印造 0%（旧式每会话假⛔）',
          len(配) == 1 and '主环 5%' in 配[0] and '复盘无「按类」之造' in 配[0] and '造 0%' not in 配[0])
        json.dump({'行': []}, open(os.path.join(d, '设定', '费账.json'), 'w', encoding='utf-8'))
        T('⑮之二 费账无章 → 不印配置比（⛔印 0%）', not any('0%' in x for x in 章检(d) if '资源配置比' in x))
    T('⑯真读：410 之配置比取得造、主环二占（法用之守.章量）', set(配置之量(410)[0]) == {'造', '主环'})
    T('⑰⛔读 journal 之路已删（配置比·费审.找目录 之调）', ('def 配置' + '比(') not in open(__file__, encoding='utf-8').read().split('def 自测')[0])
    # ⑱—㉖〔1119 执行之审·治3、治4(e)〕无号之行入计、末段按行序、章检认「W\d+·第\d+章」、缺即印缺
    _行18 = 行 + [{'键': 'wf_e', '名': '', '美元': 40}, {'键': '主环:2026-11-18T00:00:00Z', '名': '总编辑之坐·2026-11-18', '美元': 25},
                 {'键': 'wf_f', '名': '剧情庭·第9段', '美元': 5}]
    写18, 非18, 诸18 = 算(_行18, 表, 10)
    _诸18 = dict(诸18)
    T('⑱无 W 号之 wf_ 行以键自为一件：名空归非写书（旧 :67 跳过——1117 起 $377.49 不计）',
      'wf_e' in _诸18 and _诸18['wf_e']['写'] is False and 非18 == 60 + 40 + 25)
    T('⑲「总编辑之坐·<日>」之主环行（无号）计入非写书；无号而名为写书者（剧情庭）照名判写书；主会话:⛔重加',
      _诸18['主环:2026-11-18T00:00:00Z']['写'] is False and _诸18['wf_f']['写'] is True and 写18 == 65
      and all(x['美元'] < 999 for _, x in 诸18))
    _写20, _非20, _诸20 = 算(_行18, 表, 1)
    T('⑳末段之界：末一个 W 件（W4）之前一 W 件（W3）之末行为界，界後无号之件俱计、界前者⛔计',
      [k for k, _ in _诸20] == ['W4', 'wf_e', '主环:2026-11-18T00:00:00Z', 'wf_f'] and _写20 == 5 and _非20 == 10 + 40 + 25)
    import subprocess
    _旧 = subprocess.run(['git', 'show', 'a6c9f7a04:设定/费账.json'], cwd=ROOT, capture_output=True, text=True)
    try:
        _真 = json.loads(_旧.stdout)['行']
    except Exception:
        _真 = []
    T('㉑真迹之源：a6c9f7a04（执行之审之设计所据）之费账读得（416 行）', len(_真) == 416)
    if _真:
        _表 = 类表(ROOT)
        _w, _n, _诸 = 算(_真, _表, 10)
        _号 = [k for k, x in _诸 if x['号']]
        T('㉒回放 a6c9f7a04 之费账：末十件 W137—W146、W901—W904⛔在；wf_066cd6fe（$56.88）计入非写书；非写书之占约三成五（%.1f%%）、判红' % (100 * _n / (_w + _n)),
          _号 == ['W%d' % k for k in range(137, 147)] and not any(k.startswith('W90') for k, _ in _诸)
          and any(k.startswith('wf_066cd6fe') and not x['写'] and abs(x['美元'] - 56.88) < 0.01 for k, x in _诸)
          and 0.33 < _n / (_w + _n) < 0.37 and _w / (_w + _n) < 界)
        _至 = next((i for i, r in enumerate(_真) if r.get('键') == 'wf_21412c7e-bc2'), None)
        _段 = _真[:_至 + 1] if _至 is not None else []
        _w19, _n19, _ = 算(_段, _表, 19)
        _w19b, _n19b, _ = 算(_段 + [{'键': '主环:2026-11-19T00:00:00Z', '名': '总编辑之坐·1117—1119', '美元': 105.83}], _表, 19)
        T('㉓回放 1117 起（W128—W146）：写书 $%.2f／非写书 $%.2f＝设计所算 $958.09／$404.72；添总编辑之坐 $105.83 → 非写书 %.1f%%（约三成五）' % (
          _w19, _n19, 100 * _n19b / (_w19b + _n19b)),
          abs(_w19 - 958.09) < 0.01 and abs(_n19 - 404.72) < 0.01 and abs(_n19b - 510.55) < 0.01 and 0.34 < _n19b / (_w19b + _n19b) < 0.36)
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, '设定'))
            json.dump({'行': _真}, open(os.path.join(d, '设定', '费账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
            _账 = subprocess.run(['git', 'show', 'a6c9f7a04:设定/工作流账.json'], cwd=ROOT, capture_output=True, text=True).stdout
            open(os.path.join(d, '设定', '工作流账.json'), 'w', encoding='utf-8').write(_账)
            os.symlink(os.path.join(ROOT, '设定', '复盘'), os.path.join(d, '设定', '复盘'))
            _L = 章检(d)
        _末 = next((x for x in _L if '末五章' in x), '')
        T('㉔回放 a6c9f7a04：章检之末五章＝468—472（旧式只认「造式／二代」→ 420—427、466）',
          re.findall(r'第(\d{3})章 \$', _末) == ['468', '469', '470', '471', '472'] and '420' not in _末 and '466' not in _末)
        _配 = next((x for x in _L if '资源配置比' in x), '')
        T('㉕回放：468—472 无主环行 → 末五章印「主环 缺」⛔「主环 0%」；配置比书主环之缺而⛔「✓合配额」（旧 466 印主环 0%·✓合）',
          _末.count('主环 缺') == 5 and '主环 0%' not in _末 and '主环缺' in _配 and '✓合配额' not in _配 and '主环 0%' not in _配)
        _源 = next((x for x in _L if '量之源' in x), '')
        T('㉖回放：末三章 470—472 工作流账俱无件（W143、W145、W146）→ ⛔「逾三章无件」（只印、⛔拦）',
          _源.startswith('  ⛔') and '0/3' in _源 and 'W146' in _源 and '逾三章无件' in _源)
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, '设定', '复盘'))
        _红, _述, _ = 判(d)
        _L = 章检(d)
        T('㉗费账读不得 → 判印「缺」、⛔红、⛔「0%」；章检之末五章印「缺」',
          _红 is False and '缺' in _述 and '0%' not in _述.replace('⛔印 0%', '')
          and any('末五章：缺' in x for x in _L))
        json.dump({'行': [{'键': 'wf_x', '名': 'W7·第407章', '美元': 50}, {'键': '主环:a', '名': 'W7·第407章', '美元': 2},
                         {'键': 'wf_y', '名': 'W8·第408章', '美元': 50}, {'键': 'wf_z', '名': 'W9·第409章', '美元': 50},
                         {'键': '主环:c', '名': 'W9·第409章', '美元': 2}]},
                  open(os.path.join(d, '设定', '费账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        json.dump({'件': [{'id': 'W7', '名': '第407章（甲）', '起': '2026-01-01T00:00Z'}, {'id': 'W8', '名': '第408章（乙）', '起': '2026-01-01T00:00Z'},
                         {'id': 'W99', '名': '第409章（丙）', '起': '2026-01-01T00:00Z'}]},
                  open(os.path.join(d, '设定', '工作流账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        _源 = next((x for x in 章检(d) if '量之源' in x), '')
        T('㉘量之源：件 3/3（W99 名起「第409章」亦认）、主环行 2/3 → ⚠（⛔⛔：不足俱缺）',
          _源.startswith('  ⚠') and '件 3/3' in _源 and '主环行 2/3' in _源)
    _估行 = [{'键': 'wf_a', '名': '某审', '美元': 10, '估': '无'}, {'键': 'wf_b', '名': 'W9 x', '美元': 5, '无由': True}, {'键': 'wf_c', '名': 'W1·第1章', '美元': 50}]
    _a, _b = 无估无由(行=_估行)
    T('㉙〔治13(c)〕费账「估：无」→ 无估之件、「无由」→ 无由之非写（各计其数与美元）', [x[0] for x in _a] == ['wf_a'] and [x[0] for x in _b] == ['wf_b'])
    ok = sum(v for _, v in r)
    print('费哨·自测 %d/%d%s' % (ok, len(r), ' 全通' if ok == len(r) else ' 未过'))
    return ok == len(r)


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--自测' in a:
        sys.exit(0 if 自测() else 1)
    if '--跑' in a:
        i = a.index('--跑')
        逾, 述 = 跑中(a[i + 1], a[i + 2])
        print(述); sys.exit(1 if 逾 else 0)
    if '--章' in a:
        print('\n'.join(章检())); sys.exit(0)
    n = int(a[a.index('--件') + 1]) if '--件' in a else 10
    红, 述, 诸 = 判(ROOT, n)
    print(述)
    print(无估之印(ROOT))
    for w, x in 诸:
        print('  %s %-28s $%7.2f %s' % (w, x['名'][:28], x['美元'], '写书' if x['写'] else '非写书'))
    sys.exit(1 if 红 else 0)
