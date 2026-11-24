#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""段序之守（1023 立·作者令「设计剧情十章 → 写完这十章 → 大审这十章；定为绝对完美执行的机制，严格按此执行」）——PreToolUse 钩（Workflow）。

【其律】段＝自 381 起每十章（411—420、421—430……）；自 411 之段起严守三序，跳一步即派不出：
  ①审毕方定：开下一段之剧情庭（剧情庭.js，名／题带「势_第S段」）须上一段已大审（大审之册至第 S-1 章在），
    且其题须引 `设定/大审_至第{S-1}章.md`——审出之孤钩、大进、二稿交设计一次造进去（⛔写完再补）。
  ②定毕方写：派第 N 章之造章（造章.js、其包裹、内联调之）须本段剧情庭之势在（设定/剧情庭_势_第S段.md），
    且本段段案十章俱全（S—S+9 每章有 重、魂路）、上一段已大审。
  ③段末方审：大审.js 之 止 ≥410 者须係段末（410、420……），且 起 ＝上一册之止＋1（⛔重审、⛔漏审）。
  ④停则俱停：作者暂停令在（工具/暂停令.py·含「待」之到点）→ 剧情庭、造章、大审俱拦（args.例外 带作者所许之件者放）。
  ⑤欠则⛔写（1027 执行之审 #20① #8② #6·作者令「已定之决……须全部执行起来」）——派第 N 章之造章（N≥411）另验三样，各零 token：
    甲·账限：`账限哨.印(ROOT, N)` 有到期之条即拦（瑕疵总账之限到即先治·1021 作者问「为什么还是我自己发现」）；
    乙·还账：最新大审之册凡「已挂·限M（还账·器施）」而 M≤N 者未还即拦（⛔新章压在已写章之 fatal 上·410 大审 #1 #3—#11）；
    丙·料全：`造式验.py N --料` 红即拦，_料.md 旧於开镜卡（卡改而料未重出）亦拦（坑⑬：料缺已定之细）。
  ⑥甲之验（W921 环4·法用#执行之审·只认封证与空大审·⛔严於封：§二之行、席记诸段、行家评⛔入拦）：
    ①章验：派第 N 章之造章（含承、续跑）——N-1 正文已在 HEAD（git ls-tree）而 版本/第N-1章/ 缺 段.封版（「封版.py：」起）或缺 _十一轮.json
      （绕封入库）→ 拦；N-1 正文未在 HEAD → ⚪ 放；
    ②段首验：开第 S 段之剧情庭、派段首（N＝S）之造章——上段大审册「## 一·本回之席」有一行整格合「未交（败）」（大审.空审之式·「所读」之文
      含「未交代」⛔中）→ 拦；「未交（拒）」「未交（不识）」只 ⚠（⛔印重跑·⛔同令重请）；旧式「未交」只 ⚠；册读不出 → ⚪；
    ③补审：大审.js 之起止同上一册、且上一册有「未交（败）」→ 放（⛔为「起须接止＋1」所拦）——大审.py --录 覆写此册；
    缓：`python3 工具/段序之守.py --缓 S "由"`（由 ≥4 字）於 设定/法用册.json「缓」只行插 {id: 段序, 立: S, 至: S, 由}——盖 S 之①②；⛔钩写册；
    过渡：转拦之章（入主之章＋3·总编辑书之）未至，①②只报（exit 0·⚠ 印 stderr、书一行入 _器之迹.jsonl：器 段序之守.py·参「报：〈由〉」，
      封版之器之迹步随章入库 版本/第N章/_器之迹.md，接棒守 --巡 每巡印末三封之报）；新验自限 2 秒（逾即 ⚪）。
  410 係过渡：审 408—410（401—407 已於 407 审过，⛔重付），自 411 之段起每段之审恰十章。
【其由】大审旧逢 7 封後开（387、397、407），与段（剧情之造以十章为一段）错开三章：审出之病只能写完再补，
  而下一段之造读不到它。今段与审同界：一段写完即审，审之所得即下一段之料。
  非剧情庭／造章／大审之 workflow、他器一概放；入坏、出错 → 放（本钩守序，⛔挡书於器病）。
用法：钩自 stdin 取 JSON；`python3 工具/段序之守.py --自测`；`python3 工具/段序之守.py --缓 S "由"`（甲之验之缓·一段一缓）
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import os, sys, re, json, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
起行 = 411                      # 自此段起严守（1023 作者令）；410 及其前之章照旧
转拦之章 = 489                  # 〔W921 环4⑥〕甲之验之转拦：None 或 N 未至此即只报（1124 入主之笔书 489：485 入主＋3·三章之报俱无方转）（⚠·入 _器之迹）；总编辑於入主之笔书「入主之章＋3」（三章之报俱无方转）
甲验之限 = 2.0                  # 秒：甲之验（①②③之读）逾即 ⚪


def 段首(n):
    return 381 + (n - 381) // 10 * 10


def _上审():
    import 大审
    cs = 大审.诸册()
    return cs[-1][0] if cs else 0


def _势在(S):
    return os.path.exists(os.path.join(ROOT, '设定', '剧情庭_势_第%d段.md' % S))


def _段案缺(S):
    """→ S—S+9 之中段案缺（无 重 或 魂路）之章［］。"""
    import 章料
    缺 = []
    for n in range(S, S + 10):
        t = 章料.段案行(n, ROOT) or ''
        if not (re.search(r'^- 重：(轻|中|重)\s*$', t, re.M) and re.search(r'^- 魂路：\S', t, re.M)):
            缺.append(n)
    return 缺


def _题文(p):
    try:
        p = p if os.path.isabs(p) else os.path.join(ROOT, p)
        return open(p, encoding='utf-8', errors='replace').read()
    except Exception:
        return None


def _参(入):
    参 = 入.get('tool_input') or {}
    a = 参.get('args')
    if isinstance(a, str):
        try:
            a = json.loads(a)
        except ValueError:
            a = {}
    return 参, (a if isinstance(a, dict) else {})


def _器(参):
    """→ 'pt'（剧情庭）、'zz'（造章）、'ds'（大审）或 ''。scriptPath 之名为准；内联者看其文所调。"""
    sp = os.path.basename(str(参.get('scriptPath') or ''))
    for 名, k in (('剧情庭.js', 'pt'), ('造章.js', 'zz'), ('大审.js', 'ds')):
        if sp == 名:
            return k
    return ''


def _停():
    try:
        import 暂停令
        在, 由 = 暂停令.在(ROOT)
        return (由 if 在 else ''), 暂停令.许跑   # 1027 W75：开件所销之例外，其件进行中仍许（⛔一例外两处消费）
    except Exception:
        return '', (lambda 件: False)


def _账限(n):
    """→ [由]：瑕疵总账之限压在第 n 章头上者（账限哨·一处判）。读崩 → []（本钩守序，⛔挡书於器病）。"""
    try:
        import 账限哨
        拦, L = 账限哨.印(ROOT, n)
    except Exception:
        return []
    if not 拦:
        return []
    号 = [x.strip().split()[1] for x in L[1:] if x.strip().startswith('⛔') and len(x.strip().split()) > 1]
    return ['瑕疵总账到期 %d 条（%s）——先治或「弃：由」移已治（python3 工具/账限哨.py）' % (len(号), '、'.join(号[:8]))]


def _还账(n):
    """→ [由]：最新大审之册「已挂·限M（…）」而 M≤n 未还者（大审.限於·与开镜卡问七同一读；「入段案」者除外）。"""
    try:
        import 大审
        欠 = [(号, 限) for 号, 限, 裁 in 大审.限於(n) if '入段案' not in 裁]   # 1027 合流（线 E 复核所逮）：⛔只认字面「还账」——「已挂·限M（待撰）」漏之；入段案者归段案
    except Exception:
        return []
    if not 欠:
        return []
    return ['大审还账 %d 笔未还（%s）——册已给原句新句者照册三节出单、python3 工具/还账.py --施 <单.json> 器施（零 token·改单 --施单 禁正文）；须撰者本段之坐撰之；施毕其格改「已治·改单#…」'
            % (len(欠), '、'.join('#%s·限%d' % x for x in 欠[:12]))]


def _料验(n):
    """→ [由]：造式验 --料 之红；_料.md 旧於开镜卡逾一秒亦红（卡改而料未重出）。"""
    import subprocess
    # ★X100之隙（450 承）：正文已合（承.js 只续盲读之後与记席），料之守係起笔之守——⛔以已成之章回算开轮⑲（450 承被误拦）
    try:
        from 封版 import 正文档
        if 正文档(n):
            return []
    except Exception:
        pass
    d = os.path.join(ROOT, '版本', '第%d章' % n)
    卡, 料 = os.path.join(d, '_开镜卡.md'), os.path.join(d, '_料.md')
    try:
        p = subprocess.run([sys.executable, os.path.join(ROOT, '工具', '造式验.py'), str(n), '--料'], cwd=ROOT,
                           capture_output=True, text=True, timeout=120, env=dict(os.environ, ZM_STREAM='段序之守'))
    except Exception:
        return []
    由 = []
    if p.returncode != 0:
        由.append('料不全（%s）' % ((p.stdout.strip().split('\n') or [''])[-1][:200]))
    try:
        if os.path.exists(卡) and os.path.exists(料) and os.path.getmtime(卡) - os.path.getmtime(料) > 1:
            由.append('_料.md 旧於开镜卡（卡改而料未重出）——python3 工具/章料.py %d' % n)
    except OSError:
        pass
    return 由


# ═══ 甲之验（W921 环4）═══
def 封证之缺(m, root=None, 在HEAD=None):
    """第 m 章（派 m+1 之造章）：正文在 HEAD 而 版本/第m章/ 缺 段.封版（「封版.py：」起）或缺 _十一轮.json → 由；正文未在 HEAD → None（⚪）；崩 → None。"""
    root = root or ROOT
    try:
        if 在HEAD is None:
            import subprocess
            from 对账预筛 import 章号
            r = subprocess.run(['git', '-c', 'core.quotepath=off', 'ls-tree', '-r', '--name-only', 'HEAD', '--', '正文/'], cwd=root,
                               capture_output=True, text=True, timeout=甲验之限)
            在 = r.returncode == 0 and any(章号(x) == m for x in r.stdout.split('\n') if x.endswith('.md'))
        else:
            在 = 在HEAD(m)
        if not 在:
            return None
        d = os.path.join(root, '版本', '第%d章' % m)
        try:
            封 = str((json.load(open(os.path.join(d, '_席记.json'), encoding='utf-8')).get('段') or {}).get('封版') or '')
        except Exception:
            封 = ''
        缺 = []
        if not 封.startswith('封版.py：'):
            缺.append('席记无 段.封版（「封版.py：」起）')
        if not os.path.exists(os.path.join(d, '_十一轮.json')):
            缺.append('无 _十一轮.json')
        return ('第%d章正文已入库而%s——绕封入库（封版 --後 之诸闸未过）' % (m, '、'.join(缺))) if 缺 else None
    except Exception:
        return None


def 空审之读(S, root=None):
    """上段大审册（至第 S-1 章）「## 一·本回之席」→ (态, [席])：态 ∈ 败｜拒｜不识｜旧｜''（俱交）｜None（册读不出·⚪）。
    整格比（大审.空审之式·一处之式·坑53）：「所读」之文含「未交代」⛔中。"""
    root = root or ROOT
    try:
        import 大审
        p = os.path.join(root, '设定', '大审_至第%d章.md' % (S - 1))
        if not os.path.exists(p):
            return None, []
        文 = open(p, encoding='utf-8').read()
        if '## 一·本回之席' not in 文:
            return None, []
        节 = 文.split('## 一·本回之席', 1)[1].split('\n## ', 1)[0]
        for 态, 式 in (('败', 大审.空审之式), ('拒', 大审.拒审之式), ('不识', 大审.不识审之式), ('旧', 大审.旧审之式)):
            们 = [m_.group(1) for m_ in 式.finditer(节)]
            if 们:
                return 态, 们
        return '', []
    except Exception:
        return None, []


def 缓之有(n, root=None):
    """设定/法用册.json「缓」有 {id: 段序, 立 ≤ n ≤ 至} → 其由；无或读崩 → ''。"""
    try:
        册 = json.load(open(os.path.join(root or ROOT, '设定', '法用册.json'), encoding='utf-8'))
        for x in 册.get('缓') or []:
            if x.get('id') == '段序' and isinstance(x.get('立'), int) and isinstance(x.get('至'), int) and x['立'] <= n <= x['至']:
                return str(x.get('由') or '缓')
    except Exception:
        pass
    return ''


def 缓(S, 由, root=None):
    """`--缓 S "由"`：於 设定/法用册.json「缓」只行插一行 {id: 段序, 立: S, 至: S, 由}（坑66·⛔json.dump 整写）；json.load 验义同、坏即复原。→ rc。"""
    root = root or ROOT
    由 = str(由 or '').strip()
    if len(由) < 4:
        print('⛔ --缓 须由（≥4 字）：python3 工具/段序之守.py --缓 %d "由"' % S); return 2
    p = os.path.join(root, '设定', '法用册.json')
    原 = open(p, encoding='utf-8').read()
    旧 = json.loads(原)
    if any(x.get('id') == '段序' and x.get('立') == S for x in 旧.get('缓') or []):
        print('· 已有 段序 之缓 立 %d——⛔重书' % S); return 0
    L = 原.split('\n')
    i = next((k for k, l in enumerate(L) if l.startswith(' "缓": [')), None)
    行 = '  %s' % json.dumps({'id': '段序', '立': S, '至': S, '由': 由}, ensure_ascii=False)
    if i is None:
        print('⛔ 法用册无「缓」之列——⛔猜其位'); return 2
    if L[i].rstrip().endswith('[]') or L[i].rstrip().endswith('[],'):
        L[i] = L[i].replace('[]', '[\n%s\n ]' % 行, 1)
    else:
        L.insert(i + 1, 行 + ',')
    新 = '\n'.join(L)
    try:
        d = json.loads(新)
        加 = [x for x in d.get('缓') or [] if x not in (旧.get('缓') or [])]
        d['缓'] = [x for x in d['缓'] if x not in 加]
        assert d == 旧 and len(加) == 1
    except Exception as e:
        print('⛔ 缓之插坏（%s）——册⛔动' % e); return 2
    open(p, 'w', encoding='utf-8').write(新)
    print('✓ 缓 段序 立 %d 至 %d：%s（盖第 %d 之剧情庭、段首造章及其承／续跑之甲之验）' % (S, S, 由[:60], S))
    return 0


def _报之迹(由, root=None):
    """过渡之报：书一行入 _器之迹.jsonl（器 段序之守.py·参「报：〈由〉」·rc 0）——不抛。"""
    try:
        行 = json.dumps({'t': time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime()), '器': '段序之守.py', '参': [('报：' + 由)[:200]],
                        '秒': 0, 'rc': 0, '流': os.environ.get('ZM_STREAM', '')}, ensure_ascii=False)
        fd = os.open(os.path.join(root or ROOT, '_器之迹.jsonl'), os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
        try:
            os.write(fd, (行 + '\n').encode('utf-8'))
        finally:
            os.close(fd)
    except Exception:
        pass


def 甲之验(k, a, n, S, 封证=None, 空审=None, 缓有=None, 转=None):
    """→ (拦［由］, 警［由］)：①章验（造章 n）、②段首验（剧情庭 S、造章 n＝S）；缓盖之即俱只报。崩 → ([], [])（⛔挡书於器病）。"""
    try:
        t0 = time.time()
        封证 = 封证 or 封证之缺
        空审 = 空审 or 空审之读
        缓有 = 缓有 or 缓之有
        拦, 警 = [], []
        if k == 'zz':
            x = 封证(n - 1)
            if x:
                拦.append(x + '——回第%d章之坐跑 python3 工具/封版.py %d --後（诸闸俱过方入库）' % (n - 1, n - 1))
        if (k == 'pt' or (k == 'zz' and n == S)) and time.time() - t0 <= 甲验之限:
            态, 们 = 空审(S)
            if 态 == '败':
                拦.append('上段大审册（至第%d章）%s「未交（败）」——空大审⛔开下一段；补审：Workflow({scriptPath:\'工具/席/大审.js\', args:{起:%d, 止:%d, …}})'
                          '（起止同上一册·段序之守放）→ python3 工具/大审.py --录 <Run> %d %d 覆写此册' % (S - 1, '、'.join(们), S - 10, S - 1, S - 10, S - 1))
            elif 态 == '拒':
                警.append('上段大审册（至第%d章）%s「未交（拒）」——录（平台之拒·⛔同令重请）' % (S - 1, '、'.join(们)))
            elif 态 == '不识':                          # 〔W921 环7〕败因不识（软拒以 end_turn 终者亦在其内）：只 ⚠、⛔印补审之令（拦则诱同令重请）
                警.append('上段大审册（至第%d章）%s「未交（不识）」——录（败因不识·⛔同令重请；其 agent 档可证器病／断者方补审）' % (S - 1, '、'.join(们)))
            elif 态 == '旧':
                警.append('上段大审册（至第%d章）%s「未交」（旧式·不书因）——只 ⚠' % (S - 1, '、'.join(们)))
        if time.time() - t0 > 甲验之限:
            return [], ['甲之验逾 %.0f 秒——⚪' % 甲验之限]
        if 拦:
            c = 缓有(S if k == 'pt' else n)
            if c:
                return [], ['缓（%s）：%s' % (c[:30], x) for x in 拦] + 警
            if not (转 or (lambda n_: 转拦之章 is not None and n_ >= 转拦之章))(S if k == 'pt' else n):
                return [], ['报（过渡·转拦之章未至）：' + x for x in 拦] + 警
        return 拦, 警
    except Exception:
        return [], []


def 判(入, 上审=None, 势在=None, 段案缺=None, 题文=None, 造章之参=None, 停=None, 账限=None, 还账=None, 料验=None,
      甲验=None, 审败=None):
    """→ (拦否, 由)。诸参供自测注之（甲验：甲之验之替；审败：③补审之上册有「未交（败）」否）。"""
    if (入.get('tool_name') or '') != 'Workflow':
        return False, ''
    参, a = _参(入)
    停由, 许 = (停 or _停)()
    if 停由 and (_器(参) or (造章之参 or _造章之参())(参, a)):
        件 = str(a.get('例外') or '')
        if not (件 and 许(件)):
            return True, ('⛔段序之守·暂停：%s——剧情庭、造章、大审俱⛔开；只许零 token 之活。作者令下方解：'
                          'python3 工具/暂停令.py --解 "作者令：……"（作者亲许一件者：暂停令.py --例外 W? "作者令：…"，args 带 例外:\'W?\'）。' % 停由[:160])
    上审 = 上审 or _上审
    势在 = 势在 or _势在
    段案缺 = 段案缺 or _段案缺
    题文 = 题文 or _题文
    k = _器(参)
    if k == 'pt':
        m = re.search(r'势_第(\d+)段', str(a.get('名') or '') + ' ' + str(a.get('题') or ''))
        if not m:
            return False, ''
        S = int(m.group(1))
        if S < 起行:
            return False, ''
        上 = 上审()
        if 上 < S - 1:
            return True, ('⛔段序之守（作者 1023 令「设计十章→写十章→审十章」）：第%d—%d段之剧情庭须上一段先大审——'
                          '大审之册今至第%d章，缺 %d—%d。先：python3 工具/大审.py --包 %d %d → '
                          "Workflow({scriptPath:'工具/席/大审.js', args:{起:%d, 止:%d, 孤钩:…}})（自走印全令）。"
                          % (S, S + 9, 上, 上 + 1, S - 1, 上 + 1, S - 1, 上 + 1, S - 1))
        t = 题文(str(a.get('题') or ''))
        引 = '大审_至第%d章' % (S - 1)
        if t is None or 引 not in t:
            return True, ('⛔段序之守：第%d—%d段剧情庭之题（%s）须引 `设定/%s.md`——上一段大审所得之孤钩、大进、二稿'
                          '交设计一次造进去（⛔写完再补）。题中写明其诸笔与本段如何收之，再开庭。' % (S, S + 9, a.get('题') or '（无题）', 引))
        return _甲之果((甲验 or 甲之验)('pt', a, S, S))
    if k == 'ds':
        try:
            起, 止 = int(a.get('起')), int(a.get('止'))
        except (TypeError, ValueError):
            return False, ''
        if 止 < 410:
            return False, ''
        上 = 上审()
        if (止 - 380) % 10 != 0:
            return True, ('⛔段序之守：大审之止（%d）须係段末（410、420……）——一段写完即审其十章，⛔段中开审。' % 止)
        if 起 != 上 + 1:
            if 止 == 上 and 起 == 上 - 9 and (审败 or (lambda S_: 空审之读(S_)[0] == '败'))(上 + 1):
                return False, ''                         # 〔W921 环4③〕补审：起止同上一册而其有「未交（败）」→ 放（--录 覆写此册）
            return True, ('⛔段序之守：大审之起（%d）须接上一册之止（%d）＋1＝%d——⛔重审已审之章（已付之料⛔重付）、⛔漏审。'
                          % (起, 上, 上 + 1))
        return False, ''
    # 造章：直派、包裹、内联俱认（取 续跑之守 之认法）
    x = a if k == 'zz' else (造章之参 or _造章之参())(参, a)
    if not isinstance(x, dict):
        return False, ''
    try:
        n = int(x.get('章'))
    except (TypeError, ValueError):
        return False, ''
    if n < 起行:
        return False, ''
    S = 段首(n)
    由 = []
    上 = 上审()
    if 上 < S - 1:
        由.append('上一段未大审（册至第%d章，缺 %d—%d）' % (上, 上 + 1, S - 1))
    if not 势在(S):
        由.append('本段剧情庭之势不在（设定/剧情庭_势_第%d段.md）' % S)
    缺 = 段案缺(S)
    if 缺:
        由.append('本段段案未十章俱全（缺 %s 之 重／魂路）' % '、'.join(str(c) for c in 缺))
    if 由:
        return True, ('⛔段序之守（作者 1023 令「设计十章→写十章→审十章」）：第%d章属 %d—%d 段，未可动笔——%s。'
                      '序：上段大审 → 剧情庭（题引大审之册）→ 段料 → 段案十章（立、驳、验）→ 写。跑 `python3 工具/自走.py` 照其印。'
                      % (n, S, S + 9, '；'.join(由)))
    # ⑤欠则⛔写（1027）：账限、还账、料全——序已齐方验（⛔序未齐时多跑一器）
    欠 = (账限 or _账限)(n) + (还账 or _还账)(n) + (料验 or _料验)(n)
    if 欠:
        return True, ('⛔段序之守·欠（1027 作者令「已定之决、作者之令、要避之坑须全部执行起来」）：第%d章未可动笔——%s。'
                      '先清欠，再派（跑 `python3 工具/自走.py` 照其印）。' % (n, '；'.join(欠)))
    return _甲之果((甲验 or 甲之验)('zz', x, n, S))


def _甲之果(r):
    """甲之验之果 → (拦否, 由)：拦即印补令与缓之式；警（报、拒、旧、缓）→ (False, '⚠…')：exit 0·stderr 印、报书 _器之迹。"""
    拦, 警 = r
    if 拦:
        return True, ('⛔段序之守·甲之验（W921·法用#执行之审·只认封证与空大审）：%s。确须先行而由已明：python3 工具/段序之守.py --缓 <章或段首> "由"'
                      '（由 ≥4 字·一段一缓）。' % '；'.join(拦))
    if 警:
        for x in 警:
            if x.startswith(('报（', '缓（')):
                _报之迹(x)
        return False, '⚠ 段序之守·甲之验：' + '；'.join(警)
    return False, ''


def _造章之参():
    try:
        import 续跑之守
        return 续跑之守.派造章之参
    except Exception:
        return lambda 参, a: None


def 自测():
    import tempfile
    import subprocess
    r = []

    def T(名, 条):
        r.append(bool(条))
        print(('  ✓ ' if 条 else '  ✗ ') + 名)

    W = lambda sp, **a: {'tool_name': 'Workflow', 'tool_input': {'scriptPath': sp, 'args': a}}
    无停 = lambda: ('', lambda 件: False)
    _判 = globals()['判']

    无欠 = lambda n: []

    def 判(入, **k):                                # 诸测默认「无暂停」「无欠」「甲之验无事」（⛔读真仓之暂停令、瑕疵总账、大审之册、料）
        k.setdefault('停', 无停)
        for 键 in ('账限', '还账', '料验'):
            k.setdefault(键, 无欠)
        k.setdefault('甲验', lambda *x: ([], []))
        return _判(入, **k)
    题有 = lambda p: '…收 设定/大审_至第410章.md 之孤钩三笔…'
    题无 = lambda p: '只写势'
    全 = lambda S: []
    缺三 = lambda S: [418, 419, 420]
    在 = lambda S: True
    不在 = lambda S: False
    审至 = lambda n: (lambda: n)
    # ①审毕方定
    PT = W('工具/席/剧情庭.js', 题='设定/剧情庭题/势_第411段.md', 名='势_第411段', 式='新')
    T('①上段未审（册至407）而开 411 段剧情庭 → 拦，印大审 408—410', 判(PT, 上审=审至(407), 题文=题有)[0]
      and '起:408, 止:410' in 判(PT, 上审=审至(407), 题文=题有)[1])
    T('①之二 已审至410、题引 大审_至第410章 → 放', not 判(PT, 上审=审至(410), 题文=题有)[0])
    T('①之三 已审而题未引大审之册 → 拦（审之所得须交设计）', 判(PT, 上审=审至(410), 题文=题无)[0])
    T('①之四 401 段（起行之前）之剧情庭 → 放（照旧）', not 判(W('工具/席/剧情庭.js', 名='势_第401段', 题='x'), 上审=审至(397), 题文=题无)[0])
    T('①之五 非势之剧情庭（名题无「势_第S段」）→ 放', not 判(W('工具/席/剧情庭.js', 名='某裁', 题='设定/剧情庭题/某.md'), 上审=审至(0), 题文=题无)[0])
    # ②定毕方写
    ZZ = lambda n: W('工具/席/造章.js', 章=n, 重='重', 魂路=['换账'])
    T('②411：审至410、势在、段案十章全 → 放', not 判(ZZ(411), 上审=审至(410), 势在=在, 段案缺=全)[0])
    拦, 由 = 判(ZZ(411), 上审=审至(407), 势在=不在, 段案缺=缺三)
    T('②之二 未审、势不在、段案缺三章 → 拦，三由俱印', 拦 and '未大审' in 由 and '势不在' in 由 and '418、419、420' in 由)
    T('②之三 段案只缺末章（十章未全）→ 拦（先定十章再写）', 判(ZZ(415), 上审=审至(410), 势在=在, 段案缺=lambda S: [420])[0])
    T('②之四 410 及其前之章 → 放（照旧）', not 判(ZZ(410), 上审=审至(397), 势在=不在, 段案缺=缺三)[0])
    T('②之五 包裹（_承.js）、内联调造章 → 照其 args 之章判', 判(W('版本/第411章/_承.js'), 上审=审至(407), 势在=在, 段案缺=全,
                                                    造章之参=lambda 参, a: {'章': 411})[0]
      and not 判({'tool_name': 'Workflow', 'tool_input': {'script': 'return 1'}}, 上审=审至(407), 势在=在, 段案缺=全, 造章之参=lambda 参, a: None)[0])
    # ⑤欠则⛔写（1027 执行之审 #20① #8② #6）：账限、还账、料全——各一欠即拦；俱无即放；序未齐时⛔验欠（先印序之由）
    齐 = dict(上审=审至(410), 势在=在, 段案缺=全)
    拦账, 由账 = 判(ZZ(411), 账限=lambda n: ['瑕疵总账到期 1 条（X52）'], **齐)
    拦还, 由还 = 判(ZZ(411), 还账=lambda n: ['大审还账 10 笔未还（#1·限411）'], **齐)
    拦料, 由料 = 判(ZZ(411), 料验=lambda n: ['料不全（⛔ 第411章之料不全：无章料）'], **齐)
    T('⑤之二·正文已合之章（承续）→ 料之守⛔回算（450 承被开轮⑲误拦）；未起笔之章照验', _料验(450) == [])
    T('⑤甲乙丙 账限之欠、大审还账之欠、料不全 → 各拦，印其由与「段序之守·欠」', 拦账 and 'X52' in 由账 and 拦还 and '#1·限411' in 由还
      and 拦料 and '料不全' in 由料 and all('段序之守·欠' in x for x in (由账, 由还, 由料)))
    T('⑤之二 三样俱无欠 → 放（放行之反例）', not 判(ZZ(411), **齐)[0])
    _叫 = []
    判(ZZ(411), 上审=审至(407), 势在=不在, 段案缺=缺三, 账限=lambda n: _叫.append(n) or ['x'])
    T('⑤之三 序未齐 → 先印序之由（⛔验欠、⛔多跑一器）', _叫 == [])
    T('⑤之四 410 及其前之章 → ⛔验欠（照旧）', not 判(ZZ(410), 上审=审至(397), 账限=lambda n: ['x'], 还账=lambda n: ['x'], 料验=lambda n: ['x'])[0])
    try:   # ⑤之五 回灌旧树：db52f247 之 大审_至第410章.md（#1 #3—#11「已挂·限411（还账·器施）」）→ 派 411 欠 10 笔；派 410 → 无（限未到·放行之反例）
        import 大审 as _大5
        _旧5 = subprocess.run(['git', 'show', 'db52f247:设定/大审_至第410章.md'], cwd=ROOT, capture_output=True, text=True)
        if _旧5.returncode == 0:
            _目5 = _大5.册目
            with tempfile.TemporaryDirectory() as _d5:
                open(os.path.join(_d5, '大审_至第410章.md'), 'w', encoding='utf-8').write(_旧5.stdout)
                _大5.册目 = _d5
                try:
                    _欠411, _欠410 = _还账(411), _还账(410)
                finally:
                    _大5.册目 = _目5
            T('⑤之五 回灌旧树（db52f247 之 410 大审之册）：派 411 → 还账之欠 10 笔（#1、#3—#11）；派 410 → 无',
              len(_欠411) == 1 and '10 笔' in _欠411[0] and '#1·限411' in _欠411[0] and '#2·' not in _欠411[0] and _欠410 == [])
        else:
            print('  · ⑤之五 旧树不在（浅克隆）——略')
        T('⑤之六 真读：账限、还账、料验之读不崩（今之欠由真仓定，⛔钉其数）', all(isinstance(f(411), list) for f in (_账限, _还账, _料验)))
    except Exception as e:
        T('⑤之五 真读崩：%s' % e, False)
    # ③段末方审
    DS = lambda a, b: W('工具/席/大审.js', 起=a, 止=b, 孤钩=[])
    T('③审 408—410（过渡）→ 放；审 411—420 → 放', not 判(DS(408, 410), 上审=审至(407))[0] and not 判(DS(411, 420), 上审=审至(410))[0])
    T('③之二 止非段末（417）→ 拦（⛔段中开审）', 判(DS(408, 417), 上审=审至(407))[0])
    T('③之三 起不接上一册（重审 401—410、漏审 412—420）→ 拦', 判(DS(401, 410), 上审=审至(407))[0] and 判(DS(412, 420), 上审=审至(410))[0])
    T('③之四 止 <410 之旧审 → 放', not 判(DS(398, 407), 上审=审至(397))[0])
    T('④他器、非 Workflow → 放', not 判({'tool_name': 'Bash', 'tool_input': {'command': 'ls'}})[0]
      and not 判(W('工具/席/大升级.js', 起=1), 上审=审至(0))[0])
    # ④停则俱停
    有停 = lambda: ('暂停令在（作者令：审完即停）', lambda 件: 件 == 'W70')
    T('④之二 暂停令在：剧情庭、造章、大审俱拦（齐备亦拦）', all(_判(x, 停=有停, 上审=审至(410), 势在=在, 段案缺=全, 题文=题有)[0]
                                                  for x in (PT, ZZ(411), DS(411, 420))))
    T('④之三 暂停之中作者所许之件（args.例外）→ 放；非其件 → 拦', not _判(W('工具/席/剧情庭.js', 题='设定/剧情庭题/势_第411段.md', 名='势_第411段', 例外='W70'),
                                                                停=有停, 上审=审至(410), 题文=题有)[0]
      and _判(W('工具/席/剧情庭.js', 题='设定/剧情庭题/势_第411段.md', 名='势_第411段', 例外='W69'), 停=有停, 上审=审至(410), 题文=题有)[0])
    T('④之四 暂停之中他器（非庭非章非审）→ 放', not _判(W('工具/席/大升级.js', 起=1), 停=有停)[0])
    T('④之五 暂停之许用 暂停令.许跑（1027 W75 实踩：工作流账 --开 销例外，其件进行中之 Workflow 仍许；⛔一例外两处消费）',
      '暂停令.许跑' in open(os.path.abspath(__file__), encoding='utf-8').read().split('def 自测')[0])
    # ⑤真接得上：段案、势、大审之册之读
    try:
        T('⑤真读：401 段段案十章俱全、势在；大审之册读得出', _段案缺(401) == [] and _势在(401) and _上审() >= 407)
    except Exception as e:
        T('⑤真读崩：%s' % e, False)
    p = subprocess.run([sys.executable, os.path.abspath(__file__)], input='{坏', capture_output=True, text=True,
                       env=dict(os.environ, ZM_STREAM='自测'))
    T('⑥入坏 → rc=0', p.returncode == 0)
    p = subprocess.run([sys.executable, os.path.abspath(__file__)], input=json.dumps(DS(408, 417)), capture_output=True, text=True,
                       env=dict(os.environ, ZM_STREAM='自测'))
    T('⑥之二 真跑：段中开审 → rc=2、stderr 印段序之守', p.returncode == 2 and '段序之守' in p.stderr)
    try:
        import 大审 as _大
        T('⑧大审.到期：410（上407）→410；409、417 → 无；420、421（上410）→420；397（上387）→397',
          (_大.到期(410, 407), _大.到期(409, 407), _大.到期(417, 410), _大.到期(420, 410), _大.到期(421, 410), _大.到期(397, 387))
          == (410, None, None, 420, 420, 397))
    except Exception as e:
        T('⑧大审.到期 崩：%s' % e, False)
    try:
        st = json.load(open(os.path.join(ROOT, '.claude', 'settings.json'), encoding='utf-8'))
        钩 = [e for e in (st.get('hooks') or {}).get('PreToolUse', []) for h in e.get('hooks', []) if '段序之守' in h.get('command', '')]
        T('⑦settings 之 PreToolUse 挂本器，matcher 认 Workflow', bool(钩) and re.fullmatch(钩[0]['matcher'], 'Workflow') is not None)
    except Exception as e:
        T('⑦settings 读不出：%s' % e, False)
    # ⑨〔W921 环4〕甲之验：冻料（工具/_负测料/段序/·⛔读活档）——封证、空大审、补审、缓、过渡、时限
    try:
        料 = os.path.join(ROOT, '工具', '_负测料', '段序')
        在 = lambda m: True
        def 甲(样封, 样册, 转=lambda n: True, 缓有=lambda n: '', 在HEAD=在):
            return lambda k_, a_, n_, S_: 甲之验(k_, a_, n_, S_, 封证=lambda m: 封证之缺(m, os.path.join(料, 样封), 在HEAD),
                                               空审=lambda S2: 空审之读(S2, os.path.join(料, 样册)), 缓有=缓有, 转=转)
        齐9 = dict(上审=审至(480), 势在=在, 段案缺=全, 题文=lambda p: '…设定/大审_至第480章.md…')
        PT9 = W('工具/席/剧情庭.js', 题='设定/剧情庭题/势_第481段.md', 名='势_第481段')
        _绕 = 判(ZZ(483), 甲验=甲('绕封', '册全'), **齐9)
        T('⑨①绕封之样（第482章正文已入库而席记无 段.封版）→ 拦，印补令（封版.py 482 --後）与缓之式', _绕[0] and '绕封入库' in _绕[1]
          and 'python3 工具/封版.py 482 --後' in _绕[1] and '--缓' in _绕[1])
        T('⑨①之二 正文未入 HEAD → ⚪ 放；封全 → 放；段名改（他段易名、封版之句改而「封版.py：」起）→ 放',
          not 判(ZZ(483), 甲验=甲('绕封', '册全', 在HEAD=lambda m: False), **齐9)[0] and 判(ZZ(483), 甲验=甲('封全', '册全'), **齐9) == (False, '')
          and 判(ZZ(483), 甲验=甲('段名改', '册全'), **齐9) == (False, ''))
        T('⑨①之三 去 _十一轮.json → 拦', 判(ZZ(483), 甲验=甲('去轮', '册全'), **齐9)[0] and '无 _十一轮' in 判(ZZ(483), 甲验=甲('去轮', '册全'), **齐9)[1])
        _败pt, _败zz = 判(PT9, 甲验=甲('封全', '册败'), **齐9), 判(ZZ(481), 甲验=甲('去轮', '册败'), **齐9)
        T('⑨②上段大审册「未交（败）」→ 拦剧情庭与段首之造章（印补审之令 起:471, 止:480）；段中之章（483）⛔验册',
          _败pt[0] and '小说家' in _败pt[1] and '起:471, 止:480' in _败pt[1] and _败zz[0] and '未交（败）' in _败zz[1]
          and 判(ZZ(483), 甲验=甲('封全', '册败'), **齐9) == (False, ''))
        T('⑨②之二「所读」含「未交代」与旁引之「未交（败）」→ 放；「未交（拒）」→ 放（只 ⚠·⛔印重跑）；旧式「未交」→ 放（只 ⚠）',
          判(PT9, 甲验=甲('封全', '册未交代'), **齐9) == (False, '') and not 判(PT9, 甲验=甲('封全', '册拒'), **齐9)[0]
          and '未交（拒）' in 判(PT9, 甲验=甲('封全', '册拒'), **齐9)[1] and '重跑' not in 判(PT9, 甲验=甲('封全', '册拒'), **齐9)[1]
          and not 判(PT9, 甲验=甲('封全', '册旧'), **齐9)[0] and 空审之读(481, os.path.join(料, '册旧')) == ('旧', ['裁']))
        _识 = 判(PT9, 甲验=甲('封全', '册不识'), **齐9)
        T('⑨②之三〔W921 环7〕「未交（不识）」（软拒之类）→ 放（只 ⚠·⛔印补审之令·⛔同令重请）',
          not _识[0] and '未交（不识）' in _识[1] and 'Workflow(' not in _识[1] and 空审之读(481, os.path.join(料, '册不识')) == ('不识', ['人物']))
        DS9 = W('工具/席/大审.js', 起=471, 止=480, 孤钩=[])
        T('⑨③补审：起止同上一册且其有「未交（败）」→ 放；无败 → 照拦（⛔重审）', not 判(DS9, 上审=审至(480), 审败=lambda S_: True)[0]
          and 判(DS9, 上审=审至(480), 审败=lambda S_: False)[0] and 判(W('工具/席/大审.js', 起=461, 止=480), 上审=审至(480), 审败=lambda S_: True)[0])
        _报们 = []
        _原报 = globals()['_报之迹']
        globals()['_报之迹'] = lambda x, root=None: _报们.append(x)
        try:
            _过 = 判(ZZ(483), 甲验=甲('绕封', '册全', 转=lambda n: False), **齐9)
        finally:
            globals()['_报之迹'] = _原报
        T('⑨⑥过渡：转拦之章未至 → 放（⚠ 报）、报书 _器之迹（器 段序之守.py·参「报：」）；转拦之章或 None、或在 483 之後（入主之笔书「入主之章＋3」）',
          not _过[0] and '报（过渡' in _过[1] and len(_报们) == 1 and '绕封入库' in _报们[0] and (转拦之章 is None or 转拦之章 > 483))
        with tempfile.TemporaryDirectory() as _d9:
            os.makedirs(os.path.join(_d9, '设定'))
            import shutil as _sh9
            _sh9.copy(os.path.join(ROOT, '设定', '法用册.json'), os.path.join(_d9, '设定', '法用册.json'))
            import io, contextlib
            with contextlib.redirect_stdout(io.StringIO()):
                _rc短 = 缓(481, '短', _d9)
                _rc缓 = 缓(481, '1124·补审候其 Run（测）', _d9)
                _rc重 = 缓(481, '1124·补审候其 Run（测）', _d9)
            _册9 = json.load(open(os.path.join(_d9, '设定', '法用册.json'), encoding='utf-8'))
            _原9 = json.load(open(os.path.join(ROOT, '设定', '法用册.json'), encoding='utf-8'))
            import 法用之守 as _守9
            _缓红 = [x for x in _守9.完备(_册9, ROOT)[0] if '缓坏' in x]
            _余 = dict(_册9); _余['缓'] = [x for x in _册9['缓'] if x.get('id') != '段序']
            _缓过 = 判(ZZ(481), 甲验=甲('绕封', '册败', 缓有=lambda n: 缓之有(n, _d9)), **齐9)
            _缓pt = 判(PT9, 甲验=甲('封全', '册败', 缓有=lambda n: 缓之有(n, _d9)), **齐9)
        T('⑨⑤缓：由短 → rc 2；--缓 481 只行插一行（他键义同·json.load 验）、重书 ⛔；缓之行过完备（id 段序 在册）；承 481（造章 481）与剧情庭 481 俱放（⚠ 缓）',
          _rc短 == 2 and _rc缓 == 0 and _rc重 == 0 and _余 == _原9 and sum(1 for x in _册9['缓'] if x.get('id') == '段序') == 1 and not _缓红
          and not _缓过[0] and '缓（' in _缓过[1] and not _缓pt[0] and '缓（' in _缓pt[1])
        _限 = globals()['甲验之限']
        globals()['甲验之限'] = 0.01
        try:
            _慢 = 甲之验('zz', {}, 483, 481, 封证=lambda m: (time.sleep(0.03), '绕封')[1], 空审=lambda S_: ('', []), 缓有=lambda n: '', 转=lambda n: True)
        finally:
            globals()['甲验之限'] = _限
        T('⑨⑦时限：甲之验逾限 → ⚪（⛔拦）', _慢[0] == [] and '逾' in _慢[1][0])
        _回 = [n for n in range(412, 485) if 封证之缺(n - 1)]
        T('⑨⑧真料回放：派 412—484 之造章，前章之封证俱在（误拦 0·%s）' % (_回 or '✓'), _回 == [])
    except Exception as e:
        T('⑨甲之验之测崩：%s %s' % (type(e).__name__, e), False)
    ok = sum(r)
    print('── 负测·段序之守 %d/%d %s ──' % (ok, len(r), '全通' if ok == len(r) else '未过'))
    return ok == len(r)


if __name__ == '__main__':
    if '--自测' in sys.argv[1:]:
        sys.exit(0 if 自测() else 1)
    if sys.argv[1:2] == ['--缓']:
        if len(sys.argv) != 4 or not sys.argv[2].isdigit():
            print('用法：python3 工具/段序之守.py --缓 S "由"'); sys.exit(2)
        sys.exit(缓(int(sys.argv[2]), sys.argv[3]))
    try:
        入 = json.load(sys.stdin)
        拦, 由 = 判(入)
    except Exception:
        sys.exit(0)
    if 拦:
        print(由, file=sys.stderr)
        sys.exit(2)
    if 由:
        print(由, file=sys.stderr)              # 〔W921 环4⑥〕⚠ 之报（exit 0·stderr ⛔入模型——其迹已书 _器之迹）
    sys.exit(0)
