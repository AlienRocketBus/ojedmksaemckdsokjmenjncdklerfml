#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""续跑之守（1023 立·坑㊻：406 容器重启後以 resumeFromRunId 直续，已交之五执笔连选俱重跑，白耗约 $60）——PreToolUse 钩（Workflow）。

【其由】resumeFromRunId 只回放「自首起连续皆有果」之 agent() 调用：一席失败（journal 只有 failed、无 result），
  其後之调用——已交者亦然——俱当场重跑。406：执笔·丙 撞产出之顶而败（另派「丙·补」），选席跑中容器重启；
  会话以 resumeFromRunId 续，甲乙回放，丙丁戊己庚五席重写（$53.8）、选再跑（$6.3）——七稿当时俱在盘上。
  此坑 393、397 已踩，1016 立 args.承、1017 立 `工具/承.py`、自走之派令亦印「先跑承.py」，然俱凭记性：⛔一闸拦之。
【其法】钩自 stdin 取 PreToolUse 之 JSON，tool_name 为 Workflow 者：
  ①带 resumeFromRunId：找其 journal；按调用之序（首 started 之序），首个无果之席其後若有已成之席，
    而此 run 係造章（有「执笔·」之席）→ 拦，印将重跑之席与续之正路（承.py → _承.js）。
    无果之席在末（如选席跑中而断）→ 放（只重跑那一席）。
    包裹（_承.js）之 run 而续带 args.裁 → 拦（包裹定死 args、外之裁丢，复停於致命未净）：改 `承.py N --裁 '…'` 重写包裹再新派。
  ②新派造章——scriptPath 係 造章.js、或係包裹（_承.js 等，其文以 workflow() 调造章、args 定死於文）、或内联 script 调之——
    其 args 之 承 未盖尽 承.收(N) 所得（已交之稿、选、草、盲、审）→ 拦：无承即「新派即重写之」，有承即「承已旧、重跑承.py」。
    确要毁稿重造者，args 加 重造:true（总编辑之裁）：放行，并记重造之时（承.py 自此⛔收旧轮）。
  ①之 journal 不见、非造章、或属他章者，落到②再判（续错 run 号即全重跑）。
  造章之认（1023 审逮）：席名合 造章 之席（执笔·、选·、合稿、盲读、逻辑审·、回写、记席）——承之 run 无执笔之席亦认。
  ③（1027·开轮六检⑭ 移此）新派造章而其 N 已封——版本/第N章/_十一轮.json 在，或本库有「章-N」之标（本地枝或 origin 之踪）
    → 拦（重跑已封之章即覆其稿、回执与轮记；改旧章走 改单 --施单／还账）。重造:true 亦拦（重造只为未封之章）。
  非造章之 workflow、他器一概放（其无承之路，拦之即停书）。入坏、出错 → 放（本钩只防白耗，⛔挡书）。
  ④（1027·坑⑩㉛·#38 #85）schema 键 ASCII：Workflow 之文（内联 script，或 scriptPath 之档）跑 席法 之 schema 键检（复用 席法.查一，
    并认引号之键）——键不合 ^[A-Za-z0-9_.-]{1,64}$ 即拦（API 400 当场死；主环之内联脚本不经 席法.py·1017 实踩「席法」之键）。
  ⑤（1027·#52 #82 #40①）开件之闸：非 造章／剧情庭／大审／承 之 Workflow（新派；resumeFromRunId 之续免）须 args.W 係
    `设定/工作流账.json` 之件、状「进行」、有预估与停止线——否则拦，印 `工作流账.py --开` 之令（开法四问、方案、坑之检）。
    〔1120 W911 环6·坑65〕预审在开前：args.预审 为 true、件未在工作流账（未开）而 设定/方案/<W>.md 在 → 放（已开、已成之件带旗照旧判；预审 Run 只攻·其费 `费审 --记 <Run> "W·预审"`；
    --开 深验其 Run 之档）——旧则开件须先过方案之验、方案之验又须预审之 Run，钩载之坐即互锁。
用法：钩自 stdin 取 JSON；`python3 工具/续跑之守.py --自测`
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import os, sys, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
诸journal之根 = os.environ.get('ZM_JOURNAL_ROOT') or os.path.expanduser('~/.claude/projects')   # 环境之注只供自测之子进程


def journal之路(run, 根=None):
    """→ run 之 journal 之路（无则 None）；run 只认 wf_ 之号（⛔路径之注）。"""
    if not re.fullmatch(r'wf_[A-Za-z0-9-]{4,}', str(run or '')):
        return None
    for p in glob.glob(os.path.join(根 or 诸journal之根, '*', '*', 'subagents', 'workflows', run, 'journal.jsonl')):
        return p
    return None


def 读(路):
    行 = []
    try:
        with open(路, encoding='utf-8', errors='replace') as f:
            for l in f:
                try:
                    行.append(json.loads(l))
                except ValueError:
                    pass
    except OSError:
        pass
    return 行


造章之席 = re.compile(r'^(执笔·|选·(行家兼两眼|补)$|合稿(·补)?$|盲读(·2|·补)?$|逻辑审·[12](·补)?$|回写$|记席(·补)?$)')   # 1024：逻辑审·1·补／·2·补（N≥411 交空即补）


def 令首之章(路, 行):
    """→ journal 诸席之令首（agent-<id>.jsonl 首行）之「你是第 N 章的**」之 N（无则 None）。"""
    for d in 行:
        if d.get('type') != 'started' or not d.get('agentId'):
            continue
        try:
            with open(os.path.join(os.path.dirname(路), 'agent-%s.jsonl' % d['agentId']), encoding='utf-8', errors='replace') as f:
                m = re.search(r'你是第 (\d+) 章的\*\*', f.readline())
        except OSError:
            continue
        if m:
            return int(m.group(1))
    return None


def 续之判(行):
    """→ (将重跑之已成席之名［］, 首个无果之席名, 章号或 None, 係造章否)：照 resumeFromRunId 之回放（首个无果之调用起俱重跑）。"""
    序, 名, 成 = [], {}, set()
    章 = None
    for d in 行:
        t, k = d.get('type'), d.get('key')
        if t == 'started' and k and k not in 名:
            序.append(k)
            名[k] = d.get('label') or k[:12]
        elif t == 'result' and k and d.get('result') is not None:
            成.add(k)
            r = d.get('result')
            if isinstance(r, dict) and isinstance(r.get('draft'), dict):
                r = r['draft']                   # ★1024 通式（N≥411）：执笔之交为 {draft: {file…}, flaws}——拆键而认章
            m = re.search(r'版本/第(\d+)章/', str(r.get('file', '')) if isinstance(r, dict) else '')
            if m and 章 is None:
                章 = int(m.group(1))
    造章 = any(造章之席.match(str(v)) for v in 名.values())
    for i, k in enumerate(序):
        if k not in 成:
            return [名[x] for x in 序[i + 1:] if x in 成], 名[k], 章, 造章
    return [], None, 章, 造章


# ═══〔W919·X138·法用#拒後不再请〕N≥拒後自：拒／不识之席⛔同令再请——续跑之守 ①之二（resume 之诸无果之席）、②之二（补席之越、二稿无录、一稿无录〔W924〕）、③（重造之除席）═══
拒後自 = 489      # 门之数一源三书（造章.js、承.py、本器·负测_造章令 ⑲之七 钉其同）


def 续之诸缺(行):
    """→ resumeFromRunId 将重跑之诸无果之席（首缺起凡 started 而无 result 者·「执笔·X·查」除外）之 started 行——⛔只判首缺（首缺起俱重跑）。"""
    序, 成 = [], set()
    for d in 行:
        t, k = d.get('type'), d.get('key')
        if t == 'started' and k and k not in [x.get('key') for x in 序]:
            序.append(d)
        elif t == 'result' and k and d.get('result') is not None:
            成.add(k)
    首 = next((i for i, d in enumerate(序) if d.get('key') not in 成), None)
    if 首 is None:
        return []
    return [d for d in 序[首:] if d.get('key') not in 成 and not (str(d.get('label') or '').startswith('执笔·') and str(d.get('label') or '').endswith('·查'))]


def 拒後续之判(p, 行, n, root=None):
    """①之二：→ 拦之由（'' 放）。诸无果之席各以 承.一席之因 判（坑53 一函）——任一 拒／不识 即拦；俱断方放（封「造章之续、无缺即放」之後门）。"""
    import 承 as _承
    d = os.path.dirname(p)
    判们 = [(str(x.get('label') or ''),) + tuple(_承.一席之因(d, x, root=root or ROOT)) for x in 续之诸缺(行)]
    拒 = [(l, 由) for l, 因, 由 in 判们 if 因 == '拒']
    疑 = [(l, 由) for l, 因, 由 in 判们 if 因 == '不识']
    if not (拒 or 疑):
        return ''
    辞 = ['⛔续跑之守（X138·法用#拒後不再请）：此续将同令重跑无果之席 %s。' % '、'.join('%s（%s）' % (l, 因) for l, 因, _ in 判们)]
    if 拒:
        辞.append('拒（%s）——拒後不再请：改走 python3 工具/承.py %d 分因（拒⛔再请；断与已治之器病单补）→ 其 _承.js 新派（⛔resume）。' % ('、'.join(l for l, _ in 拒), n))
    if 疑:
        辞.append('因不明（%s）：读其转录後 python3 工具/承.py %d --因 〈席〉 断 "由"，或 python3 工具/承.py %d 分因。' % ('；'.join('%s：%s' % (l, 由[:60]) for l, 由 in 疑), n, n))
    return ''.join(辞)


def _来之默(n, 根=None, root=None):
    """第 n 章之诸 journal（承.收 之 来·界 0：不限重造之界——前轮之拒席亦在）。"""
    import 承 as _承
    return _承.收(n, glob.glob(os.path.join(根 or 诸journal之根, '*', '*', 'subagents', 'workflows', '*', 'journal.jsonl')),
                 root=root or ROOT, 界=0)[1]


def 拒後派之判(x, n, root=None, 来=None):
    """②之二、③：新派造章（N≥拒後自）→ (拦之由 '', 除席)。录读崩 → 拦（⛔猜）；唯只带稿（无补席、二稿、一稿、重造、首派）→ 只 ⚠ 而放。
    〔W924〕args.一稿（造章.js 门 1·一稿径用）而录无「一稿」之录（承.一稿之录：由 ≥4 字、晚於末次重造）→ 拦（照二稿无录）。
    〔W919 落地之查·病一二〕首派（args.承 无「诸稿」之列：造章.js 诸执笔首派）与重造俱求 S＝承.拒之执笔（录之因、因之史、历次除席 ∪ 诸 journal 现算）：
    首派而 S 非空 → 拦（走 承.py N 分因）；重造而 S 不尽在 除席 → 拦。来(n) → 诸 journal（自测注之）；取崩只 ⚠（录在照判）。"""
    import 承 as _承
    root = root or ROOT
    补席 = x.get('补席') if isinstance(x.get('补席'), list) else []
    二稿 = x.get('二稿') is True
    一稿 = x.get('一稿') is True
    重造 = x.get('重造') is True
    承x = x.get('承')
    首派 = not (isinstance(承x, dict) and (isinstance(承x.get('诸稿'), list) or x.get('_字面')))
    带稿 = isinstance(承x, dict) and isinstance(承x.get('诸稿'), list) and not 重造      # 〔W919 乙批〕带承之诸稿而续（选／合或重派）
    if not (补席 or 二稿 or 一稿 or 重造 or 首派 or 带稿):
        return '', []
    try:
        录 = _承.读席之因(n, root)
    except Exception as e:
        if not (补席 or 二稿 or 一稿 or 重造 or 首派):      # 〔W919 乙·查之治 病三〕只带稿（选合同稿之拒·新拦）：录读崩只 ⚠、略其判而放（新拦崩⛔拦）
            print('  ⚠ 续跑之守·选合同稿之拒：第%d章 _席之因.json 读崩（%s）——略此判而放' % (n, type(e).__name__), file=sys.stderr)
            return '', []
        return ('⛔续跑之守（X138）：第%d章 _席之因.json 读崩（%s）——⛔猜；查其档、重跑 python3 工具/承.py %d 分因' % (n, type(e).__name__, n)), []
    if 补席:
        许 = set((录 or {}).get('补席') or [])
        越 = [z for z in 补席 if z not in 许]
        if 越:
            return ('⛔续跑之守（X138·补席之越）：args.补席 之 %s 不在 版本/第%d章/_席之因.json 之补席（%s）——补席唯 承.py %d 分因所书（断与已治之器病）；拒／不识⛔同令再请' % (
                '、'.join(map(str, 越)), n, '、'.join(sorted(许)) or '无录', n)), []
    if 二稿 and not _承.二稿之录(n, root):
        return ('⛔续跑之守（X138·二稿无录）：args.二稿 而 版本/第%d章/_席之因.json 无「二稿」之录——总编辑定二稿择一即 python3 工具/承.py %d --二稿 "由"（照 468）' % (n, n)), []
    if 一稿 and not _承.一稿之录(n, root):
        return ('⛔续跑之守（X138·一稿无录）：args.一稿 而 版本/第%d章/_席之因.json 无「一稿」之录（或其时早於末次重造）——'
                '总编辑裁一稿径用即 python3 工具/承.py %d --一稿 "由"（整稿恰一而无可补·只用平台已交之稿·⛔另派执笔）' % (n, n)), []
    if 带稿:
        try:                             # 〔W919 乙批·落地之记之留待（总编辑裁）〕选／合之重派：诸稿之指须异於被拒之时（重造即异）——同即拦；崩只 ⚠
            try:
                诸来 = (来 or (lambda k: _来之默(k, root=root)))(n)
            except Exception as e:
                诸来 = []
                print('  ⚠ 续跑之守·选合同稿之拒：诸 journal 取不得（%s）——只凭录判' % type(e).__name__, file=sys.stderr)
            同 = _承.选合同稿之拒(n, 承x, root, 录, 诸来)
        except Exception as e:
            同 = []
            print('  ⚠ 续跑之守·选合同稿之拒 崩（%s）——照旧判' % type(e).__name__, file=sys.stderr)
        if 同:
            return ('⛔续跑之守（X138·选合之重派）：第%d章 %s——选／合之令只引诸稿之路，诸稿未重造而重派其席＝同令再请。'
                    '总编辑之路：重造（args 加 重造:true 与 除席·诸稿重出、其指即异）；因不明者读其转录後 python3 工具/承.py %d --因 〈席〉 断 "由"（拒⛔改判）'
                    % (n, '；'.join(由 for _, 由 in 同), n)), []
    if 重造 or 首派:
        诸来 = []
        try:
            诸来 = (来 or (lambda k: _来之默(k, root=root)))(n)
        except Exception as e:
            print('  ⚠ 续跑之守·拒之执笔：诸 journal 取不得（%s）——只凭录判' % type(e).__name__, file=sys.stderr)
        S = _承.拒之执笔(n, 诸来, root, 录)
        除 = [z for z in (x.get('除席') if isinstance(x.get('除席'), list) else []) if isinstance(z, str)] if 重造 else []
        缺 = [z for z in S if z not in 除]
        if 缺 and 重造:
            今 = _承.料之指(n, root)
            别 = '料不在' if not 今 else '料之改否不明（无录·以 journal 现算）' if 录 is None else '料未改（骨病之重造）' if 今 == 录.get('料之指') else '料已治而重造'
            return ('⛔续跑之守（X138·重造之除席）：第%d章有拒／不识之执笔（%s·录之因、因之史、前回除席与诸 journal 之并）——重造须尽除其席（执笔令只引 _料.md 之路·料改而令之文仍逐字同＝同令再请）：'
                    'args 加 `除席: %s`（%s）' % (n, '、'.join(S), json.dumps(S, ensure_ascii=False), 别)), []
        if 缺:
            return ('⛔续跑之守（X138·首派之拒席）：第%d章前 Run 有拒／不识之执笔（%s）——新派造章（args.承 无诸稿）即以原令首派之＝同令再请。'
                    '改走 python3 工具/承.py %d 分因（拒／不识⛔再请；断与已治之器病单补）→ 其 _承.js；确要毁稿重造：args 加 重造:true 与 `除席: %s`（总编辑之裁）'
                    % (n, '、'.join(缺), n, json.dumps(S, ensure_ascii=False))), []
        return '', 除
    return '', []


def _参(入):
    参 = 入.get('tool_input') or {}
    a = 参.get('args')
    if isinstance(a, str):
        try:
            a = json.loads(a)
        except ValueError:
            a = {}
    return 参, (a if isinstance(a, dict) else {})


包裹之式 = re.compile(r"workflow\(\s*\{\s*scriptPath:\s*['\"][^'\"]*造章\.js['\"]\s*\}\s*,\s*(\{.*\})\s*\)", re.S)
转传之式 = re.compile(r"造章\.js[\x27\x22]\s*\}\s*,\s*args\s*\)")


def 派造章之参(参, a):
    """→ 新派造章之 args（含 章）；非新派造章、或认不出者 None。
    scriptPath 係 造章.js → tool_input.args；係他档而其文以 workflow() 调造章（_承.js 等包裹）→ 其文中定死之 args；
    内联 script 调造章 → 文中之字面 args，或其转传之 tool_input.args。"""
    sp = str(参.get('scriptPath') or '')
    if sp:
        if os.path.basename(sp) == '造章.js':
            return a
        try:
            p = sp if os.path.isabs(sp) else os.path.join(ROOT, sp)
            if os.path.getsize(p) > 512 * 1024:
                return None
            文 = open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            return None
    else:
        文 = str(参.get('script') or '')
    if '造章.js' not in 文:
        return None
    m = 包裹之式.search(文)
    if m:
        try:
            return json.loads(m.group(1))
        except ValueError:
            pass
        if 转传之式.search(文):
            return a
        字 = m.group(1)
        n = re.search(r'["\']?章["\']?\s*:\s*(\d+)', 字)
        if not n:
            return None
        return {'章': int(n.group(1)), '重造': bool(re.search(r'["\']?重造["\']?\s*:\s*true', 字)),
                '承': {'?': 1} if re.search(r'["\']?承["\']?\s*:', 字) else None, '_字面': True}
    if 转传之式.search(文):
        return a
    return None


def _令(n, a, 末=''):
    """承.py 之全令（带 重、魂路、裁——旧只印 `承.py N`，无旧 _承.json 时当场 SystemExit）。"""
    c = 'python3 工具/承.py %s' % n
    if a.get('重'):
        c += ' --重 %s' % a['重']
    if isinstance(a.get('魂路'), list) and a['魂路']:
        c += ' --魂路 %s' % ','.join(str(x) for x in a['魂路'])
    if isinstance(a.get('裁'), str) and a['裁'].strip():
        c += " --裁 '%s'" % a['裁'].strip().replace("'", '’')
    return '`%s`%s' % (c, 末)


def 已封之凭(n, root=None):
    """③·⑭之移（1027）：第 n 章已封之凭——版本/第n章/_十一轮.json 在，或本库有「章-n」之标。→ 凭之语，未封 ''。
    只读本地（档与 refs，⛔连网）：钩每派一调，零 token、毫秒之费。"""
    r = root or ROOT
    if os.path.exists(os.path.join(r, '版本', '第%d章' % n, '_十一轮.json')):
        return '版本/第%d章/_十一轮.json 在' % n
    import subprocess
    for ref in ('refs/heads/章-%d' % n, 'refs/remotes/origin/章-%d' % n):
        try:
            if subprocess.run(['git', 'rev-parse', '--verify', '--quiet', ref], cwd=r,
                              capture_output=True, timeout=10).returncode == 0:
                return '有「章-%d」之标（%s）' % (n, ref)
        except Exception:
            pass
    return ''


def _文(参, root=None):
    """Workflow 之文：内联 script，或 scriptPath 之档（逾 512KB 或读不得作 ''）。"""
    sp = str(参.get('scriptPath') or '')
    if not sp:
        return str(参.get('script') or '')
    try:
        p = sp if os.path.isabs(sp) else os.path.join(root or ROOT, sp)
        if os.path.getsize(p) > 512 * 1024:
            return ''
        return open(p, encoding='utf-8', errors='replace').read()
    except OSError:
        return ''


_引键式 = re.compile(r'''(?:^|[{,\s])(['"])([^'"\n]{1,80})\1\s*:\s*\{\s*['"]?type['"]?\s*:''')
_合键 = re.compile(r'[A-Za-z0-9_.\-]{1,64}')
_属性起 = re.compile(r'''(?:^|[^\w$])(['"]?)properties\1\s*:\s*\{''')


def _属性之键(文):
    """诸 `properties: {…}`（或 JSON 之 "properties": {…}）一层之键（复核逮：旧只认「键: {type:」之紧接形——
    JSON 之式 `"席法": {"type": "string"}`、description 在 type 之前者俱漏）。串里之 ; , : { } ⛔认作结构。"""
    出 = []
    for m in _属性起.finditer(文):
        i, 深, 期 = m.end(), 1, True
        while i < len(文) and 深 > 0:
            ch = 文[i]
            if ch in '\'"`':
                j = i + 1
                while j < len(文) and 文[j] != ch:
                    j += 2 if 文[j] == '\\' else 1
                if 深 == 1 and 期 and re.match(r'\s*:', 文[j + 1:j + 40]):
                    出.append(文[i + 1:j]); 期 = False
                i = j + 1
                continue
            if ch in '{[(':
                深 += 1
            elif ch in '}])':
                深 -= 1
            elif ch == ',' and 深 == 1:
                期 = True
            elif 深 == 1 and 期 and not ch.isspace():
                mm = re.match(r'''([^\s:,{}\[\]()'"`]+)\s*:''', 文[i:i + 120])
                期 = False
                if mm:
                    出.append(mm.group(1)); i += mm.end()
                    continue
            i += 1
    return 出


def schema之坏(文):
    """④坑⑩㉛：schema 键非 ASCII 者（复用 席法.查一 之甲路，并认引号之键、JSON 之式、properties 一层诸键）→ [键]。"""
    if not 文 or 'type' not in 文:
        return []
    try:
        import 席法
        坏 = list(席法.查一(文)[0])
    except Exception:
        坏 = [k for k in re.findall(r'([^\s:,{}\'"`]+)\s*:\s*\{\s*type:', 文) if not _合键.fullmatch(k)]
    坏 += [m.group(2) for m in _引键式.finditer(文) if not _合键.fullmatch(m.group(2))]
    坏 += [k for k in _属性之键(文) if not _合键.fullmatch(k)]
    return sorted(set(坏))


免W之器 = ('造章.js', '剧情庭.js', '大审.js')
_包式 = re.compile(r'''scriptPath\s*:\s*['"][^'"]*(?:造章|剧情庭|大审)\.js['"]''')


def 免W(参, 文):
    """⑤：写书之流（造章、剧情庭、大审）与承之包裹（_承*.js、内联 workflow() 调其一）免开件之闸。"""
    sp = os.path.basename(str(参.get('scriptPath') or ''))
    return sp in 免W之器 or sp.startswith('_承') or bool(_包式.search(文 or ''))


def 开件之判(a, root=None):
    """⑤：args.W 须係 工作流账之件、状「进行」、有预估与停止线 → 拦之由（无事 ''）。"""
    W = str(a.get('W') or a.get('w') or '').strip()
    令 = ('python3 工具/工作流账.py --开 %s <时限·时> "<停止线>" "<换法>" "<有效之据·含坑之检>" "<预估·时与 $>"'
         '（方案 设定/方案/%s.md 先过 `python3 工具/方案.py --验 %s`；W913 起之 W9xx 先预审：args: {W, 预审: true} 派攻者 ≥2 →'
         ' 费审 --记 <Run> "%s·预审" → 方案.py --预审 %s <Run> 补其节）' % ((W or 'W<k>',) * 5))
    if not W:
        return ('⛔续跑之守（开件之闸·1027）：非写书之 Workflow 须带 args.W（工作流账之件）——先开件：%s；再以 args: {W: "W<k>", …} 派之。' % 令)
    try:
        账 = json.load(open(os.path.join(root or ROOT, '设定', '工作流账.json'), encoding='utf-8'))
    except Exception as e:
        return '⛔续跑之守（开件之闸）：工作流账读不出（%s）——先治账再派' % e
    件 = next((x for x in 账.get('件') or [] if x.get('id') == W), None)
    if not 件 and a.get('预审') is True and re.fullmatch(r'W\d+', W) and os.path.isfile(os.path.join(root or ROOT, '设定', '方案', W + '.md')):
        return ''                    # 〔W911 环6〕预审在开前（件未开·方案在·只攻）——⛔互锁；已开、已成之件带旗⛔放（照下之旧判）
    if not 件:
        return '⛔续跑之守（开件之闸·1027）：%s 不在工作流账——先开件：%s' % (W, 令)
    if 件.get('状态') != '进行':
        return '⛔续跑之守（开件之闸·1027）：%s 之状「%s」非「进行」——先开件：%s' % (W, 件.get('状态'), 令)
    缺 = [k for k in ('预估', '停止线') if not str(件.get(k) or '').strip()]
    if 缺:
        return '⛔续跑之守（开件之闸·1027）：%s 缺%s（开法四问：估、停止线）——重开：%s' % (W, '、'.join(缺), 令)
    return ''


def 判(入, 根=None, root=None, 收=None, 记=None, 来=None):
    """→ (拦否, 由)。收(n) → 承.收 之果；记(n) → 记重造；来(n) → 第 n 章之诸 journal（拒之执笔之现算·自测注之）。"""
    if (入.get('tool_name') or '') != 'Workflow':
        return False, ''
    参, a = _参(入)
    文 = _文(参, root)
    坏键 = schema之坏(文)
    if 坏键:
        return True, ('⛔续跑之守（坑⑩㉛·schema 键 ASCII）：键「%s」非 ASCII——API 只收 ^[A-Za-z0-9_.-]{1,64}$，派即 400 而死。'
                      '键改英文（值与令仍用汉字），再派。' % '」「'.join(坏键[:5]))
    run = 参.get('resumeFromRunId')
    if not run and not 免W(参, 文):
        由 = 开件之判(a, root)
        if 由:
            return True, 由
    if run:
        p = journal之路(run, 根)
        if p:
            行 = 读(p)
            将重, 首缺, 章, 造章 = 续之判(行)
            if 造章:
                章 = 章 or 令首之章(p, 行) or (a.get('章') if isinstance(a.get('章'), int) else None)
                if 将重:
                    n = str(章) if 章 else 'N'
                    return True, ('⛔续跑之守（坑㊻·406 白耗约 $60）：resumeFromRunId 只回放首个无果之席（%s）以前者——其後已成之 %d 席（%s）将俱重跑。'
                                  '改走承之路：%s（收诸 journal 已成之段与盘稿、写 版本/第%s章/_承.js，补自带）→ '
                                  "Workflow({scriptPath:'%s'})。" % (首缺, len(将重), '、'.join(将重), _令(n, a), n,
                                                                     os.path.join(root or ROOT, '版本', '第%s章' % n, '_承.js')))
                if 章 and 章 >= 拒後自:          # 〔W919 环4·①之二〕诸无果之席之因（⛔只判首缺）
                    try:
                        由 = 拒後续之判(p, 行, 章, root)
                    except Exception as e:
                        由 = ''
                        print('  ⚠ 续跑之守·拒後续之判 崩（%s）——照旧判' % type(e).__name__, file=sys.stderr)
                    if 由:
                        return True, 由
                sp = str(参.get('scriptPath') or '')
                if isinstance(a.get('裁'), str) and a['裁'].strip() and sp and os.path.basename(sp) != '造章.js':
                    n = str(章) if 章 else 'N'
                    return True, ('⛔续跑之守（坑㊻）：此续之 scriptPath 係包裹（%s），其 args 定死於文——外传之 args.裁 到不了造章，复停於「致命未净」。'
                                  '改：%s（裁写入新包裹）→ Workflow({scriptPath:\'%s\'})（新派、⛔带 resumeFromRunId）。' % (
                                      os.path.basename(sp), _令(n, a), os.path.join(root or ROOT, '版本', '第%s章' % n, '_承.js')))
                if not (isinstance(a.get('章'), int) and 章 and a['章'] != 章):
                    return False, ''          # 造章之续、无缺：俱自缓存回放
        # journal 不见、非造章、或属他章 → 落到②（续错 run 号即全重跑）
    x = 派造章之参(参, a)
    if not isinstance(x, dict):
        return False, ''
    try:
        n = int(x.get('章'))
    except (TypeError, ValueError):
        return False, ''
    凭 = 已封之凭(n, root)
    if 凭:
        return True, ('⛔续跑之守（⑭之移·1027）：第%d章已封（%s）——⛔重派造章（覆其稿、回执与轮记）。'
                      '改旧章走 `python3 工具/改单.py --立`／`--施单` 或大审之还账；该写之章见 `python3 工具/自走.py`。' % (n, 凭))
    除席 = []
    if n >= 拒後自:                       # 〔W919 环4·②之二、③〕补席之越、二稿无录、一稿无录〔W924〕、重造之除席
        try:
            由, 除席 = 拒後派之判(x, n, root, 来=来 or (lambda k: _来之默(k, 根, root)))
        except Exception as e:
            由 = ''
            print('  ⚠ 续跑之守·拒後派之判 崩（%s）——照旧判' % type(e).__name__, file=sys.stderr)
        if 由:
            return True, 由
    if x.get('重造') is True:
        try:
            (记 or (lambda n: __import__('承').记重造(n, 除席=除席, root=root)))(n)
        except Exception:
            pass
        return False, ''
    if 收 is None:
        import 承 as _承
        收 = lambda n: _承.收(n, glob.glob(os.path.join(根 or 诸journal之根, '*', '*', 'subagents', 'workflows', '*', 'journal.jsonl')),
                            root=root or ROOT)[0]
    已 = 收(n) or {}
    承 = x.get('承') if isinstance(x.get('承'), dict) else {}
    if x.get('_字面') and 承:
        return False, ''                  # 内联之字面带承：认不出其细，照放
    有 = {os.path.realpath(str(d.get('file', ''))) for d in (承.get('诸稿') or []) if isinstance(d, dict)}
    缺稿 = [d for d in (已.get('诸稿') or []) if os.path.realpath(str(d.get('file', ''))) not in 有]
    缺段 = [k for k in ('选', '草', '盲', '审') if k in 已 and k not in 承]
    if not (缺稿 or 缺段):
        return False, ''
    包 = os.path.join(root or ROOT, '版本', '第%d章' % n, '_承.js')
    缺 = '、'.join([os.path.basename(str(d.get('file', ''))) for d in 缺稿] + 缺段)
    共病 = (已.get('选') or {}).get('common_fatal') if isinstance(已.get('选'), dict) else ''
    已销 = isinstance(承.get('选'), dict) and bool(承['选'].get('共病之裁')) and not 承['选'].get('common_fatal')
    if 共病 and not 已销:
        return True, ('⛔续跑之守（坑㊻）：第%d章所成之选有共病（%s）——承之即复停於共病。病只在料之一处（X120）：治料（段案／开镜卡改、'
                      '`python3 工具/章料.py %d` 重出）→ `python3 工具/承.py %d --共病已治 "<治料之凭>"`（留选与诸稿续合）；病在诸稿之骨方以 args 加 重造:true 新派'
                      '（总编辑之裁；承.py 自此⛔收旧轮）。' % (n, str(共病)[:80], n, n))
    if not 承:
        return True, ('⛔续跑之守（坑㊻）：第%d章已有已成之段（%s）——新派造章即重写之。走承之路：%s → Workflow({scriptPath:\'%s\'})；'
                      '确要毁稿重造，args 加 重造:true（总编辑之裁；承.py 自此⛔收旧轮）。' % (n, 缺, _令(n, x), 包))
    return True, ('⛔续跑之守（坑㊻）：此派所带之承已旧——未盖第%d章已成之 %s（照派即重跑之）。先重跑 %s 更新 _承.js，再 Workflow({scriptPath:\'%s\'})；'
                  '确要毁稿重造，args 加 重造:true。' % (n, 缺, _令(n, x), 包))


def 自测():
    import tempfile
    import subprocess
    r = []

    def T(名, 条):
        r.append(bool(条))
        print(('  ✓ ' if 条 else '  ✗ ') + 名)

    def 席(行, k, 名, 果='成', 档=None):
        行.append({'type': 'started', 'key': k, 'agentId': 'a' + k, 'label': 名, 'phase': '造'})
        if 果 == '成':
            行.append({'type': 'result', 'key': k, 'agentId': 'a' + k, 'result': {'file': 档 or '/x/版本/第406章/起草_稿%s.md' % k}})
        elif 果 == '败':
            行.append({'type': 'failed', 'key': k, 'agentId': 'a' + k})

    with tempfile.TemporaryDirectory() as d:
        def 写j(run, 行):
            p = os.path.join(d, 'p', 's', 'subagents', 'workflows', run, 'journal.jsonl')
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, 'w', encoding='utf-8') as f:
                f.write('{"type":"launched"}\n' + ''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in 行))
        R = lambda run: {'tool_name': 'Workflow', 'tool_input': {'scriptPath': '工具/席/造章.js', 'resumeFromRunId': run}}
        行 = []
        for k, 名, 果 in [('1', '执笔·甲·换账', '成'), ('2', '执笔·乙·翻个儿', '成'), ('3', '执笔·丙·不说', '败'),
                         ('4', '执笔·丁·速度', '成'), ('5', '执笔·戊·物证', '成'), ('6', '执笔·己·咬合', '成'),
                         ('7', '执笔·庚·回声', '成'), ('8', '执笔·丙·补', '成'), ('9', '选·行家兼两眼', '断')]:
            席(行, k, 名, 果)
        写j('wf_406a-001', 行)
        拦, 由 = 判(R('wf_406a-001'), 根=d)
        T('①406 之实：丙败、丁至补已成、选断 → 拦，点名将重跑之五席与补、印承.py 406',
          拦 and '执笔·丁·速度' in 由 and '执笔·丙·补' in 由 and '承.py 406' in 由 and '执笔·甲' not in 由)
        # ★1024 通式（N≥411）：执笔之交包於 draft 之键——拆而认章；逻辑审·1·补 认作造章之席
        通行 = [{'type': 'started', 'key': 'a', 'label': '执笔·甲·换账'}, {'type': 'result', 'key': 'a', 'result': {'draft': {'file': '/x/版本/第411章/起草_稿一.md'}, 'flaws': '无'}},
                {'type': 'started', 'key': 'b', 'label': '逻辑审·1·补'}, {'type': 'started', 'key': 'c', 'label': '记席'}, {'type': 'result', 'key': 'c', 'result': {'record': {}}}]
        已成, 首缺, 章号, 是造 = 续之判(通行)
        T('①之二 通式之交（draft 键）拆而认章 411；逻辑审·1·补 无果 → 其後已成之记席点名', 章号 == 411 and 是造 and 首缺 == '逻辑审·1·补' and 已成 == ['记席']
          and 续之判([{'type': 'started', 'key': 'z', 'label': '逻辑审·2·补'}])[3])
        行 = []
        for k, 名 in [('1', '执笔·甲'), ('2', '执笔·乙'), ('3', '执笔·丙')]:
            席(行, k, 名)
        席(行, '4', '选·行家兼两眼', '断')
        写j('wf_tail-001', 行)
        T('②唯末一席（选）断、其前俱成 → 放（只重跑那一席）', not 判(R('wf_tail-001'), 根=d)[0])
        行 = []
        for k, 名 in [('1', '执笔·甲'), ('2', '执笔·乙'), ('3', '选·行家兼两眼')]:
            席(行, k, 名)
        写j('wf_done-001', 行)
        T('③俱成 → 放', not 判(R('wf_done-001'), 根=d)[0])
        行 = []
        席(行, '1', '攻·一', '败')
        席(行, '2', '攻·二')
        写j('wf_other-01', 行)
        T('④非造章之 workflow（无执笔）同式 → 放（其无承之路，⛔停书）', not 判(R('wf_other-01'), 根=d)[0])
        T('⑤journal 不见、run 号不合式（路径之注）而无 args.章 → 放（有 args.章 者落②，见⑬）', not 判(R('wf_none-001'), 根=d)[0] and not 判(R('../../etc'), 根=d)[0])
        行 = []
        席(行, '1', '执笔·甲', '败')
        席(行, '1', '执笔·甲')
        席(行, '2', '执笔·乙', '断')
        席(行, '3', '执笔·丙')
        写j('wf_twice-01', 行)
        拦, 由 = 判(R('wf_twice-01'), 根=d)
        T('⑥同键前败後成（续过一回）以成计、序以首起 → 首缺乙、拦丙', 拦 and '执笔·丙' in 由 and '（执笔·乙）' in 由)
        # ⛔自测一律用假章（9），并注 记（⛔写真仓之 承_重造.json——写了即令真章之承.py ⛔收其旧 journal）
        记们 = []
        记 = 记们.append
        F = lambda **a: {'tool_name': 'Workflow', 'tool_input': {'scriptPath': '工具/席/造章.js', 'args': dict({'章': 9, '重': '重', '魂路': ['换账', '不说']}, **a)}}
        有 = lambda n: {'诸稿': [{'file': '/x/版本/第9章/起草_稿甲.md'}], '选': {'ranking': []}} if n == 9 else {}
        拦, 由 = 判(F(), 收=有, 记=记)
        T('⑦新派造章·本章已有已交之稿·无承 → 拦，印全令（带 --重 --魂路）', 拦 and '承.py 9 --重 重 --魂路 换账,不说' in 由)
        T('⑦之二 承盖尽已成（诸稿与选）→ 放；他章无稿 → 放', not 判(F(承={'诸稿': [{'file': '/x/版本/第9章/起草_稿甲.md'}], '选': {}}), 收=有, 记=记)[0]
          and not 判(F(章=8), 收=有, 记=记)[0])
        T('⑦之三 承未盖尽（缺稿、或缺选、或 承:{诸稿:[]}）→ 拦「承已旧」', all(判(F(承=c), 收=有, 记=记)[0] for c in (
            {'诸稿': []}, {'诸稿': [{'file': '/x/版本/第9章/起草_稿甲.md'}]}, {'选': {}})) and '承已旧' in 判(F(承={'诸稿': []}), 收=有, 记=记)[1])
        T('⑦之四 重造:true → 放，且记重造之时（承.py 自此⛔收旧轮）', not 判(F(重造=True), 收=有, 记=记)[0] and 记们 == [9])
        T('⑦之五 args 以 JSON 之串传 → 照认而拦', 判({'tool_name': 'Workflow', 'tool_input': {
            'scriptPath': '/home/user/the-novel/工具/席/造章.js', 'args': '{"章": 9, "重": "重"}'}}, 收=有, 记=记)[0])
        包档 = os.path.join(d, '_承.js')
        def 包(承):
            open(包档, 'w', encoding='utf-8').write("export const meta = {name: 'x'}\nreturn await workflow({ scriptPath: '/r/工具/席/造章.js' }, %s)\n"
                                                    % json.dumps({'章': 9, '重': '重', '魂路': ['换账'], '承': 承}, ensure_ascii=False))
            return {'tool_name': 'Workflow', 'tool_input': {'scriptPath': 包档}}
        T('⑦之六 包裹（_承.js）其承已旧（後又成选）→ 拦；新者 → 放（审逮：旧只认 造章.js 之名，包裹俱放）',
          判(包({'诸稿': [{'file': '/x/版本/第9章/起草_稿甲.md'}], '补': True}), 收=有, 记=记)[0]
          and not 判(包({'诸稿': [{'file': '/x/版本/第9章/起草_稿甲.md'}], '选': {}, '补': True}), 收=有, 记=记)[0])
        内 = lambda sc, a=None: {'tool_name': 'Workflow', 'tool_input': dict({'script': sc}, **({'args': a} if a else {}))}
        T('⑦之七 内联 script 以 workflow() 调造章：字面无承 → 拦；字面带承 → 放（认不出其细）；转传 args → 照 args 判',
          判(内("return await workflow({scriptPath:'工具/席/造章.js'}, {章: 9})"), 收=有, 记=记)[0]
          and not 判(内("return await workflow({scriptPath:'工具/席/造章.js'}, {章: 9, 承: {}})"), 收=有, 记=记)[0]
          and 判(内("return await workflow({scriptPath:'工具/席/造章.js'}, args)", {'章': 9}), 收=有, 记=记)[0])
        T('⑧他器（Bash 等）、非造章之 scriptPath → 放', not 判({'tool_name': 'Bash', 'tool_input': {'command': 'ls'}}, 根=d)[0]
          and not 判({'tool_name': 'Workflow', 'tool_input': {'scriptPath': '工具/席/大审.js', 'args': {'起': 1}}}, 收=有, 记=记)[0])
        # ⑨承.收 真接得上：已交之稿其档在 → 认；档已不在 → ⛔认（稿被覆或挪走）
        ch = os.path.join(d, 'repo', '版本', '第9章')
        os.makedirs(ch)
        稿档 = os.path.join(ch, '起草_稿甲.md')
        open(稿档, 'w').write('x')
        行 = []
        席(行, '1', '执笔·甲·换账', '成', 稿档)
        写j('wf_real-409', 行)
        import 承 as _承
        原时 = _承.重造之时
        _承.重造之时 = lambda n, 档=None: 0.0          # ⛔读真仓之重造档
        try:
            T('⑨真收（承.收）：本章已交之稿档在 → 新派造章拦', 判(F(), 根=d, root=os.path.join(d, 'repo'), 记=记)[0])
            os.remove(稿档)
            T('⑨之二 稿档已不在 → 放', not 判(F(), 根=d, root=os.path.join(d, 'repo'), 记=记)[0])
        finally:
            _承.重造之时 = 原时
        # ⑫承之 run（无执笔之席）：选败、选·补与合稿已成、盲读断 → 续之即重跑选·补、合稿 → 拦（审逮：旧只认执笔·）
        行 = []
        席(行, '1', '选·行家兼两眼', '败')
        席(行, '2', '选·补', '成', '/x/选')
        席(行, '3', '合稿', '成', '/x/正文/第9章.md')
        席(行, '4', '盲读', '断')
        写j('wf_cheng-409', 行)
        a0 = os.path.join(d, 'p', 's', 'subagents', 'workflows', 'wf_cheng-409', 'agent-a1.jsonl')
        open(a0, 'w', encoding='utf-8').write(json.dumps({'message': {'content': '你是第 9 章的**选席**'}}, ensure_ascii=False) + '\n')
        拦, 由 = 判(R('wf_cheng-409'), 根=d)
        T('⑫承之 run 之续（无执笔之席）有缺 → 拦，章取令首（第 9 章）', 拦 and '选·补' in 由 and '合稿' in 由 and '承.py 9' in 由)
        # ⑬续错 run 号：journal 不见、非造章、或属他章 → 落到② 照新派判
        Rr = lambda run, n=9: {'tool_name': 'Workflow', 'tool_input': {'scriptPath': '工具/席/造章.js', 'resumeFromRunId': run, 'args': {'章': n}}}
        T('⑬续错 run 号（不见／非造章／他章之 run）而本章已有已成 → 落②而拦；本章之 run 无缺 → 放', 判(Rr('wf_none-001'), 根=d, 收=有, 记=记)[0]
          and 判(Rr('wf_other-01'), 根=d, 收=有, 记=记)[0] and 判(Rr('wf_done-001'), 根=d, 收=有, 记=记)[0]
          and not 判(Rr('wf_done-001', 406), 根=d, 收=有, 记=记)[0])
        T('⑭续之令带 --裁（致命未净之後总编辑之续：承之路接得住裁）', '--裁' in 判({'tool_name': 'Workflow', 'tool_input': {
            'scriptPath': '工具/席/造章.js', 'resumeFromRunId': 'wf_406a-001', 'args': {'章': 406, '重': '重', '魂路': ['换账'], '裁': '已亲治'}}}, 根=d)[1])
        包档2 = os.path.join(d, '_承二.js')
        open(包档2, 'w', encoding='utf-8').write("return await workflow({ scriptPath: '/r/工具/席/造章.js' }, {\"章\": 406})\n")
        拦, 由 = 判({'tool_name': 'Workflow', 'tool_input': {'scriptPath': 包档2, 'resumeFromRunId': 'wf_done-001', 'args': {'裁': '已亲治'}}}, 根=d)
        T('⑮包裹之 run 无缺而续带 args.裁 → 拦（包裹定死 args，裁到不了造章）、令带 --裁；不带裁 → 放', 拦 and "--裁 '已亲治'" in 由
          and not 判({'tool_name': 'Workflow', 'tool_input': {'scriptPath': 包档2, 'resumeFromRunId': 'wf_done-001'}}, 根=d)[0])
        病 = lambda n: {'诸稿': [{'file': '/x/版本/第9章/起草_稿甲.md'}], '选': {'common_fatal': '料之病'}}
        拦, 由 = 判(F(), 收=病, 记=记)
        T('⑯所成之选有共病 → 拦而指 承.py --共病已治（料之一处）或 重造（骨病）', 拦 and '重造:true' in 由 and '--共病已治' in 由)
        病2 = lambda n: {'诸稿': [{'file': '/x/版本/第9章/起草_稿甲.md'}, {'file': '/x/版本/第9章/起草_稿乙.md'}], '选': {'common_fatal': '料之病'}}
        销承 = {'诸稿': [{'file': '/x/版本/第9章/起草_稿甲.md'}], '选': {'ranking': ['稿甲'], 'common_fatal': '', '共病之裁': '已治於料'}}
        拦销, 由销 = 判(F(承=销承), 收=病2, 记=记)
        T('⑯之二 X120 承之选已销共病（共病之裁在）→ ⛔以共病拦（余照常：缺稿仍指承已旧）', 拦销 and '共病' not in 由销.split('——')[0] and '承已旧' in 由销)
        # ⑰（1027·开轮六检⑭ 移此）已封之章新派造章 → 拦，重造:true 亦拦；凭二：_十一轮.json、「章-N」之标（真建一库验之）
        封根 = os.path.join(d, 'sealed')
        os.makedirs(os.path.join(封根, '版本', '第9章'))
        open(os.path.join(封根, '版本', '第9章', '_十一轮.json'), 'w').write('{}')
        拦, 由 = 判(F(), root=封根, 收=lambda n: {}, 记=记)
        拦2, _ = 判(F(重造=True), root=封根, 收=lambda n: {}, 记=记)
        T('⑰已封之章（_十一轮.json 在）新派造章 → 拦、指改单／还账；重造:true 亦拦', 拦 and '已封' in 由 and '改单' in 由 and 拦2 and 记们 == [9])
        标根 = os.path.join(d, 'tagged')
        os.makedirs(标根)
        g = lambda *a: subprocess.run(['git'] + list(a), cwd=标根, capture_output=True, text=True)
        g('init', '-q')
        g('-c', 'user.email=t@t', '-c', 'user.name=t', 'commit', '-q', '--allow-empty', '-m', 'x')
        未标 = 判(F(), root=标根, 收=lambda n: {}, 记=记)[0]
        g('branch', '章-9')
        拦, 由 = 判(F(), root=标根, 收=lambda n: {}, 记=记)
        T('⑰之二 本库有「章-9」之标 → 拦；未立标之前 → 放（旧式⑭只在开轮六检、造章前⛔跑，回灌即放）', 拦 and '章-9' in 由 and not 未标)
        # ⑱（1027·坑⑩㉛）schema 键 ASCII：内联与 scriptPath 之文俱扫（1017 主环之原局：键「席法」）；ASCII 之键、值之汉字 → 放
        账根 = os.path.join(d, 'ledger')
        os.makedirs(os.path.join(账根, '设定'))
        json.dump({'件': [{'id': 'W99', '状态': '进行', '预估': '约 1 时、$5', '停止线': '三席俱交'},
                          {'id': 'W98', '状态': '已成', '预估': 'x', '停止线': 'y'},
                          {'id': 'W97', '状态': '进行', '预估': '', '停止线': 'y'},
                          {'id': 'W905', '状态': '已成', '预估': 'x', '停止线': 'y'}]},
                  open(os.path.join(账根, '设定', '工作流账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        内W = lambda sc, a=None: {'tool_name': 'Workflow', 'tool_input': dict({'script': sc}, **({'args': a} if a is not None else {}))}
        坏sc = ("export const meta = {name: 'x'}\nconst r = await agent('审', {schema: {type: 'object', properties: "
                "{席法: {type: 'string'}, ok: {type: 'boolean'}}}})\nreturn r")
        好sc = 坏sc.replace('席法', 'seat_rule')
        拦, 由 = 判(内W(坏sc, {'W': 'W99'}), root=账根)
        T('⑱内联之 schema 键「席法」（1017 原局）→ 拦、点名其键', 拦 and '席法' in 由 and 'ASCII' in 由)
        T('⑱之二 引号之键（"席 法"）→ 拦；ASCII 之键、值与令之汉字 → 放',
          判(内W("const s = {schema: {type: 'object', properties: {\"判\": {type: 'string', description: '汉字'}}}}", {'W': 'W99'}), root=账根)[0]
          and not 判(内W(好sc + "\n// 令：你是审席，判其「席法」", {'W': 'W99'}), root=账根)[0])
        # 复核逮：JSON 之式（"type" 带引号）、description 在 type 之前、嵌套之 properties → 俱拦；ASCII 之键而值与 description 含汉字冒号 → 放
        T('⑱之四 JSON 之式与 description 在前、嵌套之 properties 之汉字键 → 拦；ASCII 之键 → 放',
          判(内W('const s = {"schema": {"type": "object", "properties": {"席法": {"type": "string"}}}}', {'W': 'W99'}), root=账根)[0]
          and 判(内W("const s = {schema: {type: 'object', properties: {判: {description: '甲: 乙', type: 'string'}}}}", {'W': 'W99'}), root=账根)[0]
          and 判(内W("const s = {schema: {type: 'object', properties: {items: {type: 'array', items: {type: 'object', properties: {说明: {type: 'string'}}}}}}}", {'W': 'W99'}), root=账根)[0]
          and not 判(内W("const s = {schema: {type: 'object', properties: {verdict: {description: '判: 甲, 乙', type: 'string', enum: ['甲', '乙']}, "
                        "items: {type: 'array', items: {type: 'object', properties: {desc: {type: 'string'}}}}}}}", {'W': 'W99'}), root=账根)[0])
        坏档 = os.path.join(d, '坏.js')
        open(坏档, 'w', encoding='utf-8').write(坏sc)
        T('⑱之三 scriptPath 之档有非 ASCII 之键 → 拦；今仓 工具/席/*.js 俱放（⛔误拦）',
          判({'tool_name': 'Workflow', 'tool_input': {'scriptPath': 坏档, 'args': {'W': 'W99'}}}, root=账根)[0]
          and not any(schema之坏(open(f, encoding='utf-8').read()) for f in glob.glob(os.path.join(ROOT, '工具', '席', '*.js'))))
        # ⑲（1027·#52 #82 #40①）开件之闸：非写书之 Workflow 须 args.W ∈ 工作流账、状「进行」、有预估与停止线
        拦, 由 = 判(内W(好sc), root=账根)
        T('⑲非写书之 Workflow 无 args.W → 拦、印 工作流账.py --开 之令', 拦 and '工作流账.py --开' in 由)
        T('⑲之二 W 不在账／状非进行（已成）／缺预估 → 俱拦', all(判(内W(好sc, {'W': w}), root=账根)[0] for w in ('W01', 'W98', 'W97')))
        T('⑲之三 W 进行而有预估与停止线 → 放', not 判(内W(好sc, {'W': 'W99'}), root=账根)[0])
        os.makedirs(os.path.join(账根, '设定', '方案'), exist_ok=True)
        open(os.path.join(账根, '设定', '方案', 'W913.md'), 'w', encoding='utf-8').write('# 方案·W913·测\n')
        _预 = 判(内W(好sc, {'W': 'W913', '预审': True}), root=账根)
        T('⑲之五〔W911 环6〕预审在开前：args.预审 true 而方案在（件未开）→ 放；无方案、预审非 true（"true"）、无预审之参 → 俱拦（印预审之序）',
          not _预[0] and all(判(内W(好sc, a), root=账根)[0] for a in ({'W': 'W914', '预审': True}, {'W': 'W913', '预审': 'true'}, {'W': 'W913'}))
          and '预审' in 判(内W(好sc, {'W': 'W913'}), root=账根)[1])
        open(os.path.join(账根, '设定', '方案', 'W905.md'), 'w', encoding='utf-8').write('# 方案·W905·测\n')
        T('⑲之六〔W911 补〕旗唯许未开之件：已成之 W905 带旗（方案在）→ 拦（照旧之开件之判·⛔借旗绕闸）；未开而方案在 → 放；未开而方案不在 → 拦',
          判(内W(好sc, {'W': 'W905', '预审': True}), root=账根)[0] and not 判(内W(好sc, {'W': 'W913', '预审': True}), root=账根)[0]
          and 判(内W(好sc, {'W': 'W914', '预审': True}), root=账根)[0])
        T('⑲之四 写书之流（大审.js、剧情庭.js、造章之包裹）、resumeFromRunId 之续 → 免（⛔挡书）',
          not 判({'tool_name': 'Workflow', 'tool_input': {'scriptPath': '工具/席/剧情庭.js', 'args': {'段': 411}}}, root=账根)[0]
          and not 判({'tool_name': 'Workflow', 'tool_input': {'scriptPath': '工具/席/大审.js'}}, root=账根)[0]
          and not 判({'tool_name': 'Workflow', 'tool_input': {'script': "return await workflow({scriptPath:'工具/席/大审.js'}, {起: 1})"}}, root=账根)[0]
          and not 判({'tool_name': 'Workflow', 'tool_input': {'script': 好sc, 'resumeFromRunId': 'wf_other-01'}}, 根=d, root=账根)[0])
        # 〔W919 环4·X138〕N≥拒後自：①之二 诸无果之席之因（承.一席之因）——任一 拒／不识 即拦；俱断放；N≤488 照旧
        u_ = {'type': 'user', 'message': {'content': '[Workflow harness — computed task] x'}}
        回_ = lambda s, i='': {'type': 'assistant', 'message': {'id': 'm' + s + str(i), 'stop_reason': s, 'content': [], 'usage': {'input_tokens': 1, 'output_tokens': 1}}}
        错_ = lambda st, 文: {'type': 'assistant', 'isApiErrorMessage': True, 'apiErrorStatus': st, 'message': {'content': [{'type': 'text', 'text': 文}]}}
        拒2_ = [u_, 回_('refusal', 1), 回_('refusal', 2), 错_('invalid_request', 'API Error: 400 invalid_request')]
        def 写j档(run, 诸, n=489):
            dd = os.path.join(d, 'p', 's', 'subagents', 'workflows', run)
            os.makedirs(dd, exist_ok=True)
            行 = []
            for i, (名, rows, 果) in enumerate(诸):
                k = '%s%d' % (run[-3:], i)
                if rows is not None:
                    with open(os.path.join(dd, 'agent-a%s.jsonl' % k), 'w', encoding='utf-8') as f:
                        f.write(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows))
                行.append({'type': 'started', 'key': k, 'agentId': 'a' + k, 'label': 名})
                if 果 == '成':
                    行.append({'type': 'result', 'key': k, 'agentId': 'a' + k, 'result': {'draft': {'file': '/x/版本/第%d章/起草_稿%s.md' % (n, i), 'words': 1}}})
                elif 果 == '败':
                    行.append({'type': 'failed', 'key': k, 'agentId': 'a' + k})
            写j(run, 行)
        交_ = lambda 名: (名, [u_, 回_('end_turn')], '成')
        前四 = [交_('执笔·甲·路'), 交_('执笔·乙·路'), 交_('执笔·丙·路'), 交_('执笔·丁·路')]
        写j档('wf_ju-0001', 前四 + [('执笔·戊·物证', [u_, 回_('tool_use')], None), ('执笔·己·路', 拒2_, '败'), ('选·行家兼两眼', [u_, 错_(529, 'API Error: 529 overloaded_error')], '败')])
        拦, 由 = 判(R('wf_ju-0001'), 根=d)
        T('W919·①之二 戊断、己拒、选断（续之判 首缺戊）→ 拦、辞列己「拒後不再请」', 拦 and '执笔·己·路' in 由 and '拒後不再请' in 由 and '承.py 489' in 由)
        写j档('wf_ju-0002', 前四 + [('执笔·戊·物证', [u_, 回_('tool_use')], None)])
        T('W919·①之二 只戊断（容器之断·档在无错）→ 放', not 判(R('wf_ju-0002'), 根=d)[0])
        写j档('wf_ju-0003', 前四 + [('执笔·戊·物证', None, None)])
        拦, 由 = 判(R('wf_ju-0003'), 根=d)
        T('W919·①之二 末席 档不在 → 拦、辞「因不明」（--因 〈席〉 断）', 拦 and '因不明' in 由 and '--因' in 由)
        写j档('wf_ju-0004', 前四 + [('执笔·戊·物证', [u_, 回_('refusal'), 回_('tool_use', 2), 错_(529, 'API Error: 529 overloaded_error')], '败')])
        拦, 由 = 判(R('wf_ju-0004'), 根=d)
        T('W919·①之二 拒1 自续而 529 → 拦（不识）', 拦 and '不识' in 由)
        写j档('wf_ju-0005', 前四 + [('执笔·戊·物证', [u_, 回_('tool_use')], None), ('执笔·己·路', 拒2_, '败')], n=488)
        T('W919·①之二 488 照旧（戊断己拒 → 放·门外一字不变）', not 判(R('wf_ju-0005'), 根=d)[0])
        # ②之二、③：新派（N≥489）之补席之越、二稿无录、重造之除席（料之比以 sha）
        import 承 as _承2
        原记 = _承2.记重造
        根9 = os.path.join(d, 'r489')
        目9 = os.path.join(根9, '版本', '第489章')
        os.makedirs(目9, exist_ok=True)
        open(os.path.join(目9, '_料.md'), 'w', encoding='utf-8').write('料')
        json.dump({'章': 489, '因': {'执笔·乙': ['拒', 'refusal 终（2 回）'], '执笔·丙': ['断', '529'], '执笔·丁': ['不识', '拒 1 回後']}, '补席': ['丙'],
                   '改判': {}, '料之指': _承2.料之指(489, 根9), '重造': []}, open(os.path.join(目9, '_席之因.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        F9 = lambda **a: {'tool_name': 'Workflow', 'tool_input': {'scriptPath': '工具/席/造章.js', 'args': dict({'章': 489, '重': '中', '魂路': ['物证']}, **a)}}
        无收 = lambda n: {}
        无来 = lambda n: []                              # ⛔读真仓之 journal（拒之执笔之现算）
        记9 = []
        try:
            拦a, 由a = 判(F9(补席=['丙', '乙'], 承={'诸稿': [], '补': True}), root=根9, 收=无收, 来=无来, 记=记9.append)
            拦b = 判(F9(补席=['丙'], 承={'诸稿': [], '补': True}), root=根9, 收=无收, 来=无来, 记=记9.append)[0]
            拦c, 由c = 判(F9(二稿=True, 承={'诸稿': [], '补': True}), root=根9, 收=无收, 来=无来, 记=记9.append)
            T('W919·②之二 补席越录（乙）→ 拦；补席⊆录 → 放；二稿无录 → 拦（点 --二稿）', 拦a and '补席之越' in 由a and '乙' in 由a and not 拦b and 拦c and '--二稿' in 由c)
            # 〔W924·501〕一稿无录 → 拦（点 --一稿）；有录（承.py --一稿 所书·晚於重造）→ 放；录之一稿早於末次重造 → 拦；只带二稿之录而 args.一稿 → 拦
            拦w, 由w = 判(F9(一稿=True, 承={'诸稿': [], '补': True}, 补席=[]), root=根9, 收=无收, 来=无来, 记=记9.append)
            根一 = os.path.join(d, 'r489一')
            目一 = os.path.join(根一, '版本', '第489章')
            os.makedirs(目一, exist_ok=True)
            open(os.path.join(目一, '_料.md'), 'w', encoding='utf-8').write('料')
            稿一 = os.path.join(目一, '起草_稿三.md')
            open(稿一, 'w', encoding='utf-8').write('稿' * 300)
            录一 = {'章': 489, '因': {'执笔·甲': ['拒', 'refusal 终（2 回）']}, '补席': [], '改判': {}, '料之指': _承2.料之指(489, 根一), '重造': [],
                   '一稿': {'由': '五席俱拒、整稿一', '时': '2099-01-01T00:00:00Z'}}
            json.dump(录一, open(os.path.join(目一, '_席之因.json'), 'w', encoding='utf-8'), ensure_ascii=False)
            F一 = F9(一稿=True, 承={'诸稿': [{'file': 稿一}], '补': True}, 补席=[])
            拦x = 判(F一, root=根一, 收=无收, 来=无来, 记=记9.append)[0]
            json.dump(dict(录一, 重造=[{'时': '2099-02-01T00:00:00Z', '除席': [], '料之指': '', '料改否': False}]),
                      open(os.path.join(目一, '_席之因.json'), 'w', encoding='utf-8'), ensure_ascii=False)
            拦y, 由y = 判(F一, root=根一, 收=无收, 来=无来, 记=记9.append)
            json.dump(dict({k: v for k, v in 录一.items() if k != '一稿'}, 二稿={'由': '余席俱拒、整稿二', '时': '2099-01-01T00:00:00Z'}),
                      open(os.path.join(目一, '_席之因.json'), 'w', encoding='utf-8'), ensure_ascii=False)
            拦z = 判(F一, root=根一, 收=无收, 来=无来, 记=记9.append)[0]
            T('W924·②之二 一稿无录 → 拦（点 --一稿）；有录 → 放；录之一稿早於末次重造 → 拦；只有二稿之录而 args.一稿 → 拦',
              拦w and '一稿无录' in 由w and '--一稿' in 由w and not 拦x and 拦y and '一稿无录' in 由y and 拦z)
            拦d, 由d = 判(F9(重造=True), root=根9, 收=无收, 来=无来, 记=记9.append)
            open(os.path.join(目9, '_料.md'), 'w', encoding='utf-8').write('料已治')
            拦e, 由e = 判(F9(重造=True, 除席=['乙']), root=根9, 收=无收, 来=无来, 记=记9.append)
            T('W919·③ 录有拒／不识（乙、丁）而无除席 → 拦（料未改、料已治俱然）、辞印 `除席: ["乙", "丁"]`', 拦d and 拦e and '除席: ["乙", "丁"]' in 由d
              and '料未改' in 由d and '料已治' in 由e and 记9 == [])
            open(os.path.join(目9, '_料.md'), 'w', encoding='utf-8').write('料')      # 章料重出而文同（mtime 新·指同）
            拦f = 判(F9(重造=True, 除席=['乙', '丁']), root=根9, 收=无收, 来=无来, 记=记9.append)[0]
            录9 = None
            _承2.记重造 = lambda n, 档=None, 时=None, 除席=None, root=None: _承2.重造之笔(n, 除席, root or 根9)   # ⛔写真仓之 承_重造.json
            拦g = 判(F9(重造=True, 除席=['乙', '丁']), root=根9, 收=无收, 来=无来)[0]
            录9 = json.load(open(os.path.join(目9, '_席之因.json'), encoding='utf-8'))
            T('W919·③ 带除席（尽 S）→ 放（骨病之重造料未改亦放）；记「重造」之笔：章料重出而文同 → 料未改、除席入笔', not 拦f and 记9 == [489] and not 拦g
              and 录9['重造'][-1]['料改否'] is False and 录9['重造'][-1]['除席'] == ['乙', '丁'])
            # 〔W919 落地之查·病一二五〕首派（args.承 无诸稿）与重造俱求 S＝承.拒之执笔（录之因、因之史、历次除席 ∪ 诸 journal 现算）
            jd = os.path.join(d, 'p', 's', 'subagents', 'workflows')
            写j档('wf_jf-0001', [('执笔·乙·咬', 拒2_, '败'), ('执笔·甲·骨', [u_, 错_(529, 'API Error: 529 overloaded_error')], '败')])
            写j档('wf_jf-0002', [('执笔·甲·骨', [u_, 错_(529, 'API Error: 529 overloaded_error')], '败')])
            来拒 = lambda n: [os.path.join(jd, 'wf_jf-0001', 'journal.jsonl')]
            来断 = lambda n: [os.path.join(jd, 'wf_jf-0002', 'journal.jsonl')]
            根空 = os.path.join(d, 'r489空')
            os.makedirs(os.path.join(根空, '版本', '第489章'), exist_ok=True)
            open(os.path.join(根空, '版本', '第489章', '_料.md'), 'w', encoding='utf-8').write('料')
            拦h, 由h = 判(F9(), root=根空, 收=无收, 来=来拒, 记=记9.append)
            拦i = 判(F9(), root=根空, 收=无收, 来=来断, 记=记9.append)[0]
            拦j = 判(F9(), root=根空, 收=无收, 来=无来, 记=记9.append)[0]
            拦k = 判(F9(承={'诸稿': [], '补': True}, 补席=[]), root=根空, 收=无收, 来=来拒, 记=记9.append)[0]
            T('落地之查·病一 首派（无承·无重造·0 稿）而前 Run 乙拒 → 拦（走 承.py 489 分因）；前 Run 只断、无前 Run → 放；承.py 之包裹（承带诸稿之列）→ ⛔此判',
              拦h and '首派之拒席' in 由h and '承.py 489' in 由h and '乙' in 由h and not 拦i and not 拦j and not 拦k)
            拦l, 由l = 判(F9(重造=True), root=根空, 收=无收, 来=来拒, 记=记9.append)
            拦m = 判(F9(重造=True, 除席=['乙']), root=根空, 收=无收, 来=来拒, 记=记9.append)[0]
            T('落地之查·病二 重造而 _席之因.json 不在 → 以 journal 现算 S（乙）：无除席 → 拦、除席［乙］→ 放', 拦l and '重造之除席' in 由l and '["乙"]' in 由l and not 拦m)
            json.dump({'章': 489, '因': {'执笔·甲': ['断', '529']}, '补席': ['甲'], '改判': {}, '料之指': _承2.料之指(489, 根空),
                       '因之史': [['执笔·乙·咬', '拒', 'refusal 终', 'a乙']], '重造': [{'时': 'x', '除席': ['丙'], '料之指': '', '料改否': False}]},
                      open(os.path.join(根空, '版本', '第489章', '_席之因.json'), 'w', encoding='utf-8'), ensure_ascii=False)
            拦n, 由n = 判(F9(重造=True, 除席=['乙']), root=根空, 收=无收, 来=无来, 记=记9.append)
            拦o = 判(F9(重造=True, 除席=['乙', '丙']), root=根空, 收=无收, 来=无来, 记=记9.append)[0]
            T('落地之查·病五 录之因无乙而 因之史 有乙、前回除席丙 → 重造须除［乙、丙］（只除乙 → 拦）', 拦n and '["乙", "丙"]' in 由n and not 拦o)
            # 〔W919 乙批·落地之记之留待〕选／合之重派：带承之诸稿而将重派前次被拒之选——诸稿之指同被拒之时 → 拦；稿已重造（指异）→ 放；承有选 → 放；选断 → 放；录无其指 → 拦
            根选 = os.path.join(d, 'r489选')
            目选 = os.path.join(根选, '版本', '第489章')
            os.makedirs(目选, exist_ok=True)
            open(os.path.join(目选, '_料.md'), 'w', encoding='utf-8').write('料')
            稿们 = []
            for _i in (1, 2, 3):
                _p = os.path.join(目选, '起草_稿%d.md' % _i)
                open(_p, 'w', encoding='utf-8').write('稿%d' % _i * 200)
                稿们.append({'file': _p})
            写j档('wf_jx-0001', [('选·行家兼两眼', 拒2_, '败')])
            写j档('wf_jx-0002', [('选·行家兼两眼', [u_, 错_(529, 'API Error: 529 overloaded_error')], '败')])
            来选拒 = lambda n: [os.path.join(jd, 'wf_jx-0001', 'journal.jsonl')]
            来选断 = lambda n: [os.path.join(jd, 'wf_jx-0002', 'journal.jsonl')]
            json.dump({'章': 489, '因': {'选·行家兼两眼': ['拒', 'refusal 终（2 回）']}, '补席': [], '改判': {}, '料之指': _承2.料之指(489, 根选), '重造': [],
                       '拒时稿指': {'选·行家兼两眼': [_承2.诸稿之指(489, 根选, 稿们)]}}, open(os.path.join(目选, '_席之因.json'), 'w', encoding='utf-8'), ensure_ascii=False)
            拦p, 由p = 判(F9(承={'诸稿': 稿们, '补': True}), root=根选, 收=无收, 来=来选拒, 记=记9.append)
            拦q = 判(F9(承={'诸稿': 稿们, '补': True, '选': {'ranking': [1]}}), root=根选, 收=无收, 来=来选拒, 记=记9.append)[0]
            open(稿们[0]['file'], 'w', encoding='utf-8').write('重造之稿' * 60)
            拦r = 判(F9(承={'诸稿': 稿们, '补': True}), root=根选, 收=无收, 来=来选拒, 记=记9.append)[0]
            os.remove(os.path.join(目选, '_席之因.json'))
            拦s = 判(F9(承={'诸稿': 稿们, '补': True}), root=根选, 收=无收, 来=来选断, 记=记9.append)[0]
            拦t, 由t = 判(F9(承={'诸稿': 稿们, '补': True}), root=根选, 收=无收, 来=来选拒, 记=记9.append)
            T('W919 乙批·选合之重派：选拒而诸稿之指同被拒之时 → 拦（点重造与 --因）；承已有选 → 放；稿已重造（指异）→ 放；选断（529）→ 放；录无其指 → 拦（先分因）',
              拦p and '选合之重派' in 由p and '同被拒之时' in 由p and '重造:true' in 由p and not 拦q and not 拦r and not 拦s and 拦t and '分因' in 由t)
            open(os.path.join(目选, '_席之因.json'), 'w', encoding='utf-8').write('{坏')
            拦u = 判(F9(承={'诸稿': 稿们, '补': True}), root=根选, 收=无收, 来=来选拒, 记=记9.append)[0]
            拦v = 判(F9(承={'诸稿': 稿们, '补': True}, 补席=['丙']), root=根选, 收=无收, 来=来选拒, 记=记9.append)[0]
            os.remove(os.path.join(目选, '_席之因.json'))
            T('W919 乙·查之治 病三：只带稿（无补席、二稿、重造、首派）而 _席之因.json 读崩 → 只 ⚠、放（新拦崩⛔拦）；带稿兼补席而录读崩 → 照拦',
              not 拦u and 拦v)
            T('落地之查·来之取崩 → 只 ⚠（照录判·⛔崩拦）', not 判(F9(重造=True, 除席=['乙', '丙']), root=根空, 收=无收, 来=lambda n: 1 / 0, 记=记9.append)[0])
            open(os.path.join(目9, '_席之因.json'), 'w', encoding='utf-8').write('{坏')
            T('W919·录读崩 → 拦（⛔猜）', 判(F9(重造=True, 除席=['乙']), root=根9, 收=无收, 来=无来, 记=记9.append)[0])
            T('W919·488 之新派带 补席／二稿／一稿 → 照旧（⛔拦）', not 判({'tool_name': 'Workflow', 'tool_input': {'scriptPath': '工具/席/造章.js', 'args': {
                '章': 488, '重': '中', '补席': ['甲'], '二稿': True}}}, root=根9, 收=无收, 来=无来, 记=记9.append)[0]
              and not 判({'tool_name': 'Workflow', 'tool_input': {'scriptPath': '工具/席/造章.js', 'args': {
                '章': 488, '重': '中', '一稿': True}}}, root=根9, 收=无收, 来=无来, 记=记9.append)[0])
        finally:
            _承2.记重造 = 原记
        env = dict(os.environ, ZM_STREAM='自测', ZM_JOURNAL_ROOT=d)
        p = subprocess.run([sys.executable, os.path.abspath(__file__)], input='{坏', capture_output=True, text=True, env=env)
        T('⑩入坏 → rc=0（⛔挡书）', p.returncode == 0)
        p = subprocess.run([sys.executable, os.path.abspath(__file__)], input=json.dumps(R('wf_406a-001')), capture_output=True, text=True, env=env)
        T('⑩之二 真跑：406 之续 → rc=2、stderr 印续跑之守', p.returncode == 2 and '续跑之守' in p.stderr)
    try:
        st = json.load(open(os.path.join(ROOT, '.claude', 'settings.json'), encoding='utf-8'))
        钩 = [e for e in (st.get('hooks') or {}).get('PreToolUse', []) for h in e.get('hooks', []) if '续跑之守' in h.get('command', '')]
        T('⑪settings 之 PreToolUse 挂本器，matcher 认 Workflow', bool(钩) and re.fullmatch(钩[0]['matcher'], 'Workflow') is not None)
        许 = (st.get('permissions') or {}).get('allow') or []
        T('⑪之二 承.py 已预授（拦後之正路⛔再被权限所卡）', any('工具/承.py' in x for x in 许))
    except Exception as e:
        T('⑪settings 读不出：%s' % e, False)
    ok = sum(r)
    print('── 负测·续跑之守 %d/%d %s ──' % (ok, len(r), '全通' if ok == len(r) else '未过'))
    return ok == len(r)


if __name__ == '__main__':
    if '--自测' in sys.argv[1:]:
        sys.exit(0 if 自测() else 1)
    try:
        入 = json.load(sys.stdin)
        拦, 由 = 判(入)
    except Exception:
        sys.exit(0)                      # 入坏、出错⛔拦（本钩只防白耗，⛔挡书）
    if 拦:
        print(由, file=sys.stderr)
        sys.exit(2)
    sys.exit(0)
