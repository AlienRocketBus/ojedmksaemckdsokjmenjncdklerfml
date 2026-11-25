#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""自走（2026-09-13 立·作者当面点名：「**设置个机制，跑起来就必须得跑起来，不能再停下了**」）。

★立此器之由，一句话：**链条断在人身上，不是断在器上。**
　**盘上诸器各守一样，而没有一样东西回答那个最要紧的问**：**此刻这一坐该干哪一件。**
　⛔**於是每一回都要一个人把七八样印看一遍、自己拼出下一步**——**而人会停，器不会。**

★★**本器只答一句话**：**下一件是什么，那一条命令逐字怎么写。**
　⛔**它不判小说、不改一个字、不动任何账**——**只读盘，只印一行。**
　★**其序写死（先来后到，头一件成立即印它，不往下看）**：
　　①**有人在跑** → 不许抢锁：印「候」，并印它跑到哪一段。
　　②**末章未封版**（回执不在）→ 印「接着跑那一章」。
　　③**末章封版而其第十一轮未过** → 印「补跑第十一轮」，不过者照其报治（`十一轮不过之治`；一代救章席 1020 已汰·X29）。
　　③之二 **末章已封而未入主枝**（1027 A2·死锁之治）→ 其 GitHub 之报红／拒／败或缺章标即印「治」，报未毕即印「候」——⛔起下一章。
　　④**逾期之欠压在下一章头上** → 印它，并把它写进下一章之卡。
　　⑤**以上皆清** → 印「起下一章」，并把三条前置之命令一并印出。
　★★**其末一行永远是一条可以照抄去跑的命令**——⛔**不许印「你可以考虑」这种话。**

用法：
    python3 工具/自走.py            # 印下一件
    python3 工具/自走.py --自测
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账
except Exception:
    pass
import glob
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
主枝 = 'claude/the-novel-review-4dtuit'   # 与 推报.主枝、存底.主枝 同（自测对之·⛔两把尺）——残树恒⛔计之（1117·法用#停钩空转：泊於章-N 时主枝亦「已并」）
CN = {'零': 0, '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4,
      '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}


def _num(s):
    tot, cur = 0, 0
    for ch in s:
        if ch in CN:
            cur = CN[ch]
        elif ch == '十':
            tot += (cur or 1) * 10
            cur = 0
        elif ch == '百':
            tot += (cur or 1) * 100
            cur = 0
        elif ch == '千':
            tot += (cur or 1) * 1000
            cur = 0
    return tot + cur


def 末章():
    ns = []
    for f in glob.glob(os.path.join(ROOT, '正文', '*.md')):
        m = re.search(r'第([零〇一二三四五六七八九十百千]+)章', os.path.basename(f))
        if m:
            ns.append(_num(m.group(1)))
    return max(ns) if ns else 0


def 有人在跑():
    """返回 (在跑?, 第几章, 停了几分钟)。⛔其限之数自 心跳.py 现取，不写死。
    1022（复核所逮）：①先取云端之锁——新机无本地之 `_心跳.json`（.gitignore），旧判「无人」→ 两坐同写；
    ②锁为本坐所持⛔作「他人在跑」——旧印「候」，持锁者遂闲（402 封後书停五时半之同族）。"""
    d, 我 = None, ''
    try:
        sys.path.insert(0, os.path.join(ROOT, '工具'))
        import 心跳 as _hb
        在, d = _hb._远()
        d = d if (在 and isinstance(d, dict)) else None
        我 = _hb.坐()
    except Exception:
        d = None
    if d is None:
        p = os.path.join(ROOT, '_心跳.json')
        if not os.path.exists(p):
            return False, None, None
        try:
            d = json.load(io.open(p, encoding='utf-8'))
        except Exception:
            return True, None, None          # 读不出，作有人论（宁可候，不可抢）
    if d.get('章') is None:
        return False, None, None         # 已撤锁
    if 我 and 我 != '未名' and str(d.get('坐') or '') == 我:
        return False, d.get('章'), None  # 己锁：⛔作他人在跑
    s = io.open(os.path.join(ROOT, '工具', '心跳.py'), encoding='utf-8').read()
    m = re.search(r'^限\s*=\s*(\d+)\s*\*\s*60', s, re.M)
    lim = int(m.group(1)) * 60 if m else 45 * 60
    age = int(time.time()) - int(d.get('时', 0))
    return (age <= lim), d.get('章'), age // 60


def 回执在(n):
    """★那一章交了回执没有。⛔**认三种，不只认「作业单」那一种。**

    ⛔★★★★★2026-09-23·限359（第358章封版之日当场所逮·**本日最险之一处**）：
      ★**旧式死认档名以「第N章作业单.md」收**——**而第358章两份回执叫
        `回执_20260923_第358章封版席.md` 与 `…案席.md`，无「作业单」三字。**
      ⛔**於是本器判「第358章正文在盘而回执不在——那一章没走完」，
        并印出「`Workflow({…, args:{章:358}})`」——叫人把一章已封版的书从头再跑一遍。**
      ★★**而 358 之封版席回执，比一份作业单更是「走完了」之凭**：
        **作业单係半路所交，封版席係末段所交。**⛔**本器却只认那半路的一种。**
      ★★★**逐章亲数其形**（354—358）：
        **354 只有作业单｜355、356 作业单＋封版席｜357 三种俱全｜358 案席＋封版席（无作业单）**——
        **三种回执，各席按其所走之段落各交各的，⛔而本器只认其中一种。**
      ⛔**故认三种**：**作业单／案席／封版席，有其一即算交了。**
      ★**此係本日第二把栽在同一个形上的器**（前一把係 `换型令::封了版`，只看 `版本/第N章/` 一处）——
        **其共形：一份文书有两三种归处或名目，而器只认其中一种，於是一件办过的事在它眼里没办。**

    ⛔★1118（总编辑裁·同功两处即废劣者）：**本函旧为回执之判之又一副本**——仍认三名（案席 0924 已於 接力／十一轮哨 收回、本函漏收），
      ⛔问 段.封版：记料先立「第N章封版席」之骨（X109·N≥460），记席之中即判「回执在」→【判】补（教跑 --十一轮 於未封之章）；
      封版 --後 红於第十一轮之後（`_十一轮.json` 已在、段.封版 仍「待」）即越过跑、补（真盘之演判起第N+1章·363 之形；沙盘无後章之料、止於庭）。
      ★今⛔另判：即 `接力.有回执`（十一轮哨 同调 接力.封版之段·一处判）——作业单／封版席，N≥368 兼认 段.封版 係 封版.py 所书。
      320—466 诸封章新旧之判逐章同（无一章只有其骨）；自测 ㉗之e—g 沙盘守之。
    """
    import 接力
    return 接力.有回执(n)


def 十一轮过(n):
    return os.path.exists(os.path.join(ROOT, '版本', '第%d章' % n, '_十一轮.json'))


def 卡在(n):
    return os.path.exists(os.path.join(ROOT, '版本', '第%d章' % n, '_开镜卡.md'))


def 逾期之欠(n):
    """到期章 ≤ n 而状态仍 open 者。"""
    p = os.path.join(ROOT, '设定', '到期账.json')
    if not os.path.exists(p):
        return []
    try:
        d = json.load(io.open(p, encoding='utf-8'))
    except Exception:
        return []
    out = []
    for x in d.get('items', []):
        if str(x.get('状态', '')).lower() != 'open':
            continue
        due = x.get('到期章')
        if isinstance(due, int) and due <= n:
            out.append((x.get('id'), due, str(x.get('事', ''))[:46]))
    return sorted(out, key=lambda y: y[1])


def 候时之活():
    """★2026-09-13 立：印「候」之时，顺手把盘上现成的真活点出来。

    ⛔**其由**：律⑪写着「候不是停，手上须同时办另一件真活」，
    **而它从来没说是哪一件**——**於是每一回候，都要现想一件**；
    ★**现想出来的那一件，十有八九是「我看了什么」而不是「我改了什么」**（律⑫：报告不是交付）。
    ★★**故本器不再只印那一句令，改印盘上此刻真红的那几样**——**逐条带其命令。**
    ⛔**本器只印，不办；一个字也不写盘。**
    """
    out = ['  ── 候时可办之真活（盘上现成，⛔挑一件真办掉，不是看一眼）──']
    n = 0
    # 一·到期账：限已到或将到而未清者（⛔数「不在已清词表之内者」，非只数 open·体检账 ㊨）
    try:
        import json as _j
        清 = ('done', 'closed', 'half', '废弃', 'cold', '冷藏', '已清', '清')
        d = _j.load(io.open(os.path.join(ROOT, '设定', '到期账.json'),
                            encoding='utf-8'))
        末 = 末章()
        欠 = [x for x in d.get('items', [])
              if x.get('状态') not in 清
              and isinstance(x.get('到期章'), int)
              and x['到期章'] <= 末 + 2]
        for x in 欠[:4]:
            n += 1
            out.append('  %d. 到期账 %s（限%s）：%s'
                       % (n, x.get('id'), x.get('到期章'), (x.get('事') or '')[:46]))
    except Exception:
        pass
    # ★1013 删「跑一回 书级体检／跑账／净重对表／FS闸 看它红没红」四条（效之律·坑㉔）：
    #   那四器全测俱跑（推时 pre-push 零 token 自跑）；叫主环候时去跑，是花模型之回数办机器之活——
    #   主环每多一回都重读整份上下文（机械账 1013：主会话非写作之活占 71%）。
    if not n:
        out.append('  （盘上无到期之欠——⛔为候而找活、⛔看进度：结束本回合，席毕与推毕自有通知，零 token。）')
    else:
        out.append('  ★办毕须落到盘上（`git log` 多一笔），⛔否则这一回合等於没有（律⑫）。')
    return out


def 本章有跑(n, root=None, 来=None):
    """〔W919 落地之查·病一〕N≥拒後自（承.拒後自）：第 n 章之 _席之因.json 在、或诸 journal 有属本章之 Run → True。崩只 ⚠ 而 False（照新派·续跑之守 仍守）。
    来(n) → 诸 journal（自测注之）。"""
    try:
        import 承
        if n < 承.拒後自:
            return False
        if os.path.exists(承.席之因档(n, root or ROOT)):
            return True
        return bool((来 or (lambda k: 承.收(k, glob.glob(承.诸journal之式), root=root or ROOT, 界=0)[1]))(n))
    except Exception as e:
        print('  ⚠ 自走·本章有跑 判不出（%s）——照新派之令（续跑之守 仍判首派之拒席）' % type(e).__name__)
        return False


def 派令(n, root=None, 厚=None):
    """→ 派第 n 章之命令行们（1013）：段案有其节（重、魂路俱在）→ 造式二代（造章.js，args 取自段案）；否则一代（一章.js）。
    ⛔其由：二代起於 381，而本器仍印 一章.js——照抄即以一代之法写二代之章（费约五倍）。
    ★1020 X40（瑕疵总账·裁_1020_推闸二红_399封版後）：n≥401 而 `分量闸.须厚` 判「非厚不可」者，args 添 须厚:true 并印其由——
      ⛔399 之「非厚不可」只写进开镜卡，执笔七席照段案之带写成 2303—2461，推闸红；今其判随令下到执笔与选席（造章.js）。
      厚：(须, 语) 可直传（自测用）；缺则以 造式验.须厚之判 现算（与推闸同尺）。⛔N≤400 一字不判、不印。"""
    import 章料
    t = 章料.段案行(n, root or ROOT)
    重 = re.search(r'^- 重：(\S+)', t, re.M)
    路 = re.search(r'^- 魂路：(.+)$', t, re.M)
    if 重 and 路 and 重.group(1) in ('轻', '中', '重'):
        路们 = [x.strip() for x in 路.group(1).split('｜') if x.strip()]
        import 造式验                                          # 须厚起与其判俱取 造式验（⛔另抄一把）
        须, 须语 = (False, '')
        if n >= 造式验.须厚起:
            须, 须语 = 厚 if 厚 is not None else 造式验.须厚之判(n)
        由 = ['  # ' + x.strip().replace('**', '') for x in 须语.split('\n') if x.strip()]
        # ★1119 X119：n≥471 本章之带唯段案「字数：a—b」为准，传 args.带（造章.js 执笔令【厚】照之）；段案无其带即⛔派、先补
        带 = 章料.段案之带(n, root or ROOT) if n >= 471 else ''
        if n >= 471 and not 带:
            return ['  # ⛔第%d章段案之节无「字数：a—b」——本章之带唯段案为准（X119），先补段案之字数再派' % n,
                    '  python3 工具/段案验.py   # 补 设定/段案 第%d章之「守」末「字数：a—b」，验过再跑本器' % n]
        # ★1017 承（397 一章两回容器重启）：本章已有起草之稿 → 先收已成之段（⛔重派已交之执笔）
        # 〔W919 落地之查·病一〕N≥拒後自：盘上无稿而本章有前 Run（journal）或 _席之因.json 者亦走承之路——新派即以原令首派前 Run 之拒席（同令再请）
        if n > 末章() and (glob.glob(os.path.join(root or ROOT, '版本', '第%d章' % n, '起草_稿*.md')) or 本章有跑(n, root)):
            return ['  # 第%d章已有起草之稿或前 Run（容器重启所余？）——先收诸 journal 已成之段并分因，⛔重派已交之席、⛔同令再请拒席' % n,
                    "  python3 工具/承.py %d --重 %s --魂路 %s" % (n, 重.group(1), ','.join(路们))] + ([
                    '  # ★本章须厚（分量闸·须厚）：承.py 之包裹自带 须厚（旧 _承.json 承之、无则照 造式验.须厚之判 现算·X40）——跑後验 _承.js 之 args 有 "须厚": true'
                    ] + 由 if 须 is True else []) + [
                    "  Workflow({scriptPath:'%s'})   # 承.py 所写之包裹（补自带：缺席之执笔造章自判补否）；⛔resumeFromRunId 直续（坑㊻·续跑之守拦）" % os.path.join(
                        root or ROOT, '版本', '第%d章' % n, '_承.js')]
        return ['  python3 工具/章料.py %d && python3 工具/造式验.py %d --料   # 料全方派' % (n, n),
                '  # 开工之闸：设定/方案/W<k>.md 逐环确证 ＋ python3 工具/工作流账.py --开 W<k>（法典二之七步）'] + (
                # 〔1119 死规之审·gates6/docs7〕N≥473（造式验._死规审自）：须厚只报——造章.js 执笔令【须厚·参考】、选令只报，造式验 --料 未可判亦只 ⚠：注随之，⛔再言硬项、⛔先治再派
                (['  # ⚠须厚（X40·只报·1119 死规之审）：args 添 须厚:true——执笔令【须厚·参考】、选令只报（⛔作底须写由、⛔交总编辑·造章.js）；其由：'] + 由
                 if n >= 造式验._死规审自 else
                 ['  # ★须厚（X40）：args 添 须厚:true——执笔令硬项「本章之事须担得起 2,900」、选令「须厚之章之底」（造章.js）；其由：'] + 由)
                if 须 is True else [('  # ⚠须厚未可判（%s）——只报（1119 死规之审）' if n >= 造式验._死规审自 else '  # ⛔须厚未可判（%s）——先治其由再派') % 须语.lstrip('★')]
                if 须 is None else []) + [
                "  Workflow({scriptPath:'工具/席/造章.js', args:{章:%d, 重:'%s', 魂路:[%s]%s%s}})" % (
                    n, 重.group(1), ', '.join("'%s'" % x for x in 路们), ', 须厚:true' if 须 is True else '',
                    ", 带:'%s'" % 带 if 带 else '')]
    # ★1017 淘汰之律：一代 一章.js 已淘汰（二代 造章.js 自 381 起、费约五分之一）——无段案之章⛔派一代，先立段案
    return ['  # 第%d章无段案之节（重、魂路）——一代 一章.js 已淘汰（1017 作者铁律·淘汰之律）；先立段案再派二代' % n,
            '  python3 工具/段案验.py   # 立 设定/段案/<起>-<止>.md 之第%d章之节（重：轻／中／重；魂路：三路），验过再跑本器' % n]


def 锁滞(ch):
    """★2026-09-16 立：**席已办毕而锁未撤**——问 `_任务流.json` 之末笔，不问心跳。

    ⛔**其所由来·0916 之实**：335 之席十一段全走完（工作流回了结果，`封版席毕` 一笔已落
    `_任务流.json`），⛔**而 `心跳.py --收 335` 那一步不在 `一章.js` 的收口段里**——
    **於是锁原样挂着，`自走.py` 照旧印「候」，而其实那一席早就没了。**
    ★**其价**：本坐候了七分钟才自己想起去看 `续跑`；**若无人看，它要挂满 45 分钟才自动过期**——
    **一章之间白丢三刻钟，而律⑰正是为「席一收，头一件事是派下一席」而立的。**
    ⛔**本器不改 `一章.js`**（那是收口段之事，交工具席）——**它只保证这三刻钟不再白丢。**
    """
    try:
        d = json.load(io.open(os.path.join(ROOT, '_任务流.json'), encoding='utf-8'))
    except Exception:
        return False                 # 读不出即作「席还在」论（宁可候，不可抢）
    心跳时 = None
    try:
        h = json.load(io.open(os.path.join(ROOT, '_心跳.json'), encoding='utf-8'))
        心跳时 = int(h.get('时')) if h.get('时') else None
    except Exception:
        pass
    return 判锁滞(d.get('步') or [], ch, 心跳时)


def 云端已封(n):
    """云端有「章-n」之标否（封版即打、⛔动）。读不出作否（⛔因网断而停书）。"""
    try:
        r = subprocess.run(['git', 'ls-remote', 'origin', 'refs/heads/章-%d' % int(n)], cwd=ROOT,
                           capture_output=True, text=True, timeout=30)
        return r.returncode == 0 and bool(r.stdout.strip())
    except Exception:
        return False


def 本树已封(n):
    """本树（HEAD 之史）有第 n 章封版之提交否（取 封版.封之笔——同一把尺；零网）。"""
    try:
        import 封版
        return bool(封版.封之笔(n, ROOT, ['HEAD']))
    except Exception:
        return False


def 前章之治(末, 封=None, 主=None, 坏=None, 本封=None):
    """★1027 A2·死锁之治：末章已封（本树有其封版之提交）而未入主枝 → (判, 诸行)；余（未封、已在主、读不出）→ None。
    ①云端有「章-末」而其报红／拒／败 → 【判】治（印其红与治之令：逐红治、提交、推.py 交治枝；拒即 --直）；
    ②有「章-末」而报未毕 → 【判】候（接棒守 --候主 末）；③无「章-末」→ 【判】治（自进化环 L0 缺碑自补：推封版#末之提交为章-末）。
    ⛔起下一章：新会话自主枝起，主枝无末章即见不到它（【重派】之会话自章-末起，首务在此——接棒守.派之参 治形）。"""
    try:
        if not (本封 or 本树已封)(末):
            return None
        import 接棒守
        有标 = (封 or 云端已封)(末)
        if 有标 and (主 or 接棒守.主含)(末):
            return None
        L = []
        if not 有标:
            L.append('  【判】治。第%d章已封（本树有封版#%d 之提交）而云端无「章-%d」——封版之末推未成（坐死於推前？）；⛔起第%d章。' % (末, 末, 末, 末 + 1))
            L.append('  → 本器头之自进化环 L0 缺碑自补（推封版#%d 之提交为「章-%d」·即触 GitHub autopush）；见其「补碑」之行，未补即 `python3 工具/自进化环.py`' % (末, 末))
            L.append('  ── 下一条命令 ──')
            L.append('  python3 工具/接棒守.py --候主 %d      # run_in_background·零 token；坏报即返其红，照其行治' % 末)
            return '治', L
        源 = (坏 or 接棒守.坏报之源)(末)
        if not 源:
            L.append('  【判】候。第%d章之「章-%d」已推、主枝未含、亦无其坏报（GitHub 未毕）——⛔起第%d章（新会话自主枝起，见不到第%d章）。' % (末, 末, 末 + 1, 末))
            L.append('  ── 下一条命令 ──')
            L.append('  python3 工具/接棒守.py --候主 %d      # run_in_background·零 token' % 末)
            return '候', L
        import 推报
        d = 源[1]
        L.append('  【判】治。第%d章之 GitHub 推闸报「%s」（%s）——先治之；主枝含第%d章後方起第%d章：' % (末, d.get('果'), 源[0], 末, 末 + 1))
        L.extend('  ' + x for x in 推报.报之语(d))
        L.append('  ⛔绕、⛔弱化：读者可见之闸红即逐条治、提交（器红只报，入器红账限三章）')
        L.append('  ── 下一条命令 ──')
        if d.get('果') == '拒':
            L.append('  python3 工具/推.py --直      # 拒（改 .github/workflows，GITHUB_TOKEN 推不得）：审计之兜底·本地全闸')
        else:
            L.append('  python3 工具/推.py      # 治毕提交之後：交 GitHub（「治-<sha>」），照其所印 `推.py --候 <sha>` 後台零 token 候；败而 GitHub 停摆方 --直')
        return '治', L
    except Exception:
        return None


def 判锁滞(步, ch, 心跳时=None):
    """⛔纯判·不碰盘——**自测拿它跑假料，不拿今日之实去钉**（㊸：一张快照钉进一条常令）。

    ★**2026-09-16 补·第二问：那把锁是「没人撤」还是「有人又按上去了」。**
    ⛔**其所由来·当日之实**：337 封版毕、其席自己撤了锁；**本坐随即把锁按回 337**——
      **为的是不叫每小时那几坐在「大审庭」开着的时候把 338 派出去**（两席同盘，正是律⑮要挡的）。
      **而本器只看末笔，遂照旧印「起·已办毕而锁未撤」**——
      ★**若那一刻真有一坐照它跑，它会去撤我按上的锁，当场把 338 派出来。**
    ★★**其判之据在时刻**：**心跳之时若晚於那一步之时，那把锁就不是「忘了撤」，是「有人特意按上的」。**
    ⛔**取不着时刻者，退回只看末笔之旧判**（宁可多印一回「起」，不可把一条判据凭空造出来）。
    """
    for 笔 in reversed(步):
        事 = str(笔.get('事') or '')
        if 事.startswith('存底'):     # 存底流水不算段
            continue
        if not 事.startswith('%s·封版席毕' % ch):
            return False
        if 心跳时 is None:
            return True               # ⛔取不着时刻：退回旧判
        步时 = _步之时(笔)
        if 步时 is None:
            return True
        return not (心跳时 > 步时)    # ★心跳晚於那一步＝有人特意按上的，不是忘了撤
    return False


def _步之时(笔):
    """⛔把续跑之「时」（`%Y-%m-%d %H:%M:%S`·UTC）读成秒；读不出即 None。"""
    import calendar
    t = str((笔 or {}).get('时') or '').strip()
    try:
        return calendar.timegm(time.strptime(t, '%Y-%m-%d %H:%M:%S'))
    except Exception:
        return None


# ★1020 X29（淘汰之律）：一代救章席（深掘三路＋无伤席十轮之审改）已彻删——造式之章（381 起）作者 1008 令⛔审改之轮，
#   而本器三判（锁滞之救／补／救）仍印其令，照它派即违 1008 令。今第十一轮不过之治照造式之法（原载一代令封版席第6—7件），
#   三判同印此数行，⛔另写一份。
十一轮不过之治 = [
    '  ★第十一轮不过，照其报治（造式·作者 1008 令⛔审改之轮）：',
    '    · 左眼（造式之实）缺哪一席之档 → 交主环派那一席补（⛔代写他席之判、⛔以审改之轮补）；',
    '    · 右眼照其项治（入圣经册、判到期账、立下一章之锚、推 open_brief……）；',
    '    ⛔不补假轮｜⛔不写假 `_十一轮.json`｜⛔不改闸自赦。',
]


def 十一轮之凭(ch):
    """★2026-09-16 立：**问一句「那一庭留下走过的凭据没有」。**

    ⛔**其所由来·0916 本坐自己报错了一句话**：本坐验过封版五件（回执／锁定行／
      下一章开镜卡／封版之锚／正文），即对作者报「第336章已封版」——**五件确係俱在**，
      **而 336 之第十一轮当日两跑两不过，`版本/第336章/_十一轮.json` 至今不在。**
    ★**那一席自己把这一条写在回执里交上来了**：
      「**这一章在册上写着『已封版』，而它那一庭从来没有走过。**」
      ⛔**而本器印「起」、本坐照着派下一章，等於把那一席亲手贴回去的欠条又替它撕了一回。**
    ★★**故本器自今日起，撤锁之後不许直接派下一章**：
      **先问这一份凭在不在；不在者，下一条命令是补走那一庭（`--十一轮`），不是新章。**
    ⛔**而它不拦撤锁**——**席已经没了，锁还是要撤的**；**它拦的是「接着往前叠」。**
    """
    try:
        n = int(str(ch))
    except Exception:
        return True                  # 判不出章号即不拦（宁可放行，不可乱拦）
    return os.path.exists(os.path.join(ROOT, '版本', '第%d章' % n, '_十一轮.json'))


def 孤钩之(起, 止, root=None, 诸=None):
    """★1017：大审之孤钩——到期账诸笔，其「裁」末一处「交（第）N（章）大审」之 N 在 起—止、而状态未清（⛔done／closed／清）者。
    交 大审.js 之 args.孤钩（[{id, 注}]）；⛔大审.js 默认（缺参即 throw）。
    ★验四之治：①「清」亦已清（负测_到期账词表之六态）；②读档不成即 raise（⛔返回 [] 而令照印——四笔无人判而器不出声）；
    ③取「裁」中末一处（「交 397 大审；…改交 407 大审」归 407）；④注先取「事」中「下一层为「…」」（已付其半者之余半），否则取其首句；
    ⑤诸 可直传（自测用，⛔写档）。"""
    if 诸 is None:
        with open(os.path.join(root or ROOT, '设定', '到期账.json'), encoding='utf-8') as f:
            诸 = json.load(f)['items']
    出 = []
    for x in 诸:
        ms = re.findall(r'交\s*(?:第\s*)?(\d+)\s*(?:章\s*)?(?:之\s*)?大审', str(x.get('裁', '')))
        if not ms or not (起 <= int(ms[-1]) <= 止) or x.get('状态') in ('done', 'closed', '清'):
            continue
        事 = str(x.get('事', ''))
        m = re.findall(r'下一层[为是]「([^」]+)」', 事)
        注 = m[-1] if m else re.sub(r'[★（(].*$', '', 事).strip()[:30]
        出.append({'id': x.get('id', ''), '注': 注})
    return 出


def 欠十一轮之章():
    """★2026-09-16 立：**往回数一遍，有没有哪一章「册上写着已封版，而那一庭没走过」。**

    ⛔**其所由来·当日之实**：336 之第十一轮两跑两不过，`版本/第336章/_十一轮.json` 至今不在；
      **而 337 封版之後，本器照旧印「起第338章」**——**它只问「末章过没过」，不回头看。**
      ★**於是那一章可以一直欠着，而书一章一章往前走**：**欠的那一庭，隔的章数只会越来越多。**
    ★★**本判只往回数二十章**（⛔**不数全书**：此制立於 153 章，往回全数即把三百章之旧事翻出来，
      **那不是本器之职，那是 `十一轮哨` 之职**）；**且只认「回执已交而其凭不在」者。**
    ⛔**取不着者一律不报**（宁可少报，不可乱拦）。
    """
    欠 = []
    末 = 末章()
    for n in range(max(153, 末 - 20), 末 + 1):
        if not 回执在(n):
            continue
        if not os.path.exists(os.path.join(ROOT, '版本', '第%d章' % n, '_十一轮.json')):
            欠.append(n)
    return 欠


def 残树(跑=None, root=None, 在用=None):
    """★1027 执行之审 #63（执行主义「老旧拖累者直接删」）：已并而未删之 worktree 与枝 → (树[], 枝[])。
    已并＝其枝在 `git branch --merged HEAD`（其顶为 HEAD 之祖）；主树、本枝与主枝⛔计；枝之已检出於某树者归树、⛔重计；
    二时内有动之树（其 index 新）作「在用」⛔计（丝滑：⛔把他坐正跑之树报成残）。读崩 → ([], [])。
    ★1117（法用#停钩空转）：推後泊於「章-N」／「治-<sha12>」时主枝⛔检出於本树而为 HEAD 之祖——旧之判报之「已并而未删」并教 `git branch -d <主枝>`（险）；
      今主枝恒⛔计（枝与树俱然）。"""
    import subprocess
    root = root or ROOT
    跑 = 跑 or (lambda *a: subprocess.run(['git'] + list(a), cwd=root, capture_output=True, text=True, timeout=30).stdout)

    def _在用(路):
        try:
            gd = io.open(os.path.join(路, '.git'), encoding='utf-8').read().split('gitdir:', 1)[1].strip()
            return time.time() - os.path.getmtime(os.path.join(gd, 'index')) < 7200
        except Exception:
            return False
    在用 = 在用 or _在用
    try:
        本 = 跑('rev-parse', '--abbrev-ref', 'HEAD').strip()
        块们 = [b for b in 跑('worktree', 'list', '--porcelain').strip().split('\n\n') if b.strip()]
        并 = set(x.strip() for x in 跑('branch', '--merged', 'HEAD', '--format=%(refname:short)').splitlines()
                if x.strip() and not x.strip().startswith('('))   # 游离之 HEAD 其列作「(HEAD detached …)」⛔枝（1117 审之顺治）
    except Exception:
        return [], []
    树, 出枝 = [], set()
    for i, 块 in enumerate(块们):
        路 = re.search(r'^worktree (.+)$', 块, re.M)
        枝 = re.search(r'^branch refs/heads/(.+)$', 块, re.M)
        if 枝:
            出枝.add(枝.group(1))
        if i == 0 or not (路 and 枝) or 枝.group(1) in (本, 主枝) or 枝.group(1) not in 并:
            continue
        if not 在用(路.group(1)):
            树.append(路.group(1))
    return 树, sorted(b for b in 并 if b not in (本, 主枝) and b not in 出枝)


def 残树之印(树枝=None):
    """→ [行]：>0 即⚠（只报，⛔拦——删他树须先看其在用否）；俱无 → []。"""
    树, 枝 = 树枝 if 树枝 is not None else 残树()
    if not 树 and not 枝:
        return []
    return ['  ⚠ 已并而未删之 worktree %d／枝 %d（执行主义：老旧拖累者即删）：%s' % (
                len(树), len(枝), '、'.join([os.path.basename(x) for x in 树[:4]] + 枝[:4]) + ('……' if len(树) > 4 or len(枝) > 4 else '')),
            '     删法：git worktree remove <路>；git branch -d <枝>（-d 只删已并者；⛔-D 强删未并之枝）']


def 断(印=True):
    """返回 (判, 诸行)。判 ∈ 候／跑／补／治／救／欠／起（治：1027 A2·末章已封而未入主枝之报坏或缺章标）。"""
    L, 末 = [], 末章()
    try:
        import 暂停令 as _停
        _在, _由 = _停.在()
    except Exception:
        _在, _由 = False, ''
    if _在:
        # ★1009：作者之暂停令在盘上——⛔印「派下一席」（D6 之教训：一週之资源一事无成）
        L.append('  【判】停。' + _由)
        L.append('  ⛔开新章、⛔开耗 token 之工作流、⛔启用自走定时任务。只许零 token 之活（设计、治器、记账、复盘、推）。')
        L.append('  作者令下方解：python3 工具/暂停令.py --解 "作者令：……"；解毕再跑一回本器。')
        L.append('  ── 下一条命令 ──')
        L.append('  python3 工具/心跳.py --立停     # 停锁（时在远後）：停书之巡判止、新坐⛔跳；解令时自换空锁')
        try:   # ★1024·省审 sessions 四：停锁之下守书每唤只判「止」——关其定时之令，调毕记之（解令时 --解 印复开之参）
            if not _停.守书停记():   # 1117：兜底之巡三令俱停（乙丙每时空唤耗 token；暂停中解停由 暂停令 --解 同回合验之、GitHub cron 之巡兼察·W910）
                for _名, _参 in _停.守书之诸参(False):
                    L.append('  %s     # 停兜底之巡·%s（此为工具之调，非 shell）' % (_参, _名))
                L.append('  python3 工具/暂停令.py --守书已停     # 上三调毕即记')
        except Exception:
            pass
        L.append('  python3 工具/暂停令.py --查')
        return '停', L
    try:   # ★1021 开章之检（作者令「每一章只要一开始就看看原来的方法还行不行」）——零 token 数行
        import 费哨
        L.extend(费哨.章检(ROOT))
    except Exception:
        pass
    try:   # ★1027 执行之审 #63：已并而未删之 worktree／枝 >0 即⚠
        L.extend(残树之印())
    except Exception:
        pass
    跑, ch, 分 = 有人在跑()
    if 跑 and 锁滞(ch):

        L.append('  【判】起。第%s章之席**已办毕而锁未撤**（`_任务流.json` 末笔＝%s·封版席毕）。' % (ch, ch))
        L.append('  ★**这不是抢锁**：那一席十一段全走完了，只是收口段里没有撤锁那一步。')
        L.append('  ⛔**而先验一遍再撤**：封版五件须俱在（回执／锁定行／下一章开镜卡／封版之锚／正文）。')
        if not 十一轮之凭(ch):
            L.append('  ⛔⛔**而第%s章之第十一轮没有留下走过的凭据**'
                     '（`版本/第%s章/_十一轮.json` 不在）。' % (ch, ch))
            L.append('  ★**封版五件在，不等於那一庭过了**——**0916 本坐正是在这一处报错过一句话。**')
            L.append('  ⛔**故撤锁之後不许直接派下一章**：**先救那一章，再往前走。**')
            L.extend(十一轮不过之治)
            L.append('  ── 下一条命令 ──')
            L.append('  python3 工具/心跳.py --收 %s        '
                     '# 撤毕即跑 python3 工具/小说检察官.py --十一轮 %s（只有它产凭）' % (ch, ch))
            return '救', L
        L.append('  ── 下一条命令 ──')
        L.append('  python3 工具/心跳.py --收 %s        # 撤毕再跑一回本器，它会印「起」' % ch)
        return '起', L

    if 跑:
        L.append('  【判】候。第%s章之席在跑（%s 分钟前报到）。' % (ch, 分))
        L.append('  ⛔不许抢锁、不许动盘。★候即止：手上若已有真活（作者所派、到期之欠），办之；')
        L.append('     ⛔无则不为候而找活、⛔看进度（续跑、翻转录、ps）——结束本回合，等通知（效之律·坑㉔）。')
        L.append('  ⛔⛔而席在跑之时，一切动整个工作区的命令一律不许（律⑮）：')
        L.append('     git stash／git checkout .／git reset --hard／git clean／git add -A')
        L.append('     ——只许动我自己手上那几条明路径。要比改前改後：git show HEAD:<路径> > /tmp/旧.md')
        for x in 候时之活():
            L.append(x)
        L.append('  ── 下一条命令 ──')
        L.append('  python3 工具/续跑.py        # ⛔候时不跑——只在通知说席败、或候逾两时无通知时跑一回')
        return '候', L

    if not 回执在(末):
        L.append('  【判】跑。第%d章正文在盘而回执不在——那一章没走完。' % 末)
        L.append('  ── 下一条命令 ──')
        L.append('  python3 工具/心跳.py --跳 %d' % 末)
        L.extend(派令(末))
        return '跑', L

    if not 十一轮过(末):
        L.append('  【判】补。第%d章回执已交，而第十一轮未跑或未过。' % 末)
        L.append('  ⛔批123／126：十轮跑完须跑，不过不许封版。')
        L.extend(十一轮不过之治)
        L.append('  ── 下一条命令 ──')
        L.append('  python3 工具/小说检察官.py --十一轮 %d' % 末)
        return '补', L

    _治 = 前章之治(末)   # ★1027 A2·死锁之治：末章已封而未入主枝——先治／候，⛔起下一章（【重派】之会话自章-末起，首务在此）
    if _治:
        L.extend(_治[1])
        return _治

    # ★1021 账限哨（作者问「为什么还是我自己发现」）：瑕疵总账之限到即欠——⛔凭主环记得
    try:
        import 账限哨
        _限拦, _限L = 账限哨.印(ROOT, 末 + 1)
    except Exception:
        _限拦, _限L = False, []
    if _限拦:
        L.append('  【判】欠。瑕疵总账之限压在第%d章头上——先治；或写「延至 NNN…：<由>」（须新数限、一条至多一延，到期照拦），再起笔：' % (末 + 1))
        L.extend('  ' + x for x in _限L)
        L.append('  ── 下一条命令 ──')
        L.append('  python3 工具/账限哨.py')
        return '欠', L
    欠 = 逾期之欠(末 + 1)
    下 = 末 + 1
    if 欠:
        L.append('  【判】欠。有 %d 笔到期之账压在第%d章头上，须写进其卡再起笔：' % (len(欠), 下))
        for i, d, s in 欠:
            L.append('     · %-12s 限%-4s %s' % (i, d, s))
        L.append('  ⛔不许只挂不办；办不成即照实写明卡在哪一条，当场裁，不许无声顺延。')
        # ★★★★★★2026-09-13 补（体检账 ㊥·本坐当日两栽）：
        #   ⛔**我把两笔账的限都写成「下一章」，而没有先问一句「下一章是哪一条线」**——
        #   **327 是暗线，而那两笔皆係主线之物**：**那个限从写下来那一刻起就是空的。**
        #   ★故本器印「欠」时，必连这一问一并印出来，⛔不许下一坐再栽同一处。
        L.append('  ★★⛔而落笔之前先答这一问（体检账 ㊥·0913 本坐当日两栽）：')
        L.append('     **这一笔是谁的物、谁的线？第%d章是哪一条线？**' % 下)
        L.append('     ⛔两条对不上，即当场把它改挂到那条线走得到的头一章——')
        L.append('     **非顺延，是改挂**；★而一个挂在它走不到的章上的限，到期只会逼出')
        L.append('     破线硬插或再改一次期，两样都是账烂掉的样子。')

    # ★★★★★2026-09-14 立·大审之口（⛔其所以要补：`大审.py` 之律自书「平均十章一回」，
    #   而**盘上没有一只手在那一日把它派出去**——`一章.js` 之十一段里没有它，
    #   於是它只在 `大审.py --账` 里报一句「该开一回大审」，而没有人在读那一句
    #   （**㊛ 之骨：册上写着「器会报」而器报了没人接**；
    #    ★其实：`大审_至第313章.md` 与 `_至第323章.md` 二册皆空模子，正是没人接的那两回）。
    #   ★故本器在「起」之前先问一句：这一章封了版，大审到期没有？到了就先印它。
    try:
        _大 = __import__('大审')
        _上 = (_大.诸册() or [(0, None)])[-1][0]
        _止 = _大.到期(末, _上) if hasattr(_大, '到期') else (末 if 末 - _上 >= getattr(_大, '每', 10) else None)
        if _止:
            末 = _止                                   # ★1023 段齐：审至段末（⛔段中开审）
            L.append('  【判】庭。第%d章已封版，大审到期（审 %d—%d·410 起与段同界：设计十章→写十章→审十章）——**先开庭，再起下一章。**'
                     % (末, _上 + 1, 末))
            L.append('  ⛔**一庭两用者尤不许拖**：收站之章之欠，正要这一庭当面裁。')
            L.append('  ── 下一条命令 ──')
            # ★1017 大审.js 治四：args.孤钩 须明传——取到期账「裁」写「交 N 大审」（N 在本回之界）而未清者；读档不成即印其由（⛔印 []）
            try:
                _钩 = json.dumps(孤钩之(_上 + 1, 末), ensure_ascii=False)
            except Exception as _e:
                _钩 = None
                L.append('  ⛔到期账读不成（%s）——孤钩取不出，⛔以 [] 代；先治到期账再开庭。' % _e)
            if _钩 is not None:
                L.append("  Workflow({scriptPath:'工具/席/大审.js', args:{起:%d, 止:%d, 孤钩:%s}})"
                         % (_上 + 1, 末, _钩))
            L.insert(-1, '  python3 工具/大审.py --包 %d %d   ← 瘦式·零 token 先行（先跑；诸席同读其包）' % (_上 + 1, 末))
            L.append('  ★其後跑 python3 工具/大审.py --录 <runId> 自 journal 成册（X27·录册归器）；')
            L.append('  ⛔**只造册不填判者，`大审.py::空模子()` 当场滤掉它，不算一回大审**（㊧）。')
            L.append('  ★★办毕再跑一回本器，它自会印「起第%d章」。' % 下)
            return '庭', L
    except Exception:
        pass

    欠 = 欠十一轮之章()
    if 欠:
        n0 = 欠[0]
        L.append('  【判】救。第%d章之第十一轮没有留下走过的凭据'
                 '（`版本/第%d章/_十一轮.json` 不在），而书已写到第%d章。' % (n0, n0, 末))
        L.append('  ★**封版五件在，不等於那一庭过了**——**0916 本坐正是在这一处报错过一句话。**')
        L.append('  ⛔**欠着那一庭而接着往前叠，隔的章数只会越来越多。**')
        # ⛔⛔**0916 当日即栽·本器自己把本坐困在圈里**：
        #   头一版印的是「再派一回救章席」——**而救章席根本不产那一份凭**
        #   （`_十一轮.json` 係 `小说检察官.py --十一轮 N` 所产）；
        #   ★**照它跑，就是无限跑救章席**：跑完凭还是不在，本器照旧判「救」。
        #   ★★**故次序须写死**：**先跑那一庭**（它才产凭）；**它若不过，再看它报的是哪一头**——
        #   **右眼（检察官）报红＝书之事，照其项治；左眼（跑轮总核）报红＝账之事，先了其账。**
        #   ★1020 X29：右眼之治原印一代救章席——其席已汰（1008 令⛔审改之轮），今照其项治。
        _旗 = os.path.join(ROOT, '版本', '第%d章' % n0, '_拦停.json')
        L.append('  ── 下一条命令 ──')
        L.append('  python3 工具/心跳.py --跳 %d' % n0)
        L.append('  python3 工具/小说检察官.py --十一轮 %d      '
                 '# ★先跑那一庭——**只有它产 `_十一轮.json`**' % n0)
        L.append('  ⛔**不许头一步就派席**：**席不产那一份凭，跑一百回凭还是不在。**')
        L.append('  ★**那一庭若不过，先看它报的是哪一头**：')
        L.append('    · **右眼（检察官）报红＝书之事** → 照其项治（入圣经册、判到期账、立下一章之锚、推 open_brief……；'
                 '⛔审改之轮·1008 令）')
        L.append('    · **左眼（跑轮总核）报红＝账之事** → ⛔**席治不了**，'
                 '须先了其账（拦停旗／台账不齐／轮号不合；造式之章：缺哪一席之档交主环派那一席补）')
        if os.path.exists(_旗):
            L.append('  ⛔⛔**而第%d章此刻有拦停旗在**（`版本/第%d章/_拦停.json`）——'
                     '**旗未销，`跑轮` 一切轮务不办，左眼必不过。**' % (n0, n0))
            L.append('  ★**其账已卡成一个圈**（0916 之实）：补存被旗拦｜旗要补存才销｜'
                     '十一轮要总核过｜总核要旗销。⛔**四样互相咬住，非人当面裁不可。**')
            L.append('  ★★**故此时不必再跑那一庭**：**先把那一个圈解开，或照常令「写明卡在哪一条，'
                     '接着写下一章」。**')
        L.append('  ⛔**其治不是补一份 `_十一轮.json`**——**补一份凭据而不去走那一庭，正是它要逮的那一样。**')
        return '救', L

    if 云端已封(下):
        # 1022 复核所逮：新坐若起於未含上章之主枝，末章少一，即重写一章已封者——章-N 之标在云端即⛔起
        L.append('  【判】候。第%d章已封（云端有「章-%d」）而本树无之——⛔起（防重写已封之章）。' % (下, 下))
        L.append('  → `git fetch origin claude/the-novel-review-4dtuit && git merge --ff-only FETCH_HEAD`，或候 `python3 工具/接棒守.py --候主 %d`，再跑本器' % 下)
        return '候', L
    L.append('  【判】起。第%d章已封版且十一轮过——当起第%d章。' % (末, 下))
    if 下 >= 411:   # ★1027 法用之守：开章即印本章须用之法与其证（≤10 行·零网）；封版 --前 印其红、--後 拦
        try:
            import 法用之守
            L.extend('  ' + x for x in 法用之守.开(下))
        except Exception as _e:
            L.append('  ⛔法用之守印不出（%s）——python3 工具/法用之守.py --开 %d' % (_e, 下))
    L.append('  ── 下一条命令（⛔逐条照抄，序不许换）──')
    L.append('  python3 工具/心跳.py --跳 %d' % 下)
    if not 卡在(下):
        # ⛔★2026-09-16 正一处死处方（体检账 七十二·同族第五例，本坐当日自扫所得）：
        #   **此行原印之器名末字作「卡」，而盘上之器名末字係「庭」**
        #   （`ls 工具/` 亲印，今已改对；⛔**那个死名不在此重写一遍**——
        #     **写进注里，`死处方哨` 当场又把它逮出来**）。
        #   ⛔**即：照本器印的这一条跑，当场「can't open file」。**
        #   ★★**而本行自己的注写着「器名以磁盘为准」**——**写注的人知道这一条要对盘，而他没有对。**
        #   ★★★**这正是七十二那一条所指的形**：**处方写着一件做不成的事，而它平日不响**，
        #     **只在真有人照它跑的那一天塌**；⛔**而那一天，塌的是下一章的开镜卡。**
        L.append('  python3 工具/第零轮开镜庭.py --立 %d   # 卡不在，先立卡' % 下)
    # ★0927 敷衍普查（设定/敷衍普查_0927.md）：剧情庭之势旧只在封版之後由 剧情庭之关 事後判红——
    #   即先写後定走向，等於先交一个过得去的再补。今於派章之前即印：段之势不在，先开剧情庭（式：段·1027）。
    if 下 >= 381:
        _段 = 381 + (下 - 381) // 10 * 10
        _势 = os.path.join(ROOT, '设定', '剧情庭_势_第%d段.md' % _段)
        if not os.path.exists(_势):
            L.append('  ⛔本段（%d—%d）剧情庭之势未立——先定走向再动笔（选剧情之律§四；先交一个过得去的再补，即是反面教材）：' % (_段, _段 + 9))
            if _段 >= 411:
                L.append('  ★段序（作者 1023 令·段序之守拦）：题须引 设定/大审_至第%d章.md——上段大审之孤钩、大进、二稿交本段一次造进去；'
                         '其後段料 → 段案十章俱全（立、驳、验）方写第%d章。' % (_段 - 1, _段))
            L.append('  Workflow({scriptPath:\'工具/席/剧情庭.js\', args:{题:\'设定/剧情庭题/势_第%d段.md\', 名:\'势_第%d段\', 式:\'段\', W:\'W<号>\'}})   # 式段（总章 §四、§八.3·法用#剧情庭式段：裁席出单、主环 改单.py --施单；1027 复核：旧印式新＝裁席亲改、⛔施单，411 封版即⛔）；题档首行「料：设定/段案/_料_%d-%d.md」（先 python3 工具/段料.py %d %d）' % (_段, _段, _段, _段 + 9, _段, _段 + 9))
    L.append('  python3 工具/席法.py                      # 钥匙不绿，一个席也不许派')
    L.extend(派令(下))
    return ('欠' if 欠 else '起'), L


def 前哨():
    """→ 零 token 之红行（1024）：守书之巡停而令已解（书断流之险）。行首⛔，默印即收入「前置诸哨之红」。"""
    出 = []
    try:
        import 暂停令
        出 += 暂停令.守书之哨()
    except Exception as e:
        出.append('⚠ 守书之哨跑不起来：%s' % e)
    try:   # 1024 盘坏之哨：<git 公目>/盘坏.flag 在即首印（存底守 06:25 起每回败而只入日志之教）
        import 重取
        l = 重取.印()
        if l:
            出.insert(0, l)
    except Exception as e:
        出.append('⚠ 盘坏之哨跑不起来：%s' % e)
    try:   # 1027 丝滑主义·问题早见：备份/报 之 报/推、报/演 未为後之成所消之 红／拒／败（一取·零 token·≤三行；经 推报.诸报）
        import 法用之守
        出 += 法用之守.报之读()
    except Exception as e:
        出.append('⚠ 报之读跑不起来：%s' % e)
    return 出


def 报():
    for _l in 前哨():
        print(_l)
    判, L = 断()
    # ★★★★★2026-09-24 作者当面令（律⑳）——**每一坐一开眼先看见这两句，不许再停下来问作者**：
    print('⭐【律⑳·总编辑之权】你是这本书的总负责人：凡须裁之事，照「让书更好看、成中国第一」当场裁定、落账、执行；'
          '⛔不许把裁推回作者而停（1027 第一律·自决：自裁、记由、办毕报所为）。⛔此权只朝书更好看一个方向用（不凑字、不造高潮、不放宽闸让自己过）。')
    print('⭐【裁之生效】做了的决定须有器守且真在跑——`工具/裁之生效.py` 每坐必跑；⛔只写在纸上的裁不算裁。')
    try:
        import subprocess as _sp20, os as _os20
        _sp20.run([sys.executable, _os20.path.join(_os20.path.dirname(_os20.path.abspath(__file__)), '裁之生效.py')],
                  timeout=120)
    except Exception as _e20:
        print('  ⛔裁之生效跑不起来：%s' % _e20)
    # ★★★★★2026-09-25 作者令：「是整本书让人上瘾，不是每一章刻意去吊；最怕刻意——审美疲劳、全书割裂、每章自立山头。」
    print('⭐【总编辑】你是总话事人、总决策人：规矩是死的，人是活的——凡规不利於这本书成中国第一，当场改或废，⛔不请示。')
    try:
        _sp20.run([sys.executable, _os20.path.join(_os20.path.dirname(_os20.path.abspath(__file__)), '总编辑复核.py')], timeout=60)
    except Exception as _e22:
        print('  ⛔总编辑复核跑不起来：%s' % _e22)
    print('⭐【一切皆可改】圣经、设定、已写之章，皆可改——唯一前提：改了之後书更好（说得出好在哪）；'
          '每改必 `python3 工具/改单.py --立` 立单、备份改前原文、提交写「改单#」；说不出更好在哪，不改。')
    print('⭐【写章唯一之规】无招胜有招：每一章尽全力写到质量最高——何谓最高，即诸章合起来，这本书是中国第一的小说。'
          '⛔不立刻意之规去绑一章怎么写。')
    # ★1118 总编辑复核·刻意之疲 → 改（0ad2fad7c）：旧於此每坐跑一回刻意之疲、印给写者——撤。
    #   其镜给大审之通读者（大审.py 零先之器 之包一路），⛔逼写者刻意换收法（0925 四裁·无招胜有招）。
    # ★★★★★2026-09-24 接·**未上库哨在头一行**（作者当面令）：
    #   ⛔**今日之实**：远端末笔 09-18，而今 09-24——**350—363 十四章 GitHub 上一个字也没有**；
    #   ★**而本坐六天里每天跑本器，本器每天印「接着办下一件」**，
    #     **一次也没有把「还没进库」顶到作者面前。**
    #   ★★**故它落在这一行之前**：**在「此刻该干哪一件」之前，先问「丢了没有」。**
    try:
        import importlib.util as _u9, os as _o9
        _s9 = _u9.spec_from_file_location(
            '未上库哨', _o9.path.join(_o9.path.dirname(_o9.path.abspath(__file__)),
                                      '未上库哨.py'))
        _m9 = _u9.module_from_spec(_s9)
        _s9.loader.exec_module(_m9)
        _m9.报()
        # ★★★★★2026-09-24 接·**自进化环在最前**（作者令「须有时刻运营之自我进化与纠错机制」）：
        #   ⛔**它与上面那道哨之别**：**哨只会报，环会自己修**——
        #     L0 存底枝逾 30 分未更新即**自存一回**；L1 主枝落後即**自推一回**（走闸不绕）；
        #     **同一因连两回修不好即判卡死——换法自通（另一合规之路），记由入裁档，办毕报所为；⛔停工候作者**（1027 第一律·自决）；
        #     L3 **同族病逮到第二回而无器管它即红**（其账在 `设定/病族账.md`）。
        #   ★**本环每跑一回落一行 `设定/自进化环.log`**——**逾两钟头没跑过，即本环自己停了**。
        #   ⛔**此处只跑 L0／L1／L3（快）**；L2（尺之校＋自省哨）在下面各自跑，免重跑。
        _s6 = _u9.spec_from_file_location(
            '自进化环', _o9.path.join(_o9.path.dirname(_o9.path.abspath(__file__)),
                                      '自进化环.py'))
        _m6 = _u9.module_from_spec(_s6)
        _s6.loader.exec_module(_m6)
        _过6 = set()
        for _名6, _层 in (('L4', _m6.L4), ('L0', _m6.L0), ('L1', _m6.L1), ('L3', _m6.L3)):  # ⭐L4 书之进化列最前
            try:
                _ok6, _语6 = _层()
                for _l6 in _语6:
                    print('  ' + _l6)
                if _ok6:
                    _过6.add(_名6)
            except Exception as _e6:
                print('  ⛔自进化环一层跑不起来：%s' % _e6)
        _m6.记脉('自走头·L0L1L3')   # 脉由自进化环自落（本器不动盘）
        # 〔1119 W908 环7〕销陈账（自进化环.陈账·一处判）：旧自走只跑诸层而⛔销，全环（自进化环.跑）无入口——陈账自 1027 不销；
        #   今照 跑() 之式：本回跑过之层（报过，或跑毕而全好）其旧因未再见即销；首见逾七日而只见一回者自销；崩层⛔销
        try:
            _d6 = _m6._读挂()
            _陈6, _旧6 = _m6.陈账(_d6, set(_m6.本回所报之层) | _过6, _m6.本回所见)
            if _陈6 or _旧6:
                for _k6 in _陈6 + _旧6:
                    _d6.pop(_k6, None)
                _m6._写挂(_d6)
                print('  ✓自进化环·销陈账 %d 笔：%s' % (len(_陈6 + _旧6), '；'.join(x[:40] for x in _陈6 + _旧6)))
        except Exception as _e6:
            print('  ⚠自进化环·销陈账未成：%s' % _e6)
        _卡6 = [(k, v) for k, v in _m6._读挂().items() if v.get('回', 0) >= _m6.卡死之回]
        if _卡6:
            print('  ⛔⛔⛔ **卡死 %d 处——换法自通（另一合规之路），记由入裁档，办毕报所为；⛔停工候作者、⛔默默往下写**：%s'
                  % (len(_卡6), '；'.join(k for k, _ in _卡6)))
        # ★★★★★2026-09-24 接·**尺之校在未上库哨之下**（律⑰）：
        #   ⛔0924 之实：一条清不掉的红堵了推六天，而其真身是一把尺瞎了六十章。
        _s8 = _u9.spec_from_file_location(
            '尺之校', _o9.path.join(_o9.path.dirname(_o9.path.abspath(__file__)),
                                    '尺之校.py'))
        _m8 = _u9.module_from_spec(_s8)
        _s8.loader.exec_module(_m8)
        if not _m8.报():
            print('⛔★上列诸处：**先校那把尺，⛔不要先治那几章**（律⑰）。')
        # ★★★★★2026-09-24 接·**自省哨在尺之校之下**（律⑱·作者令「须有自我纠错与进化之机制」）：
        #   ⛔其所问只一样：**器上写着的话，有没有一道器在读它。**
        _s7 = _u9.spec_from_file_location(
            '自省哨', _o9.path.join(_o9.path.dirname(_o9.path.abspath(__file__)),
                                    '自省哨.py'))
        _m7 = _u9.module_from_spec(_s7)
        _s7.loader.exec_module(_m7)
        if not _m7.报():
            print('⛔★上列诸处：**器上写着的话没有人在读它**——**这一族病今日逮到六处**（律⑱）。')
    except Exception as _e9:                                  # pragma: no cover
        print('⛔未上库哨跑不起来（%s）——⛔**跑不起来不是绿**，须当面查。' % _e9)
    # 0930 作者令：GitHub 为唯一之记忆——每回先印工作流账（已成／进行／可开与续之令），⛔重做已成之件
    try:
        import subprocess as _sp9
        _sp9.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), '工作流账.py')])
    except Exception as _e9:
        print('  ⛔工作流账印不出：%s' % _e9)
    # 〔1119 W908 环7〕D1 之器之印去：D1 1027 已器施毕（瑕疵总账 X17），D1施／行号随移 二器与其负测俱删（法用册 废·D1施之器、行号随移之器）
    print('· 封版之序（1027 A2·一章一提交一推）：记席毕、`封版.py N --前 --红` 绿 → `复盘.py W… --简 --平台 $X`（$X＝get_session 之 cost_usd·1027 无 --平台 即拒）与交接现状（⛔另提交）→ '
          '`心跳.py --跳 N+1` → `封版.py N --後`（封版#N 一提交载之；其末推「章-N」——一章唯此一推；沙盒⛔跑全闸）→ `接棒守.py --候主 N`')
    print('· 推送：一律 `python3 工具/推.py`——交 GitHub（推「治-<sha>」、本地⛔全测；GitHub 分片而闸、绿即并入主枝），'
          '其印之 `推.py --候 <sha>` 後台零 token 候；封版後只 `接棒守.py --候主 N`（章-N 已触 autopush）；'
          '报「拒」或 GitHub 停摆方 `推.py --直`（审计之兜底·本地全闸；坑51；文件锁、不排队、被拦即停；⛔自写排队脚本、⛔pgrep 猜进程）')
    print('════ 自走 · 此刻该干哪一件 ════')
    for x in L:
        print(x)
    print('  ⛔本器只印一行命令。★照它跑，跑完再跑一回本器——**中间不许停下来问。**')
    return 判


def 自测():
    R = []
    判, L = 断(印=False)
    _派 = 派令(382)
    R.append(('派令·有段案之章印造章.js（二代），其重与魂路取自段案；无段案之章⛔派一代（已淘汰）、印先立段案',
               any("造章.js" in x and "重:'中'" in x and "'换账'" in x for x in _派) and not any('一章.js' in x and 'Workflow' in x for x in 派令(999)) and any('段案' in x for x in 派令(999))))
    # 〔W919 落地之查·病一〕N≥489：盘上无稿而本章有前 Run（journal）或 _席之因.json → 派令走承之路（⛔新派：新派即同令首派前 Run 之拒席）
    import tempfile as _tf, contextlib as _cl
    with _tf.TemporaryDirectory() as _t:
        os.makedirs(os.path.join(_t, '版本', '第989章'))
        _跑无 = 本章有跑(989, _t, 来=lambda k: [])
        _跑有 = 本章有跑(989, _t, 来=lambda k: ['/x/journal.jsonl'])
        _跑旧 = 本章有跑(488, _t, 来=lambda k: ['/x/journal.jsonl'])
        with _cl.redirect_stdout(io.StringIO()) as _buf:
            _跑崩 = 本章有跑(989, _t, 来=lambda k: 1 / 0)
        open(os.path.join(_t, '版本', '第989章', '_席之因.json'), 'w', encoding='utf-8').write('{}')
        _跑录 = 本章有跑(989, _t, 来=lambda k: [])
    R.append(('落地之查·病一 本章有跑：N≥489 有前 Run 或 _席之因.json → 真；无 → 假；488 → 假；取崩 → 只 ⚠ 而假',
              not _跑无 and _跑有 and not _跑旧 and not _跑崩 and '⚠' in _buf.getvalue() and _跑录))
    # ★1020 X40：须厚入令——n≥401 而判「非厚不可」者 args 添 须厚:true 並印其由；⛔N≤400 一字不变（厚直传，⛔钉盘上之数）
    import 章料 as _章料
    _段旧 = _章料.段案行
    try:
        _章料.段案行 = lambda n, root=None: '（设定/段案/9001-9002.md）\n- 重：中\n- 魂路：物证｜换账｜翻个儿\n- 守：⛔凑。**字数：2,900—3,300**（须厚未可判）'
        _厚 = 派令(9001, 厚=(True, '⛔**第9001章非厚不可**：其前四篇暗线……\n    ⛔**其治只有一样：换一件更大的事**'))
        _薄 = 派令(9001, 厚=(False, '★第9001章不须厚'))
        _未 = 派令(9001, 厚=(None, '★第9001章之须厚未可判'))
        _厚旧 = 派令(472, 厚=(True, '⛔**第472章非厚不可**：桩'))     # 〔1119 死规之审·gates6〕N<473 之注照旧（坑㉚）
        _未旧 = 派令(472, 厚=(None, '★第472章之须厚未可判'))
        _章料.段案行 = lambda n, root=None: '（设定/段案/9001-9002.md）\n- 重：中\n- 魂路：物证｜换账｜翻个儿'
        _无带 = 派令(9001, 厚=(False, '★不须厚'))
        _旧章 = 派令(470, 厚=(False, '★不须厚'))
        _章料.段案行 = lambda n, root=None: '（设定/段案/9001-9002.md）\n- 重：中\n- 魂路：物证｜换账｜翻个儿\n- 守：⛔凑。**字数：2,900—3,300**'
        _原跑 = globals()['本章有跑']
        try:                                           # 〔W919 落地之查·病一〕盘上无稿而本章有前 Run → 派令走承.py 之路（⛔新派）
            globals()['本章有跑'] = lambda n, root=None, 来=None: True
            _承路 = 派令(9001, 厚=(False, '★不须厚'))
        finally:
            globals()['本章有跑'] = _原跑
    finally:
        _章料.段案行 = _段旧
    R.append(('X40·派令：须厚之章（n≥401）args 添 须厚:true 并印其由；不须者⛔添；未可判者印其由而⛔添；N≤400 传之亦⛔添（与不传者同）',
               any("Workflow" in x and "args:{章:9001, 重:'中', 魂路:['物证', '换账', '翻个儿'], 须厚:true, 带:'2,900—3,300'}" in x for x in _厚)
               and any('第9001章非厚不可' in x and x.startswith('  # ') for x in _厚) and _厚[-1].lstrip().startswith('Workflow')
               and not any('须厚:true' in x for x in _薄 + _未) and len(_薄) == 3
               and any('须厚未可判' in x for x in _未)
               and 派令(382, 厚=(True, '⛔x')) == _派 and not any('须厚' in x for x in _派)))
    # 〔1119 死规之审·gates6/docs7〕N≥473 须厚之注只报（⛔「硬项」、⛔「先治其由再派」）；472 照旧；args 之 须厚:true 照传（执笔令【须厚·参考】）
    R.append(('死规审·派令：N≥473 须厚之注只报（⚠·⛔硬项、⛔先治再派），须厚:true 照传；472 之注照旧',
               any('⚠须厚（X40·只报' in x for x in _厚) and not any('硬项「本章之事须担得起' in x for x in _厚)
               and any('⚠须厚未可判' in x and '只报' in x for x in _未) and not any('先治其由再派' in x for x in _未)
               and any('硬项「本章之事须担得起 2,900」' in x for x in _厚旧) and any('须厚:true' in x for x in _厚旧)
               and any('⛔须厚未可判' in x and '先治其由再派' in x for x in _未旧)))
    R.append(('落地之查·病一 派令：盘上无稿而本章有前 Run（本章有跑 真）→ 印 承.py 9001 --重 --魂路 与 _承.js（⛔印新派之 造章.js args）；无前 Run → 新派',
              any('承.py 9001 --重 中 --魂路 物证,换账,翻个儿' in x for x in _承路) and any('_承.js' in x for x in _承路)
              and not any("scriptPath:'工具/席/造章.js'" in x for x in _承路) and any("scriptPath:'工具/席/造章.js'" in x for x in _薄)))
    R.append(('X119·派令：n≥471 args 带段案之带（带:\'2,900—3,300\'）；段案无「字数」者⛔派、印先补；N≤470 ⛔带',
               any("Workflow" in x and "args:{章:9001, 重:'中', 魂路:['物证', '换账', '翻个儿'], 带:'2,900—3,300'}" in x for x in _薄)
               and not any('Workflow' in x for x in _无带) and any('先补段案之字数' in x for x in _无带)
               and any("Workflow" in x and '带:' not in x for x in _旧章)))
    R.append(('①判得出一个字（候／跑／补／救／欠／起／庭／停）',
               判 in ('候', '跑', '补', '救', '欠', '起', '庭', '停')))
    R.append(('②末一行是一条可照抄之命令', any(
        x.strip().startswith(('python3', 'Workflow')) for x in L)))
    R.append(('③末章取自正文档名，非版本目录（版本底下有第999章之试样）',
              末章() == max([_num(re.search(
                  r'第([零〇一二三四五六七八九十百千]+)章',
                  os.path.basename(f)).group(1))
                  for f in glob.glob(os.path.join(ROOT, '正文', '*.md'))
                  if re.search(r'第([零〇一二三四五六七八九十百千]+)章',
                               os.path.basename(f))])))
    # ④⛔心跳之限不写死在本器里（体检账 ㊖：判据里不许有「今天才成立」的数）
    src = io.open(os.path.abspath(__file__), encoding='utf-8').read()
    码 = src.split('def 自测')[0]          # ★只数自测以上之码，否则测在数它自己
    # ⑨★2026-09-14 补：大审之口须真在码里，且其判之名在①之表内
    #   ⛔其所以要验：`大审.py` 之律自书「平均十章一回」，而盘上从来没有一只手在那一日把它派出去
    #   （㊛ 之骨：册上写着「器会报」而器报了没人接；313／323 二册之空模子即其实）。
    R.append(('⑨大审之口在码里（其判作「庭」，并印席之命令）',
               '工具/席/大审.js' in 码 and "'庭', L" in 码))
    R.append(('⑨之三·大审到期取 大审.到期（1023 段齐：410 起审至段末、⛔段中开审）；暂停之判印立停锁',
               "_大.到期(末, _上)" in 码 and "心跳.py --立停" in 码))
    # ⑨之二★1017：大审之令须带 孤钩（大审.js 缺 args.孤钩 即 throw）；孤钩之 取到期账「交 N 大审」而未清者
    _桩 = [{'id': 'A', '裁': '交 397 大审裁', '状态': 'cold', '事': '甲事★其後'},
          {'id': 'B', '裁': '交 397 大审', '状态': 'done', '事': 'b'},
          {'id': 'C', '裁': '交397大审', '状态': '清', '事': 'c'},
          {'id': 'D', '裁': '交 397 大审；後改交 407 大审', '状态': 'open', '事': 'd'},
          {'id': 'E', '裁': '交第397章大审', '状态': 'half', '事': '头问★★其下一层为「余半之问」'},
          {'id': 'F', '裁': '交 386 大审', '状态': 'cold', '事': 'f'},
          {'id': 'G', '状态': 'cold', '事': 'g'}]
    _得 = 孤钩之(388, 397, 诸=_桩)
    R.append(('⑨之二·大审之令带孤钩；孤钩之 只取界内（末一处）而未清（done／closed／清）者，注取余半之问',
               '孤钩:%s' in 码 and [x['id'] for x in _得] == ['A', 'E']
               and _得[0]['注'] == '甲事' and _得[1]['注'] == '余半之问'
               and [x['id'] for x in 孤钩之(398, 407, 诸=_桩)] == ['D']
               and all(x.get('id') for x in 孤钩之(1, 9999))))
    # ⑩★2026-09-16 立：**锁滞之判须真跑得出，且宁可候不可抢**
    #   ⛔其所以要验：335 之席办毕而锁未撤，本器照旧印「候」，白丢七分钟（若无人看要挂满 45 分钟）。
    #   ★其判之据係 `_任务流.json` 之末笔（略过存底流水），⛔**读不出即作「席还在」论**。
    R.append(('⑩锁滞·读不出即作席还在论（宁可候不可抢）',
               'def 锁滞' in 码 and 'return False                 # 读不出' in 码))
    R.append(('⑩之二·锁滞之判略过存底流水（存底不算一段）',
               "事.startswith('存底')" in 码 and "continue" in 码))
    # ⑪★2026-09-16 立：**封版五件在，不等於那一庭过了**
    #   ⛔0916 本坐正是在这一处报错过一句话：验过五件即报「336已封版」，
    #   而 336 之第十一轮两跑两不过，`_十一轮.json` 至今不在。
    # ★2026-09-22 治一笔「前提过期」之红（`体检账 51` 之型）：
    #   本格原写「今日之实：335 有、336 无」，**而 336 之 `_十一轮.json` 後来补上了**
    #   （`ls 版本/第336章/_十一轮.json` 今印得着）——**於是此格自那一日起恒红，
    #   本器一路印 25/26**，⛔**而那一红说的不是器坏了，是它拿一件会变的事当了尺。**
    #   ★**其治**：**「有凭」拿真盘上一章验（335），「无凭」拿一个盘上永不会有的章号验**
    #   ——⛔**不再拿某一章此刻的欠当尺**。
    R.append(('⑪十一轮之凭·有凭者读得出（335·真盘）', 十一轮之凭('335') is True))
    R.append(('⑪之四 无凭者判红（第9998章·盘上无此档，不随书之长短而变）',
               十一轮之凭('9998') is False))
    R.append(('⑪之二 判不出章号者不乱拦（宁可放行）', 十一轮之凭('乙') is True))
    R.append(('⑪之三 无凭者其判作「救」而非「起」（下一条命令是补走那一庭 --十一轮）',
               'return \'救\', L' in 码 and '# 撤毕即跑 python3 工具/小说检察官.py --十一轮 %s' in 码))

    # ⑬★2026-09-16 立·**往回数一遍：有没有哪一章「册上写着已封版，而那一庭没走过」**
    #   ⛔当日之实：336 之凭不在，而 337 封版後本器照旧印「起第338章」——它只问末章，不回头看。
    _欠 = 欠十一轮之章()
    R.append(('⑬欠十一轮之章·真数得出（今日之实：336 在其内）', isinstance(_欠, list)))
    R.append(('⑬之二 其判作「救」且印不过之治（造式之法·十一轮不过之治）',
               "'救', L" in 码 and 码.count('L.extend(十一轮不过之治)') >= 2))
    # ⑬之五★2026-09-16 当日即栽：**头一版印「再派救章席」，而救章席不产那一份凭**——
    #   照它跑就是无限跑救章席。今写死其序：先跑那一庭（只有它产凭），再看它报的是哪一头。
    R.append(('⑬之五 头一步係「--十一轮」而非派席（席不产其凭）',
               '--十一轮 %d' in 码 and '不许头一步就派席' in 码))
    # ⑬之八★1020 X29（淘汰之律）：**码里所印之 Workflow 席，盘上须在**——
    #   一代救章席已彻删，而旧码三判仍印其 scriptPath；照它派，当场取不着那一席（且违 1008 令⛔审改之轮）。
    #   ★回灌：旧码之一行（逐字）灌进同一判，须逮出；今码须零。
    #   ★X43⑤：其尺⛔自抄——与 囤灰闸.派令之席 同出 囤灰闸.派令之路（剔注、容转义之引号、子目录之路亦认）
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location('_囤灰闸', os.path.join(ROOT, '工具', '囤灰闸.py')); _囤 = _iu.module_from_spec(_sp); _sp.loader.exec_module(_囤)
    def _死席(文):
        return sorted(p for p in _囤.派令之路([('自走.py', 文)]) if not os.path.exists(os.path.join(ROOT, p)))
    _旧行 = "L.append('     Workflow({scriptPath:\\'工具/席/救章.js\\', args:{章:%d}})' % 末)"
    _SP = 'scriptPath:' + "'工具/席/"   # 拆写：本档自身亦係派令之文（囤灰闸读之），测之串⛔作真派令
    _注行 = "x = 1   # 旧派 Workflow({" + _SP + "救章.js'})——已汰\n# L.append(\"Workflow({" + _SP + "救章.js'})\")\n"
    R.append(('⑬之八 码里所印之席盘上皆在（X29·救章席已汰）；旧码之行回灌须逮出；注里之 scriptPath ⛔算（X43⑤·与囤灰闸一尺）；子目录之死路亦逮',
               _死席(码) == [] and _死席(_旧行) == ['工具/席/救章.js'] and _死席(_注行) == []
               and _死席("L.append(\"Workflow({" + _SP + "_旧/无此席.js'})\")") == ['工具/席/_旧/无此席.js']))
    R.append(('⑬之六 分得清左眼右眼（账之事席治不了）',
               '右眼（检察官）报红＝书之事' in 码 and '左眼（跑轮总核）报红＝账之事** → ⛔**席治不了**' in 码))
    R.append(('⑬之七 有拦停旗者当场说明其圈（不叫人白跑一庭）',
               '_拦停.json' in 码 and '四样互相咬住' in 码))
    R.append(('⑬之三 只往回数二十章（不翻三百章之旧事）', '末 - 20' in 码))
    # ── 0923 立·回执之三种（⛔每改必同日负测，且以旧式回灌验）──
    #   ★其立之由：358 两份回执叫「案席」「封版席」，无「作业单」三字，
    #     旧式遂判它「没走完」，并印命令叫人把一章已封版的书从头再跑一遍。
    _旧式回执 = lambda n: bool(glob.glob(os.path.join(ROOT, '设定', '回执_*_第%d章作业单.md' % n)))
    R.append(('㉗新式·358 之回执认得着（其档名係「封版席」「案席」）', 回执在(358) is True))
    R.append(('㉗之b ⛔旧式之下 358 看不见（此即其病之形·⛔它会叫人重跑一章已封版的书）',
              _旧式回执(358) is False))
    R.append(('㉗之c ★而 354（只有作业单）两式皆认得（⛔证新式非把旧路废掉）',
              回执在(354) and _旧式回执(354)))
    R.append(('㉗之d ⛔未写之章照旧不认（⛔不许把闸开成「凡有档皆算」）', 回执在(999) is False))
    # ㉗之e ★1118 改（总编辑裁·非删）：旧格验「三名之字俱在码内」——字在码里不等於判对（案席 0924 已於 接力／十一轮哨 收回、本函漏收，旧格照绿）；
    #   今本函即 接力.有回执（同功一处）——改验其行於沙盘（⛔真盘·⛔验码之字面）：作业单、封版席照认（⛔退回只认作业单）；案席一份⛔作数；
    #   ㉗之f（X109·记席之中）封版席之骨＋段.封版「待 封版.py」→ 未封、【判】跑（旧式回灌：判补·教跑 --十一轮 於未封之章）；
    #   ㉗之g（封版 --後 红於第十一轮之後）骨＋_十一轮.json 而段.封版 仍「待」→【判】跑（⛔补、⛔起；旧式回灌越过跑、补）
    import tempfile as _tf, shutil as _sh, 接力 as _接t, 暂停令 as _停g
    _旧三名 = lambda n: any(glob.glob(os.path.join(ROOT, '设定', '回执_*_第%d章%s.md' % (n, k))) for k in ('作业单', '案席', '封版席'))
    _G = globals()
    _存 = {k: _G[k] for k in ('ROOT', '末章', '有人在跑', '回执在')}
    _存接, _存停 = _接t.ROOT, _停g.在
    _沙 = _tf.mkdtemp(prefix='自走回执_')
    _判e = {}
    try:
        os.makedirs(os.path.join(_沙, '设定'))

        def _回(n, k):
            io.open(os.path.join(_沙, '设定', '回执_20261118_第%d章%s.md' % (n, k)), 'w', encoding='utf-8').write('沙盘')

        def _记(n, 封, 轮=False):
            d = os.path.join(_沙, '版本', '第%d章' % n)
            os.makedirs(d, exist_ok=True)
            json.dump({'章': n, '段': {'记': '记落.py：俱过', '封版': 封}}, io.open(os.path.join(d, '_席记.json'), 'w', encoding='utf-8'), ensure_ascii=False)
            if 轮:
                io.open(os.path.join(d, '_十一轮.json'), 'w', encoding='utf-8').write('{}')
        _回(300, '作业单'); _回(360, '封版席')
        _回(9100, '案席'); _记(9100, '封版.py：俱过', 轮=True)          # 只有案席（段.封版 俱过）
        _回(9101, '封版席'); _记(9101, '封版.py：俱过', 轮=True)        # 真封
        _回(9102, '封版席'); _记(9102, '待 封版.py')                    # X109 之骨·记席之中
        _回(9103, '封版席'); _记(9103, '待 封版.py', 轮=True)           # 骨＋第十一轮已跑·封版 --後 红
        _G['ROOT'] = _接t.ROOT = _沙
        _停g.在 = lambda root=None: (False, '')
        _G['有人在跑'] = lambda: (False, None, None)
        for n in (300, 360, 9100, 9101, 9102, 9103):
            _判e[n] = (回执在(n), _接t.有回执(n), _旧三名(n))
        for n in (9102, 9103):
            _G['末章'] = (lambda m: lambda: m)(n)
            _G['回执在'] = _存['回执在']
            _新 = 断(印=False)[0]
            _G['回执在'] = _旧三名                                      # 旧式回灌：三名、⛔问 段.封版
            try:
                _旧 = 断(印=False)[0]
            except Exception as _e:
                _旧 = '崩:%s' % type(_e).__name__
            _判e['断', n] = (_新, _旧)
    finally:
        _G.update(_存)
        _接t.ROOT, _停g.在 = _存接, _存停
        _sh.rmtree(_沙, ignore_errors=True)
    R.append(('㉗之e（1118 改·沙盘）回执之判即 接力.有回执：作业单（300）、封版席（360）俱认；封版席＋段.封版 俱过（9101）认；只有案席（9100）⛔作数'
              '｜旧式回灌（三名）认 9100——上格非陪跑',
              all(_判e[n][0] == _判e[n][1] for n in (300, 360, 9100, 9101, 9102, 9103))
              and _判e[300][0] is True and _判e[360][0] is True and _判e[9101][0] is True and _判e[9100][0] is False and _判e[9100][2] is True))
    R.append(('㉗之f（X109·记席之中）封版席之骨＋段.封版「待 封版.py」→ 回执在 %s、【判】%s；旧式回灌 回执在 %s、【判】%s'
              % (_判e[9102][0], _判e['断', 9102][0], _判e[9102][2], _判e['断', 9102][1]),
              _判e[9102][0] is False and _判e['断', 9102][0] == '跑' and _判e[9102][2] is True and _判e['断', 9102][1] == '补'))
    R.append(('㉗之g（封版 --後 红於第十一轮之後）骨＋_十一轮.json 而段.封版「待」→【判】%s（⛔补、⛔起）；旧式回灌越过跑、补（【判】%s）'
              % (_判e['断', 9103][0], _判e['断', 9103][1]),
              _判e[9103][0] is False and _判e['断', 9103][0] == '跑' and _判e['断', 9103][1] not in ('跑', '补')))
    R.append(('⑬之四 只认「回执已交而其凭不在」者', '回执在(n)' in 码 and '_十一轮.json' in 码))

    # ⑫★2026-09-16 立·**那把锁是「没人撤」还是「有人又按上去了」**
    #   ⛔当日之实：337 封版毕、其席自己撤了锁，本坐随即把锁按回 337——为的是不叫别坐
    #   在「大审庭」开着的时候把 338 派出去；而本器只看末笔，照旧印「起」。
    _步t = [{'事': '9·封版席毕', '时': '2026-09-16 12:00:00'},
            {'事': '存底·第9章封版', '时': '2026-09-16 12:01:00'}]
    # ⛔**其二时当场算出，不写死**：⭑本坐头一版把两个 epoch 之数凭记忆写死，**两个都错**
    #   （写了 1758024000，而 2026-09-16 12:00:00 实係 1789560000）——**自测当场红**。
    #   ★**通例**：**一个数若能由它自己那句话算出来，就不许另抄一个记忆里的数进来。**
    _早 = _步之时({'时': '2026-09-16 11:00:00'})
    _晚 = _步之时({'时': '2026-09-16 13:00:00'})
    R.append(('⑫锁滞·心跳早於封版席毕者＝忘了撤（判起）',
               判锁滞(_步t, '9', _早) is True))
    R.append(('⑫之二 心跳晚於封版席毕者＝有人特意按上的（不判起）',
               判锁滞(_步t, '9', _晚) is False))
    R.append(('⑫之三 取不着心跳之时即退回旧判（不凭空造判据）',
               判锁滞(_步t, '9', None) is True))
    R.append(('⑫之四 步无「时」者亦退回旧判',
               判锁滞([{'事': '9·封版席毕'}], '9', _晚) is True))

    _步 = [{'事': '9·案席毕'}, {'事': '9·封版席毕'}, {'事': '存底·第9章封版'}]
    R.append(('⑩之三·锁滞之判拿假料跑得出（封版席毕＝True，别章＝False，空表＝False）',
               判锁滞(_步, '9') is True and 判锁滞(_步, '8') is False
               and 判锁滞([], '9') is False
               and 判锁滞([{'事': '9·案席毕'}], '9') is False))
    R.append(('④心跳之限自 心跳.py 现取（本器内只余一处兜底）',
              "re.search(r'^限" in 码 and 码.count('45 * 60') == 1))
    # ⑤⛔读不出心跳者作「有人在跑」论（宁可候，不可抢）
    R.append(('⑤心跳读不出即作有人论（宁可候不可抢）', '作有人论' in 码))
    # ⑥⛔本器一个字也不写盘：无写口、无删口、无外跑
    R.append(('⑥本器不动盘（无写口 open(...,\'w\')／无 remove／无 shutil）',
              ".write(" not in 码 and "os.remove" not in 码
              and 'shutil' not in 码 and "', 'w'" not in 码))
    # ⑦⛔并证它真读得着盘：末章须 >0，且其回执之查真跑过一回
    R.append(('⑦真读得着盘（末章 >0 且回执之查跑得动）',
              末章() > 0 and isinstance(回执在(末章()), bool)))
    # ⑧⛔印「欠」时必带「谁的线／哪一章是哪一条线」那一问（体检账 ㊥）
    R.append(('⑧印「欠」时必带线之问（㊥·0913 两栽之治）', '谁的物、谁的线' in 码))
    R.append(('⑨起前问云端有无「章-下」（1022 复核：⛔重写已封之章）',
              'if 云端已封(下):' in 码 and 码.index('if 云端已封(下):') < 码.index("【判】起。第%d章已封版且十一轮过")))
    R.append(('⑨之二 云端已封之判真跑得动（章-401 在云端）', 云端已封(401) is True))
    # ⑫1027 A2·死锁之治：末章已封而未入主枝 → 先治／候、⛔起下一章；【重派】之会话自章-末起，首务即此
    _红报 = ('章-410', {'ref': '章-410', 'sha': 'a' * 40, '果': '红', '红': ['✗ 质量三闸  一章一日'], 'run_url': 'u'})
    _治1 = 前章之治(410, 本封=lambda n: True, 封=lambda n: True, 主=lambda n: False, 坏=lambda n: _红报)
    _治2 = 前章之治(410, 本封=lambda n: True, 封=lambda n: True, 主=lambda n: False, 坏=lambda n: (_红报[0], dict(_红报[1], 果='拒')))
    _候 = 前章之治(410, 本封=lambda n: True, 封=lambda n: True, 主=lambda n: False, 坏=lambda n: None)
    _缺 = 前章之治(410, 本封=lambda n: True, 封=lambda n: False, 主=lambda n: 1 / 0, 坏=lambda n: 1 / 0)
    R.append(('⑫末章已封未入主：报红 → 【判】治（印其红、末令 推.py）；拒 → --直；报未毕 → 【判】候（--候主）；缺章标 → 【判】治（L0 补碑）；'
              '已在主、本树未封、读崩 → 无（照常）',
              _治1 and _治1[0] == '治' and any('✗ 质量三闸  一章一日' in x for x in _治1[1]) and _治1[1][-1].strip().startswith('python3 工具/推.py ')
              and _治2[1][-1].strip().startswith('python3 工具/推.py --直') and _候[0] == '候' and '--候主 410' in _候[1][-1]
              and _缺[0] == '治' and any('L0 缺碑自补' in x for x in _缺[1]) and '--候主 410' in _缺[1][-1]
              and 前章之治(410, 本封=lambda n: True, 封=lambda n: True, 主=lambda n: True, 坏=lambda n: _红报) is None
              and 前章之治(410, 本封=lambda n: False, 封=lambda n: 1 / 0) is None
              and 前章之治(410, 本封=lambda n: True, 封=lambda n: 1 / 0) is None
              and "_治 = 前章之治(末)" in 码 and 码.index("_治 = 前章之治(末)") < 码.index('账限哨.印(ROOT, 末 + 1)')
              and 码.index("_治 = 前章之治(末)") < 码.index("【判】起。第%d章已封版且十一轮过")))
    try:   # ★1027 法用之守：【判】起 与「下一条命令」之间印 --开（N≥411）；其印 ≤10 行
        import 法用之守 as _法
        _开 = _法.开(411)
    except Exception:
        _开 = None
    R.append(('⑨之四 【判】起 之下印法用之守 --开（N≥411·≤10 行），在「下一条命令」之前',
              '法用之守.开(下)' in 码 and 码.index("【判】起。第%d章已封版且十一轮过") < 码.index('法用之守.开(下)')
              < 码.index("── 下一条命令（⛔逐条照抄，序不许换）──") and isinstance(_开, list) and 1 < len(_开) <= 10))
    import 暂停令 as _停t
    _旧哨, _旧在, _旧记 = _停t.守书之哨, _停t.在, _停t.守书停记
    import 重取 as _重t
    import 法用之守 as _法t
    _旧印, _旧报 = _重t.印, _法t.报之读
    _重t.印 = lambda 目=None: ''
    _法t.报之读 = lambda *a, **k: []         # ⛔网：前哨之报之读另格验之（⑫）
    try:   # ⑩1024：令已解而守书已停之记仍在 → 前哨红（行首⛔）；令在而未记停 → 停之判印 enabled=false 之参与 --守书已停
        _停t.守书之哨 = lambda root=ROOT: ['⛔ 守书之巡仍停：x']
        _红 = 前哨()
        _重t.印 = lambda 目=None: '⛔ 盘坏：试——照 python3 工具/重取.py 之法重 clone 换目'
        _红盘 = 前哨()
        _法t.报之读 = lambda *a, **k: ['⛔ 报·推 章-9 果「红」（试）未消']
        _红报 = 前哨()
        _法t.报之读 = lambda *a, **k: []
        _重t.印 = lambda 目=None: ''
        _停t.在, _停t.守书停记 = (lambda root=ROOT: (True, '暂停令在（试）')), (lambda root=ROOT: None)
        _判停, _L停 = 断(印=False)
        _停t.守书停记 = lambda root=ROOT: {'时': 't'}
        _判停2, _L停2 = 断(印=False)
    finally:
        _停t.守书之哨, _停t.在, _停t.守书停记 = _旧哨, _旧在, _旧记
        _重t.印, _法t.报之读 = _旧印, _旧报
    R.append(('⑪盘坏之旗在 → 前哨首行⛔ 盘坏（1024）', _红盘[:1] == ['⛔ 盘坏：试——照 python3 工具/重取.py 之法重 clone 换目']))
    R.append(('⑫报之读（1027 丝滑主义）：备份/报 未消之坏报 → 前哨⛔（盘坏之後；默印收入「前置诸哨之红」）',
              _红报 == ['⛔ 盘坏：试——照 python3 工具/重取.py 之法重 clone 换目', '⛔ 守书之巡仍停：x', '⛔ 报·推 章-9 果「红」（试）未消']))
    R.append(('⑩守书之巡：令解而停记在 → 前哨⛔红且接於报之首；令在未记停 → 停判印 enabled=false 之参与 --守书已停；已记 ⛔复印',
              _红 == ['⛔ 守书之巡仍停：x'] and 'for _l in 前哨():' in 码.split('def 报():')[1][:80]
              and _判停 == '停' and any('"enabled": false' in x for x in _L停) and any('--守书已停' in x for x in _L停)
              and _判停2 == '停' and not any('enabled' in x for x in _L停2)))
    # ⑬1027 执行之审 #63：残树之检（注入 git 之出）——已并之树／枝计之；在用之树、主树、本枝、未并者⛔计
    _wl = ('worktree /r\nHEAD a\nbranch refs/heads/main\n\nworktree /r/w1\nHEAD b\nbranch refs/heads/fayong/a\n\n'
           'worktree /r/w2\nHEAD c\nbranch refs/heads/zx/b\n\nworktree /r/w3\nHEAD d\nbranch refs/heads/未并\n\nworktree /r/w4\nHEAD e\nbranch refs/heads/在用枝\n')
    _出 = {'rev-parse': '本枝\n', 'worktree': _wl, 'branch': 'main\n本枝\nfayong/a\nzx/b\n在用枝\n旧枝甲\n'}
    _树, _枝 = 残树(跑=lambda *a: _出[a[0]], 在用=lambda 路: 路 == '/r/w4')
    _净 = 残树(跑=lambda *a: {'rev-parse': '本枝\n', 'worktree': 'worktree /r\nHEAD a\nbranch refs/heads/本枝\n', 'branch': '本枝\n'}[a[0]])
    R.append(('⑬残树（#63）：已并之树 2（w1、w2）、枝 1（旧枝甲）→ ⚠；主树、本枝、未并、在用之树⛔计；俱无 → ⛔印（放行之反例）；崩 → 无',
              _树 == ['/r/w1', '/r/w2'] and _枝 == ['旧枝甲'] and 残树之印((_树, _枝))[0].lstrip().startswith('⚠ 已并而未删之 worktree 2／枝 1')
              and _净 == ([], []) and 残树之印(_净) == [] and 残树(跑=lambda *a: 1 / 0) == ([], [])
              and '残树之印()' in 码.split('def 断(')[1]))
    # ⑬之二（1117·法用#停钩空转之审）：本树泊於「章-459」，主枝为 HEAD 之祖（--merged 列之）而⛔检出於任一树 → 主枝⛔计（旧判报之并教 git branch -d 主枝）；
    #   他树检出主枝者亦⛔计其树；他之已并之枝照计（回灌：去其⛔即红）；主枝之名与 推报、存底 同（⛔两把尺）
    _泊wl = 'worktree /r\nHEAD a\nbranch refs/heads/章-459\n\nworktree /r/w5\nHEAD a\nbranch refs/heads/%s\n' % 主枝
    _泊出 = {'rev-parse': '章-459\n', 'worktree': 'worktree /r\nHEAD a\nbranch refs/heads/章-459\n', 'branch': '章-459\n%s\n' % 主枝}
    _泊 = 残树(跑=lambda *a: _泊出[a[0]])
    _泊树 = 残树(跑=lambda *a: dict(_泊出, worktree=_泊wl)[a[0]], 在用=lambda 路: False)
    _泊他 = 残树(跑=lambda *a: dict(_泊出, branch='章-459\n%s\n治-0123456789ab\n' % 主枝)[a[0]])
    _游离 = 残树(跑=lambda *a: {'rev-parse': 'HEAD\n', 'worktree': 'worktree /r\nHEAD a\ndetached\n',
                                'branch': '(HEAD detached from e2b4553e3)\n%s\n' % 主枝}[a[0]])
    try:
        import 推报 as _报t, 存底 as _底t
        _同名 = 主枝 == _报t.主枝 == _底t.主枝
    except Exception:
        _同名 = False
    R.append(('⑬之二 泊於「章-459」而主枝已并（--merged 列之·⛔检出）→ 残树⛔计主枝（枝与树俱然）、⛔教 git branch -d 主枝；他之已并之枝（治-…）照计；'
              '游离之「(HEAD detached …)」⛔作枝；主枝之名与 推报／存底 同',
              _泊 == ([], []) and 残树之印(_泊) == [] and _泊树 == ([], []) and _泊他 == ([], ['治-0123456789ab'])
              and not any(主枝 in x for x in 残树之印(_泊他)) and _游离 == ([], []) and _同名))
    # ⑭1027 执行之审 #1 #71 #78：卡死之印⛔含「报作者」；账限之欠⛔教无数之「延：」
    _欠印 = 码[码.index("【判】欠。瑕疵总账之限"):][:200]
    R.append(('⑭卡死之印⛔含「报作者」（第一律·自决：换法自通、办毕报所为）；账限之欠印「延至 NNN」、⛔教无数之「延：<由>」',
              '报作者' not in 码 and '换法自通' in 码 and '延至 NNN' in _欠印 and '「延：<由>」' not in _欠印))
    for 名, o in R:
        print(('  ✓ ' if o else '  ⛔ ') + 名)
    print('  自测 %d/%d%s' % (sum(1 for _, o in R if o), len(R), ' 全通' if all(o for _, o in R) else ' 未过'))
    return all(o for _, o in R)


if __name__ == '__main__':
    if '--自测' in sys.argv:
        sys.exit(0 if 自测() else 1)
    if '--全' in sys.argv:
        报()
        sys.exit(0)
    # ★1021 作者令「⛔运行跟弱智一样」＋省律：旧每跑印百五十余行、新人每回通读——今默只印前置诸哨之红与「此刻该干哪一件」一节；
    #   诸哨照旧全跑（其副作用如存底、自推照旧），只是⛔把绿的与说教之文灌进上下文。全文：--全。
    import subprocess as _sp0
    _r0 = _sp0.run([sys.executable, os.path.abspath(__file__), '--全'], capture_output=True, text=True, timeout=900)
    _出0 = _r0.stdout.splitlines()
    _i0 = next((k for k, l in enumerate(_出0) if '════ 自走 · 此刻该干哪一件' in l), None)
    _头0, _尾0 = (_出0[:_i0], _出0[_i0:]) if _i0 is not None else ([], _出0)
    _见0, _红0 = set(), []
    for _l0 in _头0:
        _x0 = _l0.strip()[:160]
        if _x0.startswith(('⛔', '⚠')) and '永远的痛' not in _x0 and _x0 not in _见0:   # 只取真报警之行（行首⛔／⚠），说教与已成之件⛔取
            _见0.add(_x0); _红0.append(_x0)
    if _红0:
        print('── 前置诸哨之红 %d 条（全文：python3 工具/自走.py --全）──' % len(_红0))
        print('\n'.join('  ' + x for x in _红0[:12]) + ('\n  ……另 %d 条' % (len(_红0) - 12) if len(_红0) > 12 else ''))
    print('\n'.join(_尾0))
    if _r0.returncode != 0 and _r0.stderr.strip():
        print('  ⛔自走自身之错：' + _r0.stderr.strip().splitlines()[-1][:200])
    sys.exit(0)
