#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""接棒守（1022 立·402 封後无人接棒、书停五时半）——书不停之零 token 三锁之二。

【其由】402 之坐封版时 `心跳.py --跳 403` 自持其锁，写毕交接即收工；Stop 钩（席在跑吗）见「有人在跑」放行——
  那「人」正是它自己。无人开 403 之会话，书停五时半（23:17→04:50），作者醒来自见。
【三锁】
  ①Stop 钩（`工具/席在跑吗.py`）：本坐持写书之锁而手上无席、无後台之活 → 拦（⛔再认己锁作「他人在跑」）。
  ②本器 `--候 N`：交棒者收锁、开新会话之後，後台跑之（零 token）；每分取云端心跳——见第 N 章之锁为他坐所持且新鲜
    → ✓接棒成（rc=0）；逾限（默三十分）无人接 → rc=2，醒交棒者重开。候时 Stop 钩认之放行。
  ③停书警报（1117 交 GitHub）：云巡之跑停逾九十分即红——哨 PR 之言即达作者（总编辑之坐亦死之兜底）；旧每时新会话之警报汰。`--哨` 留与写书之坐自查。
  ④停书之巡（1116 作者令「一定要有一个机制防止这种事情再次出现」「stops at most 1 hour」——455 之坐容器死，书停三日）：
    1117 作者令「定时检查能不能不花费 token……最大程度的去利用 github」「没有额度限制 可以无限跑」→ 交 GitHub（`.github/workflows/巡.yml`）：
    章推之環每五分跑 `--云巡`（＝巡()）：有人在写／交棒中／暂停即「止」——零 token；停写／解停／合入之卡 → 於哨 PR（头枝 备份/巡警）留一言，
    唤总编辑之坐（其订此 PR·唯其能派；同局二十分一唤）；每跑落 备份/巡印。总编辑醒即跑 `--巡`（沙盒并验巡印·rc 5 即環未随章起）。
    兜底之巡（三令入总编辑之坐·见 兜底之令；平台定时之令最短一时，故常＝甲:27＋乙:57 每三十分·缓存恒温，降级＝丙:07 启＋乙改:47 每二十分·其记粘於巡应之「降」至 rc 7）防 GitHub 之巡自停、并守两章之间。
    坐死至新坐开 ≤ 60 分（章推之環在时〔早止之前〕≤ 50；两章之间、GitHub 死俱 心跳.限 25＋兜底 30＋5）、降级後 ≤ 50。
    1117 再治（環）：*/5 之 cron 不可恃 → 巡.yml 改「環」。W910（环11 之裁·降其占：旧一机终日）：章推之環——「章-N」之推即起一環
    （每五分一巡、至多九十分；主枝含章-N 且新坐已接〔心跳之章 ≥N+1 而其坐异於章-N 之封者〕或暂停，连三巡止即早止〔--早止 N〕；局悬方续〔末巡非止、或末之 --早止 rc 1·fen 60·同局至多四续〕），
    cron 三十分只巡一回、⛔起環；rc 5（末封之章推逾十五分而巡印旧於其推）之印即 run_workflow huan=1 zhi=N 补起。
    1117 作者续令「效果至少要和现在一样，最好能超越」→ 不劣之审：闭环（总编辑每 --巡 落 备份/巡应，云巡同局首唤而三十分未应即红·哨 PR 之言即达作者）、
    常对拍（沙盒复云巡之判，异即 rc 6）、护额（仓转私有即云巡自停）——见⑤。
用法：
  python3 工具/接棒守.py --候主 403 [分]   # 封版後候主枝含 403（run_in_background；零 token）：0 已含（已快进）｜3 GitHub 报红／拒／败（印其红）｜2 逾限（印 workflow_dispatch 之兜底·⛔沙盒跑闸）
  python3 工具/接棒守.py --候 404 [分]     # 交棒後以 run_in_background 跑
  python3 工具/接棒守.py --在候            # rc=0 在候
  python3 工具/接棒守.py --立守书          # 守书之会话首回立之（⛔写书之坐立之）
  python3 工具/接棒守.py --哨              # 定时之保用：有人在写或交棒中 rc=0；停写 rc=2 并印开写书会话之令
  python3 工具/接棒守.py --派令 404 [--重]  # 交棒：印 create_trigger 之参（run_once_at 已算）；总编辑醒即以其中之参原样 create_session 一回
                                           #   403 未入主枝而其报红／拒／败（或缺章标而 备份/存底 有其封版之提交）→ 自出【重派】之参：自「章-403」（或其源）起、先治（1027 A2）
  python3 工具/接棒守.py --巡              # 停书之巡（总编辑之坐·醒於哨 PR 之言或兜底之巡）：印「止」或【重派】之参（rc 0 止｜2 派｜3 解停｜4 合入之卡：坏报或无果逾三十分、被顶即判〔W908 环2(b)〕｜5 環未随章起（末封之章推逾十五分而巡印旧於其推·W910）→降级｜6 对拍不合｜7 巡印复鲜而前巡应之降未复→复常〔W911 重造：降之粘——巡应之「降」rc 4／3／2 ⛔覆〕）；沙盒每跑落 备份/巡应
                                           #   〔W911 重造 环1②〕rc 0 而本坐（总编辑）上下文逾三十万 → 「止」之次行印「⚠ 本坐上下文 N 万……宜作者键 /compact……；答「止」并转此行告作者」（首行恒「止」·见 ⑧）
                                           #   〔W911 重造 环1④〕rc 0 而本唤冷（与前唤隔逾一时、首回缓存读≈0）→ 次行印「⚠ 本唤冷……list_triggers 对 接棒守.兜底之令」（见 ⑧之二）
                                           #   〔1119 执行之审·治1〕沙盒并验活守：钩活、存底刻、钩死之自决代扫与补印、每日首巡（印俱 stderr·stdout 照旧·唯 ⑧ 之次行）——见 ⑥活守
                                           #   〔W908 环12〕印之首行＝00_总章.md 第一律之首句；自决代扫之果（扫至、红、片、首）入巡应——见 ⑦自决之机
                                           #   〔W921 环6〕X132：rc 7 唯巡印之义「鲜／随章」（章推未逾十五分、t 取不得 承前之降·⛔每章一摆）；巡印之证时唯 環／手（cron、试⛔掩 rc 5）；
                                           #     执行之查（stderr）：败（费审.败之扫·摘外）、执行之图、版之鲜（心跳之器、本地 施-*／w9xx 以章界计）、段序之守之报（末三封）、
                                           #     云巡之期（巡印逾期 1.5 倍 → run_workflow 巡.yml）——⚠／🟡 唯异方印；⛔／🔴／败 每巡必印（见「执行之查」节）
  python3 工具/接棒守.py --早止 N          # 章推之環（巡.yml）每巡後跑：主枝含章-N 且新坐已接（心跳之章 ≥N+1 而其坐异於章-N 之封者·其提交之 Claude-Session）或暂停 → 0 可止｜1 局悬｜2 读不出｜3 坐之易不可验
  python3 工具/接棒守.py --云巡 [--试]      # GitHub（巡.yml·章推之環每五分一巡）：巡()、落巡印、非止即於哨 PR 留言唤总编辑（--试 必留一言，验唤醒之路）
                                           #   〔W908 环12〕巡应之自决红未清 → 哨 PR 一言（附片与第一律之句·同局一唤）而红
                                           #   〔W921 环6〕巡印添 源（push→環、schedule→cron、workflow_dispatch→手、--试→试）、環时、器（rev-parse HEAD·⛔GITHUB_SHA）、期（巡.yml 近十回 schedule 之隔之中位·取不得⛔书）
  python3 工具/接棒守.py --自测
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import os, re, sys, time, json, fcntl, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, '工具'))


def _仓目():
    try:
        p = subprocess.run(['git', 'rev-parse', '--git-common-dir'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        if p:
            return p if os.path.isabs(p) else os.path.join(ROOT, p)
    except Exception:
        pass
    return os.path.join(ROOT, '.git')


锁档 = os.path.join(_仓目(), '接棒守.lock')


def _读锁():
    import 存底
    return 存底._锁()          # (新鲜?, 坐, 章)——⛔另造一把尺


def _我():
    import 心跳
    return 心跳.坐()


def 接了(新鲜, 坐, 章, n, 我):
    """⛔纯判：第 n 章之锁为他坐所持且新鲜 → 接棒成。"""
    try:
        return bool(新鲜 and 坐 and 坐 != 我 and 坐 != '未名' and 章 is not None and int(章) == int(n))
    except (TypeError, ValueError):
        return False


def 候(n, 限分=30, 隔=60, 读=None, 我=None, 今=time.time, 睡=time.sleep):
    读 = 读 or _读锁
    我 = 我 or _我()
    f = open(锁档, 'a+')
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print('✓接棒守已在候（他一守）——本守即止')
        return 0
    始 = 今()
    while True:
        新鲜, 坐, 章 = 读()
        if 接了(新鲜, 坐, 章, n, 我):
            print('✓接棒成：第%s章之锁已为坐 %s 所持——交棒者可收工' % (n, 坐))
            return 0
        if 今() - 始 >= 限分 * 60:
            print('⛔接棒未成：第%s章 %d 分无人接锁——再跑 `python3 工具/接棒守.py --派令 %s`、照其所印 create_trigger 一回，'
                  '再 `接棒守.py --候 %s`；⛔本坐自写、⛔候人' % (n, 限分, n, n))
            return 2
        睡(隔)


主枝 = 'claude/the-novel-review-4dtuit'
总编辑 = 'session_018Kg61wMkRDSZXTWBa5imhH'   # 唯其有 create_session 之器（1106 迁仓：RobotSpa 之迁仓之坐接为总编辑；旧 016Hgfc2）
def _源():
    """〔W919·X146〕仓之正址（工具/_仓.py 唯一之源）——⛔取 origin：环境重置其机即把 origin 改回旧仓（RobotSpa/the-novel），
    旧之推法（自 origin 推）令【重派】之 create_session 之 source_url 随之指旧仓。"""
    try:
        import _仓
        return _仓.正址
    except Exception:
        return 'https://github.com/AlienRocketBus/ojedmksaemckdsokjmenjncdklerfml'   # _仓 载不得之退（同 _仓.正址）


源 = _源()


def 务之名(n, 上审=None, 待至=None, 段至=None):
    """第 n 章之会话开头实将做何——只为题名（零 token），令⛔随之变。1024 立：题恒为「第N章」，
    而 411 之会话实做 408—410 之大审，作者见题即疑「怎么开始写 411 了」。"""
    try:
        import 大审
        上 = 上审 if 上审 is not None else ((大审.诸册() or [[0]])[-1][0])
        止 = 大审.到期(int(n) - 1, 上)
    except Exception:
        止 = None
    if not 止:
        return '第%d章' % int(n)
    if 待至 is None and 段至 is None:
        try:
            _待 = json.load(open(os.path.join(ROOT, '设定', '暂停令.json'), encoding='utf-8'))
            _待 = (_待.get('待') or {}) if not _待.get('解') else {}
            待至, 段至 = _待.get('大审至'), _待.get('段案至')
        except Exception:
            待至 = 段至 = None
    if 段至 and str(段至).isdigit() and int(段至) == int(n):     # ★1120 待之「段案至」：审毕、立段案验过即停（⛔写其首章）
        return '大审第%d—%d章（审毕、立第%d—%d章之段案验过後暂停·⛔写第%d章）' % (上 + 1, 止, int(n), int(n) + 9, int(n))
    return '大审第%d—%d章（%s）' % (上 + 1, 止, '审毕暂停' if 待至 and int(待至) == 止 else '後接第%d章' % int(n))


def 派之参(n, 重=False, 名=None, 治=None):
    """开第 n 章之会话之 create_session 参——唯此一形（会话之守逐键比之，⛔手拟）。
    治（1027 A2·死锁之治）：前章（n-1）已封而未入主枝、且其报红／拒／败（或缺章标而 备份/存底 有其封版之提交）——
      【重派】之会话自 治（「章-(n-1)」或其治枝、封版之提交之 sha）起（⛔自主枝：主枝无其章），首务治其红；令之首个章号仍係 n（会话之守认之）。"""
    n = int(n)
    if 治:
        令 = ('接《镇冢秘术》第 %d 章之棒（先治第 %d 章：其封版已交而未入主枝——GitHub 之报红／拒／败或缺章标；本会话自「%s」起）：'
              '先 `python3 工具/心跳.py --跳 %d`（被拒即止——他坐已写）、再读总章、跑自走——照其【判】治 治第 %d 章'
              '（红者逐条治、提交、`python3 工具/推.py` 交治枝、`python3 工具/接棒守.py --候主 %d`；⛔绕、⛔弱化），'
              '主枝含第 %d 章後照自走所判续办；末了照总章三之5 接棒；⛔候人' % (n, n - 1, 治, n, n - 1, n - 1, n - 1))
        return {'title': '镇冢秘术·治第%d章（後接第%d章）' % (n - 1, n), 'model': 'claude-opus-5-5', 'source_url': 源,
                'source_revision': 治, 'outcome_branch': 主枝, 'prompt': '【重派】' + 令}
    令 = ('接《镇冢秘术》第 %d 章之棒：先 `python3 工具/心跳.py --跳 %d`（被拒即止——他坐已写）、再读总章、跑自走、'
          '照其所判办（写此章、先大审、或照暂停令停）；末了照总章三之5 接棒；⛔候人' % (n, n))
    return {'title': '镇冢秘术·' + (名 or 务之名(n)), 'model': 'claude-opus-5-5', 'source_url': 源,
            'source_revision': 主枝, 'outcome_branch': 主枝, 'prompt': ('【重派】' if 重 else '') + 令}


def 派令(n, 重=False, 今=time.time, 治=None):
    """交棒之 create_trigger 参（零 token 算好 run_once_at）——总编辑醒来只以其中之参原样 create_session 一回（1024：
    交棒⛔经总编辑另查——锁、暂停、已封、前章入主、重派、参之形俱由会话之守钩验；醒一回由约 $4 降至一呼）。
    治（1027 A2）：前章须治之源（`派令之治` 所判）——即出【重派】自其源起之参。"""
    参 = json.dumps(派之参(n, 重 or bool(治), 治=治), ensure_ascii=False)
    return {'persistent_session_id': 总编辑, 'name': '【派】第%d章%s' % (int(n), '（先治第%d章）' % (int(n) - 1) if 治 else ''),
            'initiation': 'own_followup',
            'run_once_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(今()) + 120)),
            'prompt': ('【派】开第 %d 章之写书会话%s：以下参原样调 create_session 一回即毕（会话之守钩自验锁、暂停、已封、前章入主、'
                       '重派与参之形；拦即照其由办），⛔另查、⛔改参：%s' % (int(n), '（重派·自「%s」起、先治第 %d 章）' % (治, int(n) - 1) if 治 else '', 参))}


# ── ④停书之巡（1116 作者令「stops at most 1 hour」；1117 作者令「定时检查不花 token、最大程度利用 GitHub」→ 交 GitHub：见⑤云巡）──
#   巡()：GitHub 章推之環每五分跑之（`--云巡`），止即零 token；非止方唤总编辑之坐（哨 PR 一言）——唯其有 create_session（定时所唤之新会话⛔能派·1116 演练二回）。
#   总编辑醒（哨 PR 之言、或兜底之巡每三十分）跑 `--巡`（沙盒：并验巡印之鲜、常对拍、落巡应）：印「止」即答「止」一字而止（次行「⚠ 本坐上下文」者并转其行告作者·⑧）。
#   旧三条每时之令（:07 :27 :47·每二十分唤总编辑一回、日七十二唤）1117 汰：日常之巡零 token。
解停之令 = "python3 -c \"import sys;sys.path.insert(0,'工具');import 心跳,自走;print(心跳.解停(自走.末章()+1))\""


def 巡判(d, 今, 限, 停在=True, 末=None):
    """⛔纯判（停书之巡）：云端心跳 d → (形, 号, 由)。形：'止' 有人在写／交棒中／暂停｜'派' 停写→【重派】第 号 章｜'解' 停锁残留而令已解。
    读不出 → 作停写（fail→派，与 哨判 同）；号取心跳之章（或毕），皆无则 末（自走.末章()+1）。"""
    if isinstance(d, dict) and d.get('章') == '暂停':
        if 停在:
            return '止', None, '暂停令在（停锁）'
        return '解', None, '⛔停锁残留而暂停令已解（解停之推未成）——书⛔能续'
    rc, 由 = 哨判(d, 今, 限)
    if rc == 0:
        return '止', None, 由
    号 = None
    if isinstance(d, dict):
        try:
            号 = int(d.get('章') if d.get('章') is not None else d.get('毕'))
        except (TypeError, ValueError):
            号 = None
    return '派', (号 if 号 is not None else 末), 由


合入之界分 = 30   # 封版之章逾此分未入主枝 → 停书（GitHub 停摆·1116 实见：455 封於 10:25，GitHub 一时无报，心跳鲜而巡判止）
_排候之态 = ('queued', 'pending', 'waiting', 'requested')   # GitHub REST 跑之 status 所列之未起四值（并发组之候今未实取其值·宁宽：多认一候只令再闸⛔派）


def 冲突之档(r):
    """报之冲突之档（W908 环4：gate 之 merge 败出其档、推报 --写 --冲突 入报之「冲突」；未入即 []）→ [档]（至多十）。"""
    v = (r or {}).get('冲突') if isinstance(r, dict) else None
    if isinstance(v, str):
        v = [x for x in re.split(r'[\s,，、]+', v) if x]
    return [str(x) for x in (v or [])][:10]


def 闸跑之态(n, sha, 仓=None, 取=None):
    """〔W908 环2(b)〕云端 autopush 於「章-n」（head_sha＝sha）诸跑之态 → '顶'｜'候'｜'飞'｜'毕'｜None。
    顶：其跑俱毕而末跑 cancelled（并发组只容一候，後推者顶之）、且 autopush 无他跑排候（再闸即成唯一之候·⛔顶他人）；
    候：末跑 cancelled 而他跑排候（再闸即顶之——候其起）；飞：其跑有未毕者；毕：末跑非 cancelled。
    读不出（沙盒无 GITHUB_TOKEN、非 GitHub 之机、API 败、无其跑）→ None：合入之卡退回三十分之界（方案「败则」）。
    取（径 → JSON）可注（自测）。"""
    import urllib.parse
    仓 = 仓 or os.environ.get('GITHUB_REPOSITORY', '')
    if 取 is None:
        if os.environ.get('GITHUB_ACTIONS') != 'true' or not 仓:
            return None
        取 = lambda 径: _接口('GET', 径)
    基 = '/repos/%s/actions/workflows/autopush.yml/runs?per_page=%d' % (仓, 20)
    try:
        诸 = [x for x in ((取(基 + '&branch=' + urllib.parse.quote('章-%d' % int(n))) or {}).get('workflow_runs') or [])
             if isinstance(x, dict) and x.get('head_sha') == sha]
        if not 诸:
            return None
        if any(x.get('status') != 'completed' for x in 诸):
            return '飞'
        末 = max(诸, key=lambda x: (str(x.get('created_at') or ''), int(x.get('id') or 0)))
        if 末.get('conclusion') != 'cancelled':
            return '毕'
        队 = (取(基) or {}).get('workflow_runs') or []
        return '候' if any(isinstance(x, dict) and x.get('status') in _排候之态 for x in 队) else '顶'
    except Exception:
        return None


_候之态 = ('候', '飞', '治')   # 合入之卡之态：其跑排候／在飞／含此章之治在飞 → 云巡⛔再闸（再派即顶他人之候跑、或自顶）
_卡之态 = ''                  # 合入之卡 末判之态（'坏'｜'顶'｜'候'｜'飞'｜'治'｜'毕'｜''）——云巡读之定再闸之派否（同 _巡之心：所判与所派同一回）


def 提交之时(引, 根=None):
    """git 之物 引（sha 或 ref）之提交之时（%ct）；读不得 → 0。合入之卡（章-n 之 sha）与 章推之时（其 ref）同尺（W910·坑53：⛔两处各写）。"""
    r = subprocess.run(['git', 'log', '-1', '--format=%ct', 引], cwd=根 or ROOT, capture_output=True, text=True)
    try:
        return int(r.stdout.strip() or 0) if r.returncode == 0 else 0
    except ValueError:
        return 0


def 合入之卡(d, 今=None, 标=None, 含=None, 时=None, 坏=None, 报=None, 跑态=None, 飞=None, 治报=None):
    """心跳之章 N 鲜（封版之坐已跳 N+1、或新坐写 N）而第 N-1 章之封（章-(N-1)）未入主 → 印合入之卡；否则 ''。末判之态记於 _卡之态。
    〔W908 环2(b)〕先读 章-(N-1) 之坏报（坏报之源·同一把尺）：
      ①有坏报 → 逾 合入之界分 方印之（推报.报之语·同一把尺：果、因、红、器红、逾、演、run_url；merge 末添冲突之档）——
        界内⛔印：封版之坐之 --候主 rc 3 先治（⛔两处同治）；
      ②无坏报（无报、旧标之报、或「败·重派」在飞）而云端见其跑 cancelled（闸跑之态「顶」）→ 先问 治之在飞：
        含此章之治在飞（未有坏报）→ 「治」：同坐後推之治顶之、其果归治（治之被顶由同坐後推自吸·⛔卡⛔派）；
        否则判「被顶」、即印（⛔候三十分）——云巡唤时再闸（同局一派）；
      ③余：逾 合入之界分 方印「无果」之由（跑在飞／排候／治在飞／读不出）。
    ⛔断「额度用光」（旧并令作者换号）：本仓公开、Actions 不计分（总章:16④）——唯仓转私有方有额度之忧，其支归 私停（云巡自停而另印）。
    坏（n → (枝, 报)｜None）、报（n → 章-n 之报｜None）、跑态（(n, sha) → 闸跑之态）、飞（标 → [(治枝, sha)]）、治报（治枝 → 报｜None）可注（自测）。"""
    global _卡之态
    _卡之态 = ''
    try:
        n = int(d.get('章')) - 1 if isinstance(d, dict) and d.get('章') not in (None, '暂停') else None
    except (TypeError, ValueError):
        n = None
    if not n:
        return ''
    sha = (标 or 云端章标)(n)
    if not sha or (含 or 主含)(n):
        return ''
    try:
        t = (时 or 提交之时)(sha)
    except Exception:
        t = 0
    分 = ((今 or int(time.time())) - t) // 60 if t else -1
    界内 = 0 <= 分 < 合入之界分
    头 = '⛔ 合入之卡：第%d章已封（章-%d %s）%s未入主枝' % (n, n, sha[:12], ('%d 分' % 分) if 分 >= 0 else '久')
    import 推报
    try:
        r0 = (报 or (lambda k: 推报.读('章-%d' % k, ROOT)))(n)
    except Exception:
        r0 = None
    r0 = r0 if isinstance(r0, dict) and r0.get('sha') == sha else None        # 旧标之报⛔认
    源 = None
    if not 界内:              # 界内⛔取坏报之源（其治之在飞须 ls-remote 与 fetch）：界内有坏报亦⛔印，被顶之判只读 r0
        try:
            源 = (坏 or (lambda k: 坏报之源(k, 读=lambda 枝: r0 if 枝 == '章-%d' % k else 推报.读(枝, ROOT, 取=False), 标=sha)))(n)
        except Exception:
            源 = None
    if 源:                                                                   # ①坏报（逾界）
        枝, r = 源
        _卡之态 = '坏'
        if r.get('因') == 'merge':
            冲 = 冲突之档(r)
            治 = '主枝未进则再闸必败（再闸⛔派）：总编辑并之（七账 merge=账并 自并、余档手并），`python3 工具/推.py` 交'
            末 = ['    · 冲突之档：' + '、'.join(冲) if 冲 else '    · 冲突之档未入报（看 run_url 之 prepare 步）']
        else:
            治 = {'红': '推闸之红逐条治（⛔绕、⛔弱化）、`python3 工具/推.py` 交治枝',
                  '拒': '兜底 `python3 工具/推.py --直`（GITHUB_TOKEN 推不得改 .github/workflows 之提交）'}.get(r.get('果'), '看 run_url')
            末 = []
        return '\n'.join(['%s——GitHub 之闸已报（%s）；%s' % (头, 枝, 治)] + ['  ' + x for x in 推报.报之语(r)] + 末)
    在飞之报 = r0 is None or (r0.get('果') == '败' and r0.get('因') == '重派')
    try:
        态 = (跑态 or 闸跑之态)(n, sha) if 在飞之报 else None
    except Exception:
        态 = None
    治飞 = []
    if 态 == '顶':            # 判顶之前先问含此章之治（W908 环2(b)·复核反例一：章之候跑被同坐後推之治所顶，治之跑在飞——旧即出卡、再闸一已在之章）
        读治 = 治报 or (lambda b: 推报.读(b, ROOT, 取=False))
        try:
            for 枝, s in (飞 or 治之在飞)(sha):
                x = 读治(枝)
                if not (isinstance(x, dict) and x.get('sha') == s and 推报.坏(x)):     # 治已坏报（红／拒／败）⛔作在飞
                    治飞.append((枝, s))
        except Exception:
            治飞 = []
            态 = None             # 治之读不出 → 退回三十分之界（⛔以未明判顶）
        if 治飞:
            态 = '治'
    _卡之态 = 态 or ''
    if 态 == '顶':                                                            # ②被顶：即判、云巡唤时再闸
        return ('%s——其 autopush 之跑 cancelled 而无报（被顶：并发组只容一候，後推者顶之；或逾时被止），亦无含此章之治在飞：'
                '云巡唤时再闸（同局一派·⛔候 %d 分）' % (头, 合入之界分))
    if 界内:
        return ''
    if r0 is not None and 推报.坏(r0):      # 章坏而坏报之源⛔返：含此章之治在飞未毕（坏报之源之判）——再闸⛔派
        _卡之态 = '治'
        由 = 'GitHub 之闸报%s%s，其治枝在飞未毕——再闸⛔派（派即顶并发组之候跑）' % (r0.get('果'), ('（因 %s）' % r0['因']) if r0.get('因') else '')
    elif 态 == '治':
        由 = '其 autopush 之跑被含此章之治（%s）所顶、治之果未出——其果归治（推.py --候 读治枝之报）；再闸⛔派（派即顶并发组之候跑）' % '、'.join(b for b, _ in 治飞[:3])
    elif 态 == '飞':
        由 = '其 autopush 之跑在飞（排候或久跑）；再闸⛔派（派即顶并发组之候跑）'
    elif 态 == '候':
        由 = '其 autopush 之跑被顶而他跑排候——再闸⛔派（派即顶并发组之候跑）、候其起，下唤再问'
    else:
        由 = 'GitHub 之闸无报（查 Actions「autopush」之跑：未触、挂、被顶）'
    return ('%s——%s；本仓公开、Actions 不计分（⛔断额度）：仓若转私有，云巡自停而另印（私停）；兜底 `python3 工具/推.py --直`（直推主枝须作者许）'
            % (头, 由))


_巡之心 = None   # 巡() 所读之云端心跳（云巡落巡印之 心时 取此——所判与所记同一心跳，常对拍方准）
_前巡应 = None   # 〔W911 重造 环1①〕巡(查印=True) 开头所读之前巡应（一回·⛔再 fetch）——复常之判与 落巡应 之「降」俱取此


def 前降(前):
    """⛔纯（W911 重造 环1①·降之粘）：前巡应 → 降级未复否：其「降」为真、或旧巡应（无「降」键）之 rc 5。
    巡() 之复常判与 巡应之体 之承同经此（一把尺·坑㊱）。旧病：复常唯判前巡应 rc==5，rc 4／3／2 之巡落巡应即覆之 → 降级永驻。"""
    前 = 前 if isinstance(前, dict) else {}
    return bool(前.get('降') or 前.get('rc') == 5)


def 巡(查印=False):
    global _巡之心, _前巡应, _巡印之义
    _前巡应 = _读枝档(巡应枝, 巡应档) if 查印 else None   # 〔W911 重造 环1①〕开头即读（rc 4／3／2 之支先返，落巡应亦须承其降）；云巡（查印 False）⛔读
    import 心跳
    在, d = 心跳._远()
    _巡之心 = d if 在 else None
    try:
        import 暂停令
        停在 = bool(暂停令.在()[0])     # 1117 治：旧 bool(元组) 恒真——令解而停锁残留，巡恒判止、⛔察解停
    except Exception:
        停在 = True
    末 = None
    if not (在 and isinstance(d, dict)) or (d.get('章') is None and d.get('毕') is None):
        try:
            import 自走
            末 = 自走.末章() + 1
        except Exception:
            末 = None
    形, 号, 由 = 巡判(d if 在 else None, int(time.time()), 心跳.限, 停在=停在, 末=末)
    if 形 == '止':
        卡 = 合入之卡(d)
        if 卡:
            print(卡)
            return 4
        if 查印:      # 沙盒（总编辑之坐）：验 GitHub 之巡之鲜（rc 5）→ 降级之复（rc 7）→ 常对拍（rc 6）
            印d = _读枝档(巡印枝, 巡印档)
            _巡印之义 = '鲜'
            印由 = 巡印之由(d=印d)
            if 印由:
                print(印由)
                return 5
            if 前降(_前巡应) and _巡印之义 in ('鲜', '随章'):      # 〔W911 重造〕降之粘：前巡应之降未复（rc 4／3／2 之巡⛔覆）→ 复常；〔W921 X132①〕唯鲜／随章方复（未逾、无t 承前之降·巡应之「降」随承）
                print('GitHub 之巡复鲜——复常（兜底之巡 %s＝每三十分·撤降级之每二十分）：%s' % (兜底之刻(), 兜底之改(False)))
                return 7
            异 = 对拍判(印d, _巡之心, 停在, 心跳.限)
            if 异:
                print(异)
                return 6
        print('止')
        return 0
    print(由)
    if 形 == '解':
        print('  ①重跑解停：' + 解停之令)
        print('  ②再 `python3 工具/接棒守.py --派令 <末章+1>`，以其参 create_session 一回')
        return 3
    if 号 is None:
        print('  ⛔章号读不出——跑 `python3 工具/自走.py` 取下一章，再 `python3 工具/接棒守.py --派令 N --重`、以其参 create_session')
        return 2
    坐 = str(d.get('坐') or '') if isinstance(d, dict) else ''
    if isinstance(d, dict) and d.get('章') is not None and 坐 and 坐 not in ('暂停令', '未名'):
        print('  ①先 get_session session_%s 看实时之状：正跑一回（running）即⛔重派、答「候」而止；其 rate_limit_info.status 非 allowed（周限·坑59：额度未复，派亦即败）即⛔重派、答「候·周限至 resetsAt」而止；否则续②（痛三：动他会话只凭实时之状）' % 坐)
    治 = 派令之治(号)
    print('  ②create_session 参原样（【重派】·会话之守钩拦即照其参／其由办）%s：' % ('（先治第%d章·源「%s」）' % (号 - 1, 治) if 治 else ''))
    print('  ' + json.dumps(派之参(号, True, 治=治), ensure_ascii=False))
    return 2


# ── ⑤云巡（1117 作者令「定时检查能不能不花费 token 而且能够达到最好的效果……最大程度的去利用 github」；同日「没有额度限制 可以无限跑」）──
#   停书之巡交 GitHub（.github/workflows/巡.yml）：章推之環每五分跑 `--云巡`＝巡()；「止」即毕——零 token。
#   非止（停写→派｜解停｜合入之卡｜器自败）→ 於哨 PR（头枝 备份/巡警）留一言：总编辑之坐订其动静（subscribe_pr_activity），一言即唤之
#   （候时零 token）；同一停之局 唤之隔 二十分一唤（⛔每五分刷）；停逾 警之界 九十分（或器自败、合入之卡、唤而未应）→ 唤之跑红：哨 PR 之言即达作者（W908 环2(f) 正其语）
#   （红随唤：二十分一红·⛔每五分一邮）。每跑落 备份/巡印（单提交、force）之 _巡印.json（并记其所判之心跳之时 心时）。
#   1117 作者续令「转移到 GitHub 上……效果至少要和现在一样，最好能超越」→ 不劣之审（法用#云巡）：
#     ①闭环：总编辑每跑沙盒之 --巡 落 备份/巡应；云巡唤後逾 应之候 三十分未应 → 红（总编辑之坐失联／订阅断——旧制无人知）；
#     ②常对拍：沙盒之 --巡 以同一心跳复云巡之判，异即 rc 6（GitHub 之判⛔与沙盒异）；
#     ③护额：仓转私有（Actions 按分计）→ 云巡自停（disable 巡.yml·⛔耗尽 autopush 之额度而书停）、唤总编辑降级（1117 作者令开源·仓公开，此为其变之守）；
#     ④兜底之巡每三十分（甲 :27＋乙 :57 二令——平台定时之令最短一时，一令二刻〔27,57〕1117 平台拒之；缓存一时内恒温，每唤约 $0.1—0.2；
#       每三时则缓存恒冷、每唤约 $1——日耗反不逾每三时，而守倍密·1117 审计实测）：验巡印（rc 5 即降级：丙 :07 启＋乙改 :47＝每二十分如旧；复鲜 rc 7 即复——降之记粘於巡应之「降」，rc 4／3／2 之巡⛔覆〔W911 重造·旧病降级永驻〕）；
#       两章之间（章推之環已早止）之停写唯兜底与平台之 child-session-event 察之（W910 降占之价）。
#   坐死至新坐开 ≤ 60（⑩钉之）：章推之環在时（早止之前）≤ 心跳.限 25 ＋ 云巡之隔 5 ＋ GitHub 之迟（留 15）＋ 派之数分 ≤ 50；
#     两章之间与 GitHub 死俱 ≤ 25 ＋ 兜底之隔 30 ＋ 5 ≤ 60，降级後 ≤ 50。
#   1117 再治（環·GitHub 之 */5 定时不可恃、dispatch 之跑俱成）；W910（环11 之裁「事驱＋疏 cron」·旧一机终日占而九成八係 sleep）——章推之環：
#     「章-N」之推即起一環（job huan·ref 恒主枝·zhi＝N；每 jian 三百秒一巡、至多 fen 九十分、每巡先取主枝之新）；
#     每巡後 --早止 N（早止之局：主枝含章-N 且心跳之章 ≥N+1 而其坐异於章-N 之封者，或暂停）连三巡 rc 0 而本巡止即早止；
#     環末唯局悬（末巡非止、或末之 --早止 rc 1）且续之次 <4 方自派一短環（fen 60）——有事方续；
#     cron 三十分只巡一回、⛔起環；无 huan 无 shi 之手 dispatch 为再起之器；巡.yml 被停（私停）→ 環於本巡後即止、⛔续。
#     巡印判：環唯章起，巡印之旧⛔即停摆——唯末封之章推逾 巡印之鲜分 而巡印旧於其推方 rc 5（其印 run_workflow huan=1 zhi=N 补起）。
云巡之隔分 = 5
GitHub之迟分 = 15
唤之隔分 = 20
警之界分 = 90
应之候分 = 30          # 总编辑之坐长回合时唤候至回合末——十五分则忙而误红；三十分合一时之界（坐死 25＋5＋30≈一时即红·哨 PR 之言即达作者）
巡警枝 = '备份/巡警'     # 哨 PR 之头枝（⛔并；只为唤总编辑之坐）
巡印枝 = '备份/巡印'     # 单提交（无父）之枝，其上只 _巡印.json——云巡每跑 force 写之
巡印档 = '_巡印.json'
巡印之鲜分 = 15      # W910：巡印鲜於此分即⛔取章推之时（零请）；末封之章推逾此分而巡印之时旧於其推 → 環未随章起（rc 5）
巡应枝 = '备份/巡应'     # 单提交（无父）之枝，其上只 _巡应.json——总编辑沙盒之 --巡 每跑 force 写之（云巡验其应）
巡应档 = '_巡应.json'
# 兜底之巡三令（总编辑之坐之定时之令，各跑 `--巡`·验巡印之鲜）：平台定时之令最短一时（1117 拒 '27,57 * * * *' 之一令）→ 每令一时至多一跑。
#   （名, 号, 常之 cron, 降之 cron, 常时开否）——降级三令俱开。常：甲 :27＋乙 :57＝每三十分（缓存一时内恒温）；
#   降级（GitHub 之巡停摆·rc 5）：丙 :07 启＋乙改 :47 → :07 :27 :47＝每二十分＝旧三令之隔；复常（rc 7·前巡应之降未复而巡印复鲜）反之。
#   〔W911 重造·坑61〕常之隔须 <60：缓存一时之档，唤隔逾一时则缓存恒冷——每唤约十倍（1120 驳席实测冷唤 $3.3—4.1）；自测钉之（独立之断言）。印之令俱由 兜底之改 出（⛔手拟）。
兜底之令 = (
    ('甲', 'trig_01Q7EtciYmueJhVgjeNAzrgU', '27 * * * *', '27 * * * *', True),    # 常开；号同 席在跑吗.守书之令（暂停令三令俱停、解停复常——暂停令.守书之诸参 取此表）
    ('乙', 'trig_01TNKutzRmdDGYtauqe2YHx9', '57 * * * *', '47 * * * *', True),    # 常 :57，降级改 :47
    ('丙', 'trig_014QwEoUV4uaYJXmQrUtHSGh', '7 * * * *', '7 * * * *', False),     # 常停；降级启（:07）
)
兜底之隔分 = 30      # 常之隔（降级二十分）


def 兜底之分(降=False):
    """→ 兜底之巡所开诸令之分（升序）：常 [27, 57]；降 [7, 27, 47]。"""
    return sorted(int(m) for _, _, 常, 降之, 开 in 兜底之令 if 降 or 开 for m in (降之 if 降 else 常).split()[0].split(','))


def 兜底之刻(降=False):
    """→ 「:27 :57」之类（兜底之巡所跑之刻）。"""
    return ' '.join(':%02d' % m for m in 兜底之分(降))


def 兜底之改(降):
    """→ 降级（降=True·rc 5）或复常（降=False·rc 7）之 update_trigger 诸令：只列所改之令、所改之栏（先 enabled 後 cron_expression），以「；」连。"""
    开停, 改 = [], []
    for 名, 号, 常, 降之, 开 in 兜底之令:
        (旧c, 旧开), (新c, 新开) = ((常, 开), (降之, True)) if 降 else ((降之, True), (常, 开))
        if 旧开 != 新开:
            开停.append('update_trigger %s（%s）之 enabled「%s」' % (号, 名, 'true' if 新开 else 'false'))
        if 旧c != 新c:
            改.append('update_trigger %s（%s）之 cron_expression「%s」' % (号, 名, 新c))
    return '；'.join(开停 + 改)


警记 = '<!-- 巡警:%s -->'
再闸之印 = '· 已自 workflow_dispatch autopush.yml'   # 再闸已派之印：唤之体带之即同局已派之记（_旧言 认之·旧制之言亦带·⛔另立记）


def 卡之题(印):
    """⛔纯（W908 环2(e)）：合入之卡之印 → 唤之题「合入之卡 N 分·章-M」（旧用心跳之龄「停书 0 分」：心跳鲜而卡在合入，其题恒误）；读不出即「合入之卡」。"""
    m = re.search(r'第(\d+)章已封（章-\d+ [^）]*）(\d+ 分|久)', 印 or '')
    return '合入之卡 %s·章-%s' % (m.group(2), m.group(1)) if m else '合入之卡'


def 再闸之机(rc, 唤, 键, 旧言, 试=False):
    """⛔纯判（云巡）：调 再闸 否——合入之卡（rc 4）、本跑唤（唤之体即派之记：⛔每五分一派）、同局未派（旧言无「闸·<键>」）。
    〔W908 复核〕旧「同局首唤方调」：首唤时其跑排候／在飞（再闸⛔派）则其後态转「顶」亦永不再闸——卡云「再闸」而行不至。"""
    return rc == 4 and not 试 and bool(唤) and not any(k == '闸·' + str(键) for _, k in 旧言)


def 云巡判(rc, d, 今, 旧言, 印=''):
    """⛔纯判（云巡）：巡之 rc、云端心跳 d、今、哨 PR 之旧言 [(时, 键)] → (唤?, 键, 红?, 停分)。
    rc 0 → 不唤、不红。键＝同一停之局（rc·章或毕·心跳之时）；同键之末言未逾 唤之隔分 → ⛔再唤。
    红：器自败（rc ∉ 0/2/3/4/5）、合入之卡（rc 4）、或停逾 警之界分。"""
    if rc == 0:
        return False, '', False, 0
    时 = 0
    if isinstance(d, dict):
        try:
            时 = int(d.get('时') or 0)
        except (TypeError, ValueError):
            时 = 0
    停分 = (今 - 时) // 60 if 时 else -1
    m4 = re.search(r'第(\d+)章已封', 印 or '') if rc == 4 else None
    if rc in (2, 3) and isinstance(d, dict):
        键 = 'rc%d·%s·%d' % (rc, d.get('章') if d.get('章') is not None else d.get('毕'), 时)
    elif m4:
        键 = 'rc4·%s' % m4.group(1)        # 合入之卡之印带「N 分」——以章为键（⛔每跑异键而每五分一唤）
    else:
        import hashlib
        键 = 'rc%d·%s' % (rc, hashlib.sha1((印 or '').split('\n')[0].encode('utf-8')).hexdigest()[:10])
    末 = max([t for t, k in 旧言 if k == 键] or [0])
    唤 = not (末 and 今 - 末 < 唤之隔分 * 60)
    红 = rc not in (2, 3, 5) or 停分 >= 警之界分
    return 唤, 键, 红, 停分


def _接口(法, 径, 体=None):
    """GitHub REST（GITHUB_TOKEN；⛔沙盒用——沙盒走 git 与会话之器）。→ 解析之 JSON。"""
    import urllib.request
    api = os.environ.get('GITHUB_API_URL', 'https://api.github.com')
    req = urllib.request.Request(api + 径, method=法, data=json.dumps(体).encode('utf-8') if 体 is not None else None,
                                 headers={'Authorization': 'Bearer ' + os.environ.get('GH_TOKEN', os.environ.get('GITHUB_TOKEN', '')),
                                          'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode('utf-8') or 'null')


def 哨PR(仓=None):
    """→ 哨 PR 之号（头枝 备份/巡警、开着者）；无即 None。"""
    import urllib.parse
    仓 = 仓 or os.environ.get('GITHUB_REPOSITORY', '')
    诸 = _接口('GET', '/repos/%s/pulls?state=open&per_page=100&head=%s' % (仓, urllib.parse.quote('%s:%s' % (仓.split('/')[0], 巡警枝))))
    return 诸[0]['number'] if 诸 else None


def _旧言(仓, 号, 今, 取=None):
    """哨 PR 上 github-actions 所留、带 警记 之言（近六时）→ [(时, 键)]；其体带 再闸之印（再闸已派）者并出 (时, '闸·'+键)——同局一派之记。
    取（径 → 言之列）可注（自测）。"""
    import calendar, re as _re
    起 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(今 - 6 * 3600))
    言 = (取 or (lambda 径: _接口('GET', 径)))('/repos/%s/issues/%d/comments?per_page=100&since=%s' % (仓, 号, 起)) or []
    出 = []
    for c in 言:
        体 = c.get('body') or ''
        m = _re.search(r'<!-- 巡警:(.+?) -->', 体)
        if m and (c.get('user') or {}).get('type') == 'Bot':
            t = calendar.timegm(time.strptime(c['created_at'], '%Y-%m-%dT%H:%M:%SZ'))
            出.append((t, m.group(1)))
            if 再闸之印 in 体:
                出.append((t, '闸·' + m.group(1)))
    return 出


def _刻(t):
    return time.strftime('%m-%d %H:%M', time.gmtime(int(t))) if t else '无'


def _砌(档, 体, 信):
    """单档、单提交（无父）之 commit（hash-object＋mktree＋commit-tree：⛔经索引、⛔碰 HEAD 与工作区）→ sha 或 ''。"""
    def 跑令(*a, **k):
        return subprocess.run(a, cwd=ROOT, capture_output=True, text=True, **k)
    b = 跑令('git', 'hash-object', '-w', '--stdin', input=体).stdout.strip()
    t = 跑令('git', 'mktree', input='100644 blob %s\t%s\n' % (b, 档)).stdout.strip()
    env = dict(os.environ, GIT_AUTHOR_NAME='xun', GIT_AUTHOR_EMAIL='xun@users.noreply.github.com',
               GIT_COMMITTER_NAME='xun', GIT_COMMITTER_EMAIL='xun@users.noreply.github.com')
    return subprocess.run(['git', 'commit-tree', t or '-', '-m', 信], cwd=ROOT, capture_output=True, text=True, env=env).stdout.strip()   # 树空即败而返空


读枝之限 = 15                    # 秒：〔W921 环7〕新添之步（落巡印之前、--巡 之执行之查）之 fetch／show 之时限（逾即作读不出·⛔拖巡）


def _读枝档(枝, 档, 限=None):
    """云端单档之枝（巡印、巡应、心跳）→ dict｜None（读不出）。先 fetch。限（秒）：fetch、show 各之时限，逾即 None；None 照旧（无限）。"""
    try:
        subprocess.run(['git', 'fetch', '-q', 'origin', '+refs/heads/%s:refs/remotes/origin/%s' % (枝, 枝)], cwd=ROOT, capture_output=True, timeout=限)
        r = subprocess.run(['git', 'show', 'origin/%s:%s' % (枝, 档)], cwd=ROOT, capture_output=True, text=True, timeout=限)
    except subprocess.TimeoutExpired:
        return None
    try:
        d = json.loads(r.stdout) if r.returncode == 0 else None
    except Exception:
        d = None
    return d if isinstance(d, dict) else None


_源之名 = {'push': '環', 'schedule': 'cron', 'workflow_dispatch': '手'}


def 巡之源(试=False, 环=None):
    """〔W921 环6①·X132②〕本巡之源：--试 → 试；GITHUB_EVENT_NAME：push → 環、schedule → cron、workflow_dispatch → 手（環之续派与手起俱认）；余 → 其名或「?」。"""
    if 试:
        return '试'
    e = (环 if 环 is not None else os.environ).get('GITHUB_EVENT_NAME', '')
    return _源之名.get(e, e or '?')


def 本器之版(根=None):
    """〔W921 环6②〕本器之版＝git rev-parse HEAD（環每巡 fetch＋reset 之後·⛔GITHUB_SHA：其为触发之笔、非实跑之码）；取不得 → ''。"""
    try:
        r = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=根 or ROOT, capture_output=True, text=True, timeout=10)
        return r.stdout.strip() if r.returncode == 0 else ''
    except Exception:
        return ''


def 巡印之体(rc, 印, 今, 跑='', 心=None, 私=False, 源='?', 前=None, 器='', 期=None):
    """⛔纯：_巡印.json 之体。〔W921 环6〕添「源」「環时」（環／手方更·余承前；前无源者以其时承）、「器」（rev-parse HEAD）、「期」（云巡之期·分·取不得⛔书）。"""
    try:
        心时 = int((心 or {}).get('时') or 0) if isinstance(心, dict) else 0
    except (TypeError, ValueError):
        心时 = 0
    d = {'时': 今, '刻': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(今)), 'rc': rc,
         '印': (印 or '').strip().split('\n')[0][:200], '心时': 心时, '私': bool(私), '跑': 跑, '源': 源,
         '環时': 今 if 源 in ('環', '手') else 巡印之证时(前), '器': 器}
    if isinstance(期, (int, float)) and not isinstance(期, bool) and 期 > 0:
        d['期'] = 期
    return d


def 云巡之期(仓, 取=None):
    """〔W921 环6⑤〕Actions 之 API 取 巡.yml 近十回 schedule 之跑时，其隔之中位（分·整）；取不得或不足三跑 → None（⛔书期：体系总图 ⚪「期未测」）。"""
    try:
        d = (取 or (lambda: _接口('GET', '/repos/%s/actions/workflows/%%E5%%B7%%A1.yml/runs?event=schedule&per_page=10' % 仓)))()
        import calendar
        ts = sorted(calendar.timegm(time.strptime(str(x.get('created_at') or x.get('run_started_at'))[:19], '%Y-%m-%dT%H:%M:%S'))
                    for x in (d or {}).get('workflow_runs') or [] if x.get('created_at') or x.get('run_started_at'))
        隔 = sorted(b - a for a, b in zip(ts, ts[1:]) if b > a)
        if len(隔) < 2:
            return None
        m = 隔[len(隔) // 2] if len(隔) % 2 else (隔[len(隔) // 2 - 1] + 隔[len(隔) // 2]) / 2.0
        return int(round(m / 60.0))
    except Exception:
        return None


def 落巡印(rc, 印, 今, 跑='', 心=None, 私=False, 源=None, 期=None):
    """→ 落 备份/巡印（单提交、force）之 _巡印.json（rc、印之首行、所判之心跳之时 心时〔常对拍〕、仓私否、〔W921〕源、環时、器、期）；成否。"""
    try:
        前 = _读枝档(巡印枝, 巡印档, 限=读枝之限)      # 〔W921 环7〕新添之读·带时限（⛔拖云巡）
    except Exception:
        前 = None
    体 = json.dumps(巡印之体(rc, 印, 今, 跑, 心, 私, 源 or 巡之源(), 前, 本器之版(), 期), ensure_ascii=False)
    c = _砌(巡印档, 体, '巡印 rc=%s' % rc)
    if not c:
        return False
    return subprocess.run(['git', '-c', 'core.hooksPath=/dev/null', 'push', '-q', '-f', 'origin', '%s:refs/heads/%s' % (c, 巡印枝)],
                          cwd=ROOT, capture_output=True, text=True).returncode == 0


def 巡应之体(rc, 今, 态=None, 前=None):
    """→ _巡应.json 之体。〔W911 重造 环1①〕「降」：rc 5 → 真；rc 7 → 假；余承 前（前巡应）之降（前降·旧巡应无「降」者以 rc 5 论）——
    降级之记⛔被 rc 4／3／2 之巡覆（旧病：降级永驻）。〔1119 执行之审·治1(e)〕态（活守() 之返）在即添三键「钩」「存底刻」「钩死起」——云巡之 活守判 以之兜底（〔W910〕唯存底刻定红·钩之态只记）；
    活守败（态 None）即⛔添（云巡作旧巡应论、⛔红：缺之由已印於沙盒之 stderr）。
    〔W908 环12②〕态带「自决」（自决之代扫之果：扫至、红、片、首）即并入——云巡之 自决之巡 读之（⛔另立枝）。"""
    d = {'时': 今, '刻': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(今)), 'rc': rc, '坐': os.environ.get('CLAUDE_CODE_SESSION_ID', ''),
         '降': True if rc == 5 else (False if rc == 7 else 前降(前)), '器': 本器之版()}     # 〔W921 环6②〕器＝rev-parse HEAD
    if isinstance(态, dict):
        d.update({'钩': 态.get('钩'), '存底刻': 态.get('存底刻'), '钩死起': 态.get('钩死起')})
        if isinstance(态.get('自决'), dict):
            d['自决'] = 态['自决']
    return json.dumps(d, ensure_ascii=False)


def 落巡应(rc, 今=None, 态=None, 前=None):
    """沙盒（总编辑之坐）每跑 --巡 → 落 备份/巡应（单提交、force）：云巡验总编辑之应（唤而未应即红）；成否。
    〔1119 执行之审·治1(e)〕体带 活守 之三键（钩、存底刻、钩死起）——见 巡应之体。
    〔W911 重造 环1①〕前＝巡(查印=True) 开头所读之前巡应（_前巡应·⛔再 fetch）——体之「降」承之。"""
    今 = 今 or int(time.time())
    体 = 巡应之体(rc, 今, 态, 前)
    c = _砌(巡应档, 体, '巡应 rc=%s' % rc)
    if not c:
        return False
    return subprocess.run(['git', '-c', 'core.hooksPath=/dev/null', 'push', '-q', '-f', 'origin', '%s:refs/heads/%s' % (c, 巡应枝)],
                          cwd=ROOT, capture_output=True, text=True).returncode == 0


def 巡印判(d, 今, 章=None):
    """→ 巡印判之义 之由（''｜停摆之由）——旧之口（自测与他器）照旧。"""
    return 巡印判之义(d, 今, 章)[0]


def 巡印之证时(d):
    """〔W921 环6①·X132②〕巡印之「環随章」之证时：带「環时」者取之（環／手之巡方更·cron、试之巡⛔更）；带「源」而无「環时」者唯 環／手 取其时；
    旧式（无「源」）取其时（过渡·⛔误报）。→ int（0＝无证）。"""
    if not isinstance(d, dict):
        return 0
    try:
        if '環时' in d:
            return int(d.get('環时') or 0)
        if '源' in d:
            return int(d.get('时') or 0) if d.get('源') in ('環', '手') else 0
        return int(d.get('时') or 0)
    except (TypeError, ValueError):
        return 0


def 巡印判之义(d, 今, 章=None):
    """⛔纯判：巡印 d（dict 或 None）→ (由, 义)：由＝''（環随章、或无从判）或停摆之由（附再起与降级之令）；
    〔W921 环6①·X132①〕义 ∈ 私｜鲜（证时鲜於十五分）｜随章（证时 ≥ 章推之时）｜未逾（章推未逾十五分）｜无t（t 取不得、章缺或取之败）｜坏（停摆）——
    巡() 唯「鲜／随章」许 rc 7 复常，余承前之降（⛔每章一摆）。证时唯 環／手 之巡印（巡印之证时·cron 之巡印⛔掩 rc 5）。
    〔W910·环11 之裁〕環唯章起，巡印之旧⛔即停摆：章＝(n, t)——末封之章 n 与其云端「章-n」之提交之时 t；或返之之函（惰取：巡印鲜於 巡印之鲜分 即⛔调——零请）。
    今−t ≥ 巡印之鲜分 而巡印之时 < t → 停摆（環未随章起），其再起之令带 {"huan":"1","zhi":"<n>"}；t 取不得（0）、章缺或取之败 → ''（⛔误报）。私停之支照旧。"""
    降级 = '降级（兜底之巡 %s＝每二十分·如旧之三令）：%s' % (兜底之刻(True), 兜底之改(True))
    if isinstance(d, dict) and d.get('私'):
        return ('⛔ GitHub 之巡自停：仓已转私有（Actions 按分计——章推之環日占数时，将耗 autopush 之额度而书停，故自 disable 巡.yml·環即止）'
                '——%s；仓复公开即 enable 巡.yml（Actions 页「巡」之 Enable workflow），再 run_workflow 巡.yml ref 主枝 inputs {"huan":"1"} 起環' % 降级), '私'
    时 = 巡印之证时(d)
    if 时 and 今 - 时 < 巡印之鲜分 * 60:
        return '', '鲜'
    try:
        n, t = (章() if callable(章) else 章) or (0, 0)
        n, t = int(n), int(t or 0)
    except Exception:
        return '', '无t'
    if not t:
        return '', '无t'
    if 今 - t < 巡印之鲜分 * 60:
        return '', '未逾'
    if 时 >= t:
        return '', '随章'
    降 = ('——①先再起：actions_run_trigger run_workflow 巡.yml ref 主枝 inputs {"huan":"1","zhi":"%d"}（起章推之環：每五分一巡、至多九十分·早止；'
          '環已在则排候、⛔重環）；②%s——巡印复鲜，--巡 即印 rc 7 而复常（%s＝每三十分）' % (n, 降级, 兜底之刻()))
    if not 时:
        return ('⛔ GitHub 之巡停摆：备份/巡印 读不出（或无環／手之巡印），而第%d章推已 %d 分（章-%d·%s UTC）——環未随章起（巡.yml 未跑或被停）'
                % (n, (今 - t) // 60, n, _刻(t)) + 降), '坏'
    return ('⛔ GitHub 之巡停摆：第%d章推已 %d 分（章-%d·%s UTC）而環／手之巡印末更於其前（%s UTC）——環未随章起：查 Actions「巡」之「巡环·章-%d」（未触／被停）'
            % (n, (今 - t) // 60, n, _刻(t), _刻(时), n) + 降), '坏'


def 末封之章(d):
    """〔W910〕末封之章：写第 N 章（心跳之章 N）→ N−1；交棒中（毕＝所交之章·收 N+1，见 席在跑吗:302、心跳.解停 末章+1）→ 毕−1；
    暂停、读不出 → 自走.末章()（正文之末）。"""
    if isinstance(d, dict):
        章 = d.get('章')
        if isinstance(章, int) and not isinstance(章, bool):
            return 章 - 1
        if 章 is None and d.get('毕') is not None:
            try:
                return int(d['毕']) - 1
            except (TypeError, ValueError):
                pass
    import 自走
    return 自走.末章()


def 章推之时(n, 根=None):
    """〔W910〕云端「章-n」之提交之时（提交之时·同 合入之卡 之尺）：本地无其物先 fetch 之；取不得 → 0。"""
    引 = 'refs/remotes/origin/章-%d' % int(n)
    t = 提交之时(引, 根)
    if not t:
        try:
            subprocess.run(['git', 'fetch', '-q', 'origin', '+refs/heads/章-%d:%s' % (int(n), 引)], cwd=根 or ROOT, capture_output=True, timeout=60)
        except Exception:
            return 0
        t = 提交之时(引, 根)
    return t


def 巡印之由(今=None, d=None, 心=None):
    """沙盒（总编辑之兜底之巡）：取云端巡印验之 → ''｜停摆之由。
    〔W910〕心（云端心跳）缺即取 巡() 所读者（_巡之心·所判与所验同一心跳）；末封之章与其章推之时惰取——巡印鲜即⛔取（零请）。"""
    心 = 心 if 心 is not None else _巡之心

    global _巡印之义
    心 = 心 if 心 is not None else _巡之心

    def 章():
        n = 末封之章(心)
        return n, (章推之时(n) if n and n > 0 else 0)
    由, _巡印之义 = 巡印判之义(d if d is not None else _读枝档(巡印枝, 巡印档), 今 or int(time.time()), 章=章)   # 〔W921 X132①〕其义留 _巡印之义（巡() 读之）
    return 由


_巡印之义 = '鲜'   # 〔W921 环6①·X132①〕巡印之由 末判之义（鲜｜随章｜未逾｜无t｜坏｜私）——巡() 唯鲜／随章 许 rc 7；未经 巡印之由（注之）即作鲜（照旧）


def 章之坐(n, 根=None, 标=None):
    """〔W910 复核要害〕「章-n」之封者之坐：其提交之 Claude-Session 之尾（封版.py 之 尾：`…/session_<CLAUDE_CODE_REMOTE_SESSION_ID 去 session_／cse_>`），
    依 心跳.坐() 之取（去 session_／cse_、前三十二字）→ str；无尾、无其枝、读不出 → ''（早止之判即⛔早止）。标（sha）可注（自测）；本地无其物先 fetch 之。"""
    try:
        sha = 标 if 标 is not None else 云端章标(n)
        if not sha:
            return ''
        for 次 in (0, 1):
            r = subprocess.run(['git', 'log', '-1', '--format=%B', sha], cwd=根 or ROOT, capture_output=True, text=True)
            if r.returncode == 0 or 次:
                break
            subprocess.run(['git', 'fetch', '-q', 'origin', 'refs/heads/章-%d' % int(n)], cwd=根 or ROOT, capture_output=True, timeout=60)
        尾 = [x.split(':', 1)[1].strip() for x in r.stdout.split('\n') if x.startswith('Claude-Session:')] if r.returncode == 0 else []
        return re.sub(r'^(session_|cse_)', '', 尾[-1].rstrip('/').rsplit('/', 1)[-1])[:32] if 尾 else ''
    except Exception:
        return ''


def 早止之局(d, n, 含, 旧坐=None):
    """⛔纯判（W910·章推之環之早止）：云端心跳 d、所随之章 n、含（主枝含章-n 否）、旧坐（章-n 之封者·章之坐）→ (rc, 由)：
    0 可止｜1 局悬（主未含、交棒中〔章 None·其宽二十分内巡亦判止〕、心跳之章 ≤n、其坐即旧坐）｜2 读不出｜3 坐之易不可验（旧坐不可取、心跳之坐空或未名）。
    可止：章＝'暂停'（暂停中无可察·⛔问含）；或 含 且心跳之章为 int、≥ n+1、其坐异於旧坐——新坐已接。
    〔复核要害〕封版之坐先 `心跳.py --跳 N+1`、後 `封版.py N --後` 推章-N，至 `--候主 N` 报含方 `--收 N+1`（00_总章.md 三之3、5）：
    章推之时心跳即 {章 N+1, 坐 封者}——单凭章 ≥N+1 即认旧坐为新坐（旧坐推後、收前死，则早止而交棒实未成）。故须见坐之易。"""
    if not isinstance(d, dict):
        return 2, '心跳读不出'
    章 = d.get('章')
    if 章 == '暂停':
        return 0, '暂停中（无可察·解停由 暂停令 --解 同回合验之）'
    try:
        n = int(n)
    except (TypeError, ValueError):
        return 2, '章号读不出'
    if not 含:
        return 1, '主枝未含章-%d' % n
    if not (isinstance(章, int) and not isinstance(章, bool)) or 章 < n + 1:
        return 1, '心跳之章 %s（交棒中、或新坐未接第%d章）' % (章, n + 1)
    坐 = str(d.get('坐') or '')
    if not 旧坐:
        return 3, '章-%d 之封者不可取（其提交无 Claude-Session 之尾）——坐之易不可验' % n
    if 坐 in ('', '未名'):
        return 3, '心跳之坐%s——坐之易不可验' % ('空' if not 坐 else '未名')
    if 坐 == str(旧坐):
        return 1, '心跳之章 %s 之坐即章-%d 之封者 %s（封版之坐未收·新坐未接）' % (章, n, 坐[:12])
    return 0, '主枝含章-%d、心跳之章 %s 之坐 %s 异於封者 %s（新坐已接）' % (n, 章, 坐[:12], str(旧坐)[:12])


def 早止判(d, n, 含, 旧坐=None):
    """⛔纯判：早止之局 之 rc 0 否（可止）。"""
    return 早止之局(d, n, 含, 旧坐)[0] == 0


def 早止(n):
    """`--早止 N`（巡.yml 章推之環每巡後跑·零 token）：读 心跳._远()、主含(N)、章之坐(N) → 早止之局 之 rc（0 可止｜1 局悬｜2 读不出｜3 坐之易不可验）；异常⛔崩（rc 2）。
    環之早止：本 rc 0 且该巡 rc 0、印首「止」连三巡（十五分内无变）方止；環末局悬（末之 rc 1）方续——见 .github/workflows/巡.yml。"""
    try:
        n = int(n)
        import 心跳
        在, d = 心跳._远()
        if not (在 and isinstance(d, dict)):
            print('读不出：云端心跳%s——续' % ('不在' if not 在 else '读不出'))
            return 2
        含 = 主含(n)
        旧坐 = 章之坐(n) if 含 else ''
    except Exception as e:
        print('读不出：%s——续' % str(e)[:200])
        return 2
    rc, 由 = 早止之局(d, n, 含, 旧坐)
    print('%s：%s' % ({0: '可止', 1: '续', 2: '读不出', 3: '续（⛔早止）'}[rc], 由))
    return rc


def 应判(旧言, 应时, 今, 键=None):
    """⛔纯判（闭环·1117 不劣之审）：哨 PR 之真唤（⛔试、⛔私）——同局（键同；键缺即诸真唤）之首唤逾 应之候分 而 巡应 未更於其後
    → 唤而未应之由；否则 ''。
    〔W908 环2(d)〕以同局首唤之时量：旧取末唤，而同局唤隔 唤之隔分（二十）＜应之候分（三十），末唤恒未逾——闭环实死；
    限同局一红：首唤＋应之候 之後已有同局之唤（其唤已带此红）即⛔再红。"""
    真 = [t for t, k in 旧言 if not str(k).startswith(('试', '私', '闸·')) and (键 is None or k == 键)]
    if not 真:
        return ''
    t = min(真)
    try:
        应时 = int(应时 or 0)
    except (TypeError, ValueError):
        应时 = 0
    if 今 - t < 应之候分 * 60 or 应时 >= t:
        return ''
    if any(x >= t + 应之候分 * 60 for x in 真):
        return ''
    return ('⛔ 唤而未应：同局首唤（%s UTC）逾 %d 分而 备份/巡应 未更（末应 %s）——总编辑之坐或已失联、或其订此 PR 之路已断：'
            '作者知悉（开总编辑之会话，令其 subscribe_pr_activity 哨 PR #1、跑 `python3 工具/接棒守.py --巡`）' % (_刻(t), (今 - t) // 60, _刻(应时)))


def 对拍判(印d, 心d, 停在, 限):
    """⛔纯判（常对拍·1117 不劣之审）：云巡所判之心跳（巡印之 心时）与沙盒所读者同一 → 沙盒以 巡判 复其时之判；rc 异 → 不合之由；否则 ''。
    只对 rc 0/2/3（4 关云端之标、1 器败、5 不出於云）。"""
    try:
        印时, 云rc, 心时 = int(印d['时']), int(印d['rc']), int(印d.get('心时') or 0)
        我心时 = int((心d or {}).get('时') or 0)
    except Exception:
        return ''
    if 云rc not in (0, 2, 3) or not 心时 or 我心时 != 心时:
        return ''
    当 = {'止': 0, '派': 2, '解': 3}[巡判(心d, 印时, 限, 停在=停在)[0]]
    if 当 == 云rc:
        return ''
    return ('⚠ 对拍不合：云巡（%s）判 rc=%d，沙盒以同一心跳（时 %d）复其时之判当 rc=%d——GitHub 之判与沙盒异：'
            '查云巡之境（暂停令、心跳之读、主枝之旧）而治之（法用#云巡·常对拍）；本回照沙盒之判' % (印d.get('刻', ''), 云rc, 心时, 当))


def 仓私(仓):
    """→ True 私有｜False 公开｜None 读不出（⛔因读不出而自停）。"""
    try:
        return bool((_接口('GET', '/repos/%s' % 仓) or {}).get('private'))
    except Exception:
        return None


def 私停(仓, 今):
    """仓转私有（Actions 按分计）：章推之環日占数时（W910 前一机终日≈月四万三千分）将耗 autopush 之额度而书停 → 自 disable 巡.yml（環於本巡後见之即止）、唤总编辑降级。→ 1（红）。"""
    import urllib.parse
    由 = '⛔ 仓已转私有（Actions 按分计：章推之環日占数时，将耗 autopush 之额度而书停）——云巡自停（disable 巡.yml·環即止）'
    try:
        _接口('PUT', '/repos/%s/actions/workflows/%s/disable' % (仓, urllib.parse.quote('巡.yml')))
    except Exception as e:
        由 += '——而 disable 不成（%s）：作者於 Actions 页停之' % e
    print(由)
    try:
        号 = 哨PR(仓)
        if 号:
            _接口('POST', '/repos/%s/issues/%d/comments' % (仓, 号), {'body': '【巡警】%s\n\n总编辑：沙盒跑 `python3 工具/接棒守.py --巡`，照其 rc 5 之印降级（兜底之巡每二十分如旧）。\n\n%s'
                                                                         % (由, 警记 % ('私·%d' % 今))})
    except Exception as e:
        print('⛔ 唤不成：%s' % e)
    return 1


def 云端主枝():
    """→ 云端主枝之 sha；读不出即 ''。"""
    r = subprocess.run(['git', 'ls-remote', 'origin', 'refs/heads/' + 主枝], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.split()[0] if r.returncode == 0 and r.stdout.strip() else ''


def 再闸(仓, n, 报=None, 标=None, 今主=None, 派=None, 态=None):
    """合入之卡（rc 4）之唤：workflow_dispatch autopush.yml（ref 章-n·tries 0）令 GitHub 再跑其闸——旧须总编辑醒而手派（1117 GitHub 化之审·D）。→ 印之语。
    〔W908 环2(c)〕章-n 之报（sha 即其标）「败·因 merge」：报之 main_after（merge 败则主枝未进，即其闸之主前）＝今主 → 再派必同败：⛔派、唤并；
      今主已进 → 许一派（同局一派：云巡只於同局未派之唤调本函、派则记 闸记）；主前或今主读不出 → 照旧派（败亦一分即毕）。
    〔W908 环2(b)·复核反例二〕态（合入之卡 之 _卡之态）∈ _候之态（其跑排候／在飞／含此章之治在飞）→ ⛔派：派即顶他人之候跑（并发组只容一候）
      或自顶——卡之语「候其起」与派相悖；下唤再问（未派⛔记，态转「顶」即派）。
    报、标、今主、派（体 → None）、态可注（自测）。"""
    import urllib.parse
    if 态 in _候之态:
        return ('· 再闸⛔派：章-%s %s——派即顶并发组之候跑（并发组只容一候）；下唤再问（同局一派·未派⛔记）'
                % (n, {'候': '之跑被顶而他跑排候', '飞': '之跑在飞', '治': '之果归含此章之治（治在飞）'}[态]))
    try:
        sha = 标 if 标 is not None else 云端章标(int(n))
        if 报 is None:
            import 推报
            报 = 推报.读('章-%s' % n, ROOT)
    except Exception:
        sha, 报 = '', None
    注 = ''
    if isinstance(报, dict) and sha and 报.get('sha') == sha and 报.get('果') == '败' and 报.get('因') == 'merge':
        前 = str(报.get('main_after') or '')
        try:
            今 = 今主 if 今主 is not None else 云端主枝()
        except Exception:
            今 = ''
        冲 = 冲突之档(报)
        if 前 and 今 and 前 == 今:
            return ('⛔ 再闸⛔派：章-%s 之闸败於 merge（%s），而主枝未进（主前＝今主 %s）——再派必同败；唤总编辑并之：'
                    '并「章-%s」入主枝（七账 merge=账并 自并、余档手并），`python3 工具/推.py` 交'
                    % (n, '冲突之档：' + '、'.join(冲) if 冲 else '冲突之档未入报·看 run_url', 今[:12], n))
        if 前 and 今:
            注 = '（merge 之败而主枝已进 %s→%s：许一派）' % (前[:12], 今[:12])
    try:
        (派 or (lambda 体: _接口('POST', '/repos/%s/actions/workflows/%s/dispatches' % (仓, urllib.parse.quote('autopush.yml')), 体)))(
            {'ref': '章-%s' % n, 'inputs': {'tries': '0'}})
        return '%s（ref 章-%s）%s——GitHub 再跑其闸（零 token）；总编辑候其果，二十分後仍卡即再唤（同局⛔复派）' % (再闸之印, n, 注)
    except Exception as e:
        return '⚠ 再闸不成（workflow_dispatch autopush.yml·章-%s：%s）——总编辑照印手派' % (n, str(e)[:120])


# ── ⑥活守〔1119 执行之审·治1〕巡即总编辑之坐之活守（根乙：守之活只靠一触、且只见一坐）──
#   1119 实踩：总编辑之坐 cwd＝/home/user、仓之 .claude/settings.json 不载——开头之钩、Stop（自决之守）、PreToolUse（链之检、续跑之守⑤）俱停：
#   本坐 _器之迹 中 链之检（无参）末迹 11-16T13:12:23；存底守.log 自 11-16 13:17:09 跳至 11-19 16:31:45；同期巡 106 回俱 rc 0，三日无一器见。
#   今沙盒之 --巡 每跑（零 token）：
#   (a) 钩活：_器之迹 末 64KB 里本巡前 60 秒内有 链之检.py（参 []）一行即活；连三巡无方判死（⛔误拦），态记 <git 公目>/钩之态.json（同 存底守.log·⛔入仓）；
#   (b) 存底刻：存底守.log 末一存（✓ 之行）逾十五分即「存底迟」（抓「守在跑却不存」；守方起而未逾一隔⛔算）；
#   (c) 钩死即 Stop 钩不在：以 自决之守.中问() 扫本坐转录自末活之巡以来之答（「自决红」）；首见钩死、其後每见 compact_boundary，
#       补印开头之钩之串（.claude/settings.json 之 SessionStart「startup|compact|clear」原令·⛔另拟）；
#   (d) 每日首巡记本坐昨日之费（费审 之主环「总编辑之坐·<昨日>」·写书之坐之主环行由其复盘记、⛔重计；本坐自开之件（W9xx）之复盘亦记本坐之主环切片——
#       日行让其交（〔1119 执行之审·复核〕⛔重计：见 本坐日行）；本坐上下文逾三十万即印「减本坐之活」（一日一印）；
#   (e) 落巡应带「钩」「存底刻」「钩死起」：云巡唯见存底迟逾二十四时，态变方唤而红（键唯存底迟之起）；旧巡应无此三键⛔红。
#       〔W910〕钩死⛔作红与唤之由：钩复载已弃（方法账「钩复载…弃」·以巡代钩——本坐 cwd 为 /home/user、仓之钩永不载，
#       (c) 每巡代扫自决、代印开头之串），钩死即已裁之常态；钩之态仍记於巡应、沙盒之巡仍印其 ⚠。
#   诸印俱走 stderr——stdout 仍只「止」或旧印（云巡之对拍⛔乱；〔W911 重造〕唯 ⑧ 上下文之察 於「止」之次行印一行·首行恒「止」）。回：删此节与 巡应之体 之三键即复旧。
钩之态档 = os.path.join(os.path.dirname(锁档), '钩之态.json')     # <git 公目>（同 锁档·⛔再跑 git）
迹档 = os.path.join(ROOT, '_器之迹.jsonl')
迹尾 = 64 * 1024
钩之窗秒 = 60
钩死之巡 = 3
存底迟分 = 15
活守之界时 = 24
录首读 = 4 * 1024 * 1024     # 初跑（无态）：转录自末 4MB 读起（⛔重扫三十兆）；换档（坑62）：新档自首——俱以「扫自」之时滤之


def _迹时(s):
    """_器之迹 之 t（「%Y-%m-%dT%H:%M:%S」·UTC）→ epoch；坏即 0。"""
    import calendar
    try:
        return calendar.timegm(time.strptime(str(s)[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return 0


def _录时(s):
    """转录之 timestamp（「2026-11-16T12:57:39.027Z」）→ epoch；坏即 0。"""
    from datetime import datetime, timezone
    try:
        t = datetime.fromisoformat(str(s).replace('Z', '+00:00'))
        return int((t if t.tzinfo else t.replace(tzinfo=timezone.utc)).timestamp())
    except Exception:
        return 0


def _读尾(档, n=迹尾):
    """→ 档末 n 字节之诸行（文本；首行或残即弃）；读不出即 []。"""
    try:
        with open(档, 'rb') as f:
            f.seek(0, 2)
            大 = f.tell()
            f.seek(max(0, 大 - n))
            b = f.read()
    except Exception:
        return []
    行 = b.decode('utf-8', 'ignore').split('\n')
    return 行[1:] if 大 > n else 行


def 钩活判(迹行, 今, 窗=钩之窗秒):
    """⛔纯判（治1·a）：_器之迹 之诸行（文本或 dict）里，[今-窗, 今+1] 之内有 链之检.py（参 []·PreToolUse 钩所跑）一行 → True。
    带参之 链之检（--自测 等）⛔算：唯钩无参。"""
    for l in 迹行:
        d = l if isinstance(l, dict) else None
        if d is None:
            if '链之检.py' not in l and '\\u94fe\\u4e4b\\u68c0' not in l:     # 速滤（_账 以 ensure_ascii=False 写；转义之形亦认）
                continue
            try:
                d = json.loads(l)
            except Exception:
                continue
        if isinstance(d, dict) and d.get('器') == '链之检.py' and d.get('参') == [] and 今 - 窗 <= _迹时(d.get('t')) <= 今 + 1:
            return True
    return False


def 钩态推(旧, 活, 今, 界=钩死之巡):
    """⛔纯判（治1·a）：旧态、本巡钩活否 → 新态。钩：活｜疑（缺而未满 界 巡）｜死；无钩＝连缺之巡数；首缺＝连缺之首巡之时；
    钩死起＝判死时取首缺（⛔取判死之巡：三巡之前已缺）。活即清之。"""
    新 = dict(旧 or {})
    if 活:
        新.update(钩='活', 无钩=0, 首缺=None, 钩死起=None, 末活=今)
    else:
        n = int(新.get('无钩') or 0) + 1
        首 = 新.get('首缺') or 今
        新.update(无钩=n, 首缺=首, 钩='死' if n >= 界 else '疑', 钩死起=首 if n >= 界 else None)
    return 新


def 存底末刻(行们, 今):
    """⛔纯判（治1·b）：存底守.log 之诸行 → (末一存之时, 末起之时)（无即 0）。存＝「✓」之行（已存、或树未改而无须存）；「⛔」之行⛔算存。
    log 之刻「MM-DD HH:MM:SS」（UTC·无年）：取今之年，逾今一日即作去年。"""
    import calendar
    存 = 起 = 0
    年 = time.gmtime(今).tm_year
    for l in 行们:
        m = re.match(r'(\d\d)-(\d\d) (\d\d):(\d\d):(\d\d) (.*)', l or '')
        if not m:
            continue
        try:
            t = calendar.timegm((年, int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), 0, 0, 0))
            if t > 今 + 86400:
                t = calendar.timegm((年 - 1, int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), 0, 0, 0))
        except Exception:
            continue
        体 = m.group(6).lstrip()
        if 体.startswith('✓'):
            存 = max(存, t)
        elif 体.startswith('起 '):
            起 = max(起, t)
    return 存, 起


def 存底迟判(存, 起, 今, 守先在=True, 界=存底迟分):
    """⛔纯判（治1·b）→ ''｜「存底迟」之由。守本在跑、其起晚於末存而未逾一隔（五分＋一分）→ 候其首存（⛔迟）；
    守係本巡方起（先不在）→ ⛔宽（机换、守死俱须见）。"""
    if 存 and 今 - 存 <= 界 * 60:
        return ''
    if 守先在 and 起 and 起 >= 存 and 今 - 起 <= 6 * 60:
        return ''
    尾 = '（守今方起）' if not 守先在 else ''
    if not 存:
        return '⚠ 存底迟：存底守.log 无一存之行（缺）%s——`python3 工具/存底守.py --一回` 手存一回、`--状` 查其守' % 尾
    return ('⚠ 存底迟：存底守.log 末一存 %s UTC（%d 分前，逾 %d 分）%s——守在跑却不存、或守死：'
            '`python3 工具/存底守.py --一回` 手存一回、`--状` 查其守（法用#防失稿三锁）' % (_刻(存), (今 - 存) // 60, 界, 尾))


def 本坐转录(根=None, 坐=None):
    """→ 本坐之转录（~/.claude/projects/*/<CLAUDE_CODE_SESSION_ID>.jsonl 之最新者——会话换目录而续即另开同名之档·坑62）；无即 ''。"""
    import glob
    根 = 根 or os.path.expanduser('~/.claude/projects')
    坐 = 坐 if 坐 is not None else os.environ.get('CLAUDE_CODE_SESSION_ID', '')
    诸 = glob.glob(os.path.join(根, '*', 坐 + '.jsonl')) if 坐 else []
    return max(诸, key=os.path.getmtime) if 诸 else ''


def 转录之增(路, 偏, 自=0):
    """→ (新偏, 诸答 [(时, 文)], compact 之数, 末上下文)：读 路 自 偏（字节）至末一完整之行；自＞0 即只计其时 ≥ 自 之行
    （初跑、换档之滤）。上下文＝增量里末一回之 自决之守.一回之上下文（同一把尺）；无即 0。"""
    import 自决之守
    答, 压, 上 = [], 0, 0
    try:
        with open(路, 'rb') as f:
            f.seek(0, 2)
            大 = f.tell()
            偏 = 偏 if 0 <= 偏 <= 大 else 0
            f.seek(偏)
            b = f.read()
    except Exception:
        return 偏, [], 0, 0
    末 = b.rfind(b'\n')
    if 末 < 0:
        return 偏, [], 0, 0
    for l in b[:末 + 1].split(b'\n'):
        if not l.strip():
            continue
        try:
            d = json.loads(l)
        except Exception:
            continue
        n = 自决之守.一回之上下文(d)
        if n:
            上 = n
        if 自 and _录时(d.get('timestamp')) < 自:
            continue
        if d.get('type') == 'system' and d.get('subtype') == 'compact_boundary':
            压 += 1
        elif d.get('type') == 'assistant':
            for x in (d.get('message') or {}).get('content') or []:
                if isinstance(x, dict) and x.get('type') == 'text' and x.get('text'):
                    答.append((_录时(d.get('timestamp')), x['text']))
    return 偏 + 末 + 1, 答, 压, 上


def 开头之串(根=ROOT):
    """→ .claude/settings.json 之 SessionStart（matcher 含 compact）之令——补印即跑此令（⛔另拟·同一把尺）；无即 ''。"""
    try:
        h = json.load(open(os.path.join(根, '.claude', 'settings.json'), encoding='utf-8')).get('hooks', {})
        for m in h.get('SessionStart', []):
            if 'compact' in (m.get('matcher') or ''):
                for x in m.get('hooks', []):
                    if x.get('command'):
                        return x['command']
    except Exception:
        pass
    return ''


def 补印(由, 根=ROOT):
    """钩死之补（治1·c）：跑 开头之串（CLAUDE_PROJECT_DIR＝仓根），其印归 stderr——总章首段、法用之守 --报 --首 前六行、费哨 --章、升级链末五。"""
    令 = 开头之串(根)
    if not 令:
        sys.stderr.write('⚠ 补印不成：.claude/settings.json 无 SessionStart（compact）之令\n')
        return 1
    try:
        r = subprocess.run(['sh', '-c', 令], cwd=根, env=dict(os.environ, CLAUDE_PROJECT_DIR=根), capture_output=True, timeout=120)
        出 = r.stdout.decode('utf-8', 'replace').rstrip()      # 令中之 cut -c 或截字於半（其末五行）——⛔因之全败
    except Exception as e:
        出 = '⚠ 补印之令败：%s' % e
    sys.stderr.write('── 补印开头之钩（%s·本坐之钩不载，代 SessionStart「startup|compact|clear」）──\n%s\n── 补印毕 ──\n' % (由, 出))
    return 0


def 记费之参(日):
    """⛔纯（治1·d）：今日（UTC「YYYY-MM-DD」）→ (名「总编辑之坐·<昨日>」, 昨日 00:00Z, 今日 00:00Z)——费审 --记主 之参。"""
    from datetime import datetime, timedelta
    昨 = (datetime.strptime(日, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    return '总编辑之坐·' + 昨, 昨 + 'T00:00:00Z', 日 + 'T00:00:00Z'


本坐件式 = re.compile(r'W9\d\d$')     # 〔1119 执行之审·复核〕总编辑之坐自开之件（W901—W906…；写书之坐之件今 W1xx）——其复盘於本坐记「主环:<起>」之切片
_日行之键 = (('回', '来回'), ('新', '新入'), ('建', '缓存建'), ('读', '缓存读'), ('出', '产出'), ('全', '全量'), ('金', '美元'))


def _秒(s):
    """「2026-11-19T17:56Z」「2026-11-19T17:56」「2026-11-19T00:00:00Z」→ epoch；坏即 None。"""
    m = re.match(r'(\d{4}-\d\d-\d\dT\d\d:\d\d)(:\d\d)?', str(s or ''))
    return _录时(m.group(1) + (m.group(2) or ':00') + 'Z') if m else None


def _iso(t):
    """epoch → 「%Y-%m-%dT%H:%M:%S」（⛔尾 Z：费审 以字串比时——同 复盘 之「…T17:56」，起於整秒之回（17:56:00.5Z）⛔漏）。"""
    return time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(t))


def 本坐日行(日, 主, 件们, 行们):
    """⛔纯（治1·d；〔1119 执行之审·复核〕⛔与本坐自开之件之主环切片重计）→ (名, 起, 止, 行｜None, 让[(件, 美元)], 截)。
    主（自 ISO, 至 ISO）→ 费审.主环 之果（dict：回 新 建 读 出 全 金 末…）｜None。
    复盘.py 遇件有「起」即记「主环:<起>」（名「W·题」）＝本坐 [件起, 复盘之时) 之费——总编辑自开之件（W9xx）其切片与日行同出一坐、同一段：
      费账已有其切片 → 日行减其与 [起, 止) 之交（切 R 自 s 起：交＝min(R, 主(s, 止)) − 主(s, 起)〔s<起〕，逐项、⛔负）；
      件「进行」而切片未记 → 日行让 [max(件起, 起), 止)（其复盘将记 [件起, 复盘之时)，含之）；
      件已了而无切片（复盘未记主环）→ ⛔让（其费唯日行记之）。
    本坐并行之件（11-19 W905 起 17:56、W906 起 18:51 俱进行）：其切片各计其段而相叠（复盘之事）——日行逐件减（⛔以并集减），
      费账之合方每回一计；减逾日行之某项即截零（截＝True·印之：其叠逾本坐件外之活，费账之合偏多其逾）。
    昨日无来回、或让尽 → 行 None（⛔记零行）。"""
    名, 起, 止 = 记费之参(日)
    r = 主(起, 止)
    if not r or not r.get('回'):
        return 名, 起, 止, None, [], False
    t起, t止 = _秒(起), _秒(止)
    减 = {k: 0.0 for k, _ in _日行之键}
    让 = []
    for x in 件们 or []:
        wid, s = str(x.get('id') or ''), _秒(x.get('起'))
        if not 本坐件式.fullmatch(wid) or s is None or s >= t止:
            continue
        切 = next((y for y in 行们 or [] if str(y.get('键', '')).startswith('主环:') and str(y.get('名', '')).startswith(wid + '·')), None)
        if 切 is not None:
            s = _秒(切.get('时')) or _秒(str(切['键'])[3:]) or s
            if s >= t止:
                continue
            a1 = 主(_iso(s), 止) or {}
            a0 = (主(_iso(s), 起) or {}) if s < t起 else {}
            交 = {k: max(0.0, min(float(切.get(f) or 0), float(a1.get(k) or 0)) - float(a0.get(k) or 0)) for k, f in _日行之键}
        elif x.get('状态') == '进行':
            a = 主(_iso(max(s, t起)), 止) or {}
            交 = {k: float(a.get(k) or 0) for k, _ in _日行之键}
        else:
            continue
        if 交['回'] or 交['金']:
            让.append((wid, round(交['金'], 4)))
            for k in 减:
                减[k] += 交[k]
    行 = dict(r)
    截 = False
    for k, _ in _日行之键:
        v = float(r.get(k) or 0) - 减[k]
        截 = 截 or v < -1e-9
        v = max(0.0, v)
        行[k] = v if k == '金' else int(round(v))
    if not 行['回']:
        return 名, 起, 止, None, 让, 截
    return 名, 起, 止, 行, 让, 截


def 记本坐之费(日, root=ROOT, f=None):
    """每日首巡（治1·d）：本坐昨日之主环（费审.主环 [昨日 00:00Z, 日 00:00Z)）记「总编辑之坐·<昨日>」一行入费账（零 token；键同 `费审 --记主`）。
    〔1119 执行之审·复核〕本坐自开之件（W9xx）之复盘所记之主环切片与此重——日行让之（本坐日行）：费哨⛔两回计（11-19 W905／W906 实踩）。
    昨日无来回（或让尽）即⛔记（⛔记零行）。印归 stderr。f：转录之档（自测注之；None 即 主档们）。→ rc。"""
    try:
        import 费审
        try:
            件们 = json.load(open(os.path.join(root, '设定', '工作流账.json'), encoding='utf-8')).get('件') or []
        except Exception:
            件们 = []
        try:
            行们 = json.load(open(os.path.join(root, '设定', '费账.json'), encoding='utf-8')).get('行') or []
        except Exception:
            行们 = []
        名, 起, 止, 行, 让, 截 = 本坐日行(日, lambda a, b: 费审.主环(a, f=f, 至=b), 件们, 行们)
    except Exception as e:
        sys.stderr.write('⚠ 本坐之费量不成（%s）——⛔记\n' % e)
        return 1
    if 让:
        sys.stderr.write('· 本坐日行让本坐自开之件之主环（⛔重计）：%s%s\n' % ('、'.join('%s $%.2f' % kv for kv in 让),
                         '——⚠ 让逾日行而截零（本坐并行之件之切相叠·复盘.py 之事）' if 截 else ''))
    if 行 is None:
        sys.stderr.write('· 本坐 %s 无来回%s——⛔记费\n' % (起[:10], '（让尽）' if 让 else ''))
        return 0
    import contextlib
    with contextlib.redirect_stdout(sys.stderr):
        费审.记('主环:%s' % 起, 名, [行], None, root, 时=起)
    return 0


def 活守(今=None, 守先在=True, 态档=None, 迹=None, 志=None, 录=None, 补=None, 记费=None):
    """沙盒之 --巡（〔1119 执行之审·治1〕a—d）→ 新态（落巡应用其「钩」「存底刻」「钩死起」）。诸印俱以 print 出，主调以 redirect_stdout(stderr) 包之。
    补、记费 可注（自测）；态档、迹、志、录 可注（回放）。"""
    今 = 今 or int(time.time())
    态档 = 态档 or 钩之态档
    try:
        旧 = json.load(open(态档, encoding='utf-8'))
        旧 = 旧 if isinstance(旧, dict) else {}
    except Exception:
        旧 = {}
    # (a) 钩活
    活 = 钩活判(_读尾(迹 or 迹档), 今)
    态 = 钩态推(旧, 活, 今)
    # (b) 存底刻
    if 志 is None:
        try:
            import 存底守
            志 = 存底守.日志
        except Exception:
            志 = os.path.join(_仓目(), '存底守.log')
    try:
        志行 = open(志, encoding='utf-8', errors='ignore').read().split('\n')[-400:]
    except Exception:
        志行 = []
    存, 起 = 存底末刻(志行, 今)
    态['存底刻'] = 存 or None
    迟 = 存底迟判(存, 起, 今, 守先在)
    if 迟:
        print(迟)
    # (c) 钩不活：扫本坐转录（自决）、补印
    路 = 本坐转录() if 录 is None else 录
    上, 决 = 0, None                 # 决：〔W908 环12②〕自决之代扫之果（钩死而转录可读方扫）——入巡应，云巡读之
    if 路:
        换 = 路 != 旧.get('录') or not isinstance(旧.get('偏'), int)
        if 换:                       # 初跑：自末 4MB 起；换档（坑62·会话换目录而续）：新档自首起——俱以 扫自 之时滤之
            try:
                大 = os.path.getsize(路)
            except Exception:
                大 = 0
            偏 = 0 if 旧.get('录') else max(0, 大 - 录首读)
        else:
            偏 = 旧['偏']
        扫自 = int(旧.get('扫自') or (今 - 35 * 60))
        新偏, 答, 压, 上 = 转录之增(路, 偏, 扫自 - 60)
        if 态['钩'] == '死':
            import 自决之守
            中 = []
            for t, 文 in 答:
                片 = 自决之守.中问(文)
                if 片 and 片 not in [x for _, x in 中]:
                    中.append((t, 片))
            决 = 自决之果(中, 今, 旧.get('自决首'))
            for t, 片 in 中[-5:]:
                print('⛔ 自决红：「%s」（%s UTC）——钩死而 Stop 之自决之守不在：第一律⛔候作者之许，照最好之法自决自办、办毕再报' % (片.strip(), _刻(t)))
            print('⚠ 钩死（连 %d 巡无 链之检.py 之迹·起 %s UTC）：本坐之钩不载——开头之钩、Stop（自决之守）、PreToolUse（链之检、续跑之守⑤）俱停'
                  '（钩复载已弃·以巡代钩：本巡代扫自决、代印开头之串）' % (态['无钩'], _刻(态['钩死起'])))
            if 旧.get('钩') != '死':
                (补 or 补印)('首见钩死')
            elif 压:
                (补 or 补印)('compact 之後 %d 回' % 压)
        if 态['钩'] != '疑':          # 疑（缺而未满三巡）⛔进偏：判死之巡自末活之处扫起（⛔漏其间之答）
            态.update(录=路, 偏=新偏, 扫自=今)
        else:
            态.update(录=路, 偏=偏, 扫自=扫自)
    elif 态['钩'] == '死':
        print('⚠ 本坐转录读不出（CLAUDE_CODE_SESSION_ID 缺或档不在）——钩死而自决⛔能代扫（缺）')
    态['自决'] = 决 or {'扫至': None, '红': 0, '片': [], '首': None,
                     '由': {'活': '钩活（Stop 之自决之守在·⛔代扫）', '疑': '钩疑（未满三巡·⛔扫）'}.get(态['钩'], '转录读不出（⛔能代扫）')}
    态['自决首'] = 态['自决']['首']
    # (d) 每日首巡：记本坐昨日之费；上下文逾三十万即印「减本坐之活」（一日一印）
    日 = time.strftime('%Y-%m-%d', time.gmtime(今))
    if 旧.get('日') != 日:
        try:
            (记费 or 记本坐之费)(日)
        except Exception as e:
            print('⚠ 记本坐之费不成：%s' % e)
        态['日'] = 日
    try:
        import 自决之守
        界 = 自决之守.压之界
    except Exception:
        界 = 300000
    上 = 上 or int(旧.get('上下文') or 0)
    态['上下文'] = 上
    if 上 > 界 and 旧.get('压日') != 日:
        print('⚠ 减本坐之活：本坐上下文约 %d 万（逾三十万）——读档、审、算交给子席或 Workflow，主坐只裁；'
              '与作者对谈即照常令 1024 令（压缩对话）② 於答末一行请作者按 /compact（〔1119 执行之审·复核〕器⛔与常令分歧·删否待总编辑另裁）' % round(上 / 10000))
        态['压日'] = 日
    # (e)〔执行之制·治13(b)（1124·482 主环收批）〕立停之巡：工作流账「进行」之件带 Run（--标 W wf_）者，跑中之费对其估——逾 1.5 倍即印立停
    try:
        for 行 in 立停之巡(今=今):
            print(行)
    except Exception as e:
        print('⚠ 立停之巡不成：%s' % e)
    态['末巡'] = 今
    try:
        tmp = 态档 + '.tmp%d' % os.getpid()
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(态, f, ensure_ascii=False)
        os.replace(tmp, 态档)
    except Exception as e:
        print('⚠ 钩之态落不成：%s' % e)
    return 态


立停之鲜 = 3600          # Run 之目录一时内有动方算「跑中」（已毕之 Run ⛔每巡复印立停）


def 立停之巡(今=None, 件们=None, 跑中=None, 估之=None, 鲜之=None):
    """〔执行之制·治13(b)〕→ [印行]。件们（工作流账之件）、跑中（费哨.跑中）、估之（复盘.估之元）、鲜之（rid → 末动之秒｜None）可注（自测）。
    唯「进行」之件、其末一 Run 跑中（目录一时内有动）者对估；逾 1.5 倍即「立停：TaskStop <id>」；件无估即印「无估」（⛔当 $0·治13(c)）。"""
    今 = 今 or int(time.time())
    if 件们 is None:
        try:
            件们 = json.load(open(os.path.join(_仓目(), '设定', '工作流账.json'), encoding='utf-8'))['件']
        except Exception:
            return []
    if 跑中 is None:
        import 费哨
        跑中 = 费哨.跑中
    if 估之 is None:
        import 复盘
        估之 = 复盘.估之元
    if 鲜之 is None:
        def 鲜之(rid):
            import 费审
            d = 费审.找目录(rid)
            if not d:
                return None
            try:
                return max([os.path.getmtime(os.path.join(a, f)) for a, _, fs in os.walk(d) for f in fs] or [os.path.getmtime(d)])
            except Exception:
                return None
    出 = []
    for x in 件们 or []:
        if x.get('状态') != '进行' or not x.get('Run'):
            continue
        rid = x['Run'][-1]
        t = 鲜之(rid)
        if t is None or 今 - t > 立停之鲜:
            continue
        估 = 估之(x.get('id'))
        if not 估:
            出.append('⚠ 立停之巡：%s 跑中 %s 而件无估（工作流账之预估、方案之费俱无 $）——⛔当 $0，补估（治13(c)·无估之件）' % (x.get('id'), rid))
            continue
        逾, 述 = 跑中(rid, 估)
        if 逾:
            出.append('⛔ 立停：TaskStop %s（%s %s）——%s' % (rid, x.get('id'), str(x.get('名', ''))[:20], 述))
    return 出


def _活守之起(应d, 今, 界时=活守之界时):
    """⛔纯（治1·e；W908 环2(a)；W910）：巡应 → None（旧巡应·无三键、读不出）｜(应时, 存底迟起)——末一存逾 界时 者取其刻（未逾 0）。
    活守判 与 活守之键 同经此（⛔另造一把尺）。〔W910〕钩死⛔入（钩复载已弃·以巡代钩：已裁之常态⛔红⛔唤）——钩之态只记於巡应。"""
    if not isinstance(应d, dict) or any(k not in 应d for k in ('钩', '存底刻', '钩死起')):
        return None
    try:
        应时 = int(应d.get('时') or 0) or 今
        存 = int(应d.get('存底刻') or 0)
    except (TypeError, ValueError):
        return None
    return 应时, (存 if (存 and 应时 - 存 >= 界时 * 3600) else 0)


def 活守判(应d, 今, 界时=活守之界时):
    """⛔纯判（治1·e·云巡）：巡应 → ''｜红之由。旧巡应（无「钩」「存底刻」「钩死起」三键）→ ''（⛔红）。
    其久以巡应之时量（沙盒所见；巡应陈旧係坐死，归 应判）；唯末一存逾 界时 → 红。
    〔W910〕钩死逾 界时 ⛔红：钩复载已弃（以巡代钩·沙盒之巡每巡代扫自决、代印开头之串）——已知、已裁之常态之空警（虫洞⛔）。"""
    起 = _活守之起(应d, 今, 界时)
    if not 起 or not 起[1]:
        return ''
    应时, 存 = 起
    return ('⛔ 总编辑之坐之活守逾 %d 时未复（巡应 %s UTC）：存底迟 %d 时（末一存 %s UTC）——作者知悉；'
            '总编辑醒即跑 `python3 工具/接棒守.py --巡` 照其 stderr 之印办（存底迟即 `python3 工具/存底守.py --一回`）'
            % (界时, _刻(应时), (应时 - 存) // 3600, _刻(存)))


def 活守之键(应d, 今, 界时=活守之界时):
    """⛔纯（W908 环2(a)；W910）：巡应 → (键, 自)｜('', 0)。键「活守·<存底迟起>」（UTC 至分）——态变方唤：
    存底迟起（或复存再迟）即易其键而唤；态不变即恒一键、⛔再唤。〔W910〕键唯存底迟之起定：钩死、复活再死俱⛔易其键（⛔红⛔唤·见 活守判）。
    自＝此键之言最早可落之时（存底迟起＋界时，留十分）——查旧言自此（⛔只查今日）。"""
    起 = _活守之起(应d, 今, 界时)
    if not 起 or not 起[1]:
        return '', 0
    return '活守·%s' % time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime(起[1])), 起[1] + 界时 * 3600 - 600


def _诸键(仓, 号, 自):
    """哨 PR 上 github-actions 自 自（epoch）以来所留之 警记 之键（分页·至多十页）。"""
    import re as _re
    起 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(max(0, int(自 or 0))))
    键们 = set()
    for 页 in range(1, 11):
        言 = _接口('GET', '/repos/%s/issues/%d/comments?per_page=100&page=%d&since=%s' % (仓, 号, 页, 起)) or []
        for c in 言:
            m = _re.search(r'<!-- 巡警:(.+?) -->', c.get('body') or '')
            if m and (c.get('user') or {}).get('type') == 'Bot':
                键们.add(m.group(1))
        if len(言) < 100:
            break
    return 键们


def _暂停中(心=None):
    """〔1119 执行之审·复核〕暂停否：巡() 所读之心跳之章「暂停」、或 暂停令.在()[0]（读不出即否）。"""
    心 = _巡之心 if 心 is None else 心
    if isinstance(心, dict) and 心.get('章') == '暂停':
        return True
    try:
        import 暂停令
        return bool(暂停令.在()[0])
    except Exception:
        return False


def 活守之巡(仓, 今, 应d=None, 号=None, 键们=None, 发=None, 停=None):
    """云巡（rc 0 之跑·治1·e）：活守判 红（〔W910〕唯存底迟·钩死⛔红⛔唤）→ 态变方唤（哨 PR 一言，键 活守之键「活守·<存底迟起>」）而红（rc 1）；
    此态已唤 → 0（红随唤·⛔每五分一邮）；无事 → 0。〔W908 环2(a)〕旧键「活守·<日>」：钩死不复即每日一空唤一红。
    〔1119 执行之审·复核〕暂停中（停 None 即 _暂停中()）→ 只印、0：总章 §三.5 暂停令「三令俱停」，正为免空唤——
    活守之巡⛔为暂停中唯一之新唤源（巡应停於末回之态，存底迟逾二十四时即恒红）。"""
    应d = _读枝档(巡应枝, 巡应档) if 应d is None else 应d
    由 = 活守判(应d, 今)
    if not 由:
        return 0
    if _暂停中() if 停 is None else 停:
        print('· 暂停中⛔唤（活守）：%s' % 由)
        return 0
    print(由)
    键, 自 = 活守之键(应d, 今)
    try:
        号 = 哨PR(仓) if 号 is None else 号
        if not 号:
            print('⛔ 哨 PR（头枝 %s）不在——唤不得：总编辑立之、订之' % 巡警枝)
            return 1
        if 键 in (_诸键(仓, 号, 自) if 键们 is None else 键们):
            print('· 活守此态已唤（%s）——⛔再唤（态变方唤；红随唤）' % 键)
            return 0
        体 = ('【巡警·活守】%s\n\n总编辑：醒即沙盒跑 `python3 工具/接棒守.py --巡`，照其 stderr 之印办（存底迟、自决红）。\n\n'
              '⚠ 本跑红——哨 PR 之言即达作者（态变方唤）。\n\n%s' % (由, 警记 % 键))
        (发 or (lambda b: _接口('POST', '/repos/%s/issues/%d/comments' % (仓, 号), {'body': b})))(体)
        print('✓ 已唤（哨 PR #%s·%s）' % (号, 键))
        return 1
    except Exception as e:
        print('⛔ 唤不成：%s' % e)
        return 1


# ── ⑦自决之机·GitHub 之半〔W908 环12·作者 1119 令「GitHub 能否时刻提醒你……让这件事完全奏效」〕──
#   ①沙盒之 --巡 印之首行＝00_总章.md「第一律·自决」之首句（唯一之源·随仓进化；⛔另写其文）——读不得即「⚠ 第一律读不得」；
#   ②钩死之自决代扫（⑥活守 (c)·自决之守.中问 同尺）之果——扫至、红、片、首（红之首见之刻）——入每巡既落之 备份/巡应（⛔另立枝）；
#   ③云巡（诸 rc 俱验·私停之後）读巡应：自决红未清 → 哨 PR 一言唤总编辑之坐，附其片与第一律之句（同局一唤：键「自决·<首>」）而红；
#     暂停中只印（作者亲令之停·候其令下合第一律）；无红零 API。回：删此节、活守之「决」、巡应之体之「自决」、云巡之 自决之巡 即复旧。
总章档 = '00_总章.md'


def 第一律之句(根=ROOT):
    """⛔纯（读档·W908 环12①）：00_总章.md 首「**★第一律·自决（…）：」之体之首句（至括、引之外之首「。」）——照录（⛔另写）；读不得即 ''。"""
    try:
        文 = open(os.path.join(根, 总章档), encoding='utf-8').read()
    except Exception:
        return ''
    m = re.search(r'^\*\*★?第一律·自决', 文, re.M)
    if not m:
        return ''
    行, 深, 起 = 文[m.start():].split('\n', 1)[0], 0, None
    for i, ch in enumerate(行):
        if ch in '（(「『':
            深 += 1
        elif ch in '）)」』':
            深 = max(0, 深 - 1)
        elif 深 == 0 and ch == '：' and 起 is None:
            起 = i + 1
        elif 深 == 0 and ch == '。' and 起 is not None:
            return 行[起:i + 1].strip()
    return ''


def 第一律之印(根=ROOT):
    """→ 「第一律·自决（00_总章.md）：<首句>」｜「⚠ 第一律读不得……」——--巡 之首行、自决之唤之言同取此（⛔两写）。"""
    句 = 第一律之句(根)
    return ('第一律·自决（%s）：%s' % (总章档, 句)) if 句 else '⚠ 第一律读不得（%s 首「第一律·自决」之首句取不出）' % 总章档


def 自决之果(中, 今, 旧首=None):
    """⛔纯（W908 环12②）：本巡代扫所中 [(时, 片)] → 巡应之「自决」{扫至, 红, 片（末三·各≤80 字）, 首}。
    首＝红之首见之刻（转录之时）：连红之巡承旧首（同局）；红 0 即清（首 None）——云巡之键取之（同局一唤）。"""
    红 = len(中)
    return {'扫至': 今, '红': 红, '片': [str(x).strip()[:80] for _, x in 中[-3:]],
            '首': (旧首 or min(t for t, _ in 中) or 今) if 红 else None}


def 自决之键(应d):
    """⛔纯判（W908 环12③）：巡应 → (键, 决)｜('', None)。「自决」之红＞0（未清）→ 键「自决·<首·UTC 至分>」；
    旧巡应（无「自决」）、红 0、坏 → ('', None)（⛔红）。"""
    决 = 应d.get('自决') if isinstance(应d, dict) else None
    if not isinstance(决, dict):
        return '', None
    try:
        红, 首 = int(决.get('红') or 0), int(决.get('首') or 0) or int(应d.get('时') or 0)
    except (TypeError, ValueError):
        return '', None
    if 红 <= 0:
        return '', None
    return '自决·' + time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime(首)), 决


def 自决之巡(仓, 今, 应d=None, 号=None, 键们=None, 发=None, 停=None, 根=ROOT):
    """云巡（W908 环12③）：巡应之「自决」红未清 → 哨 PR 一言唤总编辑之坐（附其片与第一律之句）而红（rc 1）；
    同局（键「自决·<红之首见之刻>」）已唤 → 0（同局一唤·红随唤）；无红、旧巡应 → 0（零 API）；暂停中（停 None 即 _暂停中()）→ 只印、0。"""
    应d = _读枝档(巡应枝, 巡应档) if 应d is None else 应d
    键, 决 = 自决之键(应d)
    if not 键:
        return 0
    片 = '｜'.join('「%s」' % x for x in (决.get('片') or [])) or '（片缺）'
    由 = ('⛔ 自决红未清：总编辑之坐之答中「问作者／候作者之许」之式 %s 处（代扫至 %s UTC·自决之守.中问 同尺）：%s'
          % (决.get('红'), _刻(决.get('扫至')), 片))
    if _暂停中() if 停 is None else 停:
        print('· 暂停中⛔唤（自决）：%s' % 由)
        return 0
    print(由)
    try:
        号 = 哨PR(仓) if 号 is None else 号
        if not 号:
            print('⛔ 哨 PR（头枝 %s）不在——唤不得：总编辑立之、订之' % 巡警枝)
            return 1
        if 键 in (_诸键(仓, 号, (int(决.get('首') or 0) or 今) - 600) if 键们 is None else 键们):
            print('· 自决此局已唤（%s）——⛔再唤（同局一唤；红随唤）' % 键)
            return 0
        体 = ('【巡警·自决】%s\n\n%s\n\n总编辑：醒即照第一律自决自办（⛔候作者之许、⛔列选项请作者择），办毕再报；'
              '并沙盒跑 `python3 工具/接棒守.py --巡`（代扫其後之答，无新红即清）。\n\n'
              '⚠ 本跑红——哨 PR 之言即达作者（同局一唤）。\n\n%s' % (由, 第一律之印(根), 警记 % 键))
        (发 or (lambda b: _接口('POST', '/repos/%s/issues/%d/comments' % (仓, 号), {'body': b})))(体)
        print('✓ 已唤（哨 PR #%s·%s）' % (号, 键))
        return 1
    except Exception as e:
        print('⛔ 唤不成：%s' % e)
        return 1


def 云巡(试=False):
    """GitHub（巡.yml）之跑：巡() → 落巡印 → 仓私即自停 → 非止即唤（哨 PR 留一言；唤而未应即红）。→ 0 绿｜1 红（随唤：停逾九十分、器败、合入之卡、唤而未应；唤不成；私停）。"""
    import io, contextlib, traceback
    global _巡之心, _卡之态
    今 = int(time.time())
    _巡之心, _卡之态 = None, ''
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rc = 巡()
    except Exception:
        rc = 1
        buf.write('⛔ 云巡自败：\n' + traceback.format_exc()[-1500:])
    印 = buf.getvalue()
    print(印.rstrip())
    d = _巡之心
    仓 = os.environ.get('GITHUB_REPOSITORY', '')
    跑 = '%s/%s/actions/runs/%s' % (os.environ.get('GITHUB_SERVER_URL', 'https://github.com'), 仓, os.environ.get('GITHUB_RUN_ID', ''))
    私 = 仓私(仓) is True
    期 = 云巡之期(仓) if (仓 and not 试) else None      # 〔W921 环6⑤〕巡.yml 近十回 schedule 之隔之中位（取不得 ⛔书）
    if not 落巡印(rc, 印, 今, 跑, 心=d, 私=私, 源=巡之源(试), 期=期):
        print('⚠ 巡印落不成（备份/巡印）')
    if 私 and not 试:
        return 私停(仓, 今)
    应 = {} if 试 else (_读枝档(巡应枝, 巡应档) or {})
    决rc = 0 if 试 else 自决之巡(仓, 今, 应d=应)      # 〔W908 环12③〕自决红未清 → 同局一唤而红（诸 rc 俱验；无红零 API）
    if rc == 0 and not 试:
        return max(活守之巡(仓, 今, 应d=应), 决rc)   # 〔1119 执行之审·治1(e)〕巡应示存底迟逾二十四时 → 态变方唤而红（W908 环2(a)；W910 钩死⛔红⛔唤）；余 0（零 token）
    try:
        号 = 哨PR(仓)
        if not 号:
            print('⛔ 哨 PR（头枝 %s）不在——唤不得：总编辑立之、订之' % 巡警枝)
            return 1
        try:
            旧 = _旧言(仓, 号, 今)
        except Exception as e:      # 读旧言败 → 宁多唤一回、⛔因去重之败而不唤
            print('⚠ 旧言读不出（%s）——作无旧言论' % e)
            旧 = []
        旧唤 = [k for _, k in 旧 if not k.startswith('闸·')]
        print('· 哨 PR #%d：近六时旧唤 %d（%s）' % (号, len(旧唤), '、'.join(旧唤[-3:]) or '无'))
        唤, 键, 红, 停分 = 云巡判(rc, d, 今, 旧, 印)
        应由 = '' if 试 else 应判(旧, (_读枝档(巡应枝, 巡应档) or {}).get('时'), 今, 键)     # W908 环2(d)：同局首唤之时量
        if 应由:
            print(应由)
            红 = True
        闸由 = ''
        if 再闸之机(rc, 唤, 键, 旧, 试):     # 合入之卡：同局一派（卡之态 ∈ _候之态 → 再闸⛔派、⛔记，态转「顶」之唤再派·W908 复核反例二）
            闸由 = 再闸(仓, 键.split('·', 1)[1], 态=_卡之态)
            print(闸由)
        if 试:
            唤, 键 = True, '试·%d' % 今
        if not 唤:
            print('· 同局（%s）%d 分内已唤——⛔再唤（红随唤：二十分一红，⛔每五分一邮）' % (键, 唤之隔分))
            return 决rc
        体 = ('【巡警】%s\n\n```\n%s\n```\n\n总编辑：醒即照总章三之5「醒於【巡】」办——沙盒跑 `python3 工具/接棒守.py --巡` 自验（⛔凭此言径派）。'
              '%s%s\n\n%s' % ('试唤（验唤醒之路·无须派）' if 试 else (卡之题(印) if rc == 4 else ('停书 %s 分' % 停分 if 停分 >= 0 else '器之报')),
                              印.strip()[:3000], ''.join('\n\n' + x for x in (闸由, 应由) if x),
                              '\n\n⚠ 本跑红——哨 PR 之言即达作者。' if (红 and not 试) else '', 警记 % 键))
        _接口('POST', '/repos/%s/issues/%d/comments' % (仓, 号), {'body': 体})
        print('✓ 已唤（哨 PR #%d·%s）' % (号, 键))
        return max(1 if (红 and not 试) else 0, 决rc)
    except Exception as e:
        print('⛔ 唤不成：%s' % e)
        return 1


# ── ⑧本坐上下文之察〔W911 重造 环1②·1120 作者问「每次……都会唤醒对话……从头到尾会话再去读一遍……非常的消耗 token」〕──
#   每唤之费 ∝ 本坐之上下文（缓存读·一时之档：唤隔 <60 方暖·坑61）——唤隔⛔改（逾一时即冷、每唤约十倍），减费之根唯上下文；本坐⛔能自压，唯作者键 /compact。
#   沙盒之 --巡 印「止」（rc 0）之後：本坐为总编辑之坐（心跳.坐() 去前缀＝总编辑之号·同 席在跑吗.守书开头之判）→ 倒读本坐转录之尾
#   （本坐转录·_读尾：64KB 起、至 8MB·⛔全读数十兆）求末一回 assistant 之入三项（自决之守.一回之上下文·同一把尺）与其模型；
#   逾 自决之守.压之界（三十万·与 活守(d)、自决之守.压之示 同「>」）即印次行（stdout）「⚠ 本坐上下文 N 万（逾 M 万）：每唤约 $X——宜作者键 /compact
#   （压後约 $Y）；答「止」并转此行告作者」（M 取其界·⛔写死；末句告本坐：兜底之令「印止即答止」而此行⛔转则作者⛔见——X134 之效⛔恃模型之裁）：
#   X＝3 回 × 其模型之缓存读之价（费审.一回之金·设定/价目.json）、Y 以十五万计。读不得、模型不在价目、非总编辑之坐 → 静（⛔印、⛔崩、⛔改 rc）；
#   云巡（--云巡）与 GitHub 之 --巡 ⛔调。活守(d) 之 态['上下文'] ⛔借：其量无模型（价须模型），借之仍须倒读其尾——故独读而同尺（一回之上下文）、同界、同比。
#   回：删此节、__main__ 之 上下文之印 一行、自测「W911 重造 环1②」之段（其调 上下文之察／上下文之印／察尾们）即复旧。
压後之上下文 = 150000      # 作者 1120 /compact 後之实（154,657·11:01 之末回）
一唤之回 = 3               # 每唤约三回（跑 --巡、读其印、答「止」）
察尾们 = (64 * 1024, 1024 * 1024, 8 * 1024 * 1024)


def _坐号(s):
    """会话之号去 session_／cse_ 之前缀（同 心跳.坐、席在跑吗.守书开头之判）。"""
    return re.sub(r'^(session_|cse_)', '', str(s or '').strip())


def 末回之用(路, 尾们=察尾们):
    """→ (末一回 assistant 之入三项, 其模型)｜(0, '')：倒读转录之尾（尾们 依次放宽·⛔全读），逢 usage 非零之 assistant 之行即止。"""
    import 自决之守
    for n in 尾们:
        for l in reversed(_读尾(路, n)):
            if '"usage"' not in l or '"assistant"' not in l:
                continue
            try:
                d = json.loads(l)
            except Exception:
                continue
            c = 自决之守.一回之上下文(d)
            if c:
                return c, str((d.get('message') or {}).get('model') or '')
        try:
            if os.path.getsize(路) <= n:
                break
        except Exception:
            break
    return 0, ''


def 上下文之察(坐=None, 录=None, 目=None, 尾们=察尾们):
    """→ ''（静）｜「止」之次行（见 ⑧）。坐、录（转录之路）、目（价目）可注（自测）。"""
    try:
        if _坐号(坐 if 坐 is not None else _我()) != _坐号(总编辑):
            return ''
        路 = 本坐转录() if 录 is None else 录
        if not 路:
            return ''
        try:
            import 自决之守
            界 = 自决之守.压之界
        except Exception:
            界 = 300000
        C, 模 = 末回之用(路, 尾们)
        if C <= 界 or not 模:      # 逾界方印（「>」·同 活守(d) 与 自决之守.压之示）
            return ''
        import 费审
        目 = 目 or 费审.价目(ROOT)
        金, 疑 = 费审.一回之金(模, {'cache_read_input_tokens': C}, 目)
        金後, 疑後 = 费审.一回之金(模, {'cache_read_input_tokens': 压後之上下文}, 目)
        if 疑 or 疑後 or not 金:
            return ''
        return ('⚠ 本坐上下文 %d 万（逾 %d 万）：每唤约 $%.2f——宜作者键 /compact（压後约 $%.2f）；答「止」并转此行告作者'
                % (round(C / 10000), 界 // 10000, 一唤之回 * 金, 一唤之回 * 金後))
    except Exception:
        return ''


def 上下文之印(rc, 察=None):
    """沙盒之 --巡 於 巡(查印=True) 之後调之：rc 0（已印「止」）而 上下文之察 有言 → 印为次行；余⛔印。rc ⛔改、⛔崩。"""
    if rc != 0:
        return
    try:
        言 = (察 or 上下文之察)()
    except Exception:
        言 = ''
    if 言:
        print(言)


# ── ⑧之二 冷唤之察〔W911 重造 环1④·预审（声明之律 险5）：兜底之隔之声明可虚书——update_trigger 手改（或解停只开甲）而码不改，诸钉俱绿〕──
#   零 token：倒读本坐转录之尾（同 末回之用·⛔全读），诸 assistant 之回（流式之重行同唤即聚）自末往前；同唤之回相隔 <十分（巡、读印、答）；
#   本唤之首回 F 与前唤之末回 P 相隔逾一时（缓存一时之档·坑61）而 F 之缓存读 ≤ 其上下文之 5%、缓存写 ≥ 其半 → 冷：「止」之次行印
#   「⚠ 本唤冷（隔 N 分）——兜底之令之实或已改：list_triggers 对 接棒守.兜底之令」。暂停令在（兜底之令俱停）、非总编辑之坐、读不得、
#   前唤不在尾内 → 静（⛔印、⛔崩、⛔改 rc）；云巡⛔调。每唤之出（如 W912 之图之摘）亦入上下文——增印者须并算其费（坑61·预审 险12）。
冷唤之界秒 = 3600
同唤之聚秒 = 600


def _停在():
    try:
        import 暂停令
        return bool(暂停令.在(ROOT)[0])
    except Exception:
        return False


def 冷唤之察(坐=None, 录=None, 停=None, 尾们=察尾们):
    """→ ''（静）｜「⚠ 本唤冷……」（见 ⑧之二）。坐、录、停（→ 暂停否）可注（自测）。"""
    from datetime import datetime
    try:
        if _坐号(坐 if 坐 is not None else _我()) != _坐号(总编辑) or (停 or _停在)():
            return ''
        路 = 本坐转录() if 录 is None else 录
        if not 路:
            return ''
        for n in 尾们:
            回 = []
            for l in reversed(_读尾(路, n)):
                if '"usage"' not in l or '"assistant"' not in l:
                    continue
                try:
                    d = json.loads(l)
                    m = d.get('message') or {}
                    u = m.get('usage') or {}
                    if d.get('type') != 'assistant' or not u:
                        continue
                    读, 写 = int(u.get('cache_read_input_tokens') or 0), int(u.get('cache_creation_input_tokens') or 0)
                    回.append((datetime.fromisoformat(str(d['timestamp']).replace('Z', '+00:00')).timestamp(),
                              读, 写, 读 + 写 + int(u.get('input_tokens') or 0)))
                except Exception:
                    continue
            i = 0
            while i + 1 < len(回) and 回[i][0] - 回[i + 1][0] < 同唤之聚秒:
                i += 1
            if i + 1 < len(回):
                (t首, 读, 写, 全), t前 = 回[i], 回[i + 1][0]
                if t首 - t前 <= 冷唤之界秒 or not 全 or 读 > 0.05 * 全 or 写 < 0.5 * 全:
                    return ''
                return ('⚠ 本唤冷（隔 %d 分·缓存写 %d 万）——兜底之令之实或已改（码之常 %s）：list_triggers 对 接棒守.兜底之令；答「止」并转此行告作者'
                        % ((t首 - t前) // 60, round(写 / 10000), 兜底之刻()))
            try:
                if os.path.getsize(路) <= n:
                    break
            except Exception:
                break
        return ''
    except Exception:
        return ''


def 冷唤之印(rc, 察=None):
    """沙盒之 --巡 於 上下文之印 之後调之：rc 0 而 冷唤之察 有言 → 印为次行；余⛔印。rc ⛔改、⛔崩。"""
    if rc != 0:
        return
    try:
        言 = (察 or 冷唤之察)()
    except Exception:
        言 = ''
    if 言:
        print(言)


def 派令之治(n, 主=None, 治=None):
    """`--派令 n` 之判（1027 A2）：前章（n-1）已在主枝 → None（常形）；否则 治之源(n-1)（报坏或缺章标而存底有其封）。读不出 → None（常形·会话之守照拦）。"""
    try:
        if (主 or 主含)(int(n) - 1):
            return None
        return (治 or 治之源)(int(n) - 1)
    except Exception:
        return None


def 主含(n):
    """云端主枝已含第 n 章之封版否（章-n 之标係其封版之提交，为主枝之祖即含）。"""
    def 跑(*a):
        return subprocess.run(a, cwd=ROOT, capture_output=True, text=True)
    r = 跑('git', 'ls-remote', 'origin', 'refs/heads/章-%d' % int(n))
    sha = r.stdout.split()[0] if r.returncode == 0 and r.stdout.strip() else ''
    if not sha:
        return False
    跑('git', 'fetch', '-q', 'origin', 'refs/heads/章-%d' % int(n), 'refs/heads/' + 主枝)
    f = 跑('git', 'ls-remote', 'origin', 'refs/heads/' + 主枝)
    主 = f.stdout.split()[0] if f.returncode == 0 and f.stdout.strip() else ''
    return bool(主) and 跑('git', 'merge-base', '--is-ancestor', sha, 主).returncode == 0


def 治之在飞(标):
    """→ 云端治枝之含 标（章-n 之封版之笔）者 [(枝, sha)]：章红而治推已交、GitHub 未毕——其果当读治枝之报。"""
    r = subprocess.run(['git', '-c', 'core.quotepath=off', 'ls-remote', 'origin', 'refs/heads/治-*'], cwd=ROOT, capture_output=True, text=True)
    诸 = [(x.split('refs/heads/', 1)[1], x.split()[0]) for x in r.stdout.split('\n') if 'refs/heads/治-' in x]
    if 诸:
        subprocess.run(['git', 'fetch', '-q', 'origin'] + ['refs/heads/' + 枝 for 枝, _ in 诸], cwd=ROOT, capture_output=True)
    return [(枝, s) for 枝, s in 诸 if subprocess.run(['git', 'merge-base', '--is-ancestor', 标, s], cwd=ROOT,
                                                     capture_output=True).returncode == 0]


def 云端章标(n):
    """→ 云端「章-n」之 sha；无或读不出即 ''。"""
    r = subprocess.run(['git', 'ls-remote', 'origin', 'refs/heads/章-%d' % int(n)], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.split()[0] if r.returncode == 0 and r.stdout.strip() else ''


def 坏报之源(n, 读=None, 标=None, 飞=None):
    """→ (枝, 报) 或 None：GitHub autopush 於 备份/报 之 报/推/章-n.json 之果为红／拒／败、且其 sha 即云端 章-n 之标者。
    章红而含此章之治枝已交（治在飞）：⛔以章之旧红早返——诸治俱有坏报方返其最晚者（枝＝其治枝），有未毕（或已成待并）即 None（候）。"""
    import 推报
    读 = 读 or (lambda 枝: 推报.读(枝, ROOT))
    d = 读('章-%d' % int(n))
    if not 推报.坏(d):                  # 1027 坑54：败·重派係在飞（autopush 已自重派本枝）——候其新跑之报
        return None
    if 标 is None:
        标 = 云端章标(n)
    if 标 and d.get('sha') != 标:
        return None                    # 旧标之报（⛔认他笔之果）
    在飞 = (飞 or 治之在飞)(标 or d.get('sha', ''))
    if 在飞:
        # 治枝红者不删（autopush 只删已并者）：旧治红而新治已交未毕，⛔以旧治之红早返——诸治俱有坏报方返，取其最晚者
        配 = [(枝, x) for x, (枝, s) in zip([读(枝) for 枝, _ in 在飞], 在飞) if x and x.get('sha') == s]
        if len(配) < len(在飞) or any(not 推报.坏(x) for _, x in 配):
            return None                # 治在飞而有未毕者（或已成待并）——候
        return max(配, key=lambda t: str(t[1].get('时') or ''))
    return '章-%d' % int(n), d


def 存底之封(n):
    """→ 云端 备份/存底（及诸坐之旁枝 备份/存底-*）之史里第 n 章封版之提交（「（造式二代·封版#n）」）之 sha；无即 ''。
    （封版之提交已成、「章-n」未推而坐死：存底守五分一存，其存以 HEAD 为父，故封版之提交在存底之史里）"""
    r = subprocess.run(['git', 'ls-remote', 'origin', 'refs/heads/备份/存底*'], cwd=ROOT, capture_output=True, text=True)
    诸 = [x.split()[1] for x in r.stdout.split('\n') if x.strip() and 'refs/heads/备份/存底' in x and '-旧' not in x]
    if not 诸:
        return ''
    subprocess.run(['git', 'fetch', '-q', 'origin'] + ['+%s:refs/remotes/origin/%s' % (x, x[len('refs/heads/'):]) for x in 诸],
                   cwd=ROOT, capture_output=True)
    import 封版                                   # 封版之提交之认：同一把尺（⛔另写）
    return 封版.封之笔(n, ROOT, ['refs/remotes/origin/' + x[len('refs/heads/'):] for x in 诸]) or ''


def 治之源(n, 坏=None, 标=None, 存=None):
    """第 n 章已封而未入主枝、须治（1027 A2·死锁之治：封版之坐死於 GitHub 报红之後，守书【派】n+1 而会话之守拦「第n章未入主枝」，
    无人治 n、书停）——→ 重派之会话之起（source_revision）：①其报红／拒／败 → 「章-n」（或其最晚之坏治枝）；
    ②云端无「章-n」而 备份/存底 之史有其封版之提交 → 其 sha（L0 缺碑自补之、治同上）；余 → ''（候主、⛔重派）。"""
    源 = (坏 or 坏报之源)(n)
    if 源:
        return 源[0]
    if 标 is None:
        标 = 云端章标(n)
    return '' if 标 else ((存 or 存底之封)(n) or '')


def 章之坏报(n, 读=None, 标=None, 飞=None):
    """→ 印之行：GitHub autopush 於 备份/报 之 报/推/章-n.json 之果为红／拒／败、且其 sha 即云端 章-n 之标者；否则 []。
    （1027 坑51：旧候主只问主枝含否，autopush 红了亦白候九十分。读与 推.py --候 同一把尺：推报.读）
    章红而含此章之治枝已交（治在飞）：⛔以章之旧红早返——读治枝之报，坏即返其红、未毕即候（判归 坏报之源）。"""
    import 推报
    源 = 坏报之源(n, 读, 标, 飞)
    if not 源:
        return []
    d = 源[1]
    L = 推报.报之语(d)
    if d.get('果') == '拒':
        L.append('  → 兜底：python3 工具/推.py --直（GITHUB_TOKEN 推不得改 .github/workflows 之提交；本地全闸直推主枝）')
    elif d.get('果') == '红':
        L.append('  → 推闸之红逐条治（⛔绕、⛔弱化）、提交，再 python3 工具/推.py（交 GitHub）→ 其所印 --候；治毕再交棒')
    else:
        L.append('  → 看 run_url；GitHub 停摆即 python3 工具/推.py --直')
    return L


def 候主(n, 限分=90, 隔=120, 查=None, 报=None, 进=None, 今=time.time, 睡=time.sleep):
    """封版之後、交棒之前：候 GitHub autopush 把第 n 章推进主枝（零 token；Stop 钩认本器之进程放行）。
    rc=0 已含→本地快进主枝、即交棒（总章三之5）；rc=3 备份/报 报章-n 红／拒／败→即返其红（⛔白候）；
    rc=2 逾限→印 workflow_dispatch 之兜底（GitHub 再跑 章-n 之闸·零 token）；⛔沙盒跑闸（1027 A2）——其仍无果（GitHub 停摆）方 `推.py --直`（审计·本地全闸）。
    非成之返（3、2）并印 存底包 之令：主枝（阅读器）未含本章，作者手上之书⛔由那道闸说了算（0924 作者令）。主含先问：章已由治推入主即⛔认旧坏报。"""
    查 = 查 or 主含
    报 = 报 or 章之坏报
    if 进 is None:
        import 推报
        进 = lambda: 推报.快进(ROOT)
    始 = 今()
    while True:
        if 查(n):
            print('✓主枝已含第%s章——即照总章三之5 交棒（收锁、开新会话、--候）' % n)
            print(进()[1])
            return 0
        坏 = 报(n)
        if 坏:
            print('\n'.join(坏))
            print('⛔GitHub autopush 未并第%s章（见上）——照其末行办；主枝含之後再交棒' % n)
            print(存底包之语(n))
            return 3
        if 今() - 始 >= 限分 * 60:
            print('⛔主枝 %d 分未含第%s章、亦无其坏报——⛔沙盒跑闸；先 workflow_dispatch 令 GitHub 再跑「章-%s」之闸（零 token）：'
                  '`gh workflow run autopush.yml --ref 章-%s`（或 GitHub 之器 actions_run_trigger：workflow autopush.yml、ref 章-%s），'
                  '再 `python3 工具/接棒守.py --候主 %s`；仍无果（GitHub 停摆）方 `python3 工具/推.py --直`（审计之兜底·本地全闸）；治毕再交棒'
                  % (限分, n, n, n, n, n))
            print('⛔⛔ 报作者（1108 作者令）：GitHub Actions 跑不动了——即告作者「GitHub 跑不动了」并附 Actions「autopush」之跑之态；⛔断「额度用光」（本仓公开、Actions 不计分·W908 环2(b)）：唯仓已转私有（Actions 按分计·云巡自停而另印）方言额度。总编辑之坐当场告作者（对话＋推送通知）；写书之坐 create_trigger 入总编辑之会话（接棒守.总编辑）、令以「【报】GitHub 跑不动」起')
            print(存底包之语(n))
            return 2
        睡(隔)


def 存底包之语(n):
    """候主非成之返（1027 A2）：主枝未含本章，阅读器即无之——存底包打全本单档、SendUserFile 交作者（0924 作者令「推被拦下，存底包照送」）。"""
    return ('· 作者手上之书⛔由那道闸说了算（0924 令）：主枝未含第%s章、阅读器无之——`python3 工具/存底包.py`（全本单档 .txt、正文 .tar.gz、全仓 .bundle），'
            '其印之路以 SendUserFile 交作者（打了⛔送等於没打）；主枝含之後⛔再打' % n)


交棒之宽分 = 20     # 撤锁後此内无人接，作「交棒中」（⛔误判停写而另开一坐）；1116 一时之令 30→20（与 席在跑吗.交棒之宽 同）


def 哨判(d, 今, 限):
    """⛔纯判（定时之保用）：云端心跳 d（dict 或 None）→ (rc, 由)。rc=0 有人在写或交棒中｜2 停写。"""
    if not isinstance(d, dict):
        return 2, '⛔停写：心跳读不出或不在'
    try:
        时 = int(d.get('时') or 0)
    except (TypeError, ValueError):
        时 = 0
    分 = (今 - 时) // 60
    if d.get('章') is not None:
        if 今 - 时 <= 限:
            return 0, '✓有人在写：第%s章（坐 %s，%d 分前报到）' % (d.get('章'), str(d.get('坐') or '')[:12], 分)
        return 2, '⛔停写：第%s章之锁 %d 分未续（逾 %d 分）' % (d.get('章'), 分, 限 // 60)
    if 今 - 时 < 交棒之宽分 * 60:
        return 0, '✓交棒中：交第%s章之棒、撤锁 %d 分（宽 %d 分）' % (d.get('毕'), 分, 交棒之宽分)
    return 2, '⛔停写：交第%s章之棒、撤锁已 %d 分无人接' % (d.get('毕'), 分)


def 哨():
    import 心跳
    在, d = 心跳._远()
    rc, 由 = 哨判(d if 在 else None, int(time.time()), 心跳.限)
    print(由)
    if rc:
        N = (d or {}).get('章') or (d or {}).get('毕') if (在 and isinstance(d, dict)) else None
        if not N:
            try:
                import 自走
                N = 自走.末章() + 1
            except Exception:
                N = '?'
        print('  下一章 N=%s' % N)
        print('  → 子会话无开会话之器：`python3 工具/接棒守.py --派令 %s`、照其所印 create_trigger 一回（入总编辑之会话）'
              '→ `python3 工具/接棒守.py --候 %s`（run_in_background）' % (N, N))
    return rc


def 在候():
    try:
        f = open(锁档, 'a+')
    except Exception:
        return False
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        fcntl.flock(f, fcntl.LOCK_UN)
        return False
    except BlockingIOError:
        return True
    finally:
        f.close()


# ── 执行之查（W921 环6·X132、版之鲜、败之必见、段序之守之报、云巡之期）──
#   沙盒（总编辑之坐）之 --巡 於活守之後、执行之图之前後印之（stderr·stdout 仍只「止」或旧印·rc ⛔动）：
#   ①败：费审.败之扫（自 费审.败扫之自·已裁与旧者不报）——每巡必印至 --裁 或重跑；独跑於摘之前（⛔共其二十秒）；
#   ②版之鲜：写书之坐之心跳「器」之基（merge-base 之工具树）≠ origin/主:工具 → 🟡「旧版在跑」、主之工具变後已过一章界犹异 🔴、物不知 ⚪；
#     本地 施-*／w9xx 之枝未入主：末笔後过一章界 🟡、过二 🔴；其 W 在施（工作流账 状态非「已成」）只列；
#   ③段序之守之报：origin/主 末三封之 版本/第N章/_器之迹.md「段序之守之报」——每巡必印（三章俱无方转拦）；
#   ④云巡之期：巡印带「期」而其时逾期之 1.5 倍 → 印 run_workflow 巡.yml 之令（补 cron 之疏·零 token）；
#   ⑤唯异方印：⚠／🟡 之行同前巡（指纹去其数）即略；⛔／🔴／败／甲之拦／段序之守之报 每巡必印；摘逾时之行附前巡之 🔴 数。
#   版之鲜与败俱⛔入库之清单、⛔入 体系总图 --验 之 ⛔③ 与 rc。
巡之印态档 = os.path.join(os.path.dirname(锁档), '巡之印态.json')     # <git 公目>（同 锁档）


def _git出(a, 根=None, 限=10):
    try:
        r = subprocess.run(['git', '-c', 'core.quotepath=off'] + list(a), cwd=根 or ROOT, capture_output=True, text=True, timeout=限)
        return r.stdout if r.returncode == 0 else ''
    except Exception:
        return ''


def 章界之数(自秒, 根=None):
    """origin/主 上 自秒 之後之「封版#」之笔之数（章界）。"""
    return sum(1 for 题 in _git出(['log', '--since=@%d' % (int(自秒) + 1), '--format=%s', '-n', '300', 'refs/remotes/origin/' + 主枝], 根).split('\n')
               if '封版#' in 题)


def 版之鲜(心=None, 根=None, 账=None):
    """→ [行]（🟡／🔴／⚪／·）。心：云端心跳（巡() 所读·_巡之心）；崩之项即略（⛔崩巡）。"""
    出 = []
    try:
        主树 = _git出(['rev-parse', 'refs/remotes/origin/%s:工具' % 主枝], 根).strip()
        器 = (心 or {}).get('器') if isinstance(心, dict) else None
        if isinstance(器, dict) and 器.get('基') and 主树 and 器['基'] != 主树:
            坐 = str((心 or {}).get('坐') or '')[:12]
            if subprocess.run(['git', 'cat-file', '-e', 器['基']], cwd=根 or ROOT, capture_output=True).returncode != 0:
                出.append('⚪ 版之鲜：写书之坐（%s·第%s章）之工具树 %s 本地物不知——⛔判' % (坐, (心 or {}).get('章'), 器['基'][:12]))
            else:
                t = 提交之时(_git出(['log', '-1', '--format=%H', 'refs/remotes/origin/' + 主枝, '--', '工具'], 根).strip() or '0' * 40, 根)
                n = 章界之数(t, 根) if t else 0
                出.append('%s 版之鲜：写书之坐（%s·第%s章）旧版在跑——其基之工具树 %s ≠ 主枝 %s%s' % (
                    '🔴' if n >= 1 else '🟡', 坐, (心 or {}).get('章'), 器['基'][:12], 主树[:12],
                    ('（主之工具变後已过 %d 章界犹异：新坐自主枝起即愈；在跑之坐⛔中断）' % n) if n >= 1 else '（主之工具新变·本章封後之新坐即随）'))
        try:
            件们 = {x.get('id'): x for x in (账 if 账 is not None else json.load(open(os.path.join(根 or ROOT, '设定', '工作流账.json'), encoding='utf-8')).get('件') or [])}
        except Exception:
            件们 = {}
        for b in _git出(['for-each-ref', '--format=%(refname:short)', 'refs/heads'], 根).split('\n'):
            b = b.strip()
            if not b or not (b.startswith('施-') or re.match(r'(?i)wt?9\d\d', b)):
                continue
            k = _git出(['rev-list', '--count', 'refs/remotes/origin/%s..%s' % (主枝, b)], 根).strip()
            if not k.isdigit() or int(k) == 0:
                continue
            ct = 提交之时(b, 根)
            n = 章界之数(ct, 根) if ct else 0
            m = re.search(r'(?i)w(9\d\d)', b)
            W = ('W' + m.group(1)) if m else ''
            状 = str((件们.get(W) or {}).get('状态') or '')
            if W and 状 and 状 != '已成':
                出.append('· 版之鲜：本地 %s 未入主 %s 笔（%s 在施·%s·只列）' % (b, k, W, 状))
            elif n >= 1:
                出.append('%s 版之鲜：本地 %s 未入主 %s 笔，末笔後已过 %d 章界——入主或推 origin 备份/%s 而删本地枝（带由）' % ('🔴' if n >= 2 else '🟡', b, k, n, b))
    except Exception as e:
        出.append('⚠ 版之鲜之查崩（%s）' % type(e).__name__)
    return 出


def 末三封之报(心=None, 根=None):
    """origin/主 末三封之 版本/第N章/_器之迹.md 之「段序之守之报」→ [行]；无即 []。"""
    出 = []
    try:
        n = 末封之章(心)
        for m in range(n, n - 3, -1):
            文 = _git出(['show', 'refs/remotes/origin/%s:版本/第%d章/_器之迹.md' % (主枝, m)], 根)
            if '## 段序之守之报' in 文:
                出 += ['⛔ 段序之守之报·第%d章 %s' % (m, l[2:].strip()) for l in 文.split('## 段序之守之报', 1)[1].split('\n## ', 1)[0].split('\n')
                      if l.startswith('- ')][:4]
    except Exception:
        pass
    return 出


def 巡印逾期(印d, 今=None):
    """巡印带「期」（云巡之期·分）而其时逾期之 1.5 倍 → 一行（补 cron 之疏之令）；无期、读不出 → ''。"""
    try:
        期 = (印d or {}).get('期')
        时 = int((印d or {}).get('时') or 0)
        今 = 今 or int(time.time())
        if isinstance(期, (int, float)) and 期 > 0 and 时 and 今 - 时 > 1.5 * 期 * 60:
            return ('⚠ 云巡之期：巡印 %d 分未更（逾其期 %s 分之 1.5 倍）而无環在跑——补 cron 之疏：actions_run_trigger run_workflow 巡.yml ref 主枝'
                    '（零 token·GitHub 分钟）' % ((今 - 时) // 60, 期))
    except Exception:
        pass
    return ''


_必印式 = re.compile(r'^\S{1,2} 败 \S|^⚠ 图之摘逾时')   # 〔W921 环7〕败之印（断之败以 ⚠ 起）、摘逾时（附前巡 🔴 数）每巡必印至 --裁（方案环6④）


def 印之滤(行们, 前=None):
    """⑤唯异方印：→ (所印, 今之指纹, 略数)。⚠／🟡 起之行同前巡（指纹＝去其数）即略；余（⛔、🔴、败、·、题）俱印——
    败之印（费审.败之印：断以 ⚠ 起）与摘逾时之行虽以 ⚠ 起亦每巡必印（_必印式）。"""
    前 = set(前 or ())
    出, 指, 略 = [], [], 0
    for l in 行们:
        t = l.strip()
        if t.startswith(('⚠', '🟡')) and not _必印式.search(t):
            fp = re.sub(r'\d+(?:\.\d+)?', '#', t)[:200]
            指.append(fp)
            if fp in 前:
                略 += 1
                continue
        出.append(l)
    return 出, 指, 略


def _印态(写=None):
    try:
        if 写 is not None:
            json.dump(写, open(巡之印态档, 'w', encoding='utf-8'), ensure_ascii=False)
            return 写
        return json.load(open(巡之印态档, encoding='utf-8'))
    except Exception:
        return {}


def 执行之查(心=None, 摘行=None, 摘超=False, 印d=None, 败扫=None, 态=None, 今=None, 写态=True):
    """→ [行]（印於 stderr）：败、执行之图（摘）、版之鲜、段序之守之报、云巡之期——唯异方印；态之指纹与 🔴 之数随写。崩项只 ⚠。"""
    态 = _印态() if 态 is None else 态
    前指, 前红 = 态.get('指') or [], 态.get('🔴')
    行 = []
    try:
        if 败扫 is None:
            import 费审
            败扫 = 费审.败之扫()
        import 费审 as _费
        for rid, 败 in 败扫:
            行 += [x for x in _费.败之印(rid, 败)[1][:-1]]
        if 败扫:
            行.append('  （裁之方销：python3 工具/费审.py --裁 <Run> "由"——器病须治後重跑、断提重跑、拒⛔同令重请）')
    except Exception as e:
        行.append('⚠ 败之扫崩（%s）' % type(e).__name__)
    if 摘超:
        行.append('── 执行之图 ──')
        行.append('⚠ 图之摘逾时（二十秒·⛔拦巡）——前巡 🔴 %s' % (前红 if 前红 is not None else '未知'))
    elif 摘行 is not None:
        行.append('── 执行之图 ──')
        行 += 摘行
        m = re.search(r'🔴 (\d+)、析崩', (摘行 or [''])[-1])
        if m:
            态['🔴'] = int(m.group(1))
    行 += 版之鲜(心)
    行 += 末三封之报(心)
    x = 巡印逾期(印d, 今)
    if x:
        行.append(x)
    出, 指, 略 = 印之滤(行, 前指)
    if 略:
        出.append('·（⚠／🟡 同前巡 %d 行略·唯异方印）' % 略)
    态['指'] = 指
    if 写态:
        _印态(态)
    return 出


def 自测():
    import tempfile
    global 锁档
    r = []

    def T(名, 条):
        r.append(bool(条))
        print(('  ✓ ' if 条 else '  ✗ ') + 名)

    T('①他坐持第 404 章之鲜锁 → 接了', 接了(True, 'B', 404, 404, 'A'))
    T('①之二 己锁 → ⛔接了（402 之病：己锁当作他人在跑）', not 接了(True, 'A', 404, 404, 'A'))
    T('①之三 锁已陈 → ⛔接了', not 接了(False, 'B', 404, 404, 'A'))
    T('①之四 他坐持前章之锁 → ⛔接了', not 接了(True, 'B', 403, 404, 'A'))
    T('①之五 锁空（章空）、未名之坐 → ⛔接了', not 接了(True, 'B', None, 404, 'A') and not 接了(True, '未名', 404, 404, 'A'))
    旧 = 锁档
    with tempfile.TemporaryDirectory() as d:
        锁档 = os.path.join(d, 'l')
        钟 = [0.0]
        序 = iter([(False, '', None), (True, 'A', 404), (True, 'B', 404)])
        rc = 候(404, 限分=30, 隔=60, 读=lambda: next(序), 我='A', 今=lambda: 钟[0], 睡=lambda s: 钟.__setitem__(0, 钟[0] + s))
        T('②候：锁空 → 己锁 → 他坐接 → rc=0（候了两分）', rc == 0 and 钟[0] == 120)
        钟[0] = 0.0
        rc = 候(404, 限分=30, 隔=60, 读=lambda: (False, '', None), 我='A', 今=lambda: 钟[0], 睡=lambda s: 钟.__setitem__(0, 钟[0] + s))
        T('②之二 三十分无人接 → rc=2（醒交棒者重开）', rc == 2 and 钟[0] == 30 * 60)
        f = open(锁档, 'a+')
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        T('③候时 在候() 为真（Stop 钩认之放行）', 在候())
        T('③之二 已有一守在候 → 再起之守即止（⛔两守）', 候(404, 读=lambda: (False, '', None), 我='A') == 0)
        fcntl.flock(f, fcntl.LOCK_UN)
        f.close()
        T('③之三 守毕锁释 → 在候() 为假', not 在候())
    锁档 = 旧
    今, 限 = 100000, 45 * 60
    T('④哨：锁新鲜 → rc=0 有人在写', 哨判({'章': 403, '时': 今 - 600, '坐': 'B'}, 今, 限)[0] == 0)
    T('④之二 锁逾四十五分未续 → rc=2 停写', 哨判({'章': 403, '时': 今 - 46 * 60, '坐': 'B'}, 今, 限)[0] == 2)
    T('④之三 撤锁十分（交棒中）→ rc=0（⛔另开一坐）', 哨判({'章': None, '毕': 403, '时': 今 - 600}, 今, 限)[0] == 0)
    T('④之四 撤锁逾三十分无人接 → rc=2 停写（402 封後书停之形）', 哨判({'章': None, '毕': 402, '时': 今 - 31 * 60}, 今, 限)[0] == 2)
    T('④之五 心跳读不出 → rc=2', 哨判(None, 今, 限)[0] == 2)
    import io, contextlib
    钟 = [0.0]
    序 = iter([False, False, True])
    进了 = []
    无报 = lambda n: []
    with contextlib.redirect_stdout(io.StringIO()):
        rc = 候主(404, 隔=120, 查=lambda n: next(序), 报=无报, 进=lambda: (进了.append(1), (True, '快进'))[1],
                 今=lambda: 钟[0], 睡=lambda x: 钟.__setitem__(0, 钟[0] + x))
    T('⑤候主：第三查含 → rc=0（候了四分）、本地快进一回', rc == 0 and 钟[0] == 240 and 进了 == [1])
    钟[0] = 0.0
    with contextlib.redirect_stdout(io.StringIO()) as o:
        rc = 候主(404, 隔=120, 查=lambda n: False, 报=无报, 进=lambda: (True, ''), 今=lambda: 钟[0], 睡=lambda x: 钟.__setitem__(0, 钟[0] + x))
    T('⑤之二 九十分不含、亦无坏报 → rc=2：先印 workflow_dispatch（⛔沙盒跑闸），GitHub 停摆方 推.py --直；并印存底包（1027 A2）',
      rc == 2 and '推.py --直' in o.getvalue() and 'gh workflow run autopush.yml --ref 章-404' in o.getvalue()
      and o.getvalue().index('workflow run') < o.getvalue().index('推.py --直') and '存底包.py' in o.getvalue())
    # ⑤之三—六 1027 坑51：备份/报 之坏报即早返（⛔白候九十分）；主含先问；旧标之报⛔认
    红报 = {'ref': '章-404', 'sha': 'a' * 40, '果': '红', '红': ['✗ 质量三闸  一章一日', '⛔全测未过：质量三闸'], 'run_url': 'u', '时': 't'}
    钟[0] = 0.0
    with contextlib.redirect_stdout(io.StringIO()) as o:
        rc = 候主(404, 查=lambda n: False, 报=lambda n: 章之坏报(n, 读=lambda 枝: dict(红报), 标='a' * 40, 飞=lambda 标: []), 进=lambda: (True, ''),
                 今=lambda: 钟[0], 睡=lambda x: 钟.__setitem__(0, 钟[0] + x))
    T('⑤之三 报/推/章-N.json 红 → 即 rc=3、印其红行（⛔候）、并印存底包', rc == 3 and 钟[0] == 0 and '✗ 质量三闸  一章一日' in o.getvalue()
      and '存底包.py' in o.getvalue())
    with contextlib.redirect_stdout(io.StringIO()):
        rc = 候主(404, 查=lambda n: True, 报=lambda n: ['⛔红'], 进=lambda: (True, ''), 今=lambda: 0, 睡=lambda x: None)
    T('⑤之四 主枝已含（治推已并）→ rc=0，⛔认旧坏报', rc == 0)
    T('⑤之五 旧标之报（sha 非今之章标）、成报 → ⛔坏', 章之坏报(404, 读=lambda 枝: dict(红报), 标='b' * 40, 飞=lambda 标: []) == []
      and 章之坏报(404, 读=lambda 枝: dict(红报, 果='成', 红=[]), 标='a' * 40) == [] and 章之坏报(404, 读=lambda 枝: None, 标='') == [])
    无飞 = lambda 标: []
    拒 = 章之坏报(404, 读=lambda 枝: dict(红报, 果='拒', 因='workflow', 红=['⛔拒：改 .github/workflows']), 标='a' * 40, 飞=无飞)
    T('⑤之六 拒 → 印 --直 兜底与其由', any('推.py --直' in x for x in 拒) and any('workflow' in x for x in 拒))
    T('⑤之六b 败·重派（1027 坑54：autopush 被拒而已自重派本枝）係在飞 → ⛔坏、照候；败·他因 → 坏',
      章之坏报(404, 读=lambda 枝: dict(红报, 果='败', 因='重派', 红=[]), 标='a' * 40, 飞=无飞) == []
      and bool(章之坏报(404, 读=lambda 枝: dict(红报, 果='败', 因='non-ff', 红=[]), 标='a' * 40, 飞=无飞)))
    诸报 = {'章-404': dict(红报), '治-bbbbbbbbbbbb': None}
    飞 = lambda 标: [('治-bbbbbbbbbbbb', 'b' * 40)] if 标 == 'a' * 40 else []
    候中 = 章之坏报(404, 读=lambda 枝: 诸报.get(枝), 标='a' * 40, 飞=飞)
    诸报['治-bbbbbbbbbbbb'] = dict(红报, ref='治-bbbbbbbbbbbb', sha='b' * 40, 红=['✗ 改单  治推又红'])
    治红 = 章之坏报(404, 读=lambda 枝: 诸报.get(枝), 标='a' * 40, 飞=飞)
    T('⑤之七 章红而含此章之治枝在飞：未毕 → 候（⛔以章之旧红早返）；治报红 → 返治之红', 候中 == [] and any('治推又红' in x for x in 治红)
      and not any('一章一日' in x for x in 治红))
    # ⑤之八 旧治红（其枝不删）而新治已交未毕 → 候（⛔以旧治之红早返）；二治俱红 → 返最晚者之红
    诸报['治-cccccccccccc'] = None
    飞2 = lambda 标: [('治-bbbbbbbbbbbb', 'b' * 40), ('治-cccccccccccc', 'c' * 40)]
    旧红新候 = 章之坏报(404, 读=lambda 枝: 诸报.get(枝), 标='a' * 40, 飞=飞2)
    诸报['治-bbbbbbbbbbbb']['时'] = '2026-10-27T01:00:00Z'
    诸报['治-cccccccccccc'] = dict(红报, ref='治-cccccccccccc', sha='c' * 40, 红=['✗ 新治之红'], 时='2026-10-27T02:00:00Z')
    俱红 = 章之坏报(404, 读=lambda 枝: 诸报.get(枝), 标='a' * 40, 飞=飞2)
    T('⑤之八 旧治红而新治未毕 → 候（⛔以旧治之红早返）；二治俱红 → 返最晚者之红', 旧红新候 == []
      and any('新治之红' in x for x in 俱红) and not any('治推又红' in x for x in 俱红))
    src = open(os.path.abspath(__file__), encoding='utf-8').read().split('def 自测')[0]
    段主含 = src.split('def 主含(')[1].split('\ndef ')[0]
    段候主 = src.split('def 候主(')[1].split('\ndef ')[0]
    T('⑥候主之默认查係 主含、默认报係 章之坏报、默认进係 推报.快进（1022 复核：⛔以注入之假查充其验）',
      '查 = 查 or 主含' in 段候主 and '报 = 报 or 章之坏报' in 段候主 and '推报.快进(ROOT)' in 段候主
      and "推报.读(枝, ROOT)" in src.split('def 坏报之源(')[1].split('\ndef ')[0]
      and '源 = 坏报之源(n, 读, 标, 飞)' in src.split('def 章之坏报(')[1].split('\ndef ')[0])
    # ⑨1027 A2·死锁之治：封版之坐死於 GitHub 报红之後，守书【派】N+1 而会话之守拦「第N章未入主枝」——无人治 N、书停。
    #   治之源：报坏 → 「章-N」（或其最晚之坏治枝）；缺章标而存底有其封 → 其 sha；报未毕／成、或章标在而无坏报 → ''（候主、⛔重派）
    _坏 = lambda 枝: (lambda n: (枝, {'果': '红'}))
    T('⑨治之源：报红 → 章-N；坏在治枝 → 其治枝；缺章标而存底有封 → 其 sha；章标在而报未坏 → 空；俱无 → 空',
      治之源(410, 坏=_坏('章-410')) == '章-410' and 治之源(410, 坏=_坏('治-bbbbbbbbbbbb')) == '治-bbbbbbbbbbbb'
      and 治之源(410, 坏=lambda n: None, 标='', 存=lambda n: 'f' * 40) == 'f' * 40
      and 治之源(410, 坏=lambda n: None, 标='a' * 40, 存=lambda n: 'f' * 40) == ''
      and 治之源(410, 坏=lambda n: None, 标='', 存=lambda n: '') == '')
    _源 = 坏报之源(404, 读=lambda 枝: dict(红报), 标='a' * 40, 飞=lambda 标: [])
    _源治 = 坏报之源(404, 读=lambda 枝: 诸报.get(枝), 标='a' * 40, 飞=飞2)
    T('⑨之二 坏报之源：章红 → (章-N, 报)；二治俱红 → 最晚之治枝；章之坏报只经之（同一把尺）',
      _源 == ('章-404', 红报) and _源治 and _源治[0] == '治-cccccccccccc')
    治参 = 派之参(411, True, 治='章-410')
    T('⑨之三 治之参：自「章-410」起（⛔主枝）、【重派】、令之首个章号仍 411、题名「治第410章」；派令同形且名带「先治」',
      治参['source_revision'] == '章-410' and 治参['outcome_branch'] == 主枝 and 治参['prompt'].startswith('【重派】接《镇冢秘术》第 411 章之棒')
      and 治参['title'] == '镇冢秘术·治第410章（後接第411章）' and '【判】治' in 治参['prompt'] and 'python3 工具/推.py' in 治参['prompt']
      and 派之参(411, False, 治='章-410') == 治参
      and json.JSONDecoder().raw_decode(派令(411, 今=lambda: 0, 治='章-410')['prompt'].split('⛔改参：', 1)[1])[0] == 治参
      and '先治第410章' in 派令(411, 今=lambda: 0, 治='章-410')['name'] and '先治' not in 派令(411, 今=lambda: 0)['name'])
    T('⑨之四 --派令 之判：前章已在主 → 常形（⛔查治）；未在主 → 治之源；读崩 → 常形',
      派令之治(411, 主=lambda n: True, 治=lambda n: 1 / 0) is None and 派令之治(411, 主=lambda n: False, 治=lambda n: '章-%d' % n) == '章-410'
      and 派令之治(411, 主=lambda n: 1 / 0) is None and '治 = 派令之治(int(a[i + 1]))' in open(os.path.abspath(__file__), encoding='utf-8').read())
    T('⑥之二 主含真查云端：章-N 之标为主枝之祖', all(k in 段主含 for k in ("'merge-base', '--is-ancestor'", "'refs/heads/章-%d'", 'ls-remote')))
    参 = 派之参(411, 名='第411章')
    T('⑦派之参：题、模、源、枝、令俱定形', 参['title'] == '镇冢秘术·第411章' and 参['model'] == 'claude-opus-5-5'
      and 参['source_revision'] == 参['outcome_branch'] == 主枝 and 参['source_url'] == 源 and __import__('re').match(r'^https://github\.com/[^/]+/[^/]+$', 源)
      and '第 411 章' in 参['prompt'] and '--跳 411' in 参['prompt'] and not 参['prompt'].startswith('【重派】'))
    T('⑦之二 重派：令首带【重派】、余同', 派之参(411, True, '第411章')['prompt'] == '【重派】' + 参['prompt'])
    T('⑦之五 题名实务：大审到期即名其段（1024 作者疑「怎么开始写 411」）',
      务之名(411, 上审=407, 待至=410) == '大审第408—410章（审毕暂停）' and 务之名(421, 上审=410, 待至=410) == '大审第411—420章（後接第421章）'
      and 务之名(412, 上审=410) == '第412章' and 务之名(411, 上审=410) == '第411章'
      and 务之名(481, 上审=470, 段至=481) == '大审第471—480章（审毕、立第481—490章之段案验过後暂停·⛔写第481章）' and 务之名(481, 上审=470, 段至=491) == '大审第471—480章（後接第481章）')   # ★1120 待之段案至
    T('⑦之六 令⛔言「写」第 N 章（实务由自走判）', '照其所判办' in 参['prompt'] and not 参['prompt'].startswith('写'))
    令 = 派令(411, 今=lambda: 0)
    T('⑦之三 派令：入总编辑之会话、二分後、令中之参可原样解回', 令['persistent_session_id'] == 总编辑
      and 令['run_once_at'] == '1970-01-01T00:02:00Z' and 令['prompt'].startswith('【派】开第 411 章')
      and json.JSONDecoder().raw_decode(令['prompt'][令['prompt'].index('{'):])[0] == 派之参(411))
    # ⑩1116 停书之巡（作者令「stops at most 1 hour」）：巡判逐形；一时之界：限＋云巡之隔＋GitHub 之迟＋派 ＜ 六十分（1117 交 GitHub）
    import 心跳 as _心
    _今 = 10 ** 9
    _限 = _心.限
    import 席在跑吗 as _席
    def _分(c):      # cron 之分栏（'27 * * * *'）→ [27]
        return [int(x) for x in c.split()[0].split(',')]
    def _隔(ms):     # 所开诸令之分之并 → 相邻之隔之最大者（环一时）
        m = sorted(set(ms))
        return max((m[(i + 1) % len(m)] - m[i]) % 60 or 60 for i in range(len(m)))
    _常分 = [x for _, _, c, _, 开 in 兜底之令 if 开 for x in _分(c)]
    _降分 = [x for _, _, _, c, _ in 兜底之令 for x in _分(c)]     # 降级三令俱开
    T('⑩一时之界（1117 云巡·不劣之审；W910 章推之環）：章推之環在时（早止之前）心跳.限 25＋云巡之隔 5＋GitHub 定时之迟 15＋派 5 ≤ 50；'
      '两章之间（環已早止）与 GitHub 死俱 25＋兜底之隔 30＋5 ≤ 60、降级後 25＋20＋5 ≤ 50——隔取所开诸令之分之并（常 甲乙、降 甲乙丙）；交棒之宽 ≤ 心跳.限；甲之号 即 席在跑吗.守书之令',
      _限 == 25 * 60 and 云巡之隔分 == 5 and _限 // 60 + 云巡之隔分 + GitHub之迟分 + 5 <= 50 and 交棒之宽分 * 60 <= _限
      and _隔(_常分) == 兜底之隔分 == 30 and _限 // 60 + 兜底之隔分 + 5 <= 60 and _隔(_降分) == 20 and _限 // 60 + _隔(_降分) + 5 <= 50
      and 兜底之分() == sorted(_常分) and 兜底之分(True) == sorted(_降分) and 兜底之刻() == ':27 :57' and 兜底之刻(True) == ':07 :27 :47'
      and [x[0] for x in 兜底之令] == ['甲', '乙', '丙'] and len({x[1] for x in 兜底之令}) == 3 and all(str(x[1]).startswith('trig_') for x in 兜底之令)
      and 兜底之令[0][1] == _席.守书之令 and 兜底之令[0][4] is True)   # 旧三令之号之去：法用册「废·停书之巡三令与每时之警报」之去证守之
    T('⑩之六 兜底之巡每令一时至多一跑（平台定时之令最短一时·1117 拒「27,57 * * * *」之一令）：常、降之 cron 俱五栏、分栏只一数（0—59）、余栏俱「*」',
      all(len(c.split()) == 5 and re.fullmatch(r'[0-9]{1,2}', c.split()[0]) and int(c.split()[0]) < 60 and c.split()[1:] == ['*'] * 4
          for _, _, 常, 降之, _ in 兜底之令 for c in (常, 降之)))
    T('⑩之二 巡判逐形：在写／交棒中→止；停写→派（号取章或毕；皆无取末）；读不出→派末；暂停→止；停锁残而令解→解',
      巡判({'章': 455, '时': _今 - 600, '坐': 'A'}, _今, _限)[0] == '止'
      and 巡判({'章': None, '毕': 456, '时': _今 - 600}, _今, _限)[0] == '止'
      and 巡判({'章': 455, '时': _今 - _限 - 60, '坐': 'A'}, _今, _限)[:2] == ('派', 455)
      and 巡判({'章': None, '毕': 456, '时': _今 - 交棒之宽分 * 60 - 60}, _今, _限)[:2] == ('派', 456)
      and 巡判(None, _今, _限, 末=457)[:2] == ('派', 457)
      and 巡判({'时': 'x'}, _今, _限, 末=458)[:2] == ('派', 458)
      and 巡判({'章': '暂停', '时': 4102444800, '坐': '暂停令'}, _今, _限)[0] == '止'
      and 巡判({'章': '暂停', '时': 4102444800, '坐': '暂停令'}, _今, _限, 停在=False)[0] == '解')
    import io as _io, contextlib as _cl, 暂停令 as _停令
    _旧远, _旧在 = _心._远, _停令.在
    try:   # 1117 治：巡之 停在 取 暂停令.在()[0]——旧 bool(元组) 恒真，令解而停锁残留则巡（云巡亦然）恒判止、⛔察解停
        _心._远 = lambda: (True, {'章': '暂停', '时': 4102444800, '坐': '暂停令'})
        with _cl.redirect_stdout(_io.StringIO()):
            _停令.在 = lambda root=None: (False, '已解（试）'); _rc解 = 巡()
            _停令.在 = lambda root=None: (True, '暂停令在（试）'); _rc止 = 巡()
    finally:
        _心._远, _停令.在 = _旧远, _旧在
    T('⑩之七 巡之停在取 暂停令.在()[0]：停锁在而令已解 → rc 3（解）、令在 → rc 0（止）——暂停中兜底三令俱停，解停由 暂停令 --解 同回合验之、GitHub cron 之巡兼察（W910：章推之環於暂停早止）',
      _rc解 == 3 and _rc止 == 0)
    _段巡 = src.split('def 巡(查印=False):')[1].split('\ndef ')[0] if 'def 巡(查印=False):' in src else ''
    _无8 = dict(坏=lambda n: None, 报=lambda n: None, 跑态=lambda n, s: None, 飞=lambda 标: [], 治报=lambda b: None)   # 无坏报、无报、跑态读不出（沙盒）、无治在飞 → 退回三十分之界
    _卡31 = 合入之卡({'章': 456, '时': 1}, 今=10000, 标=lambda n: 'a' * 40, 含=lambda n: False, 时=lambda s: 10000 - 31 * 60, **_无8)
    T('⑩之四 合入之卡：封逾三十分未入主→合入之卡（无报之由·⛔断额度）；未封／已入主／未逾→空（无坏报、跑态读不出·退回三十分之界）',
      '合入之卡：第455章已封' in _卡31 and '31 分未入主枝' in _卡31 and '无报' in _卡31 and '额度用光' not in _卡31 and '换号' not in _卡31
      and 合入之卡({'章': 456, '时': 1}, 今=10000, 标=lambda n: '', 含=lambda n: False, 时=lambda s: 0, **_无8) == ''
      and 合入之卡({'章': 456, '时': 1}, 今=10000, 标=lambda n: 'a' * 40, 含=lambda n: True, 时=lambda s: 0, **_无8) == ''
      and 合入之卡({'章': 456, '时': 1}, 今=10000, 标=lambda n: 'a' * 40, 含=lambda n: False, 时=lambda s: 10000 - 600, **_无8) == ''
      and 合入之卡({'章': None, '毕': 456}, 今=10000) == '' and 合入之卡({'章': '暂停'}, 今=10000) == '')
    T('⑩之三 巡之派参俱【重派】（越会话之守「一时内同章已派」之拦）、先 get_session 其坐、印「止」即止',
      '派之参(号, True, 治=治)' in _段巡 and 'get_session' in _段巡 and "print('止')" in _段巡
      and 派之参(455, True)['prompt'].startswith('【重派】'))
    T('⑩之五 巡之重派先核周限（坑59·1117：周限尽则写书之坐与诸巡俱停十一时；额度未复⛔派）',
      'rate_limit_info' in _段巡 and '周限' in _段巡)
    _旧 = [(_今 - 600, 'rc2·455·%d' % (_今 - _限 - 60))]
    _d = {'章': 455, '时': _今 - _限 - 60, '坐': 'A'}
    T('⑪云巡判（1117）：止→⛔唤⛔红；停写→唤（键＝rc·章·心跳之时）；同键二十分内⛔再唤、逾即再唤；停逾九十分或器败或合入之卡→红',
      云巡判(0, _d, _今, [])[:3] == (False, '', False)
      and 云巡判(2, _d, _今, [])[:3] == (True, 'rc2·455·%d' % (_今 - _限 - 60), False)
      and 云巡判(2, _d, _今, _旧)[0] is False
      and 云巡判(2, _d, _今 + 唤之隔分 * 60, _旧)[0] is True
      and 云巡判(2, {'章': 455, '时': _今 - 警之界分 * 60, '坐': 'A'}, _今, [])[2] is True
      and 云巡判(1, None, _今, [], '⛔ 云巡自败')[2] is True and 云巡判(4, _d, _今, [], '⛔ 停书')[2] is True
      and 云巡判(3, {'章': '暂停', '时': _今 - 60}, _今, [])[2] is False)
    _t章 = _今 - (巡印之鲜分 + 5) * 60        # 末封之章推於二十分前
    _停印 = 巡印判({'时': _t章 - 60}, _今, 章=(476, _t章))
    _调 = []
    _鲜印 = 巡印判({'时': _今 - 600}, _今, 章=lambda: (_调.append(1), (476, _t章))[1])          # 鲜：章之函⛔调（零请·记调而⛔吞）
    _旧印调 = 巡印判({'时': _t章 - 60}, _今, 章=lambda: (_调.append(2), (476, _t章))[1])        # 旧：调之（对照）
    T('⑪之二 巡印判（W910·環唯章起，巡印之旧⛔即停摆）：巡印鲜（<十五分）→空且⛔取章推之时（零请）；章推逾十五分而巡印旧於其推→停摆、再起之令带 zhi；'
      '環随章（巡印新於章推）→空；章推未逾十五分→空；两章之间（巡印旧数时而新於末章之推）→空；章推之时取不得（0）、章缺、取之败→空（⛔误报）；读不出而章推逾十五分→停摆',
      巡印之鲜分 == 15 and _鲜印 == '' and _调 == [2] and '停摆' in _旧印调
      and '停摆' in _停印 and '環未随章起' in _停印 and '"huan":"1","zhi":"476"' in _停印 and '章-476' in _停印
      and 巡印判({'时': _t章 + 30}, _今, 章=(476, _t章)) == ''
      and 巡印判({'时': _今 - 3600}, _今, 章=(477, _今 - 600)) == ''
      and 巡印判({'时': _今 - 6 * 3600}, _今, 章=(476, _今 - 7 * 3600)) == ''
      and 巡印判({'时': _今 - 3600}, _今, 章=(476, 0)) == '' and 巡印判({'时': _今 - 3600}, _今) == ''
      and 巡印判({'时': _今 - 3600}, _今, 章=lambda: 1 / 0) == ''
      and '停摆' in 巡印判(None, _今, 章=(476, _t章)) and '读不出' in 巡印判(None, _今, 章=(476, _t章))
      and '停摆' in 巡印判({'时': 'x'}, _今, 章=lambda: (476, _t章)) and 巡印判(None, _今, 章=(476, 0)) == '')
    import 自走 as _走
    _旧心, _旧推 = globals()['_巡之心'], globals()['章推之时']
    _推取 = []
    try:      # 行为之钉（复核：旧以子串「_巡之心」钉之，函之文档即满之·删码行仍绿）——心缺取 _巡之心、心明取心、巡印鲜⛔取章推之时
        globals()['_巡之心'] = {'章': 9001, '时': _今 - 60, '坐': 'B'}       # 章号取远於正文之末者（心缺而退 自走.末章() 即异）
        globals()['章推之时'] = lambda n, 根=None: (_推取.append(n), _今 - 3 * 60)[1]
        _由心 = 巡印之由(_今, d={'时': _今 - 3600})
        _由明 = 巡印之由(_今, d={'时': _今 - 3600}, 心={'章': 470, '时': _今 - 60})
        _由鲜 = 巡印之由(_今, d={'时': _今 - 60})
    finally:
        globals()['_巡之心'], globals()['章推之时'] = _旧心, _旧推
    T('⑪之二b 末封之章：写第 N 章→N−1；交棒中（毕＝所交之章：收 N+1）→毕−1；暂停、读不出→自走.末章()；巡印之由惰取章推之时（鲜⛔取）、心缺取 _巡之心（9001→章推之时(9000)）、心明取心（470→469）%s' % _推取,
      末封之章({'章': 477, '时': 1}) == 476 and 末封之章({'章': None, '毕': 478, '时': 1}) == 477
      and 末封之章({'章': '暂停'}) == _走.末章() and 末封之章(None) == _走.末章() and 末封之章({'章': True}) == _走.末章()
      and _推取 == [9000, 469] and _由心 == _由明 == _由鲜 == ''
      and all(k in src.split('def 巡印之由(')[1].split('\ndef ')[0] for k in ('末封之章(心)', '章推之时(n)', '章=章')))
    with tempfile.TemporaryDirectory() as _gd:
        _ge = dict(os.environ, GIT_AUTHOR_NAME='t', GIT_AUTHOR_EMAIL='t@t', GIT_COMMITTER_NAME='t', GIT_COMMITTER_EMAIL='t@t',
                   GIT_AUTHOR_DATE='@1700000000 +0000', GIT_COMMITTER_DATE='@1700000000 +0000')
        subprocess.run(['git', 'init', '-q', _gd], capture_output=True)
        subprocess.run(['git', 'commit', '-q', '--allow-empty', '-m', 't'], cwd=_gd, capture_output=True, env=_ge)
        subprocess.run(['git', 'update-ref', 'refs/remotes/origin/章-9', 'HEAD'], cwd=_gd, capture_output=True)
        _t9, _t10 = 章推之时(9, 根=_gd), 章推之时(10, 根=_gd)
        _tH, _tX = 提交之时('HEAD', 根=_gd), 提交之时('0' * 40, 根=_gd)
        # 本地无「章-n」之物 → fetch 之退路（总编辑之沙盒无他坐新推之章·rc 5 唯恃之）；章之坐 同（封者之尾）——以临时之 bare 为 origin（⛔网·⛔推）
        _bare = os.path.join(_gd, 'o.git')
        subprocess.run(['git', 'init', '-q', '--bare', _bare], capture_output=True)
        _树 = subprocess.run(['git', '--git-dir', _bare, 'mktree'], input='', capture_output=True, text=True).stdout.strip()
        _o = {}
        for _k, _言, _t in ((10, '封版#10\n\nCo-Authored-By: x\nClaude-Session: https://claude.ai/code/session_ABC123xyz', 1700000500),
                           (11, '封版#11（无尾）', 1700000600), (12, '封版#12\n\nClaude-Session: https://claude.ai/code/session_%s' % ('Q' * 40), 1700000700)):
            _e = dict(_ge, GIT_AUTHOR_DATE='@%d +0000' % _t, GIT_COMMITTER_DATE='@%d +0000' % _t)
            _o[_k] = subprocess.run(['git', '--git-dir', _bare, 'commit-tree', _树, '-m', _言], capture_output=True, text=True, env=_e).stdout.strip()
            subprocess.run(['git', '--git-dir', _bare, 'update-ref', 'refs/heads/章-%d' % _k, _o[_k]], capture_output=True)
        subprocess.run(['git', 'remote', 'add', 'origin', _bare], cwd=_gd, capture_output=True)
        _t11o = 章推之时(11, 根=_gd)                   # 本地无 refs/remotes/origin/章-11（亦未 fetch 其枝）→ fetch 之退路（先於诸 fetch：⛔为他 fetch 之顺更 ref 所掩）
        _ref11 = subprocess.run(['git', 'rev-parse', '-q', '--verify', 'refs/remotes/origin/章-11'], cwd=_gd, capture_output=True, text=True).stdout.strip()
        _坐10 = 章之坐(10, 根=_gd, 标=_o[10])          # 本地无其物 → fetch 而读其尾
        _坐11, _坐12, _坐空, _坐坏 = 章之坐(11, 根=_gd, 标=_o[11]), 章之坐(12, 根=_gd, 标=_o[12]), 章之坐(13, 根=_gd, 标=''), 章之坐(13, 根=_gd, 标='f' * 40)
        _旧env = {k: os.environ.get(k) for k in ('CLAUDE_CODE_REMOTE_SESSION_ID',)}
        try:
            os.environ['CLAUDE_CODE_REMOTE_SESSION_ID'] = 'session_ABC123xyz'
            _心坐 = _心.坐()
        finally:
            for k, v in _旧env.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
    _封源 = open(os.path.join(ROOT, '工具', '封版.py'), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT, '工具', '封版.py')) else ''
    _段卡 = src.split('def 合入之卡(')[1].split('\ndef ')[0]
    T('⑪之二c 章推之时：本地有其物即 git log %%ct（%s）；无而 fetch 不得（无 origin）→ 0（⛔抛）；本地无而 origin 有 → fetch 而得其时（%s）且留其 ref；与 合入之卡 同取 提交之时（坑53：%%ct 唯一处）；'
      '章之坐（复核要害）：章-N 之提交之 Claude-Session 之尾 → 封者之坐（%s·＝心跳.坐() 於同一会话之号·依 封版.py 之 尾；前三十二字）；本地无其物先 fetch；无尾、无标、坏标 → 空' % (_t9, _t11o, _坐10),
      _t9 == 1700000000 and _t10 == 0 and _tH == 1700000000 and _tX == 0 and _t11o == 1700000600 and _ref11 == _o[11]
      and _坐10 == 'ABC123xyz' == _心坐 and _坐11 == '' and _坐12 == 'Q' * 32 and _坐空 == _坐坏 == ''
      and "Claude-Session: https://claude.ai/code/session_%s' % _坐" in _封源 and "_坐 = re.sub(r'^(session_|cse_)', '', os.environ.get('CLAUDE_CODE_REMOTE_SESSION_ID'" in _封源
      and '(时 or 提交之时)(sha)' in _段卡 and '%ct' not in _段卡 and '提交之时(引, 根)' in src.split('def 章推之时(')[1].split('\ndef ')[0]
      and src.count("'--format=%ct'") == 1)
    _流 = open(os.path.join(ROOT, '.github', 'workflows', '巡.yml'), encoding='utf-8').read() if os.path.exists(
        os.path.join(ROOT, '.github', 'workflows', '巡.yml')) else ''
    _段云 = src.split('def 云巡(')[1].split('\ndef ')[0]
    T('⑪之四 云巡：读旧言败即作无旧言（宁多唤⛔不唤）；哨 PR 不在即红；巡印每跑俱落（止亦落）',
      "旧 = []" in _段云 and '哨 PR' in _段云 and 'return 1' in _段云
      and _段云.index('落巡印(') < _段云.index('if rc == 0 and not 试'))
    _xs = re.search(r"(?m)^  xun:\n(?:    .*\n|\n)*", _流)
    _xs = _xs.group(0) if _xs else ''
    _再 = re.search(r'(?m)^      - name: 再起之察.*\n        if: (.*)$', _xs)
    _续步 = _流.split('      - name: 续')[1].split('      - name: 红随唤')[0] if '      - name: 续' in _流 and '      - name: 红随唤' in _流 else ''
    T('⑪之三 巡.yml（W910·章推之環）：cron 三十分（只巡一回）、push 章-* 起環（huan 之 if 兼之：ref 恒主枝·zhi＝N·fen 90·jian 300）、dispatch 之 fen 上限 90、'
      'inputs zhi／xu、每巡後 --早止 连三止即早止、局唯以印之首行（巡() 之判）定（首⛔行只作 summary 与 ::error 之文·复核③b）、'
      '续唯局悬（末巡之局非止、或末之 --早止 rc 1）且 xu<4（fen 60·zhi 同·xu+1）、云巡之 stderr 另档（⛔乱首行）、槽与墙钟俱计、本组已有章推之環在候即⛔续（读不出照派）、concurrency 巡环-主枝（章推与主枝之手起同组）、job 之限 120、'
      'run-name「巡环·章-N」与「巡环·{fen}分·隔{jian}秒」、xun 之再起之察唯无 huan 无 shi 之手 dispatch（schedule ⛔起環）而认章推之環；'
      '跑 --云巡、可写言（issues）、哨 PR 之言须 pull-requests 之写（1120 巡演 --试：只读即 403·⛔再收）、可推巡印（contents）；沙盒之 --巡 验巡印（rc 5）、GitHub 之 --巡⛔验；巡.yml 被停即止',
      "cron: '*/30 * * * *'" in _流 and "cron: '*/5" not in _流 and "branches: ['备份/巡演', '章-*']" in _流
      and '接棒守.py --云巡' in _流 and 'issues: write' in _流 and 'pull-requests: write' in _流
      and 'contents: write' in _流 and 'actions: write' in _流 and '巡印之由(d=印d)' in _段巡
      and all(k in _流 for k in ('      huan:\n', '      zhi:\n', '      xu:\n', "default: '90'",
                                  "    if: (github.event_name == 'workflow_dispatch' && inputs.huan == '1') || (github.event_name == 'push' && startsWith(github.ref_name, '章-'))\n",
                                  'timeout-minutes: 120\n', "group: 巡环-${{ github.event_name == 'push' && 'claude/the-novel-review-4dtuit' || github.ref_name }}",
                                  "ref: ${{ github.event_name == 'push' && 'claude/the-novel-review-4dtuit' || github.ref }}",
                                  'if [ "$GITHUB_EVENT_NAME" = push ]; then REF=claude/the-novel-review-4dtuit; ZHI="${GITHUB_REF_NAME#章-}"; FEN=90; JIAN=300; fi',
                                  '[ "$FEN" -gt 90 ] && FEN=90', 'cancel-in-progress: false', 'fetch -q origin "$REF"', 'reset -q --hard FETCH_HEAD',
                                  '接棒守.py --早止 "$ZHI"', 'if [ "$ZRC" -eq 0 ] && [ "$RC" -eq 0 ] && [ "$MO" -eq 0 ]; then LZ=$((LZ + 1)); else LZ=0; fi',
                                  'if [ "$LZ" -ge 3 ]; then ZAO=1;', '{ IFS= read -r TOU; IFS= read -r SHOU; }', 'print((l or ["（无印）"])[0][:160]);print((h or l or e[-1:]',
                                  '--云巡 > "$RUNNER_TEMP/巡之印" 2> "$RUNNER_TEMP/巡之误"; RC=$?', 'case "$ZRC" in 0|1|3) ZR=$ZRC ;; esac', 'echo "zr=$ZR"',
                                  '{ [ "$NEXT" -ge $((T0 + FEN * 60)) ] || [ "$NOW" -ge $((T0 + FEN * 60)) ]; } && break',
                                  'MO=0; [ "$TOU" != 止 ] && MO=1', 'if [ "$RC" -ne 0 ] || [ "$MO" -eq 1 ]; then FZ=$((FZ + 1));',
                                  "format('巡环·{0}', github.ref_name)", "format('巡环·{0}分·隔{1}秒', inputs.fen, inputs.jian)",
                                  '-X POST', '/actions/workflows/%E5%B7%A1.yml/dispatches', 'startswith("巡环")', 'b.startswith("章-")', '!= active', 'until curl'))
      and 'timeout-minutes: 355' not in _流 and '-gt 340' not in _流 and '"$SHOU" != 止' not in _流 and '"$SHOU" = 止' not in _流
      and "if: ${{ !cancelled() && steps.huan.outputs.xu != '0' }}" in _续步
      and '--云巡 > "$RUNNER_TEMP/巡之印" 2>&1' not in _流
      and all(k in _续步 for k in ('if [ "$ZAO" = 1 ]; then', 'if [ -z "$MO" ]; then', 'if [ "$MO" != 1 ] && [ "$ZR" != 1 ]; then', 'ZR: ${{ steps.huan.outputs.zr }}', 'if [ "$XC" -ge 4 ]; then',
                                   '"fen":"60"', '"zhi":sys.argv[3],"xu":sys.argv[4]', '"$((XC + 1))"'))
      and _续步.index('if [ "$XC" -ge 4 ]; then') < _续步.index('/runs?per_page=50') < _续步.index('until curl')
      and all(k in _续步 for k in ('if [ "$REF" = claude/the-novel-review-4dtuit ]; then', 'startswith("巡环·章-")', 'str(r.get("id")) != sys.argv[1]',
                                   '"$GITHUB_RUN_ID" 2> /dev/null)" || HOU=', 'if [ -n "$HOU" ]; then'))
      and "if: github.event_name == 'schedule' || (github.event_name == 'workflow_dispatch' && inputs.huan != '1') || (github.event_name == 'push' && !startsWith(github.ref_name, '章-'))" in _xs
      and bool(_再) and _再.group(1).strip() == "github.event_name == 'workflow_dispatch' && inputs.shi == '' && inputs.huan != '1'"
      and 'schedule' not in _再.group(1)
      and all(k in open(os.path.abspath(__file__), encoding='utf-8').read().split("\nif __name__ == '__main__':")[1] for k in ("_rc = 巡(查印=True)", '落巡应(_rc, 态=_态, 前=_前巡应)', 'sys.exit(巡())')))   # 〔1119 执行之审·治1(e)〕落巡应带活守之态；〔W911 重造〕承前巡应之降
    # ⑪之三b 桩局（W910 复核③b）：以桩代 接棒守.py、git、curl、sleep，照 GitHub 之 shell: bash（--noprofile --norc -eo pipefail）真跑 巡.yml 之環与续之 bash
    import shutil

    def _步(名):
        m = re.search(r'(?m)^      - name: %s.*\n(?:        .*\n)*?        run: \|\n((?:          .*\n)*)' % re.escape(名), _流)
        return re.sub(r'(?m)^          ', '', m.group(1)) if m else ''
    _环脚, _续脚 = _步('環'), _步('续')
    _桩果 = {}
    _真date = shutil.which('date') or '/bin/date'
    if _环脚 and _续脚 and all(shutil.which(x) for x in ('bash', 'timeout')):
        with tempfile.TemporaryDirectory() as _根:
            _bin = os.path.join(_根, 'bin')
            os.makedirs(_bin)
            os.makedirs(os.path.join(_根, '工具'))
            for _名, _体 in (('git', 'case "$*" in *rev-parse*) echo abc123def456 ;; esac\nexit 0\n'), ('sleep', 'exit 0\n'),
                             ('curl', 'case "$*" in *"-X POST"*) printf "%s\\n" "$*" >> "$ZHUANG_PAI"; exit 0 ;;\n'
                                      '*/runs*) [ -s "$ZHUANG_PAO" ] || exit 22; cat "$ZHUANG_PAO"; exit 0 ;;\n*) echo \'{"state":"active"}\' ;; esac\n'),
                             ('date', 'if [ -n "$ZHUANG_SHI" ] && [ "$*" = "+%%s" ]; then t=$(cat "$ZHUANG_SHI"); echo "$t"; echo $((t + ZHUANG_BU)) > "$ZHUANG_SHI"; exit 0; fi\n'
                                      'exec %s "$@"\n' % _真date)):     # date 之桩：设 ZHUANG_SHI 即假钟（每 `date +%s` 进 ZHUANG_BU 秒·墙钟之局），余照真 date
                with open(os.path.join(_bin, _名), 'w') as f:
                    f.write('#!/bin/sh\n' + _体)
                os.chmod(os.path.join(_bin, _名), 0o755)
            with open(os.path.join(_根, '工具', '接棒守.py'), 'w', encoding='utf-8') as f:
                f.write('import json,os,sys\nj=json.load(open(os.environ["ZHUANG_JU"],encoding="utf-8"))\n'
                        'if "--早止" in sys.argv:\n    z=j["早"]\n'
                        '    if isinstance(z,list):\n        c=os.environ["ZHUANG_JI"]+"_早";i=int(open(c).read()) if os.path.exists(c) else 0;open(c,"w").write(str(i+1));z=z[min(i,len(z)-1)]\n'
                        '    print("桩");sys.exit(z)\n'
                        'c=os.environ["ZHUANG_JI"];i=int(open(c).read()) if os.path.exists(c) else 0\nopen(c,"w").write(str(i+1))\n'
                        'if j.get("误"):\n    sys.stderr.write("DeprecationWarning: 桩之警\\n");sys.stderr.flush()\n'
                        'y,rc=j["巡"][min(i,len(j["巡"])-1)]\nprint(y);sys.exit(rc)\n')

            def _跑(脚, 环境):
                _档 = os.path.join(_根, '脚.sh')
                with open(_档, 'w', encoding='utf-8') as f:
                    f.write(脚)
                return subprocess.run(['bash', '--noprofile', '--norc', '-eo', 'pipefail', _档], cwd=_根, env=环境, capture_output=True, text=True, timeout=60)

            _活 = '止\n⛔ 总编辑之坐之活守逾 24 时未复：存底迟 25 时（末一存 11-19 18:27 UTC）\n· 活守此态已唤（活守·2026-11-19T18:27Z）——⛔再唤（态变方唤；红随唤）'
            _停 = '⛔ 停写：第477章之心跳 40 分未更（限 25 分）——派\n· 同局（rc2·477）20 分内已唤——⛔再唤（红随唤：二十分一红，⛔每五分一邮）'
            for _号, _巡, _早, _分, _续们, _外 in (
                    ('活早', [[_活, 0]], 0, 3, [('', 0)], {}),                  # 活守已唤（rc 0·首行止）而早止可 → 连三止即早止、⛔续
                    ('活', [[_活, 0]], 1, 1, [('', 0)], {}),                    # 早止之察局悬（交棒中／主未含／封版之坐未收·rc 1）→ 跑满、末巡止而局悬 → 续（复核要害）
                    ('不验', [[_活, 0]], 3, 3, [('', 0)], {}),                  # 封者不可取（rc 3）→ ⛔早止、跑满、局止 → ⛔续（晚起之環同·⛔每章空续四回）
                    ('读不', [[_活, 0]], 2, 1, [('', 0)], {}),                  # 早止之察恒读不出（rc 2）→ ⛔续（器坏⛔每章空续四回）
                    ('末读不', [[_活, 0]], [1, 2], 1, [('', 0)], {}),           # 末巡之察读不出而前巡局悬 → zr 取末之可读者（1）→ 续
                    ('易', [[_活, 0]], [1, 1, 0], 3, [('', 0)], {}),            # 封版之坐持 N+1（rc 1）二巡、新坐接（rc 0）後连三止 → 第五巡早止
                    ('误', [['止', 0]], 0, 3, [('', 0)], {'误': 1}),            # 云巡之 stderr 有行（警）而 stdout「止」→ 首行仍止、三巡早止（stderr 另档）
                    ('墙', [['止', 0]], 1, 3, [], {'钟': 100}),                 # 每巡实耗逾 jian（假钟每读进百秒）→ 墙钟逾 fen 即止（槽计则六巡）
                    ('首唤', [[_活, 1], [_活, 0]], 0, 3, [('', 0)], {}),         # 活守首唤（rc 1·首行止）：其巡⛔计连止、红随唤；後三止早止
                    ('停', [[_停, 0]], 0, 1, [('', 0), ('', 4), ('候', 0), ('败', 0)], {})):   # 停写已唤（rc 0·首行⛔）→ 续；xu 4、新章之環在候⛔续；跑之列读不出照派
                _局档 = os.path.join(_根, '局_%s.json' % _号)
                with open(_局档, 'w', encoding='utf-8') as f:
                    json.dump({'巡': _巡, '早': _早, '误': _外.get('误', 0)}, f, ensure_ascii=False)
                _出档, _摘档 = os.path.join(_根, '出_%s' % _号), os.path.join(_根, '摘_%s' % _号)
                _境 = dict(os.environ, PATH=_bin + os.pathsep + os.environ.get('PATH', ''), ZHUANG_JU=_局档, ZHUANG_JI=os.path.join(_根, '计_%s' % _号),
                          GITHUB_OUTPUT=_出档, GITHUB_STEP_SUMMARY=_摘档, RUNNER_TEMP=_根, GITHUB_EVENT_NAME='workflow_dispatch',
                          GITHUB_REF_NAME='claude/the-novel-review-4dtuit', GITHUB_API_URL='https://api.invalid', GITHUB_REPOSITORY='o/r',
                          GITHUB_RUN_ID='900', GH_TOKEN='x', FEN=str(_分), JIAN='30', ZHI='477')
                _境.pop('ZHUANG_SHI', None)
                if _外.get('钟'):
                    with open(os.path.join(_根, '钟_%s' % _号), 'w') as f:
                        f.write('1700000000')
                    _境.update(ZHUANG_SHI=os.path.join(_根, '钟_%s' % _号), ZHUANG_BU=str(_外['钟']))
                _r = _跑(_环脚, _境)
                _出 = dict(x.split('=', 1) for x in open(_出档, encoding='utf-8').read().split('\n') if '=' in x) if os.path.exists(_出档) else {}
                _派们 = []
                for _候, _xc in _续们:
                    _派档, _跑档 = os.path.join(_根, '派_%s_%s%d' % (_号, _候, _xc)), os.path.join(_根, '跑_%s_%s%d' % (_号, _候, _xc))
                    with open(_跑档, 'w', encoding='utf-8') as f:
                        f.write('' if _候 == '败' else json.dumps({'workflow_runs': [{'id': 900, 'status': 'in_progress', 'head_branch': 'claude/the-novel-review-4dtuit', 'display_title': '巡环·90分·隔300秒'},
                                                                                {'id': 901, 'status': 'completed', 'head_branch': '章-476', 'display_title': '巡环·章-476'}]
                                                               + ([{'id': 902, 'status': 'pending', 'head_branch': '章-478', 'display_title': '巡环·章-478'}] if _候 == '候' else [])}, ensure_ascii=False))
                    _r2 = _跑(_续脚, dict(_境, ZHUANG_PAI=_派档, ZHUANG_PAO=_跑档, JIAN=_出.get('jian', ''), ZHI=_出.get('zhi', ''), REF=_出.get('ref', ''),
                                         ZAO=_出.get('zao', ''), MO=_出.get('mo', ''), ZR=_出.get('zr', ''), XC=str(_xc))) if _出.get('xu') != '0' else None
                    _派们.append((_r2.returncode if _r2 else None, open(_派档, encoding='utf-8').read() if os.path.exists(_派档) else '', _r2.stdout if _r2 else ''))
                _桩果[_号] = (_r.returncode, _出, _r.stdout.count('· 第 '), _派们)
    _桩 = lambda 号: _桩果.get(号, (None, {}, 0, []))
    _派了 = lambda 号: _桩(号)[3][0][0] == 0 and all(k in _桩(号)[3][0][1] for k in ('/dispatches', '"fen": "60"', '"zhi": "477"', '"xu": "1"', '"huan": "1"'))
    T('⑪之三b 桩局（复核③b·真跑環与续之 bash·桩代器）：印「止」「⛔活守…已唤」（rc 0）→ 连止照计、三巡早止、⛔续；早止之察局悬（rc 1：交棒中／主未含／封版之坐未收）→ 跑满而末巡止亦续（复核要害）；'
      '坐之易不可验（rc 3）、恒读不出（rc 2）→ ⛔早止、⛔续；末巡读不出 → zr 取末之可读者；封版之坐持 N+1 二巡（rc 1）、坐易後连三止 → 第五巡早止；云巡之 stderr 另档（首行仍止·早止）；墙钟逾 fen 即止；'
      '活守首唤（rc 1·首行止）→ 其巡⛔计连止、红、後三止早止；「⛔停写…」「· 同局已唤」（rc 0）→ 末巡之局非止而续（fen 60·zhi 同·xu 1）；xu 4、本组新章之環在候→⛔续；跑之列读不出（-eo pipefail）→ 照派 %s'
      % {k: (v[0], v[1].get('zao'), v[1].get('mo'), v[1].get('zr'), v[2], [(x[0], bool(x[1])) for x in v[3]]) for k, v in _桩果.items()},
      (not shutil.which('bash') or not shutil.which('timeout'))
      or (_桩('活早')[0] == 0 and _桩('活早')[1].get('zao') == '1' and _桩('活早')[1].get('mo') == '0' and _桩('活早')[2] == 3
          and _桩('活早')[1].get('hong') == '0' and _桩('活早')[3][0][:2] == (0, '') and '早止' in _桩('活早')[3][0][2]
          and _桩('活')[1].get('zao') == '0' and _桩('活')[1].get('mo') == '0' and _桩('活')[1].get('zr') == '1' and _桩('活')[2] == 2
          and _派了('活') and '末巡止而早止之察见局悬' in _桩('活')[3][0][2]
          and _桩('不验')[1].get('zr') == '3' and _桩('不验')[1].get('zao') == '0' and _桩('不验')[2] == 6
          and _桩('不验')[3][0][:2] == (0, '') and '未见局悬' in _桩('不验')[3][0][2]
          and _桩('读不')[1].get('zr') == '' and _桩('读不')[3][0][:2] == (0, '') and '未见局悬' in _桩('读不')[3][0][2]
          and _桩('末读不')[1].get('zr') == '1' and _派了('末读不')
          and _桩('易')[1].get('zao') == '1' and _桩('易')[2] == 5 and _桩('易')[3][0][:2] == (0, '')
          and _桩('误')[1].get('zao') == '1' and _桩('误')[1].get('mo') == '0' and _桩('误')[2] == 3
          and _桩('墙')[2] == 2 and _桩('墙')[1].get('fen') == '3'
          and _桩('首唤')[1].get('zao') == '1' and _桩('首唤')[1].get('hong') == '1' and _桩('首唤')[2] == 4 and _桩('首唤')[3][0][1] == ''
          and _桩('停')[1].get('zao') == '0' and _桩('停')[1].get('mo') == '1' and _桩('停')[2] == 2 and _桩('停')[1].get('ref') == 'claude/the-novel-review-4dtuit'
          and _派了('停') and '末巡非止' in _桩('停')[3][0][2]
          and _桩('停')[3][1][:2] == (0, '') and '四续' in _桩('停')[3][1][2]
          and _桩('停')[3][2][:2] == (0, '') and '902:巡环·章-478' in _桩('停')[3][2][2]
          and _桩('停')[3][3][0] == 0 and '"xu": "1"' in _桩('停')[3][3][1]))
    T('⑪之三c 云巡先印 巡() 之出、後跑 自决之巡／活守之巡（巡.yml 以印之首行定局之所恃）',
      _段云.index('print(印.rstrip())') < _段云.index('自决之巡(仓, 今') < _段云.index('活守之巡(仓, 今'))
    _旧A, _新B = '018旧坐_封477', '018新坐_写478'
    T('⑪之十 早止判（W910·章推之環·复核要害）：主枝含章-N 而心跳之章 ≥N+1 且其坐异於章-N 之封者（旧坐）→真；旧坐持 N+1（封版之坐先跳 N+1 後推章-N、至主含方收）→假（局悬 rc 1）；'
      '旧坐不可取、心跳之坐空或未名→假（rc 3·坐之易不可验）；暂停→真（⛔问含·无可察）；交棒中（章 None·毕）、主未含、心跳之章 ≤N、非 int（字串、bool）→假（rc 1）；读不出（非 dict）、N 非数→假（rc 2）',
      早止判({'章': 478, '时': 1, '坐': _新B}, 477, True, _旧A) is True and 早止判({'章': 479, '坐': _新B}, 477, True, _旧A) is True
      and 早止判({'章': 478, '时': 1, '坐': _旧A}, 477, True, _旧A) is False and 早止之局({'章': 478, '坐': _旧A}, 477, True, _旧A)[0] == 1
      and 早止判({'章': 478, '坐': _新B}, 477, True) is False and 早止判({'章': 478, '坐': _新B}, 477, True, '') is False
      and 早止之局({'章': 478, '坐': _新B}, 477, True, '')[0] == 3
      and 早止之局({'章': 478, '坐': '未名'}, 477, True, _旧A)[0] == 3 and 早止之局({'章': 478}, 477, True, _旧A)[0] == 3
      and 早止判({'章': '暂停', '坐': '暂停令'}, 476, True) is True and 早止判({'章': '暂停', '坐': '暂停令'}, 476, False, _旧A) is True
      and 早止判({'章': None, '毕': 478, '时': 1, '坐': _旧A}, 477, True, _旧A) is False and 早止之局({'章': None, '毕': 478, '坐': _旧A}, 477, True, _旧A)[0] == 1
      and 早止判({'章': 478, '坐': _新B}, 477, False, _旧A) is False and 早止之局({'章': 478, '坐': _新B}, 477, False, _旧A)[0] == 1
      and 早止判({'章': 477, '坐': _新B}, 477, True, _旧A) is False and 早止判({'章': '478', '坐': _新B}, 477, True, _旧A) is False
      and 早止判({'章': True, '坐': _新B}, 0, True, _旧A) is False
      and 早止之局(None, 477, True, _旧A)[0] == 2 and 早止之局('x', 477, True, _旧A)[0] == 2 and 早止之局({'章': 478, '坐': _新B}, 'x', True, _旧A)[0] == 2)
    _段主0 = open(os.path.abspath(__file__), encoding='utf-8').read().split("\nif __name__ == '__main__':")[1]
    _旧远2, _旧含, _旧章坐 = _心._远, globals()['主含'], globals()['章之坐']
    _早, _取坐 = [], []
    _早印 = _io.StringIO()
    try:
        with _cl.redirect_stdout(_早印):
            for _远值, _含值, _坐值 in (((True, {'章': 478, '时': 1, '坐': _新B}), True, _旧A),       # 新坐已接 → 0
                                       ((True, {'章': 478, '时': 1, '坐': _旧A}), True, _旧A),       # 封版之坐持 N+1、主已含（推後收前）→ 1
                                       ((True, {'章': None, '毕': 478, '时': 1, '坐': _旧A}), True, _旧A),   # 交棒中 → 1
                                       ((True, {'章': 478, '坐': _新B}), False, _旧A),              # 主未含 → 1（⛔取封者）
                                       ((True, {'章': 478, '坐': _新B}), True, ''),                 # 章-N 无 Claude-Session 之尾 → 3
                                       ((False, None), True, _旧A), ((True, None), True, _旧A), (None, True, _旧A)):
                _心._远 = (lambda v=_远值: v) if _远值 is not None else (lambda: 1 / 0)
                globals()['主含'] = lambda n, v=_含值: v
                globals()['章之坐'] = lambda n, v=_坐值: (_取坐.append(n), v)[1]
                _早.append(早止(477))
            _早.append(早止('x'))
    finally:
        _心._远, globals()['主含'], globals()['章之坐'] = _旧远2, _旧含, _旧章坐
    T('⑪之十一 --早止 N 之 rc：新坐已接 0、封版之坐持 N+1（主已含）／交棒中／主未含 1、章-N 之封者不可取 3、心跳不在／读不出／读之抛／N 非数 2（异常⛔崩）；'
      '旧坐取 章之坐(N)（主未含⛔取）；首行印其判；令之入在 __main__ %s' % _早,
      _早 == [0, 1, 1, 1, 3, 2, 2, 2, 2] and _取坐 == [477, 477, 477, 477] and '可止：主枝含章-477' in _早印.getvalue() and '封版之坐未收' in _早印.getvalue()
      and "if '--早止' in a:" in _段主0 and 'sys.exit(早止(_n))' in _段主0 and 'sys.exit(2)' in _段主0.split("if '--早止' in a:")[1].split('sys.exit(早止(_n))')[0])
    T('⑪之九 合入之卡：键以章（印之分数异而键同·⛔每五分一唤）；唤时先 workflow_dispatch autopush（ref 章-N）、同局已派⛔复派（W908 复核：同局一派）',
      云巡判(4, _d, _今, [], '⛔ 停书：第456章已封（章-456 abc）31 分未入主枝')[1] == 云巡判(4, _d, _今, [], '⛔ 停书：第456章已封（章-456 abc）36 分未入主枝')[1] == 'rc4·456'
      and 云巡判(4, _d, _今, [(_今 - 300, 'rc4·456')], '⛔ 停书：第456章已封（章-456 abc）36 分未入主枝')[0] is False
      and '再闸(仓' in _段云 and '再闸之机(rc, 唤, 键, 旧, 试)' in _段云 and '态=_卡之态' in _段云
      and "'ref': '章-%s' % n" in src.split('def 再闸(')[1].split('\ndef ')[0])
    _w = [(_今 - (应之候分 + 5) * 60, 'rc2·455·1'), (_今 - 3 * 60, '试·9'), (_今 - 2 * 60, '私·9')]
    T('⑪之五 应判（闭环）：真唤逾应之候（三十分）而巡应未更於其後→未应；应新於唤、未逾应之候、无真唤（试／私不计）→空',
      应之候分 == 30 and '未应' in 应判(_w, _今 - (应之候分 + 10) * 60, _今) and 应判(_w, _今 - (应之候分 + 4) * 60, _今) == ''
      and 应判(_w, 0, _今 - 6 * 60) == ''
      and 应判([(_今 - 3600, '试·1'), (_今 - 3600, '私·1')], 0, _今) == '' and '未应' in 应判(_w, None, _今) and 应判([], 0, _今) == '')
    _hd = {'章': 455, '时': _今 - 600, '坐': 'A'}
    T('⑪之六 对拍判（常对拍）：同一心跳而云判异→不合；判同、心跳异、rc 4／1／5、心时缺→空',
      '对拍不合' in 对拍判({'时': _今, 'rc': 2, '心时': _今 - 600}, _hd, False, _限)
      and 对拍判({'时': _今, 'rc': 0, '心时': _今 - 600}, _hd, False, _限) == ''
      and 对拍判({'时': _今 + _限, 'rc': 2, '心时': _今 - 600}, _hd, False, _限) == ''
      and '对拍不合' in 对拍判({'时': _今 + _限, 'rc': 0, '心时': _今 - 600}, _hd, False, _限)
      and 对拍判({'时': _今, 'rc': 2, '心时': _今 - 601}, _hd, False, _限) == ''
      and 对拍判({'时': _今, 'rc': 4, '心时': _今 - 600}, _hd, False, _限) == '' and 对拍判({'时': _今, 'rc': 2}, _hd, False, _限) == ''
      and 对拍判(None, _hd, False, _限) == '')
    _号 = {x[0]: x[1] for x in 兜底之令}
    _降印, _私印 = 巡印判(None, _今, 章=(476, _t章)), 巡印判({'时': _今, '私': True}, _今)
    T('⑪之七 巡印判之降级：停摆→附 run_workflow 与降级之令（丙 enabled true、乙 cron :47·各名其号；甲⛔动）；私→自停之由并降级；'
      'rc 5→7 复常之印在沙盒之巡（丙 enabled false、乙 cron :57）',
      兜底之改(True) == 'update_trigger %s（丙）之 enabled「true」；update_trigger %s（乙）之 cron_expression「47 * * * *」' % (_号['丙'], _号['乙'])
      and 兜底之改(False) == 'update_trigger %s（丙）之 enabled「false」；update_trigger %s（乙）之 cron_expression「57 * * * *」' % (_号['丙'], _号['乙'])
      and 兜底之改(True) in _降印 and ':07 :27 :47' in _降印 and _号['甲'] not in _降印 and 'cron「' not in _降印
      and 'run_workflow' in _停印 and 兜底之改(True) in _停印 and '"zhi":"476"' in _降印
      and '私有' in _私印 and 兜底之改(True) in _私印 and 巡印判({'时': _今, '私': False}, _今) == ''
      and 'return 7' in _段巡 and '兜底之改(False)' in _段巡 and 'return 6' in _段巡
      and _段巡.index('return 5') < _段巡.index('return 7') < _段巡.index('return 6') < _段巡.index("print('止')"))
    T('⑪之八 云巡：仓私即自停（disable·在唤之前）、唤而未应即红；红随唤（不唤之跑⛔红）；落巡印记所判之心跳',
      '私停(仓, 今)' in _段云 and _段云.index('私停(仓, 今)') < _段云.index('哨PR(仓)') and '应判(' in _段云
      and "return 决rc\n" in _段云.split('if not 唤:')[1].split('体 =')[0] and '心=d' in _段云 and '_巡之心' in _段云   # 〔W908 环12③〕同局已唤⛔红（唯自决之唤之红随之）
      and '/disable' in src.split('def 私停(')[1].split('\ndef ')[0])
    T('⑦之四 诸印之令俱指 --派令（⛔手拟【派】）', src.count('--派令 %s') >= 2 and '令「【派】开第' not in src)
    _起们 = []
    _原迹存 = os.environ.pop('ZM_TRACE_SAVE', None)
    try:
        迹存('t', 起=lambda a, **k: _起们.append((a, k)))
    finally:
        if _原迹存 is not None:
            os.environ['ZM_TRACE_SAVE'] = _原迹存
    _段主 = open(os.path.abspath(__file__), encoding='utf-8').read().split("\nif __name__ == '__main__':")[1]
    T('X86 --候主／--派令 之末起後台之存（脱离、候三秒、⛔续心跳），迹先落而後存',
               len(_起们) == 1 and _起们[0][1].get('start_new_session') is True and 'sleep 3;' in _起们[0][0][2]
               and '--不续心跳 --存' in _起们[0][0][2] and '存底.py' in _起们[0][0][2]
               and _段主.split("'--派令' in a")[1].split('sys.exit')[0].count('迹存(') == 1
               and _段主.split("'--候主' in a")[1].split('sys.exit')[0].count('迹存(') == 1)
    _段巡沙 = _段主.split("if '--巡' in a:")[1].split('sys.exit(_rc)')[0] if "if '--巡' in a:" in _段主 else ''
    T('1119 沙盒之巡每跑验存底守在跑、不在即起（印归 stderr、⛔扰「止」）；GitHub 之巡⛔起',
      '_守.在跑()' in _段巡沙 and '_守.起()' in _段巡沙 and 'redirect_stdout(sys.stderr)' in _段巡沙
      and _段巡沙.index('_守.起()') > _段巡沙.index("GITHUB_ACTIONS") and _段巡沙.index('_守.起()') < _段巡沙.index('巡(查印=True)'))
    # ── 〔1119 执行之审·治1〕活守：以本坐真迹回放（验四格·设计「验」）──
    #   本坐 _器之迹（gitignore·只在本机）之真行：11-16T12:00—11-17T10:10 之诸 --巡 行与其前六十秒内之 链之检 行（照档之序；他行与判无涉、略之）
    _迹真 = """
{"t": "2026-11-16T12:02:42", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:02:54", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:02:59", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:03:01", "器": "接棒守.py", "参": ["--巡"], "秒": 0.41, "rc": 0, "流": ""}
{"t": "2026-11-16T12:09:41", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:09:55", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:10:39", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:10:40", "器": "接棒守.py", "参": ["--巡"], "秒": 3.43, "rc": 0, "流": ""}
{"t": "2026-11-16T12:27:54", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:27:55", "器": "接棒守.py", "参": ["--巡"], "秒": 1.97, "rc": 0, "流": ""}
{"t": "2026-11-16T12:28:06", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:28:07", "器": "接棒守.py", "参": ["--巡"], "秒": 2.66, "rc": 0, "流": ""}
{"t": "2026-11-16T12:39:25", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:39:33", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:39:53", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:39:54", "器": "接棒守.py", "参": ["--巡"], "秒": 2.63, "rc": 0, "流": ""}
{"t": "2026-11-16T12:51:13", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T12:51:13", "器": "接棒守.py", "参": ["--巡"], "秒": 1.78, "rc": 2, "流": ""}
{"t": "2026-11-16T13:10:11", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T13:10:15", "器": "接棒守.py", "参": ["--巡"], "秒": 1.73, "rc": 0, "流": ""}
{"t": "2026-11-16T13:12:23", "器": "链之检.py", "参": [], "秒": 0.01, "rc": 0, "流": ""}
{"t": "2026-11-16T13:12:24", "器": "接棒守.py", "参": ["--巡"], "秒": 2.08, "rc": 0, "流": ""}
{"t": "2026-11-16T13:28:19", "器": "接棒守.py", "参": ["--巡"], "秒": 3.32, "rc": 0, "流": ""}
{"t": "2026-11-16T13:32:14", "器": "接棒守.py", "参": ["--巡"], "秒": 2.11, "rc": 0, "流": ""}
{"t": "2026-11-16T13:50:12", "器": "接棒守.py", "参": ["--巡"], "秒": 3.45, "rc": 0, "流": ""}
{"t": "2026-11-16T14:11:24", "器": "接棒守.py", "参": ["--巡"], "秒": 3.43, "rc": 0, "流": ""}
{"t": "2026-11-16T14:27:58", "器": "接棒守.py", "参": ["--巡"], "秒": 3.53, "rc": 0, "流": ""}
{"t": "2026-11-16T14:48:41", "器": "接棒守.py", "参": ["--巡"], "秒": 4.17, "rc": 0, "流": ""}
{"t": "2026-11-16T15:10:05", "器": "接棒守.py", "参": ["--巡"], "秒": 3.91, "rc": 0, "流": ""}
{"t": "2026-11-16T15:27:49", "器": "接棒守.py", "参": ["--巡"], "秒": 3.43, "rc": 0, "流": ""}
{"t": "2026-11-17T03:05:24", "器": "接棒守.py", "参": ["--巡"], "秒": 2.03, "rc": 2, "流": ""}
{"t": "2026-11-17T03:12:13", "器": "接棒守.py", "参": ["--巡"], "秒": 1.83, "rc": 0, "流": ""}
{"t": "2026-11-17T03:27:22", "器": "接棒守.py", "参": ["--巡"], "秒": 3.09, "rc": 0, "流": ""}
{"t": "2026-11-17T03:48:19", "器": "接棒守.py", "参": ["--巡"], "秒": 2.8, "rc": 0, "流": ""}
{"t": "2026-11-17T04:07:39", "器": "接棒守.py", "参": ["--巡"], "秒": 3.32, "rc": 0, "流": ""}
{"t": "2026-11-17T04:27:42", "器": "接棒守.py", "参": ["--巡"], "秒": 3.27, "rc": 0, "流": ""}
{"t": "2026-11-17T04:47:52", "器": "接棒守.py", "参": ["--巡"], "秒": 2.81, "rc": 0, "流": ""}
{"t": "2026-11-17T05:07:38", "器": "接棒守.py", "参": ["--巡"], "秒": 3.48, "rc": 0, "流": ""}
{"t": "2026-11-17T05:28:10", "器": "接棒守.py", "参": ["--巡"], "秒": 3.04, "rc": 0, "流": ""}
{"t": "2026-11-17T05:48:26", "器": "接棒守.py", "参": ["--巡"], "秒": 4.55, "rc": 0, "流": ""}
{"t": "2026-11-17T06:08:14", "器": "接棒守.py", "参": ["--巡"], "秒": 3.65, "rc": 0, "流": ""}
{"t": "2026-11-17T06:27:50", "器": "接棒守.py", "参": ["--巡"], "秒": 3.17, "rc": 0, "流": ""}
{"t": "2026-11-17T06:49:39", "器": "接棒守.py", "参": ["--巡"], "秒": 2.87, "rc": 0, "流": ""}
{"t": "2026-11-17T07:08:40", "器": "接棒守.py", "参": ["--巡"], "秒": 3.26, "rc": 0, "流": ""}
{"t": "2026-11-17T07:28:05", "器": "接棒守.py", "参": ["--巡"], "秒": 2.92, "rc": 0, "流": ""}
{"t": "2026-11-17T08:00:06", "器": "接棒守.py", "参": ["--巡"], "秒": 2.58, "rc": 0, "流": ""}
{"t": "2026-11-17T08:06:54", "器": "接棒守.py", "参": ["--巡"], "秒": 1.89, "rc": 0, "流": ""}
{"t": "2026-11-17T08:14:45", "器": "接棒守.py", "参": ["--巡"], "秒": 6.23, "rc": 0, "流": ""}
{"t": "2026-11-17T08:19:23", "器": "接棒守.py", "参": ["--巡"], "秒": 6.42, "rc": 0, "流": ""}
{"t": "2026-11-17T08:20:41", "器": "接棒守.py", "参": ["--巡"], "秒": 4.22, "rc": 0, "流": ""}
{"t": "2026-11-17T08:24:05", "器": "接棒守.py", "参": ["--巡"], "秒": 5.45, "rc": 0, "流": ""}
{"t": "2026-11-17T08:27:34", "器": "接棒守.py", "参": ["--巡"], "秒": 5.59, "rc": 0, "流": ""}
{"t": "2026-11-17T08:48:10", "器": "接棒守.py", "参": ["--巡"], "秒": 6.16, "rc": 0, "流": ""}
{"t": "2026-11-17T09:07:40", "器": "接棒守.py", "参": ["--巡"], "秒": 5.71, "rc": 5, "流": ""}
{"t": "2026-11-17T09:08:22", "器": "接棒守.py", "参": ["--巡"], "秒": 4.36, "rc": 7, "流": ""}
{"t": "2026-11-17T09:28:12", "器": "接棒守.py", "参": ["--巡"], "秒": 6.52, "rc": 0, "流": ""}
{"t": "2026-11-17T09:57:31", "器": "接棒守.py", "参": ["--巡"], "秒": 6.04, "rc": 5, "流": ""}
{"t": "2026-11-17T09:59:02", "器": "接棒守.py", "参": ["--巡"], "秒": 4.51, "rc": 7, "流": ""}
{"t": "2026-11-17T10:08:32", "器": "接棒守.py", "参": ["--巡"], "秒": 7.19, "rc": 0, "流": ""}
""".strip().split('\n')
    _判, _态 = {}, {}
    for _i, _l in enumerate(_迹真):
        _d = json.loads(_l)
        if _d['器'] == '接棒守.py' and _d['参'][:1] == ['--巡']:
            _t = _迹时(_d['t'])
            _态 = 钩态推(_态, 钩活判(_迹真[:_i], _t), _t)        # 巡起之时所见：档中其前之诸行
            _判[_d['t']] = dict(_态)
    _末 = _判['2026-11-17T10:08:32']
    T('活守①〔治1·a·验1〕真迹回放：11-16T12:03:01、13:12:24（前 1 秒有 链之检）→ 钩活；13:28:19、13:32:14 → 疑（连缺未满三巡·⛔误拦）；'
      '13:50:12 → 死；11-17T10:08:32（链之检末迹 11-16T13:12:23）→ 死、钩死起＝首缺 11-16T13:28:19、连缺 %d 巡' % _末.get('无钩', 0),
      _判['2026-11-16T12:03:01']['钩'] == '活' and _判['2026-11-16T13:12:24']['钩'] == '活'
      and [_判[k]['钩'] for k in ('2026-11-16T13:28:19', '2026-11-16T13:32:14', '2026-11-16T13:50:12')] == ['疑', '疑', '死']
      and _末['钩'] == '死' and _末['钩死起'] == _迹时('2026-11-16T13:28:19') and _末['无钩'] == 37
      and _判['2026-11-16T13:12:24']['钩死起'] is None and _判['2026-11-16T13:12:24']['末活'] == _迹时('2026-11-16T13:12:24'))
    with tempfile.TemporaryDirectory() as _dd:
        _迹档 = os.path.join(_dd, '迹.jsonl')
        open(_迹档, 'w', encoding='utf-8').write('x' * (迹尾 + 10) + '\n' + '\n'.join(_迹真) + '\n')
        _尾 = _读尾(_迹档)
        _t1312, _t1708 = _迹时('2026-11-16T13:12:24'), _迹时('2026-11-17T10:08:32')
        _杂 = [json.dumps({'t': '2026-11-16T13:12:20', '器': '链之检.py', '参': ['--自测'], 'rc': 0}),
               json.dumps({'t': '2026-11-16T13:11:23', '器': '链之检.py', '参': [], 'rc': 0})]
        T('活守①之二 读档之路（末 64KB·首残行弃）：13:12:24 → 活、11-17T10:08:32 → 无；带参之 链之检（--自测）、逾六十秒者⛔算',
          not _尾[0].startswith('x') and 钩活判(_尾, _t1312) and not 钩活判(_尾, _t1708)
          and not 钩活判(_杂, _t1312) and 钩活判(_杂[1:], _t1312 - 1))
    _志真 = ['11-16 12:56:53 ✓ 0465e7d3 → 备份/存底', '11-16 13:01:55 ✓ 无改·不推', '11-16 13:06:57 ✓ 无改·不推',
            '11-16 13:12:06 ✓ 53d6df1a → 旁枝 备份/存底-018Kg61wMkRD（第456章之锁为他坐 018Kg61yqHgh 所持）', '11-16 13:17:09 ✓ 无改·不推']
    _今17 = _迹时('2026-11-17T10:00:00')
    _存, _起 = 存底末刻(_志真, _今17)
    _复 = _志真 + ['11-19 16:31:45 ✓ 89978000 → 旁枝 备份/存底-018Kg61wMkRD（第473章之锁为他坐 018Kg61wDqAm 所持）', '11-19 16:32:21 起 pid 3192（每 5 分一回）']
    _存2, _起2 = 存底末刻(_复, _迹时('2026-11-19T16:40:00'))
    T('活守②〔治1·b·验2〕存底守.log 真行：末存 11-16 13:17:09、今 11-17 → 存底迟（守在跑却不存）；11-19 16:31:45 复存、今 16:40 → ⛔迟',
      _存 == _迹时('2026-11-16T13:17:09') and '存底迟' in 存底迟判(_存, _起, _今17) and '1242 分前' in 存底迟判(_存, _起, _今17)
      and 存底迟判(_存, _起, _存 + 14 * 60) == '' and _存2 == _迹时('2026-11-19T16:31:45') and _起2 == _迹时('2026-11-19T16:32:21')
      and 存底迟判(_存2, _起2, _迹时('2026-11-19T16:40:00')) == '')
    _旧起 = ['11-19 16:00:00 ✓ 无改·不推', '11-19 16:30:00 起 pid 1（每 5 分一回）']
    _s3, _q3 = 存底末刻(_旧起, _迹时('2026-11-19T16:33:00'))
    T('活守②之二 「⛔」之行⛔算存（全败即缺）；跨年（12-31 之行、今 01-01）取去年；守本在而方起未逾一隔 → 候（⛔迟），本巡方起之守⛔宽（附「守今方起」）',
      存底末刻(['11-16 12:30:40 ⛔ fatal: repository not found'], _今17)[0] == 0 and '缺' in 存底迟判(0, 0, _今17)
      and 存底末刻(['12-31 23:58:00 ✓ 无改·不推'], _迹时('2027-01-01T00:05:00'))[0] == _迹时('2026-12-31T23:58:00')
      and 存底迟判(_s3, _q3, _迹时('2026-11-19T16:33:00'), 守先在=True) == ''
      and '守今方起' in 存底迟判(_s3, _q3, _迹时('2026-11-19T16:33:00'), 守先在=False))
    # 验3：钩死之自决代扫与补印（转录以 11-16 之真句造：11:31 红、11:40 红、「等你下令（暂停令）」绿）
    with tempfile.TemporaryDirectory() as _dd:
        _录 = os.path.join(_dd, 'fc.jsonl')
        def _写录(诸, 续=False):
            with open(_录, 'a' if 续 else 'w', encoding='utf-8') as _f:
                for _x in 诸:
                    _f.write(json.dumps(_x, ensure_ascii=False) + '\n')
        _答 = lambda ts, 文, u=0: {'type': 'assistant', 'timestamp': ts, 'message': dict({'content': [{'type': 'text', 'text': 文}]},
                                   **({'usage': {'input_tokens': 2, 'cache_read_input_tokens': u - 2, 'cache_creation_input_tokens': 0}} if u else {}))}
        _压 = lambda ts: {'type': 'system', 'subtype': 'compact_boundary', 'timestamp': ts}
        _写录([_答('2026-11-16T11:31:32.984Z', '我去跑时，被平台的安全检查拦下了，理由是直接推主线属于危险操作。这一步要你点头，我不绕过。'),
              _答('2026-11-16T11:40:52.914Z', '2 笔本地提交都还在本机。\n\n等你开好两步验证跟我说一声，我马上重新跑一遍检查，然后推送。'),
              _答('2026-11-16T11:45:00.000Z', '411 照你上一条指示锁着，等你下令（暂停令）再开。', 334567)])
        _态档, _空迹, _志 = os.path.join(_dd, '态.json'), os.path.join(_dd, '迹.jsonl'), os.path.join(_dd, 'log')
        open(_空迹, 'w').write(json.dumps({'t': '2026-11-16T11:00:00', '器': '链之检.py', '参': []}) + '\n')
        open(_志, 'w').write('11-16 12:58:00 ✓ 无改·不推\n')
        _t = _录时('2026-11-16T13:00:00Z')
        json.dump({'钩': '疑', '无钩': 2, '首缺': _t - 3600, '录': _录, '偏': 0, '扫自': _t - 7200, '日': '2026-11-15'}, open(_态档, 'w'))
        _补, _费 = [], []
        跑 = lambda 今: 活守(今=今, 态档=_态档, 迹=_空迹, 志=_志, 录=_录, 补=_补.append, 记费=_费.append)
        with contextlib.redirect_stdout(io.StringIO()) as _o1:
            _s1 = 跑(_t)
        _写录([_压('2026-11-16T13:10:00.000Z'), _答('2026-11-16T13:11:00.000Z', '要不要我先推？')], 续=True)
        with contextlib.redirect_stdout(io.StringIO()) as _o2:
            _s2 = 跑(_t + 1800)
        open(_空迹, 'a', encoding='utf-8').write(json.dumps({'t': time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(_t + 3600)), '器': '链之检.py', '参': []},
                                                       ensure_ascii=False) + '\n')
        _写录([_答('2026-11-16T13:40:00.000Z', '这一步要你点头。')], 续=True)
        with contextlib.redirect_stdout(io.StringIO()) as _o3:
            _s3 = 跑(_t + 3600)
        _o1, _o2, _o3 = _o1.getvalue(), _o2.getvalue(), _o3.getvalue()
        T('活守③〔治1·c·验3〕钩死（第三缺）：扫末活以来之答——「这一步要你点头」（11:31）、「等你开好两步验证跟我说一声」（11:40）→ 自决红；'
          '「等你下令（暂停令）」→ ⛔红；首见钩死即补印一回、钩死起＝首缺；〔W910〕钩死之 ⚠ 书「钩复载已弃·以巡代钩」（⛔「待甲」）',
          _s1['钩'] == '死' and _s1['钩死起'] == _t - 3600 and _o1.count('自决红') == 2 and '要你点头' in _o1 and '跟我说' in _o1
          and '等你下令' not in _o1 and '钩死' in _o1 and _补[:1] == ['首见钩死']
          and '（钩复载已弃·以巡代钩：本巡代扫自决、代印开头之串）' in _o1 and '待甲' not in _o1)
        T('活守③之二 其後之巡只扫增量（⛔复红旧句）、见 compact_boundary 即再补印；钩复活即清（⛔扫、⛔补、钩死起空、偏进至末）',
          _o2.count('自决红') == 1 and '要不要我' in _o2 and _补 == ['首见钩死', 'compact 之後 1 回']
          and _s3['钩'] == '活' and _s3['钩死起'] is None and '自决红' not in _o3 and len(_补) == 2 and _s3['偏'] == os.path.getsize(_录))
        T('活守③之三〔治1·d〕每日首巡记本坐之费（一日一回）；上下文逾三十万即印「减本坐之活」（一日一印·与作者对谈照常令 1024 令（压缩对话）②·器⛔与常令分歧）；记费之参取昨日；'
          '日行之键同 `费审 --记主`（主环:<昨日 00:00Z>）',
          _费 == ['2026-11-16'] and '减本坐之活' in _o1 and '约 33 万' in _o1 and '减本坐之活' not in _o2 and _s1['上下文'] == 334567
          and '常令 1024 令（压缩对话）②' in _o1 and '⛔请作者按键' not in _o1
          and 记费之参('2026-11-19') == ('总编辑之坐·2026-11-18', '2026-11-18T00:00:00Z', '2026-11-19T00:00:00Z')
          and "费审.记('主环:%s' % 起, 名, [行], None, root, 时=起)" in src.split('def 记本坐之费(')[1].split('\ndef ')[0])
        json.dump({}, open(_态档, 'w'))
        with contextlib.redirect_stdout(io.StringIO()):
            _s4 = 跑(_t)
        T('活守③之四 疑（未满三巡）⛔进偏、⛔扫：判死之巡自末活之处扫起（⛔漏其间之答）；初跑以「扫自」之时滤之',
          _s4['钩'] == '疑' and _s4['偏'] == 0 and _s4['扫自'] == _t - 35 * 60)
    _今 = 10 ** 9
    _应 = lambda **k: dict({'时': _今, 'rc': 0, '钩': '死', '存底刻': _今 - 300, '钩死起': _今 - 25 * 3600}, **k)
    _迟 = _应(存底刻=_今 - 25 * 3600)       # 钩死且存底迟（俱逾二十四时）
    T('活守④〔治1·e·验4；W910〕云巡之判：钩死逾二十四时而存底不迟 → 空（钩复载已弃·⛔红）；钩死一时、钩活、钩疑而存底照常 → 空；旧巡应（无三键）→ 空（⛔红）；'
      '末存逾二十四时 → 红（钩活、钩死俱同·其由⛔书钩死、⛔书待甲）',
      活守判(_应(), _今) == '' and 活守判(_应(钩死起=_今 - 3600), _今) == '' and 活守判({'时': _今, 'rc': 0}, _今) == ''
      and 活守判({'时': _今, 'rc': 0, '存底刻': _今 - 25 * 3600}, _今) == ''
      and '存底迟 25 时' in 活守判(_应(钩='活', 钩死起=None, 存底刻=_今 - 25 * 3600), _今) and 活守判(_应(钩='活', 钩死起=None), _今) == ''
      and 活守判(_应(钩='疑', 钩死起=None), _今) == '' and '存底迟 25 时' in 活守判(_迟, _今)
      and '钩死' not in 活守判(_迟, _今) and '待甲' not in 活守判(_迟, _今) and '钩复载' not in 活守判(_迟, _今)
      and 活守判(_迟, _今) == 活守判(_应(钩='活', 钩死起=None, 存底刻=_今 - 25 * 3600), _今))
    _演 = dict(_末, 存底刻=_存)        # 演（上线之前·设计）：11-17、11-18 之况——巡 rc 0 而钩死、存底守不存（以上二格之真迹回放所得之态）
    _应17 = json.loads(巡应之体(0, _迹时('2026-11-17T10:08:32'), _演))
    _应18 = json.loads(巡应之体(0, _迹时('2026-11-18T00:00:00'), _演))
    _钩18 = json.loads(巡应之体(0, _迹时('2026-11-18T00:00:00'), dict(_末, 存底刻=_迹时('2026-11-17T23:55:00'))))   # 同时钩死 34 时而存底照常
    T('活守④之三 演 11-17／11-18（巡 rc 0 而钩死、存底守不存·真迹之态）：11-17T10:08 未逾二十四时 → ⛔红（沙盒自印）；11-18T00:00 → 红（存底迟 34 时·⛔书钩死）；'
      '〔W910〕11-18T00:00 钩死 34 时而存底照常 → ⛔红',
      活守判(_应17, _迹时('2026-11-17T10:08:32')) == '' and '存底迟 34 时' in 活守判(_应18, _迹时('2026-11-18T00:00:00'))
      and '钩死' not in 活守判(_应18, _迹时('2026-11-18T00:00:00')) and _应18['rc'] == 0 and _应18['钩'] == '死'
      and _钩18['钩'] == '死' and 活守判(_钩18, _迹时('2026-11-18T00:00:00')) == '')
    _发 = []
    _日键 = 活守之键(_迟, _今)[0]          # 〔W908 环2(a)；W910〕键「活守·<存底迟起>」（旧「活守·<日>」、「活守·<钩死起>·<存底迟起>」）
    with contextlib.redirect_stdout(io.StringIO()):
        _r1 = 活守之巡('o/r', _今, 应d=_迟, 号=1, 键们=set(), 发=_发.append, 停=False)
        _r2 = 活守之巡('o/r', _今, 应d=_迟, 号=1, 键们={_日键}, 发=_发.append, 停=False)
        _r3 = 活守之巡('o/r', _今, 应d=_应(存底刻=_今 - 3600), 号=1, 键们=set(), 发=_发.append, 停=False)
        _r4 = 活守之巡('o/r', _今, 应d={'时': _今, 'rc': 0}, 号=1, 键们=set(), 发=_发.append, 停=False)
        _r5 = 活守之巡('o/r', _今, 应d=_应(), 号=1, 键们=set(), 发=_发.append, 停=False)
    T('活守④之二 态变方唤：存底迟逾二十四时首跑 → 唤（键「活守·<存底迟起>」）而红；此态已唤 → ⛔唤⛔红；未逾、旧巡应 → ⛔唤；'
      '〔W910〕钩死逾二十四时而存底不迟 → ⛔唤⛔红；唤之言⛔书钩死；云巡 rc 0 之支走之（私停之後）',
      _r1 == 1 and len(_发) == 1 and (警记 % _日键) in _发[0] and _r2 == 0 and _r3 == 0 and _r4 == 0 and _r5 == 0
      and '钩死' not in _发[0] and '存底迟' in _发[0]
      and 'return max(活守之巡(仓, 今, 应d=应), 决rc)' in _段云 and _段云.index('私停(仓, 今)') < _段云.index('return max(活守之巡(仓, 今, 应d=应), 决rc)'))
    # 〔1119 执行之审·复核〕暂停中⛔唤：巡判 暂停→止→rc 0→云巡走 活守之巡；巡应停於末回之态，存底迟逾二十四时即恒红——每日一唤一红一邮（总章 §三.5「三令俱停」）
    import 暂停令 as _停令2
    _原在2 = _停令2.在
    try:
        with contextlib.redirect_stdout(io.StringIO()) as _o停:
            _r停 = 活守之巡('o/r', _今, 应d=_迟, 号=1, 键们=set(), 发=_发.append, 停=True)
        _停令2.在 = lambda root=None: (False, '无暂停令（试）')
        _停a, _停b = _暂停中({'章': '暂停', '时': _今}), _暂停中({'章': 474, '时': _今})
        _停令2.在 = lambda root=None: (True, '暂停令在（试）')
        _停c = _暂停中({'章': 474, '时': _今})
        _停令2.在 = lambda root=None: (_ for _ in ()).throw(RuntimeError('读不出'))
        _停d = _暂停中({'章': 474})
    finally:
        _停令2.在 = _原在2
    T('活守④之四〔复核〕暂停中（心跳之章「暂停」、或暂停令在）→ 只印「暂停中⛔唤（活守）」、rc 0、⛔留言；未停照唤；暂停令读不出 → 作未停；云巡之调走 _暂停中()',
      _r停 == 0 and len(_发) == 1 and '暂停中⛔唤（活守）' in _o停.getvalue() and '存底迟 25 时' in _o停.getvalue()
      and _停a and not _停b and _停c and not _停d
      and '_暂停中() if 停 is None else 停' in src.split('def 活守之巡(')[1].split('\ndef ')[0])
    _体 = json.loads(巡应之体(0, _今, {'钩': '死', '存底刻': 5, '钩死起': 7, '无钩': 9, '偏': 1}))
    _段沙 = _段主.split("if '--巡' in a:")[1].split('sys.exit(_rc)')[0]
    T('活守⑤〔治1·e〕巡应之体添「钩」「存底刻」「钩死起」（余态⛔出）；活守败即⛔添（云巡作旧论）；沙盒之巡：活守包於 redirect_stdout(sys.stderr)、'
      '在 巡(查印=True) 之前（stdout 仍只「止」或旧印）、落巡应带其态',
      (_体['钩'], _体['存底刻'], _体['钩死起']) == ('死', 5, 7) and '无钩' not in _体 and '偏' not in _体
      and '钩' not in json.loads(巡应之体(0, _今)) and _体['rc'] == 0
      and '_态 = 活守(守先在=_守先在)' in _段沙 and 'redirect_stdout(sys.stderr):\n                _态 = 活守(' in _段沙
      and _段沙.find('_态 = 活守(') < _段沙.find('_rc = 巡(查印=True)') and '落巡应(_rc, 态=_态, 前=_前巡应)' in _段沙)
    _串 = 开头之串()
    T('活守⑥〔治1·c〕补印之串＝ .claude/settings.json 之 SessionStart（startup|compact|clear）原令（总章至「## 一、」、法用之守 --报 --首 前六行、费哨 --章）——⛔另拟',
      "awk '/^## 一、/{exit}1' 00_总章.md" in _串 and '法用之守.py --报 --首' in _串 and '费哨.py --章' in _串
      and "'CLAUDE_PROJECT_DIR=根'" not in src and 'CLAUDE_PROJECT_DIR=根' in src.split('def 补印(')[1].split('\ndef ')[0])
    # 〔W908 环12〕自决之机·GitHub 之半：①--巡 首行印第一律之首句（唯一之源）；②代扫之果入巡应；③云巡读之、自决红未清即唤（同局一唤）。
    #   回灌：首行另写其文或移於活守之後、句断於括引之内、巡应缺「自决」或漏余态、连红之巡易其首（同局二唤）、红 0 亦取哨 PR、暂停中唤、云巡⛔调或调於私停之前 → 各即红。
    _句 = 第一律之句()
    _总文 = open(os.path.join(ROOT, 总章档), encoding='utf-8').read()
    with tempfile.TemporaryDirectory() as _dz:
        open(os.path.join(_dz, 总章档), 'w', encoding='utf-8').write('# 总章\n\n**★第一律·自决（甲令「一。二：三」·坑55）：我自决（问之⛔。）；⛔问作者。余句。**\n')
        _伪句 = 第一律之句(_dz)
        _dz2 = os.path.join(_dz, '空')
        os.makedirs(_dz2)
        _缺句, _缺印 = 第一律之句(_dz2), 第一律之印(_dz2)
        open(os.path.join(_dz2, 总章档), 'w', encoding='utf-8').write('# 总章\n\n**★唯一之的**：x。\n')
        _无律 = 第一律之句(_dz2)
    T('自决①〔W908 环12①〕第一律之句＝00_总章.md「第一律·自决」之首句照录（括、引之内之「：」「。」⛔断）；档缺、无其律即空而印「⚠ 第一律读不得」；'
      '沙盒之 --巡 首行印之（stderr·在存底守与活守之前）；本器⛔另写其文',
      bool(_句) and _句 in _总文 and _句.startswith('我是最高责任人') and _句.endswith('。') and '至高无上之权' in _句
      and 第一律之印() == '第一律·自决（00_总章.md）：' + _句 and _伪句 == '我自决（问之⛔。）；⛔问作者。'
      and _缺句 == '' and _缺印.startswith('⚠ 第一律读不得') and _无律 == ''
      and 'sys.stderr.write(第一律之印()' in _段沙 and -1 < _段沙.find('sys.stderr.write(第一律之印()') < _段沙.find('_守先在 = True') < _段沙.find('_态 = 活守(')
      and '至高无上之权' not in src and '第一律之印(根)' in src.split('def 自决之巡(')[1].split('\ndef ')[0])
    _体9 = json.loads(巡应之体(0, _今, dict(_s1)))
    T('自决②〔W908 环12②〕代扫之果入巡应：钩死扫得二红 → 自决｛红 2、片含「要你点头」、首＝11:31 之刻、扫至＝本巡｝；连红之巡承旧首（同局）；'
      '钩复活 → 红 0、首空、由「钩活」；疑 → 红 0、由「钩疑」；巡应之体并「自决」（余态仍⛔出）；自决之果：红 0 首空、末三片各≤80 字、转录之时坏即取今',
      _s1['自决']['红'] == 2 and any('要你点头' in x for x in _s1['自决']['片']) and _s1['自决']['首'] == _录时('2026-11-16T11:31:32.984Z')
      and _s1['自决']['扫至'] == _t and _s1['自决首'] == _s1['自决']['首']
      and _s2['自决']['红'] == 1 and _s2['自决']['首'] == _s1['自决']['首'] and '要不要我' in _s2['自决']['片'][0]
      and _s3['自决']['红'] == 0 and _s3['自决']['首'] is None and '钩活' in _s3['自决']['由'] and _s3['自决首'] is None
      and _s4['自决']['红'] == 0 and '钩疑' in _s4['自决']['由']
      and _体9.get('自决') == _s1['自决'] and not any(k in _体9 for k in ('偏', '录', '自决首', '无钩', '扫自'))
      and 自决之果([], 9) == {'扫至': 9, '红': 0, '片': [], '首': None} and 自决之果([(0, 'x')], 9)['首'] == 9
      and 自决之果([(5, 'a' * 100)], 9)['片'] == ['a' * 80] and 自决之果([(k, str(k)) for k in range(1, 6)], 9, 7) == {'扫至': 9, '红': 5, '片': ['3', '4', '5'], '首': 7})
    _应9 = {'时': _今, 'rc': 0, '自决': {'扫至': _今, '红': 2, '片': ['这一步要你点头', '跟我说一声'], '首': _今 - 600}}
    _键9 = 自决之键(_应9)[0]
    _发9, _调9 = [], []
    _原接9 = globals()['_接口']
    try:
        globals()['_接口'] = lambda 法, 径, 体=None: (_调9.append((法, 径)) or ([{'user': {'type': 'Bot'}, 'body': 警记 % _键9}] if '/comments' in 径 else [{'number': 1}]))
        with contextlib.redirect_stdout(io.StringIO()) as _o9:
            _q1 = 自决之巡('o/r', _今, 应d=_应9, 号=1, 键们=set(), 发=_发9.append, 停=False)
            _q2 = 自决之巡('o/r', _今, 应d=_应9, 号=1, 键们={_键9}, 发=_发9.append, 停=False)
            _q3 = 自决之巡('o/r', _今, 应d=dict(_应9, 自决=dict(_应9['自决'], 红=0)), 发=_发9.append, 停=False)
            _q4 = 自决之巡('o/r', _今, 应d={'时': _今, 'rc': 0}, 发=_发9.append, 停=False)
            _调前 = len(_调9)
            _q5 = 自决之巡('o/r', _今, 应d=_应9, 号=1, 键们=set(), 发=_发9.append, 停=True)
            _q6 = 自决之巡('o/r', _今, 应d=_应9, 发=_发9.append, 停=False)      # 键们 None → _诸键（哨 PR 之言）见同键 → ⛔再唤
    finally:
        globals()['_接口'] = _原接9
    _o9 = _o9.getvalue()
    T('自决③〔W908 环12③〕云巡之自决之巡：自决红未清 → 唤（键「自决·<首>」、言附片与第一律之句）而红；同局已唤（键们、或哨 PR 之言）→ ⛔唤⛔红；'
      '红 0、旧巡应 → 0 且⛔取哨 PR（零 API）；暂停中 → 只印、0；云巡於私停之後、rc 之分支之前调之（读巡应一回），诸 rc 之返并其 rc',
      _键9 == '自决·' + time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime(_今 - 600)) and _q1 == 1 and len(_发9) == 1
      and all(k in _发9[0] for k in ('【巡警·自决】', '「这一步要你点头」', _句, 警记 % _键9, '接棒守.py --巡'))
      and _q2 == 0 and _q3 == 0 and _q4 == 0 and _调前 == 0 and _q5 == 0 and '暂停中⛔唤（自决）' in _o9 and _q6 == 0 and len(_发9) == 1
      and any('/comments' in p and 'since=' in p for _, p in _调9)
      and 自决之键({'时': 1, '自决': '坏'}) == ('', None) and 自决之键({'时': _今, '自决': {'红': 1, '首': None}})[0] == '自决·' + time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime(_今))
      and "决rc = 0 if 试 else 自决之巡(仓, 今, 应d=应)" in _段云
      and _段云.index('私停(仓, 今)') < _段云.index('自决之巡(仓, 今, 应d=应)') < _段云.index('if rc == 0 and not 试')
      and 'return max(1 if (红 and not 试) else 0, 决rc)' in _段云 and '_暂停中() if 停 is None else 停' in src.split('def 自决之巡(')[1].split('\ndef ')[0])
    # 〔1119 执行之审·复核〕治1(d) 之日行⛔与本坐自开之件（W9xx）之主环切片重计（复盘.py:407-409 件有「起」即记「主环:<起>」）——
    #   11-19 实踩：W905（起 17:56Z）、W906（起 18:51Z）俱本坐自开、「进行」，其复盘将记本坐之切；11-20 首巡记 11-19 全日行即两回计。
    #   甲：复盘先（切 [17:56, 23:30) 已在费账）→ 日行只余其外；乙：日行先（件进行·切未记）→ 日行让 [17:56, 24:00)，其後复盘记
    #   [17:56, 11-20 02:00)、次日之日行减其交；写书之坐之件（W147）之切⛔让。费哨（算）之合 ＝ 转录之合（每回只计一回）。
    import 费审 as _费审, 费哨 as _费哨
    _真件 = {x.get('id'): x for x in (json.load(open(os.path.join(ROOT, '设定', '工作流账.json'), encoding='utf-8')).get('件') or [])}
    _日19 = [k for k, x in _真件.items() if 本坐件式.fullmatch(str(k)) and str(x.get('起') or '').startswith('2026-11-19')]
    with tempfile.TemporaryDirectory() as _dd:
        _录7 = os.path.join(_dd, '主.jsonl')
        _u7 = {'input_tokens': 1000, 'cache_creation_input_tokens': 10000, 'cache_read_input_tokens': 1000000, 'output_tokens': 2000,
               'cache_creation': {'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 10000}}
        with open(_录7, 'w', encoding='utf-8') as _f7:
            for _k7, _ts7 in enumerate(('2026-11-19T10:00:00.000Z', '2026-11-19T18:00:00.000Z', '2026-11-19T23:00:00.000Z',
                                         '2026-11-20T01:00:00.000Z', '2026-11-20T03:00:00.000Z')):
                _f7.write(json.dumps({'type': 'assistant', 'timestamp': _ts7, 'message': {'id': 'm%d' % _k7, 'model': 'claude-opus-5-5', 'usage': _u7,
                                      'content': [{'type': 'text', 'text': 'x'}]}}) + '\n')
        _全7 = _费审.主环('2026-11-19T00:00:00Z', f=_录7, 至='2026-11-21T00:00:00Z')
        _一7 = _全7['金'] / 5

        def _局(名):
            t7 = os.path.join(_dd, 名)
            os.makedirs(os.path.join(t7, '设定'))
            json.dump({'件': [{'id': 'W905', '名': '执行之审', '状态': '进行', '起': '2026-11-19T17:56Z'},
                             {'id': 'W147', '名': '第473章', '状态': '进行', '起': '2026-11-19T05:00Z'}]},
                      open(os.path.join(t7, '设定', '工作流账.json'), 'w', encoding='utf-8'), ensure_ascii=False)
            with contextlib.redirect_stdout(io.StringIO()):    # 写书之坐之切（他坐之转录·此处以零费之行代之）：⛔让
                _费审.记('主环:2026-11-19T05:00', 'W147·第473章', [dict(_费审.主环('2030-01-01T00:00:00Z', f=_录7) or {}, 回=0, 金=0.0)], None, t7, 时='2026-11-19T05:00Z')
            return t7

        def _复盘(t7, 至):
            with contextlib.redirect_stdout(io.StringIO()):
                _费审.记('主环:2026-11-19T17:56', 'W905·执行之审', [_费审.主环('2026-11-19T17:56', f=_录7, 至=至)], None, t7, 时='2026-11-19T17:56Z')

        def _行(t7):
            return json.load(open(os.path.join(t7, '设定', '费账.json'), encoding='utf-8'))['行']

        def _计(t7):
            w, n, _ = _费哨.算(_行(t7), {}, 99)
            return w + n
        _甲, _乙 = _局('甲'), _局('乙')
        _e乙 = io.StringIO()
        _原err = sys.stderr
        try:
            sys.stderr = io.StringIO()
            _复盘(_甲, '2026-11-19T23:30')
            _rc甲 = 记本坐之费('2026-11-20', root=_甲, f=_录7)
            sys.stderr = _e乙
            记本坐之费('2026-11-20', root=_乙, f=_录7)
            _复盘(_乙, '2026-11-20T02:00')
            记本坐之费('2026-11-21', root=_乙, f=_录7)
        finally:
            sys.stderr = _原err
        _日甲 = next((x for x in _行(_甲) if x['键'] == '主环:2026-11-19T00:00:00Z'), {})
        _日乙19 = next((x for x in _行(_乙) if x['键'] == '主环:2026-11-19T00:00:00Z'), {})
        _日乙20 = next((x for x in _行(_乙) if x['键'] == '主环:2026-11-20T00:00:00Z'), {})
        _旧日 = _费审.主环('2026-11-19T00:00:00Z', f=_录7, 至='2026-11-20T00:00:00Z')
        _计甲, _计乙 = _计(_甲), _计(_乙)
    T('活守⑦〔复核·治1(d)〕日行⛔与本坐自开之件之主环切片重计：甲（复盘先·切 [17:56, 23:30)）→ 11-19 日行只余 10:00 一回；'
      '乙（日行先·W905 进行）→ 11-19 日行让 [17:56, 24:00)、复盘记 [17:56, 11-20 02:00)、11-20 日行减其交只余 03:00 一回；'
      '费哨之合＝转录之合（每回只计一回·旧：日行全日＋切 → 两回计）；写书之坐之件（W147）之切⛔让；真账：11-19 本坐自开之件 %s' % '、'.join(sorted(_日19)),
      _rc甲 == 0 and _日甲.get('来回') == 1 and abs(_日甲.get('美元', 0) - _一7) < 1e-3
      and abs(_计甲 - 3 * _一7) < 1e-3 and _旧日['回'] == 3 and _一7 > 0.1
      and _日乙19.get('来回') == 1 and _日乙20.get('来回') == 1 and abs(_计乙 - _全7['金']) < 1e-3
      and 'W905 $' in _e乙.getvalue() and 'W147' not in _e乙.getvalue()
      and {'W905', 'W906'} <= set(_日19) and not 本坐件式.fullmatch('W147') and not 本坐件式.fullmatch('W90'))
    #   并行之件（W905 起 17:56、W906 起 18:51 俱进行·11-19 之真形）：切片各计其段而相叠（复盘之事）——日行逐件减（⛔并集），费账之合每回一计
    _回们 = [_秒('2026-11-19T%s' % h) for h in ('08:00', '09:00', '10:00', '18:00', '23:00')]

    def _主(a, b):
        n = sum(1 for t in _回们 if _秒(a) <= t < _秒(b))
        return {k: n for k, _ in _日行之键}
    _件并 = [{'id': 'W905', '状态': '进行', '起': '2026-11-19T17:56Z'}, {'id': 'W906', '状态': '进行', '起': '2026-11-19T18:51Z'},
            {'id': 'W904', '状态': '已成', '起': '2026-11-19T07:00Z'}]
    _并 = 本坐日行('2026-11-20', _主, _件并, [])
    _并截 = 本坐日行('2026-11-20', _主, _件并 + [{'id': 'W907', '状态': '进行', '起': '2026-11-19T07:30Z'}], [])
    T('活守⑦之二 并行之件（W905、W906 俱进行·相叠）：日行逐件减 → 5−2−1＝2 回，与二件将记之切（2＋1）合 5＝全日（每回一计）；'
      '已了而无切片之件（W904）⛔让；让逾日行 → 截零（截＝True·印之）',
      _并[3]['回'] == 2 and _并[4] == [('W905', 2.0), ('W906', 1.0)] and _并[5] is False
      and _并截[3] is None and _并截[5] is True)
    # ── W908 环2（接棒守之判六改·每改一局钉之）──
    #   (a) 活守之键态变方唤（旧键带日：钩死起 11-19 18:27:54 UTC → 11-20 18:28 起每日一空唤一红）
    #   〔W910〕钩死⛔作红与唤之由（钩复载已弃·以巡代钩）：键唯存底迟之起定——钩死逾二十四时、复活再死俱⛔唤
    _今8 = 10 ** 9
    _应8 = lambda 时=_今8, **k: dict({'时': 时, 'rc': 0, '钩': '死', '存底刻': 时 - 300, '钩死起': _今8 - 25 * 3600}, **k)    # 存底照常（末存恒五分前）
    _迟8 = _今8 + 86400 - 25 * 3600       # 存底迟起（次日已逾二十四时）
    _发8, _已8 = [], set()

    def _发记8(b):
        _发8.append(b)
        _已8.add(re.search(r'<!-- 巡警:(.+?) -->', b).group(1))
    with contextlib.redirect_stdout(io.StringIO()):
        _q1 = 活守之巡('o/r', _今8, 应d=_应8(), 号=1, 键们=_已8, 发=_发记8, 停=False)                                   # 钩死逾二十四时·存底照常：⛔唤
        _q2 = 活守之巡('o/r', _今8 + 86400, 应d=_应8(时=_今8 + 86400), 号=1, 键们=_已8, 发=_发记8, 停=False)            # 次日钩死不复：⛔唤
        _q3 = 活守之巡('o/r', _今8 + 86400, 应d=_应8(时=_今8 + 86400, 存底刻=_迟8), 号=1, 键们=_已8, 发=_发记8, 停=False)   # 存底迟起：唤
        _q4 = 活守之巡('o/r', _今8 + 2 * 86400, 应d=_应8(时=_今8 + 2 * 86400, 存底刻=_迟8, 钩死起=_今8 + 86400 - 3600), 号=1,
                      键们=_已8, 发=_发记8, 停=False)                                                                     # 存底迟不变而复活再死（钩死起新）：⛔唤
        _q5 = 活守之巡('o/r', _今8 + 3 * 86400, 应d=_应8(时=_今8 + 3 * 86400, 存底刻=_今8 + 3 * 86400 - 25 * 3600), 号=1,
                      键们=_已8, 发=_发记8, 停=False)                                                                     # 复存再迟（存底迟起新）：唤
        _q6 = 活守之巡('o/r', _今8 + 3 * 86400, 应d=_应8(时=_今8 + 3 * 86400, 存底刻=_今8 + 3 * 86400 - 25 * 3600, 钩='活', 钩死起=None), 号=1,
                      键们=_已8, 发=_发记8, 停=False)                                                                     # 再迟之态不变（钩复活）：⛔唤
    _ka, _za = 活守之键(_应8(时=_今8 + 86400, 存底刻=_迟8), _今8 + 86400)
    _段守 = src.split('def 活守之巡(')[1].split('\ndef ')[0]
    T('W908·环2(a)〔W910〕活守态变方唤：钩死逾二十四时而存底照常 → ⛔唤⛔红（首日、次日俱）；存底迟起 → 唤而红；存底迟不变而复活再死 → ⛔唤（键⛔易）；'
      '复存再迟 → 易键而唤；钩复活而再迟之态不变 → ⛔唤；键「活守·<存底迟起>」唯以存底迟之起定、旧言自其可落之时查（⛔只查今日）',
      (_q1, _q2, _q3, _q4, _q5, _q6) == (0, 0, 1, 0, 1, 0) and len(_发8) == 2 and len(_已8) == 2
      and _ka == '活守·%s' % time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime(_迟8)) and _za == _迟8 + 24 * 3600 - 600
      and 活守之键(_应8(), _今8) == ('', 0) and 活守之键(_应8(钩死起=_今8 - 3600), _今8) == ('', 0) and 活守之键({'时': _今8, 'rc': 0}, _今8) == ('', 0)
      and 活守之键(_应8(时=_今8 + 86400, 存底刻=_迟8, 钩死起=_今8 + 86400 - 3600), _今8 + 86400)[0] == _ka
      and 活守之键(_应8(时=_今8 + 86400, 存底刻=_迟8, 钩='活', 钩死起=None), _今8 + 86400)[0] == _ka
      and not any('钩死' in b for b in _发8)
      and '_诸键(仓, 号, 自)' in _段守 and "'%Y-%m-%d', time.gmtime(今)" not in _段守)
    #   (b) 合入之卡先读坏报：有报印果与因（merge 印冲突之档）、界内⛔印；cancelled 而无报即「被顶」、⛔候三十分；读不出退回三十分之界
    _s8 = 'a' * 40
    _m报 = {'ref': '章-473', 'sha': _s8, '果': '败', '因': 'merge', '红': ['⛔备候不成（因 merge）——未入片闸；看 run_url'],
           'main_after': 'b' * 40, 'run_url': 'https://x/actions/runs/9', '冲突': ['设定/费账.json', '设定/方法账.md']}

    def _卡8(分, **k):
        return 合入之卡({'章': 474, '时': 1}, 今=100000, 标=lambda n: _s8, 含=lambda n: False, 时=lambda s: 100000 - 分 * 60,
                     **dict(_无8, **k))
    _c1 = _卡8(37, 坏=lambda n: ('章-473', _m报))
    _c3 = _卡8(3, 跑态=lambda n, s: '顶')
    T('W908·环2(b) 合入之卡：坏报（败·merge）逾三十分 → 印果、因、冲突之档、run_url（⛔额度之断）；界内 → ⛔印（封版之坐 --候主 rc 3 先治）；'
      '无报或「败·重派」而云端末跑 cancelled → 即判被顶（3 分·⛔候三十分）；有定报（成）、旧标之报而跑在飞／排候／读不出 → 界内⛔印；逾界 → 印其由',
      '败（因 merge）' in _c1 and '设定/费账.json、设定/方法账.md' in _c1 and 'https://x/actions/runs/9' in _c1 and '额度' not in _c1
      and '合入之卡：第473章已封（章-473 %s）37 分未入主枝' % _s8[:12] in _c1
      and _卡8(10, 坏=lambda n: ('章-473', _m报)) == '' and _卡8(10, 坏=lambda n: 1 / 0, 报=lambda n: _m报, 跑态=lambda n, s: '顶') == ''   # 界内⛔取坏报之源；坏报⛔作被顶
      and '冲突之档未入报' in _卡8(31, 坏=lambda n: ('章-473', dict(_m报, 冲突=None)))
      and '推闸之红逐条治' in _卡8(31, 坏=lambda n: ('章-473', dict(_m报, 果='红', 因='')))
      and '被顶' in _c3 and '⛔候 30 分' in _c3 and '3 分未入主枝' in _c3
      and '被顶' in _卡8(3, 报=lambda n: dict(_m报, 因='重派', 红=[]), 跑态=lambda n, s: '顶')
      and '被顶' in _卡8(3, 报=lambda n: dict(_m报, sha='c' * 40), 跑态=lambda n, s: '顶')                    # 旧标之报⛔认
      and _卡8(3, 报=lambda n: dict(_m报, 果='成', 因=''), 跑态=lambda n, s: 1 / 0) == ''                     # 有定报⛔问跑态
      and _卡8(3, 跑态=lambda n, s: '飞') == '' and _卡8(3, 跑态=lambda n, s: '候') == '' and _卡8(3) == ''
      and _卡8(3, 跑态=lambda n, s: 1 / 0) == ''                                                              # 跑态崩 → 退回三十分之界
      and '在飞' in _卡8(31, 跑态=lambda n, s: '飞') and '他跑排候' in _卡8(31, 跑态=lambda n, s: '候')
      and '其治枝在飞' in _卡8(31, 报=lambda n: dict(_m报, 果='红', 因=''))
      and '请换号' not in src and '换号或等下月' not in src and '多半是本月额度' not in src and '多半 Actions 额度用光' not in src
      and '坏报之源(k, 读=' in src.split('def 合入之卡(')[1].split('\ndef ')[0])
    _r8 = lambda s, c, t, i, sha=_s8: {'head_sha': sha, 'status': s, 'conclusion': c, 'created_at': t, 'id': i}
    _取8 = lambda 章诸, 队: (lambda 径: {'workflow_runs': 章诸 if '&branch=' in 径 else 队})
    _顶8 = [_r8('completed', 'cancelled', '2026-11-19T10:05:00Z', 2), _r8('completed', 'failure', '2026-11-19T10:00:00Z', 1)]
    _旧GA = os.environ.get('GITHUB_ACTIONS')
    try:
        os.environ['GITHUB_ACTIONS'] = 'false'
        _沙8 = 闸跑之态(473, _s8, 仓='o/r')
    finally:
        if _旧GA is None:
            os.environ.pop('GITHUB_ACTIONS', None)
        else:
            os.environ['GITHUB_ACTIONS'] = _旧GA
    T('W908·环2(b) 闸跑之态：末跑 cancelled 且无他跑排候 → 顶；他跑排候 → 候（再闸即顶之）；有未毕 → 飞；末跑非 cancelled → 毕；他笔之跑、无跑、API 崩、沙盒（非 GitHub 之机）→ None',
      闸跑之态(473, _s8, 仓='o/r', 取=_取8(_顶8, [_r8('in_progress', None, 'x', 5, sha='d' * 40)])) == '顶'
      and 闸跑之态(473, _s8, 仓='o/r', 取=_取8(_顶8, [_r8('queued', None, 'x', 5, sha='d' * 40)])) == '候'
      and 闸跑之态(473, _s8, 仓='o/r', 取=_取8(_顶8 + [_r8('in_progress', None, '2026-11-19T10:06:00Z', 3)], [])) == '飞'
      and 闸跑之态(473, _s8, 仓='o/r', 取=_取8([_r8('completed', 'success', '2026-11-19T10:00:00Z', 1)], [])) == '毕'
      and 闸跑之态(473, _s8, 仓='o/r', 取=_取8([_r8('completed', 'cancelled', 'x', 1, sha='e' * 40)], [])) is None
      and 闸跑之态(473, _s8, 仓='o/r', 取=_取8([], [])) is None and 闸跑之态(473, _s8, 仓='o/r', 取=lambda 径: 1 / 0) is None
      and _沙8 is None)
    #   (c) 再闸：因 merge 而报之主前＝今主 → ⛔派、唤并；今主已进 → 许一派；余照旧派
    _派8 = []
    _z1 = 再闸('o/r', '473', 报=_m报, 标=_s8, 今主='b' * 40, 派=_派8.append)
    _n1 = len(_派8)
    _z2 = 再闸('o/r', '473', 报=_m报, 标=_s8, 今主='c' * 40, 派=_派8.append)
    _z3 = 再闸('o/r', '473', 报=dict(_m报, 果='红', 因=''), 标=_s8, 今主='b' * 40, 派=_派8.append)
    _z4 = 再闸('o/r', '473', 报=dict(_m报, sha='c' * 40), 标=_s8, 今主='b' * 40, 派=_派8.append)
    _z5 = 再闸('o/r', '473', 报=dict(_m报, main_after=''), 标=_s8, 今主='b' * 40, 派=_派8.append)
    _z6 = 再闸('o/r', '473', 报=_m报, 标=_s8, 今主='c' * 40, 派=lambda 体: 1 / 0)
    T('W908·环2(c) 再闸：merge 之败而主前＝今主 → ⛔派、印冲突之档、唤并（推.py 交）；今主已进 → 许一派；红、旧标之报、主前读不出 → 照旧派；派崩 → 印手派',
      _n1 == 0 and '⛔派' in _z1 and '设定/费账.json' in _z1 and '推.py' in _z1 and 'bbbbbbbbbbbb' in _z1
      and '许一派' in _z2 and '已自 workflow_dispatch' in _z2 and '许一派' not in _z3 and '已自' in _z3 and '已自' in _z4 and '已自' in _z5
      and len(_派8) == 4 and all(x == {'ref': '章-473', 'inputs': {'tries': '0'}} for x in _派8) and '再闸不成' in _z6)
    #   (d) 应判以同局首唤之时量（旧取末唤：唤隔二十＜应候三十，末唤恒未逾——闭环实死）；限同局一红；他局之唤⛔计
    _K8 = 'rc4·473'
    _唤8 = [(_今8, _K8), (_今8 + 唤之隔分 * 60, _K8)]
    T('W908·环2(d) 应判：同局唤於 0、20 分而未应 → 40 分之唤即红（旧以末唤 20 分＜30 恒⛔红）；红过之局再唤 → ⛔再红；应於首唤後 → 空；'
      '他局之唤⛔计；键缺即诸真唤（旧调之形）；云巡以本局之键调之',
      (_今8 + 40 * 60) - max(t for t, _ in _唤8) < 应之候分 * 60                       # 旧判之死：末唤恒未逾应候
      and '未应' in 应判(_唤8, 0, _今8 + 40 * 60, _K8) and '同局首唤' in 应判(_唤8, 0, _今8 + 40 * 60, _K8)
      and 应判(_唤8 + [(_今8 + 40 * 60, _K8)], 0, _今8 + 60 * 60, _K8) == ''
      and 应判(_唤8, _今8 + 60, _今8 + 40 * 60, _K8) == ''
      and 应判([(_今8 - 3600, 'rc2·470·1'), (_今8 + 20 * 60, _K8)], 0, _今8 + 40 * 60, _K8) == ''
      and '未应' in 应判(_唤8, 0, _今8 + 40 * 60)
      and "应判(旧, (_读枝档(巡应枝, 巡应档) or {}).get('时'), 今, 键)" in _段云)
    #   (e) rc4 之题作「合入之卡 N 分·章-N」（旧用心跳之龄：7019835106「停书 0 分」）
    T('W908·环2(e) rc4 之题：「合入之卡 37 分·章-473」（坏报）、「合入之卡 3 分·章-473」（被顶）；读不出即「合入之卡」；云巡 rc 4 取之；键仍以章（rc4·473）',
      卡之题(_c1) == '合入之卡 37 分·章-473' and 卡之题(_c3) == '合入之卡 3 分·章-473' and 卡之题('乱') == '合入之卡'
      and 卡之题(合入之卡({'章': 474, '时': 1}, 今=100000, 标=lambda n: _s8, 含=lambda n: False, 时=lambda s: 0, **_无8)) == '合入之卡 久·章-473'
      and '卡之题(印) if rc == 4' in _段云 and 云巡判(4, {'章': 474, '时': _今8}, _今8, [], _c3)[1] == 'rc4·473')
    #   (f)「GitHub 邮作者」正为「哨 PR 之言即达作者」（哨 PR 之主即作者·裁十四）
    T('W908·环2(f) 红之语：哨 PR 之言即达作者（云巡之唤、活守之唤）；「GitHub 邮作者」⛔在',
      'GitHub 邮作者' not in src and '哨 PR 之言即达作者' in _段云 and all('哨 PR 之言即达作者' in b for b in _发8))
    # ── W908 环2 复核（未过之条·每条一局钉之）──
    #   复核①（反例一）：章-473 之候跑被同坐後推之治（含此章）所顶、治之跑 in_progress → 闸跑之态「顶」——旧即出卡（4 分·红）、再闸一已在之章；今先问 治之在飞
    _段卡 = src.split('def 合入之卡(')[1].split('\ndef ')[0]
    _态反8 = 闸跑之态(473, _s8, 仓='o/r', 取=_取8(_顶8, [_r8('in_progress', None, '2026-11-19T10:06:00Z', 7, sha='d' * 40)]))
    _飞8 = lambda 标: [('治-dddddddddddd', 'd' * 40)] if 标 == _s8 else []
    _x1 = _卡8(4, 跑态=lambda n, s: _态反8, 飞=_飞8); _t1 = _卡之态
    _x2 = _卡8(31, 跑态=lambda n, s: _态反8, 飞=_飞8); _t2 = _卡之态
    _x3 = _卡8(4, 跑态=lambda n, s: '顶', 飞=_飞8, 治报=lambda b: {'sha': 'd' * 40, '果': '红', '因': ''}); _t3 = _卡之态   # 治已红：⛔作在飞 → 被顶
    _x4 = _卡8(4, 跑态=lambda n, s: '顶', 飞=_飞8, 治报=lambda b: {'sha': 'e' * 40, '果': '红', '因': ''})            # 治之旧标之红：仍在飞
    _x5 = _卡8(4, 跑态=lambda n, s: '顶', 飞=_飞8, 治报=lambda b: {'sha': 'd' * 40, '果': '败', '因': '重派'})       # 治「败·重派」：在飞
    _x6 = _卡8(4, 跑态=lambda n, s: '顶', 飞=lambda 标: 1 / 0); _t6 = _卡之态                                          # 治读不出 → 退回三十分之界
    _x7 = _卡8(4, 跑态=lambda n, s: '候', 飞=lambda 标: 1 / 0)                                                         # 非顶⛔问治（免 ls-remote）
    _x8 = _卡8(31, 报=lambda n: dict(_m报, 果='红', 因='')); _t8 = _卡之态                                              # 章红而坏报之源⛔返（治在飞）
    _x9 = _卡8(37, 坏=lambda n: ('章-473', _m报)); _t9 = _卡之态
    _x10 = _卡8(3, 跑态=lambda n, s: '顶'); _t10 = _卡之态
    T('W908·复核① 合入之卡判顶先问 治之在飞（沿用现函）：反例一（治跑 in_progress → 闸跑之态「顶」）→ 界内⛔卡（态「治」·云巡 rc 0 ⛔唤⛔红⛔派）、'
      '逾界印「含此章之治」且再闸⛔派；治已坏报 → 仍判被顶；治之旧标之报、败·重派 → 在飞；治读不出 → 退回三十分之界；非顶⛔问治；'
      '章红而治在飞 → 态「治」；坏报 → 「坏」、被顶 → 「顶」（_卡之态 每调先清）',
      _态反8 == '顶' and _x1 == '' and _t1 == '治' and '含此章之治（治-dddddddddddd）' in _x2 and '再闸⛔派' in _x2 and _t2 == '治'
      and '被顶' in _x3 and _t3 == '顶' and _x4 == '' and _x5 == '' and _x6 == '' and _t6 == '' and _x7 == ''
      and '其治枝在飞未毕' in _x8 and '再闸⛔派' in _x8 and _t8 == '治' and _x9 and _t9 == '坏' and '被顶' in _x10 and _t10 == '顶'
      and (_卡8(3), _卡之态)[1] == '' and '治之在飞)(sha)' in _段卡 and "_卡之态 = ''" in _段卡)
    #   复核②（反例二）：卡之态 ∈ 候／飞／治 → 再闸⛔派、⛔记；同局一派之记＝唤之体之 再闸之印（_旧言 认之·旧制之言亦带）；首唤⛔派者态转「顶」之唤再派
    _派9 = []
    _y9 = {k: 再闸('o/r', '473', 报={}, 标=_s8, 今主='b' * 40, 派=_派9.append, 态=k) for k in _候之态}
    _n9 = len(_派9)
    _y顶 = 再闸('o/r', '473', 报={}, 标=_s8, 今主='b' * 40, 派=_派9.append, 态='顶')
    _y空 = 再闸('o/r', '473', 报={}, 标=_s8, 今主='b' * 40, 派=_派9.append, 态='')
    _言9 = [{'body': '【巡警】合入之卡 32 分·章-473\n\n' + _y9['候'] + '\n\n' + 警记 % 'rc4·473', 'user': {'type': 'Bot'}, 'created_at': '2026-11-19T10:32:00Z'},
           {'body': '【巡警】合入之卡 3 分·章-474\n\n' + _y顶 + '\n\n' + 警记 % 'rc4·474', 'user': {'type': 'Bot'}, 'created_at': '2026-11-19T10:37:00Z'},
           {'body': '· 已自 workflow_dispatch autopush.yml（ref 章-470）——旧制之语\n' + 警记 % 'rc4·470', 'user': {'type': 'Bot'}, 'created_at': '2026-11-19T10:38:00Z'},
           {'body': _y顶 + 警记 % 'rc4·475', 'user': {'type': 'User'}, 'created_at': '2026-11-19T10:39:00Z'}]
    _旧9 = _旧言('o/r', 1, _今8, 取=lambda 径: _言9)
    import calendar
    _t32, _t37, _t38 = (calendar.timegm(time.strptime('2026-11-19T10:%s:00Z' % m, '%Y-%m-%dT%H:%M:%SZ')) for m in ('32', '37', '38'))
    _K9 = 'rc4·473'
    T('W908·复核② 再闸：卡之态 候／飞／治 → ⛔派⛔记（派即顶并发组之候跑）、顶／空 → 派而印 再闸之印；_旧言 认其印为「闸·<键>」（旧制之言亦认、他人之言⛔认）；'
      '再闸之机：首唤⛔派而未记 → 态转「顶」之唤再派（旧「首唤方调」永不再闸）、同局已派 → ⛔复派、他局之派⛔计、本跑⛔唤／非 rc 4／试 → ⛔调；应判⛔计「闸·」',
      all('再闸⛔派' in v and 再闸之印 not in v for v in _y9.values()) and _n9 == 0 and 再闸之印 in _y顶 and 再闸之印 in _y空 and len(_派9) == 2
      and _旧9 == [(_t32, 'rc4·473'), (_t37, 'rc4·474'), (_t37, '闸·rc4·474'), (_t38, 'rc4·470'), (_t38, '闸·rc4·470')]
      and 再闸之机(4, True, _K9, []) is True and 再闸之机(4, True, _K9, _旧9) is True
      and 再闸之机(4, True, _K9, _旧9 + [(_t37 + 600, '闸·' + _K9)]) is False and 再闸之机(4, True, 'rc4·474', _旧9) is False
      and not 再闸之机(4, False, _K9, []) and not 再闸之机(2, True, _K9, []) and not 再闸之机(4, True, _K9, [], 试=True)
      and 应判([(_今8 - 3600, '闸·rc4·1')], 0, _今8) == '' and '未应' in 应判([(_今8 - 3600, 'rc4·1')], 0, _今8)
      and "_巡之心, _卡之态 = None, ''" in _段云)
    #   复核③ 坏报之卡之体经 推报.报之语（同一把尺·旧自拼果／因／红／run_url 漏 逾、器红、演），merge 末添冲突之档一行
    import 推报 as _推报9
    _m报9 = dict(_m报, 器红=['器甲'], 逾=['器乙'], 演={'语': '演章过'})
    _c9 = _卡8(37, 坏=lambda n: ('章-473', _m报9))
    _L9 = _c9.split('\n')
    T('W908·复核③ 坏报之卡之体经 推报.报之语：果因、红、器红、逾（器红逾限）、演、run_url 俱出；merge 末行冲突之档（非 merge ⛔出）；首行仍头（卡之题、云巡之键可读）',
      all(x in _c9 for x in ('器红（只报不拦', '器红逾限（拦）：器乙', '演章：演章过', 'https://x/actions/runs/9', '败（因 merge）'))
      and _L9[-1] == '    · 冲突之档：设定/费账.json、设定/方法账.md' and _L9[0].startswith('⛔ 合入之卡：第473章已封（章-473 %s）37 分' % _s8[:12])
      and _L9[1:-1] == ['  ' + x for x in _推报9.报之语(_m报9)]
      and 卡之题(_c9) == '合入之卡 37 分·章-473' and 云巡判(4, {'章': 474, '时': _今8}, _今8, [], _c9)[1] == 'rc4·473'
      and '推报.报之语(r)' in _段卡 and '冲突之档' not in _卡8(37, 坏=lambda n: ('章-473', dict(_m报, 果='红', 因='', 冲突=None))))
    # 〔W911 重造 环1③〕①降之粘（巡() 之桩·落巡应 真跑而 _砌 与推俱桩）②上下文之察（假转录）③坑61 之钉——逐一退其改即红
    import 心跳 as _心11, 暂停令 as _停令11, io as _io11, contextlib as _cl11
    _今11 = int(time.time())     # 巡() 以真钟判心跳之鲜
    _原11 = {k: globals()[k] for k in ('_读枝档', '合入之卡', '巡印之由', '对拍判', '派令之治', '_砌')}
    _原远11, _原在11, _原run11 = _心11._远, _停令11.在, subprocess.run

    def _巡局11(景们, 前=None, 查印=True):
        """景：'5' 巡印停摆｜'4' 合入之卡｜'2' 停写｜'3' 停锁残而令解｜'鲜' 巡印鲜、对拍合 → [(rc, 所落巡应之降, 本巡读巡应之回)]。"""
        应, 出 = [前], []
        try:
            for 景 in 景们:
                心 = ({'章': '暂停', '时': 4102444800, '坐': '暂停令'} if 景 == '3' else
                      {'章': 480, '时': _今11 - (_心11.限 + 600 if 景 == '2' else 60), '坐': 'A'})
                读, 体们 = [], []
                _心11._远 = lambda 心=心: (True, 心)
                _停令11.在 = lambda root=None, 景=景: (景 != '3', '试')
                globals()['合入之卡'] = lambda d, *a, 景=景, **k: '⛔ 合入之卡（试）' if 景 == '4' else ''
                globals()['_读枝档'] = lambda 枝, 档: (读.append(枝), 应[0] if 枝 == 巡应枝 else {'时': _今11})[1]
                globals()['巡印之由'] = lambda 今=None, d=None, 心=None, 景=景: '⛔ 巡印停摆（试）' if 景 == '5' else ''
                globals()['对拍判'] = lambda *a, **k: ''
                globals()['派令之治'] = lambda n, *a, **k: None
                globals()['_砌'] = lambda 档, 体, 信: (体们.append(体), 'c' * 40)[1]
                with _cl11.redirect_stdout(_io11.StringIO()):
                    rc = 巡(查印=查印)
                subprocess.run = lambda *a, **k: subprocess.CompletedProcess(a, 0, '', '')
                try:
                    落巡应(rc, 今=_今11, 前=_前巡应)
                finally:
                    subprocess.run = _原run11
                应[0] = json.loads(体们[-1]) if 体们 else 应[0]
                出.append((rc, 应[0].get('降') if isinstance(应[0], dict) else None, 读.count(巡应枝)))
        finally:
            globals().update(_原11)
            _心11._远, _停令11.在, subprocess.run = _原远11, _原在11, _原run11
        return 出
    _局54, _局52, _局53 = _巡局11(['5', '4', '鲜', '鲜']), _巡局11(['5', '2', '鲜', '鲜']), _巡局11(['5', '3', '鲜', '鲜'])
    _局旧 = _巡局11(['鲜', '鲜'], 前={'时': 1, 'rc': 5})
    _局常 = _巡局11(['鲜', '4', '鲜'], 前={'时': 1, 'rc': 7, '降': False})
    _局云 = _巡局11(['鲜'], 前={'时': 1, 'rc': 5}, 查印=False)
    _体降 = lambda rc, 前=None: json.loads(巡应之体(rc, 1, None, 前)).get('降')
    T('W911 重造 环1①降之粘：5→4→鲜→7→鲜→0、5→2→鲜→7、5→3→鲜→7（rc 4／3／2 之巡⛔覆降之记·旧病降级永驻）；旧巡应（无「降」）rc 5→鲜→7；'
      '7 之後→鲜→0、常态之 4 ⛔误降；巡(查印=True) 每巡读巡应一回（开头·rc 4／3／2 之支亦读）、云巡（查印 False）⛔读；'
      '巡应之体：rc 5 → 真、rc 7 → 假、余承前（前降·旧巡应以 rc 5 论）%s' % [_局54, _局52, _局53, _局旧, _局常, _局云],
      [x[:2] for x in _局54] == [(5, True), (4, True), (7, False), (0, False)]
      and [x[:2] for x in _局52] == [(5, True), (2, True), (7, False), (0, False)]
      and [x[:2] for x in _局53] == [(5, True), (3, True), (7, False), (0, False)]
      and [x[:2] for x in _局旧] == [(7, False), (0, False)] and [x[:2] for x in _局常] == [(0, False), (4, False), (0, False)]
      and all(x[2] == 1 for x in _局54 + _局52 + _局53 + _局旧 + _局常) and _局云[0][2] == 0
      and _体降(5) is True and _体降(7, {'降': True}) is False and _体降(4, {'rc': 5}) is True and _体降(2, {'rc': 4, '降': True}) is True
      and _体降(0, {'rc': 0, '降': False}) is False and _体降(3) is False and _体降(6, {'rc': 6}) is False
      and 前降({'rc': 5}) and 前降({'降': True, 'rc': 4}) and not 前降(None) and not 前降({'rc': 7, '降': False}))
    _总11 = 总编辑

    def _录11(目录, 名, 末们, 前填=0, 後填=0):
        """假转录：前填（字节）之 user 行、末们 [(入三项之和, 模型)] 之 assistant 行、後填之 user 行（无 usage）。"""
        路 = os.path.join(目录, 名)
        填 = json.dumps({'type': 'user', 'message': {'role': 'user', 'content': 'x' * 4000}}) + '\n'
        with open(路, 'w', encoding='utf-8') as f:
            f.write(填 * (前填 // len(填)))
            for c, 模 in 末们:
                f.write(json.dumps({'type': 'assistant', 'message': {'model': 模, 'usage': {
                    'input_tokens': 2, 'cache_read_input_tokens': c - 1002, 'cache_creation_input_tokens': 1000, 'output_tokens': 50}}}) + '\n')
            f.write(填 * (後填 // len(填)))
        return 路
    with tempfile.TemporaryDirectory() as _d11:
        _r31 = _录11(_d11, 'a.jsonl', [(500000, 'claude-opus-5-5'), (310000, 'claude-opus-5-5')], 後填=3000)
        _r29 = _录11(_d11, 'b.jsonl', [(490000, 'claude-opus-5-5'), (290000, 'claude-opus-5-5')])
        _r未 = _录11(_d11, 'c.jsonl', [(310000, 'claude-x-9')])
        _r大 = _录11(_d11, 'd.jsonl', [(310000, 'claude-opus-5-5')], 前填=30 * 1024 * 1024, 後填=2 * 1024 * 1024)
        _言31 = 上下文之察(坐=_总11, 录=_r31)
        _t11 = time.time()
        _言大 = 上下文之察(坐='cse_' + _总11.replace('session_', ''), 录=_r大)
        _秒11 = time.time() - _t11
        _o11 = _io11.StringIO()
        with _cl11.redirect_stdout(_o11):
            print('止')
            _印rc = 上下文之印(0, 察=lambda: 上下文之察(坐=_总11, 录=_r31))
        _o29, _o2, _o坏 = _io11.StringIO(), _io11.StringIO(), _io11.StringIO()
        with _cl11.redirect_stdout(_o29):
            print('止')
            上下文之印(0, 察=lambda: 上下文之察(坐=_总11, 录=_r29))
        with _cl11.redirect_stdout(_o2):
            上下文之印(2, 察=lambda: 上下文之察(坐=_总11, 录=_r31))
        with _cl11.redirect_stdout(_o坏):
            上下文之印(0, 察=lambda: 1 / 0)
        _静 = [上下文之察(坐=_总11, 录=_r29), 上下文之察(坐=_总11, 录=os.path.join(_d11, '缺.jsonl')), 上下文之察(坐=_总11, 录=''),
              上下文之察(坐='ABC123', 录=_r31), 上下文之察(坐='', 录=_r31), 上下文之察(坐=_总11, 录=_r未),
              上下文之察(坐=_总11, 录=_r31, 目={'模型': {}})]
        _界言 = [上下文之察(坐=_总11, 录=_录11(_d11, 'e%d.jsonl' % c, [(c, 'claude-opus-5-5')])) for c in (300000, 300001)]   # 界之比「>」·同 活守(d)
        _境11 = {k: os.environ.get(k) for k in ('HOME', 'CLAUDE_CODE_REMOTE_SESSION_ID', 'CLAUDE_SESSION_ID', 'CLAUDE_CODE_SESSION_ID')}
        _uuid11 = '0f9e8d7c-6b5a-4321-9fed-cba987654321'
        os.makedirs(os.path.join(_d11, '.claude', 'projects', '-home-user'))
        _录11(os.path.join(_d11, '.claude', 'projects', '-home-user'), _uuid11 + '.jsonl', [(310000, 'claude-opus-5-5')])
        try:                         # 默之路（__main__ 所走·⛔注 坐／录）：坐取 心跳.坐()（REMOTE 之号＝总编辑）、录取 CLAUDE_CODE_SESSION_ID 之转录
            os.environ.update(HOME=_d11, CLAUDE_CODE_REMOTE_SESSION_ID='cse_' + _坐号(_总11), CLAUDE_CODE_SESSION_ID=_uuid11)
            os.environ.pop('CLAUDE_SESSION_ID', None)
            _默言 = 上下文之察()
            os.environ.pop('CLAUDE_CODE_REMOTE_SESSION_ID')      # 唯 CLAUDE_CODE_SESSION_ID（uuid·永⛔等总编辑）→ 静
            _默静 = 上下文之察()
        finally:
            for k, v in _境11.items():
                os.environ.pop(k, None) if v is None else os.environ.__setitem__(k, v)
    _段沙11 = _段主.split("if '--巡' in a:")[1].split('sys.exit(_rc)')[0]
    T('W911 重造 环1②上下文之察：末回 31 万 → 「止」之次行「⚠ 本坐上下文 31 万（逾 30 万）：每唤约 $0.19——宜作者键 /compact（压後约 $0.09）；答「止」并转此行告作者」'
      '（3 回×缓存读·价目；只认末回；界取 压之界·⛔写死；末句告本坐转之）、首行恒「止」、rc 非 0 ⛔印、察崩⛔崩；29 万、恰三十万（「>」·同 活守(d)）、转录缺、非总编辑之坐、模型不在价目 → 静；'
      '默之路（⛔注 坐／录）：REMOTE 之号＝总编辑即印、唯 CLAUDE_CODE_SESSION_ID 即静；'
      '三十兆之转录倒读其尾（_读尾·至 8MB·⛔全读）≤ 1 秒（%.3f 秒·末回後二兆⛔usage 亦得）；沙盒之 --巡 於 巡(查印=True) 之後、落巡应之前调之，GitHub 之 --巡 与云巡⛔调' % _秒11,
      _言31 == '⚠ 本坐上下文 31 万（逾 30 万）：每唤约 $0.19——宜作者键 /compact（压後约 $0.09）；答「止」并转此行告作者' and _言大 == _言31 and _秒11 <= 1.0
      and _界言[0] == '' and _界言[1].startswith('⚠ 本坐上下文 30 万（逾 30 万）') and _默言 == _言31 and _默静 == ''
      and _o11.getvalue().split('\n')[:2] == ['止', _言31] and _印rc is None and _o29.getvalue() == '止\n'
      and _o2.getvalue() == '' and _o坏.getvalue() == '' and _静 == [''] * 7
      and 'reversed(_读尾(路, n))' in src.split('def 末回之用(')[1].split('\ndef ')[0] and '.read()' not in src.split('def 末回之用(')[1].split('\ndef ')[0]
      and max(察尾们) <= 8 * 1024 * 1024
      and _段沙11.find('_rc = 巡(查印=True)') < _段沙11.find('上下文之印(_rc)') < _段沙11.find('落巡应(_rc')
      and _段沙11.find('GITHUB_ACTIONS') < _段沙11.find('上下文之印(_rc)')
      and '上下文之' not in src.split('def 云巡(')[1].split('\ndef ')[0].split('\n# ──')[0] and '上下文之' not in src.split('def 巡(查印=False):')[1].split('\ndef ')[0])

    # 〔W911 重造 环1④〕冷唤之察：假转录（回以 id 去重·流式之重行）——隔二时而首回缓存读 0 → 印；隔三十分、首回暖、暂停、非总编辑、rc 非 0、察崩 → 静
    def _录14(目录, 名, 回们):
        """回们：[(id, 距今秒〔负〕, 读, 写〔, 入〕)] 依时序；每回写两行（流式）。"""
        from datetime import datetime as _dt14, timezone as _tz14
        路 = os.path.join(目录, 名)
        with open(路, 'w', encoding='utf-8') as f:
            for i, 秒, 读, 写, *入 in 回们:
                for _ in range(2):
                    f.write(json.dumps({'type': 'assistant', 'timestamp': _dt14.fromtimestamp(time.time() + 秒, _tz14.utc).isoformat().replace('+00:00', 'Z'),
                                        'message': {'id': i, 'model': 'claude-opus-5-5', 'usage': {'input_tokens': (入 or [2])[0], 'cache_read_input_tokens': 读,
                                                                                                 'cache_creation_input_tokens': 写}}}) + '\n')
                f.write(json.dumps({'type': 'user', 'message': {'role': 'user', 'content': 'x'}}) + '\n')
        return 路
    with tempfile.TemporaryDirectory() as _d14:
        _冷 = _录14(_d14, '冷.jsonl', [('p1', -9010, 300000, 500), ('p2', -9000, 300500, 400), ('f1', -1800, 0, 301000), ('f2', -1790, 301000, 300)])
        _暖 = _录14(_d14, '暖.jsonl', [('p1', -3700, 300000, 500), ('f1', -1800, 300500, 900), ('f2', -1790, 301000, 300)])
        _隔暖 = _录14(_d14, '隔暖.jsonl', [('p1', -9000, 300000, 500), ('f1', -1800, 299000, 2000)])
        _无前 = _录14(_d14, '无前.jsonl', [('f1', -1800, 0, 301000), ('f2', -1790, 301000, 300)])
        _近冷 = _录14(_d14, '近冷.jsonl', [('p1', -3610, 300000, 500), ('f1', -1800, 0, 301000)])     # 隔三十分而缓存写（如 /compact 後）→ 静（界在一时）
        _半暖 = _录14(_d14, '半暖.jsonl', [('p1', -9000, 300000, 500), ('f1', -1800, 100000, 201000)])  # 隔二时而缓存读逾 5%（半暖）→ 静
        _无存 = _录14(_d14, '无存.jsonl', [('p1', -9000, 300000, 500), ('f1', -1800, 0, 1000, 300000)])  # 隔二时而缓存写不及半（入项未缓存）→ 静（⛔判冷唤）
        _不停 = lambda: False
        _言冷 = 冷唤之察(坐=_总11, 录=_冷, 停=_不停)
        _静14 = [冷唤之察(坐=_总11, 录=_暖, 停=_不停), 冷唤之察(坐=_总11, 录=_隔暖, 停=_不停), 冷唤之察(坐=_总11, 录=_无前, 停=_不停),
                冷唤之察(坐=_总11, 录=_冷, 停=lambda: True), 冷唤之察(坐='ABC123', 录=_冷, 停=_不停), 冷唤之察(坐=_总11, 录='', 停=_不停),
                冷唤之察(坐=_总11, 录=os.path.join(_d14, '缺.jsonl'), 停=_不停), 冷唤之察(坐=_总11, 录=_近冷, 停=_不停), 冷唤之察(坐=_总11, 录=_半暖, 停=_不停), 冷唤之察(坐=_总11, 录=_无存, 停=_不停)]
        _o14, _o14b = _io11.StringIO(), _io11.StringIO()
        with _cl11.redirect_stdout(_o14):
            print('止')
            冷唤之印(0, 察=lambda: 冷唤之察(坐=_总11, 录=_冷, 停=_不停))
        with _cl11.redirect_stdout(_o14b):
            冷唤之印(2, 察=lambda: 冷唤之察(坐=_总11, 录=_冷, 停=_不停))
            冷唤之印(0, 察=lambda: 1 / 0)
    T('W911 重造 环1④冷唤之察（预审·声明可虚书之守）：隔逾一时而本唤首回缓存读 0、写逾其半 → 「止」之次行「⚠ 本唤冷（隔 120 分……）——兜底之令之实或已改……list_triggers」；'
      '隔三十分（暖·或缓存写）、隔二时而首回仍暖、半暖（读逾 5%%）或写不及半、前唤不在、暂停令在、非总编辑之坐、转录缺 → 静；rc 非 0、察崩 ⛔印；--巡 之沙盒段 上下文之印 → 冷唤之印 → 落巡应，云巡⛔调——%s' % _言冷,
      _言冷.startswith('⚠ 本唤冷（隔 120 分') and 'list_triggers 对 接棒守.兜底之令' in _言冷 and 兜底之刻() in _言冷 and _静14 == [''] * 10
      and _o14.getvalue() == '止\n' + _言冷 + '\n' and _o14b.getvalue() == ''
      and _段沙11.find('上下文之印(_rc)') < _段沙11.find('冷唤之印(_rc)') < _段沙11.find('落巡应(_rc')
      and '冷唤之' not in src.split('def 云巡(')[1].split('\ndef ')[0].split('\n# ──')[0] and '冷唤之' not in src.split('def 巡(查印=False):')[1].split('\ndef ')[0]
      and 'reversed(_读尾(路, n))' in src.split('def 冷唤之察(')[1].split('\ndef ')[0] and '.read()' not in src.split('def 冷唤之察(')[1].split('\ndef ')[0])

    def _日分11(c):
        """cron 之分、时二栏 → 一日之刻（分）之集——* 、*/n、a-b、a-b/n、a,b。"""
        def _栏(f, 顶):
            诸 = set()
            for p in f.split(','):
                基, _, 步 = p.partition('/')
                lo, hi = (0, 顶 - 1) if 基 == '*' else (tuple(int(x) for x in 基.split('-')) if '-' in 基 else (int(基), int(基) if not 步 else 顶 - 1))
                诸.update(range(lo, hi + 1, int(步 or 1)))
            return 诸
        分, 时 = c.split()[:2]
        return {h * 60 + m for h in _栏(时, 24) for m in _栏(分, 60)}
    _刻11 = sorted(set().union(*[_日分11(常) for _, _, 常, _, 开 in 兜底之令 if 开]) or {0})
    _隔11 = max((_刻11[(i + 1) % len(_刻11)] - _刻11[i]) % 1440 or 1440 for i in range(len(_刻11)))
    T('坑61 之钉（W911 重造·独立之断言：一日之刻取 cron 之分与时二栏）：常态兜底之隔 %d 分 < 60、兜底之隔分 < 60——'
      '坑61：唤隔逾一时则缓存恒冷——每唤约十倍（1120 驳席实测冷唤 $3.3—4.1·费反为每三十分之 2.3 倍）' % _隔11,
      _隔11 < 60 and 兜底之隔分 < 60 and len(_刻11) >= 24)
    # 〔执行之制·治13(b)〕立停之巡：伪 Run 金 $30、估 $15 → 印立停；未逾、已毕（目录逾一时无动）、非进行 → ⛔印；无估 → 印「无估」
    _件13 = [{'id': 'W990', '名': '伪件', '状态': '进行', 'Run': ['wf_00000000-aaa']},
             {'id': 'W991', '名': '已成之件', '状态': '已成', 'Run': ['wf_00000000-bbb']},
             {'id': 'W992', '名': '无估之件', '状态': '进行', 'Run': ['wf_00000000-ccc']},
             {'id': 'W993', '名': '已毕', '状态': '进行', 'Run': ['wf_00000000-ddd']}]
    _金13 = {'wf_00000000-aaa': 30.0, 'wf_00000000-bbb': 99.0, 'wf_00000000-ccc': 5.0, 'wf_00000000-ddd': 99.0}
    _跑13 = lambda rid, 估: (_金13[rid] > 1.5 * 估, '已花 $%.2f／估 $%.2f' % (_金13[rid], 估))
    _印13 = 立停之巡(今=10000, 件们=_件13, 跑中=_跑13, 估之=lambda w: None if w == 'W992' else 15.0,
                  鲜之=lambda rid: 10000 - (7200 if rid.endswith('ddd') else 60))
    T('治13(b) 立停之巡：伪 Run 金 $30／估 $15 → 「⛔ 立停：TaskStop wf_…aaa」；已成、已毕之 Run ⛔印；无估 → 「无估」（⛔当 $0）',
      any('立停：TaskStop wf_00000000-aaa' in x for x in _印13) and not any('bbb' in x or 'ddd' in x for x in _印13)
      and any('W992' in x and '无估' in x for x in _印13) and len(_印13) == 2)
    _件13b = [dict(_件13[0])]
    T('治13(b) 之二 金未逾 1.5 倍（$20／$15）→ ⛔印立停', not 立停之巡(今=10000, 件们=_件13b, 跑中=lambda rid, 估: (False, ''), 估之=lambda w: 15.0, 鲜之=lambda rid: 9990))
    # 〔W921 环6〕X132 之三义、巡印之源與環时、版之鲜、败之必见、唯异方印、云巡之期、【重派】⛔试派
    try:
        今6 = 1_800_000_000
        _章6 = (485, 今6 - 20 * 60)
        _義 = lambda d, 章: 巡印判之义(d, 今6, 章=章)[1]
        T('⑥〔W921·X132①〕巡印判 三义分：鲜／随章 ↔ 章推未逾十五分 ↔ t 取不得；坏者 rc 5 之由；旧口 巡印判 照返由',
          _義({'时': 今6 - 60, '源': '環'}, _章6) == '鲜' and _義({'时': 今6 - 60 * 60, '源': '環'}, (485, 今6 - 70 * 60)) == '随章'
          and _義({'时': 今6 - 60 * 60, '源': '環'}, (485, 今6 - 5 * 60)) == '未逾' and _義({'时': 今6 - 60 * 60}, (485, 0)) == '无t'
          and _義({'时': 今6 - 60 * 60, '源': '環'}, _章6) == '坏' and 巡印判({'时': 今6 - 60 * 60, '源': '環'}, 今6, 章=_章6).startswith('⛔ GitHub 之巡停摆')
          and 巡印判({'时': 今6 - 60}, 今6, 章=_章6) == '')
        _坏cron = 巡印判之义({'时': 今6 - 60, '源': 'cron', '環时': 今6 - 60 * 60}, 今6, 章=_章6)
        T('⑥之二〔X132②〕cron 之巡印⛔掩 rc 5：cron 鲜而環时旧於章推 → 坏；旧式（无源）以其时（过渡）；源 試 ⛔证',
          _坏cron[1] == '坏' and _坏cron[0].startswith('⛔') and _義({'时': 今6 - 60}, _章6) == '鲜'
          and _義({'时': 今6 - 60, '源': '试'}, _章6) == '坏')
        _体a = 巡印之体(0, '止', 今6, 源='環', 前={'環时': 1}, 器='abc')
        _体b = 巡印之体(0, '止', 今6, 源='cron', 前={'環时': 今6 - 99}, 期=31)
        _体c = 巡印之体(0, '止', 今6, 源='cron', 前={'时': 今6 - 77})
        _体d = 巡印之体(0, '止', 今6, 源='cron', 前=None, 期=None)
        T('⑥之三 巡印之体：環／手更環时、cron 承前之環时（前无源者以其时承）；器、期（无期⛔书）',
          _体a['環时'] == 今6 and _体a['器'] == 'abc' and _体b['環时'] == 今6 - 99 and _体b['期'] == 31 and _体c['環时'] == 今6 - 77
          and '期' not in _体d and _体d['環时'] == 0 and 巡之源(环={'GITHUB_EVENT_NAME': 'schedule'}) == 'cron'
          and 巡之源(环={'GITHUB_EVENT_NAME': 'push'}) == '環' and 巡之源(环={'GITHUB_EVENT_NAME': 'workflow_dispatch'}) == '手' and 巡之源(True) == '试')
        _旧sha = os.environ.get('GITHUB_SHA')
        os.environ['GITHUB_SHA'] = '0' * 40
        try:
            _器 = 本器之版()
        finally:
            if _旧sha is None:
                os.environ.pop('GITHUB_SHA', None)
            else:
                os.environ['GITHUB_SHA'] = _旧sha
        T('⑥之四 器＝rev-parse HEAD（GITHUB_SHA ≠ HEAD 取 HEAD）；巡应之体带器',
          _器 == subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip() and _器 != '0' * 40
          and json.loads(巡应之体(0, 今6))['器'] == _器)
        _期 = 云巡之期('x/y', 取=lambda: {'workflow_runs': [{'created_at': '2026-11-24T%02d:%02d:00Z' % (h, m)} for h, m in ((10, 20), (11, 18), (12, 50), (15, 18), (16, 0))]})
        T('⑥之五 云巡之期：近十回 schedule 之隔之中位（分）；取不得 → None（⛔书）；巡印无「期」→ ⛔印补令；逾期 1.5 倍 → 印 run_workflow 巡.yml',
          _期 == 75 and 云巡之期('x/y', 取=lambda: 1 / 0) is None and 巡印逾期({'时': 今6 - 9999}, 今6) == ''
          and 'run_workflow 巡.yml' in 巡印逾期({'时': 今6 - 50 * 60, '期': 30}, 今6) and 巡印逾期({'时': 今6 - 40 * 60, '期': 30}, 今6) == '')
        _出1, _指1, _ = 印之滤(['🔴 甲', '⚠ 乙 3 分', '⛔ 丙'], [])
        _出2, _, _略2 = 印之滤(['🔴 甲', '⚠ 乙 4 分', '⛔ 丙', '🟡 丁'], _指1)
        T('⑥之六 唯异方印：同指纹之 🔴、⛔ 次巡仍印；⚠ 同（去数）即略；新 🟡 印', _出1 == ['🔴 甲', '⚠ 乙 3 分', '⛔ 丙']
          and _出2 == ['🔴 甲', '⛔ 丙', '🟡 丁'] and _略2 == 1)
        _败6 = {'k/n': '6/7', '因': {'器病': 6}, '席': [('察:甲', '器病', 'API Error: 400 …Property keys')], '果': 1}
        _查有 = 执行之查(None, ['体系总图·摘', '✓ 摘：用之红 0、⚠ 1、🔴 2、析崩 0（1 秒）'], False, None, [('wf_x', _败6)], 态={}, 写态=False)
        _查无 = 执行之查(None, None, True, None, [], 态={'🔴': 3}, 写态=False)
        T('⑥之七 败每巡必印（未裁之 Run·⛔ 器病 带裁之令）；已裁之败（败之扫不报）⛔印；摘逾时之行附前巡之 🔴 数',
          any(x.startswith('⛔ 败 wf_x·器病 6 席') for x in _查有) and any('--裁' in x for x in _查有)
          and not any('败 ' in x for x in _查无) and any('前巡 🔴 3' in x for x in _查无))
        _断6 = {'k/n': '1/7', '因': {'断': 1}, '席': [('察:乙', '断', 'API Error: 529 overloaded_error')], '果': 6}
        _态6 = {}
        _巡一 = 执行之查(None, None, True, None, [('wf_y', _断6)], 态=_态6, 写态=False)
        _巡二 = 执行之查(None, None, True, None, [('wf_y', _断6)], 态=_态6, 写态=False)
        T('⑥之七之二〔W921 环7〕断之败（⚠ 起）与摘逾时之行：次巡（同指纹）仍印（⛔为唯异所略）',
          any(x.startswith('⚠ 败 wf_y·断 1 席') for x in _巡一) and any(x.startswith('⚠ 败 wf_y·断 1 席') for x in _巡二)
          and any('图之摘逾时' in x for x in _巡二) and not any('同前巡' in x for x in _巡二))
        _重 = 派之参(9999, True)
        T('⑥之八【重派】⛔试派：巡() 之码⛔调 段序之守.判（新坐自起其钩判之）；主枝无第 N 章之料 → 派之参照出',
          '段序之守' not in 巡.__code__.co_names and isinstance(_重, dict) and '9999' in json.dumps(_重, ensure_ascii=False))
        T('⑥之九 版之鲜：心跳无「器」→ 无行（⛔误报）；心跳之基＝主树 → 无行',
          not [x for x in 版之鲜({'章': 1}) if '写书之坐' in x]
          and not [x for x in 版之鲜({'章': 1, '器': {'基': subprocess.run(['git', 'rev-parse', 'refs/remotes/origin/%s:工具' % 主枝], cwd=ROOT, capture_output=True, text=True).stdout.strip()}}) if '写书之坐' in x])
        _见, _原run = [], subprocess.run
        def _慢run(a_, **k_):
            _见.append(k_.get('timeout'))
            raise subprocess.TimeoutExpired(a_, k_.get('timeout') or 0)
        subprocess.run = _慢run
        try:
            _逾 = _读枝档('备份/巡印', '_巡印.json', 限=读枝之限)
        finally:
            subprocess.run = _原run
        import inspect as _insp
        _主 = open(os.path.abspath(__file__), encoding='utf-8').read().split("if __name__ == '__main__':")[-1]
        T('⑥之十〔W921 环7〕新添之读带时限：_读枝档 之 fetch 逾时 → None（⛔拖巡）；落巡印之前巡印、--巡 之执行之查（心跳、巡印）俱传 限（⛔心跳._远 之无限 fetch）',
          _逾 is None and _见 == [读枝之限] and '限=读枝之限' in _insp.getsource(落巡印)
          and '_读枝档(_心.枝, _心.档, 限=读枝之限)' in _主 and '_心._远()' not in _主)
    except Exception as e:
        T('⑥〔W921〕之测崩：%s %s' % (type(e).__name__, e), False)
    try:                             # 〔W919·X146〕origin 之址自正（工具/_仓.py·诸局显传 环）；_源 取 _仓.正址（⛔取 origin）；沙盒之 --巡 於第一律之印之後、存底守之前调之
        import _仓
        for _n46, _c46 in _仓.自测之局():
            T(_n46, _c46)
        _主46 = open(os.path.abspath(__file__), encoding='utf-8').read().split("\nif __name__ == '__main__':")[1]
        _沙46 = _主46.split("if '--巡' in a:")[1].split('sys.exit(_rc)')[0]
        _源码46 = open(os.path.abspath(__file__), encoding='utf-8').read().split('def _源():')[1].split('\n\n\n')[0]
        T('X146 接棒守._源 ＝ _仓.正址（⛔取 origin）；--巡（沙盒）首段调 _仓.正址之验 印 stderr、在第一律之印之後与存底守之前',
          源 == _仓.正址 and "'remote', 'get-url', 'origin'" not in _源码46
          and _沙46.index('第一律之印()') < _沙46.index('正址之验(ROOT)') < _沙46.index('_守先在 = True')
          and 'sys.stderr.write(_址' in _沙46)
    except Exception as e:
        T('X146 之测崩：%s %s' % (type(e).__name__, e), False)
    ok = sum(r)
    print('── 负测·接棒守 %d/%d %s ──' % (ok, len(r), '全通' if ok == len(r) else '未过'))
    return ok == len(r)


def 迹存(说, 起=None):
    """X86（1105·425 还账）：--候主／--派令 之迹於本器退出时方由 _账 追入 _器之迹.jsonl，而其时锁已收、存底守已停——新坐承云端之迹即缺。
    故於二令之末起一後台之存（脱离本器、候三秒令本器先退而迹先落），零 token；⛔续心跳（锁已收：⛔复活）。ZM_TRACE_SAVE=0 即免（自测）。"""
    if os.environ.get('ZM_TRACE_SAVE') == '0':
        return None
    令 = 'sleep 3; %s %s --不续心跳 --存 %s >/dev/null 2>&1' % (
        sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), '存底.py'), json.dumps('交棒之迹·' + 说, ensure_ascii=False))
    try:
        return (起 or subprocess.Popen)(['sh', '-c', 令], cwd=_仓目(), start_new_session=True,
                                        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        return None


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--自测' in a:
        sys.exit(0 if 自测() else 1)
    if '--立守书' in a:
        # 守书之会话立之（只查、⛔写书）：Stop 钩见之⛔令此坐写书。⛔写书之坐立之——其 Stop 钩之守即失。
        open(os.path.join(_仓目(), '守书.flag'), 'w').write('守书之会话（定时之保）\n')
        print('✓本机立为守书之坐（%s）' % os.path.join(_仓目(), '守书.flag'))
        sys.exit(0)
    if '--派令' in a:
        i = a.index('--派令')
        治 = 派令之治(int(a[i + 1]))        # 1027 A2：前章未入主而报坏（或缺章标而存底有其封）→【重派】自其源起、先治
        令 = 派令(int(a[i + 1]), '--重' in a, 治=治)
        if 治:
            print('⛔ 第%d章未入主枝而须治（源「%s」）——派【重派】之会话自其源起、先治之（会话之守认此形）' % (int(a[i + 1]) - 1, 治))
        print('照下参调 create_trigger 一回（⛔改）：')
        print(json.dumps(令, ensure_ascii=False, indent=1))
        迹存('--派令 %s' % a[i + 1])
        sys.exit(0)
    if '--候主' in a:
        i = a.index('--候主')
        _rc = 候主(int(a[i + 1]), int(a[i + 2]) if len(a) > i + 2 and a[i + 2].isdigit() else 90)
        迹存('--候主 %s rc=%s' % (a[i + 1], _rc))
        sys.exit(_rc)
    if '--哨' in a:
        sys.exit(哨())
    if '--云巡' in a:
        sys.exit(云巡('--试' in a))
    if '--早止' in a:
        try:
            _n = int(a[a.index('--早止') + 1])
        except (IndexError, ValueError):
            print('读不出：--早止 须章号 N——续')
            sys.exit(2)
        sys.exit(早止(_n))
    if '--巡' in a:
        if os.environ.get('GITHUB_ACTIONS') == 'true':
            sys.exit(巡())
        sys.stderr.write(第一律之印() + '\n')   # 〔W908 环12①〕印之首行：00_总章.md 第一律之首句（唯一之源）；读不得即「⚠ 第一律读不得」（stderr·stdout 仍只「止」或旧印）
        sys.stderr.flush()
        try:                         # 〔W919·X146〕origin 之址被环境改回旧仓即正之（工具/_仓.py）——印 stderr（stdout 仍只「止」）；存底守之前
            import _仓 as _仓_
            _址 = _仓_.正址之验(ROOT)
            if _址:
                sys.stderr.write(_址 + '\n'); sys.stderr.flush()
        except Exception as _e:
            sys.stderr.write('⚠ origin 之址之验不成：%s\n' % _e)
        import contextlib as _cl
        _守先在 = True
        try:                         # 1119 作者令「及时备份……防沙盒突然重启」（法用#防失稿三锁）：每巡验本坐之存底守在跑、不在即起——
            import 存底守 as _守      # 机换而开头之钩未跑之隙（1119 实踩：本坐 11-16 後三日无守、五十一档未存底）；零 token
            _守先在 = _守.在跑()
            if not _守先在:
                with _cl.redirect_stdout(sys.stderr):
                    _守.起()
        except Exception as _e:
            sys.stderr.write('⚠ 存底守之验起不成：%s\n' % _e)
        _态 = None
        try:                         # 〔1119 执行之审·治1〕活守：钩活、存底刻、钩死之自决与补印、每日首巡——印俱 stderr（stdout 仍只「止」或旧印）
            with _cl.redirect_stdout(sys.stderr):
                _态 = 活守(守先在=_守先在)
        except Exception as _e:
            sys.stderr.write('⚠ 活守之验不成：%s——巡应⛔带三键（云巡作旧论）\n' % _e)
        if '--代' not in a:          # 〔W912 环4〕执行之图：补印之後印 体系总图 --摘（今树即算·🔴 与用之红即红）於 stderr；逾二十秒即 ⚠（⛔拦巡）——云巡（GitHub）与 --代 之路⛔印
            _败扫 = None            # 〔W921 环6③〕败之扫独跑於摘之前（⛔共其二十秒·其自限 8 秒）
            try:
                import 费审 as _费
                _败扫 = _费.败之扫()
            except Exception as _e:
                sys.stderr.write('⚠ 败之扫不得：%s\n' % _e)
            _摘行, _摘超 = None, False
            try:
                _摘 = subprocess.run([sys.executable, os.path.join(ROOT, '工具', '体系总图.py'), '--摘'], cwd=ROOT, capture_output=True, text=True, timeout=20)
                _摘行 = (_摘.stdout or '').rstrip().split('\n') if (_摘.stdout or '').strip() else ['⚠ 图之摘无出（rc %s）' % _摘.returncode]
            except subprocess.TimeoutExpired:
                _摘超 = True
            except Exception as _e:
                _摘行 = ['⚠ 图之摘不得：%s' % _e]
            try:                     # 〔W921 环6〕执行之查：败、执行之图、版之鲜、段序之守之报、云巡之期——唯异方印（⚠／🟡）；⛔／🔴／败每巡必印
                import 心跳 as _心          # 〔W921 环7〕心跳、巡印之读带时限（_读枝档 限·⛔心跳._远 之无限 fetch）
                sys.stderr.write('\n'.join(执行之查(_读枝档(_心.枝, _心.档, 限=读枝之限), _摘行, _摘超, _读枝档(巡印枝, 巡印档, 限=读枝之限), _败扫 or [])) + '\n')
            except Exception as _e:
                sys.stderr.write('── 执行之图 ──\n%s\n⚠ 执行之查崩：%s\n' % ('\n'.join(_摘行 or ['⚠ 图之摘逾时（二十秒·⛔拦巡）']), _e))
            sys.stderr.flush()
        _rc = 巡(查印=True)          # 沙盒（总编辑之坐）：验巡印、常对拍；每跑俱落巡应（云巡验其应）
        上下文之印(_rc)               # 〔W911 重造 环1②〕「止」之次行：本坐上下文逾三十万即请作者 /compact（首行恒「止」、rc ⛔改；静则⛔印）
        冷唤之印(_rc)                 # 〔W911 重造 环1④〕「止」之次行：本唤冷（隔逾一时·缓存读≈0）即请对兜底之令之实（⛔虚书之声明）
        if not 落巡应(_rc, 态=_态, 前=_前巡应):    # 〔W911 重造 环1①〕降之粘：承前巡应之降
            sys.stderr.write('⚠ 巡应落不成（备份/巡应·先 git remote set-url origin 正址）——云巡将以「唤而未应」红\n')
        sys.exit(_rc)
    if '--在候' in a:
        sys.exit(0 if 在候() else 1)
    if '--候' in a:
        i = a.index('--候')
        n = int(a[i + 1])
        分 = int(a[i + 2]) if len(a) > i + 2 and a[i + 2].isdigit() else 30
        sys.exit(候(n, 分))
    print(__doc__)
    sys.exit(0)
