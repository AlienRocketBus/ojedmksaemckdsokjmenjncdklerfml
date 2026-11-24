#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""账并（1119 立·执行之制 治6·坑63）——两写者之账之 git merge driver：章-N 之封版（写书之坐）与总编辑之治俱追加於同账，
GitHub 之并（gate.yml 备候 `git merge`）一冲突即「败·因 merge」——章-472 入主迟 56 分、章-473 总编辑手并（81e49e8c1）。

其法（零 token）：
  ①先照常三方并（git merge-file）——净即成；唯 json 之账须其果与②之键级之并 M 语义同方成：行之并「净」而值错置者实有
    （形近之元，diff 之对齐把一侧之改移於邻元——自测⑤之二：y 之 美元 应 9 而得 1、a1 得 9），不合即走②。
    键级之「不可」分二类（复核 1119）：语义之冲突（一删一改、两侧同增一键而异、同字两改而异、键字两改而两版俱留、
    法用册同 id 两处、费账一元两侧各改其量之字）→ 推翻内建之净并、留全档之冲突（⛔静默改值）；
    结构之不判（基或一侧有重键／缺键之元、元内无键之 list 两侧俱改而序列之并亦冲突）→ 照内建之净并成之、印 ⚠（同旧·⛔比今更坏）。
    元内无键之 list（坑.守、件.产出 等）两侧俱改：以元为行（json 一行一元）做序列三方并，净即取。其底不可析者照内建成之、印 ⚠。
  ②有冲突则按档之类（下表·逐档定之）：
    json ：以 O／A／B 析得之「键级三方并」M 为准——两侧所增之键俱在且各一、一侧所删者去、一侧所改者取其改；
           list 之元两侧俱改者入元内以字为键再并（dict 以其键）；两侧改同键（同字）而异、一删一改、两侧同增一键而异 → 不可自并；
           同一 list（或 dict）中有键两侧俱删而两侧又各增他键（即键字两改而异：两版俱留之漏）→ 不可。
           先取 `git merge-file --union` 之果：须 json 可析、无重键、且与 M 语义同（键集与值同）方成；
           不合则以其档之写器出 M：dump1＝json.dump(indent=1, ensure_ascii=False)（费审.记、工作流账、方法坑账.写、改单、总编辑复核
           之写式；O／A／B 三份俱逐字为此式方用）；拼＝原文键拼（每一元之文逐字取自 A 或 B、元间之隔取 A 之原隔——⛔生一值；
           法用册係手书之册，法用之守亦以原文拼写其纸证）。写毕再析，须与 M 逐值同（序亦同）。
    md表 ：冲突之块内以行为元（表行以首格为键、他行以全行为键；块内键重即不可），键级三方并同上（键两侧俱删而两侧各增 → 不可：
           非表行两改、表行首格两改、题行两改俱属此）；毕验「行集」：果之行集＝（A∪B）−（任一侧所删之行），且无一行多於其在 A、B 之数。
  ③余俱败（档不在册、输入非 UTF-8 或不可析、验不合）：退回旧行为——留冲突之标（git merge-file 之果）、rc 1。
    器崩（未捕之异常）或 git merge-file 坏：复 %A 之原文、再以 git merge-file 写冲突之标（再不成则以本器写全档之冲突），rc 1——
    ⛔「%A 原样而 git 记冲突」（手并者照常 git add 即静默丢 theirs）。
  每自并一回印一行於 stderr（GitHub 之 log 可见）。⛔静默改值、⛔丢一行：凡验不合即败。

键之认（逐档定之）：
  设定/费账.json          json  行←键（元内以字并只许「名」：美元、全量、时等量之字须整元同改）   写 dump1（费审.记）→ 拼
  设定/法用册.json        json  法←id 待←id 废←id 缓←id 机证不能←据（并後 id 於 法／待／废／缓 间唯一）   写 拼（手书之册）
  设定/工作流账.json      json  件←id                                   写 dump1（工作流账.py）→ 拼
  设定/方法坑账.json      json  坑←号                                   写 dump1（方法坑账.写）→ 拼
  设定/改单账.json        json  单←号                                   写 dump1（改单.py）→ 拼
  设定/总编辑复核账.json  json  裁←规＋时                               写 dump1（总编辑复核.py）→ 拼
  设定/方法账.md          md表  （两写者俱有改旧行之提交：8521b402f 封版#458、575371a19 封版#467、d45ae4107 等——⛔内建 union）
  设定/成章之法.md        md表  （〔W920 环4〕§二 之行以首格〔章号〕为键：章-N 之封版插 N 行（复盘.py 器出）与总编辑改 N-1 行相邻·坑63；写者唯一另书其册§五）
                                 序：并毕（净并或自并）§二 相邻之章行按首格之数稳排（〔W920 治〕主插 485、治插 484 → 483、485、484 之乱⛔留）
  dict 以其键并（递归）；上表所列之 list 以其字为键（元两侧俱改方入元内以字并）；余之 list 两侧俱改者以元为行做序列三方并。
生成之图（W912 环2①·坑63 之由即去）：设定/体系总图.md 係器之所生（封版 --後 与总编辑之 --随治 两写者俱重画·⛔手改）——%P 合者
  ⛔并其行（机算之果，逐行三方并即生两版相杂之假图）：取 %A（ours）原样、rc 0、stderr 印「生成之图·取 ours（⚠ 待下回重生）」；
  其旧由 --验 报「档旧」、下一封版或 --随治 重生（推.py 图之闸 拦总编辑之坐之旧图）。

用法：
  python3 工具/账并.py %O %A %B %P [%L]   # git 调之（.gitattributes：<档> merge=账并）
  python3 工具/账并.py --装 [仓]           # git config --local merge.账并.driver（只此一键·幂等·写毕重读，不合即 rc 1）——推.py 每推之前、gate.yml 备候 git merge 之前
  python3 工具/账并.py --卸 [仓]           # git config --local --remove-section merge.账并（回）
  python3 工具/账并.py --自测              # 负测（全测之格「负测·账并」）：合成之例＋章-472／473 真冲突之片段（工具/_负测料/账并/）
driver 未设（merge.账并 之段全无）时 git 退回内建之三方并——与无 .gitattributes 同（自测⑲实证）。
  ⛔半装：只有 merge.账并.name 而无 driver 则 git merge 直 fatal（lacks command line）——故 --装 只设 driver 一键、遇旧之 name 即去之（自测㉚）；写不成即 rc 1（㉛）。
driver 设而本器不在其树、或 PATH 无 python3 者退回 git merge-file（留冲突之标·自测⑳、㉝）；器崩即复 %A 留冲突之标（㉞㉟）。
回：git config --remove-section merge.账并（即 --卸）；或删 .gitattributes 之行。⛔只 --unset driver（若有 name 即成半装之态）。
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import os, sys, re, json, subprocess, tempfile, shutil
from collections import Counter
from json.decoder import scanstring

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
名 = '账并'
# python3 不在（sh 之 exec 败即退 127、|| 之退路不跑）→ 先 command -v；本器不在其树（旧之检出）→ 退回 git merge-file 留冲突之标
DRIVER = ('command -v python3 >/dev/null 2>&1 && [ -f 工具/账并.py ] && exec python3 工具/账并.py %O %A %B %P %L'
          ' || exec git merge-file -L ours -L base -L theirs --marker-size=%L %A %O %B')
料目 = os.path.join(ROOT, '工具', '_负测料', '账并')

# 键：顶层 list 之元键；白：顶层 list 之元两侧俱改时许以字并之字（余字两侧俱改即须整元同改·⛔拼出不相应之量）；
# 唯一：并後之不变式（诸 list 间某字唯一——两侧各移一元於异处即两处俱在）
册 = {
    '设定/费账.json': {'类': 'json', '键': {'行': ('键',)}, '白': {'行': {'名'}}, '写': ('dump1', '拼')},
    '设定/法用册.json': {'类': 'json', '键': {'法': ('id',), '待': ('id',), '废': ('id',), '缓': ('id',), '机证不能': ('据',)},
                     '唯一': ((('法', 'id'), ('待', 'id'), ('废', 'id'), ('缓', 'id')),), '写': ('拼',)},
    '设定/工作流账.json': {'类': 'json', '键': {'件': ('id',)}, '写': ('dump1', '拼')},
    '设定/方法坑账.json': {'类': 'json', '键': {'坑': ('号',)}, '写': ('dump1', '拼')},
    '设定/改单账.json': {'类': 'json', '键': {'单': ('号',)}, '写': ('dump1', '拼')},
    '设定/总编辑复核账.json': {'类': 'json', '键': {'裁': ('规', '时')}, '写': ('dump1', '拼')},
    '设定/方法账.md': {'类': 'md表'},
    '设定/成章之法.md': {'类': 'md表', '序': '## 二、'},      # 〔W920 环4〕§二 每章一行：章-N 之提交插 N 行、总编辑之治改他行——邻行两侧俱改即内建冲突（坑63）；
                                                            # 〔W920 治〕序：并毕 §二 相邻之章行按首格之数稳排（只换序·行集之验不变）
}


# 〔W912 环2①〕生成之图：两侧俱器之所生——取 ours 原样（⚠ 待下回重生），⛔逐行并（见 docstring「生成之图」）
生成之图 = ('设定/体系总图.md',)


class 不可(Exception):
    """不可自并之由（→ 留冲突、rc 1）。行之并净时：语义之冲突 → 推翻内建、留全档之冲突。"""


class 结构不可(不可):
    """键级不判（结构：重键、缺键、元内无键之 list 两侧俱改而序列之并亦冲突、键两侧俱删而各增）——
    行之并有冲突则同 不可（留冲突·同内建）；行之并净则照内建成之、印 ⚠（同旧·⛔推翻内建之净并：比今更坏）。"""


缺 = object()


def _串(v):
    return json.dumps(v, ensure_ascii=False)


def 同(x, y):
    """逐值且逐序同（true≠1、1.0≠1；dict 之序亦计）。"""
    return _串(x) == _串(y)


def _无重键(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            raise 不可('对象重键「%s」' % k)
        d[k] = v
    return d


def 析值(t):
    """json → 值（对象重键即不可：union 之果常重一键而 json.loads 默取其末——⛔静默改值）。"""
    try:
        return json.loads(t, object_pairs_hook=_无重键)
    except 不可:
        raise
    except Exception as e:
        raise 不可('json 不可析：%s' % str(e)[:60])


# ───────────── 原文之节（拼之所据：每一值、每一员在原文之起讫） ─────────────
class 节:
    __slots__ = ('类', '始', '终', '员')

    def __init__(s, 类, 始):
        s.类, s.始, s.终, s.员 = 类, 始, None, []


_空白 = re.compile(r'[ \t\n\r]*')
_数 = re.compile(r'-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][-+]?\d+)?')


def 析节(t):
    """→ 根之节。对象之员：(键, 键之起, 值之节)；数组之员：值之节。"""
    def 值(i):
        i = _空白.match(t, i).end()
        c = t[i:i + 1]
        if c in ('{', '['):
            n = 节('o' if c == '{' else 'a', i)
            闭 = '}' if c == '{' else ']'
            j = _空白.match(t, i + 1).end()
            if t[j:j + 1] == 闭:
                n.终 = j + 1
                return n
            while True:
                if n.类 == 'o':
                    if t[j:j + 1] != '"':
                        raise 不可('原文不可析（%d）' % j)
                    k, j2 = scanstring(t, j + 1)
                    j2 = _空白.match(t, j2).end()
                    if t[j2:j2 + 1] != ':':
                        raise 不可('原文不可析（%d）' % j2)
                    v = 值(j2 + 1)
                    n.员.append((k, j, v))
                else:
                    v = 值(j)
                    n.员.append(v)
                j = _空白.match(t, v.终).end()
                if t[j:j + 1] == ',':
                    j = _空白.match(t, j + 1).end()
                    continue
                if t[j:j + 1] == 闭:
                    n.终 = j + 1
                    return n
                raise 不可('原文不可析（%d）' % j)
        n = 节('v', i)
        if c == '"':
            _, n.终 = scanstring(t, i + 1)
        else:
            m = _数.match(t, i)
            if m and m.end() > i:
                n.终 = m.end()
            else:
                for w in ('true', 'false', 'null'):
                    if t.startswith(w, i):
                        n.终 = i + len(w)
                        break
                else:
                    raise 不可('原文不可析（%d）' % i)
        return n
    try:
        r = 值(0)
    except 不可:
        raise
    except Exception as e:
        raise 不可('原文不可析：%s' % str(e)[:60])
    if t[_空白.match(t, r.终).end():]:
        raise 不可('原文之末有余')
    return r


# ───────────── 键级三方并 ─────────────
def _元键(x, 字, 径):
    if not isinstance(x, dict) or any(f not in x for f in 字):
        raise 结构不可('%s 之元无键（%s）' % ('/'.join(径), '＋'.join(字)))
    return tuple(_串(x[f]) for f in 字)


def _键名(k):
    return '＋'.join(json.loads(z) if z.startswith('"') else z for z in k) if isinstance(k, tuple) else str(k)


def _键表(lst, 字, 径):
    d = {}
    for x in lst:
        k = _元键(x, 字, 径)
        if k in d:
            raise 结构不可('%s 之键重：%s' % ('/'.join(径), _键名(k)))
        d[k] = x
    return d


def _两删各增(O, A, B, 径名):
    """O 中有键两侧俱删、而两侧又各增他键 → 不可（键字两改而异：两版俱留、原键去——行集之验管不到，因两版俱在 A∪B）。
    行之并净时属结构（同元之二字两侧各改而不相邻，内建之并对）——照内建；有冲突则留冲突（同内建）。"""
    两删 = [k for k in O if k not in A and k not in B]
    if 两删 and any(k not in O for k in A) and any(k not in O for k in B):
        raise 结构不可('%s：键两侧俱删而两侧各增他键（键字两改而异：两版俱留）：%s' % (径名, _键名(两删[0])[:40]))


def _改字(o, x):
    return {f for f in set(o) | set(x) if (f in o) != (f in x) or (f in o and not 同(o[f], x[f]))}


def _序并(o, a, b, 径名):
    """元内无键之 list 两侧俱改：以元为行（json 一行一元·⛔splitlines：U+2028 等）做序列三方并，净即取；冲突 → 结构不可。"""
    def 行(L):
        return ''.join(_串(x) + '\n' for x in L)
    t, rc = 并文(行(a), 行(o), 行(b))
    if rc != 0:
        raise 结构不可('%s：元内无键之 list 两侧俱改、序列之并亦冲突' % 径名)
    return [json.loads(l) for l in t.split('\n') if l]


def 序(o键, a键, b键, 留):
    """果之序：A 之序为本；B 所增者插於其在 B 之前驱（已在果中者）之後、并越过紧随之 A 所增者（先 ours 後 theirs·同 union 与手并之式）。"""
    果 = [k for k in a键 if k in 留]
    在 = set(果)
    o集, b集 = set(o键), set(b键)
    a增 = set(a键) - o集 - b集
    for i, k in enumerate(b键):
        if k in 在 or k not in 留:
            continue
        位 = 0
        for j in range(i - 1, -1, -1):
            if b键[j] in 在:
                位 = 果.index(b键[j]) + 1
                break
        while 位 < len(果) and 果[位] in a增:
            位 += 1
        果.insert(位, k)
        在.add(k)
    return 果


def 三并(o, a, b, 规, 径=(), 计=None, 白=None):
    """→ 并之值；不可即抛 不可（结构之不判抛 结构不可）。规：{员名: (键之字…)}（只顶层之 list）。
    白：{员名: {字…}}（顶层 list 之元两侧俱改时许以字并之字）。计：Counter（增删改之数·印用）。"""
    if 同(a, b):
        return a
    if o is not 缺 and 同(a, o):
        return b
    if o is not 缺 and 同(b, o):
        return a
    径名 = '/'.join(径) or '（根）'
    if isinstance(a, dict) and isinstance(b, dict):
        if not isinstance(o, dict):
            raise 不可('%s：两侧俱增而异' % 径名)
        return _并对(o, a, b, 规, 径, 计, 白)
    if isinstance(a, list) and isinstance(b, list) and isinstance(o, list):
        字 = 规.get(径[0]) if len(径) == 1 else None
        if 字:
            return _并列(o, a, b, 字, 径, 计, 规, 白)
        r = _序并(o, a, b, 径名)
        计 is not None and 计.update(['序并'])
        return r
    raise 不可('%s：两侧改同值而异' % 径名)


def 键并(oV, aV, bV, c, 计=None):
    """册之一档之键级三方并＋并後之不变式（唯一）。"""
    m = 三并(oV, aV, bV, c.get('键') or {}, (), 计, c.get('白'))
    for 组 in c.get('唯一', ()):
        def 重(v):
            n = Counter()
            if isinstance(v, dict):
                for L, f in 组:
                    for x in (v.get(L) if isinstance(v.get(L), list) else []):
                        if isinstance(x, dict) and f in x:
                            n[_串(x[f])] += 1
            return {k for k, z in n.items() if z > 1}
        新 = 重(m) - 重(oV) - 重(aV) - 重(bV)
        if 新:
            raise 不可('%s 间同%s两见：%s（两侧各移之於异处）' % ('／'.join(L for L, _ in 组), 组[0][1], '、'.join(sorted(json.loads(x) if x.startswith('"') else x for x in 新))[:60]))
    return m


def _并对(o, a, b, 规, 径, 计, 白=None):
    留, 值, 结 = set(), {}, []
    for k in list(dict.fromkeys(list(a) + list(b))):
        if k in a and k in b:
            try:
                值[k] = 三并(o.get(k, 缺), a[k], b[k], 规, 径 + (k,), 计, 白)
            except 结构不可 as e:   # 结构之不判後於语义之冲突（同层之一删一改等先判·行之并净时语义者推翻内建）
                结.append(e); 值[k] = a[k]
            留.add(k)
        elif k in a:
            if k not in o:
                值[k] = a[k]; 留.add(k)
            elif not 同(a[k], o[k]):
                raise 不可('%s：一删一改' % '/'.join(径 + (k,)))
        else:
            if k not in o:
                值[k] = b[k]; 留.add(k)
            elif not 同(b[k], o[k]):
                raise 不可('%s：一删一改' % '/'.join(径 + (k,)))
    if 结:
        raise 结[0]
    _两删各增(o, a, b, '/'.join(径) or '（根）')
    return {k: 值[k] for k in 序(list(o), list(a), list(b), 留)}


def _并列(o, a, b, 字, 径, 计, 规=None, 白=None):
    O, A, B = _键表(o, 字, 径), _键表(a, 字, 径), _键表(b, 字, 径)
    径名 = '/'.join(径)
    白字 = (白 or {}).get(径[0]) if len(径) == 1 else None
    留, 值, 结 = set(), {}, []
    for k in list(dict.fromkeys(list(A) + list(B))):
        if k in A and k in B:
            if 同(A[k], B[k]):
                值[k] = A[k]
                if k not in O:
                    计 is not None and 计.update(['两增同'])
            elif k in O and 同(A[k], O[k]):
                值[k] = B[k]; 计 is not None and 计.update(['B改'])
            elif k in O and 同(B[k], O[k]):
                值[k] = A[k]; 计 is not None and 计.update(['A改'])
            elif k in O and isinstance(O[k], dict) and isinstance(A[k], dict) and isinstance(B[k], dict):
                # 两侧俱改此元：入元内以字为键再三方并（dict 以其键）——两侧改同字而异方不可
                try:
                    值[k] = 三并(O[k], A[k], B[k], 规 or {}, 径 + ('〔%s〕' % _键名(k),), 计, 白)
                    计 is not None and 计.update(['两改合'])
                except 结构不可 as e:
                    结.append(e); 值[k] = A[k]
                if 白字 is not None:   # 同字两改而异者上已判；此判异字：量之字（美元、全量、时…）两侧各改，按字拼即出不相应之值（⛔静默改值）
                    fa, fb = _改字(O[k], A[k]) - 白字, _改字(O[k], B[k]) - 白字
                    if fa and fb:
                        raise 不可('%s：两侧俱改一元之量之字而异处（%s；A：%s；B：%s）——须整元同改'
                                 % (径名, _键名(k), '、'.join(sorted(fa))[:30], '、'.join(sorted(fb))[:30]))
            elif k in O:
                raise 不可('%s：两侧改同键而异（%s）' % (径名, _键名(k)))
            else:
                raise 不可('%s：两侧同增一键而异（%s）' % (径名, _键名(k)))
            留.add(k)
        elif k in A:
            if k not in O:
                值[k] = A[k]; 留.add(k); 计 is not None and 计.update(['A增'])
            elif 同(A[k], O[k]):
                计 is not None and 计.update(['B删'])
            else:
                raise 不可('%s：一删一改（%s）' % (径名, _键名(k)))
        else:
            if k not in O:
                值[k] = B[k]; 留.add(k); 计 is not None and 计.update(['B增'])
            elif 同(B[k], O[k]):
                计 is not None and 计.update(['A删'])
            else:
                raise 不可('%s：一删一改（%s）' % (径名, _键名(k)))
    if 结:
        raise 结[0]
    _两删各增(O, A, B, 径名)
    return [值[k] for k in 序(list(O), list(A), list(B), 留)]


def 正(v, 规, 顶=True):
    """语义之正形：dict 不计序；顶层规中之 list 化为 键→元（不计序·键重即不可）。"""
    if isinstance(v, dict):
        out = {}
        for k, x in v.items():
            字 = 规.get(k) if 顶 else None
            if 字 and isinstance(x, list):
                out[k] = {'\x00'.join(kk): 正(e, 规, False) for kk, e in _键表(x, 字, (k,)).items()}
            else:
                out[k] = 正(x, 规, False)
        return out
    if isinstance(v, list):
        return [正(x, 规, False) for x in v]
    return v


def 语义同(x, y, 规):
    return json.dumps(正(x, 规), ensure_ascii=False, sort_keys=True) == json.dumps(正(y, 规), ensure_ascii=False, sort_keys=True)


# ───────────── 写器 ─────────────
def _dump1(v):
    return json.dumps(v, ensure_ascii=False, indent=1)


def _是dump1(t, v):
    return t in (_dump1(v), _dump1(v) + '\n')


def 写dump1(m, oT, aT, bT, oV, aV, bV, 规):
    if not (_是dump1(oT, oV) and _是dump1(aT, aV) and _是dump1(bT, bV)):
        raise 不可('非 dump1 之式（⛔以写器重排全档）')
    return _dump1(m) + ('\n' if aT.endswith('\n') else '')


def _员起(n, i):
    x = n.员[i]
    return x[1] if n.类 == 'o' else x.始


def _员讫(n, i):
    x = n.员[i]
    return x[2].终 if n.类 == 'o' else x.终


def _隔们(n, t):
    return [t[_员讫(n, i):_员起(n, i + 1)] for i in range(len(n.员) - 1)]


def _拼器(aN, aT, bN, bT, 条):
    """条：[(源 'A'|'B', 其在源之位, 文)] → 容器之文：A 之相邻二员之间取 A 之原隔、B 之相邻取 B 之原隔，余取 A 之常隔。"""
    开, 闭 = aT[aN.始], aT[aN.终 - 1]
    if not 条:
        return 开 + 闭
    a隔, b隔 = _隔们(aN, aT), (_隔们(bN, bT) if bN is not None and bN.类 == aN.类 else [])
    常 = Counter(a隔).most_common(1)[0][0] if a隔 else (Counter(b隔).most_common(1)[0][0] if b隔 else ', ')
    if aN.员:
        前, 后 = aT[aN.始 + 1:_员起(aN, 0)], aT[_员讫(aN, len(aN.员) - 1):aN.终 - 1]
    elif bN is not None and bN.员 and bN.类 == aN.类:
        前, 后 = bT[bN.始 + 1:_员起(bN, 0)], bT[_员讫(bN, len(bN.员) - 1):bN.终 - 1]
    else:
        前 = 后 = ''
    文 = [开, 前]
    for i, (源, 位, x) in enumerate(条):
        if i:
            p源, p位, _ = 条[i - 1]
            if 源 == p源 == 'A' and 位 == p位 + 1:
                文.append(a隔[p位])
            elif 源 == p源 == 'B' and 位 == p位 + 1 and b隔:
                文.append(b隔[p位])
            else:
                文.append(常)
        文.append(x)
    文 += [后, 闭]
    return ''.join(文)


def _绘(m, aN, aT, aV, bN, bT, bV, 规, 径):
    if aN is not None and 同(m, aV):
        return aT[aN.始:aN.终]
    if bN is not None and 同(m, bV):
        return bT[bN.始:bN.终]
    if aN is None:
        raise 不可('%s：无原文可拼' % '/'.join(径))
    if isinstance(m, dict) and aN.类 == 'o':
        a位 = {k: i for i, (k, _, _) in enumerate(aN.员)}
        b位 = {k: i for i, (k, _, _) in enumerate(bN.员)} if bN is not None and bN.类 == 'o' else {}
        条 = []
        for k, mv in m.items():
            if k in a位:
                i = a位[k]
                _, ks, vn = aN.员[i]
                if 同(mv, aV[k]):
                    x = aT[ks:vn.终]
                else:
                    bvn = bN.员[b位[k]][2] if k in b位 else None
                    x = aT[ks:vn.始] + _绘(mv, vn, aT, aV[k], bvn, bT, bV[k] if bvn is not None else None, 规, 径 + (k,))
                条.append(('A', i, x))
            elif k in b位:
                j = b位[k]
                _, ks, vn = bN.员[j]
                if not 同(mv, bV[k]):
                    raise 不可('%s：B 所增之员异於 B' % '/'.join(径 + (k,)))
                条.append(('B', j, bT[ks:vn.终]))
            else:
                raise 不可('%s：员无原文' % '/'.join(径 + (k,)))
        return _拼器(aN, aT, bN, bT, 条)
    字 = 规.get(径[0]) if len(径) == 1 else None
    if 字 and isinstance(m, list) and aN.类 == 'a':
        a位 = {_元键(x, 字, 径): i for i, x in enumerate(aV)}
        b位 = {_元键(x, 字, 径): i for i, x in enumerate(bV)} if bN is not None and bN.类 == 'a' and isinstance(bV, list) else {}
        条 = []
        for x in m:
            k = _元键(x, 字, 径)
            if k in a位 and 同(x, aV[a位[k]]):
                n = aN.员[a位[k]]
                条.append(('A', a位[k], aT[n.始:n.终]))
            elif k in b位 and 同(x, bV[b位[k]]):
                n = bN.员[b位[k]]
                条.append(('B', b位[k], bT[n.始:n.终]))
            elif k in a位 and k in b位:
                i, j = a位[k], b位[k]
                条.append(('A', i, _绘(x, aN.员[i], aT, aV[i], bN.员[j], bT, bV[j], 规, 径 + ('〔%s〕' % _键名(k),))))
            else:
                raise 不可('%s：元无原文（%s）' % ('/'.join(径), _键名(k)))
        return _拼器(aN, aT, bN, bT, 条)
    if isinstance(m, list) and aN.类 == 'a' and isinstance(aV, list):
        # 元内无键之 list（序列之并之果）：每元逐字取自 A 或 B 之同值之元（先 A 後 B、各用一回·⛔生一值）
        bOK = bN is not None and bN.类 == 'a' and isinstance(bV, list)
        用a, 用b, 条 = set(), set(), []
        for x in m:
            i = next((i for i, y in enumerate(aV) if i not in 用a and 同(x, y)), None)
            if i is not None:
                用a.add(i); n = aN.员[i]; 条.append(('A', i, aT[n.始:n.终]))
                continue
            j = next((j for j, y in enumerate(bV) if j not in 用b and 同(x, y)), None) if bOK else None
            if j is None:
                raise 不可('%s：元无原文' % '/'.join(径))
            用b.add(j); n = bN.员[j]; 条.append(('B', j, bT[n.始:n.终]))
        return _拼器(aN, aT, bN, bT, 条)
    raise 不可('%s：无从拼' % '/'.join(径))


def 写拼(m, oT, aT, bT, oV, aV, bV, 规):
    aN, bN = 析节(aT), 析节(bT)
    return aT[:aN.始] + _绘(m, aN, aT, aV, bN, bT, bV, 规, ()) + aT[aN.终:]


写器 = {'dump1': 写dump1, '拼': 写拼}


# ───────────── git merge-file ─────────────
def _净env():
    e = dict(os.environ)
    for k in ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_OBJECT_DIRECTORY', 'GIT_COMMON_DIR', 'GIT_PREFIX'):
        e.pop(k, None)
    return e


def 并文(a, o, b, 式=(), 标=('ours', 'base', 'theirs'), 标长=7):
    """git merge-file -p → (文, rc)；rc：0 净｜1—127 冲突之数｜他 器坏。"""
    d = tempfile.mkdtemp(prefix='账并_')
    try:
        ps = []
        for n, x in (('a', a), ('o', o), ('b', b)):
            p = os.path.join(d, n)
            open(p, 'w', encoding='utf-8', newline='').write(x)
            ps.append(p)
        r = subprocess.run(['git', 'merge-file', '-p', '--marker-size=%d' % 标长] + list(式) +
                           ['-L', 标[0], '-L', 标[1], '-L', 标[2]] + ps, capture_output=True)
        return r.stdout.decode('utf-8', 'surrogateescape'), r.returncode
    finally:
        shutil.rmtree(d, ignore_errors=True)


def _冲突之式():
    try:
        s = subprocess.run(['git', 'config', '--get', 'merge.conflictstyle'], capture_output=True, text=True).stdout.strip()
    except Exception:
        s = ''
    return ['--' + s] if s in ('diff3', 'zdiff3') else []


# ───────────── 两类之并 ─────────────
def 并json(oT, aT, bT, c, 计):
    """→ (文, 法)。不可即抛。c：册之一档。"""
    规 = c.get('键') or {}
    oV, aV, bV = 析值(oT), 析值(aT), 析值(bT)
    m = 键并(oV, aV, bV, c, 计)
    u, urc = 并文(aT, oT, bT, ('--union',))
    if urc == 0:
        try:
            if 语义同(析值(u), m, 规):
                return u, 'union'
        except 不可:
            pass
    由 = []
    for w in c.get('写') or ():
        try:
            s = 写器[w](m, oT, aT, bT, oV, aV, bV, 规)
            if 同(析值(s), m):
                return s, w
            由.append('%s 之果异於键级之并' % w)
        except 不可 as e:
            由.append('%s：%s' % (w, e))
    raise 不可('union 之果不合、写器不成（%s）' % ('；'.join(由) or '此档无写器'))


_标 = 47


def _行键(l):
    s = l.rstrip('\n')
    if s.startswith('|'):
        c = s.split('|')
        if len(c) > 2:
            return '表:' + c[1].strip()
    return '文:' + s


def _块并(o, a, b, 计):
    def 表(ls):
        d = {}
        for l in ls:
            k = _行键(l)
            if k in d:
                raise 不可('冲突之块内键重：%s' % k[:40])
            d[k] = l
        return d
    O, A, B = 表(o), 表(a), 表(b)
    留, 值 = set(), {}
    for k in list(dict.fromkeys(list(A) + list(B))):
        if k in A and k in B:
            if A[k] == B[k]:
                值[k] = A[k]
            elif k in O and A[k] == O[k]:
                值[k] = B[k]; 计.update(['B改'])
            elif k in O and B[k] == O[k]:
                值[k] = A[k]; 计.update(['A改'])
            else:
                raise 不可('两侧改同行而异：%s' % k[:40])
            留.add(k)
        elif k in A:
            if k not in O:
                值[k] = A[k]; 留.add(k); 计.update(['A增'])
            elif A[k] == O[k]:
                计.update(['B删'])
            else:
                raise 不可('一删一改：%s' % k[:40])
        else:
            if k not in O:
                值[k] = B[k]; 留.add(k); 计.update(['B增'])
            elif B[k] == O[k]:
                计.update(['A删'])
            else:
                raise 不可('一删一改：%s' % k[:40])
    # 两版俱留之漏（复核 1119）：非表行两改、表行首格两改、题行两改 → 原键两侧俱删而两侧各增 → 不可（内建於此俱冲突）
    _两删各增(O, A, B, '冲突之块')
    return [值[k] for k in 序(list(O), list(A), list(B), 留)]


def 并md(oT, aT, bT, 计):
    if not all(x.endswith('\n') for x in (oT, aT, bT)):
        raise 不可('md 之末无换行')
    t, rc = 并文(aT, oT, bT, ('--diff3',), ('A', 'O', 'B'), _标)
    if not 0 < rc < 128:
        raise 不可('merge-file rc=%d' % rc)
    开, 基, 分, 闭 = ('<' * _标, '|' * _标, '=' * _标, '>' * _标)
    果, 态, a, o, b = [], None, [], [], []
    for l in t.splitlines(keepends=True):
        s = l.rstrip('\n')
        if 态 is None and s.startswith(开) and s[_标:_标 + 1] in ('', ' '):
            态, a, o, b = 'a', [], [], []
        elif 态 == 'a' and s.startswith(基) and s[_标:_标 + 1] in ('', ' '):
            态 = 'o'
        elif 态 == 'o' and s == 分:
            态 = 'b'
        elif 态 == 'b' and s.startswith(闭) and s[_标:_标 + 1] in ('', ' '):
            果 += _块并(o, a, b, 计)
            态 = None
        elif 态 is None:
            果.append(l)
        else:
            {'a': a, 'o': o, 'b': b}[态].append(l)
    if 态 is not None:
        raise 不可('冲突之标不闭')
    s = ''.join(果)
    OL, AL, BL, RL = (x.splitlines() for x in (oT, aT, bT, s))
    o集, a集, b集 = set(OL), set(AL), set(BL)
    期 = (a集 | b集) - ((o集 - a集) | (o集 - b集))
    if set(RL) != 期:
        raise 不可('行集不合（多 %d、缺 %d）' % (len(set(RL) - 期), len(期 - set(RL))))
    ca, cb = Counter(AL), Counter(BL)
    多 = [l for l, n in Counter(RL).items() if n > max(ca[l], cb[l])]
    if 多:
        raise 不可('行重出：%s' % 多[0][:40])
    return s, '键级·md表'


_数行式 = re.compile(r'^\|\s*(\d+)\s*\|')


def 首格稳排(s, 节头):
    """〔W920 治·甲之轻〕md表 并毕：「节头」（如「## 二、」）所领之节内，相邻之「| <数> |」行按其数稳排 → (文, 动否)。
    主插 485、治插 484（同在 483 之後）→ 键级之并取 A 之序再插 B 者 → 483、485、484；复盘.成章之法之插 取 max(前) 定位即愈乱。
    只换序、⛔增删一行（并md 之行集与行数之验俱不变）；无其节即原样。"""
    ls = s.split('\n')
    i0 = next((i for i, l in enumerate(ls) if l.startswith(节头)), None)
    if i0 is None:
        return s, False
    i1 = next((i for i in range(i0 + 1, len(ls)) if ls[i].startswith('## ')), len(ls))
    动, i = False, i0 + 1
    while i < i1:
        if not _数行式.match(ls[i]):
            i += 1
            continue
        j = i
        while j < i1 and _数行式.match(ls[j]):
            j += 1
        块 = sorted(ls[i:j], key=lambda l: int(_数行式.match(l).group(1)))
        if 块 != ls[i:j]:
            ls[i:j], 动 = 块, True
        i = j
    return '\n'.join(ls), 动


# ───────────── driver ─────────────
def _印(s):
    try:
        sys.stderr.write(s + '\n'); sys.stderr.flush()
    except Exception:
        pass


def 全档冲突(aT, oT, bT, L, 三=False, 由=''):
    """行之并净而键级不可（或器坏）：以全档为一冲突之块（ours／[base]／theirs），⛔静默取行之并。
    其由书於 ours 之标行（手解之据·⛔增一内容之行）。"""
    def n(x):
        return x if (not x or x.endswith('\n')) else x + '\n'
    注 = ('（账并：%s）' % re.sub(r'\s+', ' ', 由)[:160]) if 由 else ''
    return ('<' * L + ' ours' + 注 + '\n' + n(aT) + (('|' * L + ' base\n' + n(oT)) if 三 else '') +
            '=' * L + '\n' + n(bT) + '>' * L + ' theirs\n')


def _写(p, s):
    open(p, 'w', encoding='utf-8', newline='').write(s)


def 驱(O, A, B, P, L=7, 册们=None):
    """git 之 driver：结果写 %A；0 净或自并｜1 留冲突。git merge-file 坏即抛（驱安 复 %A、留冲突之标）。
    生成之图（%P 在 生成之图）：%A 原样（取 ours）、rc 0、印一行——⛔读、⛔并。"""
    if P in 生成之图:
        _印('账并：%s 生成之图·取 ours（⚠ 待下回重生）' % P)
        return 0
    册们 = 册 if 册们 is None else 册们
    try:
        oT, aT, bT = (open(p, 'rb').read().decode('utf-8') for p in (O, A, B))
    except UnicodeDecodeError as e:
        r = subprocess.run(['git', 'merge-file', '--marker-size=%d' % L, '-L', 'ours', '-L', 'base', '-L', 'theirs'] + _冲突之式() + [A, O, B])
        if not 0 <= r.returncode < 128:
            raise RuntimeError('git merge-file 坏（rc=%d）' % r.returncode)
        _印('账并：%s 非 UTF-8（%s）——照内建%s' % (P, str(e)[:40], '净并' if r.returncode == 0 else '留冲突'))
        return 0 if r.returncode == 0 else 1
    式 = tuple(_冲突之式())
    t, rc = 并文(aT, oT, bT, 式, 标长=L)
    c = 册们.get(P)
    if not (0 <= rc < 128):
        raise RuntimeError('git merge-file 坏（rc=%d）' % rc)
    注 = ''
    if rc == 0:
        if not (c and c.get('类') == 'json'):
            if c and c.get('序'):          # 〔W920 治〕净并亦稳排其节之章行（只换序）
                try:
                    t, 动 = 首格稳排(t, c['序'])
                    if 动:
                        _印('账并：%s 净并·「%s」节之章行乱序 → 按首格之数稳排' % (P, c['序']))
                except Exception as e:
                    _印('账并：⚠ %s 稳排不成（%s）——照净并' % (P, str(e)[:60]))
            if t != aT:
                _写(A, t)
            return 0
        # json 之账：行之三方并「净」而值或错置（形近之元，diff 之对齐移其改於邻元：自测⑤之二）——须与键级之并语义同方成
        try:
            oV, aV, bV = 析值(oT), 析值(aT), 析值(bT)
        except 不可 as e:   # 其底（O／A／B）不可析：同旧
            if t != aT:
                _写(A, t)
            _印('账并：⚠ %s 行之并净而其底不可析（%s）——照内建之净并成之（同旧）' % (P, e))
            return 0
        try:
            m = 键并(oV, aV, bV, c)
        except 结构不可 as e:   # 结构之不判（重键、缺键、元内无键之 list 序列之并亦冲突…）——内建之净并照旧（⛔比今更坏）
            if t != aT:
                _写(A, t)
            _印('账并：⚠ %s 行之并净而键级不判（%s）——照内建之净并成之（同旧）' % (P, e))
            return 0
        except 不可 as e:
            _写(A, 全档冲突(aT, oT, bT, L, bool(式), '行之并净而键级之并判冲突：%s' % e))
            _印('账并：%s 行之并净而键级之并判冲突（%s）——内建之净并於此或静默改值、⛔取；留全档之冲突' % (P, e))
            return 1
        try:
            if 语义同(析值(t), m, c.get('键') or {}):
                if t != aT:
                    _写(A, t)
                return 0
        except 不可:
            pass
        注 = '行之并净而与键级之并不合·'
    计 = Counter()
    try:
        if not c:
            raise 不可('档不在册（键未定）')
        if c['类'] == 'json':
            s, 法 = 并json(oT, aT, bT, c, 计)
        elif c['类'] == 'md表':
            s, 法 = 并md(oT, aT, bT, 计)
            if c.get('序'):                 # 〔W920 治〕并毕稳排其节之章行（只换序·并md 之验已过）；稳排崩只 ⚠、照并之果
                try:
                    s, 动 = 首格稳排(s, c['序'])
                    法 += '·章行稳排' if 动 else ''
                except Exception as e:
                    法 += '·⚠ 稳排不成（%s）' % str(e)[:40]

        else:
            raise 不可('类不识：%s' % c['类'])
        法 = 注 + 法
    except 不可 as e:
        if rc == 0:
            _写(A, 全档冲突(aT, oT, bT, L, bool(式), '行之并净而与键级之并不合、键级之果写不成：%s' % e))
            _印('账并：%s 行之并净而与键级之并不合（内建之值或错置）、键级之果写不成（%s）——⛔取；留全档之冲突' % (P, e))
            return 1
        _写(A, t)
        _印('账并：%s 不可自并（%s）——留冲突 %d 处（同内建）' % (P, e, rc))
        return 1
    _写(A, s)
    _印('账并：%s 自并（%s）——%s' % (P, 法, '、'.join('%s %d' % (k, 计[k]) for k in
                                         ('A增', 'B增', 'A改', 'B改', '两改合', '序并', 'A删', 'B删', '两增同') if 计[k]) or '无键之变'))
    return 0


def 驱安(O, A, B, P, L=7, 册们=None):
    """git 调之之入口：驱 崩（未捕之异常）或 git merge-file 坏 → 复 %A 之原文、再以 git merge-file 写冲突之标；
    再不成则以本器写全档之冲突。→ 0｜1（⛔「%A 原样而 git 记冲突」：手并者照常 git add 即静默丢 theirs）。"""
    try:
        原 = open(A, 'rb').read()
    except Exception:
        原 = None
    try:
        rc = 驱(O, A, B, P, L, 册们)
        if rc in (0, 1):
            return rc
        raise RuntimeError('驱 rc=%r' % (rc,))
    except BaseException as e:
        由 = '%s：%s' % (type(e).__name__, str(e)[:80])
        try:
            if 原 is not None:
                open(A, 'wb').write(原)
            r = subprocess.run(['git', 'merge-file', '--marker-size=%d' % L, '-L', 'ours', '-L', 'base', '-L', 'theirs'] + _冲突之式() + [A, O, B],
                               capture_output=True, timeout=120)
            if r.returncode == 0:
                _印('账并：⛔ %s 器崩（%s）——退回内建之三方并：净（同旧）' % (P, 由))
                return 0
            if 0 < r.returncode < 128:
                _印('账并：⛔ %s 器崩（%s）——退回内建之三方并：留冲突 %d 处（同旧）' % (P, 由, r.returncode))
                return 1
            由 += '；git merge-file rc=%d' % r.returncode
        except BaseException as e2:
            由 += '；退路亦崩：%s' % str(e2)[:60]
        try:
            读 = lambda p: open(p, 'rb').read().decode('utf-8', 'surrogateescape')
            aT = 原.decode('utf-8', 'surrogateescape') if 原 is not None else ''
            open(A, 'w', encoding='utf-8', errors='surrogateescape', newline='').write(全档冲突(aT, 读(O), 读(B), L, False, '器坏：' + 由))
        except BaseException:
            pass
        _印('账并：⛔ %s 器坏（%s）——留全档之冲突' % (P, 由))
        return 1


def _g(root):
    def g(*a):
        return subprocess.run(['git', '-C', root] + list(a), capture_output=True, text=True, env=_净env())
    return g


def 装(root=ROOT, 印=True):
    """git config --local merge.账并.driver（只此一键：merge.<名>.name 可选，只有 name 而无 driver 则 git merge 直 fatal——⛔半装）。
    幂等；每写查 rc、写毕重读（与 DRIVER 不同即 ⛔ rc 1）；旧装之 name 去之。→ 0 成｜1 不成（非 git 之仓、写不成、读不合）。"""
    g = _g(root)
    if g('rev-parse', '--git-dir').returncode != 0:
        印 and print('⛔ 账并 --装：%s 非 git 之仓' % root)
        return 1
    k, kn = 'merge.%s.driver' % 名, 'merge.%s.name' % 名
    改 = []
    if g('config', '--local', '--get-all', k).stdout != DRIVER + '\n':
        r = g('config', '--local', '--replace-all', k, DRIVER)
        if r.returncode != 0:
            印 and print('⛔ 账并 --装：写 %s 不成（rc=%d：%s）——git 退回内建之并' % (k, r.returncode, (r.stderr or '').strip()[:120]))
            return 1
        改.append(k)
    v = g('config', '--get', k)
    if v.returncode != 0 or v.stdout != DRIVER + '\n':
        印 and print('⛔ 账并 --装：写毕重读 %s 不合（rc=%d）' % (k, v.returncode))
        return 1
    if g('config', '--local', '--get-all', kn).returncode == 0:
        r = g('config', '--local', '--unset-all', kn)
        if r.returncode == 0:
            改.append('去 ' + kn)
        else:   # driver 已在，name 留之无害（半装之态唯「有 name 无 driver」）
            印 and print('⚠ 账并 --装：去旧之 %s 不成（rc=%d）——driver 已装，无害' % (kn, r.returncode))
    印 and print(('✓ 账并 --装：%s' % '、'.join(改)) if 改 else '✓ 账并 已装（%s 同·⛔改）' % k)
    return 0


def 卸(root=ROOT, 印=True):
    """回：git config --local --remove-section merge.账并（全段去之·⛔只 --unset driver 而留 name 之半装）。→ 0｜1。"""
    g = _g(root)
    if g('rev-parse', '--git-dir').returncode != 0:
        印 and print('⛔ 账并 --卸：%s 非 git 之仓' % root)
        return 1
    if g('config', '--local', '--get-regexp', r'^merge\.%s\.' % 名).returncode != 0:
        印 and print('✓ 账并 本未装（merge.%s 之段无）' % 名)
        return 0
    r = g('config', '--local', '--remove-section', 'merge.%s' % 名)
    if r.returncode != 0 or g('config', '--local', '--get-regexp', r'^merge\.%s\.' % 名).returncode == 0:
        印 and print('⛔ 账并 --卸：remove-section 不成（rc=%d：%s）' % (r.returncode, (r.stderr or '').strip()[:120]))
        return 1
    印 and print('✓ 账并 --卸：merge.%s 之段已去（git 退回内建之并）' % 名)
    return 0


# 坑63：gate.yml 备候之 --装 已演（演练「账并」run 44619377361 过），而 1119 章界之直推为平台之检所拒（Undermining Oversight·⛔绕）——
# 改 workflows 唯待许可之路；未装只 ⚠（⛔限：拦推即拖累写书，而写书之坐本地之并已有 driver·474 证）。


def gate之判(gy, 末):
    """gate.yml 之文、末章 → (态 ✓|⚠|✗, 语)。--装 须在 bei_hou 内、git merge 之前、带 || true（主之树无本器即照旧）。"""
    i装, i并, bh = gy.find('工具/账并.py --装'), gy.find('git merge --no-edit'), gy.find('bei_hou() {')
    if i装 < 0:
        return '⚠', 'gate.yml 备候未装 driver（已演·直推为平台所拒，待许可之路）——GitHub 之并退回内建；写书之坐本地并（推.py 已装 driver）'
    if 0 <= bh < i装 < i并 and '账并.py --装 || true' in gy:
        return '✓', 'gate.yml 备候於 git merge 之前装 driver（|| true：未入主之树照旧）'
    return '✗', 'gate.yml 之 --装 不在 bei_hou 内 git merge 之前、或无 || true'


# ───────────── 自测 ─────────────
def _读料(n):
    p = os.path.join(料目, n)
    return open(p, encoding='utf-8').read() if os.path.exists(p) else None


def 自测():
    ok = 共 = 0

    def T(名_, 真, 注=''):
        nonlocal ok, 共
        共 += 1
        ok += bool(真)
        print('  %s %s%s' % ('✓' if 真 else '✗', 名_, ('｜' + 注) if 注 else ''))

    t = tempfile.mkdtemp(prefix='账并测_')
    err = []
    try:
        def 跑(oT, aT, bT, P, 册们=None):
            d = tempfile.mkdtemp(dir=t)
            ps = []
            for n, x in (('O', oT), ('A', aT), ('B', bT)):
                p = os.path.join(d, n)
                open(p, 'w', encoding='utf-8', newline='').write(x)
                ps.append(p)
            import io
            旧, sys.stderr = sys.stderr, io.StringIO()
            try:
                rc = 驱安(ps[0], ps[1], ps[2], P, 7, 册们)
                e = sys.stderr.getvalue()
            finally:
                sys.stderr = 旧
            return rc, open(ps[1], encoding='utf-8').read(), e

        def 账(行, 说明='费账'):
            return _dump1({'说明': 说明, '行': 行})

        def 行(k, v=1, 时='10:00'):
            return {'键': k, '名': '', '时': 时, '美元': v}

        基 = [行('w%d' % i, i) for i in range(1, 6)]
        F = '设定/费账.json'
        # ① 净：两侧改远隔之键 → 照常三方并
        O = 账(基); A = 账([行('w1', 10)] + 基[1:]); B = 账(基[:4] + [行('w5', 50)])
        rc, s, e = 跑(O, A, B, F)
        T('① 净即成（与 git merge-file 同·⛔印自并）', rc == 0 and s == 并文(A, O, B, tuple(_冲突之式()))[0] and '自并' not in e)
        # ② 尾两增（费账之常形）→ 自并：键集＝O∪A增∪B增、各一、先 ours 後 theirs；印一行
        O = 账(基); A = 账(基 + [行('a1'), 行('a2')]); B = 账(基 + [行('b1')])
        rc, s, e = 跑(O, A, B, F)
        ks = [x['键'] for x in json.loads(s)['行']] if rc == 0 else []
        T('② 尾两增 → 自并（键无重无失·先 ours 後 theirs）', rc == 0 and ks == ['w1', 'w2', 'w3', 'w4', 'w5', 'a1', 'a2', 'b1']
          and s == 账(基 + [行('a1'), 行('a2'), 行('b1')]), e.strip())
        T('③ 每自并一回印一行於 stderr', e.count('账并：') == 1 and '自并' in e and 'A增 2' in e and 'B增 1' in e)
        # ④ 两侧改同键而异 → 败、留冲突、rc 1
        O = 账(基 + [行('x', 1)]); A = 账(基 + [行('x', 2), 行('a1')]); B = 账(基 + [行('x', 3), 行('b1')])
        rc, s, e = 跑(O, A, B, F)
        T('④ 两侧改同键（同字）而异 → 败、留冲突', rc == 1 and '<<<<<<<' in s and '>>>>>>>' in s and '两侧改同' in e, e.strip()[:70])
        # ④之二 两侧改同元之异字 → 入元以字并（dict 以其键）：名取 A、美元取 B
        O = 账(基 + [行('x', 1)]); A = 账(基 + [dict(行('x', 1), 名='甲名'), 行('a1')]); B = 账(基 + [行('x', 3), 行('b1')])
        rc, s, e = 跑(O, A, B, F)
        r = [x for x in json.loads(s)['行'] if x['键'] == 'x'] if rc == 0 else []
        T('④之二 两侧改同元之异字 → 元内以字并', rc == 0 and r == [dict(行('x', 3), 名='甲名')] and '两改合 1' in e, e.strip()[:70])
        # ⑤ 一删一改 → 败（行之并或「净」：仍须败）
        O = 账(基 + [行('x', 1), 行('y', 1)]); A = 账(基 + [行('y', 1), 行('a1')]); B = 账(基 + [行('x', 9), 行('y', 1), 行('b1')])
        rc, s, e = 跑(O, A, B, F)
        T('⑤ 一删一改 → 败、留冲突（内建於此「净」而错：x 之改落於 y）', rc == 1 and '<<<<<<<' in s and '一删一改' in e, e.strip()[:70])
        # ⑤之二 内建之净并静默改值（diff 对齐移改於邻元）→ 以键级纠之
        for 题, o, a, b, 期 in (
                ('一删一改他', 基 + [行('x'), 行('y')], 基 + [行('y'), 行('a1')], 基 + [行('x'), 行('y', 9), 行('b1')],
                 [('y', 9), ('a1', 1), ('b1', 1)]),
                ('记之移', 基 + [行('x'), 行('y'), 行('z')], 基 + [行('y'), 行('z'), 行('x', 7)], 基 + [行('x'), 行('y', 8), 行('z')],
                 [('y', 8), ('z', 1), ('x', 7)])):
            O, A, B = 账(o), 账(a), 账(b)
            t0, r0 = 并文(A, O, B)
            内错 = r0 == 0 and [(x['键'], x['美元']) for x in json.loads(t0)['行'][5:]] != 期
            rc, s, e = 跑(O, A, B, F)
            T('⑤之二 内建净而错（%s）→ 键级纠之' % 题, 内错 and rc == 0 and [(x['键'], x['美元']) for x in json.loads(s)['行'][5:]] == 期
              and '与键级之并不合' in e, e.strip()[:70])
        # ⑥ 两侧同增一键而异 → 败
        O = 账(基); A = 账(基 + [行('n', 1)]); B = 账(基 + [行('n', 2)])
        rc, s, e = 跑(O, A, B, F)
        T('⑥ 两侧同增一键而异 → 败', rc == 1 and '<<<<<<<' in s and '同增一键而异' in e)
        # ⑦ union 之果非法 JSON、其档无写器 → 败
        无写 = {'设定/测.json': {'类': 'json', '键': {'行': ('键',)}, '写': ()}}
        O = 账(基); A = 账(基 + [行('a1')]); B = 账(基 + [行('b1')])
        u, _ = 并文(A, O, B, ('--union',))
        try:
            析值(u); u坏 = False
        except 不可:
            u坏 = True
        rc, s, e = 跑(O, A, B, '设定/测.json', 无写)
        T('⑦ union 之果非法 JSON 而无写器 → 败', u坏 and rc == 1 and '<<<<<<<' in s and 'union 之果不合' in e)
        # ⑧ union 之果可析而语义不全（复活一侧所删之元）、无写器 → 败；有写器（拼）→ 自并而无复活
        O = '{"说明": "x", "行": [\n {"键": "w1"},\n {"键": "w2"},\n {"键": "w3"}\n]}\n'
        A = '{"说明": "x", "行": [\n {"键": "w1"},\n {"键": "w2v", "改": 1},\n {"键": "w3"}\n]}\n'
        B = '{"说明": "x", "行": [\n {"键": "w1"},\n {"键": "w2"},\n {"键": "b1"},\n {"键": "w3"}\n]}\n'
        u, urc = 并文(A, O, B, ('--union',))
        try:
            u可 = isinstance(析值(u), dict)
        except 不可:
            u可 = False
        rc, s, e = 跑(O, A, B, '设定/测.json', 无写)
        rc2, s2, e2 = 跑(O, A, B, '设定/测.json', {'设定/测.json': dict(无写['设定/测.json'], 写=('拼',))})
        k2 = [x['键'] for x in json.loads(s2)['行']] if rc2 == 0 else []
        T('⑧ union 可析而复活所删 → 无写器败、拼则自并（w2 去、w2v 与 b1 在）', u可 and rc == 1 and rc2 == 0 and k2 == ['w1', 'w2v', 'b1', 'w3'], e2.strip())
        # ⑨ union 致对象重键（一侧改「说明」、一侧於其旁增员）→ 判重键、⛔取其末；拼则自并
        O = '{\n "说明": "旧",\n "甲": 1\n}\n'
        A = '{\n "说明": "新",\n "甲": 1\n}\n'
        B = '{\n "说明": "旧",\n "乙": 2,\n "甲": 1\n}\n'
        规0 = {'设定/测.json': {'类': 'json', '键': {}, '写': ()}}
        rc, s, e = 跑(O, A, B, '设定/测.json', 规0)
        rc2, s2, e2 = 跑(O, A, B, '设定/测.json', {'设定/测.json': {'类': 'json', '键': {}, '写': ('拼',)}})
        T('⑨ union 致重键 → ⛔静默取末（无写器败；拼得 说明＝新、乙＝2）', rc == 1 and rc2 == 0 and json.loads(s2) == {'说明': '新', '乙': 2, '甲': 1}, e.strip()[:60])
        # ⑩ 拼：A 之未动之元逐字留（一行之元与多行之元混排·法用册之式）；union 致同 id 两见 → 判不合 → 拼
        O = '{\n "法": [\n  {"id": "甲", "名": "一"},\n  {\n   "id": "乙",\n   "名": "二"\n  },\n  {"id": "丙", "名": "三"}\n ]\n}\n'
        A = O.replace('{"id": "丙", "名": "三"}', '{"id": "丙", "名": "三改"},\n  {"id": "丁", "名": "四"}')
        B = O.replace('{"id": "丙", "名": "三"}', '{"id": "丙", "名": "三"},\n  {"id": "戊", "名": "五"}').replace('"名": "二"', '"名": "二改"')
        法规 = {'设定/法用册.json': 册['设定/法用册.json']}
        rc, s, e = 跑(O, A, B, '设定/法用册.json', 法规)
        期 = '{\n "法": [\n  {"id": "甲", "名": "一"},\n  {\n   "id": "乙",\n   "名": "二改"\n  },\n  {"id": "丙", "名": "三改"},\n  {"id": "丁", "名": "四"},\n  {"id": "戊", "名": "五"}\n ]\n}\n'
        T('⑩ 拼：未动之元逐字、所改所增取其侧之原文（union 同 id 两见即⛔取）', rc == 0 and s == 期 and '（拼）' in e, e.strip()[:80])
        # ⑪ 输入坏（一侧非法 JSON）→ 败
        O = 账(基); A = 账(基 + [行('a1')]); B = 账(基 + [行('b1')])[:-3]
        rc, s, e = 跑(O, A, B, F)
        T('⑪ 一侧非法 JSON → 败', rc == 1 and '<<<<<<<' in s)
        # ⑫ 档不在册 → 败（旧行为）
        O = 账(基); A = 账(基 + [行('a1')]); B = 账(基 + [行('b1')])
        rc, s, e = 跑(O, A, B, '设定/他.json')
        T('⑫ 档不在册 → 留冲突（同内建）', rc == 1 and s == 并文(A, O, B, tuple(_冲突之式()))[0] and '档不在册' in e)
        # ⑬ md表：两侧尾增 → 自并；一改一增（相邻）→ 自并且旧行⛔复活；两侧改同行而异 → 败
        M = '方法账.md'
        P = '设定/方法账.md'
        头 = '# 账\n\n| 件 | 法 |\n|---|---|\n| 甲 | 一 |\n| 乙 | 二 |\n'
        rc, s, e = 跑(头, 头 + '| 丙 | 三 |\n| 丁 | 四 |\n', 头 + '| 戊 | 五 |\n', P)
        T('⑬ md表 两侧尾增 → 自并（先 ours 後 theirs）', rc == 0 and s == 头 + '| 丙 | 三 |\n| 丁 | 四 |\n| 戊 | 五 |\n', e.strip()[:60])
        rc, s, e = 跑(头, 头.replace('| 乙 | 二 |', '| 乙 | 二·已行 |'), 头 + '| 戊 | 五 |\n', P)
        T('⑭ md表 一改旧行一增於其後 → 自并（旧行⛔复活）', rc == 0 and s == 头.replace('| 乙 | 二 |', '| 乙 | 二·已行 |') + '| 戊 | 五 |\n'
          and '| 乙 | 二 |' not in s, e.strip()[:60])
        rc, s, e = 跑(头, 头.replace('| 乙 | 二 |', '| 乙 | 二甲 |'), 头.replace('| 乙 | 二 |', '| 乙 | 二乙 |'), P)
        T('⑮ md表 两侧改同表行之他格而异 → 败', rc == 1 and '<<<<<<<' in s)
        rc, s, e = 跑(头, 头.replace('| 乙 | 二 |\n', ''), 头.replace('| 乙 | 二 |', '| 乙 | 二改 |') + '| 戊 | 五 |\n', P)
        T('⑯ md表 一删一改 → 败', rc == 1 and '<<<<<<<' in s)
        # ㉔ 两版俱留之漏（复核 1119）：md 非表行两改、表行首格两改、题行两改 → 败（内建於此俱冲突；旧器两版俱留而 rc 0）
        头2 = '# 方法账（旧题）\n\n**用法**：旧之用法\n\n| 件 | 法 |\n|---|---|\n| 甲 | 一 |\n| 乙 | 二 |\n| 丙 | 三 |\n'
        for 题, a, b in (('非表行两改', ('旧之用法', '甲之用法'), ('旧之用法', '乙之用法')),
                        ('表行首格两改', ('| 甲 | 一 |', '| 甲✓ | 一 |'), ('| 甲 | 一 |', '| 甲·废 | 一 |')),
                        ('题行两改', ('旧题', 'A题'), ('旧题', 'B题'))):
            rc, s, e = 跑(头2, 头2.replace(*a), 头2.replace(*b), P)
            T('㉔ md表 %s → 败、留冲突（⛔两版俱留）' % 题, rc == 1 and '<<<<<<<' in s and 0 < 并文(头2.replace(*a), 头2, 头2.replace(*b))[1] < 128, e.strip()[:80])
        # ㉕ JSON 键字两改而异（总编辑复核账 裁←规＋时）→ 败；同元之二键字两侧各改而不相邻（内建净而对）→ 照内建（⚠·⛔推翻）
        Fz = '设定/总编辑复核账.json'
        裁 = lambda 改=None: _dump1({'裁': [dict({'规': '规%d' % i, '果': '可', '注': '', '时': '11-0%d' % i}, **(改 or {}).get(i, {})) for i in range(1, 6)]})
        rc, s, e = 跑(裁(), 裁({3: {'规': '规3（A 修字）'}}), 裁({3: {'规': '规3（B 修字）'}}), Fz)
        T('㉕ JSON 键字两改而异 → 败（⛔两元俱留）', rc == 1 and '<<<<<<<' in s and '两版俱留' in e, e.strip()[:80])
        Az, Bz = 裁({3: {'规': '规3甲'}}), 裁({3: {'时': '11-30'}})
        t0, r0 = 并文(Az, 裁(), Bz)
        rc, s, e = 跑(裁(), Az, Bz, Fz)
        T('㉕之二 同元之二键字两侧各改（内建净）→ 照内建之净并、印 ⚠（结构之不判·⛔比今更坏）', r0 == 0 and rc == 0 and s == t0
          and [(x['规'], x['时']) for x in json.loads(s)['裁']][2] == ('规3甲', '11-30') and '⚠' in e and '键级不判' in e, e.strip()[:80])
        # ㉖ 元内无键之 list 两侧俱改（坑.守：A 改首项、B 末增）→ 序列三方并：内建净者照成（旧器全档冲突）；行之并有冲突者亦自并
        Fk = '设定/方法坑账.json'
        坑 = lambda: {'说明': 'x', '坑': [{'号': i, '名': '坑%d' % i, '守': ['工具/a%d.py' % j for j in range(6)], '复踩': [], '格': ['g']} for i in range(1, 6)]}
        import copy
        o, a, b = 坑(), 坑(), 坑()
        a['坑'][2]['守'][0] = '工具/改.py'; b['坑'][2]['守'].append('工具/新.py')
        期守 = ['工具/改.py'] + ['工具/a%d.py' % j for j in range(1, 6)] + ['工具/新.py']
        t0, r0 = 并文(_dump1(a), _dump1(o), _dump1(b))
        rc, s, e = 跑(_dump1(o), _dump1(a), _dump1(b), Fk)
        T('㉖ 元内无键之 list 两侧异处改（内建净而对）→ 照成（⛔全档冲突）', r0 == 0 and rc == 0 and json.loads(s)['坑'][2]['守'] == 期守 and '<<<' not in s, e.strip()[:80])
        a2, b2 = copy.deepcopy(a), copy.deepcopy(b)
        a2['坑'].append({'号': 6, '名': '坑6', '守': [], '复踩': [], '格': []}); b2['坑'].append({'号': 7, '名': '坑7', '守': [], '复踩': [], '格': []})
        rc, s, e = 跑(_dump1(o), _dump1(a2), _dump1(b2), Fk)
        T('㉖之二 同上而两侧尾各增一坑（行之并冲突）→ 自并（序并 1·坑 6、7 俱在）', rc == 0 and json.loads(s)['坑'][2]['守'] == 期守
          and [x['号'] for x in json.loads(s)['坑']] == [1, 2, 3, 4, 5, 6, 7] and '序并 1' in e, e.strip()[:80])
        a3, b3 = copy.deepcopy(o), copy.deepcopy(o)
        a3['坑'][2]['守'].append('工具/甲.py'); b3['坑'][2]['守'].append('工具/乙.py')
        a3['坑'].append({'号': 6, '名': '坑6', '守': [], '复踩': [], '格': []}); b3['坑'].append({'号': 7, '名': '坑7', '守': [], '复踩': [], '格': []})
        rc, s, e = 跑(_dump1(o), _dump1(a3), _dump1(b3), Fk)
        T('㉖之三 元内无键之 list 两侧同处各增（序列之并亦冲突）→ 败、留冲突', rc == 1 and '<<<<<<<' in s and '序列之并亦冲突' in e, e.strip()[:80])
        # ㉗ 基有重键（_键表 不判）而两侧改远隔之元（内建净）→ 照内建、印 ⚠（旧器全档冲突）
        o = 基 + [行('w1', 9)] + [行('p%d' % i) for i in range(8)]
        a = [行('w1', 10)] + o[1:]; b = o[:-1] + [行('p7', 70)]
        t0, r0 = 并文(账(a), 账(o), 账(b))
        rc, s, e = 跑(账(o), 账(a), 账(b), F)
        T('㉗ 基有重键、两侧改远隔（内建净）→ 照内建之净并、印 ⚠', r0 == 0 and rc == 0 and s == t0 and '键重' in e and '⚠' in e, e.strip()[:80])
        # ㉘ 法用册：一侧移 待X→法、一侧移 待X→废（内建净而 X 两处俱在）→ 败（并後 id 唯一之不变式）；全档冲突之标行书其由
        法基 = {'说明': 'x', '法': [{'id': 'f%d' % i} for i in range(3)], '待': [{'id': 'X', '证': []}, {'id': 'Y', '证': []}],
              '机证不能': [], '缓': [], '废': [{'id': 'z%d' % i} for i in range(3)]}
        a, b = copy.deepcopy(法基), copy.deepcopy(法基)
        a['待'].pop(0); a['法'].append({'id': 'X', '证': ['a']})
        b['待'].pop(0); b['废'].append({'id': 'X', '由': '废'})
        rc, s, e = 跑(_dump1(法基), _dump1(a), _dump1(b), '设定/法用册.json')
        T('㉘ 法用册 同 id 两侧各移於异处 → 败（全档冲突·标行书由）', rc == 1 and s.startswith('<<<<<<< ours（账并：') and '两见' in s.split('\n')[0], e.strip()[:80])
        # ㉙ 费账一元两侧各改其量之字（时、美元·不相邻·内建净而拼出不相应之量）→ 败；名（白）与量各改 → 自并（④之二）
        量 = lambda **k: dict({'键': 'x', '名': '', '时': '10:00', '席': 1, '来回': 2, '全量': 3, '美元': 1}, **k)
        o, a, b = 基 + [量()], 基 + [量(时='11:00')], 基 + [量(美元=2)]
        t0, r0 = 并文(账(a), 账(o), 账(b))
        rc, s, e = 跑(账(o), 账(a), 账(b), F)
        T('㉙ 费账一元两侧各改量之字（内建净而拼）→ 败（须整元同改）', r0 == 0 and rc == 1 and '<<<<<<<' in s and '整元同改' in e, e.strip()[:80])
        # ⑰ 回放之片段（真冲突·工具/_负测料/账并/）
        诸 = [('473·费账', '473_费账', '.json', '设定/费账.json'),
              ('473·法用册', '473_法用册', '.json', '设定/法用册.json'),
              ('473·方法账', '473_方法账', '.md', '设定/方法账.md'),
              ('484·成章之法（W920：主改 483 行、章插 484 行）', '484_成章之法', '.md', '设定/成章之法.md'),
              ('472·费账', '472_费账', '.json', '设定/费账.json')]
        for 题, 前, 后, P in 诸:
            O, A, B, Mn = (_读料(前 + '.' + x + 后) for x in ('O', 'A', 'B', 'M'))
            if None in (O, A, B):
                T('⑰ 回放 %s' % 题, False, '料缺：工具/_负测料/账并/%s.*%s' % (前, 后))
                continue
            真冲 = 0 < 并文(A, O, B)[1] < 128
            rc, s, e = 跑(O, A, B, P)
            if 后 == '.json':
                规 = 册[P]['键']
                if Mn is not None:
                    合 = rc == 0 and 语义同(析值(s), 析值(Mn), 规)
                else:
                    a行, b行 = 析值(A)['行'], 析值(B)['行']
                    r行 = 析值(s)['行'] if rc == 0 else []
                    kr = [x['键'] for x in r行]
                    合 = (rc == 0 and len(kr) == len(set(kr)) and set(kr) == {x['键'] for x in a行} | {x['键'] for x in b行}
                          and all(any(同(x, y) for y in a行 + b行 if y['键'] == x['键']) for x in r行))
            else:
                合 = rc == 0 and set(s.splitlines()) == set(Mn.splitlines()) and Counter(s.splitlines()) == Counter(Mn.splitlines())
            T('⑰ 回放 %s：旧并冲突 → 今自并且%s' % (题, '与手并语义同' if Mn is not None else '键无重无失'), 真冲 and 合, e.strip()[:90])
        # ⑰之二〔W920 治·甲之轻〕成章之法：主插 485、治插 484（俱在 483 之後）→ 自并且 §二 之章行 483、484、485（⛔483、485、484）；节外⛔动
        O8, B8 = _读料('484_成章之法.O.md'), _读料('484_成章之法.B.md')
        if None in (O8, B8):
            T('⑰之二 成章之法 主插 N、治插 N-1', False, '料缺')
        else:
            r483 = next(l for l in O8.split('\n') if l.startswith('| 483 |'))
            r485 = r483.replace('| 483 |', '| 485 |').replace('丁·速度', '甲·物证')
            A8 = O8.replace(r483 + '\n', r483 + '\n' + r485 + '\n')
            rc, s, e = 跑(O8, A8, B8, '设定/成章之法.md')
            号 = [l[2:5] for l in s.split('\n') if re.match(r'^\| \d{3} \|', l)]
            rc0, s0, _ = 跑(O8, A8, B8, '设定/成章之法.md', {'设定/成章之法.md': {'类': 'md表'}})
            号0 = [l[2:5] for l in s0.split('\n') if re.match(r'^\| \d{3} \|', l)]
            T('⑰之二 成章之法 主插 485、治插 484 → 自并、§二 稳排 483、484、485（无序之册 → 483、485、484）', 0 < 并文(A8, O8, B8)[1] < 128
              and rc == 0 and 号[-3:] == ['483', '484', '485'] and Counter(s.splitlines()) == Counter(A8.splitlines() + [l for l in B8.splitlines() if l not in O8.splitlines()])
              and rc0 == 0 and 号0[-3:] == ['483', '485', '484'], e.strip()[:90])
            s3, 动3 = 首格稳排('# 册\n\n## 一、\n\n| 9 | a |\n| 1 | b |\n\n## 二、账\n\n| 章 | x |\n|---|---|\n| 3 | c |\n| 2 | d |\n\n| 5 | e |\n| 4 | f |\n\n## 三、\n\n| 8 | g |\n| 7 | h |\n', '## 二、')
            T('⑰之三 首格稳排：只在其节、相邻之数行各段内排；节外⛔动', 动3 and '| 9 | a |\n| 1 | b |' in s3 and '| 2 | d |\n| 3 | c |' in s3
              and '| 4 | f |\n| 5 | e |' in s3 and '| 8 | g |\n| 7 | h |' in s3 and 首格稳排(s3, '## 二、') == (s3, False) and 首格稳排('无节\n', '## 二、') == ('无节\n', False))
        # ⑱ 真 git merge（临时之仓）：--装 幂等；装则自并；⛔装（driver 未设）则同无 .gitattributes 之冲突（退路之证）
        env = _净env()
        env.update(GIT_AUTHOR_NAME='t', GIT_AUTHOR_EMAIL='t@t', GIT_COMMITTER_NAME='t', GIT_COMMITTER_EMAIL='t@t',
                   GIT_CONFIG_NOSYSTEM='1', HOME=t)

        def g(d, *a):
            return subprocess.run(['git', '-c', 'core.hooksPath=/dev/null', '-c', 'init.defaultBranch=主'] + list(a),
                                  cwd=d, capture_output=True, text=True, env=env)

        def 仓(附, 装否, 前=None):
            d = tempfile.mkdtemp(dir=t)
            g(d, 'init', '-q')
            os.makedirs(os.path.join(d, '设定')); os.makedirs(os.path.join(d, '工具'))
            open(os.path.join(d, F), 'w', encoding='utf-8').write(账(基))
            if 附:
                open(os.path.join(d, '.gitattributes'), 'w', encoding='utf-8').write('设定/费账.json merge=账并\n')
                shutil.copy(os.path.abspath(__file__), os.path.join(d, '工具', '账并.py'))
            g(d, 'add', '-A'); g(d, 'commit', '-qm', '基')
            g(d, 'checkout', '-qb', '章')
            open(os.path.join(d, F), 'w', encoding='utf-8').write(账(基 + [行('b1')]))
            g(d, 'commit', '-qam', '章')
            g(d, 'checkout', '-q', '主')
            open(os.path.join(d, F), 'w', encoding='utf-8').write(账(基 + [行('a1'), 行('a2')]))
            g(d, 'commit', '-qam', '治')
            if 装否:
                装(d, 印=False)
            if 前:
                前(d)
            m = g(d, 'merge', '--no-edit', '-m', '并', '章')
            return d, m
        d1, m1 = 仓(True, True)
        k1 = [x['键'] for x in json.loads(open(os.path.join(d1, F), encoding='utf-8').read())['行']] if m1.returncode == 0 else []
        drv = g(d1, 'config', '--get', 'merge.账并.driver').stdout.strip()
        装(d1, 印=False)
        二 = g(d1, 'config', '--get-all', 'merge.账并.driver').stdout.strip().split('\n')
        段 = g(d1, 'config', '--get-regexp', r'^merge\.').stdout.strip().split('\n')
        T('⑱ 真 git merge：装 driver 与 attributes → 自并（印见於 git 之 stderr）、--装 幂等、只此一键（⛔name·半装之由）',
          m1.returncode == 0 and k1 == ['w1', 'w2', 'w3', 'w4', 'w5', 'a1', 'a2', 'b1'] and '账并：设定/费账.json 自并' in m1.stderr
          and drv == DRIVER and 二 == [DRIVER] and 段 == ['merge.账并.driver ' + DRIVER], (m1.stderr.strip().split('\n') or [''])[-1][:80])
        d2, m2 = 仓(True, False)
        d3, m3 = 仓(False, False)
        f2, f3 = (open(os.path.join(d, F), encoding='utf-8').read() for d in (d2, d3))
        s2, s3 = (g(d, 'status', '--porcelain').stdout for d in (d2, d3))
        T('⑲ 退路：attributes 在而 driver 未设 → 与无 attributes 同（同冲突、同文、同状）',
          m2.returncode != 0 and m3.returncode != 0 and f2 == f3 and '<<<<<<<' in f2 and s2 == s3
          and 'CONFLICT' in m2.stdout + m2.stderr and '账并' not in m2.stderr)
        # ⑳ driver 之令：本器不在其树（旧之检出）→ 退回 git merge-file、留冲突之标（⛔%A 原样而 rc 非 0）
        d = tempfile.mkdtemp(dir=t)
        O = 账(基); A = 账(基 + [行('a1')]); B = 账(基 + [行('b1')])
        for n, x in (('O', O), ('A', A), ('B', B)):
            open(os.path.join(d, n), 'w', encoding='utf-8').write(x)
        令 = DRIVER.replace('%O', 'O').replace('%A', 'A').replace('%B', 'B').replace('%P', "'设定/费账.json'").replace('%L', '7')
        r = subprocess.run(['sh', '-c', 令], cwd=d, capture_output=True, text=True, env=env)
        T('⑳ driver 之令於无本器之树 → 退回 git merge-file（留冲突之标、rc 非 0）', r.returncode != 0 and '<<<<<<<' in open(os.path.join(d, 'A'), encoding='utf-8').read())
        # ㉚ 半装之态（只有 merge.账并.name 而无 driver）：git merge 直 fatal（复核实跑·比今更坏）→ --装 补 driver、去 name 即通
        da, ma = 仓(True, False, lambda d: g(d, 'config', 'merge.账并.name', '旧装之名'))
        db, mb = 仓(True, False, lambda d: (g(d, 'config', 'merge.账并.name', '旧装之名'), 装(d, 印=False)))
        T('㉚ 半装（只有 name）：git merge 直 fatal → --装 补 driver 去 name 即自并',
          ma.returncode != 0 and 'lacks command line' in ma.stderr and mb.returncode == 0 and '自并' in mb.stderr
          and g(db, 'config', '--get', 'merge.账并.name').returncode != 0, ma.stderr.strip()[:60])
        # ㉛ --装 写不成（.git/config.lock 在）→ rc 非 0、印 ⛔（旧器印 ✓ 回 0 而实未装）
        dc = tempfile.mkdtemp(dir=t)
        g(dc, 'init', '-q')
        锁 = os.path.join(dc, '.git', 'config.lock')
        open(锁, 'w').close()
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()) as 印:
            rc_l = 装(dc)
        os.remove(锁)
        T('㉛ config.lock 在 → --装 回非 0、印 ⛔（⛔印 ✓ 而实未装）', rc_l != 0 and '⛔' in 印.getvalue() and '✓' not in 印.getvalue()
          and g(dc, 'config', '--get', 'merge.账并.driver').returncode != 0, 印.getvalue().strip()[:80])
        # ㉜ --卸（回）：remove-section 全段去之、幂等；卸後同⑲退回内建
        r1, r2 = 卸(d1, 印=False), 卸(d1, 印=False)
        T('㉜ --卸 全段去之（⛔只 --unset driver 而留 name）、幂等', r1 == 0 and r2 == 0 and g(d1, 'config', '--get-regexp', r'^merge\.').returncode != 0)
        # ㉝ PATH 无 python3：sh 之 exec 败即退 127、|| 之退路不跑（旧令：git 记冲突而 %A 原样）→ 今令 command -v 先判、退回 git merge-file
        bin_ = tempfile.mkdtemp(dir=t)
        os.symlink(shutil.which('git'), os.path.join(bin_, 'git'))
        d = tempfile.mkdtemp(dir=t)
        os.makedirs(os.path.join(d, '工具'))
        shutil.copy(os.path.abspath(__file__), os.path.join(d, '工具', '账并.py'))
        旧令 = '[ -f 工具/账并.py ] && exec python3 工具/账并.py %O %A %B %P %L || exec git merge-file -L ours -L base -L theirs --marker-size=%L %A %O %B'

        def 跑令(令0):
            for n, x in (('O', O), ('A', A), ('B', B)):
                open(os.path.join(d, n), 'w', encoding='utf-8').write(x)
            令1 = 令0.replace('%O', 'O').replace('%A', 'A').replace('%B', 'B').replace('%P', "'设定/费账.json'").replace('%L', '7')
            r = subprocess.run(['/bin/sh', '-c', 令1], cwd=d, capture_output=True, text=True, env=dict(env, PATH=bin_))
            return r.returncode, open(os.path.join(d, 'A'), encoding='utf-8').read()
        r旧, a旧 = 跑令(旧令)
        r新, a新 = 跑令(DRIVER)
        T('㉝ PATH 无 python3 → 退回 git merge-file、留冲突之标', r新 != 0 and '<<<<<<<' in a新,
          '旧令 rc %d、冲突之标 %d 处' % (r旧, a旧.count('<<<<<<<')))
        # ㉞ 驱崩（写半而抛）→ 复 %A 之原文、退回 git merge-file 留冲突之标（⛔%A 原样或半而 git 记冲突）
        内, _ = 并文(A, O, B, tuple(_冲突之式()))
        旧写 = globals()['_写']

        def 坏写(p, s):
            open(p, 'w', encoding='utf-8').write('半')
            raise RuntimeError('试崩')
        globals()['_写'] = 坏写
        try:
            rc, s, e = 跑(O, A, B, F)
        finally:
            globals()['_写'] = 旧写
        T('㉞ 驱崩（写半而抛）→ 复 %A、退回 git merge-file 留冲突之标', rc == 1 and s == 内 and '器崩' in e, e.strip()[:80])
        # ㉟ git 亦不得跑（PATH 空）→ 本器写全档之冲突（标行书由）、rc 1
        旧PATH = os.environ.get('PATH', '')
        os.environ['PATH'] = tempfile.mkdtemp(dir=t)
        try:
            rc, s, e = 跑(O, A, B, F)
        finally:
            os.environ['PATH'] = 旧PATH
        T('㉟ 器与 git merge-file 俱坏 → 本器写全档之冲突、rc 1', rc == 1 and s.startswith('<<<<<<< ours（账并：器坏') and A in s and B in s, e.strip()[:80])
        # ㊱ 全档回放（真 blob·有史方跑：GitHub 片闸 fetch-depth 0；浅仓即 ⚠ 不计）：章-473（81e49e8c1 之二亲）三账、
        #    章-472（322f93409 之二亲）费账——自并之果与手并逐字同；设计之验 f743735c6 对 de2715a62：并成、键无重无失、每行之值取自一侧
        def 史(*a):
            return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, env=_净env())

        def 史文(c, P_):
            return 史('show', '%s:%s' % (c, P_)).stdout.decode('utf-8')
        for 题, cm, 档们 in (('473', '81e49e8c1', ('设定/费账.json', '设定/法用册.json', '设定/方法账.md')), ('472', '322f93409', ('设定/费账.json',))):
            亲 = 史('rev-parse', cm + '^1', cm + '^2').stdout.decode().split()
            if len(亲) != 2:
                print('  ⚠ ㊱ 全档回放 章-%s：史不在（浅仓）——不计' % 题)
                continue
            cb0 = 史('merge-base', *亲).stdout.decode().strip()
            for P_ in 档们:
                O_, A_, B_, M_ = (史文(x, P_) for x in (cb0, 亲[0], 亲[1], cm))
                rc, s, e = 跑(O_, A_, B_, P_)
                T('㊱ 全档回放 章-%s %s（%d KB·%s＋%s）：旧并冲突 → 今自并且与手并 %s 逐字同' % (题, P_.split('/')[-1], len(A_.encode('utf-8')) // 1024, 亲[0][:9], 亲[1][:9], cm),
                  0 < 并文(A_, O_, B_)[1] < 128 and rc == 0 and s == M_, e.strip()[:80])
        if 史('cat-file', '-e', 'de2715a62^{commit}').returncode or 史('cat-file', '-e', 'f743735c6^{commit}').returncode:
            print('  ⚠ ㊱之二 设计之验（f743735c6 对 de2715a62）：史不在——不计')
        else:
            cb0 = 史('merge-base', 'de2715a62', 'f743735c6').stdout.decode().strip()
            O_, A_, B_ = (史文(x, F) for x in (cb0, 'de2715a62', 'f743735c6'))
            rc, s, e = 跑(O_, A_, B_, F)
            a行, b行 = 析值(A_)['行'], 析值(B_)['行']
            r行 = 析值(s)['行'] if rc == 0 else []
            kr = [x['键'] for x in r行]
            T('㊱之二 设计之验 f743735c6 对 de2715a62（全档）：并成、键无重无失、每行之值取自一侧',
              0 < 并文(A_, O_, B_)[1] < 128 and rc == 0 and len(kr) == len(set(kr)) and set(kr) == {x['键'] for x in a行 + b行}
              and all(any(同(x, y) for y in a行 + b行 if y['键'] == x['键']) for x in r行), '%d 行；%s' % (len(kr), e.strip()[:60]))
        # ㊲（W912 环2①）生成之图：驱直调——两侧俱改图 → rc 0、%A 原样（取 ours）、无冲突之标、印一行；册外之他档照旧（不在册 → 留冲突）
        图 = 生成之图[0]
        O图, A图, B图 = '# 图\n\n- 截至第 1 章\n- 件 9\n', '# 图\n\n- 截至第 2 章\n- 件 9\n', '# 图\n\n- 截至第 1 章\n- 件 10\n'
        rc, s, e = 跑(O图, A图, B图, 图)
        rc他, s他, _ = 跑(O图, A图.replace('件 9', '件 8'), B图.replace('件 10', '件 7'), '设定/他之图.md')
        T('㊲ 生成之图（%s）两侧俱改 → 取 ours 原样、rc 0、无冲突之标、印「生成之图·取 ours（⚠ 待下回重生）」；册外之档照旧留冲突' % 图,
          rc == 0 and s == A图 and '<<<<<<<' not in s and '生成之图·取 ours（⚠ 待下回重生）' in e and e.count('账并：') == 1
          and rc他 == 1 and '<<<<<<<' in s他, e.strip()[:80])
        # ㊲之二 真 git merge（临时之仓·.gitattributes 含图之行·装 driver）：两侧俱改图 → 并成、无冲突之标、档＝ours；无其行 → 冲突（对照）
        def 图仓(附):
            d = tempfile.mkdtemp(dir=t)
            g(d, 'init', '-q')
            os.makedirs(os.path.join(d, '设定')); os.makedirs(os.path.join(d, '工具'))
            open(os.path.join(d, 图), 'w', encoding='utf-8').write(O图)
            open(os.path.join(d, '.gitattributes'), 'w', encoding='utf-8').write(('%s merge=账并\n' % 图) if 附 else '')
            shutil.copy(os.path.abspath(__file__), os.path.join(d, '工具', '账并.py'))
            g(d, 'add', '-A'); g(d, 'commit', '-qm', '基')
            g(d, 'checkout', '-qb', '章')
            open(os.path.join(d, 图), 'w', encoding='utf-8').write(B图)
            g(d, 'commit', '-qam', '章之封·图重画')
            g(d, 'checkout', '-q', '主')
            open(os.path.join(d, 图), 'w', encoding='utf-8').write(A图)
            g(d, 'commit', '-qam', '总编辑之治·--随治')
            装(d, 印=False)
            m = g(d, 'merge', '--no-edit', '-m', '并', '章')
            return m, open(os.path.join(d, 图), encoding='utf-8').read(), g(d, 'status', '--porcelain').stdout
        m1, f1, st1 = 图仓(True)
        m0, f0, _ = 图仓(False)
        T('㊲之二 真 git merge：两侧俱改图（封版之重画×总编辑之 --随治）→ 并成、无冲突之标、档＝ours、印见於 git 之 stderr；无其行即冲突（坑63 之由）',
          m1.returncode == 0 and f1 == A图 and '<<<<<<<' not in f1 and not st1.strip() and '生成之图·取 ours' in m1.stderr
          and m0.returncode != 0 and '<<<<<<<' in f0, (m1.stderr.strip().split('\n') or [''])[-1][:80])
        # ㊳ 回放 476／477 之章与治之并（本仓之史·git merge-tree 於 --shared 之临时裸仓；info/attributes 加图之行、driver 指今之器）：
        #    冲突之档集 ⊆ 无其行之集（⛔新冲突）；强基之局（两侧俱改图：第476章之封 × 第477章之封，基＝475 之并）→ 图⛔冲突、其 blob＝ours。浅仓即 ⚠ 不计
        并们 = ('ef9535690', '663d5ae59', 'd3ac58725', '08814d5be')
        if any(史('cat-file', '-e', x + '^{commit}').returncode for x in 并们 + ('02e9a74ff', '092aa5387', '4aa802217')):
            print('  ⚠ ㊳ 回放 476／477：史不在（浅仓）——不计')
        else:
            裸 = os.path.join(t, '回放.git')
            r裸 = subprocess.run(['git', 'clone', '-q', '--bare', '--shared', ROOT, 裸], capture_output=True, env=_净env())
            令 = 'python3 %s %%O %%A %%B %%P %%L' % os.path.abspath(__file__)

            def 树并(*a):
                # 〔W912 并主〕裸仓之 attr 默取 HEAD 之树（git ≥2.42）：本仓 .gitattributes 既含图之行，对照（无其行）即失——钉 attr.tree 为空树，唯认 info/attributes
                r = subprocess.run(['git', '-C', 裸, '-c', 'attr.tree=4b825dc642cb6eb9a060e54bf8d69288fbee4904', '-c', 'core.quotepath=off',
                                    '-c', 'merge.账并.driver=' + 令, 'merge-tree', '--write-tree',
                                    '--name-only'] + list(a), capture_output=True, text=True, env=_净env(), timeout=120)
                行 = (r.stdout or '').split('\n')
                冲 = set()
                for x in 行[1:]:
                    if not x.strip():
                        break
                    冲.add(x.strip())
                return r.returncode, (行[0].strip() if 行 else ''), 冲, r.stderr or ''

            def 加行(有):
                os.makedirs(os.path.join(裸, 'info'), exist_ok=True)
                open(os.path.join(裸, 'info', 'attributes'), 'w', encoding='utf-8').write(('%s merge=账并\n' % 图) if 有 else '')
            诸 = []
            if r裸.returncode == 0:
                for cm in 并们:
                    加行(False)
                    rc0, _, 冲0, _ = 树并(cm + '^1', cm + '^2')
                    加行(True)
                    rc1, _, 冲1, e1 = 树并(cm + '^1', cm + '^2')
                    诸.append((cm, rc0, 冲0, rc1, 冲1))
                加行(False)
                rcq0, _, 冲q0, _ = 树并('--merge-base=02e9a74ff', '092aa5387', '4aa802217')
                加行(True)
                rcq1, 树1, 冲q1, eq1 = 树并('--merge-base=02e9a74ff', '092aa5387', '4aa802217')
                bo = subprocess.run(['git', '-C', 裸, 'rev-parse', '%s:%s' % (树1, 图), '092aa5387:' + 图], capture_output=True, text=True,
                                    env=_净env()).stdout.split()
                坏rc = [x for x in [rc for _, a, _, b, _ in 诸 for rc in (a, b)] + [rcq0, rcq1] if x not in (0, 1)]
            else:
                坏rc = []
            if r裸.returncode == 0 and 坏rc:              # 省取之仓（GitHub 片闸 blob:limit）缺大 blob（阅读器、总圣经…）即 merge-tree 不得——⚠ 不计
                print('  ⚠ ㊳ 回放 476／477：merge-tree 不得（rc %s·省取之仓缺 blob？）——不计' % sorted(set(坏rc)))
            else:
                T('㊳ 回放 476／477 之章与治之并（%s）：加图之行而冲突之档⛔增（%s）；强基之局（476 封×477 封·两侧俱改图）：无其行即图冲突、有其行即图⛔冲突而取 ours'
                  % ('、'.join(并们), '；'.join('%s %d→%d' % (cm[:7], len(a), len(b)) for cm, _, a, _, b in 诸)),
                  r裸.returncode == 0 and len(诸) == len(并们) and all(b <= a and 图 not in b for _, _, a, _, b in 诸)
                  and 图 in 冲q0 and 图 not in 冲q1 and len(bo) == 2 and bo[0] == bo[1] and '生成之图·取 ours' in eq1,
                  '强基：冲 %d→%d' % (len(冲q0), len(冲q1)) if r裸.returncode == 0 else (r裸.stderr or b'')[:80].decode('utf-8', 'replace'))
        # ㉑ .gitattributes 与册同（册中每档俱 merge=账并；attributes 之 账并 俱在册）
        ga = os.path.join(ROOT, '.gitattributes')
        行们 = [l.split() for l in open(ga, encoding='utf-8').read().splitlines() if l.strip() and not l.lstrip().startswith('#')] if os.path.exists(ga) else []
        并者 = {x[0] for x in 行们 if 'merge=%s' % 名 in x[1:]}
        T('㉑ .gitattributes 与册同（册之账＋生成之图）', 并者 == set(册) | set(生成之图),
          '缺 %s｜余 %s' % (sorted((set(册) | set(生成之图)) - 并者), sorted(并者 - set(册) - set(生成之图))))
        # ㉒ 推.py 每推之前装（交、直推）
        try:
            推 = open(os.path.join(ROOT, '工具', '推.py'), encoding='utf-8').read()
        except Exception:
            推 = ''
        体 = {m.group(1): m.group(2) for m in re.finditer(r'^def (交|直推|装并器)\(.*?\n(.*?)(?=^def )', 推, re.M | re.S)}
        T('㉒ 推.py 之 交、直推 俱於推前装 driver（装并器 → 账并.py --装）', all(re.search(r'装并器\(root\)[\s\S]*?push', 体.get(k, '')) for k in ('交', '直推'))
          and "'账并.py'" in 体.get('装并器', '') and "'--装'" in 体.get('装并器', ''))
        # ㉓ gate.yml 备候：git merge 之前装（改 workflows：autopush 拒，总编辑演练後直推）——坑63 之 GitHub 之半；
        #    未推只 ⚠：1119 章界直推为平台之检所拒（⛔绕），⛔以限拦推（拦即拖累写书）
        try:
            gy = open(os.path.join(ROOT, '.github', 'workflows', 'gate.yml'), encoding='utf-8').read()
        except Exception:
            gy = ''
        try:
            import 方法坑账
            末 = 方法坑账.末章(ROOT)
        except Exception:
            末 = 0
        态, 语 = gate之判(gy, 末)
        if 态 == '⚠':
            print('  ⚠ ㉓ ' + 语)
        else:
            T('㉓ ' + 语, 态 == '✓')
        假 = 'bei_hou() {\n  git checkout -q --detach "$B0"\n  %s\n  if ! git merge --no-edit -m x "$T"; then :; fi\n}\n'
        T('㉓之二 gate 之判：未装 → ⚠（不论末章）；装於 merge 之前（|| true）→ ✓；装於 merge 之後 → 红',
          gate之判(假 % ':', 475)[0] == '⚠' and gate之判(假 % ':', 9999)[0] == '⚠'
          and gate之判(假 % 'python3 工具/账并.py --装 || true', 9999)[0] == '✓'
          and gate之判(假.replace('%s\n  if', 'if') + '  python3 工具/账并.py --装 || true\n', 0)[0] == '✗')
    except Exception as e:
        import traceback
        err.append(traceback.format_exc().replace('Traceback (most recent call last)', '崩之迹'))
        T('自测崩', False, str(e)[:120])
    finally:
        shutil.rmtree(t, ignore_errors=True)
    for x in err:
        print(x)
    print('账并·自测 %d/%d %s' % (ok, 共, '全通' if ok == 共 else '未过'))
    return ok == 共


def 主(a):
    if a == ['--自测']:
        return 0 if 自测() else 1
    if a[:1] == ['--装'] and len(a) <= 2:
        return 装(a[1] if len(a) == 2 else os.getcwd())
    if a[:1] == ['--卸'] and len(a) <= 2:
        return 卸(a[1] if len(a) == 2 else os.getcwd())
    if len(a) in (4, 5) and not a[0].startswith('--'):
        try:
            L = int(a[4]) if len(a) == 5 else 7
        except ValueError:
            L = 7
        return 驱安(a[0], a[1], a[2], a[3], L)
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(主(sys.argv[1:]))
