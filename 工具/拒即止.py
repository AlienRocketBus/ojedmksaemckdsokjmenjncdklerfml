#!/usr/bin/env python3
"""拒即止（1126 立·X161 之治·法用#拒即止）——PreToolUse 钩：工作流之席（subagents/workflows/ 下之 agent 档）一见平台之检之 refusal，
其後之一切工具之调俱拒，令其席即止、交 flaws「拒」。

其由：491 执笔乙丙、492 丁己、494 甲乙俱遭平台之检拒——拒後平台自续九至十一来回、终於二拒或 invalid_request，俱无稿，三章白耗 $6.46—$8.96。
造章.js 之门（X138·拒後不再请）只管进程间⛔同令再请；席之内拒後之自续，脚本管不着——此钩管之。
此钩只令其席止，⛔改令、⛔换路、⛔重请（平台之检⛔绕）：止损而已。

判：钩之输入（stdin JSON）带 agent_transcript_path，或 agent_id（於 ~/.claude/projects/*/*/subagents/workflows/*/agent-<id>.jsonl 寻）；
其档在 subagents/workflows/ 下且有 assistant 之行 stop_reason＝refusal → 拒（permissionDecision deny）。
主会话（无 agent 之号）、非工作流之席、档不在、读崩——一律放行（⛔误拦·丝滑）。
用法：钩自跑；python3 工具/拒即止.py --自测
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账   # 每跑追一行於 _器之迹.jsonl（法用#拒即止之行为之证）
except Exception:
    pass
import glob
import json
import os
import sys

由 = ('本席已遭平台之检拒（refusal）——拒即止（X161·法用#拒即止）：⛔再调工具、⛔改措辞重试、⛔另路续写（平台之检⛔绕）。'
     '即结束本回合：StructuredOutput 若可交，只交 flaws「拒」；主环以 承.py 分因。')


def 席档(inp):
    p = inp.get('agent_transcript_path')
    if isinstance(p, str) and p:
        return p
    a = inp.get('agent_id')
    if not isinstance(a, str) or not a or '/' in a:
        return None
    根 = os.environ.get('ZM_拒即止_根') or os.path.expanduser('~/.claude/projects')
    c = glob.glob(os.path.join(根, '*', '*', 'subagents', 'workflows', '*', 'agent-%s.jsonl' % a)) + \
        glob.glob(os.path.join(根, '*', 'subagents', 'workflows', '*', 'agent-%s.jsonl' % a))
    return c[0] if c else None


def 已拒(f):
    if not f or '/subagents/workflows/' not in f.replace(os.sep, '/') or not os.path.exists(f):
        return False
    with open(f, encoding='utf-8', errors='replace') as h:
        for l in h:
            if 'refusal' not in l:
                continue
            try:
                d = json.loads(l)
            except ValueError:
                continue
            m = d.get('message') if isinstance(d, dict) else None
            if d.get('type') == 'assistant' and isinstance(m, dict) and m.get('stop_reason') == 'refusal':
                return True
    return False


def 判(inp):
    if inp.get('tool_name') in ('StructuredOutput', 'SubagentHandback'):   # 交卷之器放行：令其速交 flaws「拒」而止
        return False
    try:
        return 已拒(席档(inp))
    except Exception:
        return False


def 自测():
    import tempfile
    t = tempfile.mkdtemp()
    d = os.path.join(t, 'p', 's', 'subagents', 'workflows', 'wf_x')
    os.makedirs(d)
    行 = lambda sr: json.dumps({'type': 'assistant', 'message': {'stop_reason': sr, 'content': []}}, ensure_ascii=False)
    写 = lambda n, ls: open(os.path.join(d, 'agent-%s.jsonl' % n), 'w').write('\n'.join(ls) + '\n')
    写('拒', [json.dumps({'type': 'user'}), 行('tool_use'), 行('refusal'), 行('tool_use')])
    写('常', [json.dumps({'type': 'user'}), 行('tool_use'), 行('end_turn'), json.dumps({'type': 'user', 'message': {'content': '谈 refusal 一词'}})])
    os.environ['ZM_拒即止_根'] = t
    主 = os.path.join(t, 'p', 'main.jsonl')
    open(主, 'w').write(行('refusal') + '\n')
    例 = [('席拒（agent_id）', {'agent_id': '拒'}, True),
         ('席拒（agent_transcript_path）', {'agent_transcript_path': os.path.join(d, 'agent-拒.jsonl')}, True),
         ('负：席常（字中有 refusal 而无拒）', {'agent_id': '常'}, False),
         ('负：主会话之拒（无 agent 号）', {'transcript_path': 主}, False),
         ('负：非工作流之档', {'agent_transcript_path': 主}, False),
         ('负：档不在', {'agent_id': '无此席'}, False),
         ('负：号带路', {'agent_id': '../x'}, False),
         ('负：拒席交卷（StructuredOutput 放行）', {'agent_id': '拒', 'tool_name': 'StructuredOutput'}, False)]
    败 = [n for n, i, 期 in 例 if 判(i) != 期]
    for n in 败:
        print('✗', n)
    print('拒即止自测 %d/%d' % (len(例) - len(败), len(例)))
    return 0 if not 败 else 1


def main():
    if '--自测' in sys.argv:
        sys.exit(自测())
    try:
        inp = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    if isinstance(inp, dict) and 判(inp):
        print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'permissionDecision': 'deny',
                                                 'permissionDecisionReason': 由}}, ensure_ascii=False))
    sys.exit(0)


if __name__ == '__main__':
    main()
