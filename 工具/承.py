#!/usr/bin/env python3
"""承.py——容器重启後，从诸 workflow 之 journal 收第 N 章已成之段，造 造章.js 之 args.承（版本/第N章/_承.json）与包裹（_承.js）。

为何立（1017·397 逮）：容器重启频（397 一章两回：执笔之半、选之半），每回主环手翻 journal、手认 label、
手拼 args.承——393、397、397 三回皆手办，易错（稿与执笔之对、丙稿成而未交者之补）。今一器办毕：
  python3 工具/承.py 397            # 扫诸 journal，收 397 之已成段，写 _承.json 与 _承.js，印续之令
  python3 工具/承.py 397 --印       # 只印所收，⛔写
  python3 工具/承.py 397 --再回写   # 「致命未净」（回写一回後复验仍读误／硬崩）：以 盲读·2、逻辑审·2 之果作 盲、审，⛔承回写——再走一回 回写→盲读→审→记席
  python3 工具/承.py 397 --裁 "总编辑之裁"   # 「致命未净」後总编辑亲治、续记（args.裁 写入 _承.js；旧 _承.json 之裁承之）
  python3 工具/承.py 452 --裁 "已亲治读误：…" --销   # X101①：亲治後单席补盲读已验销 → 造章.js（N≥452）越 盲读·2／逻辑审·2、只跑记席
  python3 工具/承.py 411 --查 甲 版本/第411章/起草_稿三.md   # 查席之器（N≥411·造章.js 补派整席之前派之）：留前席构思之底、量之入账，验盘稿
  python3 工具/承.py 472 --共病已治 "段案拍六已改…、章料已重出"   # X120：选判共病而病只在料之一行——治料（段案或开镜卡改、章料重出，俱在选之後）後销共病、留选与诸稿续合（⛔手改包、⛔毁稿重造）
  python3 工具/承.py 489                # 〔W919·X138〕N≥489 另分因（终态之判）：唯断与已治之器病入 args.补席 单补，拒／不识⛔同令再请；选以下之段末次拒／不识 → rc 3 停而交总编辑；写 版本/第N章/_席之因.json
  python3 工具/承.py 489 --因 执笔·丁 断 "读转录：容器之断"   # 不识→断 之改判（拒⛔改判）
  python3 工具/承.py 489 --二稿 "余席俱拒、整稿二"            # 整稿恰二而无可补（或补後仍二）→ 二稿之录（造式、大师之关以 2 为界；造章.js 二稿择一·照 468）
  python3 工具/承.py 489 --器病已治 "费审之器已治 input_schema"  # 器病之席方入补席
  python3 工具/承.py --自测

1023（坑㊻·续跑之守之审所逮）：
  ①补自带：选未成者承.补 为 true——缺席之执笔由 造章.js 自判补否（宽足⛔补）；旧之「手加补」写不进 _承.js（包裹定死 args）、致不足三之环。
     选已成者⛔补（选不读补来之稿，补即白耗一执笔）。
  ②重造之界：续跑之守放行 args.重造 之新派时记其时（git 公目 承_重造.json）；此前之 journal、稿档与旧 _承.json（只留 重、魂路、须厚）⛔收。
  ③盘稿：journal 无果（他机之 journal、执笔交了稿而败於 StructuredOutput）而 版本/第N章/起草_稿*.md 在（≥200 字节、界後、有【本章亮点】——稿半⛔收）者亦收。
  ④盲读之壳（未交、被截）⛔收——承之即令造章.js 当场停於「盲读未交」、续之复停。

所收（label → 承之键）：执笔·*→诸稿（以 file 认，後者覆前者）；选·行家兼两眼／选·补→选；合稿／合稿·补→草；
盲读／盲读·补→盲；逻辑审·1→审；回写→回写（true）。盲读·2、逻辑审·2、记席⛔收（造章.js 之承不认之，照跑）。
稿档已不在者⛔收（稿被覆或挪走）。
1024（省 token 之审·records③／seats①·failures①）：
  ⑤拆键：N≥411 诸席共一通式，交为 {draft|pick|merge|blind|audit|rewrite: 旧式之果, flaws}——收时拆出其键；缺键、或缺其子式之必填者作未交⛔收
    （必填之表＝造章.js 通式诸子式之 required，负测_造章令.py 对之）；旧式之果原样。逻辑审·1·补 亦收作审。
  ⑥--查：缺稿之执笔补派之前，查席一跑——前席之构思逾 200 字节者抄留 起草_X_构思_前.md（⛔承·⛔mv：造式.py 认甲乙丙之构思、宽足⛔补时原档须在），
    零 token 量其魂、拍表（拍数）、满分之问、①—⑤，记入 版本/第N章/_补前稿账.json；盘稿在、有【本章亮点】、界後、净重过铁底、硬项零者印「稿：{…}」交回。args 之 章／重／魂路 取旧 _承.json，无则须 --重 与 --魂路。
⛔本器只读 journal、只写 版本/第N章/_承.json 与 _承.js；⛔git。
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
诸journal之式 = os.path.expanduser('~/.claude/projects/*/*/subagents/workflows/*/journal.jsonl')
键表 = [(re.compile(r'^执笔·'), '诸稿'), (re.compile(r'^选·(行家兼两眼|补)$'), '选'), (re.compile(r'^合稿(·补)?$'), '草'),
       (re.compile(r'^盲读(·补)?$'), '盲'), (re.compile(r'^逻辑审·1(·补)?$'), '审'), (re.compile(r'^回写$'), '回写')]
# ★1024 通式（N≥411）：承之键 → 通式之键（ASCII·坑⑩）与其子式之必填（照 造章.js 稿式、选式、合式、盲读式、崩式、写式之 required）
通键 = {'诸稿': 'draft', '选': 'pick', '草': 'merge', '盲': 'blind', '审': 'audit', '回写': 'rewrite'}
通之必 = {'draft': ['file', 'beats', 'words', 'soul'], 'pick': ['ranking', 'why', 'fatal', 'leap', 'common_fatal', 'beat_scores'],
         'merge': ['file', 'beats', 'words', 'base', 'gates', 'gates_green', 'ledger', 'recap'],
         'blind': ['understood', 'confused', 'misread', 'want_next', 'why_next', 'happened', 'remember', 'prior'],
         'audit': ['hard', 'soft', 'gate', 'misread'], 'rewrite': ['done'], 'record': ['done', 'left']}


def 式之键(l, 键们):
    return next((k for 式, k in 键们 if 式.search(l)), '')


def 拆(r, k, 通=True):
    """通（N≥411）：通式之果 → 其键之子（缺键、缺必填、交空者 None：作未交）；N≤410 原样。"""
    if not 通:
        return r
    if not isinstance(r, dict):
        return None
    键 = 通键.get(k, k)
    x = r.get(键)
    if not isinstance(x, dict) or any(x.get(f) is None for f in 通之必.get(键, [])):
        return None
    return x


盲未交 = lambda x: (not x) or bool(re.match(r'\s*(未交|未完成|未作答|未答)', str(x.get('happened', '')))) or bool(
    re.search(r'(安全分类器|分类器截|被截停|被拦下|safeguard)', str(x.get('happened', '')) + str(x.get('confused', '')) + str(x.get('why_next', '')), re.I))
盘稿之下限 = 200   # 字节：空档、半档⛔作稿


def _仓目():
    import subprocess
    try:
        p = subprocess.run(['git', 'rev-parse', '--git-common-dir'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        if p:
            return p if os.path.isabs(p) else os.path.join(ROOT, p)
    except Exception:
        pass
    return os.path.join(ROOT, '.git')


def _重造档():
    return os.path.join(_仓目(), '承_重造.json')


def 重造之时(n, 档=None):
    """→ 第 n 章末一回重造之时（秒；无则 0）——此前之 journal 与稿档俱属旧轮。"""
    try:
        return float(json.load(open(档 or _重造档(), encoding='utf-8')).get(str(n), 0))
    except Exception:
        return 0.0


def 记重造(n, 档=None, 时=None, 除席=None, root=None):
    import time
    档 = 档 or _重造档()
    try:
        d = json.load(open(档, encoding='utf-8'))
    except Exception:
        d = {}
    d[str(n)] = 时 if 时 is not None else time.time()
    with open(档, 'w', encoding='utf-8') as o:
        json.dump(d, o)
    try:                                         # 〔W919·X138〕N≥拒後自 且 _席之因.json 在：书「重造」之一笔（料之指·料改否·除席）——崩只 ⚠
        重造之笔(n, 除席, root or ROOT)
    except Exception as e:
        print('  ⚠ 承.记重造：重造之笔未书（%s）' % type(e).__name__)


def 读(路):
    行 = []
    try:
        with open(路, encoding='utf-8', errors='replace') as f:   # 截於半字之 journal ⛔崩（一份坏即诸章之承俱死）
            for l in f:
                try:
                    行.append(json.loads(l))
                except ValueError:
                    pass
    except OSError:
        pass
    return 行


def 首令属(路, 诸id, n):
    """承之 run 无执笔之果（选起）——以其席之令首（agent-<id>.jsonl 首行）有「你是第 n 章的**」认之（造章.js 七席之令俱有）。"""
    记 = '你是第 %d 章的**' % n
    for i in 诸id:
        try:
            with open(os.path.join(os.path.dirname(路), 'agent-%s.jsonl' % i), encoding='utf-8', errors='replace') as f:
                if 记 in f.readline():
                    return True
        except OSError:
            continue
    return False


def 收(n, 诸路, root=ROOT, 再=False, 界=None):
    """诸 journal 依 mtime 升序扫；属第 n 章之 run（有执笔之果其 file 在 版本/第n章/）方收；後者覆前者。
    界（重造之时，缺则取 承_重造.json）以前之 journal 与稿档⛔收；盲读之壳⛔收；journal 无果之盘稿亦收。"""
    界 = 重造之时(n) if 界 is None else 界
    章目 = os.path.join(root, '版本', '第%d章' % n) + os.sep
    承 = {}
    稿 = {}
    来 = []
    键们 = 键表 + ([(re.compile(r'^盲读·2$'), '盲'), (re.compile(r'^逻辑审·2(·补)?$'), '审')] if 再 else [])
    for 路 in sorted(诸路, key=lambda p: os.path.getmtime(p) if os.path.exists(p) else 0):
        try:
            if os.path.getmtime(路) < 界:
                continue
        except OSError:
            continue
        行 = 读(路)
        标 = {d.get('key'): d.get('label', '') for d in 行 if d.get('type') == 'started'}
        果 = [(标.get(d.get('key'), ''), d.get('result')) for d in 行 if d.get('type') == 'result']
        # 通式（N≥411）拆键；回写之果⛔拆（造章.js 不取其果，交了即算办过——缺 rewrite 键而重跑回写即白耗一席）
        果 = [(l, r if 式之键(l, 键们) in ('回写', '') else 拆(r, 式之键(l, 键们), n >= 411)) for l, r in 果]
        # 查席之稿 file 係相对之路（蒙档）——N≥411 依 root 补成绝对：否则其键与下盘稿之 glob 不同，一稿收两回、诸稿重名（怀疑者逮）
        果 = [(l, dict(r, file=os.path.join(root, r['file'])) if n >= 411 and l.startswith('执笔·') and isinstance(r, dict)
               and isinstance(r.get('file'), str) and r['file'] and not os.path.isabs(r['file']) else r) for l, r in 果]
        属 = any(isinstance(r, dict) and str(r.get('file', '')).startswith(章目) for l, r in 果 if l.startswith('执笔·')) \
            or 首令属(路, [d.get('agentId') for d in 行 if d.get('type') == 'started'], n)
        if not 属:
            continue
        来.append(路)
        for l, r in 果:
            for 式, k in 键们:
                if not 式.search(l) or r is None:
                    continue
                if k == '诸稿':
                    if isinstance(r, dict) and r.get('file') and os.path.exists(r['file']):
                        稿[r['file']] = r
                elif k == '回写':
                    承['回写'] = True
                elif k == '盲' and isinstance(r, dict) and 盲未交(r):
                    continue
                elif isinstance(r, dict):
                    承[k] = r
    for f in sorted(glob.glob(os.path.join(章目, '起草_稿*.md'))):
        try:
            if f in 稿 or os.path.getsize(f) < 盘稿之下限 or os.path.getmtime(f) < 界:
                continue
            if '【本章亮点】' not in open(f, encoding='utf-8', errors='replace').read():
                continue                         # 稿半（397「一席稿半」）⛔作已交——亮点与稿同一回写，无之即未写完，交补
            try:
                import 净重对表
                字 = 净重对表.净重(f)
            except Exception:
                字 = len(re.findall(r'[\u4e00-\u9fff]', open(f, encoding='utf-8', errors='replace').read()))
        except OSError:
            continue
        稿[f] = {'file': f, 'words': 字, 'beats': 0, 'soul': '（盘稿：journal 无其果）', '盘': True}
    if 稿:
        承['诸稿'] = list(稿.values())
    if 再:
        承.pop('回写', None)   # 再回写：回写⛔承——造章.js 见 审 有病即再派回写，以 审（逻辑审·2）之读误与硬崩为令
    return 承, 来


# ═══〔W919·X138·法用#拒後不再请〕N≥拒後自：平台之检所拒或因不明之席⛔同令再请——主环以终态分因，唯断与已治之器病单补 ═══
拒後自 = 489      # 门之数一源三书（造章.js、本器、续跑之守.py 之 拒後自 俱 489·负测_造章令 ⑲之七 以正则各取而比）
_名们 = '甲乙丙丁戊己庚'
_稿号 = ['稿一', '稿二', '稿三', '稿四', '稿五', '稿六', '稿七']
_席键 = [(re.compile(r'^执笔·'), 'draft'), (re.compile(r'^选·'), 'pick'), (re.compile(r'^合稿'), 'merge'), (re.compile(r'^盲读'), 'blind'),
        (re.compile(r'^逻辑审·'), 'audit'), (re.compile(r'^回写'), 'rewrite'), (re.compile(r'^记席'), 'record')]
_分类器式 = re.compile(r'(安全分类器|分类器截|被截停|被拦下|safeguard)', re.I)
_无 = object()


def 宽之数(n, 重):
    """同 造章.js 之 宽（N≥475 轻 4、中重 6）。"""
    return ({'轻': 4, '中': 6, '重': 6} if n >= 475 else {'轻': 3, '中': 5, '重': 5 if n >= 407 else 7}).get(重)


def 蒙号(n, 宽, 名):
    """同 造章.js 之 蒙号：稿号[(执笔之序 + N) % 宽]。"""
    return _稿号[(_名们.index(名) + n) % 宽]


def 档之因(f, root=ROOT):
    """一席之 agent 档 → (因, 由)·以终态判（费审.审一 之「终序」；器病／断之式取 费审·⛔另写正则）：
    末回 refusal、或 refusal 紧接 API 错（482 之 拒2→invalid_request）→ 拒；拒过而平台自续、终於断（529、容器之断）→ 不识（⛔自补·总编辑读转录可 --因 席 断）；
    末回 API 错：器病之式 → 器病、断之式 → 断、他 → 不识；无终、末回 tool_use（容器之断）→ 断；末回 end_turn 等而无果（软拒之疑）→ 不识；档不在、读崩 → 不识。"""
    if not f or not os.path.exists(f):
        return '不识', 'agent 档不在（读转录後 --因 席 断 "由"）'
    try:
        import 费审
        r = 费审.审一(f, '', root=root if os.path.exists(os.path.join(root, '设定', '价目.json')) else ROOT)
        序 = r.get('终序') or []
    except Exception as e:
        return '不识', '读崩（%s）' % type(e).__name__
    拒数 = sum(1 for x in 序 if x[0] == 'refusal')
    if 序 and (序[-1][0] == 'refusal' or (序[-1][0] == 'API错' and len(序) >= 2 and 序[-2][0] == 'refusal')):
        return '拒', 'refusal 终（%d 回）' % 拒数
    if 拒数:
        return '不识', '拒 %d 回後平台自续、终於断（⛔自补·总编辑读转录可 --因 席 断 "由"）' % 拒数
    末 = 序[-1] if 序 else None
    if 末 and 末[0] == 'API错':
        文 = ('%s %s' % (末[1], 末[2])).strip()
        if 费审._器病式.search(文):
            return '器病', 文[:120]
        if 费审._断式.search(文):
            return '断', 文[:120]
        return '不识', 文[:120] or 'API错'
    if 末 is None or 末[0] == 'tool_use':
        return '断', '无果无错·末回 %s（容器之断）' % (末[0] if 末 else '无')
    return '不识', '末回 %s 而无果（软拒之疑·⛔自补）' % 末[0]


def 一席之因(d, 行, 果=_无, root=ROOT):
    """席之因一函（坑53：本器分因、续跑之守 ①之二、复盘之同令俱载之）。d＝Run 之目录；行＝其席之 started 之行；
    果＝其 result 之值（无 result 者不传）。→ (因, 由)：因 ∈ 交｜拒｜断｜器病｜不识｜查（「执笔·X·查」⛔入分因：其果只供收盘稿）。"""
    l = str(行.get('label') or '')
    if l.startswith('执笔·') and l.endswith('·查'):
        return '查', ''
    if 果 is not _无 and 果 is not None:
        键 = next((k for 式, k in _席键 if 式.search(l)), '')
        if 键 == 'rewrite' or not 键:
            return '交', ''
        x = 果.get(键) if isinstance(果, dict) else None
        if 键 == 'draft':
            if isinstance(x, dict) and str(x.get('file') or '').strip() and (x.get('words') or 0) > 0:
                return '交', ''
            return '不识', '交而缺键或空（X118）'
        if not isinstance(x, dict) or any(x.get(k) is None for k in 通之必.get(键, [])):
            return '不识', '交而缺键（%s）' % 键
        if 键 == 'blind' and 盲未交(x):
            if _分类器式.search(str(x.get('happened', '')) + str(x.get('confused', '')) + str(x.get('why_next', ''))):
                return '拒', '盲读之壳（安全分类器之截）'
            return '不识', '盲读之壳（未交）'
        return '交', ''
    a = 行.get('agentId') or ''
    return 档之因(os.path.join(d, 'agent-%s.jsonl' % a) if a else None, root)


def 席之诸因(路, root=ROOT):
    """一 journal → [(label, 因, 由, 时序)]（依 started 之序；·查 除外）。"""
    行 = 读(路)
    d = os.path.dirname(路)
    果 = {x.get('key'): x.get('result') for x in 行 if x.get('type') == 'result'}
    出, 见 = [], set()
    for x in 行:
        if x.get('type') != 'started' or x.get('key') in 见:
            continue
        见.add(x.get('key'))
        因, 由 = 一席之因(d, x, 果[x['key']] if x.get('key') in 果 else _无, root)
        if 因 != '查':
            出.append((str(x.get('label') or ''), 因, 由))
    return 出


def 席之因档(n, root=ROOT):
    return os.path.join(root, '版本', '第%d章' % n, '_席之因.json')


def 读席之因(n, root=ROOT):
    """→ 录（dict）｜None（不在）。读崩即抛（续跑之守 拦·⛔猜）。"""
    p = 席之因档(n, root)
    if not os.path.exists(p):
        return None
    return json.load(open(p, encoding='utf-8'))


def 料之指(n, root=ROOT):
    """版本/第N章/_料.md 之 sha256 前十六（⛔mtime：章料重出而文同即「料未改」）；不在 → ''。"""
    import hashlib
    p = os.path.join(root, '版本', '第%d章' % n, '_料.md')
    try:
        return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]
    except OSError:
        return ''


def 二稿之录(n, root=ROOT):
    """库函（坑53·造式、大师之关载之）：N≥拒後自 且 版本/第N章/_席之因.json 之「二稿」带由 ≥4 字 → True；余（含读崩）False。"""
    try:
        if n < 拒後自:
            return False
        录 = 读席之因(n, root) or {}
        由 = ((录.get('二稿') or {}).get('由') or '').strip()
        return len(由) >= 4
    except Exception:
        return False


def 整稿之界(n, root=ROOT):
    """造式.py、大师之关.py 之整稿之界（坑53 一函）：N≥拒後自 且有二稿之录 → 2；余 3。"""
    return 2 if 二稿之录(n, root) else 3


def _改判之用(改判, l):
    for 席, v in (改判 or {}).items():
        if (l == 席 or l.startswith(席 + '·')) and isinstance(v, dict) and v.get('因') == '断':
            return True
    return False


def 分因(n, 来, 承, 重, root=ROOT, 改判=None, 器病已治=''):
    """〔X138②③〕本章诸 journal（来·依时序）之席 → {因: {席: [因, 由]}, 补席: [], 停: '', 整: k, 补过: []}。
    执笔（未交者）：诸次（首派、·补；·查 除外）俱断（或器病而 器病已治 带由）→ 入补席；拒／不识永⛔入。
    选、合稿、盲读、逻辑审·1／·2、回写、记席：末次 拒／不识 而其果未收 → 停（rc 3·⛔写 _承.js）；断者照承（续即再派）。
    改判（--因 席 断 "由"·只改 不识→断）照用。"""
    宽 = 宽之数(n, 重) or 0
    次 = {}
    for 路 in 来:
        for l, 因, 由 in 席之诸因(路, root):
            if 因 == '不识' and _改判之用(改判, l):
                因, 由 = '断', '改判（总编辑读转录）：' + 由
            次.setdefault(l, []).append((因, 由))
    交名 = set()
    for x in 承.get('诸稿') or []:
        for 名 in _名们[:宽]:
            if str(x.get('file', '')).endswith('起草_%s.md' % 蒙号(n, 宽, 名)):
                交名.add(名)
    因, 补席, 补过 = {}, [], []
    for 名 in _名们[:宽]:
        if 名 in 交名:
            continue
        诸 = [(l, c) for l, v in 次.items() if l.startswith('执笔·%s·' % 名) for c in v]
        if not 诸:
            continue
        cs = [c[0] for _, c in 诸]
        首 = next((c for _, c in 诸 if c[0] in ('拒', '不识')), None) or next((c for _, c in 诸 if c[0] == '器病'), None) or 诸[-1][1]
        因['执笔·' + 名] = [首[0], 首[1]]
        if any(l.endswith('·补') for l, _ in 诸):
            补过.append(名)
        if all(c in ('断', '器病') for c in cs) and ('器病' not in cs or len((器病已治 or '').strip()) >= 4) and '交' not in cs:
            补席.append(名)
    停 = ''
    for 段, 式 in (('选', r'^选·'), ('草', r'^合稿'), ('盲', r'^盲读(·补)?$'), ('审', r'^逻辑审·1(·补)?$'), (None, r'^逻辑审·2(·补)?$'),
                   ('回写', r'^回写$'), (None, r'^记席')):
        if 段 and 段 in 承:
            continue
        cs = [(l, c) for l, v in 次.items() if re.search(式, l) for c in v]
        if not cs:
            continue
        l, (c, 由) = cs[-1]
        if c in ('拒', '不识'):
            因[l] = [c, 由]
            停 = 停 or ('%s 末次「%s」（%s）——⛔同令再请（X138③）：停而交总编辑（拒者⛔改判；不识者读其转录後 `python3 工具/承.py %d --因 %s 断 "由"` 方续）'
                      % (l, c, 由, n, l))
        elif c in ('断', '器病'):
            因[l] = [c, 由]
    return {'因': 因, '补席': 补席, '停': 停, '整': len(承.get('诸稿') or []), '补过': 补过}


def 写席之因(n, 果, root=ROOT, 二稿=None, 改判=None, 时=None):
    """写 版本/第N章/_席之因.json（写者唯一：本器）：{章, 因, 补席, 改判, 二稿{由, 时}, 料之指, 重造, 时}；旧录之 改判、二稿、重造 照留。"""
    import time
    时 = 时 or time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    try:
        旧 = 读席之因(n, root) or {}
    except Exception:
        旧 = {}
    录 = {'章': n, '时': 时, '因': 果['因'], '补席': 果['补席'], '改判': dict(旧.get('改判') or {}, **(改判 or {})),
          '料之指': 料之指(n, root), '重造': 旧.get('重造') or []}
    if 二稿 or 旧.get('二稿'):
        录['二稿'] = 二稿 or 旧['二稿']
    p = 席之因档(n, root)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as o:
        json.dump(录, o, ensure_ascii=False, indent=1)
    return 录


def 重造之笔(n, 除席=None, root=ROOT, 时=None):
    """承.记重造 所调（N≥拒後自 且录在）：录之「重造」添一笔 {时, 料之指, 料改否, 除席}——料之比以 sha（⛔mtime）；复盘据之辨骨病之重造（料未改）与料已治而重造。"""
    import time
    if n < 拒後自:
        return None
    录 = 读席之因(n, root)
    if 录 is None:
        return None
    今 = 料之指(n, root)
    笔 = {'时': 时 or time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '料之指': 今, '料改否': bool(今 and 今 != 录.get('料之指')),
         '除席': [x for x in (除席 or []) if isinstance(x, str)]}
    录.setdefault('重造', []).append(笔)
    with open(席之因档(n, root), 'w', encoding='utf-8') as o:
        json.dump(录, o, ensure_ascii=False, indent=1)
    return 笔


def 读误只余(审):
    """X82：审只犯读误（misread 真、hard 空）——再回写无效之形（419：窗外前情之读误，回写逐回只收一环）。"""
    审 = 审 or {}
    return bool(审.get('misread')) and str(审.get('misread')).lower() not in ('false', '否', '0', '') and not 审.get('hard')


def 量构思(文):
    """前席构思之零 token 之量（failures① safeguard⑤）。〔W919·X138④〕承前（亡席之构思入席）永⛔：此量只入账（_补前稿账.json），⛔入任何席之令——负测_造章令 ⑲之四 钉之。"""
    行 = 文.split('\n')
    表 = [l for l in 行 if l.startswith('|')]
    分 = any(re.match(r'^\|\s*-{3}', l) for l in 表)
    魂 = [l for l in 行 if l.startswith('魂')]
    满 = 文.split('满分之问', 1)[1] if '满分之问' in 文 else ''
    return {'字节': len(文.encode('utf-8')), '魂': bool(魂), '进化账所避': '进化账所避' in 文, '满分之问': bool(满),
            '写法数': len(re.findall(r'^\s*[-·]?\s*写法', 满.split('\n## ', 1)[0], re.M)) if 满 else 0,
            '拍表': '拍表' in 文 and 分, '拍数': max(0, len(表) - 2) if 分 else 0,
            '①—⑤': ''.join(c for c in '①②③④⑤' if c in 文)}


def 查(n, 名, 档, root=ROOT, 界=None, 时=None):
    """→ (稿 dict 或 None, 由)。抄留前席之构思、量之入 _补前稿账.json；验盘稿。"""
    import shutil
    import time
    界 = 重造之时(n) if 界 is None else 界
    章目 = os.path.join(root, '版本', '第%d章' % n)
    构 = os.path.join(章目, '起草_%s_构思.md' % 名)
    条 = {'时': 时 if 时 is not None else time.strftime('%m-%d %H:%M:%S'), '名': 名, '稿档': 档}
    魂 = ''
    if os.path.exists(构) and os.path.getsize(构) > 盘稿之下限:
        文 = open(构, encoding='utf-8', errors='replace').read()
        前 = os.path.join(章目, '起草_%s_构思_前.md' % 名)
        k = 2
        while os.path.exists(前):
            前 = os.path.join(章目, '起草_%s_构思_前%d.md' % (名, k))
            k += 1
        shutil.copy2(构, 前)
        条['构思_前'] = os.path.basename(前)
        条['量'] = 量构思(文)
        魂们 = [l for l in 文.split('\n') if l.startswith('魂')]
        魂 = 魂们[-1].split('：', 1)[-1].strip() if 魂们 else ''
    else:
        条['构思_前'] = None
    p = 档 if os.path.isabs(档) else os.path.join(root, 档)
    稿, 由 = None, ''
    if not os.path.exists(p) or os.path.getsize(p) < 盘稿之下限:
        由 = '稿档不在或不足 %d 字节' % 盘稿之下限
    elif os.path.getmtime(p) < 界:
        由 = '稿档在重造之界前（旧轮之稿）'
    elif os.path.exists(os.path.join(章目, '_料.md')) and os.path.getmtime(p) < os.path.getmtime(os.path.join(章目, '_料.md')):
        由 = '稿档早於 _料.md（前轮之稿·料已重出）'   # failures① safeguard①③：只收本轮料出之後之稿（怀疑者补）
    else:
        t = open(p, encoding='utf-8', errors='replace').read()
        if '【本章亮点】' not in t:
            由 = '稿无【本章亮点】（稿半）'
        else:
            try:
                import 净重对表
                字, 红 = 净重对表.稿之量(p)
            except Exception as e:
                字, 红 = 0, {'量不起': str(e)[:60]}
            if 红 or 字 < 2000:
                由 = '净重 %d%s' % (字, ('｜硬项 ' + '、'.join('%s %s' % kv for kv in 红.items())) if 红 else '｜低於铁底 2000')
            else:
                白 = t.split('【本章亮点】')[0].split('\n')
                稿 = {'file': 档, 'beats': sum(1 for l in 白 if l.strip() == '＊') + 1, 'words': 字,
                      'soul': 魂 or '（查席收盘稿：魂见构思）'}
                由 = '盘稿收（净重 %d、硬项零）' % 字
    条['稿'] = '收' if 稿 else '无'
    条['由'] = 由
    账 = os.path.join(章目, '_补前稿账.json')
    try:
        旧 = json.load(open(账, encoding='utf-8'))
    except Exception:
        旧 = []
    旧.append(条)
    os.makedirs(章目, exist_ok=True)
    with open(账, 'w', encoding='utf-8') as o:
        json.dump(旧, o, ensure_ascii=False, indent=1)
    return 稿, 由, 条


def 须厚判(n):
    try:
        import 造式验
        return 造式验.须厚之判(n)[0]
    except Exception:
        return None


def 造(n, 承, 旧=None, 重=None, 魂路=None, 再=False, 裁=None, 补=True, 界=0, 销=False):
    旧 = 旧 or {}
    a = {'章': n, '重': 重 or 旧.get('重'), '魂路': 魂路 or 旧.get('魂路')}
    # ★1020 X40 驳席逮：重启续跑之 args 须带 须厚（旧 _承.json 有则承之；无则照 造式验.须厚之判 现算——与自走之派令同尺）；⛔丢则执笔令、选令之须厚条随之消失
    if 旧.get('须厚') or (n >= 401 and 须厚判(n) is True):
        a['须厚'] = True
    # ★1119 X119：n≥471 之 args 须带段案之带（旧 _承.json 有则承之；无则照 章料.段案之带 现取——与自走之派令同尺）；⛔丢则执笔令之带回落於卡
    if 旧.get('带') or n >= 471:
        import 章料
        带 = 旧.get('带') or 章料.段案之带(n)
        if 带:
            a['带'] = 带
    if not a['重'] or not a['魂路']:
        raise SystemExit('⛔承：无旧 _承.json 可取 重／魂路——须 --重 中 --魂路 物证,回声,不说（照 自走.py 之派令）')
    裁 = 裁 or 旧.get('裁')
    if isinstance(裁, str) and 裁.strip():
        a['裁'] = 裁.strip()                     # 造章.js：致命未净而有裁者越停续记
    if 销:
        if not a.get('裁'):
            raise SystemExit('⛔承 --销：须同带 --裁（亲治读误之一句）——无裁而销，读误无人担')
        a['销'] = True                           # ★1112 X101①：补盲读已销 → 造章.js（N≥452）越 盲读·2／逻辑审·2，只跑记席
    旧承 = 旧.get('承') or {}
    合 = dict(旧承)
    合.pop('补', None)
    if 承.get('诸稿') or 旧承.get('诸稿'):
        by = {x['file']: x for x in (旧承.get('诸稿') or []) if os.path.exists(x.get('file', '')) and os.path.getmtime(x['file']) >= 界}
        by.update({x['file']: x for x in 承.get('诸稿', [])})
        合['诸稿'] = list(by.values())
    for k in ('选', '草', '盲', '审', '回写'):
        if k in 承:
            合[k] = 承[k]
    if isinstance(合.get('盲'), dict) and 盲未交(合['盲']):
        合.pop('盲')                             # 旧 _承.json 所带之盲读之壳⛔承（承之即停於盲读未交）
    if 补 and '选' not in 合:
        合['补'] = True                          # 1023：缺席之执笔由 造章.js 自判补否（宽足⛔补）；选已成⛔补（补来之稿选不读）
    if 再:
        合.pop('回写', None)
    a['承'] = 合
    return a


def 共病治料之验(n, root=None):
    """X120（472 逮）：→ '' 合；否则由。治料之凭须机证：段案之档或开镜卡之改晚於选（_行家评.md 选席所写），章料（_料.md）又晚於其改。"""
    root = root or ROOT
    章目 = os.path.join(root, '版本', '第%d章' % n)
    评 = os.path.join(章目, '_行家评.md')
    料 = os.path.join(章目, '_料.md')
    if not os.path.exists(评):
        return '无 _行家评.md（选未成，何来共病）'
    选时 = os.path.getmtime(评)
    改 = [f for f in sorted(glob.glob(os.path.join(root, '设定', '段案', '[0-9]*-[0-9]*.md'))) + [os.path.join(章目, '_开镜卡.md')]
         if os.path.exists(f) and os.path.getmtime(f) > 选时]
    if not 改:
        return '段案与开镜卡俱未改於选之後——料未治，⛔销共病'
    if not os.path.exists(料) or os.path.getmtime(料) < max(os.path.getmtime(f) for f in 改):
        return '章料未於治料之後重出（python3 工具/章料.py %d）——⛔销共病' % n
    return ''


def 销共病(承, 凭, 时=None):
    """所承之选：common_fatal 移入 共病之裁（总编辑之凭＋时），留 ranking 与诸稿——造章.js 照胜稿续合。"""
    import time
    选 = dict(承.get('选') or {})
    原 = 选.get('common_fatal') or ''
    选['共病之裁'] = '%s 总编辑裁（承.py --共病已治）：原共病「%s」已治於料——%s' % (time.strftime('%m%d', time.gmtime(时)), 原[:120], 凭.strip())
    选['common_fatal'] = ''
    承['选'] = 选
    return 承


def 旧之滤(旧, 旧路, 界):
    """重造前之 _承.json：旧轮之选、草、盲、审、裁、稿⛔承，只留章之设（重、魂路、须厚）——1023 复核逮：只滤 收 而⛔滤旧档，重造之界形同虚设。"""
    if 旧 and 界 and os.path.getmtime(旧路) < 界:
        return {k: 旧[k] for k in ('重', '魂路', '须厚', '带') if k in 旧}
    return 旧


def 包裹(a):
    已 = [k for k in ('选', '草', '盲', '审', '回写') if k in a['承']]
    return ("export const meta = {\n  name: '造章·%d·承',\n  description: '第%d章承已成之段（诸稿 %d%s）续跑',\n"
            "  phases: [{ title: '造' }, { title: '选' }, { title: '合' }, { title: '验' }, { title: '记' }],\n}\n"
            "return await workflow({ scriptPath: '%s' }, %s)\n"
            % (a['章'], a['章'], len(a['承'].get('诸稿', [])), ('、' + '、'.join(已)) if 已 else '',
               os.path.join(ROOT, '工具', '席', '造章.js'), json.dumps(a, ensure_ascii=False)))


def 自测_拒後():
    """〔W919 环3〕分因之局：终态六局、分因八局、·查之局、单席之拦、二稿之录、改判（拒⛔改）、器病须由、料之指、键位（args 顶层）、N≤488 照旧。"""
    import tempfile
    R = []
    u = {'type': 'user', 'message': {'content': '[Workflow harness — computed task] x'}}
    回 = lambda s, i='': {'type': 'assistant', 'message': {'id': 'm' + s + str(i), 'stop_reason': s, 'content': [], 'usage': {'input_tokens': 1, 'output_tokens': 1}}}
    错 = lambda st, 文: {'type': 'assistant', 'isApiErrorMessage': True, 'apiErrorStatus': st, 'message': {'content': [{'type': 'text', 'text': 文}]}}
    拒2 = [u, 回('refusal', 1), 回('refusal', 2), 错('invalid_request', 'API Error: 400 invalid_request')]
    断529 = [u, 回('tool_use'), 错(529, 'API Error: 529 overloaded_error')]
    with tempfile.TemporaryDirectory() as t:
        def 档(名, rows):
            p = os.path.join(t, 名)
            with open(p, 'w', encoding='utf-8') as o:
                o.write('\n'.join(json.dumps(r, ensure_ascii=False) for r in rows) + '\n')
            return p
        终局 = [('拒2→invalid_request', 拒2, '拒'), ('末回 refusal', [u, 回('tool_use'), 回('refusal')], '拒'),
              ('拒1 自续而 529', [u, 回('refusal'), 回('tool_use', 2), 错(529, 'API Error: 529 overloaded_error')], '不识'),
              ('拒1 自续而容器之断', [u, 回('refusal'), 回('tool_use', 2)], '不识'), ('末回 tool_use 无果', [u, 回('tool_use')], '断'),
              ('end_turn 无果', [u, 回('tool_use'), 回('end_turn')], '不识'), ('input_schema 之 400', [u, 错(400, 'API Error: 400 tools.0.input_schema')], '器病'),
              ('首回即死（只令）', [u], '断')]
        坏 = [名 for i, (名, rows, 期) in enumerate(终局) if 档之因(档('e%d.jsonl' % i, rows), t)[0] != 期]
        坏 += ['档不在'] if 档之因(os.path.join(t, '无.jsonl'), t)[0] != '不识' else []
        R.append(('W919·终态之局（拒2 拒、末回拒 拒、拒1自续而529／容器之断 不识、tool_use 断、end_turn 不识、器病、首回即死 断、档不在 不识）%s' % ('｜⛔' + '、'.join(坏) if 坏 else ''), not 坏))
        n = 989
        章目 = os.path.join(t, '版本', '第%d章' % n)
        os.makedirs(章目)
        稿 = lambda 名: '版本/第%d章/起草_%s.md' % (n, 蒙号(n, 6, 名))
        for 名 in '丁戊':
            open(os.path.join(t, 稿(名)), 'w', encoding='utf-8').write('字' * 300 + '【本章亮点】')
        open(os.path.join(章目, '_料.md'), 'w', encoding='utf-8').write('料')
        def run(名, 诸):
            d = os.path.join(t, 'runs', 名)
            os.makedirs(d)
            J = []
            for i, (label, rows, 终) in enumerate(诸):
                a = '%s%02d' % (名, i)
                with open(os.path.join(d, 'agent-%s.jsonl' % a), 'w', encoding='utf-8') as o:
                    o.write('\n'.join(json.dumps(r, ensure_ascii=False) for r in rows) + '\n')
                J.append({'type': 'started', 'key': 'k%d' % i, 'agentId': a, 'label': label})
                if 终 is not None:
                    J.append(dict(终, key='k%d' % i, agentId=a))
            p = os.path.join(d, 'journal.jsonl')
            with open(p, 'w', encoding='utf-8') as o:
                o.write('\n'.join(json.dumps(x, ensure_ascii=False) for x in J) + '\n')
            return p
        交稿 = lambda 名: ('执笔·%s·路' % 名, [u, 回('end_turn')], {'type': 'result', 'result': {'draft': {'file': 稿(名), 'words': 2800, 'beats': 5, 'soul': '魂'}, 'flaws': '无'}})
        败 = {'type': 'failed'}
        壳 = {'understood': False, 'confused': '', 'misread': '', 'want_next': True, 'why_next': '', 'happened': '未交：答被安全分类器截停', 'remember': '', 'prior': ''}
        j1 = run('a', [('执笔·甲·骨', 断529, 败), ('执笔·乙·路', 拒2, 败), ('执笔·丙·路', [u, 回('tool_use')], None), 交稿('丁'), 交稿('戊'),
                       ('执笔·己·路', [u, 回('refusal'), 回('tool_use', 2)], None), ('执笔·甲·查', [u, 回('end_turn')], {'type': 'result', 'result': {'flaws': '无稿'}}),
                       ('执笔·乙·查', [u, 回('end_turn')], {'type': 'result', 'result': {'flaws': '无稿'}})])
        诸 = dict((l, c) for l, c, _ in 席之诸因(j1, t))
        承0 = {'诸稿': [{'file': os.path.join(t, 稿(名))} for 名 in '丁戊']}
        果 = 分因(n, [j1], 承0, '中', t)
        R.append(('W919·分因（甲 529 断·有·查、乙 拒2、丙 未终 断、丁戊 交、己 未终而拒 不识）→ 补席［甲、丙］·「·查」⛔入分因',
                  诸.get('执笔·甲·骨') == '断' and 诸.get('执笔·乙·路') == '拒' and 诸.get('执笔·丙·路') == '断' and 诸.get('执笔·己·路') == '不识'
                  and 诸.get('执笔·丁·路') == '交' and not any(l.endswith('·查') for l in 诸) and 果['补席'] == ['甲', '丙'] and not 果['停']
                  and 果['因']['执笔·乙'][0] == '拒' and 果['因']['执笔·己'][0] == '不识'))
        j2 = run('b', [('执笔·甲·路', [u, 回('end_turn')], {'type': 'result', 'result': {'draft': {'file': '', 'words': 0, 'beats': 0, 'soul': ''}, 'flaws': '无'}}),
                       ('执笔·乙·路', [], 败), ('盲读', [u, 回('end_turn')], {'type': 'result', 'result': {'blind': 壳, 'flaws': '无'}}),
                       ('选·行家兼两眼', 断529, 败)])
        os.remove(os.path.join(t, 'runs', 'b', 'agent-b01.jsonl'))
        诸2 = dict((l, c) for l, c, _ in 席之诸因(j2, t))
        果2 = 分因(n, [j2], {}, '中', t)
        R.append(('W919·分因（交空 不识、档不在 不识、盲读之壳带分类器之字 拒、选 断）→ 单席之拦［盲读］、补席［］',
                  诸2.get('执笔·甲·路') == '不识' and 诸2.get('执笔·乙·路') == '不识' and 诸2.get('盲读') == '拒' and 诸2.get('选·行家兼两眼') == '断'
                  and 果2['补席'] == [] and '盲读' in 果2['停'] and '⛔同令再请' in 果2['停']))
        改 = 分因(n, [j1], 承0, '中', t, {'执笔·己': {'因': '断', '由': '读转录：容器之断'}})
        R.append(('W919·改判（不识→断）照用：己入补席', 改['补席'] == ['甲', '丙', '己']))
        j3 = run('c', [('执笔·甲·路', [u, 错(400, 'API Error: 400 tools.0.input_schema: Property keys')], 败), 交稿('丁'), 交稿('戊')])
        R.append(('W919·器病须由：无 --器病已治 → 补席［］；带由 → ［甲］',
                  分因(n, [j3], 承0, '中', t)['补席'] == [] and 分因(n, [j3], 承0, '中', t, None, '费审之器已治')['补席'] == ['甲']))
        # CLI 之层：拒後之分因（写录、键位、改判拒⛔、二稿）
        def 跑(a, 来, 承=None):
            args = {'章': n, '重': '中', '魂路': ['物证'], '承': dict(承 if 承 is not None else 承0, 补=True)}
            取 = lambda k: a[a.index(k) + 1] if k in a and a.index(k) + 1 < len(a) else None
            import io, contextlib
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = 拒後之分因(n, a, 取, 来, args, root=t)
            return rc, args, buf.getvalue()
        rc, args, _ = 跑([], [j1])
        录 = 读席之因(n, t)
        R.append(('W919·键位：args 顶层带 补席［甲、丙］（⛔入 args.承）；_席之因.json 书 因、补席、料之指（sha256 前十六）',
                  rc == 0 and args.get('补席') == ['甲', '丙'] and '补席' not in args['承'] and '二稿' not in args['承'] and 录['补席'] == ['甲', '丙']
                  and 录['料之指'] == 料之指(n, t) and len(录['料之指']) == 16 and '包裹' not in 录
                  and json.loads(re.search(r"scriptPath: '[^']*' \}, (\{.*\})\)", 包裹(args), re.S).group(1)).get('补席') == ['甲', '丙']))
        rc1, _, o1 = 跑(['--因', '执笔·乙', '断', '读转录所见'], [j1])
        rc2, a2, _ = 跑(['--因', '执笔·己', '断', '读转录：容器之断'], [j1])
        R.append(('W919·--因：拒⛔改判（rc 3）；不识→断 入录之「改判」而入补席', rc1 == 3 and '拒⛔改判' in o1 and rc2 == 0 and a2['补席'] == ['甲', '丙', '己']
                  and '执笔·己' in 读席之因(n, t)['改判']))
        rc3, _, _ = 跑(['--器病已治', '短'], [j3])
        R.append(('W919·--器病已治 由 <4 字 → rc 2', rc3 == 2))
        j4 = run('d', [('执笔·甲·路', 拒2, 败), ('执笔·乙·路', 拒2, 败), ('执笔·丙·路', 拒2, 败), ('执笔·己·路', 拒2, 败), 交稿('丁'), 交稿('戊')])
        os.remove(席之因档(n, t))
        rc4, _, o4 = 跑([], [j4])
        R.append(('W919·整稿二而余席俱拒 → rc 3、点 --二稿；二稿之录未书', rc4 == 3 and '--二稿' in o4 and not 二稿之录(n, t)))
        rc5, a5, _ = 跑(['--二稿', '余席俱拒、整稿二'], [j4])
        R.append(('W919·--二稿 "由" → 二稿之录真、args 顶层 二稿:true', rc5 == 0 and a5.get('二稿') is True and '二稿' not in a5['承'] and 二稿之录(n, t)
                  and not 二稿之录(488, t)))
        rc6, _, _ = 跑(['--二稿', '只一稿亦书'], [j4], {'诸稿': [{'file': os.path.join(t, 稿('丁'))}]})
        R.append(('W919·整稿一 --二稿 → rc 3', rc6 == 3))
        笔 = 重造之笔(n, ['乙'], t)
        open(os.path.join(章目, '_料.md'), 'w', encoding='utf-8').write('料')   # 章料重出而文同（mtime 新）
        笔2 = 重造之笔(n, [], t)
        open(os.path.join(章目, '_料.md'), 'w', encoding='utf-8').write('料已治')
        笔3 = 重造之笔(n, [], t)
        R.append(('W919·重造之笔：料之比以 sha（重出而文同 → 料未改；文改 → 料已改）、除席入笔；N≤488 ⛔书',
                  笔['料改否'] is False and 笔['除席'] == ['乙'] and 笔2['料改否'] is False and 笔3['料改否'] is True
                  and len(读席之因(n, t)['重造']) == 3 and 重造之笔(488, [], t) is None))
        R.append(('W919·门数 拒後自 = 489；N≤488 之 承.py 主流⛔分因（main 之门）', 拒後自 == 489 and 'if n >= 拒後自:' in open(os.path.abspath(__file__), encoding='utf-8').read()))
    return R


def 自测():
    import tempfile
    R = []
    with tempfile.TemporaryDirectory() as t:
        os.makedirs(os.path.join(t, '版本', '第9章'))
        for x in ('稿一', '稿二', '稿三'):
            open(os.path.join(t, '版本', '第9章', '起草_%s.md' % x), 'w').close()
        f = lambda x: os.path.join(t, '版本', '第9章', '起草_%s.md' % x)
        j1, j2, j3 = (os.path.join(t, 'j%d.jsonl' % i) for i in (1, 2, 3))
        def 写(p, 行):
            with open(p, 'w', encoding='utf-8') as o:
                o.write('\n'.join(json.dumps(x, ensure_ascii=False) for x in 行))
        写(j1, [{'type': 'started', 'key': 'a', 'label': '执笔·甲·物证'}, {'type': 'result', 'key': 'a', 'result': {'file': f('稿一'), 'words': 1}},
                {'type': 'started', 'key': 'b', 'label': '执笔·乙·回声'}])
        写(j2, [{'type': 'started', 'key': 'c', 'label': '执笔·乙·补'}, {'type': 'result', 'key': 'c', 'result': {'file': f('稿二'), 'words': 2}},
                {'type': 'started', 'key': 'g', 'label': '执笔·丙·补'}, {'type': 'result', 'key': 'g', 'result': {'file': f('稿四'), 'words': 4}},
                {'type': 'started', 'key': 'd', 'label': '选·行家兼两眼'}, {'type': 'result', 'key': 'd', 'result': {'ranking': ['稿二']}},
                {'type': 'started', 'key': 'e', 'label': '盲读·2'}, {'type': 'result', 'key': 'e', 'result': {'x': 1}},
                {'type': 'started', 'key': 'h', 'label': '回写'}, {'type': 'result', 'key': 'h', 'result': 'ok'}])
        写(j3, [{'type': 'started', 'key': 'z', 'label': '执笔·甲·物证'}, {'type': 'result', 'key': 'z', 'result': {'file': '/别处/版本/第8章/起草_稿一.md'}},
                {'type': 'started', 'key': 'y', 'label': '选·行家兼两眼'}, {'type': 'result', 'key': 'y', 'result': {'ranking': ['他章']}}])
        j4 = os.path.join(t, 'r4', 'journal.jsonl'); os.makedirs(os.path.dirname(j4))
        写(j4, [{'type': 'started', 'key': 'm', 'agentId': 'q1', 'label': '合稿'}, {'type': 'result', 'key': 'm', 'result': {'file': '正文'}}])
        写(os.path.join(t, 'r4', 'agent-q1.jsonl'), [{'message': {'content': '你是第 9 章的**合稿席'}}])
        os.utime(j1, (1, 1)); os.utime(j2, (2, 2)); os.utime(j3, (3, 3)); os.utime(j4, (4, 4))
        承, 来 = 收(9, [j1, j2, j3, j4], root=t, 界=0)
        R.append(('①只收属本章之 run（他章之 j3 ⛔收，其选⛔覆）；承之 run 以令首认章（j4 之合稿收）',
                  来 == [j1, j2, j4] and 承.get('选') == {'ranking': ['稿二']} and 承.get('草') == {'file': '正文'}))
        R.append(('②诸稿以 file 认、稿档不在者⛔收', sorted(x['file'] for x in 承['诸稿']) == [f('稿一'), f('稿二')]))
        R.append(('③盲读·2 ⛔收；回写记 true', '盲' not in 承 and 承.get('回写') is True))
        a = 造(9, 承, 旧={'重': '中', '魂路': ['物证'], '承': {'补': True, '诸稿': [{'file': f('稿三'), 'words': 3}]}})
        R.append(('④并旧 _承.json：旧稿留、旧补去（所收有选⛔补·⑬）、重魂路承旧', len(a['承']['诸稿']) == 3 and '补' not in a['承'] and a['重'] == '中'
                  and '补' not in 造(9, 承, 旧={'重': '中', '魂路': ['物证'], '承': {'补': True}}, 补=False)['承']))
        R.append(('⑤包裹调 造章.js 而带 args', '造章.js' in 包裹(a) and '"章": 9' in 包裹(a)))
        R.append(('⑤之三·旧 _承.json 带「带」者承之（X119）；无旧带之 9 章⛔添', 造(9, 承, 旧={'重': '中', '魂路': ['物证'], '带': '2,900—3,300', '承': {}}).get('带') == '2,900—3,300' and '带' not in 造(9, 承, 旧={'重': '中', '魂路': ['物证'], '承': {}})))
        R.append(('⑤之二·旧 _承.json 带须厚者承之（X40）', 造(9, 承, 旧={'重': '中', '魂路': ['物证'], '须厚': True, '承': {}}).get('须厚') is True and '须厚' not in 造(9, 承, 旧={'重': '中', '魂路': ['物证'], '承': {}})))
        承2, _ = 收(9, [j1, j2, j3, j4], root=t, 再=True, 界=0)
        a2 = 造(9, 承2, 旧={'重': '中', '魂路': ['物证'], '承': {'回写': True}}, 再=True)
        R.append(('⑦再回写：盲读·2 作盲、回写⛔承（新旧俱去）', 承2.get('盲') == {'x': 1} and '回写' not in a2['承']))
        R.append(('⑦之二 X82：只余读误（无硬崩）→ 读误只余；有硬崩、或无读误 → 否', 读误只余({'misread': True, 'hard': [], 'misread_fix': 'x'})
                  and not 读误只余({'misread': True, 'hard': [{'kind': 'x'}]}) and not 读误只余({'misread': False}) and not 读误只余(None)))
        # 1023 坑㊻之审所逮
        j5 = os.path.join(t, 'j5.jsonl')
        写(j5, [{'type': 'started', 'key': 'p', 'label': '执笔·甲·物证'}, {'type': 'result', 'key': 'p', 'result': {'file': f('稿一'), 'words': 9}},
                {'type': 'started', 'key': 'q', 'label': '盲读'}, {'type': 'result', 'key': 'q', 'result': {'happened': '未交：被安全分类器截停'}}])
        os.utime(j5, (5, 5))
        承5, _ = 收(9, [j1, j2, j3, j4, j5], root=t, 界=0)
        R.append(('⑧盲读之壳（未交、被截）⛔收（承之即令造章停於盲读未交）', '盲' not in 承5))
        承6, 来6 = 收(9, [j1, j2, j3, j4, j5], root=t, 界=4.5)
        R.append(('⑨重造之界：界前之 journal（旧轮之选、草）⛔收', 来6 == [j5] and '选' not in 承6 and '草' not in 承6))
        盘 = f('稿五')
        open(盘, 'w', encoding='utf-8').write('第9章 甲\n' + '她' * 300 + '\n【本章亮点】一')
        半 = f('稿六')
        open(半, 'w', encoding='utf-8').write('她' * 400)
        承7, _ = 收(9, [], root=t, 界=0)
        R.append(('⑩盘稿：journal 无果而稿档在（≥200 字节、有亮点）→ 收、量净重；空档（稿三）、稿半（稿六·无亮点）⛔收',
                  [x['file'] for x in 承7.get('诸稿', [])] == [盘] and 承7['诸稿'][0]['words'] == 300))
        os.utime(盘, (3, 3))
        R.append(('⑩之二 盘稿在界前（旧轮）→ ⛔收', not 收(9, [], root=t, 界=4)[0].get('诸稿')))
        a3 = 造(9, 承, 旧={'重': '中', '魂路': ['物证']}, 裁='已亲治读误')
        R.append(('⑪--裁 入 args（造章.js 越致命未净而续记）；旧 _承.json 之裁承之', a3.get('裁') == '已亲治读误'
                  and 造(9, 承, 旧={'重': '中', '魂路': ['物证'], '裁': '旧裁'}).get('裁') == '旧裁' and '裁' not in 造(9, 承, 旧={'重': '中', '魂路': ['物证']})))
        a销 = 造(9, 承, 旧={'重': '中', '魂路': ['物证']}, 裁='已亲治读误', 销=True)
        try:
            造(9, 承, 旧={'重': '中', '魂路': ['物证']}, 销=True); 无裁拒 = False
        except SystemExit:
            无裁拒 = True
        R.append(('⑪之二 X101①：--销 带 --裁 → args.销；无裁而销即拒；不带 --销 ⛔有 销', a销.get('销') is True and 无裁拒 and '销' not in a3))
        R.append(('⑬选已成 → ⛔补（补来之稿选不读，白耗一执笔）；选未成 → 补', '补' not in 造(9, {'选': {'ranking': []}}, 旧={'重': '中', '魂路': ['物证']})['承']
                  and 造(9, {}, 旧={'重': '中', '魂路': ['物证']})['承'].get('补') is True))
        旧稿 = f('稿七')
        open(旧稿, 'w').write('x')
        os.utime(旧稿, (3, 3))
        a8 = 造(9, {}, 旧={'重': '中', '魂路': ['物证'], '承': {'诸稿': [{'file': 旧稿}], '盲': {'happened': '未交'}}}, 界=4)
        R.append(('⑭造：界前之旧稿⛔承、旧 _承.json 之盲读之壳⛔承', not a8['承'].get('诸稿') and '盲' not in a8['承']))
        旧路 = os.path.join(t, '_承.json')
        open(旧路, 'w').write('{}')
        os.utime(旧路, (3, 3))
        旧9 = {'重': '中', '魂路': ['物证'], '裁': '旧裁', '承': {'选': {'common_fatal': '旧之共病'}, '诸稿': [{'file': f('稿一')}]}}
        a9 = 造(9, {}, 旧之滤(旧9, 旧路, 4), 界=4)
        R.append(('⑭之二 重造後之全路（旧之滤→造）：旧 _承.json 之共病之选、裁、稿俱⛔承，重魂路留；界前不滤', '选' not in a9['承']
                  and '裁' not in a9 and not a9['承'].get('诸稿') and a9['重'] == '中' and 旧之滤(旧9, 旧路, 2) is 旧9 and 旧之滤(旧9, 旧路, 0) is 旧9))
        坏 = os.path.join(t, 'r4', 'bad.jsonl')
        open(坏, 'wb').write(json.dumps({'type': 'started', 'key': 'k', 'label': '执笔·甲'}, ensure_ascii=False).encode('utf-8') + b'\n\xe5\x9b')
        try:
            收(9, [坏], root=t, 界=0)
            R.append(('⑮截於半字之 journal ⛔崩（一份坏即诸章之承俱死）', True))
        except Exception:
            R.append(('⑮截於半字之 journal ⛔崩（一份坏即诸章之承俱死）', False))
        # ★1024 通式（N≥411）：拆键
        j6 = os.path.join(t, 'j6.jsonl')
        盲全 = {'understood': True, 'confused': '全懂', 'misread': '无', 'want_next': True, 'why_next': '想', 'happened': '事', 'remember': '记', 'prior': '无'}
        写(j6, [{'type': 'started', 'key': 'a', 'label': '执笔·甲·物证'}, {'type': 'result', 'key': 'a', 'result': {'draft': {'file': f('稿一'), 'beats': 5, 'words': 9, 'soul': '魂'}, 'flaws': '无'}},
                {'type': 'started', 'key': 'b', 'label': '执笔·乙·查'}, {'type': 'result', 'key': 'b', 'result': {'flaws': '无稿'}},
                {'type': 'started', 'key': 'c', 'label': '选·行家兼两眼'}, {'type': 'result', 'key': 'c', 'result': {'pick': {'ranking': ['稿一']}, 'flaws': '缺必填'}},
                {'type': 'started', 'key': 'd', 'label': '选·补'}, {'type': 'result', 'key': 'd', 'result': {'pick': {'ranking': ['稿一'], 'why': '由', 'fatal': [], 'leap': [], 'common_fatal': '', 'beat_scores': '分'}}},
                {'type': 'started', 'key': 'e', 'label': '合稿'}, {'type': 'result', 'key': 'e', 'result': {}},
                {'type': 'started', 'key': 'g', 'label': '盲读'}, {'type': 'result', 'key': 'g', 'result': {'blind': 盲全}},
                {'type': 'started', 'key': 'h', 'label': '逻辑审·1'}, {'type': 'result', 'key': 'h', 'result': {'merge': {'file': 'x'}}},
                {'type': 'started', 'key': 'i', 'label': '逻辑审·1·补'}, {'type': 'result', 'key': 'i', 'result': {'audit': {'hard': [], 'soft': '', 'gate': '闸', 'misread': False}}}])
        os.makedirs(os.path.join(t, '版本', '第411章'))
        f11 = os.path.join(t, '版本', '第411章', '起草_稿一.md')
        open(f11, 'w').close()
        j6文 = open(j6, encoding='utf-8').read().replace(f('稿一'), f11)
        open(j6, 'w', encoding='utf-8').write(j6文)
        承8, 来8 = 收(411, [j6], root=t, 界=0)
        R.append(('⑯通式拆键：稿以 draft 认章、选缺必填⛔收而其补收、合交空⛔收、盲收、审错键⛔收而 逻辑审·1·补 收；只 flaws 之查⛔作稿',
                  来8 == [j6] and [x['file'] for x in 承8.get('诸稿', [])] == [f11] and 承8.get('选', {}).get('why') == '由'
                  and '草' not in 承8 and 承8.get('盲') == 盲全 and 承8.get('审', {}).get('gate') == '闸'))
        R.append(('⑯之二 N≤410 之果原样（拆⛔动旧章）；N≥411 只 flaws、交空、非对象俱作未交', 拆({'ranking': ['稿二']}, '选', False) == {'ranking': ['稿二']}
                  and 拆('ok', '回写', False) == 'ok' and 拆({}, '草', False) == {} and 收(9, [j1, j2], root=t, 界=0)[0].get('选') == {'ranking': ['稿二']}
                  and 拆({'flaws': '无'}, '选') is None and 拆({}, '草') is None and 拆('ok', '回写') is None
                  and 拆({'rewrite': {'done': True}}, '回写') == {'done': True}))
        # ★1024 --查：抄留前席之构思、量之入账；盘稿验之
        构 = os.path.join(t, '版本', '第9章', '起草_甲_构思.md')
        open(构, 'w', encoding='utf-8').write('# 执笔·甲之构思\n魂（物证路）：一物作证\n进化账所避：某\n## ① 一拍\n## 满分之问\n- 写法甲\n- 写法乙\n- 写法丙\n拍表：\n| 拍 | 其事 | 其物 | 最要之一句 |\n|---|---|---|---|\n| 一 | 事 | 物 | 句 |\n| 二 | 事 | 物 | 句 |\n③ 平处\n' + '想' * 80)
        稿查 = f('稿四')
        open(稿查, 'w', encoding='utf-8').write('第九章 试\n' + '她走过去，停了一下。' * 220 + '\n＊\n' + '他没说话。' * 10 + '\n【本章亮点】骨\n')
        档相 = '版本/第9章/起草_稿四.md'
        稿9, 由9, 条9 = 查(9, '甲', 档相, root=t, 界=0, 时='T')
        账9 = json.load(open(os.path.join(t, '版本', '第9章', '_补前稿账.json'), encoding='utf-8'))
        R.append(('⑰--查：前席构思抄留 _前（原档仍在·⛔mv）、量其魂拍表满分之问①—⑤ 入账', 条9.get('构思_前') == '起草_甲_构思_前.md'
                  and os.path.exists(构) and os.path.exists(os.path.join(t, '版本', '第9章', '起草_甲_构思_前.md'))
                  and 账9[-1]['量'] == {'字节': 账9[-1]['量']['字节'], '魂': True, '进化账所避': True, '满分之问': True, '写法数': 3, '拍表': True, '拍数': 2, '①—⑤': '①③'}))
        R.append(('⑰之二 盘稿过铁底、有亮点、硬项零 → 稿（file 照参、beats 以「＊」数、魂取构思）', bool(稿9) and 稿9['file'] == 档相 and 稿9['beats'] == 2
                  and 稿9['words'] >= 2000 and 稿9['soul'] == '一物作证' and 账9[-1]['稿'] == '收'))
        open(稿查, 'w', encoding='utf-8').write('第九章 试\n' + '她' * 300 + '\n')
        稿10, 由10, _ = 查(9, '甲', 档相, root=t, 界=0)
        open(稿查, 'w', encoding='utf-8').write('第九章 试\n' + '她' * 300 + '\n【本章亮点】骨\n')
        稿11, 由11, _ = 查(9, '甲', 档相, root=t, 界=0)
        账10 = json.load(open(os.path.join(t, '版本', '第9章', '_补前稿账.json'), encoding='utf-8'))
        R.append(('⑰之三 稿半（无亮点）、低於铁底 → 无稿；再查之前稿另名（_前2·⛔覆前账）', 稿10 is None and '稿半' in 由10 and 稿11 is None and '铁底' in 由11
                  and len(账10) == 3 and 账10[1]['构思_前'] == '起草_甲_构思_前2.md'))
        R.append(('⑰之四 无构思之席：前稿无、照验其稿', 查(9, '乙', 档相, root=t, 界=0)[2]['构思_前'] is None))
        # ★1024 怀疑者补：查席之稿 file 相对 → 依 root 补绝对，⛔与盘稿之 glob 重收；料重出後之旧稿⛔收
        f12 = os.path.join(t, '版本', '第411章', '起草_稿二.md')
        open(f12, 'w', encoding='utf-8').write('第四一一章 试\n' + '她走过去。' * 100 + '\n【本章亮点】骨\n')
        j7 = os.path.join(t, 'j7.jsonl')
        写(j7, [{'type': 'started', 'key': 'a', 'label': '执笔·乙·查'},
                {'type': 'result', 'key': 'a', 'result': {'draft': {'file': '版本/第411章/起草_稿二.md', 'beats': 2, 'words': 2200, 'soul': '魂'}, 'flaws': '无'}},
                {'type': 'started', 'key': 'b', 'label': '执笔·甲·物证'}, {'type': 'result', 'key': 'b', 'result': {'draft': {'file': f11, 'beats': 5, 'words': 9, 'soul': '魂'}}}])
        旧目 = os.getcwd()
        os.chdir(t)                              # 真跑之 cwd 即仓根：相对之路 exists 为真，旧式即重收
        try:
            承9 = 收(411, [j7], root=t, 界=0)[0]
        finally:
            os.chdir(旧目)
        R.append(('⑯之三 查席之稿（相对之路）补成绝对、一稿只收一回（⛔与盘稿重收）', sorted(x['file'] for x in 承9.get('诸稿', [])) == sorted([f11, f12])))
        open(稿查, 'w', encoding='utf-8').write('第九章 试\n' + '她走过去，停了一下。' * 220 + '\n＊\n' + '他没说话。' * 10 + '\n【本章亮点】骨\n')
        料9 = os.path.join(t, '版本', '第9章', '_料.md')
        open(料9, 'w').write('料')
        os.utime(稿查, (100, 100))
        稿12, 由12, _ = 查(9, '甲', 档相, root=t, 界=0)
        os.remove(料9)
        R.append(('⑰之五 稿档早於 _料.md（料已重出·前轮之稿）→ 无稿', 稿12 is None and '早於' in 由12 and bool(查(9, '甲', 档相, root=t, 界=0)[0])))
        档 = os.path.join(t, '承_重造.json')
        记重造(9, 档=档, 时=123.0)
        R.append(('⑫记重造／重造之时 往返；他章 0', 重造之时(9, 档) == 123.0 and 重造之时(8, 档) == 0))
        # X120：共病已治之验——段案／开镜卡晚於选、章料又晚於其改方合；销後留选之名次、common_fatal 空、裁在
        章9 = os.path.join(t, '版本', '第9章')
        评9 = os.path.join(章9, '_行家评.md'); 卡9 = os.path.join(章9, '_开镜卡.md'); 料9 = os.path.join(章9, '_料.md')
        for x in (评9, 卡9, 料9):
            open(x, 'w').write('x')
        os.utime(评9, (200, 200)); os.utime(卡9, (100, 100)); os.utime(料9, (300, 300))
        r1 = 共病治料之验(9, root=t)
        os.utime(卡9, (250, 250)); os.utime(料9, (240, 240))
        r2 = 共病治料之验(9, root=t)
        os.utime(料9, (260, 260))
        r3 = 共病治料之验(9, root=t)
        销 = 销共病({'选': {'ranking': ['稿一'], 'common_fatal': '三台之图前文零见'}}, '开镜卡拍六已改、章料重出')
        R.append(('⑱X120 共病已治：料未改→拦；改而章料未重出→拦；俱後→合；销後名次留、共病空、裁在',
                  '未改' in r1 and '重出' in r2 and r3 == '' and 销['选']['ranking'] == ['稿一']
                  and 销['选']['common_fatal'] == '' and '三台之图' in 销['选']['共病之裁']))
        for x in (评9, 卡9, 料9):
            os.remove(x)
        try:
            造(9, 承)
            R.append(('⑥无 重／魂路 即停', False))
        except SystemExit:
            R.append(('⑥无 重／魂路 即停', True))
    try:
        R += 自测_拒後()
    except Exception as e:
        import traceback; traceback.print_exc()
        R.append(('W919·拒後之局崩（%s）' % e, False))
    for k, ok in R:
        print('  %s %s' % ('✓' if ok else '✗', k))
    ok = sum(1 for _, o in R if o)
    print('── 负测·承 %d/%d %s ──' % (ok, len(R), '全通' if ok == len(R) else '未过'))
    return all(o for _, o in R)


def 拒後之分因(n, a, 取, 来, args, root=ROOT):
    """→ rc（0 续写 _承.js；2 参误；3 停而交总编辑·⛔写 _承.js）。写 _席之因.json；args 顶层添 补席、二稿（⛔入 args.承·造章.js 所读同键位）。"""
    import time
    try:
        录旧 = 读席之因(n, root) or {}
    except Exception as e:
        print('  ⛔ 分因：_席之因.json 读崩（%s）——⛔猜；查其档後再跑' % type(e).__name__)
        return 3
    改判 = dict(录旧.get('改判') or {})
    器病已治 = (取('--器病已治') or '').strip()
    if '--器病已治' in a and len(器病已治) < 4:
        print('  ⛔ --器病已治 须带由（≥4 字：何器何病、何笔已治）')
        return 2
    if '--因' in a:
        i = a.index('--因')
        席, 判, 由 = (a[i + 1:i + 4] + ['', '', ''])[:3]
        if 判 != '断' or len(由.strip()) < 4 or not 席:
            print('  ⛔ --因 之式：--因 〈席〉 断 "由"（由 ≥4 字·读其转录所见；只许 不识→断）')
            return 2
        果0 = 分因(n, 来, args['承'], args['重'], root, 改判)
        对 = {k: v for k, v in 果0['因'].items() if k == 席 or k.startswith(席 + '·') or 席.startswith(k + '·')}
        if any(v[0] == '拒' for v in 对.values()):
            print('  ⛔ --因：%s 之因係「拒」——拒⛔改判（X138·平台之检所拒⛔同令再请）' % 席)
            return 3
        if not any(v[0] == '不识' for v in 对.values()):
            print('  ⛔ --因：%s 无「不识」之因可改（今之因：%s）' % (席, json.dumps(对, ensure_ascii=False) or '无'))
            return 3
        改判[席] = {'因': '断', '由': 由.strip(), '时': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    果 = 分因(n, 来, args['承'], args['重'], root, 改判, 器病已治)
    print('  分因（X138·法用#拒後不再请）：%s；补席 %s' % ('；'.join('%s %s（%s）' % (k, v[0], v[1][:40]) for k, v in 果['因'].items()) or '无未交之席',
                                              '［%s］' % '、'.join(果['补席'])))
    二稿 = None
    if '--二稿' in a:
        由 = (取('--二稿') or '').strip()
        if len(由) < 4:
            print('  ⛔ --二稿 须带由（≥4 字）')
            return 2
        if 果['整'] == 2 and all(x in 果['补过'] for x in 果['补席']):
            二稿 = {'由': 由, '时': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
        elif 果['整'] <= 1:
            print('  ⛔ --二稿：整稿 %d（≤1）——停而交总编辑' % 果['整'])
            return 3
        else:
            print('  ⛔ --二稿：唯整稿恰二而无可补（补席空或补後仍二）方书——今整稿 %d、补席［%s］' % (果['整'], '、'.join(果['补席'])))
            return 3
    写席之因(n, 果, root, 二稿=二稿, 改判=改判)
    print('  ✓ 写 %s' % os.path.relpath(席之因档(n, root), root))
    if 果['停']:
        print('  ⛔ ' + 果['停'])
        return 3
    args['补席'] = list(果['补席'])
    if 二稿之录(n, root):
        args['二稿'] = True
    if '选' not in args['承']:
        args['承']['诸稿'] = args['承'].get('诸稿') or []   # 门内⛔首派（[] 亦作已承）：缺席唯 args.补席 单补
        if not 果['补席'] and 果['整'] < 3 and not (果['整'] == 2 and args.get('二稿')):
            print('  ⛔ 整稿 %d、可补［%s］——%s' % (果['整'], '、'.join(果['补席']),
                  '整稿恰二而无可补：总编辑定二稿择一即 `python3 工具/承.py %d --二稿 "由"`（照 468）' % n if 果['整'] == 2 and not 果['补席']
                  else '不足二稿而余席拒／不识：停而交总编辑（不识者读转录後 `--因 〈席〉 断 "由"`；无 journal 者新派走 自走之派令）'))
            return 3
    return 0


def main():
    a = sys.argv[1:]
    if '--自测' in a:
        sys.exit(0 if 自测() else 1)
    if not a or not a[0].isdigit():
        print(__doc__)
        sys.exit(2)
    n = int(a[0])
    取 = lambda k: a[a.index(k) + 1] if k in a and a.index(k) + 1 < len(a) else None
    if '--查' in a:
        i = a.index('--查')
        名, 档 = (a[i + 1:i + 3] + ['', ''])[:2]
        if 名 not in '甲乙丙丁戊己庚' or len(名) != 1 or not re.fullmatch(r'版本/第%d章/起草_稿[一二三四五六七]\.md' % n, 档):
            print('无稿：--查 之参不合（须 执笔之名一字 与 版本/第%d章/起草_稿X.md）' % n)
            sys.exit(2)
        稿, 由, 条 = 查(n, 名, 档)
        print('查·第%d章·执笔·%s：前席构思 %s%s' % (n, 名, 条.get('构思_前') or '无（或不足 %d 字节）' % 盘稿之下限,
              ('｜量 ' + json.dumps(条['量'], ensure_ascii=False)) if 条.get('量') else ''))
        print('  入账：版本/第%d章/_补前稿账.json' % n)
        print('稿：' + json.dumps(稿, ensure_ascii=False) if 稿 else '无稿：' + 由)
        return
    再 = '--再回写' in a
    承, 来 = 收(n, glob.glob(诸journal之式), 再=再)
    if 再 and not (承.get('审') or {}).get('misread') and not (承.get('审') or {}).get('hard'):
        print('  ⚠ --再回写：所收之审无读误亦无硬崩——再回写无的，照常续（去 --再回写）即可')
    # ★1105 X82（419 逮：读误只余而再回写二回 $7.36、逐回只收一环）：N≥421 回写一回後只余读误（无硬崩）→ ⛔再回写，总编辑照 misread_fix 原字亲治一句、存版，`--裁` 续记
    if 再 and n >= 421 and 读误只余(承.get('审')):
        print('  ⛔ --再回写（X82）：回写一回後只余读误、无硬崩——⛔再回写；照审之 misread_fix 亲治一句：%s\n'
              '     治毕 `python3 工具/跑轮.py --存 %d "总编辑亲治读误"` → `python3 工具/承.py %d --裁 "已亲治读误：<一句>" --销`（X101／X114：N≥466 器自派 盲读·3＋逻辑审·3 验其销，销方只跑记席、不销即停）'
              % (str((承.get('审') or {}).get('misread_fix') or '（审未交 misread_fix——读 _轮记 之逻辑审·2 节）')[:200], n, n))
        sys.exit(3)
    章目 = os.path.join(ROOT, '版本', '第%d章' % n)
    旧路 = os.path.join(章目, '_承.json')
    旧 = json.load(open(旧路, encoding='utf-8')) if os.path.exists(旧路) else None
    界 = 重造之时(n)
    旧 = 旧之滤(旧, 旧路, 界)
    魂路 = 取('--魂路').split(',') if 取('--魂路') else None
    凭 = 取('--共病已治')
    if '--共病已治' in a:
        if not (承.get('选') or {}).get('common_fatal'):
            print('  ⚠ --共病已治：所收之选无共病——照常承')
        else:
            由 = 共病治料之验(n) if (凭 or '').strip() and len(凭.strip()) >= 8 else '须带治料之凭（≥8 字：改了何档何拍、章料已重出）'
            if 由:
                print('  ⛔ --共病已治：' + 由)
                sys.exit(3)
            承 = 销共病(承, 凭)
    elif (承.get('选') or {}).get('common_fatal') and ((旧 or {}).get('承', {}).get('选') or {}).get('共病之裁') \
            and (旧['承']['选'].get('ranking') == 承['选'].get('ranking')):
        承['选'] = dict(旧['承']['选'])          # 前回已销之共病：同一之选承其裁（⛔复停）
    args = 造(n, 承, 旧, 取('--重'), 魂路, 再=再, 裁=取('--裁'), 补='--不补' not in a, 界=界, 销='--销' in a)
    if n >= 拒後自:                              # 〔W919·X138〕分因：唯断与已治之器病单补（args.补席）、拒／不识⛔同令再请；整稿二而无可补 → --二稿 "由"
        rc = 拒後之分因(n, a, 取, 来, args)
        if rc:
            sys.exit(rc)
    print('承·第%d章：journal %d 份；诸稿 %d（%s）；%s' % (
        n, len(来), len(args['承'].get('诸稿', [])),
        '、'.join('%s·%s字' % (os.path.basename(x['file']), x.get('words')) for x in args['承'].get('诸稿', [])),
        '、'.join(k for k in ('选', '草', '盲', '审', '回写') if k in args['承']) or '其後诸段俱未成'))
    if len(args['承'].get('诸稿', [])) < 3:
        print('  ⚠ 诸稿不足三——包裹已带「补」，造章.js 补派缺席之执笔' if args['承'].get('补') else '  ⛔诸稿不足三而无补——造章.js 必停')
    if (args['承'].get('选') or {}).get('common_fatal'):
        print('  ⛔所承之选有共病（%s）——承之即复停於共病。病只在料之一处：治料（段案／开镜卡改、`章料.py %d` 重出）→ `承.py %d --共病已治 "<治料之凭>"`；病在诸稿之骨方以 args 重造:true 新派' % (str(args['承']['选']['common_fatal'])[:60], n, n))
    if '--印' in a:
        return
    with open(旧路, 'w', encoding='utf-8') as o:
        json.dump(args, o, ensure_ascii=False, indent=1)
    with open(os.path.join(章目, '_承.js'), 'w', encoding='utf-8') as o:
        o.write(包裹(args))
    print('  ✓ 写 %s 与 _承.js\n  ── 续之令 ──\n  Workflow({scriptPath:\'%s\'})' % (旧路, os.path.join(章目, '_承.js')))


if __name__ == '__main__':
    main()
