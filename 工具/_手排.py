# -*- coding: utf-8 -*-
"""〔W919·坑66〕手排之账⛔整写：手排之 JSON 账（法用册、写者册、大审专问……一行之元与多行之元混排）以 json.dump 整写即式全改、diff 失读、并时必撞。
整写之式(文)：文係 json.dumps 之某式（indent None／1／2／3／4／tab、ensure_ascii、sort_keys），或一行之档，或一行之元尽失（展开之式）→ 由；否则 None。
手排之检(root, 基)：基（与 origin/<主枝> 之分叉点；gate 之候取 HEAD^1）至 HEAD 所改之 .json——基之文手排（整写之式 None）而 HEAD 之文整写之式 → 红。
基已整写（机写之账：费账、工作流账……）、新档、无基 → ⛔判（自测之造局亦免）。库（工具/_*.py）：推.py 速检、全测之格、法用之守 自测 共用。"""
import json, re, os, subprocess
_内联 = re.compile(r'^\s*(?:"[^"]*"\s*:\s*)?([\[{]).*([\]}]),?\s*$')
def 内联数(文):
    n = 0
    for l in 文.split('\n'):
        m = _内联.match(l)
        if not m or l.strip() in ('{}', '[]', '{},', '[],'):
            continue
        s = l.strip().rstrip(',')
        s = re.sub(r'^"[^"]*"\s*:\s*', '', s)
        try:
            v = json.loads(s)
        except Exception:
            continue
        if isinstance(v, (dict, list)) and v:
            n += 1
    return n
def 有套(o):
    if isinstance(o, dict): return any(isinstance(v,(dict,list)) and v for v in o.values()) or any(有套(v) for v in o.values())
    if isinstance(o, list): return any(isinstance(v,(dict,list)) and v for v in o) or any(有套(v) for v in o)
    return False
def 整写之式(文, 基文=None, 增删=None):
    """→ None（手排）｜由（整写之式）。「一行之元尽失」之支须 基文 之内联 ≥3 且 增删（numstat 增＋删）≥50 或 ≥ 基档行数之二成（W919 预审·b5a0f80cf 之小改⛔误红）"""
    try: o = json.loads(文)
    except Exception: return None
    for ind in (None, 1, 2, 3, 4, '\t', ' '):
        for ea in (False, True):
            for sk in (False, True):
                s = json.dumps(o, ensure_ascii=ea, indent=ind, sort_keys=sk)
                if 文.rstrip('\n') == s:
                    return 'json.dump 之式（indent=%r, ensure_ascii=%s, sort_keys=%s）' % (ind, ea, sk)
    if 文.count('\n') <= 1 and len(文) > 200:
        return '一行之档（整写）'
    if (有套(o) and 内联数(文) == 0 and 基文 is not None and 内联数(基文) >= 3
            and 增删 is not None and (增删 >= 50 or 增删 >= 0.2 * max(1, 基文.count('\n')))):
        return '一行之元尽失（展开之式：整写）'
    return None


def 手排之检(root, 基):
    """→ [红之行]。"""
    if not 基:
        return []
    r = subprocess.run(['git', '-c', 'core.quotepath=off', 'diff', '--name-only', '--diff-filter=M', 基, 'HEAD', '--', '*.json'], cwd=root, capture_output=True, text=True)
    出 = []
    for 路 in [x for x in r.stdout.split('\n') if x.strip()]:
        b = subprocess.run(['git', 'show', '%s:%s' % (基, 路)], cwd=root, capture_output=True, text=True)
        h = subprocess.run(['git', 'show', 'HEAD:%s' % 路], cwd=root, capture_output=True, text=True)
        if b.returncode or h.returncode:
            continue
        try:
            json.loads(b.stdout)
        except Exception:
            continue
        if 整写之式(b.stdout) is None:
            ns = subprocess.run(['git', '-c', 'core.quotepath=off', 'diff', '--numstat', 基, 'HEAD', '--', 路], cwd=root, capture_output=True, text=True).stdout.split()
            增删 = (int(ns[0]) + int(ns[1])) if len(ns) >= 2 and ns[0].isdigit() and ns[1].isdigit() else None
            由 = 整写之式(h.stdout, b.stdout, 增删)
            if 由:
                出.append('  ✗ 手排之账整写（坑66）：%s——%s；以 git checkout %s -- %s 复其式、只行改（Edit／定点之串换），json.load 验义同' % (路, 由, 基[:12], 路))
    return 出


if __name__ == '__main__':
    import sys
    _根 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if sys.argv[1:2] == ['--自测']:
        _旧 = '{\n "法": [\n  {"id": "a", "证": [{"档": "x"}]},\n  {"id": "b", "证": [{"档": "y"}]},\n  {"id": "c", "证": [{"档": "z"}]}\n ]\n}\n'
        _o = json.loads(_旧)
        _展 = json.dumps(_o, ensure_ascii=False, indent=2).replace('\n  ', '\n   ') + '\n\n'
        _局 = [('手排之文 → None', 整写之式(_旧) is None),
              ('json.dump(indent=1) 之整写 → 判', bool(整写之式(json.dumps(_o, ensure_ascii=False, indent=1), _旧, 20))),
              ('展开之式（非 dumps 之式）·基内联 3·增删 20（逾二成）→ 判', bool(整写之式(_展, _旧, 20))),
              ('展开之式·基内联 <3（b5a0f80cf 之形：去其唯一一行之元 env）→ 静', 整写之式('{\n  "allow": [\n    "Bash"\n  ],\n  "ttl":"1h"\n}', '{\n  "allow": [\n    "Bash"\n  ],\n  "env": {"A": "1"}\n}', 2) is None),
              ('展开之式·增删 <50 且 <二成 → 静', 整写之式(_展, _旧 + '\n' * 200, 20) is None),
              ('一行之改（加 "轻": true）→ 静', 整写之式(_旧.replace('"x"}', '"x", "轻": true}'), _旧, 2) is None)]
        for _名, _果 in _局:
            print(('✓ ' if _果 else '✗ ') + _名)
        print('_手排·自测 %d/%d' % (sum(1 for _, x in _局 if x), len(_局)))
        sys.exit(0 if all(x for _, x in _局) else 1)
    if sys.argv[1:2] == ['--检']:
        _基 = sys.argv[2] if len(sys.argv) > 2 else 'HEAD^1'
        _r = subprocess.run(['git', 'rev-parse', '--verify', '-q', _基], cwd=_根, capture_output=True, text=True)
        红 = 手排之检(_根, _r.stdout.strip()) if _r.returncode == 0 else []
        print('\n'.join(红) or '✓ 手排之检：本推无手排之账被整写')
        sys.exit(1 if 红 else 0)
