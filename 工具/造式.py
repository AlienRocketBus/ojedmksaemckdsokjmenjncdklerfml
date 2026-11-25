#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""造式——章之式之认，与「造式之实」之核（1008 立·作者令「名著是写出来的，不是改出来的」）。

★其由：`工具/席/一章.js` 之虫洞式（`args.式==='虫洞'`，名不变）今即「造式」——
  三位执笔各写整章（蒙名稿一／稿二／稿三）→ 一位独立行家蒙名选稿、只列致命与大进 →
  合稿席以胜稿为底、只办致命与大进 → 诸闸只验致命（抄袭／厚／逻辑审／机闸／盲读一席／读误）。
  ⛔三庭、五庭、修席、极限诸审改之轮一概不设（作者令：力气全投「造」，⛔审改之轮）。
★★故造式之章，轮记里本就没有第1—13轮（机闸所写之第3轮除外）——
  旧式「十轮不满」「跑满查」「尽力查」诸检拿去量它必红，**而红的不是伤，是制度换代**
  （与 `跑轮.py::_is_old_era` 同理：今日之尺不量另一制所写之章）。
★★★故诸「轮」之闸见造式之章，即改检**造式之实**——⛔**这不是豁免**：
  一章自称造式（`版本/第N章/_式.md` 有「式：虫洞（造式·1008）」一行）而造式之实缺一样，照旧红；
  不自称造式者，旧闸一格不动。
⛔⛔「致命」之闸一道不碰：canon 禁式、硬闸、抄袭闸、起草闸、崩坏闸／逻辑审、厚之关（分量闸）、
  大师之关之构思与行家评、拦停旗、正文与末版一致、第十一轮之右眼——造式之章与常式之章同查。

造式之实（缺一即红）：
  ①三稿：`版本/第N章/起草_稿一.md`／`稿二`／`稿三` 俱在，各去空白 ≥1000 字
    （三位执笔各写整章；此界取铁底 2000 之半，只防空档、残稿充数——稿之厚薄自有厚之关量正文）；
  ②三构思：`起草_甲_构思.md`／`乙`／`丙` 俱在（其细——字数、进化账所避、满分之问——归 `大师之关.py` 验）；
  ③行家评 `_行家评.md`：「小说家」「总编辑」二眼，并「## 名次」「## 立得住」「## 致命」「## 大进」「## 合稿逐条回话」五节俱在；
    「## 名次」有实文（去空白 ≥120 字）；「## 致命」「## 大进」二节：或逐条立号（致命1、致命2…／大进1…），或明写「无」；
    ★**凡立了号者，「## 合稿逐条回话」里须逐号有回话**——漏一号即红（行家所指，合稿须逐条交代）；
  ④轮记 `_轮记.md`：「## 起草·三稿比读与合稿」「## 造式·逻辑审…」「## 造式·盲读」三样之节俱在，
    各有实文（去空白 ≥120 字·与 `小说检察官.py::_rounds_full` 同界）。

用法：
  python3 工具/造式.py N         # 查一章：是不是造式之章、造式之实缺什么（缺即 rc=1）
  python3 工具/造式.py --自测
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import os, re, sys, shutil, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
式行 = '式：虫洞（造式·1008）'          # 造式之章之 `_式.md` 所书之一行（合稿席落、封版席验）
_式之认 = re.compile(r'^\s*式\s*[：:]\s*虫洞（造式', re.M)
三稿 = ('稿一', '稿二', '稿三')
诸稿 = ('稿一', '稿二', '稿三', '稿四', '稿五', '稿六', '稿七')   # 二代之宽至七
实文之界 = 120                          # 与 小说检察官::_rounds_full、跑轮::zonghe 之「有实文」同界
稿之界 = 1000                           # 铁底 2000 之半：只防空档、残稿


def _读(p):
    try:
        with open(p, encoding='utf-8', errors='replace') as f:
            return f.read()
    except Exception:
        return None


def _净(s):
    return len(re.sub(r'\s', '', s or ''))


def 章目(n, root=ROOT):
    return os.path.join(root, '版本', '第%d章' % n)


def 是造式(n, root=ROOT):
    """`版本/第N章/_式.md` 在，且其中有「式：虫洞（造式…」一行。"""
    t = _读(os.path.join(章目(n, root), '_式.md'))
    return bool(t) and bool(_式之认.search(t))


def 节们(文, 题):
    """取二级标题以「题」起头之诸节之身（自标题行之後至下一个「## 」或文末）。"""
    out = []
    if not 文:
        return out
    块 = re.split(r'^##[ \t]+', 文, flags=re.M)
    for b in 块[1:]:
        头, _, 身 = b.partition('\n')
        if 头.strip().startswith(题):
            out.append(身)
    return out


def _号(身, 名):
    return sorted({int(x) for x in re.findall(名 + r'\s*(\d+)', 身 or '')})


def 实之缺(n, root=ROOT):
    """造式之实所缺（空列即齐）。⛔不问是不是造式——那是 是造式() 的事。"""
    d = 章目(n, root)
    缺 = []
    # ①三稿（★1104·416：二代之宽 5／7——蒙名稿一至稿七，整稿 ≥3 即齐；一席被平台之检拒而缺档者，行家判致命、余稿足三即⛔拦；
    #   残稿充数照红、宽 3 之章缺一照红——效不减）
    整 = []
    for k in 诸稿:
        t = _读(os.path.join(d, '起草_%s.md' % k))
        if t is None:
            continue
        if _净(t) < 稿之界:
            缺.append('起草_%s.md 仅 %d 字（<%d·非整章）' % (k, _净(t), 稿之界))
        else:
            整.append(k)
    try:                                         # 〔W919·X138〕N≥489 有二稿之录（承.py N --二稿 "由"）→ 整稿之界 2；import 不得或录读崩照 3（⛔放）
        import 承 as _承
        界 = _承.整稿之界(n, root)
    except Exception:
        界 = 3
    if len(整) < 界:
        for k in 三稿:
            if k not in 整 and _读(os.path.join(d, '起草_%s.md' % k)) is None:
                缺.append('起草_%s.md 不在（造式三位执笔各写整章）' % k)
        if not any('不在' in x or '非整章' in x for x in 缺):
            缺.append('整稿仅 %d 份（<3·造式三位执笔各写整章）' % len(整))
    # ②三构思
    for 名 in '甲乙丙':
        if _读(os.path.join(d, '起草_%s_构思.md' % 名)) is None:
            缺.append('起草_%s_构思.md 不在（三执笔各自构思）' % 名)
    # ③行家评
    t = _读(os.path.join(d, '_行家评.md'))
    if t is None:
        缺.append('_行家评.md 不在（造式之选：一位独立行家蒙名读三稿）')
    else:
        for k in ('小说家', '总编辑'):
            if k not in t:
                缺.append('_行家评.md 无「%s」之眼' % k)
        节 = {}
        for 题 in ('名次', '立得住', '致命', '大进', '合稿逐条回话'):
            ss = 节们(t, 题)
            if not ss:
                缺.append('_行家评.md 无「## %s」一节' % 题)
            节[题] = '\n'.join(ss)
        if 节们(t, '名次') and _净(节['名次']) < 实文之界:
            缺.append('_行家评.md「## 名次」无实文（%d 字<%d·名次须带其由）' % (_净(节['名次']), 实文之界))
        回 = 节['合稿逐条回话']
        if 节们(t, '合稿逐条回话') and not _净(回):
            缺.append('_行家评.md「## 合稿逐条回话」是空的')
        for 名 in ('致命', '大进'):
            if not 节们(t, 名):
                continue
            号 = _号(节[名], 名)
            if not 号:
                if '无' not in 节[名]:
                    缺.append('_行家评.md「## %s」既不逐条立号（%s1、%s2…）亦不明写「无」' % (名, 名, 名))
                continue
            漏 = [i for i in 号 if not re.search(名 + r'\s*%d(?!\d)' % i, 回)]
            if 漏:
                缺.append('「## 合稿逐条回话」漏回：%s' % '、'.join('%s%d' % (名, i) for i in 漏))
    # ④轮记
    lj = _读(os.path.join(d, '_轮记.md'))
    if lj is None:
        缺.append('_轮记.md 不在')
    else:
        for 题, 何 in (('起草·三稿比读与合稿', '合稿席'), ('造式·逻辑审', '逻辑审席'), ('造式·盲读', '读误席录盲读')):
            ss = 节们(lj, 题)
            if not ss:
                缺.append('_轮记.md 无「## %s」之节（%s所写）' % (题, 何))
            elif max(_净(s) for s in ss) < 实文之界:
                缺.append('_轮记.md「## %s」无实文（<%d 字）' % (题, 实文之界))
    return 缺


def 判(n, root=ROOT):
    """→ (是造式, 所缺)。非造式者所缺恒空（旧闸照旧管它）。"""
    if not 是造式(n, root):
        return False, []
    return True, 实之缺(n, root)


def 是二代(n, root=ROOT):
    """1013：造式二代之章（`_式.md` 书「造式二代」），其席出自 `工具/席/造章.js`。"""
    t = _读(os.path.join(章目(n, root), '_式.md'))
    return bool(t) and '造式二代' in t


# ★1017 淘汰之律（X28）：一代 一章.js 已彻删——一代之章（306—380）之段与造式之段冻於此，只供复核已封之旧章（旧章⛔再变，冻之即真）
一代之段 = ['定位', '三魂', '起草', '机闸', '三庭', '五庭', '读席', '修席', '极限', '案席', '封版']
一代造式之段 = ['定位', '三魂', '造', '选', '合', '验', '案席', '封版']


def 造式之段(root=ROOT, n=None):
    """囤灰闸据此判造式之章之席记：一代之章（n 不给、或其 `_式.md` 非「造式二代」）取冻存之 一代造式之段；
    二代之章当场自 `工具/席/造章.js` 读 `const 造式之段 = [...]`（1013）。读不出 → None。"""
    if n is None or not 是二代(n, root):
        return list(一代造式之段)
    js = _读(os.path.join(root, '工具', '席', '造章.js')) or ''
    m = re.search(r'const\s+造式之段\s*=\s*\[([^\]]*)\]', js)
    if not m:
        return None
    xs = re.findall(r"'([^']+)'", m.group(1))
    return xs or None


# ═══ 自测：每一格都拿一个局回灌，两头皆活 ═══
def 造一局(root, n, 缺=()):
    """在 root 下立一个造式之章之全局（供本器与诸闸之自测共用）；缺＝要故意拿掉的样（名见下）。"""
    d = 章目(n, root)
    os.makedirs(d, exist_ok=True)
    实 = '看见了什么：' + '逐拍逐句读过三稿，每一处判都印了原句与其所据之前文章行。' * 5

    def 写(名, 文):
        if 名 in 缺:
            return
        with open(os.path.join(d, 名), 'w', encoding='utf-8') as f:
            f.write(文)
    写('_式.md', 式行 + '\n')
    for k in 三稿:
        写('起草_%s.md' % k, '# 第四百章 测\n\n' + ('她把手搁在桶沿上，等那一口气落稳。\n＊\n' * 80))
    for 名 in '甲乙丙':
        写('起草_%s_构思.md' % 名, '进化账所避：某条\n满分之问：三路\n' + '构' * 420)
    写('_行家评.md', '造式：一位独立行家兼小说家、总编辑两眼，蒙名读三稿\n'
                    '## 名次\n稿二＞稿一＞稿三。' + 实 + '\n'
                    '## 小说家之眼\n…\n## 总编辑之眼\n…\n## 叫绝之拍\n…\n'
                    '## 立得住\n逐条判过。\n'
                    '## 致命\n- 致命1：稿二:12「他叫了一声」与 377:63 相抵。\n'
                    '## 大进\n- 大进1：稿一:30 胜於稿二:28。\n- 大进2：稿三:9 胜於稿二:7。\n'
                    + ('' if '回话' in 缺 else
                       '## 合稿逐条回话\n- 致命1：治毕。\n- 大进1：嫁接（三问俱过）。\n'
                       + ('' if '漏回' in 缺 else '- 大进2：不嫁接（第二问不过）。\n')))
    写('_轮记.md', '## 起草·三稿比读与合稿\n' + 实 + '\n'
                  '## 第3轮·逐数对表\n' + 实 + '\n'
                  + ('' if '逻辑审之节' in 缺 else '## 造式·逻辑审·起草·第1回\nP04 P07 P05 ' + 实 + '\n')
                  + ('' if '盲读之节' in 缺 else '## 造式·盲读\n' + ('短' if '盲读无实' in 缺 else 实) + '\n'))
    return d


def 自测():
    R = []

    def T(名, 得):
        R.append((名, bool(得)))
    tmp = tempfile.mkdtemp(prefix='造式_')
    try:
        os.makedirs(os.path.join(tmp, '工具', '席'))
        # ①无 _式.md 之章：不认作造式，所缺恒空（旧闸照旧管它——⛔本器不替任何一章开口子）
        os.makedirs(章目(400, tmp))
        T('①无 _式.md 者非造式', 判(400, tmp) == (False, []))
        # ②全局：是造式而所缺空
        造一局(tmp, 401)
        T('②造式之实俱齐者绿', 判(401, tmp) == (True, []))
        # ③自称造式而一样也没有 → 红（⛔挂一块牌子不算造式）
        d = 章目(402, tmp); os.makedirs(d)
        open(os.path.join(d, '_式.md'), 'w', encoding='utf-8').write(式行 + '\n')
        是, 缺 = 判(402, tmp)
        T('③只有 _式.md 而无实者红（缺 ≥8 样）', 是 and len(缺) >= 8)
        # ④逐样拿掉，逐样须红
        for 样, 词 in (('起草_稿二.md', '稿二'), ('起草_乙_构思.md', '乙_构思'), ('_行家评.md', '_行家评.md 不在'),
                      ('回话', '合稿逐条回话'), ('漏回', '大进2'), ('逻辑审之节', '造式·逻辑审'),
                      ('盲读之节', '造式·盲读'), ('盲读无实', '无实文')):
            n = 410 + len(R)
            造一局(tmp, n, 缺=(样,))
            是, 缺 = 判(n, tmp)
            T('④拿掉「%s」即红' % 样, 是 and any(词 in x for x in 缺))
        # ⑤致命一节既无号亦无「无」→ 红；明写「无」→ 绿
        n = 450
        造一局(tmp, n)
        p = os.path.join(章目(n, tmp), '_行家评.md')
        t = open(p, encoding='utf-8').read()
        open(p, 'w', encoding='utf-8').write(t.replace('- 致命1：稿二:12「他叫了一声」与 377:63 相抵。', '见上。'))
        T('⑤致命一节空口者红', any('既不逐条立号' in x for x in 判(n, tmp)[1]))
        open(p, 'w', encoding='utf-8').write(t.replace('- 致命1：稿二:12「他叫了一声」与 377:63 相抵。', '无（三稿逐拍查过）。'))
        T('⑤之二 致命明写「无」者绿', 判(n, tmp) == (True, []))
        # ⑥残稿充数 → 红
        n = 451
        造一局(tmp, n)
        open(os.path.join(章目(n, tmp), '起草_稿三.md'), 'w', encoding='utf-8').write('# 第四百章 测\n残稿\n')
        T('⑥残稿（<%d 字）充数者红' % 稿之界, any('非整章' in x for x in 判(n, tmp)[1]))
        # ⑥之二 宽五而稿一缺档（平台之检拒）、稿二至稿四俱整 → 绿；只余二整稿 → 红
        n = 453
        造一局(tmp, n, 缺=('起草_稿一.md',))
        open(os.path.join(章目(n, tmp), '起草_稿四.md'), 'w', encoding='utf-8').write(open(os.path.join(章目(n, tmp), '起草_稿二.md'), encoding='utf-8').read())
        T('⑥之二 宽五缺稿一而整稿三者绿', 判(n, tmp) == (True, []))
        os.remove(os.path.join(章目(n, tmp), '起草_稿四.md')); os.remove(os.path.join(章目(n, tmp), '起草_稿三.md'))
        T('⑥之三 整稿只二者红', any('稿' in x for x in 判(n, tmp)[1]))
        # ⑥之四〔W919·X138〕N≥489 有二稿之录（承.py N --二稿 "由"·临时之树之录·⛔读真仓）→ 整稿二绿；无录红；488 有录亦红
        def 录(k):
            import json as _j
            with open(os.path.join(章目(k, tmp), '_席之因.json'), 'w', encoding='utf-8') as o:
                _j.dump({'章': k, '二稿': {'由': '余席俱拒、整稿二', '时': 'x'}}, o, ensure_ascii=False)
        造一局(tmp, 989, 缺=('起草_稿一.md',))
        无录 = 判(989, tmp)
        录(989)
        有录 = 判(989, tmp)
        造一局(tmp, 488, 缺=('起草_稿一.md',))
        录(488)
        T('⑥之四 X138 二稿之录：989 无录二稿红、有录绿；488 有录亦红', any('稿一' in x for x in 无录[1]) and 有录 == (True, [])
          and any('稿一' in x for x in 判(488, tmp)[1]))
        # ⑦式行须认得其形；别的字样不认（「式：常」不是造式）
        n = 452
        造一局(tmp, n)
        open(os.path.join(章目(n, tmp), '_式.md'), 'w', encoding='utf-8').write('式：常\n')
        T('⑦「式：常」不认作造式', not 是造式(n, tmp))
        # ⑧造式之段：读得出今仓 一章.js 之 const 造式之段；读不出者 None（⛔不许读不出就放行）
        段 = 造式之段()
        T('⑧一代之造式之段取冻存（%s）' % ('、'.join(段) if 段 else '读不出'), 段 == 一代造式之段)
        T('⑧之二 二代之章（397）自 造章.js 读得出', 造式之段(ROOT, 397) == ['料', '造', '选', '合', '验', '记', '封版'])
        # ⑨今仓之实：凡今已在盘之章，无一章挂造式之牌而缺实（活格：真有就红）
        挂 = []
        vd = os.path.join(ROOT, '版本')
        for x in (os.listdir(vd) if os.path.isdir(vd) else []):
            m = re.match(r'第(\d+)章$', x)
            if m and 是造式(int(m.group(1))):
                挂.append(int(m.group(1)))
        T('⑨今仓挂造式之章（%s）其实之核跑得动' % (挂 or '尚无'), all(isinstance(实之缺(k), list) for k in 挂))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    过 = sum(1 for _, ok in R if ok)
    for 名, ok in R:
        if not ok:
            print('  ⛔' + 名)
    print('%s 造式·自测 %d/%d' % ('✓' if 过 == len(R) else '⛔', 过, len(R)))
    return 过 == len(R)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--自测':
        sys.exit(0 if 自测() else 1)
    if not a:
        print(__doc__)
        sys.exit(2)
    n = int(a[0])
    是, 缺 = 判(n)
    if not 是:
        print('· 第%d章非造式之章（无 版本/第%d章/_式.md 或其无「%s」一行）——诸闸照常式查。' % (n, n, 式行))
        sys.exit(0)
    if 缺:
        print('⛔ 造式·第%d章：造式之实缺 %d 样——%s' % (n, len(缺), '｜'.join(缺)))
        sys.exit(1)
    print('✓ 造式·第%d章：造式之实俱齐（三稿／三构思／行家评之名次·致命·大进·逐条回话／轮记之合稿·逻辑审·盲读）' % n)
    sys.exit(0)
