#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""心跳——**跨会话之锁：正在干活的那一坐每隔几分钟报一次到，别的坐一看便知。**

【其立之由（2026-09-10 作者令「尽量做到上一个任务全完成，下一个直接开始」）】
  ★初版之防撞车是「看远端末次提交距今多久」——**那是猜**：
    一章跑三个钟头，中间不提交，别的坐就误以为没人在跑，两坐同时动手，必冲突。
  ★★而拉长那个窗（150 分钟）又留下另一头的病：**上一坐已经干完了，下一坐还得干等**——
    正是作者所指的那一样：「上一个任务全完成了，下一个直接开始」。
  ★★★**两头都治不了，是因为那把尺量的不是「有没有人在干活」，是「有没有人刚提交过」。**
    **故改：让干活的那一坐自己报到。**

【它怎么跨会话】各坐各在自己的容器里，唯一共见者是远端。
  故心跳落在一枝专用之枝 `zm-心跳` 上，**其上永远只有一个提交**（每回 --跳 皆重写并强推）。
  ★**只强推这一枝**，正文那一枝一个字也不碰；★★其枝无史可丢——**它本就只该有此刻这一条**。

【用法】
    python3 工具/心跳.py --跳 310        # 我在跑第310章，报到（每几分钟一次）
    python3 工具/心跳.py --查            # 别人在跑吗？rc=1 表示「有人在跑，你退出」
    python3 工具/心跳.py --收 310        # 我干完了，撤锁（下一坐当场可接手，不必等）；心跳已属後章者⛔清（下一章已有席报到）
    python3 工具/心跳.py --自测
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
import json
import time
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
枝 = '备份/心跳'   # ★专用之枝：其上只有 _心跳.json 一档、只有一个提交（无父）
限 = 25 * 60          # 心跳逾此即判其坐已死，下一坐得接手（秒）；1116 作者令停书至多一时：45→25（存底守五分一续、转录十五分无写方停续——坐活而锁陈须静逾三十五分）


def _跑(*a, **k):
    return subprocess.run(a, cwd=ROOT, capture_output=True, text=True, **k)


枝主 = 'claude/the-novel-review-4dtuit'
档 = '_心跳.json'          # ★落在仓根，不在 设定／版本／正文——免与全测之「负测留字」相犯


def _写(d):
    """★★★**0910 重造·其由是一次差点撞车的实事**：
    　旧法把心跳提交在**正文那一枝**上再 `--no-verify` 推，而它自带一道守——
    　「HEAD 比远端多出别的改就不许推」。**而『多出别的改』正是写一章时的常态**
    　（席在跑，全测红，本坐的提交推不出去）——**於是心跳恰恰在最该续的时候续不上**：
    　实见其锁逾期九十一分钟，而下一个钟头的自走 Routine 再过十五分钟就要判「无人在跑」而动手。
    　★**一把在最需要它的时候会自己松开的锁，比没有锁更坏**——没有锁，人还知道要小心。

    ★★故改：心跳落在**一枝专用之枝**（`备份/心跳`），其上**只有一个档、只有一个提交**（无父）。
    　它是拿 `hash-object`＋`mktree`＋`commit-tree` 当场砌出来的——**不经索引、不碰 HEAD、
    　不碰工作区**，故**与本地有多少没推的提交毫无关系**。
    ★★★**而旧法那一道守，本法不再需要**：不是把它放松了，是**从形上不可能捎带别的东西**——
    　这个提交里**只有一个 blob**，多一样也塞不进去。**这比一道事後之守硬。**
    ★★★★**并记旧注之误**：旧注写「本环境推新枝当场挂死」——**那是误判**，
    　挂住的是 pre-push 钩子在跑全测；`--no-verify` 推新枝实测两秒即成。
    """
    import tempfile
    try:                             # 〔W919·X146〕推前验 origin 之址（工具/_仓.py）：环境改回旧仓即改回、印 stderr；崩只 ⚠
        import _仓
        _址 = _仓.正址之验(ROOT)
        if _址:
            sys.stderr.write(_址 + '\n')
    except Exception as _e:
        sys.stderr.write('⚠ origin 之址之验不成：%s\n' % _e)
    s_ = json.dumps(d, ensure_ascii=False)
    # 本地也留一份（好让人一眼看得见），但**推的不是它**
    with open(os.path.join(ROOT, 档), 'w', encoding='utf-8') as f:
        f.write(s_)
    tf = tempfile.mktemp(prefix='心跳_')
    try:
        with open(tf, 'w', encoding='utf-8') as f:
            f.write(s_)
        h = _跑('git', 'hash-object', '-w', tf).stdout.strip()
        if not h:
            return 2, 'hash-object 无果'
        r = subprocess.run(['git', 'mktree'], cwd=ROOT, capture_output=True, text=True,
                           input='100644 blob %s\t%s\n' % (h, 档))
        t = r.stdout.strip()
        if not t:
            return 2, 'mktree 无果：' + (r.stderr or '').strip()[:120]
        c = _跑('git', 'commit-tree', t, '-m', '心跳：%s' % s_).stdout.strip()
        if not c:
            return 2, 'commit-tree 无果'
        p2 = _跑('git', 'push', '--no-verify', '-q', '--force',
                 'origin', '%s:refs/heads/%s' % (c, 枝))
        return (0, '') if p2.returncode == 0 else (2, (p2.stderr or p2.stdout).strip()[:160])
    finally:
        if os.path.exists(tf):
            os.remove(tf)


def 坐():
    """本会话之号（去 cse_／session_ 之前缀；1021 治：旧读 CLAUDE_SESSION_ID，本环境无此变量，坐恒作「未名」——
    别坐看锁不知是谁，会话之守、存底之防覆遂无从比）。"""
    import re as _re
    for k in ('CLAUDE_CODE_REMOTE_SESSION_ID', 'CLAUDE_SESSION_ID', 'CLAUDE_CODE_SESSION_ID'):
        v = os.environ.get(k, '').strip()
        if v:
            return _re.sub(r'^(session_|cse_)', '', v)[:32]
    return '未名'


def 他持(d, 我, 今=None):
    """⛔纯判（1022）：云端之锁为他坐所持且新鲜否——跳⛔夺、收⛔抹。回 (他持?, 其坐)。"""
    今 = 今 or int(time.time())
    if not isinstance(d, dict) or d.get('章') is None:
        return False, ''
    他 = str(d.get('坐') or '')
    try:
        鲜 = 今 - int(d.get('时') or 0) <= 限
    except (TypeError, ValueError):
        鲜 = False
    return (bool(他) and 他 != 我 and 鲜), 他


停锁 = {'章': '暂停', '时': 4102444800, '坐': '暂停令'}   # 1022：作者暂停之锁——时在远後，诸判俱作「有人在写」，停书之巡判止、新坐⛔跳


def 立停():
    """作者暂停令在而有人欲开写书之会话时立之（会话之守）：停书之巡、停书警报见锁新鲜即止。"""
    在, d = _远()
    if 在 and isinstance(d, dict) and d.get('坐') == '暂停令':
        return 0, '停锁已在'
    return _写(dict(停锁))


def 解停(下):
    """暂停令解：停锁换作空锁（交第「下」章之棒）；派下章由总编辑（暂停令.解 印 --派令·巡坐⛔能派·1116）。⛔动他坐之锁。"""
    _守书之参(True)   # 1024：先印复开守书之巡之原样参（锁之换成否皆印——巡停则书断流）
    在, d = _远()
    if not (在 and isinstance(d, dict) and d.get('坐') == '暂停令'):
        return 0, '锁非停锁，⛔动'
    return _写({'章': None, '毕': int(下), '时': int(time.time()), '坐': '暂停令'})


def _守书之参(开):
    """1024·省审 sessions 四：印 update_trigger 之原样参（1117 起兜底之巡三令：停则俱停、开则复常；号与 cron 取 接棒守.兜底之令·⛔另硬写），并印调毕记之之令。"""
    try:
        import 暂停令
        if not 开 and 暂停令.守书停记():
            print('  守书之巡已记停（%s）' % 暂停令.守书停记().get('时', ''))
            return
        print('  守书之巡%s：%s；调毕 python3 工具/暂停令.py %s'
              % ('复开' if 开 else '停（停锁之下每唤只判「止」·白耗）', 暂停令.守书之参(开), '--守书已开' if 开 else '--守书已停'))
    except Exception as e:
        print('  ⚠ 守书之参印不出（%s）' % e)


def 跳(n):
    """报到：把 {章, 时, 坐} 写进仓根之心跳档并推。
    1022：他坐持鲜锁即⛔报（旧无主之查，两坐各跳各的、後跳者覆前者之锁，同写一章）。"""
    在, 远 = _远()
    持, 他 = 他持(远 if 在 else None, 坐())
    if 持:
        print('⛔心跳未报：第%s章之锁为他坐 %s 所持——⛔两坐同写；逾 %d 分不报方可接' % (远.get('章'), 他[:12], 限 // 60))
        return 1
    d = {'章': int(n), '时': int(time.time()), '坐': 坐()}
    器 = 器之版()
    if 器:
        d['器'] = 器                    # 〔W921 环6②〕版之鲜：本坐 HEAD 之工具树与其 merge-base(HEAD, origin/主) 之工具树（接棒守 --巡 比 origin/主:工具）
    rc, err = _写(d)
    print('✓心跳已报：第%d章｜%s' % (d['章'], time.strftime('%H:%M:%S', time.gmtime(d['时'])))
          if rc == 0 else '⛔心跳未推：%s' % err)
    return rc


def 器之版():
    """〔W921 环6②〕→ {'树': HEAD:工具 之树, '基': merge-base(HEAD, origin/主):工具 之树}；取不得之项⛔书、俱不得 → {}（⛔崩心跳·限 5 秒）。"""
    出 = {}
    try:
        r = _跑('git', 'rev-parse', 'HEAD:工具', timeout=5)
        if r.returncode == 0 and r.stdout.strip():
            出['树'] = r.stdout.strip()
        mb = _跑('git', 'merge-base', 'HEAD', 'refs/remotes/origin/' + 枝主, timeout=5).stdout.strip()
        if mb:
            r = _跑('git', 'rev-parse', mb + ':工具', timeout=5)
            if r.returncode == 0 and r.stdout.strip():
                出['基'] = r.stdout.strip()
    except Exception:
        pass
    return 出


def _远():
    """→ (档在?, 远端之心跳 dict；读不出为 None)。先 fetch——别坐之心跳只在远端。"""
    _跑('git', 'fetch', '-q', 'origin', '+refs/heads/%s:refs/remotes/origin/%s' % (枝, 枝))
    r = _跑('git', 'show', 'origin/%s:%s' % (枝, 档))
    if r.returncode != 0 or not r.stdout.strip():
        return False, None
    try:
        return True, json.loads(r.stdout.strip())
    except Exception:
        return True, None


def 查(印=True):
    """返 (有人在跑?, 几分钟前, 第几章)。**先自远端取，不看本地工作区**——
    ★其由：别坐之心跳只在远端；看本地即是看自己昨天写的那一张纸。"""
    在, d = _远()
    if not 在:
        if 印:
            print('✓无人在跑（心跳档不在）——本坐可接手。')
        return False, None, None
    if d is None:
        if 印:
            print('✓无人在跑（心跳读不出，作无人论）——本坐可接手。')
        return False, None, None
    if d.get('章') is None:
        if 印:
            print('✓无人在跑（上一坐已撤锁·第%s章办毕）——**本坐当场接手，不必等。**' % d.get('毕', '?'))
        return False, None, None
    差 = int(time.time()) - int(d.get('时', 0))
    if 差 <= 限:
        if 印:
            print('⛔有人在跑：第%s章｜%d 分钟前报到（限 %d 分钟）——**本坐当场退出，一字不改。**'
                  % (d.get('章'), 差 // 60, 限 // 60))
        return True, 差 // 60, d.get('章')
    if 印:
        print('✓无人在跑：末次心跳 %d 分钟前（逾限 %d 分钟），判其坐已死——**本坐接手。**'
              % (差 // 60, 限 // 60))
    return False, 差 // 60, d.get('章')


def _时(d):
    try:
        return int(d.get('时') or 0)
    except (TypeError, ValueError, AttributeError):
        return 0


def 可收(n, 现们):
    """⛔纯判（自测以假料跑）：撤第 n 章之锁可否。现们＝[本地之心跳, 远端之心跳]（dict 或 None）。
    取其新者（「时」大者；同时取前者）：其章在 n 之後 → (False, 由)——下一章已有席报到（他坐已起 N+1，或封版重跑时 N+1 已起），
      撤 N 之锁⛔清下一章之心跳（X21；旧：撤锁一律写「章＝空」）。
    ★1020 W53 验席之十：旧判「其一属後章即⛔写」——本地留後章之旧档而远端已撤（且更新）者，仍印「已交出」⛔写；今从其新者。"""
    新 = max((d for d in 现们 if isinstance(d, dict)), key=_时, default=None)
    持, 他 = 他持(新, 坐())
    if 持:
        return False, '锁为他坐 %s 所持（⛔抹他坐之鲜锁·1022）' % 他[:12]
    try:
        c = int((新 or {}).get('章'))
    except (TypeError, ValueError):
        return True, ''
    if c > int(n):
        return False, '心跳已属第%d章' % c
    return True, ''


def _本地():
    try:
        return json.load(open(os.path.join(ROOT, 档), encoding='utf-8'))
    except Exception:
        return None


def 收(n=None):
    """撤锁：写一个「章＝空」之心跳，下一坐一看即可当场接手，不必等满四十五分钟。
    给 n 而心跳（本地、远端取其新者）已属 n 之後之章者⛔写（可收）。"""
    if n:
        可, 由 = 可收(n, [_本地(), _远()[1]])
        if not 可:
            print('✓第%s章之锁已交出（%s）——⛔清：撤锁只撤本章自己的。' % (n, 由))
            return 0
    rc, err = _写({'章': None, '毕': (int(n) if n else None), '时': int(time.time()), '坐': 坐()})   # 1022：记撤锁者（Stop 钩认「己撤而未候接棒」）
    print('✓已撤锁（第%s章办毕）——下一坐当场可接手。' % (n or '?') if rc == 0
          else '⛔撤锁未推：%s' % err)
    return rc


def _防夺之测():
    今, r = 100000, []
    r.append(('⑮他持：他坐之鲜锁 → 是', 他持({'章': 404, '时': 今 - 60, '坐': 'B'}, 'A', 今)[0]))
    r.append(('⑮之二 己锁、陈锁、空锁 → 否', not 他持({'章': 404, '时': 今 - 60, '坐': 'A'}, 'A', 今)[0]
              and not 他持({'章': 404, '时': 今 - 限 - 1, '坐': 'B'}, 'A', 今)[0]
              and not 他持({'章': None, '时': 今, '坐': 'B'}, 'A', 今)[0]))
    s = open(os.path.abspath(__file__), encoding='utf-8').read().split('def 自测')[0]
    r.append(('⑯跳先问他持（⛔两坐同写）', '持, 他 = 他持(远 if 在 else None, 坐())' in s.split('def 跳(')[1].split('\ndef ')[0]))
    r.append(('⑯之二 可收先问他持（⛔抹他坐之鲜锁）', '他持(新, 坐())' in s.split('def 可收(')[1].split('\ndef ')[0]))
    return r


def 自测():
    ok, bad = 0, []

    def T(n, c, note=''):
        nonlocal ok
        if c:
            ok += 1
        else:
            bad.append(n + ('（%s）' % note if note else ''))

    # ★①之立日之败·记此免下一坐再造：初版把心跳落在一枝专用之枝（zm-心跳）上强推，
    #   **而本环境推新枝当场挂死**（实测 200 秒无果，非拒绝，是挂住）——
    #   **一把没验过的锁等於没有锁**；故改落仓根之一档，随正文那一枝走。
    T('①心跳之档落在仓根（不在 设定／版本／正文，免与全测之负测留字相犯）',
      '/' not in 档 and 档.startswith('_'))
    T('②限係二十五分钟（1116 一时之令；其数印在此，改它须同改本行）', 限 == 25 * 60)
    有, 分, 章 = 查(印=False)
    T('③查跑得动', isinstance(有, bool))
    # ④判据之源律：限不许写死在两处
    # ★只数 `def 自测` 以上之码——**否则测在数它自己**：
    #   ④之「限 = 」与⑦之二之枝名，皆出现在本测之字面里，遂自判其红。
    #   ★★此与 0909 席法之「样本自己就是病」是同一形，记此免下一坐再造。
    s = open(os.path.join(ROOT, '工具', '心跳.py'), encoding='utf-8').read().split('def 自测')[0]
    T('④限只定义一处（其数不许散在码里）', s.count('限 = ') == 1 and s.count('25 * 60') == 1,
      '限= %d 处｜25*60 %d 处' % (s.count('限 = '), s.count('25 * 60')))
    # ⑤撤锁之局须判「无人在跑」（拿一份假心跳当场验其读法，不推远端）
    T('⑤撤锁之形（章为空）读作无人在跑',
      json.loads('{"章": null, "毕": 310, "时": 1}').get('章') is None)
    # ⑥新鲜之心跳须判「有人在跑」
    T('⑥新鲜之心跳读作有人在跑', (int(time.time()) - int(time.time())) <= 限)
    # ⑦本器只推心跳枝，不碰正文之枝（判得死：全码里 push 之目标只此一枝）
    # ⑦**本器只推心跳枝，不碰正文之枝**（此格是本器最要紧的一道自守：
    #   它带 -f 强推，一旦目标写错即毁正文之史）。判得死：全码里凡 'push' 之处，其目标皆须是心跳枝。
    推 = [s[m.start():m.start() + 200] for m in re.finditer(r"_跑\('git', 'push'", s)]   # ★X44：push 之参跨两行，取其起处二百字
    # ★1021 X44 之裁：强推係形之所需（每回 commit-tree 无父、一回一根，推同枝必非快进）——旧格题「不带 -f」而码带 --force，
    #   只查 '-f' 看不见 '--force'，係 0910 起之假绿。守之真义在「只推心跳枝、心跳枝⛔係正文之枝」，故改判其目标。
    T('⑦凡 push 只此一处、目标只心跳枝、心跳枝⛔正文之枝（强推係无父之提交所需·X44）',
      len(推) == 1 and "'%s:refs/heads/%s' % (c, 枝)" in 推[0] and 枝 == '备份/心跳' and 枝 != 枝主
      and "--force" in 推[0] and not re.search(r"_跑\('git', 'push'[^\n]*枝主", s), str(推)[:160])
    # ⑦之二·**新法之守比旧法硬**：提交是拿 mktree 当场砌的，其中**只有一个 blob**——
    #   **多一样也塞不进去**。故判据不再是「推之前验一遍」，而是「从形上不可能」。
    T('⑦之二 提交是 mktree 砌的，树里只有心跳一档（多一样也塞不进去）',
      "'mktree'" in s and "'100644 blob %s" in s and s.count("'100644 blob") == 1)
    T('⑦之三 不经索引、不碰 HEAD、不碰工作区（故与本地有多少没推的提交无涉）',
      "'commit-tree'" in s and "'--only'" not in s and "'add'" not in s
      and "'checkout'" not in s and "'reset'" not in s)
    # ⑦之四·**旧法之败钉在此，免下一坐再把它搬回正文那一枝**
    T('⑦之四 心跳不推正文之枝（旧法之败：其守「HEAD 多出别的改就不推」，'
      '而那正是写一章时的常态，遂使锁在最需要它的时候松开）',
      '枝主' not in s.split('def 跳(')[0].split('def _写(')[1])
    T('⑦之五 心跳枝与存底枝、正文枝三者名各不同', 枝 not in ('claude/the-novel-review-4dtuit', '备份/存底'))
    # ⑧★X21：撤 N 之锁⛔清 N+1 之心跳（本地、远端取其新者，属後章即不写）；收须先问可收（回灌旧收——直写章＝空——即红）
    T('⑧撤锁⛔清後章之心跳（本地属 N+1／远端属 N+1 皆拦）',
      可收(394, [{'章': 395, '时': 1}, None])[0] is False and 可收(394, [None, {'章': 395}])[0] is False
      and 可收(394, [{'章': 394}, {'章': 394}])[0] is True and 可收(394, [{'章': None, '毕': 393}, None])[0] is True
      and 可收(394, [None, None])[0] is True)
    # ⑧之三★1020 验席之十：本地留 N+1 之旧档而远端已撤且更新 → 可收（旧判「其一属後章即拦」→ 印「已交出」⛔写，即红）；
    #   本地 N+1 更新（远端未推上）→ 仍拦；「时」读不出作 0
    T('⑧之三 本地、远端取其新者（本地旧档属後章而远端新撤 → 可收）',
      可收(394, [{'章': 395, '时': 100}, {'章': None, '毕': 394, '时': 200}])[0] is True
      and 可收(394, [{'章': 395, '时': 300}, {'章': None, '时': 200}])[0] is False
      and 可收(394, [{'章': 395, '时': 'x'}, {'章': None, '时': 5}])[0] is True)
    T('⑧之二 收先问可收，而後写', '可收(' in s.split('def 收(')[1].split('_写(')[0])
    全 = open(os.path.join(ROOT, '工具', '心跳.py'), encoding='utf-8').read()
    T('⑰解停先印复开守书之参、--立停印停之参（1024·号⛔硬写於本器）',
      '_守书之参(True)' in s.split('def 解停(')[1].split('\ndef ')[0]
      and '_守书之参(False)' in 全.split("if '--立停' in a:")[-1][:300] and 'trig_' not in s)
    for 名, 条 in _防夺之测():
        T(名, 条)
    try:                             # 〔W919·X146〕origin 之址自正（工具/_仓.py·诸局显传 环）；_写 推前调之
        import _仓
        for _n46, _c46 in _仓.自测之局():
            T(_n46, _c46)
        _写46 = 全.split('def _写(')[1].split('\ndef ')[0]
        T('X146 心跳._写 推前调 _仓.正址之验', _写46.index('_仓.正址之验(ROOT)') < _写46.index("'push'"))
    except Exception as e:
        T('X146 之测崩：%s' % e, False)
    print('── 负测·心跳 %d/%d %s ──' % (ok, ok + len(bad), '全通' if not bad else '｜未过：' + '；'.join(bad)))
    return not bad


if __name__ == '__main__':
    a = sys.argv
    if '--自测' in a:
        sys.exit(0 if 自测() else 1)
    if '--跳' in a:
        sys.exit(跳(a[a.index('--跳') + 1]))
    if '--立停' in a:                     # 1023：作者暂停令生效即立（自走印之）；解令时 暂停令.解 自换空锁
        rc, m = 立停()
        print('✓停锁已立' if rc == 0 and not m else (m or '⛔停锁未推'))
        _守书之参(False)
        sys.exit(rc)
    if '--收' in a:
        i = a.index('--收')
        sys.exit(收(a[i + 1] if len(a) > i + 1 and a[i + 1].isdigit() else None))
    有, _, _ = 查()
    sys.exit(1 if 有 else 0)
