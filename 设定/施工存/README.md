# 施工存（1120 立·作者令「把所有的任务认认真真的保存在这个GitHub上面……下次启动……知道具体做到什么地方」）

施工树（scratchpad 下之 git worktree）随容器而亡；凡未入主枝之施工，俱以此目录存於主枝，⛔只在本机。
总交接见 `设定/总编辑交接.md`（先读其〇节）。本目录只是「物」，「做到何处、下一步、细法」俱在总交接。

| 档 | 是什么 | 基 | 复原之令（於仓根跑） |
|---|---|---|---|
| W912.bundle | W912 一轮之施工枝（5 提交：e42c6a313 开 → 7668cfe38 → bf2dd9b26 一轮 → 9cbc16a9c 并主枝 → 848ea9bf0 账并㊳），俱签 | 主枝 ea83111c9 之祖 | `git fetch 设定/施工存/W912.bundle 施-W912:施-W912` |
| W912.diff | 同上之可读之 diff（13 档 +2003 −39；对主枝之 merge-base） | — | 只读 |
| W912_未提交.diff | wt912 之未提交之改（1120 19:30 UTC 存·98 行）：设定/方案/W912.md 二轮之全（逐环 7—12、兜底之隔、图之用增行、合计〔一轮实 $68.29〕、坑之检二轮）＋设定/工作流账.json W912 之裁「续」（15:10Z）与时限 9.0——二轮稿.md 所无者俱在此 | 施-W912（848ea9bf0）之上 | 复原 bundle 後於其树 `git apply 设定/施工存/W912_未提交.diff` |
| W912_二轮稿.md | W912 二轮（环7—12）之逐环表稿：版之鲜、取须见其亮、待入之账、图之自随、自入可裁、怀疑之验 | — | 只读；入 W912.md 之逐环表 |
| W913.bundle | W913 之施工枝（2 提交：6ff2e12ef 方案定稿＋费账 → 5c879571c 再复审六险之纳＋费账） | 主枝 9e2b48095 之上 | `git fetch 设定/施工存/W913.bundle 施-W913:施-W913` |
| W913.md | W913 方案定稿（约 130KB·首审 39 险＋复审 13 险＋再复审 6 险俱纳） | — | 复原後在 设定/方案/W913.md |
| W914.bundle | W914 之施工枝（1 提交 0061b3af2：方案定稿＋费账） | 主枝之上 | `git fetch 设定/施工存/W914.bundle 施-W914:施-W914` |
| W914.md | W914 方案定稿（执行之清·纳预审 27 险） | — | 复原後在 设定/方案/W914.md |
| W914_裁表.md | W914 之 42 件之裁表（接／汰／留／判误／归W913）之稿 | — | 只读 |
| W915_稿.md | W915 反bug之机之稿（含「待纳之环」：预审之复、禁字之免之守） | — | 只读；预审前入 设定/方案/W915.md |
| 本周预算.md | 1120 立之本周余量之预算（作者告余 25%） | — | 只读 |
| 预审之档/*.json | 预审之 Run 之档（wf_33599ddb-aed W913 首审、wf_3c935b8b-2d0 W913 复审、wf_a76cd78c-d81 W914 预审、wf_84e5fa60-474 W912 二轮预审·中止、wf_3761bb37-542 W913 再复审） | — | 见下「深验之复」 |

## 深验之复（`工作流账.py --开 W913／W914` 之前必办）

`工具/方案.py` 之 预审之深验 读 `~/.claude/projects/*/*/workflows/<Run>.json`；新容器无之即「拒开」。复之：

```bash
mkdir -p ~/.claude/projects/施工存/复/workflows
cp 设定/施工存/预审之档/*.json ~/.claude/projects/施工存/复/workflows/
python3 -c "import sys,datetime;sys.path.insert(0,'工具');import 方案;print(方案.预审之深验('W913','.',datetime.datetime.now(datetime.UTC)))"   # 须 ([], [])
```

（Run 之 json 内含其脚本全文〔script〕，⛔赖 scriptPath。）

## 复原施工树之式

```bash
git fetch 设定/施工存/W913.bundle 施-W913:施-W913
git worktree add <scratchpad>/wt913 施-W913
cd <scratchpad>/wt913 && git merge --no-edit origin/claude/the-novel-review-4dtuit   # 并今之主枝（费账、法用册之冲由 账并 之驱自并）
```
