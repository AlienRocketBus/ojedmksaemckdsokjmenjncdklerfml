# -*- coding: utf-8 -*-
"""〔W919·X146〕_仓（库）：仓之正址之唯一之源（坑53），与 origin 之自验自正。
为何立：环境每回重置其机即把 origin 改回旧仓（RobotSpa/the-novel·1116 换号前之址）——巡应推不成、摘之取迹逾时、
接棒守._源（create_session 之 source_url）随 origin 而指旧仓；「每回先 set-url」係人记（X146）。
接者：推.py __main__（--自测 之後首步·记 .git/推.log）、接棒守.py --巡（第一律之印之後·印 stderr）、接棒守._源（取 正址·⛔取 origin）、
存底.存／存底.标（推前）、心跳._写（推前）。
址之析(u)：https／http 之 github.com、ssh（git@github.com:）、代理（…/git/〈主〉/〈仓〉）→ (式, 主, 仓)；本地之路、他域 → None（⛔改：
  --shared 之演、worktree 之 origin 係本地之路，改之即直推 GitHub）。
正址之验(root, 环=None, 改=True)：url 与 pushurl 俱验；主／仓大小写⛔计；代理式只换其路、保其 host；他式 set 正址；
  环（env 之参·None 即读 os.environ·⛔以默参定死）之 GITHUB_ACTIONS 为 true ⛔动；崩即一行 ⚠（⛔崩推、⛔崩巡）。
换号即改 正址 一行。"""
import os, re, subprocess

正址 = 'https://github.com/AlienRocketBus/ojedmksaemckdsokjmenjncdklerfml'   # 1116 换号（RobotSpa 被标记→AlienRocketBus）、同日作者改仓名·唯此一处
_正 = re.search(r'github\.com/([^/]+)/([^/]+)$', 正址).groups()
_式们 = (('gh', re.compile(r'^(?:https?://)(?:[^@/\s]+@)?github\.com[:/]+([^/\s]+)/([^/\s]+?)(?:\.git)?/?$')),
        ('ssh', re.compile(r'^(?:ssh://)?git@github\.com[:/]+([^/\s]+)/([^/\s]+?)(?:\.git)?/?$')),
        ('代', re.compile(r'^https?://[^/\s]+/git/([^/\s]+)/([^/\s]+?)(?:\.git)?/?$')))


def 址之析(u):
    """→ (式, 主, 仓)｜None（本地之路、他域、不识 → ⛔改）。"""
    u = (u or '').strip()
    for 式, rx in _式们:
        m = rx.match(u)
        if m:
            return 式, m.group(1), m.group(2)
    return None


def 是正(u):
    析 = 址之析(u)
    return bool(析) and (析[1].lower(), 析[2].lower()) == (_正[0].lower(), _正[1].lower())


def _git(root, a):
    return subprocess.run(['git'] + a, cwd=root, capture_output=True, text=True, timeout=10)


def 正址之验(root, 环=None, 改=True):
    """→ ''（正·静）｜一行或数行（已改回／应改回／⚠）。⛔崩。"""
    try:
        环 = os.environ if 环 is None else 环
        if 环.get('GITHUB_ACTIONS') == 'true':
            return ''
        出 = []
        for 键 in ('url', 'pushurl'):
            r = _git(root, ['config', '--get', 'remote.origin.' + 键])
            u = (r.stdout or '').strip()
            if r.returncode != 0 or not u:
                continue
            析 = 址之析(u)
            if not 析:
                if 键 == 'url' and re.search(r'github|/git/', u):
                    出.append('⚠ origin 之址不识「%s」——⛔改（X146）' % u[:80])
                continue
            式, 主, 仓 = 析
            if (主.lower(), 仓.lower()) == (_正[0].lower(), _正[1].lower()):
                continue
            新 = 正址 if 式 in ('gh', 'ssh') else re.sub(r'/git/[^/\s]+/[^/\s]+?(?:\.git)?/?$', '/git/%s/%s' % _正, u)
            if 改:
                w = _git(root, ['config', 'remote.origin.' + 键, 新])
                if w.returncode != 0:
                    出.append('⚠ origin%s 之址被改作 %s/%s 而改回不成：%s——手跑：git config remote.origin.%s %s（X146）'
                             % ('' if 键 == 'url' else '（push）', 主, 仓, (w.stderr or '').strip()[:80], 键, 新))
                    continue
            出.append('⚠ origin%s 之址被改作 %s/%s —— %s正址 %s/%s（X146）'
                     % ('' if 键 == 'url' else '（push）', 主, 仓, '已改回' if 改 else '应改回', _正[0], _正[1]))
        return '\n'.join(出)
    except Exception as e:
        return '⚠ origin 之址之验不成：%s（X146）' % str(e)[:80]


def 自测之局():
    """→ [(名, 条)]：诸接者（推、接棒守、存底、心跳）之自测共载之（诸局俱显传 环·⛔读 os.environ——GitHub 之片 GITHUB_ACTIONS=true 亦同果）。"""
    import tempfile, shutil
    局 = []
    d = tempfile.mkdtemp(prefix='仓之测_')
    _e = dict({k: v for k, v in os.environ.items() if not k.startswith('GIT_')}, GIT_CONFIG_GLOBAL=os.devnull)

    def 仓(u, push=None):
        t = tempfile.mkdtemp(dir=d)
        subprocess.run(['git', 'init', '-q', t], capture_output=True, env=_e)
        subprocess.run(['git', 'remote', 'add', 'origin', u], cwd=t, capture_output=True, env=_e)
        if push:
            subprocess.run(['git', 'config', 'remote.origin.pushurl', push], cwd=t, capture_output=True, env=_e)
        return t

    def 址(t, 键='url'):
        return _git(t, ['config', '--get', 'remote.origin.' + 键]).stdout.strip()
    try:
        改们 = []
        for u in ('https://github.com/RobotSpa/the-novel', 'https://github.com/RobotSpa/the-novel.git', 'git@github.com:RobotSpa/the-novel.git'):
            t = 仓(u)
            语 = 正址之验(t, 环={})
            改们.append(址(t) == 正址 and '已改回' in 语)
        t = 仓('http://local_proxy@127.0.0.1:41077/git/RobotSpa/the-novel')
        语代 = 正址之验(t, 环={})
        代 = 址(t) == 'http://local_proxy@127.0.0.1:41077/git/%s/%s' % _正 and '已改回' in 语代
        局.append(('X146 旧仓之 https、.git、ssh 三式 → set 正址、代理式只换其路保 host', all(改们) and 代))
        静们 = []
        for u in (正址, 'https://github.com/alienrocketbus/OJEDMKSAEMCKDSOKJMENJNCDKLERFML.git', '/home/user/the-novel', 'https://gitlab.com/x/y'):
            t = 仓(u)
            静们.append(正址之验(t, 环={}) == '' and 址(t) == u)
        局.append(('X146 正址、大小写异、本地之路、他域 → 静而⛔改', all(静们)))
        t = 仓(正址, push='https://github.com/RobotSpa/the-novel')
        语推 = 正址之验(t, 环={})
        局.append(('X146 pushurl 亦验：url 正而 pushurl 旧 → 只改 pushurl', 址(t, 'pushurl') == 正址 and 址(t) == 正址 and '（push）' in 语推))
        t = 仓('https://github.com/RobotSpa/the-novel')
        局.append(('X146 环之 GITHUB_ACTIONS=true → 静而⛔改（GitHub 之机）', 正址之验(t, 环={'GITHUB_ACTIONS': 'true'}) == ''
                   and 址(t) == 'https://github.com/RobotSpa/the-novel'))
        局.append(('X146 改=False → 只印「应改回」⛔改', '应改回' in 正址之验(t, 环={}, 改=False) and 址(t) == 'https://github.com/RobotSpa/the-novel'))
        语崩 = 正址之验(os.path.join(d, '不在'), 环={})
        局.append(('X146 根不在 → 一行 ⚠ 或静（⛔崩）', 语崩 == '' or 语崩.startswith('⚠')))
    except Exception as e:
        局.append(('X146 _仓 之局崩：%s' % e, False))
    finally:
        shutil.rmtree(d, ignore_errors=True)
    return 局


if __name__ == '__main__':
    import sys
    if sys.argv[1:] == ['--自测']:
        r = 自测之局()
        坏 = [n for n, c in r if not c]
        print('── 负测·_仓 %d/%d %s ──' % (len(r) - len(坏), len(r), '全通' if not 坏 else '｜未过：' + '；'.join(坏)))
        sys.exit(1 if 坏 else 0)
    print(正址之验(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) or '· origin 正')
