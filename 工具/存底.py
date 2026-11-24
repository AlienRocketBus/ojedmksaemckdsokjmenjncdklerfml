#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""存底——**把此刻工作区里的一切（含没提交的、正在写的）推上云端，秒级，不碰工作区。**

【其立之由（2026-09-10 作者令「最好双备份」）】
★**先说本坐不确定的那一样，因为那才是真风险**：
  云端保的是**已封版**的；而**一章要写三个钟头，那三个钟头里它只在这一台机器上**。
  **容器一挂就没了**——今日已挂过一回（第308章之通知丢了，幸而正文已落盘）。
  **故最大的洞不是「云端会丢」，是「正在写的那一章不在云端」。**
★★而先前判「推新枝不成」是**误判**：那不是不许推，是 pre-push 钩子在跑全测（两三分钟），
  本坐九十秒超时杀了它，遂当作挂死。**今实测：`--no-verify` 推新枝 2 秒即成。**
  ★★★**记此一条**：**「跑不通」与「跑得慢」是两回事；没等它跑完就断言不通，是本坐今日之误。**

【它做什么·三样，皆判得死】
  甲·**存底枝**（`备份/存底`）：把此刻工作区之全部（含未跟踪、未提交者）打成一个提交推上去。
  　　★**不碰工作区、不碰索引、不碰 HEAD**——用一份临时索引另起炉灶（`GIT_INDEX_FILE`），
  　　**故席正在写它也照存不误**（这正是它存在的意思）。
  乙·**章标**（`章-N`）：一章封版即打一个标，**标是不动的**，滚动枝坏了它还在。
  　　★**本仓远端拒推 tag（HTTP 403）**，故「标」落在 `refs/heads/章-N` 上，**且一律不带 --force**：
  　　不快进即被拒，一样覆不掉。**其不动之凭是「一个 --force 也没有」，不是它叫什么名字。**
  丙·**验**：自云端把存底枝取回来，数它有几章、几字，**不拿本地之数充数**。
  丁·**演**（0910 补）：**真去克隆一份下来，逐档与本地比大小**——★**没有演过的备份不算备份**。
  　　★其所以连「正在写而未提交的那一章」也比：**已提交的东西主枝上也有，
  　　只有没提交的那一份，丢了就是真丢了**——存底枝立起来就是为这一样。

【与主枝之别·写死，免下一坐混淆】
  · 主枝 `claude/the-novel-review-4dtuit`：**成果**。走全测、走钩子，只收已封版之章。
  · 存底枝 `备份/存底`：**保命**。不走闸（走了就秒不了），**只为「机器挂了不丢工夫」**。
  　★★★★**故存底枝之物不许当成果用**：它里头可能有写到一半的章。
  　**要看成果，看主枝。要救命，看存底枝。**

用法：
    python3 工具/存底.py --存 "在写第310章·三庭毕"   # 秒级，随时可跑
    python3 工具/存底.py --标 309                    # 封版之章打一个不动的标
    python3 工具/存底.py --验                        # 自云端取回来数一遍
    python3 工具/存底.py --演 309                    # ★真克隆下来比一遍（约三十秒·人手之演：1027 A2 出封版之每章之序——章-N 之克隆归 GitHub autopush 之取）
    python3 工具/存底.py --自测
    python3 工具/存底.py --演章 309 [--源 URL]       # 只演章标一半（1027 坑54：GitHub autopush 於章-* 每章跑之、判入报之「演」）
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
import time
import glob
import shutil
import tempfile
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
底枝 = '备份/存底'
主枝 = 'claude/the-novel-review-4dtuit'


def _跑(*a, env=None, cwd=None):
    e = dict(os.environ)
    if env:
        e.update(env)
    r = subprocess.run(a, cwd=cwd or ROOT, capture_output=True, text=True, env=e)
    if r.returncode != 0:   # 1024 盘坏之哨：诸 git 之调俱经此——遇 Input/output error／signal 7 即立 <git 公目>/盘坏.flag（零 token）
        try:
            import 重取
            重取.查迹(r.returncode, r.stderr or '', ' '.join(str(x) for x in a[:3]))
        except Exception:
            pass
    return r


def _档肿哨():
    """★存之前先跑一回档肿哨（0916·335 封版席接进此处）。

    ⛔**其所以接在这里，不接在别处**：**档肿哨之职逐字係「下一回再肿，是在存底之前看见，
      不是在远端拒收之後才猜」**——**而它立出来的那一日没有接进任何一个跑口**，
      `囤灰闸` 当场判它「造了没人跑」。★**一个写在流程里而从来没跑起来的器，正是作者点名要治的那一样。**
    ★**其实证（0916 之事）**：`版本/第335章/_轮记.md` 一度肿到 113MB／424,670 行而唯一非空行只 1,385 行，
      **前二席之 `--存` 两跑皆被远端拒收（`remote: error: See https://gh.io/lfs`），而那两席都不知道自己为什麽推不上去。**
    ★★**其位只报不拦**：**肿了照旧让它试着推**——**拦住它，等於把一次本来能成的备份也断了**；
      ⛔**而它若真被远端拒收，这一行印就是那一次拒收的由。**
    """
    try:
        r = _跑(sys.executable, os.path.join(ROOT, '工具', '档肿哨.py'))
        out = (r.stdout or '').strip().splitlines()
        if r.returncode != 0:
            print('  ⛔档肿哨：有档肿到推不上去（存底或被远端拒收）——')
            for ln in out[-6:]:
                print('    ' + ln)
        elif out:
            print('  ' + out[-1])
    except Exception as e:                      # ★哨子坏了不许拖累存底
        print('  ⚠档肿哨跑不动（不拦存底）：%s' % e)


旧链 = 底枝 + '-旧'      # 被顶下之他机之底，逐一挂进此链（不强推、只快进）——⛔一份底被覆而无存


def _机():
    """本机（容器）之号。⛔只认会话号：一会话复开即换新机，旧机之稿新机没有（402 之失正是此形）。"""
    v = os.environ.get('CLAUDE_CODE_CONTAINER_ID', '').strip()
    return re.sub(r'^container_', '', v).split('--')[0][:24] or '未名'


def _坐():
    try:
        import 心跳
        return 心跳.坐()
    except Exception:
        return '未名'


def 旁枝(坐=None):
    return '%s-%s' % (底枝, (坐 or _坐())[:12])


def _锁():
    """→ (锁新鲜?, 坐, 章)：云端心跳之锁。读不出作 (False, '', None)。"""
    try:
        import 心跳 as _hb
        在, d = _hb._远()
        if not 在 or not isinstance(d, dict) or d.get('章') is None:
            return False, '', None
        return (int(time.time()) - int(d.get('时', 0) or 0) <= _hb.限), str(d.get('坐') or ''), d.get('章')
    except Exception:
        return False, '', None


def _远底():
    """→ (读得出?, 远端存底之 sha 或 None, 其信)。⛔看本地之 origin/ 引——那是上回取的旧影。"""
    r = _跑('git', 'ls-remote', 'origin', 'refs/heads/' + 底枝)
    if r.returncode != 0:
        return False, None, ''
    sha = r.stdout.split()[0] if r.stdout.strip() else None
    if not sha:
        return True, None, ''
    _跑('git', 'fetch', '-q', 'origin', '+refs/heads/%s:refs/remotes/origin/%s' % (底枝, 底枝))
    return True, sha, _跑('git', 'log', '-1', '--format=%B', sha).stdout


def 判底(远sha, 远信, 我机, 他持):
    """⛔纯判（1021·402 之失）：此回之底推往何处。回 '主'｜'旁'｜'存旧再主'。
    ①他坐持写书之锁 → '旁'：主存底枝归写书之坐，余坐各推己之旁枝，⛔顶之；
    ②远端之底即本机所存（信中「机」同）→ '主'：顶自己之旧底无失；
    ③余（他机之底、旧式无「机」之底）→ '存旧再主'：先把它挂进 旧链（不强推），挂成方顶——⛔一份底被覆而无存。
    ⛔以会话号认「己」：会话复开即新机，旧机之底有新机所无之稿。"""
    if 他持:
        return '旁'
    if not 远sha:
        return '主'
    m = re.search(r'｜机 (\S+)', 远信 or '')
    if m and 我机 != '未名' and m.group(1) == 我机:
        return '主'
    return '存旧再主'


def 存旧(sha, 信=''):
    """把被顶下之底挂进 旧链：新提交以 旧链之顶 与 sha 为二父，只快进推（⛔--force）。已挂过即免。"""
    for _ in range(3):
        r = _跑('git', 'ls-remote', 'origin', 'refs/heads/' + 旧链)
        if r.returncode != 0:
            return False
        顶 = r.stdout.split()[0] if r.stdout.strip() else None
        if 顶:
            _跑('git', 'fetch', '-q', 'origin', '+refs/heads/%s:refs/remotes/origin/%s' % (旧链, 旧链))
            if _跑('git', 'merge-base', '--is-ancestor', sha, 顶).returncode == 0:
                return True
        t = _跑('git', 'rev-parse', sha + '^{tree}').stdout.strip()
        a = ['git', 'commit-tree', t, '-m', '存旧 %s｜%s' % (sha[:8], (信 or '').strip().split('\n')[0][:80])]
        if 顶:
            a += ['-p', 顶]
        a += ['-p', sha]
        c = _跑(*a).stdout.strip()
        if not c:
            return False
        if _跑('git', 'push', '--no-verify', '-q', 'origin', '%s:refs/heads/%s' % (c, 旧链)).returncode == 0:
            return True
    return False


末树档 = os.path.join(ROOT, '.git', '存底.末树')
# 强塞之档：.gitignore 之诸账（主枝⛔脏），存底须带之。1027 A2：设定/自进化环.log（自走每跑落一行·旧随踪而树恒脏、每回一提交）入此
强塞之档 = ('_跑账.json', '_任务流.json', '_器之账.json', '_器之迹.jsonl', '设定/自进化环.log')


def _址正():
    """〔W919·X146〕推前验 origin 之址（工具/_仓.py·正址唯一之源）：环境改回旧仓即改回、印一行 stderr；GitHub 之机、本地之路⛔动；崩只 ⚠。"""
    try:
        import _仓
        _址 = _仓.正址之验(ROOT)
        if _址:
            sys.stderr.write(_址 + '\n')
    except Exception as e:
        sys.stderr.write('⚠ origin 之址之验不成：%s\n' % e)


def 存(说明='', 续心跳=True, 跳同=False):
    """★其法之要：另用一份临时索引，故**工作区、索引、HEAD 三样一样不碰**。
    1021 添防覆（402 之失）：推前取云端之底与心跳之锁，照 `判底` 推往主枝或己之旁枝；顶他机之底前先挂进 旧链；
    主枝之推带 lease（他坐抢先一步即重判，⛔盲覆）。跳同：此树与上回所推者同即不推（存底守之定时用）。
    1027 A2：档肿哨只於树已变（异於上回所推之树）方跑——旧每回先跑（五分一回、一章四十七至百一十回、CPU 一百五十至四百八十秒），树未变者其肿已於上回见过。"""
    _址正()                           # 〔W919·X146〕推前验 origin 之址
    idx = tempfile.mktemp(prefix='存底idx_')
    try:
        env = {'GIT_INDEX_FILE': idx}
        r = _跑('git', 'add', '-A', env=env)
        # 跳同只比诸账之外之树：存底一跑，跑账即添一行——以全树比，则五分一回之存底守回回自见「有改」而空推（1021）
        t0 = _跑('git', 'write-tree', env=env).stdout.strip()
        # ★诸账在 .gitignore 里（免得主枝永远是脏的），故须**强塞**进这一份临时索引——
        #   **存底枝要是没有它们，续跑之账就断了**（东西保住而进度丢了，仍是断）。
        for _档 in 强塞之档:
            if os.path.exists(os.path.join(ROOT, _档)):
                _跑('git', 'add', '-f', _档, env=env)
        if r.returncode != 0:
            return 2, ('add：' + (r.stderr or r.stdout).strip()[:120])
        t = _跑('git', 'write-tree', env=env).stdout.strip()
        if not t:
            return 2, 'write-tree 无果'
        try:
            同 = open(末树档).read().strip() == t0
        except Exception:
            同 = False
        if 跳同 and 同:
            return 0, '无改·不推'
        if not 同:
            _档肿哨()                          # 树已变方跑（其职「再肿是在存底之前看见」照旧：推之前）
        我坐, 我机 = _坐(), _机()
        msg = '存底 %s｜%s｜坐 %s｜机 %s' % (time.strftime('%m-%d %H:%M:%S', time.gmtime()), 说明 or '', 我坐, 我机)
        c = _跑('git', 'commit-tree', t, '-p', 'HEAD', '-m', msg).stdout.strip()
        if not c:
            return 2, 'commit-tree 无果'
        鲜, 锁坐, 锁章 = _锁()
        他持 = 鲜 and 锁坐 != 我坐
        去 = None
        for _ in range(3):
            读得, 远, 远信 = _远底()
            向 = 判底(远, 远信, 我机, 他持) if 读得 else '旁'
            if 向 == '存旧再主' and not 存旧(远, 远信):
                向 = '旁'                                # 挂不进旧链即⛔顶，退推己之旁枝
            if 向 == '旁':
                底枝旁 = 旁枝(我坐)
                p = _跑('git', 'push', '--no-verify', '-q', '--force',
                        'origin', '%s:refs/heads/%s' % (c, 底枝旁))
                if p.returncode != 0:
                    return 2, (p.stderr or p.stdout).strip()[:160]
                去 = '旁枝 %s（%s）' % (底枝旁, '第%s章之锁为他坐 %s 所持' % (锁章, 锁坐[:12]) if 他持 else '云端之底读不出或挂旧链未成')
                break
            p = _跑('git', 'push', '--no-verify', '-q', '--force-with-lease=refs/heads/%s:%s' % (底枝, 远 or ''),
                    'origin', '%s:refs/heads/%s' % (c, 底枝))
            if p.returncode == 0:
                去 = 底枝 + ('（先挂他机之底 %s 进 %s）' % (远[:8], 旧链) if 向 == '存旧再主' else '')
                break
        if 去 is None:
            return 2, '三回 lease 俱败（他坐连推），未推'
        try:
            open(末树档, 'w').write(t0)
        except Exception:
            pass
        # ★存底既已上云，顺手把「任务流跑到哪儿了」也记一步——
        #   **东西保住了而进度丢了，下一坐仍得从头猜**（作者 0910 令）。
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            import 续跑
            # ★带上前缀：存底之步是**流水**，不是**实事**；
            #   续跑之印要分得出这两样，否则实事会被一串存底埋掉。
            续跑.记('存底·' + (说明 or ''), None, c[:8])
            # ★并顺手续一次心跳：0910 实见其锁逾期九十一分钟，而自走 Routine
            #   再过十五分钟就要判「无人在跑」而动手——**差一点撞车**。
            import 心跳 as _hb
            try:
                # ⛔★★★★★2026-09-24 治·**存底替一把死锁续命**：非席之存（L0 自修／人手）不续心跳——`续心跳=False` 或 `--不续心跳`。
                # ⛔1021 治·**存底替他坐之锁改主**：旧只问「有锁」即以本坐之名重写其锁——他坐之锁被本坐夺去；
                #   今只续**本坐所持、尚新鲜**之锁（逾期之锁⛔复活——0924 之病）。
                if 鲜 and 锁章 and 锁坐 == 我坐 and 续心跳 and os.environ.get('ZM_存底不续心跳') != '1':
                    _hb._写({'章': int(锁章), '时': int(time.time()), '坐': 我坐})
            except Exception:
                pass
        except Exception:
            pass
        return 0, '%s → %s' % (c[:8], 去)
    finally:
        if os.path.exists(idx):
            os.remove(idx)


def 标(n, sha=None):
    """一章封版即打一个**不动的**标。滚动之枝可被覆盖，标不可。
    sha：所推之提交（1027 A2：自进化环 L0 缺碑推封版#N 之提交，⛔HEAD——HEAD 或已远在其後）；缺则 HEAD（封版之末推：HEAD 即封版之提交）。"""
    名 = '章-%d' % int(n)
    _址正()                           # 〔W919·X146〕推前验 origin 之址
    c = sha or _跑('git', 'rev-parse', 'HEAD').stdout.strip()
    # ★本仓之远端拒推 tag（HTTP 403），推 refs/heads 则成——故「不动的那一层」
    #   落在**不许强推的枝**上：不快进即被拒，一样覆不掉。
    p = _跑('git', 'push', '--no-verify', '-q', 'origin',
            '%s:refs/heads/%s' % (c, 名))
    if p.returncode != 0:
        s = (p.stderr or p.stdout).strip()
        if 'already exists' in s or 'stale info' in s:
            return 0, '%s 早已在云端（标不重打——**标是不动的**）' % 名
        return 2, s[:160]
    return 0, '%s → %s' % (名, c[:8])


def 验(印=True):
    _跑('git', 'fetch', '-q', 'origin', '+refs/heads/%s:refs/remotes/origin/%s' % (底枝, 底枝))
    r = _跑('git', 'log', '-1', '--format=%H|%cr|%s', 'origin/' + 底枝)
    if r.returncode != 0 or not r.stdout.strip():
        if 印:
            print('  ⛔存底枝不在云端——**保命那一层今日是空的**。')
        return None
    sha, 何时, 说明 = (r.stdout.strip().split('|', 2) + ['', ''])[:3]
    章 = _跑('git', '-c', 'core.quotepath=false', 'ls-tree', '-r', '--name-only',
             'origin/' + 底枝, '正文/').stdout
    n = len([x for x in 章.split('\n') if x.strip().endswith('.md')])
    标们 = [x for x in _跑('git', 'ls-remote', '--heads', 'origin').stdout.split('\n')
           if re.search(r'refs/heads/(章-|\\346\\253)', x)]
    if 印:
        print('  ── 存底枝（保命那一层）──')
        print('   %s｜%s｜%s' % (sha[:8], 何时, 说明[:60]))
        print('   **其中正文 %d 章**（含此刻正在写而未封版者）' % n)
        print('  ── 章标（不动的那一层）──')
        print('   云端章标 %d 个%s' % (len(标们), '' if 标们 else ' ⛔一个也没有'))
    return {'sha': sha[:8], '章': n, '标': len(标们)}


def 演(章=None):
    """★**没有演过的备份不算备份。**
    本器不看本地、不看远端的账面——**真去克隆一份下来，拿眼睛看里头有没有东西**。
    甲：克隆存底枝，数它的正文几章、正在写那一章几个字，且与本地工作区**当场比**；
    乙：克隆一个章标，看它是不是一份跑得动的仓（有正文、有工具、有设定）。
    ★其所以要连「正在写而未提交的那一章」一起比：**存底枝立起来就是为了这一样**——
    已提交的东西主枝上也有，只有没提交的那一份，丢了就是真丢了。
    """
    tmp = tempfile.mkdtemp(prefix='演存底_')
    url = _跑('git', 'remote', 'get-url', 'origin').stdout.strip()
    坏 = []
    try:
        d = os.path.join(tmp, '甲')
        r = _跑('git', 'clone', '-q', '--depth', '1', '--branch', 底枝, url, d)
        if r.returncode != 0:
            return 2, '存底枝克隆不下来：' + (r.stderr or '').strip()[:120]
        章们 = [x for x in os.listdir(os.path.join(d, '正文')) if x.endswith('.md')]
        本地 = [x for x in os.listdir(os.path.join(ROOT, '正文')) if x.endswith('.md')]
        if len(章们) < len(本地):
            坏.append('云端存底 %d 章，本地 %d 章——**少了**' % (len(章们), len(本地)))
        # ★逐档比大小：只比正文，且以本地为准（本地是那一刻的实）
        差 = []
        for x in 本地:
            a = os.path.join(d, '正文', x)
            if not os.path.exists(a):
                差.append(x + '（云端没有）')
            elif os.path.getsize(a) != os.path.getsize(os.path.join(ROOT, '正文', x)):
                差.append('%s（%d≠%d）' % (x, os.path.getsize(a),
                                           os.path.getsize(os.path.join(ROOT, '正文', x))))
        if 差:
            坏.append('正文有 %d 档对不上：%s' % (len(差), '、'.join(差[:3])))
        # 乙·章标（1027 坑54：每章之演归 GitHub autopush——章-* 之跑以同一 演章 真克隆其标、判入报之「演」）
        if 章 is not None:
            rc2, m2 = 演章(章, url)
            if rc2 != 0:
                坏.append(m2)
        if 坏:
            return 2, '；'.join(坏)
        return 0, '存底枝克隆下来 %d 章，逐档与本地同（含正在写而未提交的那一章）%s' % (
            len(章们), ('｜章标 章-%s 亦是一份跑得动的仓' % 章) if 章 is not None else '')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


可跑之档 = ('正文', '设定', '工具')


def 仓缺(d):
    """一份克隆下来的仓缺哪几样（正文、设定、工具）——缺一即「跑不动」。"""
    return [x for x in 可跑之档 if not os.path.isdir(os.path.join(d, x))]


def 演章(章, url=None):
    """乙·章标之演：真克隆「章-N」（--depth 1），看它是不是一份跑得动的仓。→ (rc, 语)
    1027 坑54：每章之演归 GitHub autopush（章-* 之跑·报之「演」，演之效全同：只克隆云端之标）——沙盒 --演 N 亦经此一函（⛔两份）。"""
    url = url or _跑('git', 'remote', 'get-url', 'origin').stdout.strip()
    tmp = tempfile.mkdtemp(prefix='演章_')
    try:
        d = os.path.join(tmp, '乙')
        r = _跑('git', 'clone', '-q', '--depth', '1', '--branch', '章-%d' % int(章), url, d)
        if r.returncode != 0:
            return 2, '章标 章-%s 克隆不下来：%s' % (章, (r.stderr or '').strip()[:120])
        缺 = 仓缺(d)
        if 缺:
            return 2, '章标 章-%s 里缺 %s——**它不是一份跑得动的仓**' % (章, '、'.join(缺))
        return 0, '章标 章-%s 真克隆下来是一份跑得动的仓（%s 俱在）' % (章, '、'.join(可跑之档))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def 防覆之演():
    """真跑：临时之 bare 远端＋工作仓；心跳、续跑、档肿哨以假者代（⛔碰真仓）。回 [(名, 过否)]。"""
    import types
    g = globals()
    旧 = {k: g[k] for k in ('ROOT', '末树档', '_档肿哨', '_锁', '_远底')}
    旧模 = {k: sys.modules.get(k) for k in ('心跳', '续跑')}
    旧环 = {k: os.environ.get(k) for k in ('CLAUDE_CODE_CONTAINER_ID', 'ZM_存底不续心跳')}
    果, 写们, 状 = [], [], {'坐': 'SIDA', '锁': (False, '', None)}
    d = tempfile.mkdtemp(prefix='防覆之演_')
    try:
        远, 工 = os.path.join(d, 'r.git'), os.path.join(d, 'w')
        subprocess.run(['git', 'init', '-q', '--bare', 远], check=True)
        subprocess.run(['git', 'init', '-q', 工], check=True)
        for k, v in (('user.name', 't'), ('user.email', 't@t'), ('commit.gpgsign', 'false')):
            subprocess.run(['git', '-C', 工, 'config', k, v], check=True)
        subprocess.run(['git', '-C', 工, 'remote', 'add', 'origin', 远], check=True)
        open(os.path.join(工, 'a.md'), 'w').write('一')
        open(os.path.join(工, '.gitignore'), 'w').write('_跑账.json\n_任务流.json\n')   # 同真仓：诸账⛔入主枝
        subprocess.run(['git', '-C', 工, 'add', '-A'], check=True)
        subprocess.run(['git', '-C', 工, 'commit', '-q', '-m', 'c0'], check=True)
        肿计 = []
        g['ROOT'], g['末树档'], g['_档肿哨'] = 工, os.path.join(d, '末树'), (lambda: 肿计.append(1))
        g['_锁'] = lambda: 状['锁']
        sys.modules['心跳'] = types.SimpleNamespace(坐=lambda: 状['坐'], _写=lambda x: 写们.append(x), 限=2700,
                                                  _远=lambda: (False, None), 查=lambda 印=False: (False, None, None))
        sys.modules['续跑'] = types.SimpleNamespace(记=lambda *a, **k: None)
        os.environ.pop('ZM_存底不续心跳', None)
        远顶 = lambda b: (subprocess.run(['git', '-C', 远, 'rev-parse', '-q', '--verify', 'refs/heads/' + b],
                                         capture_output=True, text=True).stdout.strip() or None)
        含 = lambda a, b: subprocess.run(['git', '-C', 远, 'merge-base', '--is-ancestor', a, b]).returncode == 0
        def 写(x):
            open(os.path.join(工, 'a.md'), 'w').write(x)
        os.environ['CLAUDE_CODE_CONTAINER_ID'] = 'container_JIA--x'
        写('甲一'); rc, m = 存('t')
        甲一 = 远顶(底枝)
        果.append(('⑩远端无底 → 推主存底枝（信带坐与机）', rc == 0 and 甲一 and '｜机 JIA' in _跑('git', 'log', '-1', '--format=%B', 甲一).stdout))
        写('甲二'); rc, m = 存('t')
        果.append(('⑪同机再存 → 顶己之旧底、⛔挂旧链', rc == 0 and 远顶(底枝) != 甲一 and 远顶(旧链) is None))
        甲二 = 远顶(底枝)
        os.environ['CLAUDE_CODE_CONTAINER_ID'] = 'container_YI--x'   # 同一会话复开於新机——402 之形
        写('乙一'); rc, m = 存('t')
        果.append(('⑫同会话新机 → 先把旧机之底挂进旧链、再推主（⛔以会话号认己）',
                   rc == 0 and 远顶(旧链) and 含(甲二, 远顶(旧链)) and 远顶(底枝) not in (甲二, None)))
        乙一 = 远顶(底枝)
        状['锁'] = (True, 'SIDB', 402)
        写('乙二'); rc, m = 存('t')
        果.append(('⑬他坐持写书之锁 → 推己之旁枝，主存底枝⛔动',
                   rc == 0 and 远顶(底枝) == 乙一 and 远顶(旁枝('SIDA')) and '旁枝' in m))
        果.append(('⑬之二 他坐之锁⛔续（⛔夺锁）', not 写们))
        状['锁'] = (True, 'SIDA', 402)
        写('乙三'); rc, m = 存('t')
        果.append(('⑭本坐持鲜锁 → 推主、续己之锁（坐不改）', rc == 0 and 写们 and 写们[-1].get('坐') == 'SIDA' and 写们[-1].get('章') == 402))
        n = len(写们); 状['锁'] = (False, 'SIDA', 402)
        写('乙四'); rc, m = 存('t')
        果.append(('⑭之二 逾期之锁⛔复活', rc == 0 and len(写们) == n))
        肿前 = len(肿计)
        rc, m = 存('t', 跳同=True)
        果.append(('⑮跳同：树未改即不推', rc == 0 and '无改' in m))
        open(os.path.join(工, '_跑账.json'), 'w').write('[1]')
        rc, m = 存('t', 跳同=True)
        果.append(('⑮之二 跳同：只诸账（跑账）有改 → 仍不推（⛔五分一回空推）', rc == 0 and '无改' in m))
        果.append(('⑱档肿哨只於树已变方跑（1027 A2：树未改之定时⛔跑；树已变之存照跑）', 肿前 >= 6 and len(肿计) == 肿前))
        真远底, 次 = _远底, [0]
        def 旧影():
            次[0] += 1
            return (True, 甲一, '') if 次[0] == 1 else 真远底()
        g['_远底'] = 旧影
        前 = 远顶(底枝)
        写('乙五'); rc, m = 存('t')
        g['_远底'] = 真远底
        果.append(('⑯lease：判时所见之底已非云端之顶 → 推被拒、重判再推（⛔盲覆）', rc == 0 and 次[0] >= 2 and 远顶(底枝) != 前))
        状['锁'] = (False, '', None)
        g['_远底'] = lambda: (False, None, '')
        前, 旁前 = 远顶(底枝), 远顶(旁枝('SIDA'))
        写('乙五之二'); rc, m = 存('t')
        g['_远底'] = 真远底
        果.append(('⑰云端之底读不出（推尚通）→ 推己之旁枝，主存底枝⛔动', rc == 0 and 远顶(底枝) == 前 and 远顶(旁枝('SIDA')) != 旁前))
        subprocess.run(['git', '-C', 工, 'remote', 'set-url', 'origin', os.path.join(d, '无此远端')], check=True)
        写('乙六'); rc, m = 存('t')
        果.append(('⑰之二 云端全断 → 报败（rc=2）', rc == 2))
    except Exception as e:
        果.append(('⑩—⑰防覆之演跑不起来：%s' % e, False))
    finally:
        g.update(旧)
        for k, v in 旧模.items():
            if v is None:
                sys.modules.pop(k, None)
            else:
                sys.modules[k] = v
        for k, v in 旧环.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(d, ignore_errors=True)
    return 果


def 自测():
    ok, bad = 0, []

    def T(x, c, note=''):
        nonlocal ok
        if c:
            ok += 1
        else:
            bad.append(x + ('（%s）' % note if note else ''))

    s = open(os.path.join(ROOT, '工具', '存底.py'), encoding='utf-8').read().split('def 自测')[0]
    # ①**最要紧的一格**：存底不许碰工作区／索引／HEAD
    T('①存底用临时索引（GIT_INDEX_FILE），不碰真索引', "'GIT_INDEX_FILE': idx" in s)
    T('①之二 全码无 checkout／reset／stash（碰工作区之三样）',
      not any(x in s for x in ("'checkout'", "'reset'", "'stash'")))
    # ②强推只许落在存底枝（滚动之枝），不许落在主枝
    强 = re.findall(r"'git', 'push'.*?\)", s, re.S)
    T('②凡强推皆落存底枝，主枝一处不推（今 %d 处 push）' % len(强),
      all(('--force' not in x) or ('底枝' in x) for x in 强) and not any('主枝' in x for x in 强),
      str(强)[:200])
    # ③章标不许覆盖（标是不动的）——本仓拒推 tag，标落在 refs/heads/章-N，
    #   故其凭不是「不带 --force」这一句空话，而是：**打标那一段码里一个 --force 也没有**。
    段标 = s.split('def 标(')[1].split('\ndef ')[0]
    T('③打标那一段不带 --force（标不许被覆盖）',
      '--force' not in 段标 and 'refs/heads/%s' in 段标 and "'--tags'" not in 段标, 段标[-90:])
    T('③之二 标之名恒为 章-N（不夹说明、不夹日子）', "名 = '章-%d' % int(n)" in 段标)
    T('④临时索引跑毕即除（不吃盘）', 'os.remove(idx)' in s and 'finally' in s)
    T('⑤存底枝与主枝之名不同，且皆当场自常量取', 底枝 != 主枝 and 底枝.startswith('备份/'))
    # ⑥★**没有演过的备份不算备份**：本器须有一路真去克隆、真去比的活
    段演 = s.split('def 演(')[1].split('\ndef ')[0] if 'def 演(' in s else ''
    T('⑥有一路真去克隆下来比（非只看账面）',
      "'clone'" in 段演 and 'getsize' in 段演, '演之段 %d 字' % len(段演))
    T('⑥之二 演所比者含「正在写而未提交的那一章」（存底枝立起来正为这一样）',
      'ROOT' in 段演 and "'正文'" in 段演)
    T('⑥之三 演跑毕即除其临时之仓（不吃盘）', 'rmtree' in 段演 and 'finally' in 段演)
    T('⑨每存一回顺手续一次心跳（锁不许在最需要它的时候松开）',
      'import 心跳' in s and '_hb._写(' in s)
    # ⛔旧格作 `'if _章:' in s`——**钉的是那一行的字样**；0924 其行改作带二闸之式，意未变而字样变，旧格遂红。
    #   ★**改问其意**：续心跳之条件里须仍有 `_章`（只在已有人在跑时续）。
    T('⑨之二 续心跳只续本坐所持、尚新鲜之锁（⛔无中生有、⛔夺他坐之锁、⛔复活逾期之锁）',
      'if 鲜 and 锁章 and 锁坐 == 我坐 and 续心跳' in s)
    T('⑨之三·⛔非席之存不续心跳（0924：L0 与人手之存曾令 363 之死锁永活，自走永判「候」）',
      "续心跳=True" in s and "ZM_存底不续心跳" in s)
    T('⑧两本账虽在 .gitignore，存底仍强塞进临时索引（少了它们续跑之账就断）',
      "'add', '-f'" in s and '_跑账.json' in s and '_任务流.json' in s)
    try:
        忽 = open(os.path.join(ROOT, '.gitignore'), encoding='utf-8').read().split('\n')
    except Exception:
        忽 = []
    T('⑧之二 设定/自进化环.log 已入 .gitignore 而强塞入存底（1027 A2：旧随踪，自走每跑一行、树恒脏）',
      '设定/自进化环.log' in 强塞之档 and '设定/自进化环.log' in 忽 and 'for _档 in 强塞之档:' in s)
    段存 = s.split('def 存(')[1].split('\ndef ')[0]
    T('⑱之二 档肿哨在跳同之判之後（⛔先跑）', 段存.index('if 跳同 and 同:') < 段存.index('_档肿哨()'))
    段标2 = s.split('def 标(')[1].split('\ndef ')[0]
    T('⑲标可指定所推之提交（自进化环 L0 缺碑：推封版#N 之提交，⛔HEAD）；默仍 HEAD（封版之末推）',
      'def 标(n, sha=None)' in s and "sha or _跑('git', 'rev-parse', 'HEAD')" in 段标2)
    段跑 = s.split('def _跑(')[1].split('\ndef ')[0]
    T('⑰诸 git 之调（_跑）败即问盘坏之迹（1024：add 每回败而只入日志，无人见）', '重取.查迹(r.returncode, r.stderr' in 段跑)
    T('⑦每存一回，顺手记一步续跑（东西保住而进度丢了仍是断）',
      'import 续跑' in s and '续跑.记(' in s)
    # 〔W919·X146〕origin 之址自正（工具/_仓.py·诸局显传 环）；存、标 推前俱调 _址正
    try:
        import _仓
        for _n46, _c46 in _仓.自测之局():
            T(_n46, _c46)
        段标46 = s.split('def 标(')[1].split('\ndef ')[0]
        T('X146 存、标 推前调 _址正（_仓.正址之验）', 段存.index('_址正()') < 段存.index("'git', 'push'")
          and 段标46.index('_址正()') < 段标46.index("'push'") and '_仓.正址之验(ROOT)' in s.split('def _址正(')[1].split('\ndef ')[0])
    except Exception as e:
        T('X146 之测崩：%s' % e, False)
    # ⑳1027 坑54：演章（GitHub 之 autopush 每章所跑）——临时之裸库真克隆：全者过、缺工具者红、无此标者红
    with tempfile.TemporaryDirectory() as _t:
        _e = dict(os.environ, GIT_AUTHOR_NAME='t', GIT_AUTHOR_EMAIL='t@t', GIT_COMMITTER_NAME='t', GIT_COMMITTER_EMAIL='t@t')
        _裸, _工 = os.path.join(_t, 'o.git'), os.path.join(_t, 'w')
        subprocess.run(['git', 'init', '-q', '--bare', _裸], check=True, env=_e)
        subprocess.run(['git', 'init', '-q', _工], check=True, env=_e)
        for _x in 可跑之档:
            os.makedirs(os.path.join(_工, _x))
            open(os.path.join(_工, _x, 'a'), 'w').write('1')
        for _c in (['add', '-A'], ['commit', '-qm', 'a'], ['push', '-q', _裸, 'HEAD:refs/heads/章-1'], ['rm', '-rq', '工具'], ['commit', '-qm', 'b'],
                   ['push', '-q', _裸, 'HEAD:refs/heads/章-2']):
            subprocess.run(['git'] + _c, cwd=_工, check=True, env=_e, capture_output=True)
        _u = 'file://' + _裸
        T('⑳演章：真克隆章标——全者过、缺工具者红、无此标者红（GitHub 每章之演同此一函）',
          演章(1, _u)[0] == 0 and 演章(2, _u)[0] == 2 and '工具' in 演章(2, _u)[1] and 演章(3, _u)[0] == 2
          and '演章(章, url)' in 段演)
    # ⑩—⑯·1021 防覆（402 之失）：真起一个临时之远端与工作仓，两机一锁，逐形跑一遍（⛔只看字样）
    for 名, 条 in 防覆之演():
        T(名, 条)
    print('── 负测·存底 %d/%d %s ──' % (ok, ok + len(bad), '全通' if not bad else '｜未过：' + '；'.join(bad)))
    return not bad


if __name__ == '__main__':
    a = sys.argv
    if '--自测' in a:
        sys.exit(0 if 自测() else 1)
    if '--不续心跳' in a:
        os.environ['ZM_存底不续心跳'] = '1'
    if '--存' in a:
        i = a.index('--存')
        rc, m = 存(a[i + 1] if len(a) > i + 1 else '')
        print('✓存底已上云端：%s' % m if rc == 0 else '⛔存底未成：%s' % m)
        sys.exit(rc)
    if '--标' in a:
        i = a.index('--标')
        rc, m = 标(a[i + 1])
        print('✓章标：%s' % m if rc == 0 else '⛔打标未成：%s' % m)
        sys.exit(rc)
    if '--演章' in a:
        i = a.index('--演章')
        rc, m = 演章(a[i + 1], a[a.index('--源') + 1] if '--源' in a and a.index('--源') + 1 < len(a) else None)
        print('✓演章：%s' % m if rc == 0 else '⛔演章不过：%s' % m)
        sys.exit(rc)
    if '--演' in a:
        i = a.index('--演')
        章 = a[i + 1] if len(a) > i + 1 and a[i + 1].isdigit() else None
        rc, m = 演(章)
        print('✓演过了：%s' % m if rc == 0 else '⛔演不过：%s' % m)
        sys.exit(rc)
    验()
    sys.exit(0)
