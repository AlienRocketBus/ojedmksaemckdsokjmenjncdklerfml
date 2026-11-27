# -*- coding: utf-8 -*-
"""负测 · 造章令（1020 W53·治席 G3 立·瑕疵总账 X13／X14／X26）

★造章.js 之令逐字渲染而验（node 跑其全流，诸席之交以假交代之，只收令、schema、effort）——四件：
  ①续跑之缓存（1017 作者铁律③）：N≤397 之诸令（连 schema、effort），390—397 八章×三重（轻中重）×二路（净／回写）渲染之 sha256，
    与改前之造章.js（git c299dc4c 之版，sha256 84810dae…）之基逐一同——**⛔一字之改、⛔键之换序**
    （指以原序 JSON 算：schema 之键换序即令请求之字节变、缓存即破；旧以 sort_keys 算，换序验不出——W53 验席逮）；
    390 守 N<391 之枝（无「此法之缺」），391—397 守诸枝之界。新令只许以 N≥398 之条件加。
  ②X26：N≥398 之执笔令「首回即落」——**首条消息**同发 Read 料（allow_large）与一条 Bash「cat > 构思」建档
    （392—397 三十四席读料俱用 Read，⛔以 Bash cat 读料：料逾四万字，回显只留首 2KB——W53 验席逮上回之令「读料之命令末接 cat >」之假前提）；
    想定一样以 cat >> 追记一样、全章之排在档上排（满分之问先落，拍表随第一拍落）；回数之限 28；旧「构思可先落一回」⛔再见。
  ③X14：N≥398 之盲读分二类报——schema 带 prior；①只算本章之卡、①之二前情之指⛔计入读不懂；逻辑审并入回述实证；记席录之。
  ④X13：N≥398 之记令於立卡後跑「第零轮开镜庭.py --静 N+1」，十四格（卡之自牵）红即改卡。
  ⑥X40（1020 立·裁_1020_推闸二红_399封版後）：args.须厚（自走.py 之派令以 分量闸.须厚 现判）且 N≥401 → 诸执笔令带「【硬项·须厚】本章之事须担得起 2,900 净重」、
    选令带「须厚之章，净重 <2,900 之稿作底须写其由」；N≤400 传 须厚 亦⛔认（400 之诸令与不传者原序之指同）、401 不传者⛔带。
  ⑦★1024 省 token 之审（records②③／seats①②／failures①②）——N≥411 之新行，N≤410 一字不变：
    ①之二：398—410 诸令之 sha256（改前之造章.js·c2659cdc 之版所渲，轻中重×净病择四局、401 起另带须厚）逐一同；
    通式：411 诸席（连回写、查席）传同一 schema（键 ASCII、各子式之 required 同 410 之旧式、顶层 minProperties:1）、令末「只填『X』一键」；
    交空对象即补派（执笔先查後补、选、合、盲、逻辑审·1、记席）；查收盘稿即⛔补；逻辑审·1 二回空即停；布尔严判（misread 交「否」⛔作读误，410 照旧）；
    回写之令实一字不动（411 去交之一句＝410 之令换号）；记令四刀（{done,left}、式取记料【一】、--前 --红 复跑）；
    窄审：第1回只读误者逻辑审·2 带窄审之门（稿差.py）、第1回之令记「据 正文＝vNN」、soft 并入第1回；有硬崩者照旧全审；承能拆键（承.py 之必填表＝通式之 required）。
    合流（B、C 二组之令）：411 执笔之【量】带「硬项只照 --量 所印之处」；记令带 记落.py 之末步、‹器:键› 诸占位、②之锚独立、主环之职栏⛔治；410 二者俱⛔带。
  ⑧X62（1027·X58 之余）：411 选之先跑一条命令并印诸稿净重（净重对表 --量）与诸稿亮点所引之原场（章料 --稿引）、限 5；合核胜稿之原场同器；
    逻辑审先跑并展正文亮点之引、限 8；410 之令照判俱红；选令之 --稿引 命令真跑於 410 之诸稿。
  ⑨X88／X89（1106）：N≥431 之执笔令带「构思档只录定案」「前章原字之限」二条；N≤430 ⛔带。
  ⑩X95①（1111）：N≥442 之记令带「一事一处」（本章之事详写只在全书记忆、回执与创作记录⛔复述）；N≤441 ⛔带。
  ⑭X79 R（1118 总编辑裁）：补派之「安全拒」之滤 N≥468 废（运行时之约下恒⛔行）——N≤467 诸桩局之令逐字同改前之基（_基三·已过之章、钉之）；
    N≥468 未写之章⛔钉其指（日後之令合法之改即假红）——以今之 js 与废其门之变体（改前之行）同时渲而相较：无桩、ZJ_死 诸局同，
    ZJ_拒 之混局、轻局异；混局 467 照滤、468 ⛔滤（补乙·令同今渲之 ZJ_死 三席之局）。
  ⑯X119（1119）：N≥471 args.带（段案本章「字数」）→ 诸执笔令【厚】首句「本章之带＝a—b·唯此为准」；N≤470 ⛔认。
  ⑰〔1119 死规之审〕N≥473 之令只拔逐章配额之牙（叫绝之拍逐章必有、带为标的「唯此为准／低於带不许交／带下⛔作胜稿」、须厚之硬项与选之门、
    长段之额、零数之日之补）——N≤472 诸令逐字同改前之基（_基四·468—472·git 0f8afe5d9 之版·sha256 d159af96…）；
    473 之令验新语在、旧牙⛔见，守牙仍在（铁底 2,000、硬项、致命之器、开镜卡所定之拍落到顶、咬合之令全文）；schema 与 effort 不动；
    〔1119 死规之审·复核〕咬合每五章之额（gates16／prompts7）退回：咬合哨、chk_yaohe 照硬，合令之咬合哨全文 473 照留（守牙验之）；
    盲读、逻辑审、回写之令与「⛔死规审」之变体同（⛔顺手改）。回灌：472 之令与 473「⛔死规审」之变体照 ⑰ 之判俱红。
  ⑱治16（1124·W918 环4·执行之制 批四 A4）：盲读 want_next=false → N≥485 另立「不想」之支——「回写·好看」一席（以 why_next 所指之卡处为的、
    ⛔加钩⛔掐尾吊人⛔加解释句·引复核账 0925 二废）→「盲读·2·好看」；仍不想即 log「好看之欠」、入果与下一步（复盘）、照常续记席——⛔设 misread、⛔入 病() 与 X82 之停支；
    回写或盲读·2 遇拒或 null ⛔同令再请（X138·即续记席、log 其因）；总编辑之裁在⛔派。N≤484 诸令（连 ZJ_不想 之局）逐字同改前之基（_基五·473—484·git 891fc0574
    之版·sha256 4b386588…）；485 想之局与「⛔好看门」之变体逐字同；不想之局只多二席、余席除记席外逐字同。回灌：门误书作 484 即 _基五 之 484 不想三局变；
    「⛔好看门」之变体照判新条俱红、守（⛔停、⛔设 misread）俱绿；「视同 misread」（不想并入 病()）之变体守即红。假交添 ZJ_不想（[label]·末 * 为前缀）、ZJ_写否，并收 log。
  ⑲〔W919·X138·法用#拒後不再请〕N≥489 进程内⛔同令再请（只改控制之流·诸令一字⛔动）：⑲之一 485—488×十局之令、席序、果、抛逐字同 W919 入主前之基（_基六·9a8c81b34）；
    ⑲之二 489 首跑之席＝改前之行去「·补」；⑲之三 <3 即抛、补席之外⛔补、无二稿之录而二稿即抛、一稿即抛；⑲之四 补席之令逐字同原令、承前永⛔；
    ⑲之五 选／合稿／盲读／逻辑审·1／·2／记席 null 即抛、盲读之壳即停；⑲之六 476—484 亡席之回放（门假 0）派席同 9/9；⑲之七 门之数三书同（造章.js、承.py、续跑之守.py）；
    ⑲之八 端到端（Run1 真渲之收 → 承 分因 → _承.js 之 args 顶层 → 再渲只派「执笔·甲·补」）；⑲之九 重造除席；
    ⑲之十〔落地之查·病三〕盲读令(2) 一令二席（盲读·2 null → 盲读·2·好看 ⛔派）、args.已拒 之席⛔派而照 null 之法续、488 照旧；⑲之十一 端到端（盲读·2 拒、记席断 → 分因 已拒 → 再渲⛔派 盲读·2）；
    ⑲之十二〔W924·501〕一稿之路（无 args.一稿 而一稿即抛；args.一稿 而一稿 → 过造之门、⛔派执笔、选至记席照跑；一稿而 0 稿即抛；无诸稿之列即抛）；⑲之十三 端到端（五拒一交 → 分因 rc 3 → --一稿 → 再渲）；
    ⑲之十二之二 无一稿之参 → 489 十局与「一稿恒假」之变体逐字同、488 带一稿之参照 _基六；⑲之七之二 整稿之界三书同（造章.js 之门、承.整稿之界、续跑之守之二录）。
    回灌：去门之变体俱红、键位移入 args.承 之变体 ⑲之八 红。
  回灌：②③④之判拿 397 之令（旧病）去判，须一一红；上回之假前提（读料之 Bash 末接 cat > 构思）、「思考里只想眼下这一拍」之牵灌回须红；
    ①之指换键序须变——证其判咬得住，⛔一律判过。
⛔限：渲染证得了「令里写了」，证不了「席守了」——守没守归 `工具/费审.py` 之「构思」「构思隔」两列（首落逾五分、诸写最长隔逾十分即⛔）。
用法：python3 工具/负测_造章令.py
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import os, sys, re, json, hashlib, subprocess, tempfile, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = os.path.join(ROOT, '工具', '席', '造章.js')

# 假交：label 定其交；逻辑审·1 於「病」路交硬崩与读误，令回写、盲读·2、逻辑审·2 俱跑
_器 = r"""
const fs = require('fs')
const [, , 档, n, 重, 病, 厚, 空 = ''] = process.argv
const src = fs.readFileSync(档, 'utf8').replace(/^export const meta/m, 'const meta')
const N = Number(n)
const 收 = []
const 日 = []   // ★1124 治16：log 之收（好看之欠、X138 之因俱验其 log）
// ★1124 治16：ZJ_不想＝[label]（末 * 为前缀）——其盲读交 want_next:false、why_next「不想之由·<label>」；不设者旧行不变（want_next:true、why_next「想」）
const 不想们 = process.env.ZJ_不想 ? JSON.parse(process.env.ZJ_不想) : []
const 不想 = l => 不想们.some(x => l === x || (x.endsWith('*') && l.startsWith(x.slice(0, -1))))
const 交 = (label) => {
  if (label.startsWith('执笔')) return { file: '版本/第' + N + '章/起草_稿一.md', beats: 5, words: 2800, soul: '魂', best: '最好', weak: '最弱', plan: '写法' }
  if (label.startsWith('选')) return { ranking: ['稿一', '稿二'], why: '由', fatal: [{ id: '致命1', draft: '稿一', quote: '句', against: '1:1', fix: '治' }], leap: [{ id: '大进1', win_quote: '甲', better_quote: '乙', gain: '得' }], common_fatal: '', beat_scores: '拍分', peaks: '叫绝' }
  if (label.startsWith('合稿')) return { file: '正文/x.md', beats: 5, words: 2800, base: '稿一', fatal_done: '治毕', leap_done: '嫁', peaks: '叫绝', gates: '器', gates_green: true, reds: '', ledger: '账', recap: '前情' }
  if (label === '逻辑审·1' && 病 === '串') return { hard: [], soft: '软', gate: '闸', misread: '否' }   // 布尔严判之验（旧以真值判）
  if (label.startsWith('盲读') && 壳们.some(k => label.startsWith(k))) return { understood: false, confused: '', misread: '', want_next: true, why_next: '', happened: '未交：答被安全分类器截停', remember: '', prior: '' }   // ★W919 ⑲：盲读之壳（ZJ_壳）
  if (label.startsWith('盲读')) return { understood: false, confused: '卡' + label, misread: '错', want_next: !不想(label), why_next: 不想(label) ? '不想之由·' + label : '想', happened: '事', remember: '记', prior: '前情之指' }
  if (label === '逻辑审·1') return 病 === '病' ? { hard: [{ kind: '因果断', where: '1:1', what: '断', proof: '据' }], soft: '软', gate: '闸', misread: true, misread_where: '处', misread_fix: '治' } : { hard: [], soft: '软', gate: '闸', misread: false }
  if (label.startsWith('逻辑审')) return { hard: [], soft: '软2', gate: '闸2', misread: false }
  if (label.startsWith('记席')) return { receipt: '回执', lock_row: '行', memory: '忆', next_card: '卡', open_brief: '推' }
  return '办毕'
}
// ★1024 通式（N≥411）：交包於其键；空＝逗号相隔之 label（末 * 为前缀）交 {flaws} 之空对象；「查收」令查席交盘稿
const 空们 = 空 ? 空.split(',') : []
const 通键 = l => l.startsWith('执笔') ? 'draft' : l.startsWith('选') ? 'pick' : l.startsWith('合稿') ? 'merge' : l.startsWith('盲读') ? 'blind'
  : l.startsWith('逻辑审') ? 'audit' : l.startsWith('记席') ? 'record' : 'rewrite'
const 空稿们 = process.env.ZJ_空稿 ? JSON.parse(process.env.ZJ_空稿) : []   // ★1119 X118：[label 之前缀]——其执笔交 draft 而 file 空、words 0
const 交通 = (label, prompt) => {
  if (空稿们.some(k => label.startsWith(k))) return { draft: { file: '', beats: 0, words: 0, soul: '' }, flaws: '无' }
  if (label.endsWith('·查')) { const m = /--查 \S+ (\S+)/.exec(prompt); return 空们.includes('查收') && m ? { draft: { file: m[1], beats: 3, words: 2600, soul: '魂' }, flaws: '无' } : { flaws: '无稿' } }
  if (空们.some(x => label === x || (x.endsWith('*') && label.startsWith(x.slice(0, -1))))) return { flaws: '无' }
  if (label.startsWith('记席')) return { record: { done: true, left: '无' }, flaws: '无' }
  if (label === '回写') return { rewrite: { done: true, note: '治' } }
  if (label === '回写·好看') return { rewrite: 写否 ? { done: false, note: '无可治而⛔犯三禁之处' } : { done: true, note: '治·好看' }, flaws: '无' }   // ★1124 治16（ZJ_写否：自报⛔改）
  if (label === '逻辑审·1' && 病 === '误') return { audit: { hard: [], soft: '软1', gate: '闸', misread: true, misread_where: '处', misread_fix: '治' }, flaws: '无' }
  return { [通键(label)]: 交(label), flaws: '无' }
}
const 壳们 = process.env.ZJ_壳 ? JSON.parse(process.env.ZJ_壳) : []   // ★W919 ⑲：[label 之前缀]——其盲读交安全分类器之壳；不设者旧行不变
const 拒们 = process.env.ZJ_拒 ? JSON.parse(process.env.ZJ_拒) : {}   // ★1118：{label 之前缀: 错语}——其席之 agent() 以此错拒（平台安全之检之形）；不设者旧行不变
// ★1118 总编辑复核「大师之关」→改：桩从运行时之约——ZJ_死＝[label 之前缀]：其席之 agent() 遇终错返 null（⛔throw）；parallel ⛔reject（一席之 throw 化 null）。不设者旧行不变
const 死们 = process.env.ZJ_死 ? JSON.parse(process.env.ZJ_死) : []
const 写否 = !!process.env.ZJ_写否
const agent = async (prompt, o) => { 收.push({ label: o.label, prompt, schema: o.schema || null, effort: o.effort || null }); const 拒 = Object.keys(拒们).find(k => o.label.startsWith(k)); if (拒) throw new Error(拒们[拒]); if (死们.some(k => o.label.startsWith(k))) return null; return N >= 411 ? 交通(o.label, prompt) : 交(o.label) }
const parallel = async (fs_) => Promise.all(fs_.map(f => Promise.resolve().then(f).catch(() => null)))
const AF = Object.getPrototypeOf(async function () {}).constructor
new AF('args', 'agent', 'parallel', 'phase', 'log', src)(Object.assign(厚 === '厚' ? { 章: N, 重, 须厚: true } : { 章: N, 重 }, process.env.ZJ_ARGS ? JSON.parse(process.env.ZJ_ARGS) : {}), agent, parallel, () => {}, s => 日.push(String(s)))
  .then(r => process.stdout.write(JSON.stringify({ 收, 果: r, 日 })))
  .catch(e => { if (process.env.ZJ_抛) { process.stdout.write(JSON.stringify({ 收, 果: null, 日, 抛: String(e && e.message || e) })); return }   // ★W919 ⑲：抛之语亦收（ZJ_抛）
    process.stderr.write(String(e && e.stack || e)); process.exit(3) })
"""

# ①之基：改前之造章.js（git c299dc4c 之版·sha256 84810dae…）渲染所得、以原序 JSON 算——N≤397 之令⛔动、⛔换序
_基 = {"390轻净": "446235d2ae12bfba", "390轻病": "c3b7b946890cc774", "390中净": "4c039e947b88a4a5", "390中病": "2637239d514be0cc",
      "390重净": "e962618acc460b20", "390重病": "7376f43ef2c8f1b4",
      "391中净": "d81731e5a2dea60b", "391中病": "d8df30474c07d5eb", "391轻净": "2ef492c74b0b1c20", "391轻病": "25202b027ddbd821",
      "391重净": "5a08da748604da17", "391重病": "c8ed175f14e8b3c4", "392中净": "c4a354ffca3e63ee", "392中病": "e8d88c9b7b026432",
      "392轻净": "21148e279fff6a2e", "392轻病": "fa1e4966a4c70230", "392重净": "d3c0a29713e4a2d5", "392重病": "0094443a0ddedfae",
      "393中净": "7306c13984cf3c5e", "393中病": "b98108879d0ec573", "393轻净": "836cab91bef46d4c", "393轻病": "be2746a40f57838b",
      "393重净": "8c55b4f8d50995fa", "393重病": "3dc6098873b8147b", "394中净": "f986b2cbaf38e5ca", "394中病": "3f29cde7a5094979",
      "394轻净": "801ee39fe9f1a7c1", "394轻病": "c58dbe02c4a36d3a", "394重净": "12e5ad7ec936c3a7", "394重病": "fb064f52de193a1e",
      "395中净": "a42aa5140441d7f1", "395中病": "c1ad447e9931274f", "395轻净": "d82459e843fbffeb", "395轻病": "2c0775a51a2be9ae",
      "395重净": "37009624103bce82", "395重病": "fd95b43fa75a8a9b", "396中净": "cbf17443256db523", "396中病": "e4d2a0c73aeada3e",
      "396轻净": "f9c81aae5e0080fa", "396轻病": "d08aab083108656a", "396重净": "68e35a52033e2415", "396重病": "05a98b9f58006d82",
      "397中净": "c582cc7d1b2eb860", "397中病": "2fe8c3db8e3f2603", "397轻净": "d2f7c5b79f2e31e4", "397轻病": "1ca55a9cd69543c6",
      "397重净": "51e00fda90975036", "397重病": "2ee9fe5da8bd43e0"}

# ①之二（1024 立）：398—410 之基——改前之造章.js（git c2659cdc 之版）所渲、原序 JSON；N≤410 之令⛔动、⛔换序（通式等新行只走 N≥411）
62
_基二 = {"398轻病": "b043bdd206d3a656", "398中净": "73bdff10966a522d", "398中病": "21a09b28c87b3264", "398重净": "a9f3ff5d7c1f8de3", "399轻病":
      "be3913b136a3eaab", "399中净": "3d9d4176cffcb8ba", "399中病": "550206833592cc37", "399重净": "57259bae95edf249", "400轻病": "cc2722f80b290c66",
      "400中净": "cd63e765854c9528", "400中病": "2f0f9f8a927a7d5a", "400重净": "f8af0f233433f30c", "401轻病": "a099e494702cae64", "401中净":
      "ebe0464da8d040f3", "401中病": "03365259c1a77674", "401中病厚": "fcb4d740715963fe", "401重净": "81cb569f4a2e5401", "402轻病": "a5439713032de288",
      "402中净": "ecab5acee1802de6", "402中病": "ab83ef2897f2a7ad", "402中病厚": "c3271da46a52f90b", "402重净": "895993fb1618ce0c", "403轻病":
      "2fec25541a0392ab", "403中净": "f2b8f2380c4ae413", "403中病": "a888dbbd70378c4a", "403中病厚": "cd5d6088a65cae37", "403重净": "a7201e19aa55903f",
      "404轻病": "84237899e0cdf045", "404中净": "ada8eec59ede6911", "404中病": "44814d2d01a7d195", "404中病厚": "5e42ebb8141dc218", "404重净":
      "1ce08bd9bc4ae209", "405轻病": "b926801932fc47dc", "405中净": "17ef5a438de2c04d", "405中病": "76e0f82f67f0dd76", "405中病厚": "24aae86ef238650d",
      "405重净": "42874012d888b405", "406轻病": "78d18d4668fd5ce4", "406中净": "4b3d76af3158dcdc", "406中病": "081f07a566c62ed8", "406中病厚":
      "2250d46d70347dd7", "406重净": "580eb02f50afc9d5", "407轻病": "3f3630644bad9f77", "407中净": "2a7ba5f66021ff64", "407中病": "939f8277a547eed3",
      "407中病厚": "6d5367ca74b32680", "407重净": "2a7ba5f66021ff64", "408轻病": "7ee6af815adeffa6", "408中净": "5473d397060c645e", "408中病":
      "985c42cb3e4d5370", "408中病厚": "22babd03cb8c00b7", "408重净": "5473d397060c645e", "409轻病": "b24109ae94d2f39e", "409中净": "a8af6bef9a125627",
      "409中病": "6f0bfcaa993725ce", "409中病厚": "55528e6aed0df661", "409重净": "a8af6bef9a125627", "410轻病": "f8db9ae1b43a3f23", "410中净":
      "b3c8a8460bd40311", "410中病": "0053d64e255a2ba5", "410中病厚": "9d9437e0ddeb2db4", "410重净": "b3c8a8460bd40311"}

# ⑭之基（1118 总编辑裁·X79 R）：改前之造章.js（git 126ab1d8a 之版·sha256 1d0d816b…）所渲、原序 JSON——键＝章、重、桩局（见 ⑭ 之 _局）；
#   N≤467 诸桩局（无桩、ZJ_拒、ZJ_死、混）之令⛔动（已过之章·467 在写、缓存⛔破）。★N≥468 未写之章⛔入此基——
#   其令日後合法之改（如 X115 N≥467 之条）即令钉指假红、逼後来者改此不相干之测；故 ⑭ 以今之 js 对废其门之变体同时渲而相较（见 ⑭）
_基三 = {"420中净": "01b60a816dd2177e", "420中拒乙": "b2e55ed7a32ac018", "420中死乙": "b2e55ed7a32ac018", "420中死三": "c5d9b87ab6415652",
       "420中混": "fd010ce0cfe05025", "464中净": "7d02afa86e46c1f5", "464中拒乙": "2be2c28989a14209", "464中死乙": "31333f14c858d8db",
       "464中死三": "369c9772c42065b1", "464中混": "5cc95d490e6f09d4", "466中净": "c95560c2b16a4e4e", "466中拒乙": "6c434a0edba9d197",
       "466中死乙": "bd6cb7980497b614", "466中死三": "7c040a1b5889e1f6", "466中混": "89b5417c613caf21", "467中净": "c44cd2f4b2574b43",
       "467中拒乙": "16075c51cb8e8615", "467中死乙": "16075c51cb8e8615", "467中死三": "cbcf3984f52fc7fd", "467中混": "44af2cfa9fd717df",
       "467轻净": "63530afd77b6d74e"}

# ⑰之基（〔1119 死规之审〕）：改前之造章.js（git 0f8afe5d9 之版·sha256 d159af96…）所渲、原序 JSON——键＝章、重、病、厚（须厚:true）、带（args.带 2,900—3,300）；
#   N≤472 之令⛔动（已过之章与在写之章·续跑之缓存）；N≥473 之新令以 ⑰ 之判验其语（⛔钉其指：日後合法之改即假红）
_基四 = {"468中净": "f6187d67ea192d9a", "468中病": "a69517b68793d128", "468轻病": "e99aae48870e6e85", "468中病厚": "ceddbd94cb3c0ea0", "468中病带": "a69517b68793d128",
       "468中病厚带": "ceddbd94cb3c0ea0", "469中净": "8412db43f234be1f", "469中病": "3461917c86eb4b51", "469轻病": "b1725f621188a85e", "469中病厚": "ecfed1f573dba03e",
       "469中病带": "3461917c86eb4b51", "469中病厚带": "ecfed1f573dba03e", "470中净": "cf82691956a32a25", "470中病": "9f3d947e85c5a166", "470轻病": "fba86f633a51dca6",
       "470中病厚": "41a42d5eba8bc5c8", "470中病带": "9f3d947e85c5a166", "470中病厚带": "41a42d5eba8bc5c8", "471中净": "b537bd61643ba6ca", "471中病": "70e9c20582570d67",
       "471轻病": "ab3eac855a2593cf", "471中病厚": "d64a4808fdef14d6", "471中病带": "a8b38d9495b21dc1", "471中病厚带": "c26c32b8f4d62f44", "472中净": "0ecc268fe77c1684",
       "472中病": "2c87dfd356b2b854", "472轻病": "e470fd9f3844aff7", "472中病厚": "57129ef60a05105e", "472中病带": "c0e4424819c4d251", "472中病厚带": "6930649da58d6397"}

# ⑱之基（1124 治16·W918 环4）：改前之造章.js（git 891fc0574 之版·sha256 4b386588…）所渲、原序 JSON——键＝章、重、病（净／病／误）、旗（厚带：须厚＋args.带；
#   不想：ZJ_不想=["盲读*"]，诸盲读交 want_next:false）；N≤484 之令⛔动（已封之章与 484·或已开·续跑之缓存）——「不想」之局亦同（旧器於不想只入 log 与记令）。
#   N≥485 之新支以 ⑱ 之判验其行（⛔钉其指：日後合法之改即假红）
_基五 = {"473中净": "6eca6428884216bc", "473中病": "26be10b9bf38bedc", "473轻病": "8d451ede3a9fdf71", "473轻净不想": "8c04c76676d61a0a", "473中误": "abeb68e0ef24cf99", "473中病厚带": "24ae9472a4ee8c60",
       "473中净不想": "4d17e8ac56447004", "473中误不想": "5e61236b5f585158", "474中净": "ad1d1f1dc8390e65", "474中病": "e252f0e43e0dfc57", "474轻病": "a34d094fbabaea41", "474轻净不想": "242b8ac8a1f9f3d4",
       "474中误": "668ae7ee91220430", "474中病厚带": "0c48d9a34d17decc", "474中净不想": "fbcf9a0a936fffb6", "474中误不想": "0074f6921ad6f1ed", "475中净": "b860c80368b0382e", "475中病": "c466771a5d28b8db",
       "475轻病": "e3caa6f02b73b284", "475轻净不想": "486572b8078b0443", "475中误": "7f318d54ec6365c0", "475中病厚带": "c17a4176e6fd4904", "475中净不想": "c2cb62dd8a17986e", "475中误不想": "40dbce77ee2cddbe",
       "476中净": "ec4f26ee391d6836", "476中病": "4a10ad9059703320", "476轻病": "463e328fe948265b", "476轻净不想": "e1f32fb19a6bb703", "476中误": "7003b1b54627623d", "476中病厚带": "3706e376c0a41c43",
       "476中净不想": "bdd29fec7c9db9f0", "476中误不想": "5f6b2a3311646e59", "477中净": "5babef0efc577f67", "477中病": "9b3d4baf6187775a", "477轻病": "47f18c748bc21a34", "477轻净不想": "7b953f9f78c187b6",
       "477中误": "4a0fb3a8c8614751", "477中病厚带": "20259bc172ba4126", "477中净不想": "91bee90fbc928e6d", "477中误不想": "c74c58538216b61b", "478中净": "1578a00a21f2c2ee", "478中病": "7d9d123627055df2",
       "478轻病": "37f3a76eb819def9", "478轻净不想": "5f92ae846b711204", "478中误": "58fc179645d421e8", "478中病厚带": "2df4e048966ec791", "478中净不想": "772908014177cfa9", "478中误不想": "07371f3d31bdf513",
       "479中净": "c1c287d77da5fe58", "479中病": "486a357a9a99598a", "479轻病": "362a78d9fd3de8e7", "479轻净不想": "60e4eb3f132e4526", "479中误": "e554e03e36607d85", "479中病厚带": "4dba989c5c271d4c",
       "479中净不想": "653d469f8c7e0b4c", "479中误不想": "deb7b10118e14979", "480中净": "98060907cff16a35", "480中病": "464fb08161194503", "480轻病": "54aff2c814d79a9a", "480轻净不想": "9e0aff558747cfa8",
       "480中误": "726be2ca8af1ae10", "480中病厚带": "46831aff2c2536af", "480中净不想": "734a9fa11697b6ac", "480中误不想": "f6875ea9f6a74b27", "481中净": "355bddf91a8e1696", "481中病": "3995594cb9fed0c6",
       "481轻病": "5f85a67a39b79b85", "481轻净不想": "c54c37c718425969", "481中误": "b825305d2b0c2d87", "481中病厚带": "ea96e7696c296377", "481中净不想": "af034589587ff77d", "481中误不想": "caa2c578f7ea8a70",
       "482中净": "f738b5d4e0d7517f", "482中病": "c6bd3d481ac7bda8", "482轻病": "08244c97cef3fb5a", "482轻净不想": "253b32fdfdf3591a", "482中误": "89c8f7b8c750d9fd", "482中病厚带": "c47def0518f1e02e",
       "482中净不想": "705aed5b415d4f76", "482中误不想": "3bd0357cf975360d", "483中净": "6d07ed8657107bd5", "483中病": "d1399263c73ccd01", "483轻病": "cb3eb823a9e19b58", "483轻净不想": "03dd68e6acf34667",
       "483中误": "1908ed551c10623a", "483中病厚带": "8d34ccaef1ed5c9a", "483中净不想": "b811c6cbd64c7923", "483中误不想": "86931d41ec53e893", "484中净": "0556b867fd3e9549", "484中病": "7a30231cfba2de9a",
       "484轻病": "d78ec94c9f96cf30", "484轻净不想": "65e96404c662a58c", "484中误": "45d980a669612b53", "484中病厚带": "cd7d471bda762f2e", "484中净不想": "91ea35d944ba706a", "484中误不想": "2b7e511639416264"}


# ⑲之基（W919·X138·法用#拒後不再请）：W919 入主前之造章.js（git 9a8c81b34 之版·sha256 b341b92a…）所渲——键＝章（485—488）＋局（净、病、误、死乙、死四、选死、盲读死、盲读壳、逻辑审死、记死）；
#   指＝{收（诸席之令、席序、schema、effort）, 果, 抛} 之原序 sha256。N≤488 之令与控制之流⛔动（485—488 在写·续跑之缓存）；N≥489 之新支以 ⑲ 之判验其行
_基六 = {"485净": "87fbe609a031f072", "485死乙": "78453a07e5e11b03", "485死四": "ae5fffe94178a094", "485病": "1b59e779f33e3aaf", "485盲读壳": "efb010fcb29d48cb",
       "485盲读死": "efb010fcb29d48cb", "485记死": "c89a3bb829f22401", "485误": "bfff57d632c054e7", "485选死": "8b19fdef1e81c060", "485逻辑审死": "22dfc335f652a621",
       "486净": "efa0ef12728540b9", "486死乙": "3dc3c30626a28d70", "486死四": "9235281dd39e3f8b", "486病": "0bda5743e4283270", "486盲读壳": "99d4da3d3f8e3e18",
       "486盲读死": "99d4da3d3f8e3e18", "486记死": "3d903b377f827165", "486误": "5805dba9018d581f", "486选死": "d72d6d2f21783a3e", "486逻辑审死": "41d03518e00f824f",
       "487净": "e682c2fd362ce913", "487死乙": "f956ac179d7913a3", "487死四": "45f9c8706430837f", "487病": "282eac5f91436def", "487盲读壳": "b409e63375068ba0",
       "487盲读死": "b409e63375068ba0", "487记死": "96a7230eece348d0", "487误": "fd6c227cbeee456a", "487选死": "74772e77a4069d81", "487逻辑审死": "3fa5a13db88524c6",
       "488净": "e64086e72160addb", "488死乙": "ccf5fa63c5161009", "488死四": "0edae498c9c0f34c", "488病": "da81e8e5158f03c6", "488盲读壳": "f096051f70588212",
       "488盲读死": "f096051f70588212", "488记死": "114b022fd03383d3", "488误": "8f8b38e9a24fc2eb", "488选死": "0777f35426240edd", "488逻辑审死": "657bb12e86adf83c"}
_局19 = {'净': dict(病='净'), '病': dict(病='病'), '误': dict(病='误'), '死乙': dict(病='净', 死=['执笔·乙']),
        '死四': dict(病='净', 死=['执笔·甲', '执笔·乙', '执笔·丙', '执笔·己']), '选死': dict(病='病', 死=['选·']), '盲读死': dict(病='病', 死=['盲读']),
        '盲读壳': dict(病='病', 壳=['盲读']), '逻辑审死': dict(病='病', 死=['逻辑审·1']), '记死': dict(病='病', 死=['记席'])}
_门19 = 'const 拒後自 = 489, 拒後 = N >= 拒後自'


def _渲19(器, n, js=JS, **kw):
    r = 渲(器, n, '中', js=js, 抛=True, **kw)
    return r, 指({'收': r['收'], '果': r.get('果'), '抛': r.get('抛')})


def 拒後之判(器, d, js=JS):
    """⑲之二至五、之八至之十三（js 可换·回灌用）→ [(条, ok)]。"""
    出 = []
    import importlib
    承 = importlib.import_module('承')
    无门 = os.path.join(d, '造章_无拒後门.js')
    open(无门, 'w', encoding='utf-8').write(open(JS, encoding='utf-8').read().replace(_门19, 'const 拒後自 = 9999, 拒後 = N >= 拒後自'))
    # ⑲之二 489 首跑之席与改前（⛔门之行）逐字同、只删「·补」
    异 = []
    for k, kw in _局19.items():
        a, _ = _渲19(器, 489, js, **kw)
        b, _ = _渲19(器, 489, 无门, **kw)
        if a['收'] != [c for c in b['收'] if not c['label'].endswith('·补')]:
            异.append(k)
    出.append(('⑲之二 489 首跑十局之席（令、schema、effort、序）＝改前之行去「·补」%s' % ('｜⛔异：' + '、'.join(异) if 异 else ''), not 异))
    # ⑲之三 <3 即抛、补席之外⛔补、无 二稿 而二稿即抛、一稿即抛
    r4, _ = _渲19(器, 489, js, **_局19['死四'])
    标4 = [c['label'] for c in r4['收']]
    稿 = lambda 名: '版本/第489章/起草_%s.md' % 承.蒙号(489, 6, 名)
    二 = [{'file': 稿(名), 'beats': 5, 'words': 2800, 'soul': '魂'} for 名 in '丁戊']
    rq, _ = _渲19(器, 489, js, 加={'承': {'诸稿': 二, '补': True}, '补席': []})
    r1, _ = _渲19(器, 489, js, 加={'承': {'诸稿': 二[:1], '补': True}, '补席': [], '二稿': True})
    r2, _ = _渲19(器, 489, js, 加={'承': {'诸稿': 二, '补': True}, '补席': [], '二稿': True})
    标2 = [c['label'] for c in r2['收']]
    出.append(('⑲之三 死四 → 查四、⛔补、抛「交稿 2（<3·⛔进程内补）」点 承.py 489；补席［］无二稿之录 → 抛（点 --二稿）、⛔补；二稿之录在 → 二稿择一（log·⛔补）；一稿 → 抛',
              sum(1 for l in 标4 if l.endswith('·查')) == 4 and not any(l.endswith('·补') for l in 标4) and '交稿 2（<3·⛔进程内补）' in (r4.get('抛') or '')
              and '承.py 489' in (r4.get('抛') or '') and '--二稿' in (rq.get('抛') or '') and not any(c['label'].startswith('执笔') for c in rq['收'])
              and not r2.get('抛') and any('二稿择一' in x for x in r2['日']) and not any(l.startswith('执笔') for l in 标2) and '选·行家兼两眼' in 标2
              and '二稿之录在而 ≤1' in (r1.get('抛') or '')))
    # ⑲之四 补席之令逐字同原令；补席之外⛔补；诸执笔令与补令无「构思_前」「前席之构思」
    原, _ = _渲19(器, 489, js, 病='净')
    原甲 = next(c['prompt'] for c in 原['收'] if c['label'].startswith('执笔·甲·'))
    rb, _ = _渲19(器, 489, js, 加={'承': {'诸稿': 二, '补': True}, '补席': ['甲']})
    补 = [c for c in rb['收'] if c['label'].startswith('执笔')]
    出.append(('⑲之四 补席［甲］→ 唯「执笔·甲·补」一席、其令逐字同原令（schema、effort 同）；诸执笔令无「构思_前」「前席之构思」（承前永⛔）',
              [c['label'] for c in 补] == ['执笔·甲·补'] and 补[0]['prompt'] == 原甲
              and 补[0]['schema'] == next(c['schema'] for c in 原['收'] if c['label'].startswith('执笔·甲·'))
              and not any(('构思_前' in c['prompt'] or '前席之构思' in c['prompt']) for c in 原['收'] + rb['收'] if c['label'].startswith('执笔') and not c['label'].endswith('·查'))))
    # ⑲之五 六段 null 即抛（⛔「·补」）、盲读之壳即停
    五 = []
    for k, 段 in (('选死', '选：'), ('盲读死', '盲读：'), ('逻辑审死', '逻辑审·1：'), ('记死', '记：')):
        r, _ = _渲19(器, 489, js, **_局19[k])
        五.append(not any(c['label'].endswith('·补') for c in r['收']) and (r.get('抛') or '').startswith(段) and '⛔同令再请' in r['抛'])
    for 死, 段 in ((['合稿'], '合：'), (['逻辑审·2'], '逻辑审·2：')):
        r, _ = _渲19(器, 489, js, 病='病', 死=死)
        五.append(not any(c['label'].endswith('·补') for c in r['收']) and (r.get('抛') or '').startswith(段))
    r, _ = _渲19(器, 489, js, **_局19['盲读壳'])
    五.append((r.get('果') or {}).get('停') == '盲读未交' and (r.get('果') or {}).get('下') == '壳' and '盲读·补' not in [c['label'] for c in r['收']] and not r.get('抛'))
    出.append(('⑲之五 选／合稿／盲读／逻辑审·1／逻辑审·2／记席 null → 径抛、无「·补」；盲读之壳 → 停「盲读未交」（下：壳）、无「盲读·补」（%d/7）' % sum(五), all(五) and len(五) == 7))
    # ⑲之八 端到端：489 门内 Run1 真渲之收 → journal（甲 529 断、乙丙己 拒2→invalid_request、诸·查 交 {flaws:无稿}、丁戊交）→ 承 分因 → _承.js 之 args → 再渲
    import tempfile as _tf
    t = _tf.mkdtemp(prefix='承19_')
    try:
        r1_, _ = _渲19(器, 489, js, **_局19['死四'])
        rd = os.path.join(t, 'run1'); os.makedirs(rd)
        os.makedirs(os.path.join(t, '版本', '第489章'))
        u = lambda p: {'type': 'user', 'message': {'content': '[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. The computed task text follows:\n  ' + p.replace('\n', '\n  ')}}
        回 = lambda s, i='': {'type': 'assistant', 'message': {'id': 'm' + s + str(i), 'stop_reason': s, 'content': [], 'usage': {'input_tokens': 1, 'output_tokens': 1}}}
        错 = lambda st, 文: {'type': 'assistant', 'isApiErrorMessage': True, 'apiErrorStatus': st, 'message': {'content': [{'type': 'text', 'text': 文}]}}
        J = []
        for i, c in enumerate(r1_['收']):
            l, a = c['label'], 'z%02d' % i
            名 = l.split('·')[1] if l.startswith('执笔·') else ''
            if l.endswith('·查'):
                rows, 终 = [u(c['prompt']), 回('end_turn')], {'type': 'result', 'result': {'flaws': '无稿：稿档不在'}}
            elif 名 == '甲':
                rows, 终 = [u(c['prompt']), 回('tool_use'), 错(529, 'API Error: 529 overloaded_error')], {'type': 'failed'}
            elif 名 in '乙丙己':
                rows, 终 = [u(c['prompt']), 回('refusal', 1), 回('refusal', 2), 错('invalid_request', 'API Error: 400 invalid_request')], {'type': 'failed'}
            else:
                open(os.path.join(t, 稿(名)), 'w', encoding='utf-8').write('字' * 300 + '\n【本章亮点】')
                rows, 终 = [u(c['prompt']), 回('end_turn')], {'type': 'result', 'result': {'draft': {'file': 稿(名), 'beats': 5, 'words': 2800, 'soul': '魂'}, 'flaws': '无'}}
            open(os.path.join(rd, 'agent-%s.jsonl' % a), 'w', encoding='utf-8').write('\n'.join(json.dumps(x, ensure_ascii=False) for x in rows) + '\n')
            J += [{'type': 'started', 'key': 'k%d' % i, 'agentId': a, 'label': l}, dict(终, key='k%d' % i, agentId=a)]
        jp = os.path.join(rd, 'journal.jsonl')
        open(jp, 'w', encoding='utf-8').write('\n'.join(json.dumps(x, ensure_ascii=False) for x in J) + '\n')
        承0, 来 = 承.收(489, [jp], root=t, 界=0)
        a = 承.造(489, 承0, {'重': '中', '魂路': ['物证'], '带': '2,900—3,300'})
        a.pop('须厚', None)
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            rc = 承.拒後之分因(489, [], lambda k: None, 来, a, root=t)
        包 = 承.包裹(a)
        m = re.search(r"scriptPath: '[^']*' \}, (\{.*\})\)", 包, re.S)
        a2 = json.loads(m.group(1)) if m else {}
        r2_, _ = _渲19(器, 489, js, 加=a2)
        r0_, _ = _渲19(器, 489, js, 病='净', 加={k: v for k, v in a2.items() if k not in ('承', '补席', '二稿', '除席')})
        造2 = [c for c in r2_['收'] if c['label'].startswith('执笔')]
        原甲2 = next(c['prompt'] for c in r0_['收'] if c['label'].startswith('执笔·甲·'))
        出.append(('⑲之八 端到端（Run1 真渲：甲 529 断、乙丙己 拒2、诸·查 无稿、丁戊交）→ 承 分因（rc %s·补席 %s）→ _承.js 之 args 顶层 补席（⛔入 args.承）→ 再渲：只派「执笔·甲·补」、其令逐字同原令、选续'
                   % (rc, a2.get('补席')), rc == 0 and a2.get('补席') == ['甲'] and '补席' not in a2.get('承', {}) and '二稿' not in a2.get('承', {})
                   and [c['label'] for c in 造2] == ['执笔·甲·补'] and 造2[0]['prompt'] == 原甲2 and not r2_.get('抛')
                   and '选·行家兼两眼' in [c['label'] for c in r2_['收']] and '构思_前' not in json.dumps(a2, ensure_ascii=False)))
    finally:
        shutil.rmtree(t, ignore_errors=True)
    # ⑲之九 args.重造 带 除席：除席之执笔於首派、查、补俱⛔派、log 宽减
    r9, _ = _渲19(器, 489, js, 加={'重造': True, '除席': ['乙', '己']}, 死=['执笔·甲', '执笔·丙'])
    标9 = [c['label'] for c in r9['收']]
    出.append(('⑲之九 重造除席［乙、己］（死甲丙）→ 乙己於首派、查、补俱⛔派；log「重造除席」宽 6→4；甲丙照查、<3 即抛',
              not any(l.startswith(('执笔·乙', '执笔·己')) for l in 标9) and '执笔·甲·查' in 标9 and '执笔·丙·查' in 标9
              and any('重造除席：乙、己' in x and '6→4' in x for x in r9['日']) and '交稿 2' in (r9.get('抛') or '')))
    # ⑲之十〔W919 落地之查·病三〕盲读令(2) 一令二席：进程内 盲读·2 未交 → 盲读·2·好看 ⛔派；args.已拒（承.py 分因所书）→ 其席⛔派、照 null 之法续；488 照旧
    标 = lambda r: [c['label'] for c in r['收']]
    ra = 渲(器, 489, '中', '误', js=js, 抛=True, 不想=['盲读*'], 死=['盲读·2'])
    rb_ = 渲(器, 488, '中', '误', js=JS, 抛=True, 不想=['盲读*'], 死=['盲读·2'])
    rc_ = 渲(器, 489, '中', '误', js=js, 抛=True, 不想=['盲读*'], 加={'已拒': ['盲读·2']})
    rd_ = 渲(器, 489, '中', '净', js=js, 抛=True, 不想=['盲读*'], 加={'已拒': ['回写·好看']})
    re_ = 渲(器, 489, '中', '误', js=js, 抛=True, 加={'已拒': ['盲读·2·好看']})
    rf_ = 渲(器, 488, '中', '误', js=JS, 抛=True, 加={'已拒': ['盲读·2', '回写·好看']}, 不想=['盲读*'])
    rg_ = 渲(器, 488, '中', '误', js=JS, 抛=True, 不想=['盲读*'])
    出.append(('⑲之十 盲读令(2) 一令二席：489 盲读·2 null → 盲读·2·好看 ⛔派（好看.盲读2「⛔派·盲读·2 已未交」）；已拒［盲读·2］→ 盲读·2 与 盲读·2·好看 俱⛔派、逻辑审·2 照跑；'
               '已拒［回写·好看］→ ⛔派、好看之欠照书、记席照跑；已拒［盲读·2·好看］→ 盲读·2 亦⛔派；488 有 null 照派 盲读·2·好看、带已拒之参与无参逐字同',
               '盲读·2·好看' not in 标(ra) and (ra['果'].get('好看') or {}).get('盲读2') == '⛔派·盲读·2 已未交·X138' and '回写·好看' in 标(ra) and 标(ra)[-1] == '记席'
               and '盲读·2·好看' in 标(rb_)
               and '盲读·2' not in 标(rc_) and '盲读·2·好看' not in 标(rc_) and '逻辑审·2' in 标(rc_) and '回写·好看' in 标(rc_) and any('⛔盲读·2 ⛔派' in x for x in rc_['日'])
               and '回写·好看' not in 标(rd_) and (rd_['果'].get('好看') or {}).get('回写', '').startswith('⛔派（回写·好看') and (rd_['果'].get('好看') or {}).get('欠') == '不想之由·盲读' and 标(rd_)[-1] == '记席'
               and '盲读·2' not in 标(re_) and '逻辑审·2' in 标(re_) and not re_.get('抛')
               and rf_['收'] == rg_['收'] and '盲读·2' in 标(rf_) and '盲读·2·好看' in 标(rf_)))
    # ⑲之十一 端到端：Run1（盲读·2 拒2、记席 529 断）→ 承 分因 → _承.js 之 args 顶层 已拒［盲读·2］（⛔停·⛔入 args.承）→ 再渲：⛔派 盲读·2、逻辑审·2 与记席照跑
    t = _tf.mkdtemp(prefix='承19十_')
    try:
        rd = os.path.join(t, 'run1'); os.makedirs(rd)
        os.makedirs(os.path.join(t, '版本', '第489章'))
        u = lambda p: {'type': 'user', 'message': {'content': '[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. The computed task text follows:\n  ' + p}}
        回 = lambda s, i='': {'type': 'assistant', 'message': {'id': 'm' + s + str(i), 'stop_reason': s, 'content': [], 'usage': {'input_tokens': 1, 'output_tokens': 1}}}
        错 = lambda st, 文: {'type': 'assistant', 'isApiErrorMessage': True, 'apiErrorStatus': st, 'message': {'content': [{'type': 'text', 'text': 文}]}}
        果们 = [('执笔·%s·路' % 名, {'draft': {'file': os.path.join(t, 稿(名)), 'beats': 5, 'words': 2800, 'soul': '魂'}, 'flaws': '无'}) for 名 in '甲乙丙']
        for 名 in '甲乙丙':
            open(os.path.join(t, 稿(名)), 'w', encoding='utf-8').write('字' * 300 + '\n【本章亮点】')
        果们 += [('选·行家兼两眼', {'pick': {'ranking': ['稿一'], 'why': '由', 'fatal': [], 'leap': [], 'common_fatal': '', 'beat_scores': '拍'}}),
               ('合稿', {'merge': {'file': '正文/x.md', 'beats': 5, 'words': 2800, 'base': '稿一', 'gates': '器', 'gates_green': True, 'ledger': '账', 'recap': '前情'}}),
               ('盲读', {'blind': {'understood': True, 'confused': '', 'misread': '错', 'want_next': True, 'why_next': '想', 'happened': '事', 'remember': '记', 'prior': '无'}}),
               ('逻辑审·1', {'audit': {'hard': [], 'soft': '软', 'gate': '闸', 'misread': True, 'misread_where': '处', 'misread_fix': '治'}}),
               ('回写', {'rewrite': {'done': True, 'note': '治'}}), ('盲读·2', None), ('逻辑审·2', {'audit': {'hard': [], 'soft': '软2', 'gate': '闸2', 'misread': False}}), ('记席', 'x')]
        J = []
        for i, (l, r) in enumerate(果们):
            a = 'y%02d' % i
            if l == '盲读·2':
                rows, 终 = [u('盲读之令'), 回('refusal', 1), 回('refusal', 2), 错('invalid_request', 'API Error: 400 invalid_request')], {'type': 'failed'}
            elif l == '记席':
                rows, 终 = [u('记席之令'), 回('tool_use'), 错(529, 'API Error: 529 overloaded_error')], {'type': 'failed'}
            else:
                rows, 终 = [u('你是第 489 章的**' + l), 回('end_turn')], {'type': 'result', 'result': r}
            open(os.path.join(rd, 'agent-%s.jsonl' % a), 'w', encoding='utf-8').write('\n'.join(json.dumps(x, ensure_ascii=False) for x in rows) + '\n')
            J += [{'type': 'started', 'key': 'k%d' % i, 'agentId': a, 'label': l}, dict(终, key='k%d' % i, agentId=a)]
        jp = os.path.join(rd, 'journal.jsonl')
        open(jp, 'w', encoding='utf-8').write('\n'.join(json.dumps(x, ensure_ascii=False) for x in J) + '\n')
        承0, 来 = 承.收(489, [jp], root=t, 界=0)
        a = 承.造(489, 承0, {'重': '中', '魂路': ['物证'], '带': '2,900—3,300'})
        a.pop('须厚', None)
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            rc = 承.拒後之分因(489, [], lambda k: None, 来, a, root=t)
        m = re.search(r"scriptPath: '[^']*' \}, (\{.*\})\)", 承.包裹(a), re.S)
        a2 = json.loads(m.group(1)) if m else {}
        r11 = 渲(器, 489, '中', '净', js=js, 抛=True, 加=a2)
        出.append(('⑲之十一 端到端（Run1：盲读·2 拒2、记席 529 断）→ 承 分因（rc %s·已拒 %s）→ _承.js 之 args 顶层 已拒（⛔入 args.承）→ 再渲：⛔派 盲读·2、逻辑审·2 与记席照跑' % (rc, a2.get('已拒')),
                   rc == 0 and a2.get('已拒') == ['盲读·2'] and '已拒' not in a2.get('承', {}) and '盲读·2' not in 标(r11) and '逻辑审·2' in 标(r11)
                   and 标(r11)[-1] == '记席' and not r11.get('抛') and not any(l.startswith(('执笔', '选', '合稿')) for l in 标(r11))))
    finally:
        shutil.rmtree(t, ignore_errors=True)
    # ⑲之十二〔W924·501〕一稿之路（门 1·只用平台已交之稿）：无一稿之参而一稿 → 抛、⛔补；args.一稿 而一稿 → 过造之门、⛔派执笔、选至记席照跑；
    #   一稿而 0 稿 → 抛；args.承 无诸稿之列 → 抛（⛔首派）；补席在 → ⛔补（log 其⛔派）；一稿、二稿俱在 → 门 1；二稿而一稿 → 照抛（⑲之三）
    一 = 二[:1]
    执 = lambda r: [l for l in 标(r) if l.startswith('执笔')]
    rq1, _ = _渲19(器, 489, js, 加={'承': {'诸稿': 一, '补': True}, '补席': []})
    ry, _ = _渲19(器, 489, js, 加={'承': {'诸稿': 一, '补': True}, '补席': [], '一稿': True})
    r0y, _ = _渲19(器, 489, js, 加={'承': {'诸稿': [], '补': True}, '补席': [], '一稿': True})
    rny, _ = _渲19(器, 489, js, 加={'一稿': True})
    rby, _ = _渲19(器, 489, js, 加={'承': {'诸稿': 一, '补': True}, '补席': ['甲'], '一稿': True})
    r12, _ = _渲19(器, 489, js, 加={'承': {'诸稿': 一, '补': True}, '补席': [], '一稿': True, '二稿': True})
    rcy, _ = _渲19(器, 489, js, 加={'承': {'诸稿': 一, '补': True}, '一稿': True})          # 未分因（args 无补席）而一稿：查席亦⛔派
    出.append(('⑲之十二 一稿之路：无 args.一稿 而整稿一 → 抛「交稿 1」、⛔补；args.一稿 而整稿一 → 过造之门（log「一稿径用」）、⛔派执笔、选·合·盲读·审·记席照跑；'
               '一稿而 0 稿 → 抛「一稿之录在而 0」；args.承 无诸稿之列 → 抛、⛔派一席；补席［甲］→ ⛔补（log「补席［甲］⛔派」）；一稿、二稿俱在 → 门 1；args 无补席 → 查席亦⛔派',
               (rq1.get('抛') or '').startswith('造：交稿 1') and not 执(rq1)
               and not ry.get('抛') and not 执(ry) and any('一稿径用' in x for x in ry['日']) and '选·行家兼两眼' in 标(ry) and '合稿' in 标(ry)
               and '盲读' in 标(ry) and '逻辑审·1' in 标(ry) and 标(ry)[-1] == '记席' and len((ry.get('果') or {}).get('蒙名') or []) == 1
               and '一稿之录在而 0' in (r0y.get('抛') or '') and not 执(r0y)
               and '无诸稿之列' in (rny.get('抛') or '') and rny['收'] == []
               and not rby.get('抛') and not 执(rby) and any('补席［甲］⛔派' in x for x in rby['日'])
               and not r12.get('抛') and not 执(r12) and 标(r12)[-1] == '记席' and not rcy.get('抛') and not 执(rcy) and 标(rcy)[-1] == '记席'))
    # ⑲之十三 端到端（501 之形）：Run1 真渲（甲乙丙丁己 拒2、诸·查 无稿、戊交一整稿）→ 承 分因 rc 3（点 --一稿）→ --一稿 "由" → _承.js 之 args 顶层 一稿:true（⛔入 args.承）→ 再渲：⛔派执笔、选至记席照跑
    t = _tf.mkdtemp(prefix='承19一_')
    try:
        r1y, _ = _渲19(器, 489, js, 病='净', 死=['执笔·甲', '执笔·乙', '执笔·丙', '执笔·丁', '执笔·己'])
        rd = os.path.join(t, 'run1'); os.makedirs(rd)
        os.makedirs(os.path.join(t, '版本', '第489章'))
        u = lambda p: {'type': 'user', 'message': {'content': '[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. The computed task text follows:\n  ' + p.replace('\n', '\n  ')}}
        回 = lambda s, i='': {'type': 'assistant', 'message': {'id': 'm' + s + str(i), 'stop_reason': s, 'content': [], 'usage': {'input_tokens': 1, 'output_tokens': 1}}}
        错 = lambda st, 文: {'type': 'assistant', 'isApiErrorMessage': True, 'apiErrorStatus': st, 'message': {'content': [{'type': 'text', 'text': 文}]}}
        J = []
        for i, c in enumerate(r1y['收']):
            l, a = c['label'], 'w%02d' % i
            名 = l.split('·')[1] if l.startswith('执笔·') else ''
            if l.endswith('·查'):
                rows, 终 = [u(c['prompt']), 回('end_turn')], {'type': 'result', 'result': {'flaws': '无稿：稿档不在'}}
            elif 名 and 名 != '戊':
                rows, 终 = [u(c['prompt']), 回('refusal', 1), 回('refusal', 2), 错('invalid_request', 'API Error: 400 invalid_request')], {'type': 'failed'}
            else:
                open(os.path.join(t, 稿(名)), 'w', encoding='utf-8').write('字' * 300 + '\n【本章亮点】')
                rows, 终 = [u(c['prompt']), 回('end_turn')], {'type': 'result', 'result': {'draft': {'file': 稿(名), 'beats': 5, 'words': 2032, 'soul': '魂'}, 'flaws': '无'}}
            open(os.path.join(rd, 'agent-%s.jsonl' % a), 'w', encoding='utf-8').write('\n'.join(json.dumps(x, ensure_ascii=False) for x in rows) + '\n')
            J += [{'type': 'started', 'key': 'k%d' % i, 'agentId': a, 'label': l}, dict(终, key='k%d' % i, agentId=a)]
        jp = os.path.join(rd, 'journal.jsonl')
        open(jp, 'w', encoding='utf-8').write('\n'.join(json.dumps(x, ensure_ascii=False) for x in J) + '\n')
        承0, 来 = 承.收(489, [jp], root=t, 界=0)
        import io, contextlib
        def 分(cli):
            a = 承.造(489, 承0, {'重': '中', '魂路': ['物证'], '带': '2,900—3,300'})
            a.pop('须厚', None)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = 承.拒後之分因(489, cli, lambda k: cli[cli.index(k) + 1] if k in cli else None, 来, a, root=t)
            m = re.search(r"scriptPath: '[^']*' \}, (\{.*\})\)", 承.包裹(a), re.S)
            return rc, (json.loads(m.group(1)) if m else {}), buf.getvalue()
        rcA, _, oA = 分([])
        rcB, aB, _ = 分(['--一稿', '五席俱拒、整稿一'])
        r13, _ = _渲19(器, 489, js, 加=aB)
        出.append(('⑲之十三 端到端（501 之形：甲乙丙丁己 拒2、诸·查 无稿、戊交一整稿）→ 承 分因 rc %s（点 --一稿）→ --一稿 "由" rc %s → _承.js 之 args 顶层 一稿:true（⛔入 args.承）→ 再渲：⛔派执笔、选至记席照跑' % (rcA, rcB),
                   rcA == 3 and '--一稿' in oA and rcB == 0 and aB.get('一稿') is True and '一稿' not in aB.get('承', {}) and aB.get('补席') == []
                   and len(aB.get('承', {}).get('诸稿') or []) == 1 and 承.一稿之录(489, t) and 承.整稿之界(489, t) == 1
                   and not r13.get('抛') and not 执(r13) and '选·行家兼两眼' in 标(r13) and 标(r13)[-1] == '记席'))
    finally:
        shutil.rmtree(t, ignore_errors=True)
    return 出


def 渲(器, n, 重='中', 病='病', js=JS, 厚='否', 空='', 果=False, 加=None, 拒=None, 死=None, 空稿=None, 不想=None, 写否=False, 日=False, 抛=False, 壳=None):
    环 = dict(os.environ, **({'ZJ_空稿': json.dumps(空稿, ensure_ascii=False)} if 空稿 else {}), **({'ZJ_ARGS': json.dumps(加, ensure_ascii=False)} if 加 else {}), **({'ZJ_拒': json.dumps(拒, ensure_ascii=False)} if 拒 else {}),
              **({'ZJ_死': json.dumps(死, ensure_ascii=False)} if 死 else {}), **({'ZJ_不想': json.dumps(不想, ensure_ascii=False)} if 不想 else {}),
              **({'ZJ_写否': '1'} if 写否 else {}), **({'ZJ_抛': '1'} if 抛 else {}), **({'ZJ_壳': json.dumps(壳, ensure_ascii=False)} if 壳 else {}))
    for k in ('ZJ_空稿', 'ZJ_ARGS', 'ZJ_拒', 'ZJ_死', 'ZJ_不想', 'ZJ_写否', 'ZJ_抛', 'ZJ_壳'):   # 外之环境⛔漏入（基之局只由参定）
        if not {'ZJ_空稿': 空稿, 'ZJ_ARGS': 加, 'ZJ_拒': 拒, 'ZJ_死': 死, 'ZJ_不想': 不想, 'ZJ_写否': 写否, 'ZJ_抛': 抛, 'ZJ_壳': 壳}[k]:
            环.pop(k, None)
    o = subprocess.run(['node', 器, js, str(n), 重, 病, 厚, 空], capture_output=True, text=True, cwd=ROOT, timeout=60, env=环)
    if o.returncode:
        raise RuntimeError('造章.js 渲染不起（%d %s %s）：%s' % (n, 重, 病, o.stderr.strip()[:300]))
    d = json.loads(o.stdout)
    if 抛:
        return d                                  # ★W919 ⑲：{收, 果, 日, 抛?}
    return (d['收'], d['果'], d['日']) if 日 else (d['收'], d['果']) if 果 else d['收']


def 指(收):
    """原序 JSON 之 sha256（⛔sort_keys：schema 之键换序，请求之字节即变、缓存即破——须验得出）。"""
    return hashlib.sha256(json.dumps(收, ensure_ascii=False).encode()).hexdigest()[:16]


def _令(收, 首):
    return [c for c in 收 if c['label'].startswith(首)]


def 新条(收, n):
    """→ [(条, 合否)]：N≥398 之诸条（X26／X14／X13）。拿 397 之令来判须一一不合（回灌）。"""
    笔 = _令(收, '执笔·甲')
    笔 = 笔[0]['prompt'] if 笔 else ''
    盲 = _令(收, '盲读')
    审 = _令(收, '逻辑审·1')
    记 = _令(收, '记席')
    记 = 记[0]['prompt'] if 记 else ''
    假前提 = ('读料那一条命令', '&& cat > 版本/第%d章/起草_甲_构思.md' % n)   # 上回之令：读料之 Bash 末接 cat > 构思（席读料俱用 Read）
    return [
        ('X26·首条消息 Read 料与 Bash 建构思档同发（⛔以 Bash cat 读料；上回之假前提⛔见）',
         '首回即落】' in 笔 and '**第一条消息**同发两个调用' in 笔 and ('① Read「版本/第%d章/_料.md」（allow_large' % n) in 笔
         and ("② 一条 Bash「cat > 版本/第%d章/起草_甲_构思.md <<'EOF'」建档" % n) in 笔 and '⛔以 Bash cat 读料' in 笔
         and not any(x in 笔 for x in 假前提)),
        ('X26·想定一样即以 cat >> 追记、每定一拍即追记；费审量首落与最长隔',
         '想定一样即以 cat >> 追记一样' in 笔 and '每定一拍即追记一行' in 笔 and '构思首落−席起' in 笔 and '构思诸写之最长隔' in 笔),
        ('X26·全章之排在档上排（满分之问先落、拍表随第一拍落）；⛔「思考里只想眼下这一拍」之牵',
         '全章之排在档上排' in 笔 and '「## 满分之问」（三种写法与其比）先落' in 笔 and '随第一拍同落' in 笔
         and '思考里只想眼下这一拍' not in 笔),
        ('X26·回数之限 28（逐样追记有其回）', '至多 28 回工具' in 笔),
        ('X26·旧「构思可先落一回」⛔再见（彻删於新令）', bool(笔) and '构思可先落一回' not in 笔),
        ('X14·盲读 schema 带 prior 且必交', bool(盲) and all('prior' in (c['schema'] or {}).get('required', []) for c in 盲)),
        ('X14·盲读①只算本章之卡、①之二前情之指⛔计入读不懂',
         bool(盲) and all('只算本章之卡' in c['prompt'] and '①之二 prior' in c['prompt'] and '⛔写进 confused' in c['prompt'] and '六答' in c['prompt'] for c in 盲)),
        ('X14·逻辑审把前情之指并入回述实证', bool(审) and '前情之指「' in 审[0]['prompt'] and '并入下「回述实证」逐条核' in 审[0]['prompt']),
        ('X14·记席录前情之指', '前情之指：' in 记 and '盲读六答' in 记),
        ('X13·记席立卡後跑开镜庭十四格', ('第零轮开镜庭.py --静 %d' % (n + 1)) in 记 and '十四·卡之自牵' in 记),
    ]


硬项须厚 = '【硬项·须厚】本章须厚（分量闸·须厚）：本章之事须担得起 2,900 净重——⛔凑字、⛔撒感官；担不起即换一件更大的事，写进构思之满分之问'
选须厚 = '须厚之章，净重 <2,900 之稿作底须写其由'


def 带须厚(收):
    """→ (诸执笔令俱带其硬项, 有执笔令带其硬项, 选令带其底)。"""
    笔 = [c['prompt'] for c in _令(收, '执笔')]
    选 = [c['prompt'] for c in _令(收, '选')]
    return (bool(笔) and all(硬项须厚 in p for p in 笔), any(硬项须厚 in p for p in 笔),
            bool(选) and all(选须厚 in p for p in 选))


def 须厚之条(器):
    """★1020 X40：→ [(条, 合否)]。⛔动 N≤400——400 传 须厚 与不传者原序之指须同（args.须厚 於 N≤400 一字不认）。"""
    出 = []
    for 重 in ('中', '轻', '重'):
        a = 带须厚(渲(器, 401, 重, '净', 厚='厚'))
        出.append(('401（须厚:true·%s）之诸执笔令俱带「本章须厚」之硬项、选令带「须厚之章之底」' % 重, a[0] and a[2]))
    b = 带须厚(渲(器, 401, '中', '净'))
    出.append(('401 不传 须厚 者⛔带（执笔令、选令俱无）', not b[1] and not b[2]))
    c400 = 渲(器, 400, '中', '病', 厚='厚')
    d = 带须厚(c400)
    出.append(('400（传 须厚:true）之执笔令、选令⛔带——N≤400 之令⛔动', not d[1] and not d[2]))
    出.append(('400 传 须厚 与不传者原序之指同（轻中重×净病俱同）',
              all(指(渲(器, 400, 重, 病, 厚='厚')) == 指(渲(器, 400, 重, 病)) for 重 in ('轻', '中', '重') for 病 in ('净', '病'))))
    # 回灌：把 401 之硬项抹去（假其被删），本条须红
    抹 = [dict(c, prompt=c['prompt'].replace(硬项须厚, '')) for c in 渲(器, 401, '中', '净', 厚='厚')]
    出.append(('回灌·抹去 401 之「本章须厚」硬项 → 本条红', not 带须厚(抹)[0]))
    return 出


def _键之句(k):
    return '【交之键】诸席共一交卷之式：StructuredOutput 只填「%s」一键' % k


通之键 = [('执笔', 'draft'), ('选', 'pick'), ('合稿', 'merge'), ('盲读', 'blind'), ('逻辑审', 'audit'), ('回写', 'rewrite'), ('记席', 'record')]


def 通之条(器):
    """★1024 省 token 之审：→ [(条, 合否)]。N≥411 之通式、补派、严判、记令四刀、窄审；拿 410 之令回灌须红。"""
    出 = []
    收, 果 = 渲(器, 411, 果=True)
    收410 = 渲(器, 410)
    式们 = [c['schema'] for c in 收]
    ASCII = lambda o: all(re.fullmatch(r'[A-Za-z0-9_.-]{1,64}', k) for k in (o.get('properties') or {}))
    通 = 式们[0] or {}
    旧式 = {k: next((c['schema'] for c in 收410 if c['label'].startswith(首) and c['schema']), None) for 首, k in 通之键 if k != 'rewrite'}
    出.append(('通式：411 诸席（%d·连回写）传同一 schema（原序之指同）、键俱 ASCII（坑⑩）、顶层 minProperties:1、带 flaws' % len(收),
              all(式们) and len({指(x) for x in 式们}) == 1 and ASCII(通) and all(ASCII(v) for v in 通.get('properties', {}).values() if isinstance(v, dict))
              and 通.get('minProperties') == 1 and list(通.get('properties', {})) == ['draft', 'pick', 'merge', 'blind', 'audit', 'rewrite', 'record', 'flaws']))
    出.append(('通式：各子式之 required 与 properties 同 410 之旧式（记式另验）；回写之子式 required done',
              all(通['properties'][k].get('required') == (旧式[k] or {}).get('required') and 通['properties'][k].get('properties') == {
                  kk: vv for kk, vv in (旧式[k] or {}).get('properties', {}).items() if kk != 'flaws'} for k in ('draft', 'pick', 'merge', 'blind', 'audit'))
              and 通['properties']['rewrite'].get('required') == ['done']))
    出.append(('令末一句「只填『X』一键」，X 与席相应（%d 席）' % len(收),
              all(_键之句(next(k for 首, k in 通之键 if c['label'].startswith(首))) in c['prompt'].rsplit('\n\n', 1)[-1] for c in 收)))
    出.append(('回灌·410 之令⛔带交之键、诸席之 schema 各异（旧式·N≤410 ⛔动）',
              not any('【交之键】' in c['prompt'] for c in 收410) and len({指(c['schema']) for c in 收410 if c['schema']}) > 1))
    写411 = next(c['prompt'] for c in 收 if c['label'] == '回写')
    写410 = next(c['prompt'] for c in 收410 if c['label'] == '回写')
    五大 = re.match(r'【六大主义[^\n]*\n(?:\d\.[^\n]*\n){6}', 写411)      # 1027 #33：N≥411 之共令首段（五大主义五行）；410 ⛔带
    # 1027 X58（章料拆二档·合流）：N≥411 之料律点名 _料_前文.md——料律一段除外，余仍一字不动；410 ⛔带彼档之名
    去料律 = lambda t: re.sub(r'【只读章料·⛔自己搜料】.*?费占一半）。', '【料律】', t, flags=re.S)
    出.append(('回写之令实一字不动：411 去首段之五大主义、去交之一句、料律（X58 点名 _料_前文.md）除外＝410 之令换号（410 ⛔带五大主义、⛔带 _料_前文）', bool(五大)
              and 去料律(写411[五大.end():].rsplit('\n\n【交之键】', 1)[0]) == 去料律(写410.replace('410', '411')) and '【六大主义' not in 写410
              and '_料_前文.md' in 写411 and '_料_前文.md' not in 写410))
    # 交空对象即补派
    def 标(空, 病='病'):
        c, r = 渲(器, 411, '中', 病, 空=空, 果=True)
        return [x['label'] for x in c], r
    for 空, 补 in (('选·行家兼两眼', '选·补'), ('合稿', '合稿·补'), ('盲读', '盲读·补'), ('逻辑审·1', '逻辑审·1·补'), ('记席', '记席·补')):
        L, _ = 标(空)
        出.append(('交空对象即补派：%s 交 {flaws} → 派 %s' % (空, 补), 补 in L))
    L, _ = 标('执笔·甲*')
    出.append(('交空对象即补派：执笔·甲交空 → 先派「执笔·甲·查」、查无稿再「执笔·甲·补」（⛔径派整席）', '执笔·甲·查' in L and '执笔·甲·补' in L and L.index('执笔·甲·查') < L.index('执笔·甲·补')))
    L, _ = 标('执笔·甲*,查收')
    查令 = next((c for c in 渲(器, 411, 空='执笔·甲*,查收') if c['label'] == '执笔·甲·查'), {'prompt': '', 'effort': None})
    出.append(('查席收盘稿 → ⛔补；查令只跑 承.py 411 --查 甲 <蒙档>、effort low、首句认章', '执笔·甲·查' in L and '执笔·甲·补' not in L
              and bool(re.search(re.escape('python3 工具/承.py 411 --查 甲 ') + r'\S+/第411章/起草_稿[一二三四五]\.md', 查令['prompt'])) and 查令['effort'] == 'low'   # re.escape：死处方哨认「承\.py」为器名而红
              and 查令['prompt'].startswith('你是第 411 章的**')))
    L, r = 标('逻辑审·1,逻辑审·1·补')
    出.append(('逻辑审·1 二回交空 → 停「逻辑审未交」（旧以 null 作无病照放）', r.get('停') == '逻辑审未交' and '记席' not in L))
    L, r = 标('逻辑审·2,逻辑审·2·补')
    出.append(('逻辑审·2 二回交空 → 停（⛔无复审而记）', r.get('停') == '致命未净' and '逻辑审·2·补' in L and '记席' not in L))
    L, _ = 标('', '串')
    L410 = [c['label'] for c in 渲(器, 410, '中', '串')]
    出.append(('布尔严判：misread 交「否」→ 411 ⛔作读误（无回写）；410 照旧真值判（有回写·旧行⛔动）', '回写' not in L and '回写' in L410))
    # 记令四刀
    记 = next(c for c in 收 if c['label'] == '记席')
    记410 = next(c['prompt'] for c in 收410 if c['label'] == '记席')
    出.append(('记令四刀：式 {done,left}、式取记料【一】⛔另读前章回执、治毕复跑 --前 --红、交 left 含 §十四',
              通['properties']['record'] == {'type': 'object', 'properties': {'done': {'type': 'boolean'}, 'left': {'type': 'string'}}, 'required': ['done', 'left']}
              and '式取记料【一】，⛔另读前章回执' in 记['prompt'] and '式照前章回执（封版.py --前 印其路，读之）' not in 记['prompt']
              and 'python3 工具/封版.py 411 --前 --红' in 记['prompt'] and 'left（未了之事＋回执 §十四 交总编辑诸条' in 记['prompt'] and '交：receipt' not in 记['prompt']))
    出.append(('回灌·410 记令照旧（读前章回执、交 receipt）', '式照前章回执（封版.py --前 印其路，读之）' in 记410 and '交：receipt' in 记410 and '--前 --红' not in 记410))
    # 窄审
    c误, r误 = 渲(器, 411, '中', '误', 果=True)
    审1 = next(c['prompt'] for c in 收 if c['label'] == '逻辑审·1')
    审2误 = next(c['prompt'] for c in c误 if c['label'] == '逻辑审·2')
    审2病 = next(c['prompt'] for c in 收 if c['label'] == '逻辑审·2')
    出.append(('窄审：第1回只读误 → 逻辑审·2 带窄审之门（首跑 稿差.py 411、判全照全审、名词 grep 401—410、节名不变）；第1回之令记「据 正文＝vNN」',
              '【窄审之门' in 审2误 and '首条命令「python3 工具/稿差.py 411」' in 审2误 and '至少第 401 至 410 章' in 审2误 and '盲读·2 未复读' in 审2误
              and '「## 造式·逻辑审·合後·第2回」' in 审2误 and 'python3 工具/稿差.py 411 --据' in 审1 and '稿差' not in 审2误.split('【窄审之门')[0]))
    出.append(('窄审：第1回有硬崩 → 逻辑审·2 照旧全审（⛔窄门）；soft 并入第1回（窄者）', '窄审之门' not in 审2病
              and '〔第1回〕软1' in (r误.get('逻辑审') or {}).get('soft', '') and '〔第1回〕' not in (果.get('逻辑审') or {}).get('soft', '')))
    出.append(('回灌·410 之逻辑审令⛔带窄门、⛔带据句', not any('窄审之门' in c['prompt'] or '稿差' in c['prompt'] for c in 收410)))
    # 承能拆键：承.py 之必填表＝通式之 required；拆之得子
    import 承 as _承
    出.append(('承能拆键：承.通之必＝通式诸子式之 required；{键: 子, flaws} → 子、缺必填 → 未交',
              all(_承.通之必[k] == 通['properties'][k].get('required') for k in 通['properties'] if k != 'flaws')
              and _承.拆({'pick': {k: 1 for k in _承.通之必['pick']}, 'flaws': '无'}, '选') == {k: 1 for k in _承.通之必['pick']}
              and _承.拆({'pick': {'ranking': []}}, '选') is None and _承.拆({'flaws': '无'}, '草') is None))
    # 合流：C 组之硬项之处、B 组之记落入令——只 N≥411
    量们 = [c['prompt'] for c in 收 if '【量·⛔心算】' in c['prompt']]
    出.append(('硬项之处入执笔令：411 诸执笔之【量】俱带「硬项只照 --量 所印之处」；410 ⛔带',
              bool(量们) and all('硬项只照 --量 所印之处（白文／骨记 L行＋原句' in t for t in 量们)
              and not any('硬项只照' in c['prompt'] for c in 收410)))
    记落之句 = ['python3 工具/记落.py 411 --试', '10. **末步·记落**', '跑「python3 工具/记落.py 411」', '‹器:回执之数›', '‹器:日号›', '‹器:终稿›',
             '‹器:大审#号›', 'OPEN_BRIEF_CARD_SCHEMA[412]', '你只立②（第 412 章', '「主环之职（记席⛔治）」一栏', '交：done（1—10 俱毕否）']
    出.append(('记落入记令：411 带末步·记落、‹器:键› 诸占位、②之锚独立、主环之职栏⛔治；410 ⛔带记落、⛔带占位',
              all(k in 记['prompt'] for k in 记落之句) and '记落' not in 记410 and '‹器:' not in 记410))
    # 1027 汰：冷眼轮（记令之冷轮补执、回执之「N章冷眼轮」之签）、⑭（「除⑭」之标）、对位（造式验之器列）——只 N≥411；410 之令照旧
    合411 = next(c['prompt'] for c in 收 if c['label'] == '合稿')
    合410 = next(c['prompt'] for c in 收410 if c['label'] == '合稿')
    汰之句 = ['冷轮补执', '章冷眼轮」六字', '开轮十六检（除⑭）', '、对位、']
    出.append(('1027 汰：411 之记令⛔冷轮补执、⛔「N章冷眼轮」之签、⛔「除⑭」并令略前章回执之冷眼轮二节；合令之造式验器列⛔对位；410 照旧俱在',
              not any(k in 记['prompt'] or k in 合411 for k in 汰之句) and '⛔立冷眼轮之节' in 记['prompt']
              and all(k in 记410 + 合410 for k in 汰之句)))
    return 出


def X62之判(收, n):
    """★1027 X62（X58 之余·1024_W71 410 选席七回、审席十回）：→ [(条, 合否)]。选之先跑一条命令并印诸稿之净重（净重对表 --量）与
    诸稿亮点所引之原场（章料 --稿引·诸稿俱列）、回之限 5（<410 之 7）、致命之据⛔awk；合核胜稿之原场同器；逻辑审先跑并展正文之引、限 8（<410 之 10）。"""
    选 = next((c['prompt'] for c in 收 if c['label'].startswith('选')), '')
    合 = next((c['prompt'] for c in 收 if c['label'] == '合稿'), '')
    审 = [c['prompt'] for c in 收 if c['label'].startswith('逻辑审')]
    m = re.search(re.escape('python3 工具/章料.py --稿引') + r' ([^\n]+)', 选)
    稿 = re.findall(r'版本/第%d章/起草_稿[一二三四五六七]\.md' % n, 选.split('【先跑')[0])
    return [
        ('选之先跑一条命令：诸稿之净重（净重对表 --量）与诸稿亮点之原场（章料 --稿引·诸稿俱列）同印',
         bool(m) and bool(稿) and m.group(1).split() == 稿 and 'python3 工具/净重对表.py --量 "$f"; done; python3 工具/章料.py --稿引' in 选),
        ('选：回之限 5（<410 之 7）、首回并发；致命之据照先跑之印⛔awk 补查',
         '你这一席至多 5 回工具' in 选 and '【回之排·⛔来回翻】首回一条消息并发' in 选 and '（章:行，awk 亲印）' not in 选 and '⛔awk、sed、grep 补查' in 选),
        ('合：胜稿之原场一条命令即展（章料 --稿引 胜稿）、⛔先 awk', ('python3 工具/章料.py --稿引 版本/第%d章/起草_稿' % n) in 合 and '先 awk 亲印两处原句' not in 合),
        ('逻辑审（%d 回）：先跑并展正文亮点之引、限 8（<410 之 10）' % len(审), bool(审) and all(
            ('python3 工具/崩坏闸.py %d; python3 工具/章料.py --稿引 正文/镇冢秘术_第' % n) in p and '你这一席至多 8 回工具' in p and '（前文之据 awk 亲印）' not in p for p in 审)),
    ]


def X62之条(器):
    """411 俱过；410 之令（N≤410 ⛔动）照判俱红（回灌）；选令所载之 --稿引 命令真跑於 410 之诸稿，印得出原场。"""
    收 = 渲(器, 411)
    出 = [(条, ok) for 条, ok in X62之判(收, 411)]
    出.append(('回灌·410 之令（旧病）照 X62 之判俱红', not any(ok for _, ok in X62之判(渲(器, 410), 410))))
    选 = next(c['prompt'] for c in 收 if c['label'].startswith('选'))
    m = re.search(re.escape('python3 工具/章料.py --稿引') + r' ([^\n]+)', 选)
    稿 = m.group(1).replace('第411章', '第410章').split() if m else []
    if not 稿:
        return 出 + [('真跑·选令之 --稿引：选令无其命令', False)]
    r = subprocess.run([sys.executable, os.path.join(ROOT, '工具', '章料.py'), '--稿引'] + 稿, cwd=ROOT, capture_output=True, text=True)
    展 = [l for l in r.stdout.split('\n') if re.match(r'- \d{1,3}[:：]\d', l)]
    出.append(('真跑·选令之 --稿引 於 410 之 %d 稿：rc 0、诸稿俱列、原场展 %d 处' % (len(稿), len(展)),
              r.returncode == 0 and all(('- ' + os.path.basename(f) + '：') in r.stdout for f in 稿) and '〔原场' in r.stdout and len(展) >= 10))
    return 出


def _换笔(收, f):
    return [dict(c, prompt=f(c['prompt'])) if c['label'].startswith('执笔·甲') else c for c in 收]


def 死规之判(收, 带=None, 须厚=False):
    """〔1119 死规之审〕→ [(条, 合否, 守牙否)]。新条：N≥473 逐章配额之牙已拔（472 之令照判须红）；守牙：方法与护质之牙仍在（472、473 俱须绿）。"""
    笔 = [c['prompt'] for c in 收 if c['label'].startswith('执笔·') and not c['label'].endswith(('·查', '·补'))]
    选 = next((c['prompt'] for c in 收 if c['label'].startswith('选')), '')
    合 = next((c['prompt'] for c in 收 if c['label'] == '合稿'), '')
    记 = next((c['prompt'] for c in 收 if c['label'].startswith('记席')), '')
    厚句 = ('段案估其长约 %s（参考，⛔标的；铁底 2,000）' % 带) if 带 else '铁底 2,000 是唯一硬线，料中之带俱係参考（⛔标的）'
    全 = lambda f: bool(笔) and all(f(p) for p in 笔)
    return [
        ('执笔令（%d 席）：拍库只为尺——⛔「本章叫绝之拍逐拍对着它」（prompts3）' % len(笔), 全(lambda p: '「设定/叫绝之拍库.md」（四十拍）' in p and '逐拍对着它' not in p), False),
        ('执笔令【厚】：带係参考⛔标的（%s）、事尽而短者构思书一行；⛔「本章之带＝」「唯此为准」「低於带不许交」「回去找第二件真事」；【量】只铁底逼补（gates6·prompts9）' % ('段案估其长约 ' + 带 if 带 else '无带：铁底 2,000 是唯一硬线'),
         全(lambda p: 厚句 in p and '事已说尽而低於带者，构思写一句此章何以当短' in p and '本章之带＝' not in p and '唯此为准' not in p
                 and '低於带不许交' not in p and '回去找第二件真事' not in p and '低於铁底或硬项非零，补一回再量' in p and '事未说尽，照旧回去补真事；事已说尽，照【厚】写一句何以当短' in p), False),
        ('执笔令【节奏】：段长有呼吸、碎拍即病（90 分位 ≥30）、长段该来时别削；⛔「至少一处 120 字以上长段」（gates13·prompts10）',
         全(lambda p: '【节奏】段长有呼吸；全章切成一样长的碎拍即病（90 分位 ≥30）；长段该来时别削' in p and '120 字以上长段' not in p), False),
        (('执笔令·须厚：⛔【硬项·须厚】、⛔「担不起即换一件更大的事」；「本段若须一件更大的事，由段庭定」（docs7）' if 须厚 else '执笔令·不传须厚：⛔须厚之句'),
         全(lambda p: '【硬项·须厚】' not in p and '担不起即换一件更大的事' not in p and (('本段若须一件更大的事，由段庭定' in p) if 须厚 else '须厚' not in p)), False),
        ('选令：⛔「线之带以下之稿⛔作胜稿」；拍库之分「胜稿若有叫绝之拍…；无写「无」」（prompts9·prompts3）',
         '线之带以下之稿' not in 选 and '⑤ **拍库之分**：胜稿若有叫绝之拍，逐拍 0—10' in 选 and '｜…」）；无写「无」。' in 选, False),
        ('合令：开镜卡若定了叫绝之拍方落到顶、未定者⛔造一拍（prompts3）',
         '4. 开镜卡若定了叫绝之拍，落到顶' in 合 and '未定者⛔造一拍' in 合 and '叫绝之拍须落到顶：料中开镜卡所定之拍' not in 合, False),
        # 〔1119 死规之审·复核〕「合令·咬合」一条删：gates16／prompts7 退回（咬合哨、chk_yaohe 照硬，令⛔软於闸）——其全文改入下「守牙·合令」
        # 〔1119 死规之审·gates6／docs7·复核〕选令之须厚：⛔「作底须写其由」「稿俱不及即交总编辑」（作者 0722「2000以上长短全由戏定」）
        (('选令·须厚：⛔「净重 <2,900 之稿作底须写其由」「稿俱不及即交总编辑」；只作参考（docs7·gates6）' if 须厚 else '选令·不传须厚：⛔须厚之句'),
         ('【须厚·参考（分量闸·须厚）】分量闸报本章宜厚（约 2,900，⛔标的）：净重只作参考' in 选 and '之稿作底须写其由' not in 选 and '稿俱不及即交总编辑' not in 选)
         if 须厚 else '须厚' not in 选, False),
        ('合令：⛔「零数之日·X115」之补（gates5·466:9 即其所插）', '零数之日' not in 合 and 'X115' not in 合 and '页头前一日之数' not in 合, False),
        ('合令·致命之器：厚只铁底 2,000 致命、低於带只报（⛔「净重低於线之带」）（prompts9）',
         '崩坏闸、厚（只铁底 2,000；低於带⛔致命））必须全绿才许交' in 合 and '厚（净重低於铁底 2,000）不是你能补的' in 合 and '低於带而过铁底者只报其数（⛔补字）' in 合
         and '净重低於线之带' not in 合, False),
        ('记令·开镜卡：「下一章之一事与叫绝之拍（若有）」（prompts3·docs4）', '须写明下一章之一事与叫绝之拍（若有）。' in 记, False),
        # 守牙（472、473 俱须在）
        ('守牙·执笔令：铁底 2,000、⛔凑字、【硬项·白文与骨记同守】、⛔抄前章、构思之满分之问俱在',
         全(lambda p: '铁底 2,000' in p and '⛔凑字' in p and '【硬项·白文与骨记同守】' in p and '⛔抄前章' in p and '「## 满分之问」' in p), True),
        ('守牙·选令：⑩低於 8 不许作底、缺档残档抄 ≥12% 判致命、量叫绝之拍、拍库之分（beat_scores）',
         '⑩低於 8 者不许作底' in 选 and '缺档、残档（末段不全）或抄 ≥12% 者，判该稿致命' in 选 and '**量叫绝之拍**' in 选 and '⑤ **拍库之分**' in 选, True),
        ('守牙·合令：致命之器（起草闸、硬闸、抄袭闸、崩坏闸、厚）全绿方交、落不到顶即重排、厚之数交总编辑',
         '**致命之器（起草闸、硬闸、抄袭闸、崩坏闸、厚' in 合 and '必须全绿才许交**' in 合 and '落不到顶即回去重排那一拍（此属造）' in 合
         and '不是你能补的（不在致命与大进之列）：照报其数，交总编辑' in 合 and '「咬合：拍X（：行）……」' in 合
         # 〔1119 死规之审·复核〕咬合之令全文照留（gates16 退回：闸照硬，令⛔软）
         and '咬合哨：331 起每五章须有一章报「两件事咬在一起」' in 合 and '造式验之「咬合哨」若报满窗将空而本章非咬合，写进 reds 交总编辑' in 合, True),
        ('守牙·记令：下一章开镜卡须写明下一章之一事', '须写明下一章之一事与叫绝之拍' in 记, True),
    ]


def 好看之判(收, 果, 日, n=485):
    """★1124 治16：→ [(条, 合否, 守否)]——不想→（好看回写）→仍不想→⛔停：照常续记席、好看之欠入 log 与下一步（复盘）、⛔设 misread、⛔入 病() 与 X82 之停支。
    新条拿「⛔好看门」之变体（旧行：不想只入 log）来判须俱红；守（⛔停、⛔设 misread）旧行本即如此，两版俱须绿（回灌）。"""
    标 = [c['label'] for c in 收]
    好 = 果.get('好看') or {}
    欠 = '不想之由·盲读·2·好看'
    写 = next((c for c in 收 if c['label'] == '回写·好看'), None)
    记 = next((c['prompt'] for c in 收 if c['label'].startswith('记席')), '')
    return [
        ('不想 → 回写·好看、盲读·2·好看 各一席，在逻辑审之後、记席之前', 标.count('回写·好看') == 1 and 标.count('盲读·2·好看') == 1
         and bool(标) and 标[-3:] == ['回写·好看', '盲读·2·好看', '记席'], False),
        ('守·仍不想 → ⛔停（果无「停」、记席照跑）', '停' not in 果 and any(l.startswith('记席') for l in 标), True),
        ('好看之欠＝盲读·2 之 why_next：入果、入 log、入下一步之复盘', 好.get('欠') == 欠 and any(('好看之欠：' + 欠) in l for l in 日)
         and ('「- 好看之欠：%s」' % 欠) in 果.get('下一步', ''), False),
        ('守·⛔设 misread、⛔入 病() 之支：逻辑审 misread 照 false、⛔派读误之回写与逻辑审·2', (果.get('逻辑审') or {}).get('misread') is False
         and '回写' not in 标 and not any(l.startswith('逻辑审·2') for l in 标), True),
        ('记令带【治16·好看】：盲读诸答係盲读·2、轮记追加「## 造式·盲读·好看复验（治16）」、left 书好看之欠', '【治16·好看】盲读不想（好看回写之前·由：不想之由·盲读）' in 记
         and '想读下一章：不想（%s）' % 欠 in 记 and '「## 造式·盲读·好看复验（治16）」' in 记 and ('left 书「好看之欠：%s」' % 欠) in 记, False),
        ('回写·好看 之令：以 why_next 为的、三禁（⛔加钩／⛔掐尾吊人／⛔加解释句·引 0925 二废）、先查轮记⛔重改、造式验与存版；⛔读误之令（effort max·同通式）',
         bool(写) and '其由：「不想之由·盲读」' in 写['prompt'] and all(k in 写['prompt'] for k in (
             '**⛔加钩**', '**⛔掐尾吊人**', '**⛔加解释句**', '总编辑复核账 0925 二废', '「一章.js·收章句须踢进下一章」', '「起草庭·预五钩<7须补钩之底」',
             '已有「## 好看·合後回写（治16）」之节者', 'python3 工具/造式验.py %d' % n, 'python3 工具/跑轮.py --存 %d "造式二代·好看回写' % n,
             '只治「不想」之由所指之卡处', '只填「rewrite」一键')) and '读误只许加一个动作' not in 写['prompt'] and '逻辑审查出' not in 写['prompt']
         and 写['effort'] == 'max' and 写['schema'] == 收[0]['schema'], False),
    ]


def 跑():
    R = []
    d = tempfile.mkdtemp(prefix='造章令_')
    try:
        器 = os.path.join(d, '渲.js')
        open(器, 'w', encoding='utf-8').write(_器)
        # ①N≤397 逐字不变（键序亦入）
        坏 = []
        for k, v in sorted(_基.items()):
            if 指(渲(器, int(k[:3]), k[3], k[4])) != v:
                坏.append(k)
        R.append(('①N≤397 之诸令逐字不变、键序不变（%d 局·原序 sha256 同改前之基）%s' % (len(_基), ('｜⛔变：' + '、'.join(坏[:8])) if 坏 else ''), not 坏))
        # ①之回灌：397 之收把一份 schema 之键换序——原序之指须变（旧 sort_keys 之指不变，验不出）
        收397 = 渲(器, 397)
        i = next(j for j, c in enumerate(收397) if c['schema'])
        sc = 收397[i]['schema']
        换 = [dict(c) for c in 收397]
        换[i] = dict(换[i], schema=dict(sc, properties=dict(reversed(list(sc['properties'].items())))))
        旧指 = lambda 收: hashlib.sha256(json.dumps(收, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]
        R.append(('回灌·①schema 之键换序→原序之指即变（旧 sort_keys 之指不变：%s）' % ('验不出' if 旧指(换) == 旧指(收397) else '?'),
                  指(换) != 指(收397) and 旧指(换) == 旧指(收397)))
        # ②③④ N≥398 诸条俱在（中重·回写一路）；轻重二宽亦渲得起
        收 = 渲(器, 398)
        for 条, ok in 新条(收, 398):
            R.append(('398·' + 条, ok))
        for 重 in ('轻', '重'):
            R.append(('398·%s（宽 %d）渲得起、执笔令俱带首回即落' % (重, {'轻': 3, '重': 7}[重]),
                      all('首回即落】' in c['prompt'] for c in _令(渲(器, 398, 重, '净'), '执笔'))))
        # 回灌：397 之令（旧病）照新条判，须一一红
        旧 = 新条(收397, 397)
        R.append(('回灌·397 之令（旧病）照新条判 %d 条俱红（⛔一律判过）' % len(旧), not any(ok for _, ok in 旧)))
        # 回灌之二：把 398 之令里「首回即落」一段抹去（假其被删），X26 首条须红
        R.append(('回灌·抹去 398 之「首回即落」→ X26 首条红', not 新条(_换笔(收, lambda p: p.replace('首回即落】', '')), 398)[0][1]))
        # 回灌之三：上回（W53 治席首版）之假前提——「读料那一条命令之末接 && cat > 构思」（392—397 读料俱用 Read）→ X26 首条红
        假 = "**第一条工具调用**——读料那一条命令——之末即接「&& cat > 版本/第398章/起草_甲_构思.md <<'EOF'」建档；"
        R.append(('回灌·上回之假前提（读料之 Bash 末接 cat > 构思）→ X26 首条红',
                  not 新条(_换笔(收, lambda p: p.replace('你的**第一条消息**', 假 + '你的**第一条消息**')), 398)[0][1]))
        # 回灌之四：上回之牵扯——「思考里只想眼下这一拍」（与构思①全章怎么排、②三种写法相牵）→ 第三条红
        R.append(('回灌·「思考里只想眼下这一拍；⛔在思考里把全章排完」之牵 → X26 第三条红',
                  not 新条(_换笔(收, lambda p: p.replace('思考里一回只想一样', '思考里只想眼下这一拍')), 398)[2][1]))
        # ⑤X33（1020）：N≥399 记令述记料以今之十二节；398 照旧（已封之章之令⛔变）
        记399 = (_令(渲(器, 399), '记席') or [{'prompt': ''}])[0]['prompt']
        记398 = (_令(收, '记席') or [{'prompt': ''}])[0]['prompt']
        R.append(('399·X33 记令述记料十二节（【十二】canon 卡名在）；398 仍旧式（九件事）',
                  '十二节已汇' in 记399 and '【十二】canon' in 记399 and '九件事要翻' not in 记399 and '九件事要翻' in 记398 and '十二节已汇' not in 记398))
        # ①之二·1024：398—410 逐字不变
        坏2 = [k for k, v in sorted(_基二.items()) if 指(渲(器, int(k[:3]), k[3], k[4], 厚='厚' if k.endswith('厚') else '否')) != v]
        R.append(('①之二 N≤410 之诸令逐字不变、键序不变（%d 局·原序 sha256 同 c2659cdc 之基）%s' % (len(_基二), ('｜⛔变：' + '、'.join(坏2[:8])) if 坏2 else ''), not 坏2))
        for 名, ok in 通之条(器):
            R.append(('1024·' + 名, ok))
        for 名, ok in X62之条(器):
            R.append(('X62·' + 名, ok))
        # ⑥★1020 X40：须厚入令——401（须厚:true）之执笔令带其硬项、选令带其底；400 传之亦⛔认；401 不传者⛔带
        for 名, ok in 须厚之条(器):
            R.append(('X40·' + 名, ok))
        # ⑨★1106 X88／X89：N≥431 之执笔令带「构思档只录定案」「前章原字之限」；430 ⛔带（N≤430 之令一字不动）
        执431 = _令(渲(器, 431), '执笔'); 执430 = _令(渲(器, 430), '执笔')
        R.append(('X88／X89·431 执笔令 %d 席俱带「构思档只录定案」「前章原字之限」；430 之 %d 席⛔带' % (len(执431), len(执430)),
                  bool(执431) and all('【构思档只录定案·X88】' in c['prompt'] and '【前章原字之限·X89】' in c['prompt'] for c in 执431)
                  and bool(执430) and not any('X88】' in c['prompt'] or 'X89】' in c['prompt'] for c in 执430)))
        # ⑩★1111 X95①：N≥442 之记令带「一事一处」；441 ⛔带（N≤441 之令一字不动）
        记442 = (_令(渲(器, 442), '记席') or [{'prompt': ''}])[0]['prompt']
        记441 = (_令(渲(器, 441), '记席') or [{'prompt': ''}])[0]['prompt']
        R.append(('X95①·442 记令带「一事一处」；441 ⛔带', '【一事一处·X95①】' in 记442 and bool(记441) and 'X95①】' not in 记441))
        # ⑪★1112 X100③：N≥450 之记令带「锚之律」（⛔句号、⛔破折）；449 ⛔带
        记450 = (_令(渲(器, 450), '记席') or [{'prompt': ''}])[0]['prompt']
        记449 = (_令(渲(器, 449), '记席') or [{'prompt': ''}])[0]['prompt']
        R.append(('X100③·450 记令带「锚之律」；449 ⛔带', '【锚之律·X100③】' in 记450 and bool(记449) and 'X100③】' not in 记449))
        # ⑫★1113 X106②：N≥455 之记令带「回执之思」（先骨後判、⛔通篇拟）；454 ⛔带
        记455 = (_令(渲(器, 455), '记席') or [{'prompt': ''}])[0]['prompt']
        记454 = (_令(渲(器, 454), '记席') or [{'prompt': ''}])[0]['prompt']
        R.append(('X106②·455 记令带「回执之思」；454 ⛔带', '【回执之思·X106②】' in 记455 and bool(记454) and 'X106②】' not in 记454))
        # ⑫★1112 X101①：N≥452 承回写而 args 带 裁＋销 → ⛔派 盲读·2／逻辑审·2、只跑记席；缺销、或 451 → 照跑
        def _验席(n, 加):
            return [c['label'] for c in 渲(器, n, 加=加)]
        承病 = {'承': {'回写': True}}
        销452 = _验席(452, dict(承病, 裁='已亲治读误', 销=True))
        R.append(('X101①·452 回写既承＋裁＋销 → 盲读·2／逻辑审·2 ⛔派、记席照跑；缺销或 451 → 照派',
                  '盲读·2' not in 销452 and '逻辑审·2' not in 销452 and any(l.startswith('记席') for l in 销452)
                  and '逻辑审·2' in _验席(452, dict(承病, 裁='已亲治读误')) and '逻辑审·2' in _验席(451, dict(承病, 裁='已亲治读误', 销=True))))
        # ⑫之二★1118 X114：N≥466 --销 而只余读误 → 器自派 盲读·3＋逻辑审·3 验销（假交之审净 → 记席照跑）；465 ⛔派
        承误 = {'承': {'回写': True, '审': {'hard': [], 'soft': '软', 'gate': '闸', 'misread': True, 'misread_where': '处', 'misread_fix': '治'}}}
        销466 = _验席(466, dict(承误, 裁='已亲治读误', 销=True)); 销465 = _验席(465, dict(承误, 裁='已亲治读误', 销=True))
        R.append(('X114·466 --销 只余读误 → 盲读·3、逻辑审·3 各一席验销、记席照跑；465 ⛔派、只跑记席',
                  '盲读·3' in 销466 and '逻辑审·3' in 销466 and any(l.startswith('记席') for l in 销466) and '逻辑审·2' not in 销466
                  and '盲读·3' not in 销465 and '逻辑审·3' not in 销465 and any(l.startswith('记席') for l in 销465)))
        # ⑫之三★1118 X115：N≥467 合令带「零数之日」（一章一日照 464、466 之裁当场治）；466 ⛔带
        合467 = (_令(渲(器, 467), '合稿') or [{'prompt': ''}])[0]['prompt']; 合466 = (_令(渲(器, 466), '合稿') or [{'prompt': ''}])[0]['prompt']
        R.append(('X115·467 合令带「零数之日」；466 ⛔带', '【零数之日·X115】' in 合467 and bool(合466) and 'X115】' not in 合466))
        # ⑬★1118 无稿之标（a9e5cc5ee 根病②）：N≥464 执笔·甲乙丙被平台安全之检拦而未交 → 选之先跑首接「大师之关.py --标无稿 N 宽 稿号」（〔原场〕仍居印末），
        #   其稿号以 大师之关.号之席 逆之即被拦之席（JS 蒙号与 Python 之逆同式）、令里⛔现执笔之名（蒙名）；463、非安全之错、丁席、无拒 → ⛔接
        import importlib.util as _iu
        _sp = _iu.spec_from_file_location('大师之关', os.path.join(ROOT, '工具', '大师之关.py')); _关 = _iu.module_from_spec(_sp); _sp.loader.exec_module(_关)
        安错 = 'API Error: Claude Code is unable to respond to this request, which appears to violate our Usage Policy (AUP)'
        选令之 = lambda n, 拒=None, 重='中': (_令(渲(器, n, 重, '净', 拒=拒), '选') or [{'prompt': ''}])[0]['prompt']
        标 = lambda s: (re.search(re.escape('：python3 工具/大师之关.py --标无稿 ') + r'(\d+) (\d) ([^;\s]+); for f in ', s) or [None] * 4)   # re.escape：死处方哨认「大师之关\.py」为器名而红（同 242 行之例）
        m464 = 标(选令之(464, {'执笔·乙': 安错}))
        m464二 = 标(选令之(464, {'执笔·丙': 安错, '执笔·甲': 安错}, '重'))
        R.append(('无稿之标·464 乙被安全之检拦 → 选之先跑接 --标无稿 464 5 %s（逆之＝%s·令里⛔执笔之名）；甲丙俱拦（重·宽五·余三稿足）→ %s；463、非安全之错、丁被拦、无拒 → ⛔接'
                  % (m464[3] if m464[0] else '?', _关.号之席(464, 5, m464[3]) if m464[0] else '?', m464二[3] if m464二[0] else '?'),
                  bool(m464[0]) and (m464[1], m464[2]) == ('464', '5') and _关.号之席(464, 5, m464[3]) == '乙' and not re.search('[甲乙丙丁戊己庚]', m464[0])
                  and bool(m464二[0]) and m464二[2] == '5' and sorted(_关.号之席(464, 5, h) for h in m464二[3].split(',')) == ['丙', '甲']
                  and '--标无稿' not in 选令之(463, {'执笔·乙': 安错})
                  and '--标无稿' not in 选令之(464, {'执笔·乙': 'Request timed out after retries'})
                  and '--标无稿' not in 选令之(464, {'执笔·丁': 安错})
                  and '--标无稿' not in 选令之(464)))
        # ⑬之二★1118 总编辑复核「大师之关」→改（桩从运行时之约·ZJ_死：其席之 agent() 返 null、拒因恒空）：N≥467 拦号凭「甲乙丙之席无稿」之实（⛔凭拒因）——
        #   467 乙 null → 选之先跑接「--标无稿 467 宽 稿号」（逆之＝乙·令里⛔执笔之名）；重·甲丙 null → 二号（逆之＝甲丙）；丁 null、无 null → ⛔接；
        #   466 乙 null → ⛔接（464—466 之支凭 安全拒·拒因恒空·一字未动）
        选令死 = lambda n, 死=None, 重='中': (_令(渲(器, n, 重, '净', 死=死), '选') or [{'prompt': ''}])[0]['prompt']
        m467 = 标(选令死(467, ['执笔·乙']))
        m467二 = 标(选令死(467, ['执笔·甲', '执笔·丙'], '重'))
        R.append(('无稿之标·467 乙 agent() 返 null（运行时之约）→ 选之先跑接 --标无稿 467 5 %s（逆之＝%s·令里⛔执笔之名）；重·甲丙 null → %s；丁 null、无 null、466 乙 null → ⛔接'
                  % (m467[3] if m467[0] else '?', _关.号之席(467, 5, m467[3]) if m467[0] else '?', m467二[3] if m467二[0] else '?'),
                  bool(m467[0]) and (m467[1], m467[2]) == ('467', '5') and _关.号之席(467, 5, m467[3]) == '乙' and m467[3] == _关.席之号(467, 5, '乙')
                  and not re.search('[甲乙丙丁戊己庚]', m467[0])
                  and bool(m467二[0]) and m467二[2] == '5' and sorted(_关.号之席(467, 5, h) for h in m467二[3].split(',')) == ['丙', '甲']
                  and '--标无稿' not in 选令死(467, ['执笔·丁'])
                  and '--标无稿' not in 选令死(467)
                  and '--标无稿' not in 选令死(466, ['执笔·乙'])))
        # ⑭★1118 总编辑裁·X79 R：补派之「安全拒」之滤（⛔同令补派）於运行时之约下恒⛔行（agent() 遇终错返 null、parallel ⛔reject、拒因恒空），
        #   420—466 未发一回——X79 之活守係 足()（整稿 ≥3 ⛔补）＋缺稿不足三时一回补＋补後 <3 即停；其滤 N≥468 废（拒因、安全拒、.catch 照留·⑬ 赖之）。
        #   N≤467 诸桩局之令逐字同改前之基（已过之章·钉）。N≥468 未写之章⛔钉其指（其令日後合法之改即假红）——以今之 js 与废其门之变体
        #   （420≤N≤467 → N≥420，即改前之行）同时渲而相较：无桩、ZJ_死（运行时之约）、ZJ_拒 而稿足三诸局两版同；ZJ_拒（非运行时之桩·throw）甲丙死、乙被拒（混）：
        #   467 照滤（补甲丙、⛔补乙），468 ⛔滤（补甲乙丙·其令逐字同今渲之 ZJ_死 三席之局：拒与死不复异行）；轻（宽三）乙一席被拒：467 照停、468 补乙而足三
        def _局(n, 重, k):
            净收 = 渲(器, n, 重, '净')
            f = {x: next(c['label'] for c in 净收 if c['label'].startswith('执笔·' + x + '·')) for x in '甲乙丙'}   # 首回之全 label（补、查之 label ⛔中）
            return {'净': {}, '拒乙': {'拒': {'执笔·乙': 安错}}, '死乙': {'死': ['执笔·乙']}, '死三': {'死': [f['甲'], f['乙'], f['丙']]},
                    '混': {'拒': {f['乙']: 安错}, '死': [f['甲'], f['丙']]}, '拒乙全': {'拒': {f['乙']: 安错}}}[k]
        def _渲局(键, js=JS):
            n, 重, k = int(键[:3]), 键[3], 键[4:]
            return 渲(器, n, 重, '净', js=js, **_局(n, 重, k))
        坏3 = [k for k, v in sorted(_基三.items()) if 指(_渲局(k)) != v]
        补之席 = lambda 收: ''.join(sorted((c['label'][3] for c in 收 if c['label'].startswith('执笔·') and c['label'].endswith('·补')), key='甲乙丙丁戊'.index))
        def _试局(键, js=JS):   # → (收, 停之由)：停（交稿不足三之 throw）者收为 []
            try:
                return _渲局(键, js), ''
            except RuntimeError as e:
                return [], str(e)
        # 废其门之变体：今之 js 唯去 420≤N≤467 之上界（滤与其 log 二处）——即改前之行；N≥468 之令日後之改两版同带，相较⛔假红
        门 = 'N >= 420 && N <= 467 && '
        源 = open(JS, encoding='utf-8').read()
        废门 = os.path.join(d, '造章_废门.js')
        open(废门, 'w', encoding='utf-8').write(源.replace(门, 'N >= 420 && '))
        门在 = 源.count(门 + '安全拒(x.名)') == 1 and 源.count(门) == 2
        对 = lambda 键, js=JS: (lambda r: '停' if r[1] else 指(r[0]))(_试局(键, js))
        同局 = ('468中净', '468中死乙', '468中死三', '468中拒乙', '470中净', '470中死乙', '470中死三', '467中混')
        异局 = ('468中混', '468轻拒乙全', '470中混', '470轻拒乙全')
        坏同 = [k for k in 同局 if 对(k) != 对(k, 废门)]
        坏异 = [k for k in 异局 if 对(k) == 对(k, 废门)]
        混467, 混468, 混468废 = _渲局('467中混'), _渲局('468中混'), _渲局('468中混', 废门)
        停467 = _试局('467轻拒乙全')[1]
        轻468, 停468 = _试局('468轻拒乙全')
        R.append(('X79 R·N≤467 诸桩局（无桩、ZJ_拒、ZJ_死、混）之令逐字同改前之基（%d 局·已过之章）%s'
                  % (len(_基三), ('｜⛔变：' + '、'.join(坏3[:8])) if 坏3 else ''), not 坏3))
        R.append(('X79 R·N≥468 ⛔钉指——今之 js 对废其门之变体（改前之行）同时渲：无桩、ZJ_死、拒而稿足三诸局两版同（%d 局·467 混局亦同：门只动 N≥468）、'
                  '468 拒乙＝死乙（稿足三⛔补）；ZJ_拒 混局、轻局两版异（%d 局）%s'
                  % (len(同局), len(异局), ''.join(['' if 门在 else '｜⛔门之文不见（滤与 log 二处）', ('｜⛔异：' + '、'.join(坏同)) if 坏同 else '',
                                                  ('｜⛔同：' + '、'.join(坏异)) if 坏异 else ''])),
                  门在 and not 坏同 and not 坏异 and 对('468中拒乙') == 对('468中死乙')))
        R.append(('X79 R·ZJ_拒 混局（甲丙死、乙被安全之检拒）：467 照滤（补%s）、468 ⛔滤（补%s·令逐字同今渲之 ZJ_死 三席之局；废门之变体照滤·补%s）'
                  % (补之席(混467), 补之席(混468), 补之席(混468废)),
                  补之席(混467) == '甲丙' and 补之席(混468) == '甲乙丙' and 指(混468) == 指(_渲局('468中死三'))
                  and 补之席(混468废) == '甲丙' and 指(混468) != 指(混468废)))
        R.append(('X79 R·轻（宽三）乙一席被拒：467 照停（交稿不足三·其滤犹在）；468 先查後补乙而足三（补%s%s）' % (补之席(轻468), '｜⛔468 停' if 停468 else ''),
                  '交稿不足三（2）' in 停467 and not 停468 and 补之席(轻468) == '乙' and '执笔·乙·查' in [c['label'] for c in 轻468]))
        # ⑮★1119 X118：468 执笔·甲交 {draft:{file:"",words:0}} 而认已交、丁戊死，整稿只二、补派⛔起——N≥470 空稿作未交：
        #   470 甲空稿＋丁戊死 → 先查甲、再补甲丁戊（交稿足三）；甲空稿而余四席俱交 → ⛔补（足三）、选之列⛔含甲；469 同局照旧（甲认已交、⛔查⛔补）
        def _首(n, 重='中'):
            净收 = 渲(器, n, 重, '净')
            return {x: next(c['label'] for c in 净收 if c['label'].startswith('执笔·' + x + '·')) for x in '甲乙丙丁戊'}
        f470, f469 = _首(470), _首(469)
        收470 = 渲(器, 470, '中', '净', 空稿=[f470['甲']], 死=[f470['丁'], f470['戊']])
        收469 = 渲(器, 469, '中', '净', 空稿=[f469['甲']], 死=[f469['丁'], f469['戊']])
        收470足 = 渲(器, 470, '中', '净', 空稿=[f470['甲']])
        标470 = [c['label'] for c in 收470]; 标469 = [c['label'] for c in 收469]; 标足 = [c['label'] for c in 收470足]
        补470 = ''.join(sorted((l[3] for l in 标470 if l.startswith('执笔·') and l.endswith('·补')), key='甲乙丙丁戊'.index))
        R.append(('X118·470 甲空稿（file 空、words 0）＋丁戊死 → 查甲、补%s；469 同局照旧（⛔查⛔补）；470 甲空稿余四俱交 → ⛔补（足三）'
                  % (补470 or '无'),
                  '执笔·甲·查' in 标470 and 补470 == '甲丁戊' and not any(l.endswith('·查') or l.endswith('·补') for l in 标469)
                  and not any(l.endswith('·补') for l in 标足)))
        # ⑯★1119 X119：N≥471 args.带（段案本章「字数」）→ 诸执笔令【厚】首句「本章之带＝a—b」；N≤470 传之亦⛔认（与不传者原序之指同）；式不合（非 d,ddd—d,ddd）⛔认
        带句 = '**本章之带＝2,900—3,300**（段案本章「字数」——唯此为准'
        笔471 = [c['prompt'] for c in 渲(器, 471, '中', '净', 加={'带': '2,900—3,300'}) if c['label'].startswith('执笔')]
        笔471无 = [c['prompt'] for c in 渲(器, 471, '中', '净') if c['label'].startswith('执笔')]
        笔471坏 = [c['prompt'] for c in 渲(器, 471, '中', '净', 加={'带': '2900-3300'}) if c['label'].startswith('执笔')]
        R.append(('X119·471 带 2,900—3,300 → 诸执笔令俱带「本章之带」；不传、式坏者⛔带；470 传之与不传者之指同',
                  bool(笔471) and all(带句 in p for p in 笔471) and not any('本章之带＝' in p for p in 笔471无 + 笔471坏)
                  and 指(渲(器, 470, '中', '净', 加={'带': '2,900—3,300'})) == 指(渲(器, 470, '中', '净'))))
        # ⑰〔1119 死规之审〕N≥473 只拔逐章配额之牙；N≤472 逐字同改前之基（_基四）；守牙仍在；schema、effort、余席之令⛔动
        带9 = {'带': '2,900—3,300'}
        渲4 = lambda k, js=JS: 渲(器, int(k[:3]), k[3], k[4], js=js, 厚='厚' if '厚' in k[5:] else '否', 加=带9 if k.endswith('带') else None)
        坏4 = [k for k, v in sorted(_基四.items()) if 指(渲4(k)) != v]
        R.append(('死规审·N≤472 之诸令逐字同改前之基（%d 局·468—472×中净／中病／轻病／须厚／带／须厚带·原序 sha256 同 0f8afe5d9 之基）%s'
                  % (len(_基四), ('｜⛔变：' + '、'.join(坏4[:8])) if 坏4 else ''), not 坏4))
        收473 = 渲(器, 473, '中', '病', 厚='厚', 加=带9)
        判473 = 死规之判(收473, 带='2,900—3,300', 须厚=True)
        for 条, ok, _ in 判473:
            R.append(('死规审·473（须厚·带）' + 条, ok))
        for 重, 病, 加 in (('中', '净', None), ('轻', '病', None), ('重', '净', {'带': '2900-3300'})):   # 无带、式坏之带 → 带之句⛔现
            坏 = [条 for 条, ok, _ in 死规之判(渲(器, 473, 重, 病, 加=加), 须厚=False) if not ok]
            R.append(('死规审·473（%s%s%s）⑰ 诸条俱合%s' % (重, 病, '·式坏之带' if 加 else '·无带', ('｜⛔' + '；'.join(坏)[:200]) if 坏 else ''), not 坏))
        # 回灌：472 之令（N≤472 照旧）与 473「⛔死规审」之变体照 ⑰ 判——新条俱红、守牙俱绿（⛔一律判过）
        源4 = open(JS, encoding='utf-8').read()
        门4 = 'const 死规审自 = 473, 死规审 = N >= 死规审自'
        旧变 = os.path.join(d, '造章_无死规审.js')
        open(旧变, 'w', encoding='utf-8').write(源4.replace(门4, 'const 死规审自 = 473, 死规审 = false'))
        收472 = 渲(器, 472, '中', '病', 厚='厚', 加=带9)
        收473旧 = 渲(器, 473, '中', '病', js=旧变, 厚='厚', 加=带9)
        for 名, 收x in (('472 之令', 收472), ('473「⛔死规审」之变体', 收473旧)):
            判x = 死规之判(收x, 带='2,900—3,300', 须厚=True)
            误 = [条 for 条, ok, 牙 in 判x if ok != 牙]
            R.append(('死规审·回灌 %s：新条 %d 俱红、守牙 %d 俱绿%s' % (名, sum(1 for *_, 牙 in 判x if not 牙), sum(1 for *_, 牙 in 判x if 牙),
                                                         ('｜⛔' + '；'.join(误)[:200]) if 误 else ''), 源4.count(门4) == 1 and not 误))
        # ⛔顺手改：473 与其变体——席同、schema 同、effort 同；盲读、逻辑审、回写之令逐字同；schema 与 472 同（⛔改 schema）
        异席 = sorted({a['label'].split('·')[0] for a, b in zip(收473, 收473旧) if a['prompt'] != b['prompt']})
        R.append(('死规审·只动执笔、选、合稿、记席四令（异：%s）；盲读、逻辑审、回写逐字同；席、schema、effort 同变体，schema 同 472' % '、'.join(异席),
                  [c['label'] for c in 收473] == [c['label'] for c in 收473旧] and 异席 == ['合稿', '执笔', '记席', '选']
                  and all(a['schema'] == b['schema'] and a['effort'] == b['effort'] for a, b in zip(收473, 收473旧))
                  and 指([c['schema'] for c in 收473]) == 指([c['schema'] for c in 收472])))
        # ⑱★1124 治16（W918 环4·执行之制 批四 A4）：盲读 want_next=false → N≥485 好看回写一回、盲读·2 复读；仍不想即 log「好看之欠」入复盘、照常续记席——
        #   ⛔设 misread、⛔入 病() 与 X82 之停支；回写或盲读·2 遇拒或 null ⛔同令再请（X138）；N≤484 逐字同改前之基（_基五·473—484·891fc0574）
        带9_ = {'带': '2,900—3,300'}
        def 渲5(k, js=JS):
            n, 重, 病, 旗 = int(k[:3]), k[3], k[4], k[5:]
            return 渲(器, n, 重, 病, js=js, 厚='厚' if '厚' in 旗 else '否', 加=带9_ if '带' in 旗 else None, 不想=['盲读*'] if '不想' in 旗 else None)
        坏5 = [k for k, v in sorted(_基五.items()) if 指(渲5(k)) != v]
        R.append(('治16·N≤484 之诸令逐字同改前之基（%d 局·473—484×中净／中病／轻病／中误／须厚带／不想×三·原序 sha256 同 891fc0574 之基）%s'
                  % (len(_基五), ('｜⛔变：' + '、'.join(坏5[:8])) if 坏5 else ''), not 坏5))
        不想484 = [渲5(k) for k in ('484中净不想', '484中误不想', '484轻净不想')]
        R.append(('治16·484 同基：盲读俱不想（净、误、轻）→ ⛔好看之席（%s）、令同基' % '／'.join(str(len(x)) + '席' for x in 不想484),
                  not 坏5 and not any('好看' in c['label'] for x in 不想484 for c in x)))
        源5 = open(JS, encoding='utf-8').read()
        门5 = 'const 好看自 = 485, 好看门 = N >= 好看自'
        废5 = os.path.join(d, '造章_无好看.js'); 早5 = os.path.join(d, '造章_好看484.js')
        open(废5, 'w', encoding='utf-8').write(源5.replace(门5, 'const 好看自 = 485, 好看门 = false'))
        open(早5, 'w', encoding='utf-8').write(源5.replace(门5, 'const 好看自 = 484, 好看门 = N >= 好看自'))
        # 回灌：门误书作 484 → _基五 之 484 不想三局即变（钉咬得住）；484 想之局与 483 照同
        坏早 = [k for k, v in sorted(_基五.items()) if k[:3] in ('483', '484') and 指(渲5(k, 早5)) != v]
        R.append(('治16·回灌·门误书作 N≥484 → _基五 之 484 不想三局即变（%s）、余局照同' % ('、'.join(坏早) or '无'),
                  源5.count(门5) == 1 and sorted(坏早) == ['484中净不想', '484中误不想', '484轻净不想']))
        # 485 多回写：想之局与「⛔好看门」之变体逐字同（⛔顺手改）；不想之局只多二席、诸席之令除记席外逐字同
        想同 = [k for k in ('485中净', '485中病', '485中误', '485轻病', '485中病厚带') if 指(渲5(k)) != 指(渲5(k, 废5))]
        R.append(('治16·485 想之局（净、病、误、轻、须厚带）与「⛔好看门」之变体逐字同（读误之回写令一字未动）%s' % (('｜⛔异：' + '、'.join(想同)) if 想同 else ''), not 想同))
        for k in ('485中净不想', '485中误不想', '485轻净不想'):
            新, 旧 = 渲5(k), 渲5(k, 废5)
            新标, 旧标 = [c['label'] for c in 新], [c['label'] for c in 旧]
            新去 = [c for c in 新 if c['label'] not in ('回写·好看', '盲读·2·好看')]
            异 = sorted({a['label'] for a, b in zip(新去, 旧) if a != b})
            R.append(('治16·%s 多回写：席＝旧席＋「回写·好看」「盲读·2·好看」於记席之前（%d→%d 席）；余席之令除记席外逐字同（异：%s）' % (k, len(旧标), len(新标), '、'.join(异) or '无'),
                      新标 == 旧标[:-1] + ['回写·好看', '盲读·2·好看', '记席'] and 异 == ['记席']))
        # 不想→仍不想→不停（净、误二路）；回灌：「⛔好看门」之变体照判俱红
        收5, 果5, 日5 = 渲(器, 485, '中', '净', 不想=['盲读*'], 日=True)
        for 条, ok, _ in 好看之判(收5, 果5, 日5):
            R.append(('治16·485 不想→仍不想·' + 条, ok))
        收5误, 果5误, 日5误 = 渲(器, 485, '中', '误', 不想=['盲读*'], 日=True)
        标5误 = [c['label'] for c in 收5误]
        R.append(('治16·485 读误→回写→盲读·2→逻辑审·2 净而仍不想 → 好看回写、盲读·2·好看、记席照跑（⛔停、⛔逻辑审·3）',
                  标5误[-6:] == ['回写', '盲读·2', '逻辑审·2', '回写·好看', '盲读·2·好看', '记席'] and '停' not in 果5误
                  and (果5误.get('好看') or {}).get('欠') == '不想之由·盲读·2·好看' and not any(l.startswith('逻辑审·3') for l in 标5误)))
        旧5 = 好看之判(*渲(器, 485, '中', '净', js=废5, 不想=['盲读*'], 日=True))
        误5 = [条 for 条, ok, 守 in 旧5 if ok != 守]
        R.append(('治16·回灌·「⛔好看门」之变体（旧行：不想只入 log）照判：新条 %d 俱红、守 %d 俱绿%s' % (sum(1 for *_, 守 in 旧5 if not 守), sum(1 for *_, 守 in 旧5 if 守),
                  ('｜⛔' + '；'.join(误5)[:200]) if 误5 else ''), not 误5))
        # 回灌之二（预审 甲·环7、乙·环7 之险）：不想「视同 misread」并入 病() → 走读误之回写、X82／致命未净之停支 → 守（⛔停、⛔设 misread）即红
        病式 = 'const 病 = (r) => r && ((r.hard && r.hard.length) || 真(r.misread))'
        并病 = os.path.join(d, '造章_不想并病.js')
        open(并病, 'w', encoding='utf-8').write(源5.replace(病式, 'const 病 = (r) => r && ((r.hard && r.hard.length) || 真(r.misread) || (N >= 485 && 盲 && 盲.want_next === false))'))
        并5 = 好看之判(*渲(器, 485, '中', '净', js=并病, 不想=['盲读*'], 日=True))
        守红 = [条 for 条, ok, 守 in 并5 if 守 and not ok]
        R.append(('治16·回灌·「视同 misread」之变体（不想并入 病()）→ 守 %d 条俱红（%s）' % (len(守红), '；'.join(x.split('：')[0] for x in 守红) or '无'),
                  源5.count(病式) == 1 and len(守红) == sum(1 for *_, 守 in 并5 if 守) == 2))
        # 不想→想：好看之欠销、下一步⛔书
        收想, 果想, 日想 = 渲(器, 485, '中', '净', 不想=['盲读'], 日=True)
        R.append(('治16·485 不想→（好看回写）→想 → 好看之欠销（果、下一步⛔书）、盲读诸答取盲读·2、记席照跑',
                  [c['label'] for c in 收想][-3:] == ['回写·好看', '盲读·2·好看', '记席'] and (果想.get('好看') or {}).get('欠') == ''
                  and '好看之欠' not in 果想.get('下一步', '') and any('好看之欠销' in l for l in 日想) and (果想.get('盲读') or {}).get('want_next') is True))
        # X138：回写·好看 null／被拒、盲读·2·好看 null → ⛔同令再请、即续记席、log 其因；自报⛔改 → ⛔盲读·2
        def X138局(**kw):
            收x, 果x, 日x = 渲(器, 485, '中', '净', 不想=['盲读*'], 日=True, **kw)
            return [c['label'] for c in 收x], 果x, 日x
        首由 = '不想之由·盲读'
        for 名, kw, 标次 in (('回写·好看 null（运行时之约）', {'死': ['回写·好看']}, 0), ('回写·好看 被拒（throw）', {'拒': {'回写·好看': 安错}}, 0),
                            ('盲读·2·好看 null', {'死': ['盲读·2·好看']}, 1), ('回写·好看 自报⛔改（done:false）', {'写否': True}, 0)):
            标x, 果x, 日x = X138局(**kw)
            好x = 果x.get('好看') or {}
            R.append(('治16·X138·%s → ⛔同令再请（回写·好看 %d 席、盲读·2·好看 %d 席）、即续记席、log 其因、好看之欠照回写前之由' % (名, 标x.count('回写·好看'), 标x.count('盲读·2·好看')),
                      标x.count('回写·好看') == 1 and 标x.count('盲读·2·好看') == 标次 and not any(l.endswith('·补') for l in 标x)
                      and 标x[-1].startswith('记席') and '停' not in 果x and 好x.get('欠') == 首由
                      and any(('⛔同令再请（X138）' in l) or ('自报未改' in l) for l in 日x)
                      and (('拒：' in 好x.get('回写', '')) if '拒' in kw else True)))
        # 总编辑之裁在（裁後之文）：⛔派好看回写、只书其欠
        收裁, 果裁, _ = 渲(器, 485, '中', '病', 不想=['盲读*'], 加={'承': {'回写': True}, '裁': '已亲治'}, 日=True)
        标裁 = [c['label'] for c in 收裁]
        R.append(('治16·总编辑之裁在（承回写·盲读·2、逻辑审·2 净）→ ⛔派回写·好看与盲读·2·好看、好看之欠照书、记席照跑',
                  '回写·好看' not in 标裁 and '盲读·2·好看' not in 标裁 and 标裁[-1].startswith('记席')
                  and (果裁.get('好看') or {}).get('回写', '').startswith('⛔派') and (果裁.get('好看') or {}).get('欠') == '不想之由·盲读·2'))
        # ⑲〔W919·X138·法用#拒後不再请〕N≥489 进程内⛔同令再请（只改控制之流·诸令一字⛔动）
        坏19 = [k for k, v in sorted(_基六.items()) if _渲19(器, int(k[:3]), **_局19[k[3:]])[1] != v]
        R.append(('⑲之一 N≤488 诸局（485—488×净／病／误／死乙／死四／选死／盲读死／盲读壳／逻辑审死／记死·%d 局）之令、席序、果、抛逐字同 W919 入主前之基（9a8c81b34）%s'
                  % (len(_基六), ('｜⛔变：' + '、'.join(坏19[:6])) if 坏19 else ''), not 坏19))
        判19 = 拒後之判(器, d)
        R += 判19
        # ⑲之六 回放 476—484 之亡席（冻料之执笔之终：API错:invalid_request·拒2）→ 门假 0 之变体与旧行（⛔门）之派席、诸令逐字同
        src19 = open(JS, encoding='utf-8').read()
        零门 = os.path.join(d, '零门19.js'); 无门19 = os.path.join(d, '无门19.js')
        open(零门, 'w', encoding='utf-8').write(src19.replace(_门19, 'const 拒後自 = 0, 拒後 = N >= 拒後自'))
        open(无门19, 'w', encoding='utf-8').write(src19.replace(_门19, 'const 拒後自 = 9999, 拒後 = N >= 拒後自'))
        冻 = {}
        for n in range(476, 483):
            摘 = json.load(open(os.path.join(ROOT, '工具', '_负测料', '成章', '%d.json' % n), encoding='utf-8'))['复盘摘']
            冻[n] = ['执笔·' + m.group(1) for m in re.finditer(r'^\| 执笔·(\S)·\S+ \| API错:invalid_request \| 2 \|', 摘, re.M)]
        冻.update({483: [], 484: ['执笔·乙']})          # 1124_W158_第483章、1124_W159_第484章 之执笔之终（483 俱交、484 乙·换账 拒2）
        同19 = [n for n, 死 in 冻.items() if _渲19(器, n, 零门, 病='净', 死=死 or None)[1] == _渲19(器, n, 无门19, 病='净', 死=死 or None)[1]]
        R.append(('⑲之六 回放 476—484 之亡席（%s·凡 %d 席）→ 门假 0 之变体与旧行之派席、诸令逐字同 %d/9'
                  % ('、'.join('%d:%s' % (n, ''.join(x[3] for x in v)) for n, v in 冻.items() if v), sum(len(v) for v in 冻.values()), len(同19)),
                  len(同19) == 9 and sum(len(v) for v in 冻.values()) == 7))
        # ⑲之七 门之数三书同（造章.js、承.py、续跑之守.py）
        数 = [re.findall(r'(?m)^(?:const )?拒後自 = (\d+)', open(os.path.join(ROOT, '工具', f), encoding='utf-8').read()) for f in ('席/造章.js', '承.py', '续跑之守.py')]
        R.append(('⑲之七 门之数三书同：造章.js %s、承.py %s、续跑之守.py %s（俱 489）' % tuple('／'.join(x) or '无' for x in 数),
                  all(x == ['489'] for x in 数) and src19.count(_门19) == 1))
        # ⑲之七之二〔W924〕整稿之界三书同：造章.js 之门（一稿 1／二稿 2／余 3）＝承.整稿之界（一稿之录 1／二稿之录 2／余 3）；续跑之守 验二录（args.一稿／二稿 无录即拦）
        _承src = open(os.path.join(ROOT, '工具', '承.py'), encoding='utf-8').read()
        _守src = open(os.path.join(ROOT, '工具', '续跑之守.py'), encoding='utf-8').read()
        R.append(('⑲之七之二 整稿之界三书同：造章.js「诸稿.length < (一稿 ? 1 : 二稿 ? 2 : 3)」＝承.整稿之界「1 if 一稿之录 … 2 if 二稿之录 … 3」；续跑之守验 一稿之录、二稿之录',
                  src19.count('诸稿.length < (一稿 ? 1 : 二稿 ? 2 : 3)') == 1 and 'return 1 if 一稿之录(n, root) else 2 if 二稿之录(n, root) else 3' in _承src
                  and "if 一稿 and not _承.一稿之录(n, root):" in _守src and "if 二稿 and not _承.二稿之录(n, root):" in _守src))
        # ⑲之十二之二〔W924〕无 args.一稿 之参 → 489 十局之令、席序、果、抛与「一稿恒假」之变体逐字同；488 十局带 args.一稿 → 照 _基六（N≤488 ⛔认）
        _一门 = 'const 一稿 = 拒後 && !!(args && args.一稿 === true)'
        恒假 = os.path.join(d, '造章_一稿恒假.js')
        open(恒假, 'w', encoding='utf-8').write(src19.replace(_一门, 'const 一稿 = false'))
        异一 = [k for k, kw in _局19.items() if _渲19(器, 489, **kw)[1] != _渲19(器, 489, 恒假, **kw)[1]]
        坏一 = [k for k in _局19 if _渲19(器, 488, **dict(_局19[k], 加={'一稿': True}))[1] != _基六['488' + k]]
        R.append(('⑲之十二之二 无 args.一稿 → 489 十局与「一稿恒假」之变体逐字同%s；488 十局带 args.一稿 → 照 _基六%s' % (
                  '｜⛔异：' + '、'.join(异一) if 异一 else '', '｜⛔变：' + '、'.join(坏一) if 坏一 else ''),
                  src19.count(_一门) == 1 and not 异一 and not 坏一))
        # 回灌：去门之变体 → ⑲之二至五、之八、之九 俱红；键位移入 args.承 之变体 → ⑲之八 红
        回去门 = [条 for 条, ok in 拒後之判(器, d, 无门19) if ok]
        R.append(('⑲·回灌 去门之变体（拒後自 = 9999）→ ⑲之二至五、之八至之十三 俱红（绿 %d：%s）' % (len(回去门), '；'.join(x[:12] for x in 回去门) or '无'), not 回去门))
        键移 = os.path.join(d, '造章_键移承.js')
        键src = src19.replace('const 已分因 = 拒後 && Array.isArray(args && args.补席)', 'const 已分因 = 拒後 && Array.isArray(承.补席)').replace(
            'const 补席 = 已分因 ? args.补席.filter', 'const 补席 = 已分因 ? 承.补席.filter')
        回键 = dict(拒後之判(器, d, 键移) if 键src != src19 and open(键移, 'w', encoding='utf-8').write(键src) else [])
        R.append(('⑲·回灌 键位移入 args.承 之变体 → ⑲之八 红', 键src != src19 and not next((ok for 条, ok in 回键.items() if 条.startswith('⑲之八')), True)))
    except Exception as e:
        R.append(('⛔渲染不起：%s' % e, False))
    finally:
        shutil.rmtree(d, ignore_errors=True)
    for 名, o in R:
        print(('  ✓ ' if o else '  ⛔ ') + 名)
    过 = sum(1 for _, o in R if o)
    print('  ── 负测·造章令 %d/%d %s ──' % (过, len(R), '全通' if 过 == len(R) else '⛔未过'))
    return 过 == len(R)


if __name__ == '__main__':
    sys.exit(0 if 跑() else 1)
