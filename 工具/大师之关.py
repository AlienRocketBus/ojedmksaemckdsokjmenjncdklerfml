#!/usr/bin/env python3
"""大师之关（0926·作者令立）：三执笔之构思、行家之审、创作记录、自我进化——**封了版的章，缺一样即红**。

⛔其立之由：作者令「必须得执行起来，别弄出来不执行」。席令里写了不等於席照做了；
  故凡自 `自章` 起封版之章，逐章亲查盘上之档，缺一样即红，推闸据此拦停。

查五样（第 N 章）：
  ①构思：版本/第N章/起草_甲／乙／丙_构思.md 三份俱在，各 ≥400 字，且各有「进化账所避」一行（无稿之席四条俱合者免查其细·见下★1118）；
  ②行家评：版本/第N章/_行家评.md 在，含「小说家」「总编辑」二节与「## 合稿逐条回话」；
  ③创作记录：版本/第N章/_创作记录.md 在，一至六节俱全（「一、」…「六、」）；
  ④进化：设定/大师进化账.md 里有「[第N章]」之条；
  ⑤封版：以 版本/第N章/_十一轮.json 在为「已封」之据——未封之章不查（正在写的不拦）。

用法：python3 工具/大师之关.py          # 全书（自 自章 起）
      python3 工具/大师之关.py 377      # 只查一章
      python3 工具/大师之关.py --自测
      python3 工具/大师之关.py --标无稿 N 宽 稿号[,稿号]   # 写者（造章.js 选之先跑自调·零 token；亦可主环手跑）：
            执笔未交而盘上缺档之席 → 於其构思书一行因中立之「无稿：执笔未交、盘上缺档（…其因⛔断…）」；只印稿号（⛔泄执笔之名·蒙名）。
            ⛔代「缺档」：无稿之免 照验其席之实（蒙号之稿档不在＋_创作记录.md 与 _行家评.md 俱有其号之缺档行＋起草_稿 ≥3）——本器只书其一。
★1118 总编辑复核「大师之关」→ 改（2f02beeef）：无稿之免以「无稿」之实逐席严验、⛔问其因——
  构思有「无稿：」一行（旧「无稿：…拦」并认）＋其席蒙号之稿档 起草_<号>.md 不在＋_创作记录.md 与 _行家评.md 俱有一行并载其号与「缺档」＋起草_稿 ≥3，
  四条俱合方免（缺一照查）；免者印於 ✓ 行（⛔无声）。号＝稿号[(干序+N) % 宽]（＝造章.js 蒙号），宽取 _行家评.md「蒙名读 N 稿」、无者取盘上 起草_?_构思.md 之数。
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import os, re, sys, tempfile, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
自章 = 377   # 大师之制自 377 起生效；376 及以前用旧制，不追究


干 = '甲乙丙丁戊己庚'                                          # 造章.js 功底之序
稿号们 = ('稿一', '稿二', '稿三', '稿四', '稿五', '稿六', '稿七')   # 造章.js 稿号


def 号之席(n, 宽, 号):
    """造章.js 蒙号(名)＝稿号[(干序+N) % 宽] 之逆：稿号 → 执笔之名（记料.py _胜嫁之构思 同式；负测_造章令 以真渲之令对之）。"""
    k = 稿号们.index(号)
    if not (3 <= 宽 <= 7 and k < 宽):
        raise ValueError('稿号 %s 不在宽 %d 之内' % (号, 宽))
    return 干[(k - n) % 宽]


def 席之号(n, 宽, 名):
    """号之席 之顺：执笔之名 → 其稿号＝造章.js 蒙号(名)＝稿号[(干序+N) % 宽]。"""
    i = 干.index(名)
    if not (3 <= 宽 <= 7 and i < 宽):
        raise ValueError('席 %s 不在宽 %d 之内' % (名, 宽))
    return 稿号们[(i + n) % 宽]


def 宽之(d):
    """其章执笔之宽：_行家评.md「蒙名读 N 稿」（造章.js 选令所定之档首）；无者取盘上 起草_?_构思.md 之数。"""
    import glob as _g
    f = os.path.join(d, '_行家评.md')
    m = re.search(r'蒙名读\s*(\d)\s*稿', open(f, encoding='utf-8', errors='replace').read()) if os.path.exists(f) else None
    return int(m.group(1)) if m else len(_g.glob(os.path.join(d, '起草_?_构思.md')))


def 无稿之免(d, n, 名, t):
    """★1118 总编辑复核「大师之关」→改（代 1117 之「拦而无稿」）：无稿之席不查其构思——以无稿之实逐席严验、⛔问其因。→ 其号（免）或 None（照查）。
    四条俱合方免（缺一照查）：①构思 t 有「无稿：」一行（旧「无稿：…拦」并认）；②其席蒙号之稿档 起草_<号>.md 不在；
    ③_创作记录.md 与 _行家评.md 俱有一行并载其号与「缺档」（他号之缺档⛔代）；④盘上 起草_稿*.md ≥3。
    其由：零稿之席行家判缺档致命、不入评，选、合⛔读构思，记料只喂胜嫁之构思——其构思无下游；而稿在之席照查（旧免只验「某处有缺档」，稿在亦免＝假绿）。"""
    import glob as _g
    if not re.search(r'^无稿[：:]', t, re.M):
        return None
    try:
        号 = 席之号(n, 宽之(d), 名)
    except ValueError:
        return None
    if os.path.exists(os.path.join(d, '起草_%s.md' % 号)):
        return None
    def 行载(档):
        f = os.path.join(d, 档)
        return os.path.exists(f) and any(号 in L and '缺档' in L for L in open(f, encoding='utf-8', errors='replace').read().splitlines())
    if not (行载('_创作记录.md') and 行载('_行家评.md')):
        return None
    return 号 if len(_g.glob(os.path.join(d, '起草_稿*.md'))) >= _整稿之界(n, os.path.dirname(os.path.dirname(os.path.normpath(d)))) else None


def _整稿之界(n, root):
    """〔W919·X138〕N≥489 有二稿之录（承.py N --二稿 "由"）→ 2；〔W924〕有一稿之录（--一稿）→ 1；余 3（import 不得或录读崩照 3·⛔放）。root 显传（自测之临时之树⛔读真仓之录）。"""
    try:
        import 承 as _承
        return _承.整稿之界(n, root)
    except Exception:
        return 3


def 标无稿(n, 宽, 号, root=ROOT):
    """★1118 写者：执笔未交而盘上缺档之席，於其构思书一行因中立之「无稿：…」。→ (名, 判)。
    书语因中立（执笔未交、盘上缺档、其因⛔断）：盘上只见「无稿」之实，其因（平台之检、容器重启、席首回即死…）⛔断、⛔书。
    四条俱合方书（缺一⛔书、照红）：①稿档不在（选之先跑印「缺档」之同一判） ②起草_稿*.md ≥3 ③其构思今照 查() 即红（满者⛔书） ④未书过（⛔重书）；
    只书 甲乙丙（大师之关所查）。⛔代 _创作记录.md／_行家评.md 之「缺档」——无稿之免 照验四条，本器只书其一。"""
    import glob as _g
    名 = 号之席(n, 宽, 号)
    if 名 not in '甲乙丙':
        return 名, '⛔非大师之关所查之席——⛔书'
    d = os.path.join(root, '版本', '第%d章' % n)
    if os.path.exists(os.path.join(d, '起草_%s.md' % 号)):
        return 名, '⛔稿档在——非无稿，⛔书'
    k = len(_g.glob(os.path.join(d, '起草_稿*.md')))
    if k < _整稿之界(n, root):
        return 名, '⛔起草_稿 不足三——⛔书'
    f = os.path.join(d, '起草_%s_构思.md' % 名)
    t = open(f, encoding='utf-8', errors='replace').read() if os.path.exists(f) else None
    if t is not None and re.search(r'^无稿[：:]', t, re.M):
        return 名, '已书（⛔重书）'
    if not any(x.startswith('构思·%s ' % 名) for x in 查(n, root)):
        return 名, '⛔构思照查已全——⛔书'
    行 = '无稿：执笔未交、盘上缺档（%s 不在、起草_稿 %d 份；其因⛔断；大师之关.py --标无稿 自书）\n' % (号, k)
    with open(f, 'a', encoding='utf-8') as o:
        o.write(('# 执笔·%s之构思（无稿）\n' % 名 if t is None else ('' if t.endswith('\n') or not t else '\n')) + 行)
    return 名, '已书'


def 查(n, root=ROOT, 免=None):
    """→ 缺之列；免（list）给者，无稿之免所免之席（名）追记其中。"""
    d = os.path.join(root, '版本', '第%d章' % n)
    缺 = []
    for 名 in '甲乙丙':
        f = os.path.join(d, '起草_%s_构思.md' % 名)
        if not os.path.exists(f):
            缺.append('构思·%s 不在' % 名); continue
        t = open(f, encoding='utf-8', errors='replace').read()
        if 无稿之免(d, n, 名, t):              # ★1118（代 1117 之拦而无稿）：无稿之实逐席严验、⛔问其因
            if 免 is not None:
                免.append(名)
            continue
        if len(re.sub(r'\s', '', t)) < 400:
            缺.append('构思·%s 不足 400 字' % 名)
        if '进化账所避' not in t:
            缺.append('构思·%s 无「进化账所避」' % 名)
        # 0927 作者令·完美主义（设定/反面教材.md）：自 380 章起构思须有「满分之问」
        if n >= 380 and '满分之问' not in t:
            缺.append('构思·%s 无「满分之问」（反面教材·一次到位）' % 名)
    f = os.path.join(d, '_行家评.md')
    if not os.path.exists(f):
        缺.append('_行家评.md 不在')
    else:
        t = open(f, encoding='utf-8', errors='replace').read()
        for k in ('小说家', '总编辑', '## 合稿逐条回话'):
            if k not in t:
                缺.append('_行家评.md 无「%s」' % k)
        # 0927 作者令·立得住之律（设定/立得住之律.md）：自 380 章起，行家须逐条过「因立不立得住」
        if n >= 380 and '## 立得住' not in t:
            缺.append('_行家评.md 无「## 立得住」（立得住之律）')
    f = os.path.join(d, '_创作记录.md')
    if not os.path.exists(f):
        缺.append('_创作记录.md 不在')
    else:
        t = open(f, encoding='utf-8', errors='replace').read()
        for k in '一二三四五六':
            if k + '、' not in t:
                缺.append('_创作记录.md 缺第%s节' % k)
    f = os.path.join(root, '设定', '大师进化账.md')
    t = open(f, encoding='utf-8', errors='replace').read() if os.path.exists(f) else ''
    if '[第%d章]' % n not in t:
        缺.append('进化账无「[第%d章]」之条' % n)
    return 缺


def 已封诸章(root=ROOT):
    out = []
    vd = os.path.join(root, '版本')
    if not os.path.isdir(vd):
        return out
    for x in os.listdir(vd):
        m = re.match(r'第(\d+)章$', x)
        if m and int(m.group(1)) >= 自章 and os.path.exists(os.path.join(vd, x, '_十一轮.json')):
            out.append(int(m.group(1)))
    return sorted(out)


def 全(root=ROOT, 免=None):
    """→ {章: 缺}；免（list）给者，追记 (章, 名) 之所免。"""
    红 = {}
    for n in 已封诸章(root):
        免n = []
        缺 = 查(n, root, 免n)
        if 免 is not None:
            免.extend((n, x) for x in 免n)
        if 缺:
            红[n] = 缺
    return 红


def 自测():
    ok = 0; 共 = 0
    tmp = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(tmp, '设定'))
        d = os.path.join(tmp, '版本', '第400章'); os.makedirs(d)
        open(os.path.join(tmp, '设定', '大师进化账.md'), 'w').write('# 账\n')
        # ①未封者不查
        共 += 1; ok += (全(tmp) == {})
        # ②已封而一样也没有 → 红
        open(os.path.join(d, '_十一轮.json'), 'w').write('{}')
        共 += 1; r = 全(tmp); ok += (400 in r and len(r[400]) >= 5)
        # ③五样俱全 → 绿
        for 名 in '甲乙丙':
            open(os.path.join(d, '起草_%s_构思.md' % 名), 'w').write('进化账所避：某条\n满分之问：三路\n' + '构' * 420)
        open(os.path.join(d, '_行家评.md'), 'w').write('【小说家】…\n【总编辑】…\n## 立得住\n无\n## 合稿逐条回话\n1. 改\n')
        open(os.path.join(d, '_创作记录.md'), 'w').write(''.join(k + '、x\n' for k in '一二三四五六'))
        open(os.path.join(tmp, '设定', '大师进化账.md'), 'a').write('- [第400章] 教训｜出处｜往后\n')
        共 += 1; ok += (全(tmp) == {})
        # ④构思缺「进化账所避」 → 红（不许只凑字数）
        open(os.path.join(d, '起草_乙_构思.md'), 'w').write('构' * 500)
        共 += 1; r = 全(tmp); ok += (400 in r and any('进化账所避' in x for x in r[400]))
        # ⑤行家评无合稿回话 → 红（行家之改法须逐条办）
        open(os.path.join(d, '起草_乙_构思.md'), 'w').write('进化账所避：某条\n满分之问：三路\n' + '构' * 420)
        open(os.path.join(d, '_行家评.md'), 'w').write('【小说家】…\n【总编辑】…\n')
        共 += 1; r = 全(tmp); ok += (400 in r and any('合稿逐条回话' in x for x in r[400]))
        # ⑥之一构思无「满分之问」 → 红
        open(os.path.join(d, '_行家评.md'), 'w').write('【小说家】…\n【总编辑】…\n## 立得住\n无\n## 合稿逐条回话\n1. 改\n')
        open(os.path.join(d, '起草_丙_构思.md'), 'w').write('进化账所避：某条\n' + '构' * 420)
        共 += 1; r = 全(tmp); ok += (400 in r and any('满分之问' in x for x in r[400]))
        # ⑥之二★1117→1118 改：丙无稿——构思有「无稿：」一行＋其蒙号之稿档不在（宽五·400 丙＝稿三）＋_创作记录.md 与 _行家评.md 俱有「稿三…缺档」之行＋起草_稿 ≥3 → 不查；缺一照红
        评 = '造式二代：一位独立行家兼小说家、总编辑两眼，蒙名读 5 稿（稿一／稿二／稿三／稿四／稿五）\n【小说家】…\n【总编辑】…\n## 立得住\n无\n## 合稿逐条回话\n1. 改\n'
        评缺 = 评 + '稿三：先跑印「缺档」，判致命\n'
        记 = ''.join(k + '、x\n' for k in '一二三四五六')
        open(os.path.join(d, '_行家评.md'), 'w').write(评缺)
        open(os.path.join(d, '起草_丙_构思.md'), 'w').write('# 丙\n无稿：执笔被平台安全之检拦\n')    # 旧「无稿：…拦」之行（并认）
        红丙 = lambda: any('构思·丙' in x for x in 全(tmp).get(400, []))
        共 += 1; ok += 红丙()                                                    # 记无缺档、无稿 → 照红
        open(os.path.join(d, '_创作记录.md'), 'a').write('| 稿三 | 丙 | （缺档） |\n')
        for k in '一二四':
            open(os.path.join(d, '起草_稿%s.md' % k), 'w').write('稿')
        共 += 1; ok += not 红丙()                                                # 俱足 → 不查
        os.remove(os.path.join(d, '起草_稿四.md'))
        共 += 1; ok += 红丙()                                                    # 稿只二 → 照红
        open(os.path.join(d, '起草_稿四.md'), 'w').write('稿')
        # ⑥之三★1118（总编辑复核·大师之关→改）：免者印（⛔无声）；号＝造章.js 蒙号（席之号＝号之席之顺）
        免 = []; r = 全(tmp, 免)
        共 += 1; ok += (not any('构思·丙' in x for x in r.get(400, [])) and 免 == [(400, '丙')] and 席之号(400, 5, '丙') == '稿三'
                       and all(号之席(n, w, 席之号(n, w, 名)) == 名 for n in range(377, 480) for w in range(3, 8) for 名 in 干[:w]))
        # ⑥之四★1118 洞之补：其席之稿档在（稿三在盘·入评）而标「无稿」→ 照红（旧免只验某处有缺档、稿 ≥3：假绿）
        open(os.path.join(d, '起草_稿三.md'), 'w').write('稿')
        共 += 1; ok += 红丙()
        os.remove(os.path.join(d, '起草_稿三.md'))
        # ⑥之五★1118：缺档只在他号之行（创作记录只「稿五…缺档」）→ 照红
        open(os.path.join(d, '_创作记录.md'), 'w').write(记 + '| 稿五 | 戊 | （缺档） |\n')
        共 += 1; ok += 红丙()
        open(os.path.join(d, '_创作记录.md'), 'w').write(记 + '| 稿三 | 丙 | （缺档） |\n')
        # ⑥之六★1118：行家评无「稿三…缺档」之行（其号之行无缺档、缺档只在他号）→ 照红
        open(os.path.join(d, '_行家评.md'), 'w').write(评 + '稿三：判致命\n稿五：缺档\n')
        共 += 1; ok += 红丙()
        open(os.path.join(d, '_行家评.md'), 'w').write(评缺)
        # ⑥之七★1118：因中立之行（--标无稿 所书之式）→ 免；构思无「无稿：」之行 → 照红
        open(os.path.join(d, '起草_丙_构思.md'), 'w').write('# 丙\n无稿：执笔未交、盘上缺档（稿三 不在、起草_稿 3 份；其因⛔断；大师之关.py --标无稿 自书）\n')
        共 += 1; ok += not 红丙()
        open(os.path.join(d, '起草_丙_构思.md'), 'w').write('# 丙\n执笔未交、稿三缺档\n')
        共 += 1; ok += 红丙()
        # ⑥之八★1118：宽之所取——行家评无「蒙名读 N 稿」者取盘上构思之数（三 → 400 丙＝稿一，稿一在盘）→ 照红
        open(os.path.join(d, '起草_丙_构思.md'), 'w').write('# 丙\n无稿：执笔被平台安全之检拦\n')
        open(os.path.join(d, '_行家评.md'), 'w').write(评缺.split('\n', 1)[1])
        共 += 1; ok += (宽之(d) == 3 and 红丙())
        open(os.path.join(d, '起草_丙_构思.md'), 'w').write('进化账所避：某条\n满分之问：三路\n' + '构' * 420)
        # ⑥无「立得住」 → 红
        open(os.path.join(d, '_行家评.md'), 'w').write('【小说家】…\n【总编辑】…\n## 合稿逐条回话\n1. 改\n')
        共 += 1; r = 全(tmp); ok += (400 in r and any('立得住' in x for x in r[400]))
        # ⑥自章之前者不查
        d2 = os.path.join(tmp, '版本', '第376章'); os.makedirs(d2)
        open(os.path.join(d2, '_十一轮.json'), 'w').write('{}')
        共 += 1; ok += (376 not in 全(tmp))
        # ⑦★1118 写者（标无稿·造章.js N≥464 选之先跑自调）——稿号之逆钉真例：461 稿三＝乙、459 稿二＝丙／稿五＝甲、464 稿一＝乙、宽三之 464 稿二＝丙
        共 += 1; ok += ([号之席(461, 5, '稿三'), 号之席(459, 5, '稿二'), 号之席(459, 5, '稿五'), 号之席(464, 5, '稿一'), 号之席(464, 3, '稿二')]
                       == ['乙', '丙', '甲', '乙', '丙'])
        d7 = os.path.join(tmp, '版本', '第461章'); os.makedirs(d7)
        open(os.path.join(d7, '_十一轮.json'), 'w').write('{}')
        for 名 in '甲丙':
            open(os.path.join(d7, '起草_%s_构思.md' % 名), 'w').write('进化账所避：某条\n满分之问：三路\n' + '构' * 420)
        题 = '# 执笔·乙之构思（咬合路）\n'
        open(os.path.join(d7, '起草_乙_构思.md'), 'w').write(题)                       # 461 之真形：只一题行（38 字节）
        open(os.path.join(d7, '_行家评.md'), 'w').write(评 + '稿三：先跑印「缺档」，判致命\n')   # ★1118：蒙名读 5 稿＋其号之缺档行（无稿之免逐席验之）
        open(os.path.join(d7, '_创作记录.md'), 'w').write(''.join(k + '、x\n' for k in '一二三四五六'))
        open(os.path.join(tmp, '设定', '大师进化账.md'), 'a').write('- [第461章] 教训｜出处｜往后\n')
        for k in '一二四':
            open(os.path.join(d7, '起草_稿%s.md' % k), 'w').write('稿')
        乙构 = lambda: open(os.path.join(d7, '起草_乙_构思.md'), encoding='utf-8').read()
        红乙 = lambda: any('构思·乙' in x for x in 全(tmp).get(461, []))
        # ⑦之二 稿档在（稿三在盘）→ ⛔书、构思一字不动
        open(os.path.join(d7, '起草_稿三.md'), 'w').write('稿')
        共 += 1; ok += (标无稿(461, 5, '稿三', tmp)[1].startswith('⛔稿档在') and 乙构() == 题)
        os.remove(os.path.join(d7, '起草_稿三.md'))
        # ⑦之三 稿不足三（只二）→ ⛔书
        os.remove(os.path.join(d7, '起草_稿四.md'))
        共 += 1; ok += (标无稿(461, 5, '稿三', tmp)[1].startswith('⛔起草_稿 不足三') and 乙构() == 题)
        open(os.path.join(d7, '起草_稿四.md'), 'w').write('稿')
        # ⑦之四 四条俱合 → 书；而创作记录未载缺档者照红（写者⛔代缺档）；载之即绿；再跑⛔重书
        共 += 1; ok += (标无稿(461, 5, '稿三', tmp) == ('乙', '已书') and 红乙())
        open(os.path.join(d7, '_创作记录.md'), 'a').write('| 稿三 | 乙 | 咬合 | 构思档只一题行，稿缺档 |\n')
        共 += 1; ok += (not 红乙() and 标无稿(461, 5, '稿三', tmp)[1].startswith('已书（') and 乙构().count('无稿：') == 1)
        # ⑦之四之二★1118：所书之行因中立（执笔未交、盘上缺档、其因⛔断；⛔书「拦」）
        共 += 1; ok += ('无稿：执笔未交、盘上缺档（稿三 不在、起草_稿 3 份；其因⛔断；' in 乙构() and '拦' not in 乙构())
        # ⑦之五 构思已全者 → ⛔书（满者照内容查，⛔以标免之）；构思不在者 → 立档书之（造式 ② 之「在」亦合）
        open(os.path.join(d7, '起草_乙_构思.md'), 'w').write('进化账所避：某条\n满分之问：三路\n' + '构' * 420)
        共 += 1; ok += (标无稿(461, 5, '稿三', tmp)[1].startswith('⛔构思照查已全') and '无稿' not in 乙构())
        os.remove(os.path.join(d7, '起草_乙_构思.md'))
        共 += 1; ok += (红乙() and 标无稿(461, 5, '稿三', tmp) == ('乙', '已书') and 乙构().startswith('# 执笔·乙之构思') and not 红乙())
        # ⑦之六 稿号映於 丁（461 稿五＝丁·创作记录「稿五（丁·翻个儿）」）→ ⛔书（只 甲乙丙）
        共 += 1; ok += (号之席(461, 5, '稿五') == '丁' and 标无稿(461, 5, '稿五', tmp)[1].startswith('⛔非大师之关所查')
                       and not os.path.exists(os.path.join(d7, '起草_丁_构思.md')))
        # ⑧★1118 真书之回归（总编辑复核·大师之关→改）：459 丙、461 乙、463 甲（旧「…拦」之行）俱免——其号之稿档不在、创作记录与行家评俱载其缺档、稿 ≥3
        for n, 名 in ((459, '丙'), (461, '乙'), (463, '甲')):
            免 = []; 缺 = 查(n, ROOT, 免)
            共 += 1; ok += (免 == [名] and not any(x.startswith('构思·') for x in 缺))
        # ⑧之二 464 乙（稿一·零稿·其因不明）：未标则红；--标无稿 464 5 稿一 自验而书（因中立）即免；再跑⛔重书——於盘之副本（⛔动真书；既标者先去其行以复未标之形）
        真 = os.path.join(ROOT, '版本', '第464章')
        d8 = os.path.join(tmp, 'r464', '版本', '第464章'); os.makedirs(d8); os.makedirs(os.path.join(tmp, 'r464', '设定'))
        shutil.copy(os.path.join(ROOT, '设定', '大师进化账.md'), os.path.join(tmp, 'r464', '设定'))
        for x in os.listdir(真):
            if re.fullmatch(r'起草_._构思\.md|_行家评\.md|_创作记录\.md|_十一轮\.json', x):
                shutil.copy(os.path.join(真, x), d8)
            elif re.fullmatch(r'起草_稿.\.md', x):
                open(os.path.join(d8, x), 'w').write('稿')
        f8 = os.path.join(d8, '起草_乙_构思.md')
        open(f8, 'w', encoding='utf-8').write(''.join(L for L in open(os.path.join(真, '起草_乙_构思.md'), encoding='utf-8').read().splitlines(True)
                                                       if not re.match(r'无稿[：:]', L)))
        r8 = os.path.join(tmp, 'r464'); 免 = []
        共 += 1; ok += (宽之(d8) == 5 and 席之号(464, 5, '乙') == '稿一' and any(x.startswith('构思·乙 ') for x in 查(464, r8, 免)) and 免 == [])
        免 = []
        共 += 1; ok += (标无稿(464, 5, '稿一', r8) == ('乙', '已书') and not any(x.startswith('构思·') for x in 查(464, r8, 免)) and 免 == ['乙']
                       and open(f8, encoding='utf-8').read().endswith('\n无稿：执笔未交、盘上缺档（稿一 不在、起草_稿 4 份；其因⛔断；大师之关.py --标无稿 自书）\n')
                       and 标无稿(464, 5, '稿一', r8)[1].startswith('已书（'))
        # ⑨〔W919·X138〕二稿之录（临时之树·章 989·⛔真章号）：N≥489 有录 → 整稿之界 2（无稿之免、标无稿）；无录、488 有录 → 照 3
        d9 = os.path.join(tmp, '版本', '第989章'); os.makedirs(d9)
        号9 = 席之号(989, 5, '丙')
        open(os.path.join(d9, '_行家评.md'), 'w').write('造式二代：一位独立行家兼小说家、总编辑两眼，蒙名读 5 稿\n%s：先跑印「缺档」，判致命\n' % 号9)
        open(os.path.join(d9, '_创作记录.md'), 'w').write('| %s | 丙 | （缺档） |\n' % 号9)
        for k in [x for x in ('稿一', '稿二', '稿三', '稿四', '稿五') if x != 号9][:2]:
            open(os.path.join(d9, '起草_%s.md' % k), 'w').write('稿')
        t9 = '# 丙\n无稿：执笔未交、盘上缺档\n'
        无录9 = 无稿之免(d9, 989, '丙', t9)
        open(os.path.join(d9, '_席之因.json'), 'w').write(__import__('json').dumps({'章': 989, '二稿': {'由': '余席俱拒、整稿二'}}, ensure_ascii=False))
        有录9 = 无稿之免(d9, 989, '丙', t9)
        共 += 1; ok += (无录9 is None and 有录9 == 号9 and _整稿之界(989, tmp) == 2 and _整稿之界(488, tmp) == 3 and _整稿之界(990, tmp) == 3)
        # ⑨之二〔W924·501〕一稿之录（临时之树·章 987·⛔真章号）：整稿一——无录、只二稿之录 → 照查（无稿之免⛔、标无稿⛔书）；一稿之录 → 界 1（免、书）；487 有录 → 照 3
        d10 = os.path.join(tmp, '版本', '第987章'); os.makedirs(d10)
        号10 = 席之号(987, 5, '丙')
        open(os.path.join(d10, '_行家评.md'), 'w').write('造式二代：一位独立行家兼小说家、总编辑两眼，蒙名读 5 稿\n%s：先跑印「缺档」，判致命\n' % 号10)
        open(os.path.join(d10, '_创作记录.md'), 'w').write('| %s | 丙 | （缺档） |\n' % 号10)
        open(os.path.join(d10, '起草_%s.md' % [x for x in 稿号们[:5] if x != 号10][0]), 'w').write('稿')
        录10 = lambda k, 键: open(os.path.join(tmp, '版本', '第%d章' % k, '_席之因.json'), 'w').write(
            __import__('json').dumps({'章': k, 键: {'由': '五席俱拒、整稿一'}}, ensure_ascii=False))
        无录10 = (无稿之免(d10, 987, '丙', t9), 标无稿(987, 5, 号10, tmp)[1])
        录10(987, '二稿')
        二录10 = (无稿之免(d10, 987, '丙', t9), 标无稿(987, 5, 号10, tmp)[1], _整稿之界(987, tmp))
        录10(987, '一稿')
        有录10 = (无稿之免(d10, 987, '丙', t9), _整稿之界(987, tmp), 标无稿(987, 5, 号10, tmp))
        os.makedirs(os.path.join(tmp, '版本', '第487章')); 录10(487, '一稿')
        共 += 1; ok += (无录10[0] is None and 无录10[1].startswith('⛔起草_稿 不足三') and 二录10[0] is None and 二录10[1].startswith('⛔起草_稿 不足三')
                       and 二录10[2] == 2 and 有录10[0] == 号10 and 有录10[1] == 1 and 有录10[2] == ('丙', '已书') and _整稿之界(487, tmp) == 3
                       and '无稿：执笔未交、盘上缺档（%s 不在、起草_稿 1 份' % 号10 in open(os.path.join(d10, '起草_丙_构思.md'), encoding='utf-8').read())
    finally:
        shutil.rmtree(tmp)
    print('大师之关·自测 %d/%d' % (ok, 共))
    return ok == 共


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--自测':
        sys.exit(0 if 自测() else 1)
    if a and a[0] == '--标无稿':                 # ★1118 写者：造章.js 选之先跑自调（N≥467 以无稿之实；464—466 旧支）或主环手跑——只印稿号（蒙名）、恒返 0（⛔断选之先跑）
        for 号 in a[3].split(','):
            try:
                print('· 无稿之标·%s：%s' % (号, 标无稿(int(a[1]), int(a[2]), 号)[1]))
            except Exception as e:
                print('· 无稿之标·%s：⛔判不出（%s）' % (号, e))
        sys.exit(0)
    if a:
        免 = []
        缺 = 查(int(a[0]), ROOT, 免)
        免语 = ('｜免：%s（无稿）' % '、'.join(a[0] + x for x in 免)) if 免 else ''   # ★1118：免者必印（⛔无声）
        print((('⛔ 大师之关·第%s章：' % a[0] + '｜'.join(缺)) if 缺 else '✓ 大师之关·第%s章：五样俱全' % a[0]) + 免语)
        sys.exit(1 if 缺 else 0)
    免 = []
    红 = 全(ROOT, 免)
    免语 = ('｜免：%s（无稿）' % '、'.join('%d%s' % x for x in 免)) if 免 else ''   # ★1118：免者必印（⛔无声）
    if 红:
        for n, 缺 in 红.items():
            print('⛔ 大师之关·第%d章：%s' % (n, '｜'.join(缺)))
        if 免语:
            print('· 大师之关' + 免语)
        sys.exit(1)
    print('✓ 大师之关：自第%d章起已封诸章（%d 章），构思／行家评／创作记录／进化俱全' % (自章, len(已封诸章())) + 免语)
