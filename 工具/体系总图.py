#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""体系总图——本仓一切之器、席、流、账，按心—脉—觉—长—学成一图：一件一行，其职、谁跑、何时跑、谁读其出、末真用、判。

立（1119·W909·法用#体系总图）：作者令「一定要有一个非常非常清晰明确的体系……体系分工……以最完美的方式去呈现」（常令:564）
  与「把所有我们要求的……和做出来的这些东西都执行和用起来」（常令:567）——用之审之果入图，未用、死者即红，随封版而验。
其法（零 token·只读、只并、只算：⛔改正文、⛔改账之判、⛔改他器）：
  件之集：工具/*.py、工具/席/*.js、.github/workflows/*.yml、设定/ 之账册（*.json 与非逐章之 *.md；逐章、逐段、逐事之档
    〔第N章、第N段、回执_*、裁_*〕与子目、版本/第N章/ 各只计其族一行）。
  部：以本器之部表定；名以「哨」终者归觉（W909「觉＝……诸哨」）；负测_X 随 X 之部；⛔猜：表外者入⓪「未归」。
  何职：器之 docstring 首句（去其名与括注；残者〔零 token、PreToolUse 钩、某日立〕补以 其律／其法、诸检之列、「本器……」之句、首行之引语）；
    席取 meta.description；流取首行之注；账取「说明」键、首行之引（本档由……生成）、逐条之录之目或首题。
  谁跑（静析·ast：⛔注、⛔docstring）：封版之 前()／後() 诸步与其所调之函；全测诸项之格与其 chk 函（并其所调之函）；
    workflows 非注之行；.claude/settings.json 之钩；githooks；.gitattributes 之 merge 驱；席之令与其派令；
    囤灰闸.真跑口（入口）与其所引之器；常驻之器（while 中 sleep·存底守）书「自驱·後台每 N 分」；载於有跑者者随之有跑。
    分书其类：调（列中、器()、subprocess）／「（载）」（import）／「（印令）」（只印其令：print、L.append、返之语——自走之处方、封毕之语）；
    流、git 钩、钩之令俱先去 echo／printf 之引文（「沙盒兜底 python3 工具/推.py --直」之示⛔算——跑、读俱然）；流之调唯取 python3 与 uses:；
    全测之格唯取调。全测只跑其「--自测」者标「唯自测」（⛔算本职之跑；同 囤灰闸._只自测 之义而以全名认之——彼以子串，
      负测_X 之行误作 X 之行：棘轮预检、自进化环、起草闸 三件异，⛔取其判；其治属 囤灰闸）。
  封版之序：後() 之全序（前置、步、闸〔条件、左移之拦、格、并起〕、其後〔席记、活态、--演 止、提交〕、存、收）与其所载、所印。
  谁读其出（静析）：import、from…import、spec_from_file_location、import_module、档名之串——读者：诸器、席、流、钩、总章、
    README、总圣经、canon；⛔注、⛔自引、⛔本器（其表载诸件之名）。账之读照 囤灰闸.档之囤灰（一义一判·坑36）：「名或六字以上之干」之引、
    其活档之 glob 之族（囤灰闸._glob前缀：剧情庭_、方法升级_、硬条_……·书「（族）」）；顶层 md 之「无引」再以 档之囤灰（日＝0）核之——
    彼认有引而本器寻不着其读者者书「活档」，本器有读而彼认无引者⓪ 书其异（⛔静默）。
  末真用：末十章 版本/第N章/_器之迹.md 之末见之章（其 jsonl 係 gitignored，⛔用）；无迹者书其由——迹盲（其跑俱在 GitHub、封版闸後、
    被载：迹之所不录）、窗外末见第N章（诸章之迹）、全迹无。
  判：W908「用之审之果」之名单照其判（⛔另立义）——名单唯一份：设定/方案/W908.md 该节之机读之块（```json 用之审：原、件、判、由、环、治），
    本器读之、⛔抄於码；块之「原」与该节上文之列逐判比之，异即析崩（复审改判而块不随即红）。名单外者机判——有跑且有读＝用、
    有一缺＝半用、俱无＝未用（判之由书於行）；名单判死／未用而仍有本职之跑者书「悖」，判半用而今迹见、机判用者书「候复审」（⛔改其判）；
    名单判死／未用、其治＝接入而今机判用者书「治已行——候复审」只 ⚠（治已行，⛔冻於原判而红）。
  用之审之红（器红级）：未用、死者逐件列——入 W908 治单而未逾限者 ⚠「随 W908 环N·限 L（限之源）」：限取 法用册，废之条（去证列其档）先之；
    无则甲批之环（W908「分批」之行）取 待「用之审」之限，乙批之环无专限只 ⚠（⛔借 用之审 之限：乙批俟 W907 入主，限早於其期）；
    器之机判未用、名单之死而无治、甲批之治而无限、逾限者 ⛔；账之机判未用只 ⚠（候审：同 囤灰闸.档之囤灰「只报」之义，⛔一义两判）。
  析崩即红（--验 rc 1）：诸源析不得（器之码坏、封版／全测缺或析崩、囤灰闸 载不得〔含 SystemExit〕、正文之末章不得〔0〕、名单之块缺坏或与上文异）
    俱入 源['崩']，⓪ 书之、余照出（⛔崩·⛔静默：末章静为 0 则诸限俱遮）。
  GitHub 之卡（报/卡.json·W908 环5）：只录於「☁」之行（随 备份/报 而变，--验 ⛔比）；无卡即书「卡未立」。
⛔本器之文⛔书诸件之全名（器带 .py、账带 .md 或六字以上之干）：囤灰闸之闭包、候退、档之囤灰俱以「名在活档」为引——
  器自己的文字亦在其所量之盘（囤灰闸 自测⑦之二之教）；故表中器只书其干、长档名以「+」断之，载时复之。
写者：设定/体系总图.md 由 封版 --後 与总编辑之治（--随治）重写；两写之并由 账并 之生成之图一支（两侧俱改即取 ours、⚠ 待下回重生·坑63 之冲突即去）；
  方法一变图即随（W912 环2）：总编辑之坐之治改器、席、流、法用册而图旧 → 推.py 图之闸 rc 3 ⛔交（写书之坐⛔拦）；人手欲看即 --印（只印、⛔写）。
  ⛔依 git 全史（浅克隆亦能生）。
〔W912·1120 作者令「全图也要随之更新」「执行主义……都去执行起来」「只要执行起来……它不会发亮吗？它或者变绿」〕：
  ⑥ 机制之流：mermaid（GitHub 即绘）＋文本之链——节＝平台之件（作者、总编辑之坐、写书之坐、【派】、治／章之枝、主枝、备份/报、巡印、巡应、哨 PR、
    兜底之令、钟之令〔在方立〕）与诸器；边：流之触与 job（.github/workflows/*.yml 之 on 与 job 之 if·uses）、接棒守 之表（兜底之令、钟之令、
    巡警枝、总编辑：ast 取其字面·⛔另抄）机取而注其源；余照 流之边 之表（甲, 乙, 语, 源档, 须含之串）逐边验其串在其档——失据即 ⓪ 报、书虚线（⛔崩）。
  ⑦ 近之进化：工作流账「件」W9xx 之裁之末八（件、名、裁、时、所废／较旧之摘 ≤80 字）。
  活之色：每件、每流之节带灯——🟢 当跑而已跑（末跑 ≤ 期×1.5）｜🟡 迟（≤ 期×3）｜🔴 当跑而未跑（逾期×3）或末跑败｜⚪ 按需、账、或迹不可取（⛔猜）。
    期：何时跑之机判（期之：常驻每 N 分、cron、每章〔近十章之均隔·取自 HEAD 与 origin/<主枝> 之「封版#N」之提交之时〕、每十章）；末跑：迹之源
    （_迹表：备份/巡印、巡应、心跳、存底〔按改·⛔作末跑〕、报/推〔autopush 之果；推取 治-* 之报、推报取报在〕、报/演、报/卡、章之封、图之重画；
    余取 _器之迹〔树无而主枝有之章 git show 取之〕、封版所跑、gate 之全测〔唯「全测·X」所跑而无真路之件·其格⛔在报之「免」·在「红」即败〕、
    流所调〔只承其时〕；载於有迹之器者随之一层）。共迹⛔借：诸 job 共写一枝（巡印）唯最密者认之、兜底之令借巡应 → ⚪「迹不可取」。
    末报「败·因 merge」书「合入之卡」。暂停中随写书与兜底之期 ⚪「暂停中」（GitHub 之 cron 照判），解停之後首期自解停起算。
    灯随时、随 origin/* 而变——--验 ⛔比（_比之文 去其符、一眼之红名之尾与 class 之行）；--摘、--件、--印、--随治 先取其旧之迹枝（限八秒·败即注「本地未取」），
    写（封版 --後）与 --验 ⛔取；ZM_TU_NOFETCH=1 即⛔取。本地之引或旧（⛔取之巡印／巡应／巡钟、取败）而逾期 → ⚪「迹未取」（⛔作当跑而未跑）。
  执行之查以图为据：--摘（今树即算·≤25 行）由 接棒守 --巡（总编辑之沙盒）於补印之後印之；法用之守 --报 末行书 图·用之红、⚠、🔴。
用法：
  python3 工具/体系总图.py            # 重生 设定/体系总图.md（rc 0）——封版 --後 之步
  python3 工具/体系总图.py --随治     # 总编辑之治：方法一变图即随（唯总编辑之坐·他坐 rc 2）——并交其图（推.py 图之闸）
  python3 工具/体系总图.py --印       # 印到屏、⛔写（人手之看）
  python3 工具/体系总图.py --摘       # 执行之查之据：今树即算·一眼之数、⛔即红、🔴🟡 之件与其由、⚠、半用／未用、图档旧否（≤25 行）
  python3 工具/体系总图.py --验       # 再算与档比（灯与 ☁ ⛔比）：旧只 ⚠ rc 0｜用之红 ⛔ rc 1｜析崩 ⛔ rc 1｜流之边失据 ⚠
  python3 工具/体系总图.py --件 名    # 一件之全（名：存底守、法用册.json、设定/段案/……）
  python3 工具/体系总图.py --自测     # 小样之料钉诸析，印「体系总图·自测 N/N」
"""
import os as _o, sys as _s
_s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
try:
    import _账  # 跑账·自记（工具/跑账.py）
except Exception:
    pass
import os, sys, re, ast, json, glob, time, shutil, tempfile, subprocess, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
图名 = os.path.join('设定', '体系总图.md')
本器 = '体系总图' + '.py'
迹窗 = 10                      # 末真用：末十章之迹
列限 = 4                       # 谁跑、谁读各至多列四，余书「等 N」
职限 = 60                      # 何职：至多六十字
云记 = '☁'                     # 随 备份/报 而变之行：--验 ⛔比
首行 = ('> 本档由 `工具/体系总图.py` 生成（零 token·随 封版 --後 与总编辑之 --随治），⛔手改；改其表即改其器之码或其源档。'
      '判之义照 W908「用之审之果」（用／半用／未用／死）；名单外者机判：有跑且有读＝用、有一缺＝半用、俱无＝未用。每行带其源档。')
他读之档 = (('README', 'README.md'), ('总圣经', os.path.join('设定', '00_镇冢秘术_唯一总圣经.md')),
          ('canon', os.path.join('设定', 'canon事实库.json')))   # 席所读之总档（同 囤灰闸.档之囤灰 之「他」）

# ═══ 五部（W909 方案「五部之脊」）═══
部序 = ('心', '脉', '觉', '长', '学')
部之职 = {
    '心': '作家：造章诸席与其器——起草、记、审、守书之质、书之记忆与设定',
    '脉': '丝滑：推、闸、并、存底——章之封、推、GitHub 之闸与并、存底与锁（存底守名「守」而行存底，归此；验之者在觉）',
    '觉': '守：巡、云巡、执行之守（诸钩）、诸哨（名以「哨」终者俱归此）——察停、察违、察费、察书之漂、守会话',
    '长': '进化：坑账、方法账、进化树、复盘、法用之守——方法之进与用之审',
    '学': '学：写书之道、大师进化账、拍库、起草令——写书之技之积',
}
# 部之归属之表（⛔猜：表外者入⓪「未归」）。器只书其干；负测_X 随 X 之部，X 不在表者查 负测之部（其所守之器之部）。
# 诸哨不入表：W909 方案「觉＝守：巡、云巡、执行之守、诸哨」——名以「哨」终之器（与其负测）俱归觉，⛔散入心、长（用之证环3 之治）。
_器部 = {
    '心': '''FS闸 两册对限 书名不绑 书级体检 亮点在 亮点对表 亮点界 人物链 人账 全书记忆 净重对表 净重趋 分量闸 刻意之疲
            席令之禁 剧情庭之关 剧情链 合玉闸 同步全本阅读器 含拍 器物点名 回执对账 圣经引号 圣经随裁
            外事尺 外声闸 大审 大问表 字数闸 对账预筛 小说检察官 尺之校 崩坏闸 席法 开轮六检 息日链 感官趋 承 抄袭闸
            换型令 接口验 改单 改记 数闸 无闸之卡 棘轮预检 欠账闸 段料 段案验 比带 法典闸
            漂移全书 爆窗 版档指纹 看官 硬闸 稿差 章料 第零轮开镜庭 约到期 自走
            记料 记落 质量三闸 起草闸 跑轮 还账 造式 造式验 邻拍重出 重出趋 D1施 行号随移 剧情全图''',
    '脉': '全测 全测并 存底 存底包 存底守 封版 心跳 推 推报 账并 续跑 重取',
    '觉': '会话之守 席在跑吗 接力 接棒守 推闸中 暂停令 段序之守 续跑之守 自决之守 链之检 工作流账',   # 诸哨不列：名以「哨」终者俱归觉（部之）
    '长': '坑账 方法坑账 进化树 进化链 复盘 法用之守 自进化环 囤灰闸 跑账 总编辑复核 裁之生效 方案 费审 费审对拍 机械账 体系总图 _账',
    '学': '大师之关',
}
负测之部 = {
    '心': '''FS裁过 FS闸付语与期 canon禁式之界 三尺同量 上瘾四问 亮点残引 人账之还 入出同拍之镜 公开量表格 净重一处 净重取形
            分量闸之读 分量闸取正文 到期账词表 叠词闸 向之口 吞记闸 回执三名 在场之兑 场景切换闸 外声三式 大审挂限 大审收方
            大审空模子 大问挂账 孤版闸 开镜卡带三条 承前闸 换型令之尺 摆问之嵌 数句闸 日词闸 未答闸 末行之判 本章之失两式
            棘轮v01 横评重开 段间空行闸 版档指纹当场对档 甲层之读 真轮凭轮记 窗界之换行 章型带 章型连锁 薄章之禁 行号引真
            补存说明 说明闸 账键一名 趋阈闸 连读重出 造章令 逾期之账同硬 重出趋长串 D1施改单''',
    '脉': '全测崩绿 推闸 钩路 封版之凭 封版留旗',
}
# 席、流、账：.js／.yml／.json 书全名；md 书其干（⛔.md），六字以上之干以「+」断之；族与子目书其族名
_他部 = {
    '心': '''造章.js 大审.js 剧情庭.js
            canon事实库.json 人物状态册.json 到期账.json 改单账.json 法典.json 版档指纹_裁.json 看官凭据.json 看官账.json
            节奏方差回补_优先序.json 还账账.json 抄袭回修账.json 书级基线.json 抄袭回修账
            00_镇冢秘术+_唯一总圣经 01_镇冢秘术+_逐章施工与伏笔回收表 02_余章之势+_总纲 02_全书之约+_逐站事数表 03+_人物新册
            99_镇冢秘术+_废案墓地 九鼎图鉴 二稿账 人物挂账 人物百科卡+_四主 修改清单 分量欠账 分量趋账 剧情不+合理区
            剧情庭_D10+_师兄师弟 剧情庭_D11+_终局全弧 剧情庭_D1+_老头之年 剧情庭_D3+_真拦之敌 剧情庭_D4+_玄微走九站 剧情庭_D6+_床上那人 剧情庭+_余章总案
            合玉闸账 外声账 大升级+_必修清单 大升级+_总案 大升级+_章号对照 大升级之律 大审+_347之备 大问挂账
            审计_20260717+_伏笔账本18条 审计_20260722_硬伤案例台账+_73至76 崩坏回修账 开站三数+_E4巴蜀水下 开站三数+_E6公输
            开镜卡+_用法 旧账+_东头之疤左右相犯 气鼎之律 爆窗账 硬条_345+_暗线日课之破 硬条_346+_主线日课之破 窗界账
            立得住普查+_0927 站账_E5贺兰+_对站 镇冢秘术_2026-07-13+_五项争议终局裁定 镇冢秘术+_作者版设定圣经
            镇冢秘术_全书逻辑终极闭环录+_50轮挑刺版 交付三检提示词+_逐字存档 无闸之卡账 人物之审+_至第388章
            回修案_第340章_20260917+_救章席三笔
            回执_*.md 裁_*.md 大审_至第N章.md 剧情庭_势_第N段.md 设定/段案/ 设定/全书记忆/ 设定/全书病册/ 设定/剧情庭题/
            设定/大升级通读/ 版本/第N章/''',
    '脉': 'autopush.yml gate.yml 演练.yml 写者册.json 全测均秒.json 演练账.json',
    '觉': '巡.yml 暂停令.json 工作流账.json 00_作者常令+_不停之律 执行之制 交接_续跑',
    '长': '''方法坑账.json 法用册.json 总编辑复核账.json 书之进化_棘轮.json 自进化环_挂账.json 裁之生效_棘轮.json 进化链_棘轮.json
            费账.json 价目.json 00+_自进化机制总纲 书之进化账 囤灰挂账 待验账 方法账 方法升级+_机械之活 方法升级+_造式二代
            机制体检账 瑕疵总账 病族账 虫洞法典 进化树 进化链 造之回报审+_1014 教训_D6+_方法之僵 体系总图
            设定/方案/ 设定/复盘/ 设定/_草/ 版本/第N章/_器之迹.md''',
    '学': '反面教材 叫绝之拍库 大师画像 大师进化账 执笔病历本+_模式性错误档案 立得住之律 起草令+_每章必发 选剧情之律 写书之道',
}


def _展(x):
    """表之名 → 件名：去「+」；无扩展名、非子目者补 .md。"""
    x = x.replace('+', '')
    return x if x.endswith(('.json', '.js', '.yml', '.md', '/')) else x + '.md'


# ═══ W908「用之审之果」之名单：唯一份在 设定/方案/W908.md 该节之机读之块（```json 用之审）——本器读之，⛔抄於码 ═══
#   块之一行：原（上文之名）、件（盘上之档）、判、由、环（「逐环」所治之环·null＝无治）、治（废／接入／正·null）。
#   其限⛔书死於此：判时取 法用册——废之条（去证列此档）之「限」先之；无则甲批之环取 待「用之审」之限、乙批之环只 ⚠（见 _治之）。
W908名 = os.path.join('设定', '方案', 'W908.md')
_判之名 = {'半用': '半用', '未用': '未用', '死': '死', '用而有疵': '用'}


def _去括(x):
    for _ in range(3):
        x = re.sub(r'（[^（）]*）|\([^()]*\)', '', x)
    return x


def _名单之文(节):
    """「## 用之审之果」之上文（机读之块之前）→ {(类, 判): {原}}：器之列（「**半用 15**：」下一名一行）、账册页之列（「**死 6**：甲、乙……」）。"""
    出 = {}
    器节 = 节.split('- **器**', 1)[1].split('- **账册页**', 1)[0] if '- **器**' in 节 else ''
    账节 = 节.split('- **账册页**', 1)[1].split('\n- **', 1)[0] if '- **账册页**' in 节 else ''
    判 = None
    for l in 器节.split('\n'):
        m = re.match(r'\s*- \*\*([^*]+?)\*\*', l)
        if m:                                        # 一题一判；非判之题（「复核驳去五判」）⛔承前判
            判 = _判之名.get(re.sub(r'\s*\d+$', '', m.group(1).strip()))
            continue
        m = re.match(r'\s{4,}- (.+)', l)
        if m and 判:
            出.setdefault(('器', 判), set()).add(re.split(r'[（(：:，]', m.group(1))[0].strip())
    for m in re.finditer(r'\*\*([^*\d]+?)\s*\d+\*\*[：:]([^\n]+)', 账节):
        判 = _判之名.get(m.group(1).strip())
        if 判:
            出[('账', 判)] = {x.strip(' 。.') for x in _去括(m.group(2)).split('、') if x.strip(' 。.')}
    return 出


def _件之名(p):
    """块之件（'工具/X.py'、'设定/X.json'、'版本/第N章/_器之迹.md'）→ 本图之件名（顶层之器、账书其名；族照书）。"""
    d, b = os.path.split(p)
    return b if d in ('工具', '设定') else p


def 读W908(根):
    """→ {'表': {件名: (判, 由, 环, 治, 原)}, '批': {环: 甲／乙}, '数': (器, 账), '误': [..], '在': 档在否}。
    块缺、JSON 坏、「原」与上文之列异、批之行不得 → 误（读源 入 源['崩']：析崩即红）；档缺 → 在 False（入 源['缺']）。"""
    出 = {'表': {}, '批': {}, '数': (0, 0), '误': [], '在': False}
    文 = _读(os.path.join(根, W908名))
    if 文 is None:
        return 出
    出['在'] = True
    节 = 文.split('\n## 用之审之果', 1)[1].split('\n## ', 1)[0] if '\n## 用之审之果' in 文 else ''
    m = re.search(r'```json 用之审\n(.*?)\n```', 节, re.S)
    if not m:
        出['误'].append('无机读之块（「## 用之审之果」中 ```json 用之审）')
        return 出
    try:
        块 = json.loads(m.group(1))
        行们 = [('器', x) for x in 块.get('器') or []] + [('账', x) for x in 块.get('账') or []]
        比 = {}
        for 类, x in 行们:
            比.setdefault((类, x['判']), set()).add(x['原'])
            for p in x.get('件') or []:
                出['表'][_件之名(p)] = (x['判'], x.get('由') or '', x.get('环'), x.get('治'), x['原'])
        出['数'] = (len(块.get('器') or []), len(块.get('账') or []))
    except (ValueError, KeyError, TypeError, AttributeError) as e:
        出['误'].append('机读之块坏（%s）' % str(e)[:60])
        return 出
    上 = _名单之文(节.split('### 机读之块')[0])
    for k in sorted(set(上) | set(比)):
        多, 少 = sorted(比.get(k, set()) - 上.get(k, set())), sorted(上.get(k, set()) - 比.get(k, set()))
        if 多 or 少:
            出['误'].append('块与上文异·%s %s：%s%s' % (k[0], k[1], ('块多 ' + '、'.join(多)) if 多 else '', ('；块少 ' + '、'.join(少)) if 少 else ''))
    for 批 in ('甲', '乙'):                          # 「分批」之行：- 甲批（…）：环1、环2……——
        mm = re.search(r'(?m)^- %s批[^：\n]*：([^\n]*)' % 批, 文)
        if mm:
            for n in re.findall(r'环(\d+)', mm.group(1).split('——')[0]):
                出['批'].setdefault('环' + n, 批)
    if not 出['批']:
        出['误'].append('「分批」之行不得（- 甲批……：环N、……）')
    return 出


def _部表():
    出 = {}
    for 部, 文 in _器部.items():
        出.update({x + '.py': 部 for x in 文.split()})
    for 部, 文 in _他部.items():
        出.update({_展(x): 部 for x in 文.split()})
    for 部, 文 in 负测之部.items():
        for x in 文.split():
            出.setdefault('负测_' + x + '.py', 部)
    return 出


def 部之(件名, 表=None):
    """件名 → 部（⛔猜：表外者 None·入「未归」）；名以「哨」终之器归觉（W909「觉＝……诸哨」）；负测_X.py 随 X.py 之部。"""
    表 = 表 if 表 is not None else _部表()
    本 = lambda x: 表.get(x) or ('觉' if x.endswith('哨.py') else None)
    if 件名 in 表:
        return 表[件名]
    m = re.match(r'负测_(.+\.py)$', 件名)
    return 本(m.group(1)) if m else 本(件名)


# 账册之族（逐事之档）与子目
_族 = (('回执_*.md', r'^回执_', r'(?<![\w])回执_', '诸席之回执（逐章、逐事）'),
      ('裁_*.md', r'^裁_', r'(?<![\w])裁_', '总编辑之裁（逐事）'))
_子目之职 = {'段案': '每十章之段案（骨）', '全书记忆': '全书记忆（剧情链、人物链、详记）', '全书病册': '全书之病册',
          '剧情庭题': '剧情庭之题', '大升级通读': '大升级之通读', '方案': '诸 W 之方案', '复盘': '诸任务之复盘', '_草': '诸席之草'}
# 何时跑之语
_钩之时 = {'Stop': '每回合之末', 'SessionStart': '会话之起', 'PreToolUse': '每调 %s 之前'}
_口之时 = {'自走': '自走每跑（主环）', '接棒守': '巡、候主（接棒守）', '大审': '每十章（大审之包）', '起草闸': '每章起草',
          '书级体检': '随书级体检', '跑轮': '存版（跑轮）'}
_席之时 = {'造章': '每章（造章之席）', '大审': '每十章（大审之席）', '剧情庭': '每段、改剧情前（剧情庭之席）'}


# ═══ 析 ═══
def _读(p):
    try:
        with open(p, encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception:
        return None


_名式 = re.compile(r'(?<![\w\-.])([\w\-]+\.(?:py|js|yml|json|md))(?![\w])')


def 名们(文):
    """文中之档名（X.py／X.js／X.yml／X.json／X.md）之集——⛔取他名之尾（负测_硬闸.py ⛔认作 硬闸.py）。"""
    return set(_名式.findall(文 or ''))


_定义 = (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)


def _文首(n):
    """定义之节点之 docstring 之常量节点（无即 None）。"""
    b = n.body[0] if getattr(n, 'body', None) else None
    if isinstance(b, ast.Expr) and isinstance(b.value, ast.Constant) and isinstance(b.value.value, str):
        return b.value
    return None


def _载之名(n):
    """一节点所载之模 → [干]：import、from…import、import_module、__import__、spec_from_file_location（其路之串）。"""
    if isinstance(n, ast.Import):
        return [a.name.split('.')[0] for a in n.names]
    if isinstance(n, ast.ImportFrom):
        return [n.module.split('.')[0]] if n.module and not n.level else []
    f = n.func
    fn = f.attr if isinstance(f, ast.Attribute) else f.id if isinstance(f, ast.Name) else ''
    if fn in ('import_module', '__import__') and n.args and isinstance(n.args[0], ast.Constant) and isinstance(n.args[0].value, str):
        return [n.args[0].value.split('.')[0]]
    if fn == 'spec_from_file_location':
        for a in n.args[1:] + [k.value for k in n.keywords]:
            for c in ast.walk(a):
                if isinstance(c, ast.Constant) and isinstance(c.value, str) and c.value.endswith('.py'):
                    return [os.path.basename(c.value)[:-3]]
    return []


_调函 = frozenset(('器', 'run', '跑', 'Popen', 'call', 'check_call', 'check_output', 'spec_from_file_location', 'join',
                  '_自测之项', 'exec_module', 'module_from_spec'))
_裸 = re.compile(r'[\w\-./]+')


def _函名(f):
    return f.attr if isinstance(f, ast.Attribute) else f.id if isinstance(f, ast.Name) else ''


def _节之析(节, 文档):
    """一节点 → (串〔(行, 列, 文)〕, 载, 所调之名, 印位〔(行, 列)〕)；所遇定义之 docstring 入 文档 而⛔计。
    印（只印之文，非调）：print() 中之串；或不在列、集、调函之中而非裸名之串（返之语、L.append 之令）——
      自走「只印一行命令」、封版之封毕之语，其器为「印令」（主环照跑之处方），与 调（列中、器()、subprocess）分书。"""
    串, 载, 调, 印位 = [], set(), set(), set()
    栈 = [(节, '')]
    while 栈:
        n, 境 = 栈.pop()
        子 = 境
        if isinstance(n, _定义):
            d = _文首(n)
            if d is not None:
                文档.add(id(d))
        elif isinstance(n, ast.Constant):
            if isinstance(n.value, str) and id(n) not in 文档:
                串.append((n.lineno, n.col_offset, n.value))
                if 境 == '印' or (境 != '调' and not _裸.fullmatch(n.value)):
                    印位.add((n.lineno, n.col_offset))
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            载.update(_载之名(n))
        elif isinstance(n, ast.Call):
            载.update(_载之名(n))
            if isinstance(n.func, ast.Name):
                调.add(n.func.id)
            fn = _函名(n.func)
            子 = '印' if fn == 'print' else ('调' if 境 != '印' and fn in _调函 else 境)
        elif isinstance(n, (ast.List, ast.Set)) and 境 != '印':
            子 = '调'
        栈.extend((c, 子) for c in ast.iter_child_nodes(n))
    return 串, 载, 调, 印位


def _序串(串):
    return [x for _, _, x in sorted(串, key=lambda t: (t[0], t[1]))]


def _分串(串, 印位):
    """→ (全串, 印串, 调串)（源序）。"""
    序 = sorted(串, key=lambda t: (t[0], t[1]))
    return [x for _, _, x in 序], [x for a, b, x in 序 if (a, b) in 印位], [x for a, b, x in 序 if (a, b) not in 印位]


def _常(n, 赋, 深=0):
    """常量之式（5 * 60、间）→ 数；不得即 None。"""
    if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
        return n.value
    if isinstance(n, ast.Name) and n.id in 赋 and 深 < 3:
        return _常(赋[n.id].value, 赋, 深 + 1)
    if isinstance(n, ast.BinOp):
        a, b = _常(n.left, 赋, 深), _常(n.right, 赋, 深)
        if a is not None and b is not None:
            return {ast.Mult: lambda: a * b, ast.Add: lambda: a + b, ast.Sub: lambda: a - b,
                    ast.FloorDiv: lambda: a // b if b else None}.get(type(n.op), lambda: None)()
    return None


def _驱(树, 赋):
    """常驻之器（while 中 sleep 一分以上）→ 其隔之秒；无即 None（存底守：钩起之，後台每五分自驱）。"""
    for w in ast.walk(树):
        if isinstance(w, ast.While):
            for c in ast.walk(w):
                if isinstance(c, ast.Call) and _函名(c.func) == 'sleep' and c.args:
                    v = _常(c.args[0], 赋)
                    if v and v >= 60:
                        return v
    return None


def 析py(文):
    """→ {'函': {名: (串, 载, 调, 印串, 调串)}, '全': 同, '赋': {名: 节点}, '树', 'doc', '驱'}；析不得 → None。每节点只走一遍。"""
    try:
        树 = ast.parse(文 or '')
    except (SyntaxError, ValueError):
        return None
    文档 = {id(_文首(树))} if _文首(树) is not None else set()
    函, 赋, 全串, 全载, 全调, 全印 = {}, {}, [], set(), set(), set()
    for n in 树.body:
        s, l, c, 印 = _节之析(n, 文档)
        全串 += s
        全载 |= l
        全调 |= c
        全印 |= 印
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            a, b, d = _分串(s, 印)
            函[n.name] = (a, l, c, b, d)
        elif isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    赋[t.id] = n
    a, b, d = _分串(全串, 全印)
    return {'函': 函, '全': (a, 全载, 全调, b, d), '赋': 赋, '树': 树, 'doc': ast.get_docstring(树) or '', '驱': _驱(树, 赋)}


def 函之闭包(析, 根们):
    """自根函起随其所调之顶层函（递）→ (串, 载, 印串, 调串)。"""
    串, 载, 印, 调串, 见, 待 = [], set(), [], [], set(), [x for x in 根们 if x in 析['函']]
    while 待:
        f = 待.pop(0)
        if f in 见:
            continue
        见.add(f)
        s, l, c, b, d = 析['函'][f]
        串 += s
        载 |= l
        印 += b
        调串 += d
        待 += sorted(x for x in c if x in 析['函'] and x not in 见)
    return 串, 载, 印, 调串


def _器名(串, 除=()):
    return set(x for s in 串 for x in 名们(s) if x.endswith('.py')) - set(除)


def _步之序(析, 函名):
    """函中 (名, …'X.py'…) 之组 → [(步名, X.py)]（源序）——封版之步、闸、存之列。"""
    出 = []
    for n in 析['树'].body:
        if isinstance(n, ast.FunctionDef) and n.name == 函名:
            for t in ast.walk(n):
                if isinstance(t, ast.Tuple) and t.elts and isinstance(t.elts[0], ast.Constant) and isinstance(t.elts[0].value, str):
                    py = [c.value for e in t.elts[1:] for c in ast.walk(e)
                          if isinstance(c, ast.Constant) and isinstance(c.value, str) and c.value.endswith('.py')]
                    if py:
                        出.append((t.lineno, t.col_offset, t.elts[0].value, os.path.basename(py[0])))
    return [(a, b) for _, _, a, b in sorted(出)]


def _序名(析, 函名, 除=()):
    """函之自身之串中之器名（源序·去重）。"""
    if 函名 not in 析['函']:
        return []
    return list(dict.fromkeys(x for t in 析['函'][函名][0] for x in sorted(名们(t)) if x.endswith('.py') and x not in 除))


def _元串(析, 名):
    """模之赋 名 = (…) → 其中之串（读者之快、读者之慢、活态之格、左移之拦）。"""
    n = 析['赋'].get(名)
    return [c.value for c in ast.walk(n.value) if isinstance(c, ast.Constant) and isinstance(c.value, str)] if n else []


def _条件(t, 析):
    """If 之测 → 短语：n >= 分栏之始 → N≥411；含 X.md／X.json 之串 → 有 X.md；余 None。"""
    if isinstance(t, ast.Compare) and isinstance(t.left, ast.Name) and t.left.id == 'n' and len(t.ops) == 1:
        v = _常(t.comparators[0], 析['赋'])
        op = {ast.GtE: '≥', ast.Gt: '＞', ast.LtE: '≤', ast.Lt: '＜', ast.Eq: '＝'}.get(type(t.ops[0]))
        if v is not None and op:
            return 'N%s%d' % (op, v)
    for c in ast.walk(t):
        if isinstance(c, ast.Constant) and isinstance(c.value, str) and re.search(r'\.(md|json)$', c.value):
            return '有 ' + c.value
    return None


def _返(体, 值):
    return any(isinstance(x, ast.Return) and isinstance(x.value, ast.Constant) and x.value.value is 值 for x in 体)


def _语序(体, 析, 若=None):
    """函体之语（源序·摊平 If、For、With、Try）→ [(语, 若, 路)]：路＝'败'（支末 return False：印误而返）、
    '止'（支末 return True：如 --演 之早毕，只记其支一条）、''。"""
    出 = []
    for st in 体:
        if isinstance(st, ast.If):
            if _返(st.body, True):
                出.append((st, 若, '止'))
            else:
                路 = '败' if _返(st.body, False) else ''
                出 += [(n, 若 or _条件(st.test, 析) or c, 路 or r) for n, c, r in _语序(st.body, 析)]
            出 += _语序(st.orelse, 析, 若)
        elif isinstance(st, (ast.For, ast.While, ast.With, ast.Try)):
            出.append((st, 若, ''))
        else:
            出.append((st, 若, ''))
    return 出


def _格之(t, 析):
    """一组之中 ','.join(模之元) → 其元之串（读者之快 → 改单、圣经引号……）。"""
    return [x for c in ast.walk(t) if isinstance(c, ast.Call) and _函名(c.func) == 'join' and c.args
            and isinstance(c.args[0], ast.Name) for x in _元串(析, c.args[0].id)]


def _步们(析, 函名, 拦=()):
    """函中之步之组 ('名', [器('X.py'), …], 必?) 与 左移之拦 之插处 → [{名, 器, 若, 必, 格}]（源序；若＝其 If 之条件）。"""
    节 = next((n for n in 析['树'].body if isinstance(n, ast.FunctionDef) and n.name == 函名), None)
    if 节 is None:
        return []
    候 = []
    for st, 若, 路 in _语序(节.body, 析):
        if 路 == '败':
            continue
        for t in ast.walk(st):
            if isinstance(t, ast.Tuple) and t.elts and isinstance(t.elts[0], ast.Constant) and isinstance(t.elts[0].value, str):
                py = [c.value for e in t.elts[1:] for c in ast.walk(e)
                      if isinstance(c, ast.Constant) and isinstance(c.value, str) and c.value.endswith('.py')]
                if py:
                    必 = t.elts[-1].value if isinstance(t.elts[-1], ast.Constant) and isinstance(t.elts[-1].value, bool) else None
                    候.append((t.lineno, t.col_offset, 0, {'名': t.elts[0].value, '器': os.path.basename(py[0]), '若': 若, '必': 必,
                                                         '格': _格之(t, 析)}))
            elif isinstance(t, ast.Name) and t.id == '左移之拦' and isinstance(t.ctx, ast.Load):
                for k, (a, b) in enumerate(拦):
                    候.append((t.lineno, t.col_offset, k, {'名': a, '器': b, '若': 若, '必': None, '格': []}))
    出, 见 = [], set()
    for a, b, k, x in sorted(候, key=lambda z: z[:3]):
        if (a, b, k) not in 见:
            见.add((a, b, k))
            出.append(x)
    return 出


_序外之函 = frozenset(('跑', '器', '并起', '红行', '可提交', '正文档', '後'))


def _後之全序(析, 拦=()):
    """後() 之全序（源序）→ [(组, 文)]：组＝前置、步、闸、其後、存、收；⛔＝红即停、⚠＝只报。
    步取其组（必＝True 者 ⛔）；後之闸、後之存 展其步（循其步之 for 内有 return False 者 ⛔，无者 ⚠）；他函书其名与其所调、所载、所印之器。"""
    节 = next((n for n in 析['树'].body if isinstance(n, ast.FunctionDef) and n.name == '後'), None)
    if 节 is None:
        return []
    并 = set(_元串(析, '後之并'))
    变函, 停名 = {}, set()                                  # 变→其所取之函；循之而败即返者
    for n in ast.walk(节):
        if isinstance(n, ast.Assign) and isinstance(n.value, (ast.Call, ast.Tuple)):
            诸值 = n.value.elts if isinstance(n.value, ast.Tuple) else [n.value]
            诸标 = n.targets[0].elts if isinstance(n.targets[0], ast.Tuple) else n.targets
            for 标, 值 in zip(诸标, 诸值):
                if isinstance(标, ast.Name) and isinstance(值, ast.Call):
                    变函[标.id] = _函名(值.func)
        if isinstance(n, ast.For) and any(isinstance(x, ast.Return) and isinstance(x.value, ast.Constant) and x.value.value is False
                                          for b in n.body for x in ast.walk(b)):
            for c in ast.walk(n.iter):
                if isinstance(c, ast.Name):
                    停名.add(变函.get(c.id, c.id))
                    停名.add(c.id)
    语 = _语序(节.body, 析)
    席变 = set()                                         # 席记之变：自含 '_席记.json' 之式而来者（p → j）
    for n in sorted((n for n in ast.walk(节) if isinstance(n, ast.Assign)), key=lambda z: (z.lineno, z.col_offset)):
        if any(isinstance(c, ast.Constant) and c.value == '_席记.json' or isinstance(c, ast.Name) and c.id in 席变
               for c in ast.walk(n.value)):
            席变 |= {z.id for z in n.targets if isinstance(z, ast.Name)}

    def 基(z):
        while isinstance(z, (ast.Subscript, ast.Attribute, ast.Call)):
            z = z.value if not isinstance(z, ast.Call) else z.func
        return z.id if isinstance(z, ast.Name) else None
    败测 = {c.id for st, _, 路 in 语 if 路 == '败' and isinstance(st, ast.If) for c in ast.walk(st.test) if isinstance(c, ast.Name)}
    败测 |= {c.id for st in ast.walk(节) if isinstance(st, ast.If) and _返(st.body, False) for c in ast.walk(st.test) if isinstance(c, ast.Name)}
    器干 = lambda x: x[:-3] if x.endswith('.py') else x

    def 步文(x, 组停=None):
        细 = [器干(x['器'])] if 器干(x['器']) != x['名'] or x['格'] else []
        if x['格']:
            细 = [细[0] + '；格：' + '、'.join(x['格'])] if 细 else ['格：' + '、'.join(x['格'])]
        return '%s%s%s%s' % (x['名'], ('（%s）' % 细[0]) if 细 else '', ('〔若 %s〕' % x['若']) if x['若'] else '',
                            ' ⛔' if x['必'] and 组停 is None else '')
    件们 = []
    for st, 若, 路 in 语:
        if 路 == '败':
            continue
        if 路 == '止':
            件们.append((st.lineno, st.col_offset, '其', '〔%s 至此止〕' % (('--' + st.test.id) if isinstance(st.test, ast.Name) else ast.unparse(st.test))))
            continue
        for t in ast.walk(st):
            if isinstance(t, ast.Tuple) and t.elts and isinstance(t.elts[0], ast.Constant) and isinstance(t.elts[0].value, str):
                py = [c.value for e in t.elts[1:] for c in ast.walk(e)
                      if isinstance(c, ast.Constant) and isinstance(c.value, str) and c.value.endswith('.py')]
                if py and not isinstance(st, ast.For):
                    必 = t.elts[-1].value if isinstance(t.elts[-1], ast.Constant) and isinstance(t.elts[-1].value, bool) else None
                    件们.append((t.lineno, t.col_offset, '步', 步文({'名': t.elts[0].value, '器': os.path.basename(py[0]), '若': 若,
                                                                '必': 必, '格': _格之(t, 析)})))
            elif isinstance(t, ast.Call) and isinstance(t.func, ast.Name) and t.func.id in 析['函'] and t.func.id not in _序外之函:
                f = t.func.id
                步们 = _步们(析, f, 拦)
                if 步们:                                   # 展其步：後之闸、後之存
                    停 = f in 停名
                    组 = '存' if not 停 else '闸'
                    文们 = []                               # 并起之步（後之并）书作「并〔甲、乙、丙〕」一节
                    for x in 步们:
                        if x['名'] in 并 and 文们 and isinstance(文们[-1], list):
                            文们[-1].append(步文(x, 停))
                        else:
                            文们.append([步文(x, 停)] if x['名'] in 并 else 步文(x, 停))
                    文们 = [('并〔%s〕' % '、'.join(y)) if isinstance(y, list) else y for y in 文们]
                    件们.append((t.lineno, t.col_offset, 组, (' ⛔' if 停 else ' ⚠') + '：' + '→'.join(文们)))
                    continue
                _, 载, 印, 调串 = 函之闭包(析, [f])
                调 = sorted(x[:-3] for x in _器名(调串, ('封版.py',)))
                模 = sorted(m for m in 载 if m != '封版' and (m + '.py') in 析.get('盘', ()) and m not in 调)
                印器 = sorted(x[:-3] for x in _器名(印, ('封版.py',)) if x[:-3] not in 调 and x[:-3] not in 模)
                格 = list(dict.fromkeys(_格之(next(n for n in 析['树'].body if isinstance(n, ast.FunctionDef) and n.name == f), 析)))
                细 = '；'.join(x for x in ('、'.join(调) + (('；格：' + '、'.join(格)) if 格 else '') if 调 else '',
                                         ('载 ' + '、'.join(模)) if 模 else '', ('印令 ' + '、'.join(印器)) if 印器 else '') if x)
                标 = ''
                for 父 in ast.walk(st):
                    if isinstance(父, ast.Assign) and 父.value is t and any(isinstance(z, ast.Name) and z.id in 败测 for z in 父.targets):
                        标 = ' ⛔'
                if isinstance(st, ast.Expr) and st.value is t and 调:
                    标 = ' ⚠'
                件们.append((t.lineno, t.col_offset, '函', f + 标 + (('（%s）' % 细) if 细 else '')))
            elif isinstance(t, ast.Call) and t.args and isinstance(t.args[0], ast.List):
                诸 = [e.value for e in t.args[0].elts if isinstance(e, ast.Constant) and isinstance(e.value, str)]
                if 诸[:1] == ['git'] and 'commit' in 诸:
                    件们.append((t.lineno, t.col_offset, '其', '提交'))
            elif isinstance(t, ast.Assign) and not isinstance(st, ast.For):
                for 标 in t.targets:
                    if isinstance(标, ast.Subscript) and isinstance(标.slice, ast.Constant) and isinstance(标.slice.value, str) \
                            and 基(标.value) in 席变:
                        件们.append((t.lineno, t.col_offset, '其', '席记「%s」段' % 标.slice.value))
    出, 组 = [], '前置'
    for _, _, 类, 文 in sorted(件们, key=lambda z: z[:2]):
        if 类 == '步':
            组 = '步'
        elif 类 in ('闸', '存'):
            组 = 类
            出.append((组 + 文[:2].strip(), 文[3:] if 文.startswith(' ') else 文))
            组 = '其後' if 类 == '闸' else '收'
            continue
        elif 组 == '步':
            组 = '其後'
        出.append((组, 文))
    合 = []
    for 组, 文 in 出:
        if 合 and 合[-1][0] == 组:
            合[-1] = (组, 合[-1][1] + '→' + 文)
        else:
            合.append((组, 文))
    return 合


def 析封版(文, 析=None, 盘=()):
    """封版 → {'前', '後'（调之器）, '印前', '印後'（印令之器）, '载前', '载後'（模）, '序', '快', '慢', '活'}；析不得 → None。
    调＝列中、器()、subprocess 之器；印令＝只印之语中之器（封毕之语之 接棒守 --候主）；载＝import（库：对账预筛、记落……）。"""
    析 = 析 or (析py(文) if 文 else None)
    if 析 is None or '前' not in 析['函'] or '後' not in 析['函']:
        return None
    析 = dict(析, 盘=set(盘))
    自 = ('封版.py',)
    _, 前载, 前印, 前调 = 函之闭包(析, ['前', '慢检并起'])
    _, 後载, 後印, 後调 = 函之闭包(析, ['後', '後之闸', '後之存', '活态之报'])
    後调 = 後调 + _元串(析, '左移之拦')
    拦 = []
    if '左移之拦' in 析['赋']:
        for c in ast.walk(析['赋']['左移之拦'].value):
            if isinstance(c, ast.Tuple) and len(c.elts) >= 2 and all(isinstance(e, ast.Constant) for e in c.elts[:2]):
                拦.append((c.elts[0].value, c.elts[1].value))
    前, 後 = _器名(前调, 自), _器名(後调, 自)
    return {'前': 前, '後': 後, '印前': _器名(前印, 自) - 前, '印後': _器名(後印, 自) - 後, '载前': 前载, '载後': 後载,
            '序': {'前': _序名(析, '前', 自), '前·并': _序名(析, '慢检并起', 自), '後·步': _步之序(析, '後'),
                   '後·闸': _步之序(析, '後之闸'), '後·拦': 拦, '後·存': _步之序(析, '後之存'), '後·全': _後之全序(析, 拦)},
            '快': _元串(析, '读者之快'), '慢': _元串(析, '读者之慢'), '活': _元串(析, '活态之格')}


def _唯自测(函节, 名):
    """chk 函中提 名 之列／组俱带「--自测」（或经 _自测之项 调）否。同 囤灰闸._只自测 之义；彼以子串认名（「负测_X.py」之行亦算 X 之行，
    棘轮预检、自进化环、起草闸 之本职遂误判），此以 名们（全名）认——⛔取其判，其治属 囤灰闸。"""
    见, 唯 = False, True
    for n in ast.walk(函节):
        if isinstance(n, (ast.List, ast.Tuple)):
            串 = [e.value for e in n.elts if isinstance(e, ast.Constant) and isinstance(e.value, str)]
            if any(名 in 名们(s) for s in 串):
                见, 唯 = True, 唯 and '--自测' in 串
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == '_自测之项':
            if any(isinstance(a, ast.Constant) and isinstance(a.value, str) and 名 in 名们(a.value) for a in n.args):
                见 = True
    return 见 and 唯


def 析全测(文, 析=None):
    """全测 → {格: {'器': {X.py: 唯自测否}, '载': {模}, '函', '在'}}；析不得 → None。"""
    析 = 析 or (析py(文) if 文 else None)
    if 析 is None or '诸项' not in 析['函']:
        return None
    函节 = {n.name: n for n in 析['树'].body if isinstance(n, ast.FunctionDef)}
    格们 = [(t.elts[0].value, t.elts[1].id) for t in ast.walk(函节['诸项'])
           if isinstance(t, ast.Tuple) and len(t.elts) == 2 and isinstance(t.elts[0], ast.Constant)
           and isinstance(t.elts[0].value, str) and isinstance(t.elts[1], ast.Name)]
    出 = {}
    for 格, fn in 格们:
        if 格 in 出:
            continue
        串, 载, 印, 调串 = 函之闭包(析, [fn])       # 格之所跑唯取 调（列中、run()）之器；只印之语（「先跑 X」之示）⛔算
        出[格] = {'器': {x: fn in 函节 and _唯自测(函节[fn], x) for x in sorted(_器名(调串, ('全测.py',)))},
                 '载': 载, '函': fn, '在': fn in 析['函'], '印': sorted(_器名(印, ('全测.py',)) - _器名(调串))}
    return 出


def 析流(文):
    """yml → (非注之行之文, 触之语)。"""
    行 = [l for l in (文 or '').split('\n') if not l.lstrip().startswith('#')]
    触, 在on, 键 = [], False, None
    for l in 行:
        if re.match(r'^on:\s*$', l):
            在on = True
            continue
        if 在on and re.match(r'^\S', l):
            break
        if not 在on:
            continue
        m = re.match(r'^  (\w+):', l)
        if m:
            键 = m.group(1)
            触.append({'push': 'push', 'schedule': 'cron', 'workflow_dispatch': '手派', 'workflow_call': '他流所调'}.get(键, 键))
        m2 = re.search(r"branches:\s*\[([^\]]*)\]", l)
        if m2 and 键 == 'push' and 触:
            触[-1] = 'push（%s）' % '、'.join(x.strip().strip("'\"") for x in m2.group(1).split(','))
        m3 = re.search(r"cron:\s*'([^']+)'", l)
        if m3 and 键 == 'schedule' and 触:
            触[-1] = 'cron %s' % m3.group(1)
    return '\n'.join(行), '，'.join(触) or '—'


_印之引 = re.compile(r'''\b(?:echo|printf)\b(?:[^\n;|&<>"'`]|"(?:[^"\\]|\\.)*"|'[^']*')*''')   # echo／printf 至 ; | & < > 或行末之诸参（引与否俱去）


def 流之调(文):
    """yml → 所调之器与流（源序·去重）：非注之行中 python3 所调之 工具 之器与 `uses:` 所调之流；
    echo／printf 之引文（「沙盒兜底 python3 工具/推.py --直」之示）⛔算——示非调（用之证环3：推.py 误入 autopush、gate 之调）。"""
    t = _印之引.sub(' ', 析流(文)[0])
    出 = re.findall(r'python3?\s+(?:\./)?工具/([\w\-]+\.py)', t) + re.findall(r'uses:\s*\./\.github/workflows/([\w\-.]+\.yml)', t)
    位 = {x: t.find(x) for x in 出}
    return sorted(dict.fromkeys(出), key=lambda x: 位[x])


_囤灰闸之路 = None          # 自测注之（坏之 囤灰闸 之路）；默 None＝本目之 囤灰闸


def _囤(源):
    """载 囤灰闸（入口、闭包、去注、glob 之族、档之囤灰、末章之尺、唯自测之判俱取之·⛔另写）；一回之生只载一回。
    败（SyntaxError，或 SystemExit 等 BaseException——其首行 raise SystemExit(3) 则旧之 --验 只印其头即 rc 3）→ None，崩书於 ⓪。"""
    if '囤' in 源:
        return 源['囤']
    m = None
    try:
        if _囤灰闸之路:
            import importlib.util
            spec = importlib.util.spec_from_file_location('_囤灰闸之样', _囤灰闸之路)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
        else:
            import 囤灰闸 as m
    except KeyboardInterrupt:
        raise
    except BaseException as e:
        m = None
        源['崩'].append('囤灰闸（载不得：%s %s）' % (type(e).__name__, str(e)[:60]))
    源['囤'] = m
    return m


def _去注js(文, 囤=None):
    return 囤._去注(文 or '', 'js') if 囤 else re.sub(r'(?m)^\s*//.*$', '', 文 or '')


def _壳之文(文):
    """壳之令（git 钩、钩之令）→ 去注行、去 echo／printf 之引文（示非调：「再 python3 工具/推.py」之语⛔算其跑与读）。"""
    return _印之引.sub(' ', '\n'.join(l for l in (文 or '').split('\n') if not l.lstrip().startswith('#')))


_弱式 = re.compile(r'零 ?token|PreToolUse 钩|法用#\S+|.{0,14}立|.*之[一二三四五六七八九十]')
_由首 = re.compile(r'^(?:而)?(?:其立之由|立此器之由|立此闸之由|立此工具之由|其由|所治之伤)[^：]{0,12}：')
_汉 = lambda x: len(re.sub(r'[\x00-\x7f]|[　-〿＀-￯—…·「」]', '', x))


def _弱(s):
    """首句之残：只其标（零 token、PreToolUse 钩、法用#X、「某日立」「三锁之二」）或汉字不足五。"""
    return len(re.sub(r'[\x00-\x7f]', '', s)) < 5 or bool(_弱式.fullmatch(s))


def _句(x, 界=r'[。；\n]|——(?=[·　])'):
    x = re.sub(r'\*\*|★|`', '', x)
    for _ in range(3):
        x = re.sub(r'（[^（）]*）|\([^()]*\)', '', x)
    return re.split(界, x.strip(' —：·'))[0].strip(' —：·⛔')


def 首句(文, 名=''):
    """docstring／注之首句：以段（空行为界）连其行，去 ** 与 ★（⛔留：其义为「不」）、去括注、去其名，截至「。」，≤ 职限。
    首段所余只其名或纯 ASCII（「演练——workflow_dispatch」）者，取首行之「……」引语、或其括注之末节（⛔「某日 立」、法用#X）；再无，取次段。
    所得为残（只其标、汉字不足五：零 token、PreToolUse 钩、单一真源、三锁之二）者，补以「本器……」之句、首行之引语、或次段之首句（用之证环3）。"""
    干 = re.sub(r'\.(py|js|yml|md|json)$', '', 名)
    洋 = lambda x: re.fullmatch(r'[\x00-\x7f]*', x) is not None
    截 = lambda x: x[:职限] + ('…' if len(x) > 职限 else '')
    段们 = re.split(r'\n\s*\n', 文 or '')
    首行 = re.sub(r'\*\*|★', '', (段们[0].strip().split('\n') or [''])[0].lstrip('#>').strip()) if 段们 else ''
    引 = [x for x in re.findall(r'「([^「」]{6,})」', 首行) if not 洋(x)]

    def 补(s0):
        """残之补（汉字八以上者方取）：其律／其法 → 句首之「本器……」→ 诸检之列（① 甲 —— ……）→ 首行之括注、引语 → 次段之「所治之伤／其由：……」。"""
        净 = re.sub(r'\*\*|★|`', '', 文[:2500])
        候 = [_句(m, r'[。\n]') for m in re.findall(r'(?m)(?:【其(?:律|法)】|^[\s★]*(?:其(?:律|法)|所测者[^：\n]{0,4})[：:])\s*([^。\n]{6,})', 净)]
        检 = re.findall(r'(?m)^\s*[①-⑳]\s*(\S[^—\n]{1,12}?)\s*——', 净)
        候 += ['诸检：' + '、'.join(检)] if len(检) >= 3 else []
        候 += [_句(m) for m in re.findall(r'(?:^|(?<=[\n】：，；。\s①-⑳]))本(?:器|钩|闸|哨|守)[只即]?(?!之|的)([^。\n]{6,90})', 净)]
        候 += [_句(x) for x in 引]
        for 段 in 段们[1:4]:
            x = re.sub(r'^\s*(?:【[^】]*】)?', '', ''.join(l.strip() for l in re.sub(r'\*\*|★', '', 段).split('\n')))
            if _由首.match(_句(x) + '：') or _由首.match(x):
                候.append(_句(_由首.sub('', re.sub(r'（[^（）]*）', '', x))))
        候 += [_句(re.sub(r'^[\d\-\s]*立·', '', a or b)) for a, b in re.findall(r'（([^（）]*)）|\(([^()]*)\)', 首行)]
        for x in 候:
            if _汉(x) >= 8 and not _弱(x) and not re.match(r'[第\d·（(]', x):
                return x if (not s0 or s0 in x or re.fullmatch(r'.{0,14}立', s0)) else '%s：%s' % (s0, x)
        return s0
    for k, 段 in enumerate(段们):
        s = ''.join(re.sub(r'\*\*|★', '', l.strip().lstrip('#>').strip()) for l in 段.split('\n'))
        for _ in range(3):
            s = re.sub(r'（[^（）]*）|\([^()]*\)', '', s)
        s = s.strip()
        for 前 in sorted({名, 干, 干.replace('_', ' ')} - {''}, key=len, reverse=True):
            if s.startswith(前):
                余 = s[len(前):]
                if not 余.strip(' ·:：—') or 余.lstrip().startswith('。'):
                    s = ''
                elif 余[0] in ' ·:：—':
                    s = 余.lstrip(' ·:：—').strip()
                break
        s = s.split('。')[0].strip(' —')
        if len(s) >= 4 and not 洋(s):
            return 截(补(s) if _弱(s) else s)
        if k == 0:                              # 首行之引语、括注，依序取其首可者
            候 = [re.split(r'[：·]', a or b)[-1].strip() for a, b in re.findall(r'（([^（）]*)）|\(([^()]*)\)', 首行)] + 引
            候 = [x for x in 候 if len(x) >= 6 and not 洋(x) and not _弱(x)]
            if 候:
                return 截(候[0].split('。')[0])
    return ''


# ═══ 源 ═══
def 读源(根):
    """诸源之文 → 源；缺者记其缺、析不得者记其崩（⛔崩）。"""
    源 = {'根': 根, '缺': [], '崩': []}
    取 = lambda g: {os.path.basename(f): _读(f) or '' for f in sorted(glob.glob(os.path.join(根, *g))) if os.path.isfile(f)}
    源['器'], 源['席'] = 取(('工具', '*.py')), 取(('工具', '席', '*.js'))
    源['流'], 源['git钩'] = 取(('.github', 'workflows', '*.yml')), 取(('工具', 'githooks', '*'))
    设 = _读(os.path.join(根, '.claude', 'settings.json'))
    try:
        源['钩'] = (json.loads(设).get('hooks') or {}) if 设 else None
    except ValueError:
        源['钩'] = None
        源['崩'].append('.claude/settings.json（JSON 坏）')
    源['属'] = '\n'.join(l for l in (_读(os.path.join(根, '.gitattributes')) or '').split('\n') if not l.lstrip().startswith('#'))
    源['总章'] = _读(os.path.join(根, '00_总章.md')) or ''
    源['他读'] = {标: _读(os.path.join(根, p)) or '' for 标, p in 他读之档}
    源['用法'] = _读(os.path.join(根, '工具', '席', '用法.md')) or ''
    for 有, p in ((源['器'].get('封版.py'), '工具/封版.py'), (源['器'].get('全测.py'), '工具/全测.py'), (源['钩'] is not None, '.claude/settings.json'),
                 (源['流'], '.github/workflows/*.yml'), (源['总章'], '00_总章.md')):
        if not 有:
            源['缺'].append(p)
    设定 = os.path.join(根, '设定')
    忽 = _忽(根)                                         # gitignored 之档（器红账、自进化环.log……）⛔入：沙盒有而 GitHub 无，图即两样
    源['账'] = sorted(set(os.path.basename(f) for f in glob.glob(os.path.join(设定, '*.json')) + glob.glob(os.path.join(设定, '*.md'))
                        if os.path.relpath(f, 根).replace(os.sep, '/') not in 忽)
                    | {os.path.basename(图名)})         # 本图恒在其集（⛔因其已生未生而异：--验 之比方定）
    源['账文'] = {x: (_读(os.path.join(设定, x)) or '')[:4000] for x in 源['账']}
    源['子目'] = sorted(os.path.basename(f.rstrip('/')) for f in glob.glob(os.path.join(设定, '*/')))
    源['子目数'] = {d: sum(1 for r, _, fs in os.walk(os.path.join(设定, d)) for f in fs
                         if os.path.relpath(os.path.join(r, f), 根).replace(os.sep, '/') not in 忽) for d in 源['子目']}
    源['版本章'] = sorted(int(m.group(1)) for d in glob.glob(os.path.join(根, '版本', '第*章'))
                       for m in [re.search(r'第(\d+)章$', d.rstrip('/'))] if m)
    迹们 = sorted(int(re.search(r'第(\d+)章', f).group(1)) for f in glob.glob(os.path.join(根, '版本', '第*章', '_器之迹.md')))
    源['迹档数'], 源['迹章'], 源['迹'], 源['迹全'] = len(迹们), 迹们[-迹窗:], {}, {}
    for n in 迹们:                                       # 迹全：诸章之迹（入仓之档·⛔依 git 史）——窗外之末见、无迹之由
        for l in (_读(os.path.join(根, '版本', '第%d章' % n, '_器之迹.md')) or '').split('\n'):
            m = re.match(r'\|\s*([^|\s]+\.py)\s*\|\s*\d+\s*\|', l)
            if m:
                源['迹全'][m.group(1)] = max(n, 源['迹全'].get(m.group(1), 0))
                if n in 源['迹章']:
                    源['迹'][m.group(1)] = max(n, 源['迹'].get(m.group(1), 0))
    if not 迹们:
        源['缺'].append('版本/第N章/_器之迹.md')
    源['末章'] = _末章(根, 源)
    源['W908'] = 读W908(根)
    if not 源['W908']['在']:
        源['缺'].append(W908名.replace(os.sep, '/'))
    源['崩'] += ['W908 名单（%s）' % x for x in 源['W908']['误']]
    源['废治'], 源['审限'] = {}, None
    try:
        册 = json.load(open(os.path.join(设定, '法用册.json'), encoding='utf-8'))
        源['法'] = {k: len(册.get(k) or []) for k in ('法', '待', '废')}
        for x in 册.get('废') or []:                      # 废之条：其去证所列之档、格 → (待合, 限, id)——W908 治之限以此为先
            if isinstance(x, dict) and isinstance(x.get('限'), int):
                for z in x.get('去证') or []:
                    p = isinstance(z, dict) and (z.get('无档') or z.get('无格'))
                    if isinstance(p, str):
                        源['废治'][os.path.basename(p)] = (x.get('待合') or '', x['限'], x.get('id') or '?')
        源['审限'] = next((x['限'] for x in 册.get('待') or [] if isinstance(x, dict) and x.get('id') == '用之审'
                         and isinstance(x.get('限'), int)), None)
    except Exception:
        源['法'] = None
    源['卡'] = _卡(根)
    源['接表'] = 接棒之表(根, 源['器'].get('接棒守' + '.py'))      # 〔W912〕机制之流之表（总编辑、巡警枝、兜底之令、钟之令…）·ast 取·⛔另抄
    心 = 析py(源['器'].get('心跳' + '.py') or '')
    源['心跳之限'] = _常(心['赋']['限'].value, 心['赋']) if 心 and '限' in 心['赋'] else None
    源['近'] = 近之进化(根)
    return 源


_定库之变 = ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_COMMON_DIR', 'GIT_OBJECT_DIRECTORY',
          'GIT_ALTERNATE_OBJECT_DIRECTORIES', 'GIT_NAMESPACE', 'GIT_PREFIX', 'GIT_QUARANTINE_PATH')


def _git(根, *a, **k):
    """⛔承外之 GIT_DIR 诸变（pre-push 之钩中跑全测即带之）——库只由 根 定（同 进化树._env、封版._g）。"""
    e = {x: v for x, v in os.environ.items() if x not in _定库之变}
    return subprocess.run(['git', '-c', 'core.quotepath=off'] + list(a), cwd=根, capture_output=True, text=True, env=e, **k)


def _忽(根):
    """设定、版本 之 gitignored 之档（相对之路）——⛔依史（浅克隆亦可）；无 git 即空。"""
    try:
        r = _git(根, 'ls-files', '--others', '--ignored', '--exclude-standard', '--', '设定', '版本', timeout=20)
        return set(x.strip() for x in r.stdout.split('\n') if x.strip()) if r.returncode == 0 else set()
    except Exception:
        return set()


def _末章(根, 源):
    """正文之末章（逐档读其名之章号·同 囤灰闸.末章 之尺）。败或得 0 → 入 源['崩']（⛔静默：末章静为 0 则诸限「末≤限」俱遮其红）。"""
    囤 = _囤(源)
    n, 由 = 0, None
    if 囤 is None:
        由 = '囤灰闸 载不得，章号之尺无'
    else:
        try:
            诸 = [囤._汉转数(m.group(1)) for f in glob.glob(os.path.join(根, '正文', '*.md'))
                  for m in [re.search(r'第([零〇一二两三四五六七八九十百千]+)章', os.path.basename(f))] if m]
            n = max([x for x in 诸 if x] or [0])
            由 = None if n else '正文无一章之名可认'
        except Exception as e:
            由 = '%s %s' % (type(e).__name__, str(e)[:60])
    if 由:
        源['崩'].append('正文之末章不得（%s）——末章作 0，诸限之红俱遮' % 由)
    return n


def _卡(根):
    """报/卡.json（备份/报·W908 环5）：⛔取远端、⛔依全史；无即 None（卡未立）。"""
    try:
        r = _git(根, 'show', 'refs/remotes/origin/备份/报:报/卡.json', timeout=10)
        d = json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else None
        return d if isinstance(d, dict) else None
    except Exception:
        return None


# ═══ 件 ═══
def _族之(账名):
    for 族, 认, _, _ in _族:
        if re.search(认, 账名):
            return 族
    return re.sub(r'\d+', 'N', 账名) if re.search(r'第\d+[章段]', 账名) else None


def _账职(文, 名):
    """账之职：json 取「说明／注」之键（无即书其键而标「无说明」）；md 首行为引（> 本档由……生成）者取其首句，
    首题为一条之号或日（「## G0925-01 ｜ 2026-09-25」）者书「逐条之录」与其条之目，余取首题。"""
    if 名 == os.path.basename(图名):
        return '本图：一件一行之体系总图（本器之产·随封版 --後）'
    if 名.endswith('.json'):
        m = re.search(r'"_?(?:说明|注)"\s*:\s*"((?:[^"\\]|\\.){4,1200})', 文)
        if m:
            return 首句(m.group(1).replace('\\"', '"'), 名) or m.group(1)[:职限]
        ks = re.findall(r'[{,]\s*"([^"]{1,20})"\s*:', 文[:600])
        return ('（无说明之键）键：' + '、'.join(ks[:4])) if ks else '（无说明之键）'
    行们 = [l.strip() for l in 文.split('\n') if l.strip()]
    if 行们 and 行们[0].startswith('>'):
        x = _句(' '.join(l.lstrip('>').strip() for l in 行们[:3] if l.startswith('>')))
        if _汉(x) >= 4:
            return x[:职限] + ('…' if len(x) > 职限 else '')
    for l in 行们:
        if l.startswith('#'):
            if re.match(r'#+\s*(?:[A-Z]?\d{3,}[\-\d]*|\d{4}-\d\d-\d\d)\s*[｜|]', l):     # 首题即一条之号与日
                目 = list(dict.fromkeys(re.findall(r'\*\*([^*\n]{1,12})\*\*\s*[：:]', 文)))[:3]
                return '逐条之录（首条 %s）%s' % (_句(l.lstrip('#').split('｜')[0]), ('：每条书 ' + '、'.join(目)) if 目 else '')
            return 首句(l, 名) or l.lstrip('#').strip()[:职限]
    return 首句(文, 名) or '（无首题）'


def 立件(源):
    """→ {件名: 件}：名、类（器／席／流／账／族）、路、职、部。"""
    件 = {}
    for x, 文 in 源['器'].items():
        析 = 析py(文)
        if 析 is None:
            源['崩'].append('工具/' + x)
        件[x] = {'类': '器', '路': '工具/' + x, '职': 首句(析['doc'] if 析 else '', x) or '（无 docstring）', '析': 析}
    for x, 文 in 源['席'].items():
        m = re.search(r"description:\s*'([^']*)'", 文)
        件[x] = {'类': '席', '路': '工具/席/' + x, '职': 首句(m.group(1) if m else '', x) or '（无 description）'}
    for x, 文 in 源['流'].items():
        注 = '\n'.join(re.match(r'(?:#[^\n]*\n)*', 文).group(0).split('\n')).replace('\n#   ', '').replace('\n# ', '\n')
        件[x] = {'类': '流', '路': '.github/workflows/' + x, '职': 首句(注, x) or '（无首注）'}
    族计 = {}
    for x in 源['账']:
        族 = _族之(x)
        if 族:
            族计.setdefault(族, []).append(x)
        else:
            件[x] = {'类': '账', '路': '设定/' + x, '职': _账职(源['账文'].get(x, ''), x)}
    for 族, 们 in sorted(族计.items()):
        if len(们) == 1 and 族 not in [z[0] for z in _族]:
            x = 们[0]
            件[x] = {'类': '账', '路': '设定/' + x, '职': _账职(源['账文'].get(x, ''), x)}
            continue
        职 = next((z[3] for z in _族 if z[0] == 族), '') or _账职(源['账文'].get(们[-1], ''), 们[-1])
        件[族] = {'类': '族', '路': '设定/' + 族, '职': 职, '数': len(们), '员': 们}
    for d in 源['子目']:
        k = '设定/%s/' % d
        件[k] = {'类': '族', '路': k, '职': _子目之职.get(d, '设定之子目'), '数': 源['子目数'].get(d, 0)}
    if 源['版本章']:
        件['版本/第N章/'] = {'类': '族', '路': '版本/第N章/', '职': '逐章之版、席记、料与卡', '数': len(源['版本章'])}
    if 源['迹档数']:
        件['版本/第N章/_器之迹.md'] = {'类': '族', '路': '版本/第N章/_器之迹.md', '职': '每章所跑之器与其表现（囤灰闸 --迹）', '数': 源['迹档数']}
    表 = _部表()
    for k, v in 件.items():
        v.update({'名': k, '部': 部之(k, 表), '跑': set(), '读': set(), '载': set()})
    return 件


def 标之(x):
    """件名 → 其作读者之标（器＝其干、席＝席·干、流＝流·干）。"""
    if x.endswith('.py'):
        return x[:-3]
    if x.endswith('.js'):
        return '席·' + x[:-3]
    if x.endswith('.yml'):
        return '流·' + x[:-4]
    return x


def _族之读(k, 文):
    """族、子目之件为 文 所引否。"""
    for 族, _, 读式, _ in _族:
        if k == 族:
            return bool(re.search(读式, 文))
    if k.startswith('设定/') and k.endswith('/'):
        d = re.escape(k[3:-1])
        return bool(re.search(r'设定/%s(?![\w])|[\'"]%s[\'"]' % (d, d), 文))
    if k == '版本/第N章/_器之迹.md':
        return '_器之迹.md' in 文
    if k == '版本/第N章/':
        return bool(re.search(r'版本/第|[\'"]版本[\'"]', 文))
    前 = k.split('N')[0]                    # 第N章／第N段之族：认其 N 前之段（大审_至第%d章.md）
    return len(前) >= 3 and bool(re.search(r'(?<![\w])' + re.escape(前), 文))


def 析跑读(源, 件):
    """诸件之 谁跑（标、时）、谁读（载、引）。"""
    干 = {x[:-3]: x for x in 源['器']}

    def 跑(x, 标, 时):
        if x in 件:
            件[x]['跑'].add((标, 时))

    def 载跑(模们, 标, 时, 除=None):
        for m in 模们:
            if m in 干 and 干[m] != 除:
                跑(干[m], 标, 时)

    囤 = _囤(源)
    # ── 谁读：读者之文（流、钩、git 钩先去 echo／printf 之引文：示非读）──
    读源 = [(x[:-3], '\n'.join(v['析']['全'][0]), v['析']['全'][1]) for x, v in sorted(件.items())
           if v['类'] == '器' and v.get('析') and x != 本器]
    读源 += [('席·' + x[:-3], _去注js(文, 囤), set()) for x, 文 in 源['席'].items()]
    读源 += [('流·' + x[:-4], _印之引.sub(' ', 析流(文)[0]), set()) for x, 文 in 源['流'].items()]
    读源.append(('钩', _壳之文('\n'.join(h.get('command') or '' for 们 in (源['钩'] or {}).values() for g in 们 or [] for h in g.get('hooks') or [])), set()))
    读源 += [('git钩·' + x, _壳之文(文), set()) for x, 文 in 源['git钩'].items()]
    读源.append(('总章', 源['总章'], set()))
    读源 += [(标, 文, set()) for 标, 文 in 源['他读'].items()]
    源['读者'] = [者 for 者, _, _ in 读源]
    长干 = {k: k[:-3] for k, v in 件.items() if v['类'] == '账' and k.endswith('.md') and len(k) - 3 >= 6}   # 同 囤灰闸.档之囤灰
    账名 = [k for k, v in 件.items() if v['类'] == '账']
    for 者, 文, 载 in 读源:
        有 = 名们(文)
        for x in 有:
            if x in 件 and 标之(x) != 者:
                件[x]['读'].add(('引', 者))
        for k, s in 长干.items():
            if k not in 有 and s in 文 and 标之(k) != 者:
                件[k]['读'].add(('引', 者))
        for m in 载:
            if m in 干 and m != 者:
                件[干[m]]['读'].add(('载', 者))
                件[干[m]]['载'].add(者)
        for k, v in 件.items():
            if v['类'] == '族' and _族之读(k, 文):
                v['读'].add(('引', 者))
    # ── 账之 glob 之族（囤灰闸._glob前缀·逐活档）与 档之囤灰 之核：一义一判（⛔另写其律）──
    源['判异'], 源['活档补'] = [], []
    if 囤 is not None:
        try:
            for rel, 文 in 囤._活档(源['根']):
                者 = _活档之标(rel)
                if 者 is None or 者 == 本器[:-3]:
                    continue
                前缀 = 囤._glob前缀([(rel, 文)])
                for k in 账名:
                    if 标之(k) != 者 and any(k.startswith(p) for p in 前缀):
                        件[k]['读'].add(('族', 者))
            md们 = glob.glob(os.path.join(源['根'], '设定', '*.md'))
            无引 = {os.path.basename(p) for p, _ in 囤.档之囤灰(源['根'], 日=0, 末改={
                os.path.relpath(f, 源['根']).replace(os.sep, '/'): 0 for f in md们})}
            for k in 账名:
                if not k.endswith('.md') or k == os.path.basename(图名):
                    continue
                if k not in 无引 and not 件[k]['读']:
                    件[k]['读'].add(('引', '活档'))          # 囤灰闸 认其有引（注、码之字面）而本器寻不着其读者
                    源['活档补'].append(k)
                elif k in 无引 and 件[k]['读']:
                    源['判异'].append(k)
        except Exception as e:
            源['崩'].append('囤灰闸（账之族、档之囤灰之核：%s %s）' % (type(e).__name__, str(e)[:60]))
    # ── 谁跑：封版 ──
    封 = 析封版(源['器'].get('封版.py'), (件.get('封版.py') or {}).get('析'), 源['器'])
    源['封版'] = 封
    if 封 is None and '封版.py' in 源['器']:
        源['崩'].append('工具/封版.py（前／後之析）')
    if 封:                                      # 调（步、闸、存）／载（库）／印令（只印之示）分书——三者之数与 ① 封版之序 同
        for 段, 时 in (('前', '每章封前（封版 --前）'), ('後', '每章封时（封版 --後）')):
            for x in 封[段]:
                跑(x, '封版·' + 段, 时)
            载跑(封['载' + 段], '封版·%s（载）' % 段, 时, '封版.py')
            for x in 封['印' + 段]:
                跑(x, '封版·%s（印令）' % 段, 时)
        步 = 封['序']['後·步']                  # 器之迹之步後所跑者（体系总图、诸闸、存、活态）：其迹⛔入任一章之 _器之迹.md
        i = next((k for k, (a, _) in enumerate(步) if a == '器之迹'), len(步))
        源['後迟'] = {b for _, b in 步[i + 1:]} | {b for _, b in 封['序']['後·闸'] + 封['序']['後·拦'] + 封['序']['後·存']}
    # ── 全测 ──
    测 = 析全测(源['器'].get('全测.py'), (件.get('全测.py') or {}).get('析'))
    源['全测'] = 测
    if 测 is None and '全测.py' in 源['器']:
        源['崩'].append('工具/全测.py（诸项之析）')
    封格 = set(封['快']) | set(封['慢']) | set(封['活']) if 封 else set()
    for 格, g in (测 or {}).items():
        for 时 in ('每推（GitHub 全测）',) + (('每章封时（封版 --後 之全测 --只）',) if 格 in 封格 else ()):
            for x, 唯 in g['器'].items():
                跑(x, '全测·%s%s' % (格, '（唯自测）' if 唯 else ''), 时)
            载跑(g['载'], '全测·' + 格, 时, '全测.py')
    # ── 流 ──
    源['触'] = {x: 析流(文)[1] for x, 文 in 源['流'].items()}
    源['流调'] = {x: [y for y in 流之调(文) if y != x] for x, 文 in 源['流'].items()}
    for x, 文 in 源['流'].items():
        for y in 源['流调'][x]:
            跑(y, '流·' + x[:-4], '%s（%s）' % (x[:-4], 源['触'][x]))
        跑(x, 'GitHub', 源['触'][x])
    # ── 钩、git 钩、merge 驱 ──
    for 事, 们 in (源['钩'] or {}).items():
        for g in 们 or []:
            mt = g.get('matcher') or ''
            标 = '钩·%s%s' % (事, (':' + (mt if len(mt) <= 14 else mt[:12] + '…')) if mt else '')
            时 = _钩之时.get(事, '钩 ' + 事)
            时 = 时 % ((mt if len(mt) <= 24 else mt[:22] + '…') or '诸具') if '%s' in 时 else 时
            for h in g.get('hooks') or []:
                for y in 名们(_壳之文(h.get('command') or '')):
                    跑(y, 标, 时)
    for x, 文 in 源['git钩'].items():                # pre-push 唯调 全测并；「再 python3 工具/推.py」係 echo 之示⛔算
        for y in 名们(_壳之文(文)):
            跑(y, 'git钩·' + x, '每 git ' + x.replace('pre-', ''))
    for m in re.findall(r'merge=(\S+)', 源['属']):
        跑(m + '.py', 'git·merge 驱', '并账有冲突时（git merge）')
    # ── 席：其令所跑之器；其派令（囤灰闸.派令之席）与 用法.md 之表 ──
    for x, 文 in 源['席'].items():
        for y in 名们(_去注js(文, 囤)):
            if y.endswith('.py'):
                跑(y, '席·' + x[:-3], _席之时.get(x[:-3], '席跑时'))
    派, 表, 口 = set(), {}, []
    if 囤 is not None:
        try:
            派 = 囤.派令之席([(p, 源['器'].get(os.path.basename(p)) or 源['席'].get(os.path.basename(p)) or '')
                          for p in ('工具/席/造章.js', '工具/自走.py')])
            表, 口 = 囤.席表(源['用法']), list(囤.真跑口)
        except Exception as e:
            源['崩'].append('囤灰闸（入口之析：%s）' % str(e)[:60])
    for x in 源['席']:
        位 = (表.get(x) or ('',))[0].replace('`', '')
        if x in 派:
            跑(x, '派令·自走', 位 or _席之时.get(x[:-3], '自走派'))
        elif x in 表:
            跑(x, '用法表', 位)
    # ── 入口（囤灰闸.真跑口）与其所引之器 ──
    源['入口'] = 口
    for p in 口:
        x = os.path.basename(p)
        跑(x, '入口', '主环手跑')
        if x in ('封版.py', '全测.py') or not (件.get(x) or {}).get('析'):
            continue
        _, l, _, 印, 调串 = 件[x]['析']['全']
        时 = _口之时.get(x[:-3], '随 ' + x[:-3])
        调器 = _器名(调串, (x,))
        for y in 调器:
            跑(y, '口·' + x[:-3], 时)
        for y in _器名(印, (x,)) - 调器:             # 只印其令（自走「只印一行命令」：主环照跑之处方）——与 调 分书
            跑(y, '口·%s（印令）' % x[:-3], 时)
        载跑(l, '口·%s（载）' % x[:-3], 时, x)
    # ── 自驱（常驻之器：while 中 sleep·存底守 每五分）──
    for x, v in 件.items():
        秒 = (v.get('析') or {}).get('驱') if v['类'] == '器' else None
        if 秒:
            跑(x, '自驱（後台常驻）', '後台每 %s 分（常驻·自驱）' % (('%g' % (秒 / 60)) if 秒 % 60 else 秒 // 60))
    # ── 囤灰闸之闭包（可达否·⛔另写）──
    源['可达'] = None
    if 囤 is not None:
        _旧 = 囤.ROOT
        囤.ROOT = 源['根']
        try:
            源['可达'] = 囤.器之闭包()
        except Exception as e:
            源['崩'].append('囤灰闸.器之闭包（%s）' % str(e)[:60])
        finally:
            囤.ROOT = _旧
    return 件


def _活档之标(rel):
    """囤灰闸._活档 之相对路 → 本图读者之标（器＝干、席·干、流·干、git钩·名、钩）；他者 None。"""
    d, b = os.path.split(rel)
    if d == '工具' and b.endswith('.py'):
        return b[:-3]
    if d == '工具/席' and b.endswith('.js'):
        return '席·' + b[:-3]
    if d == '.github/workflows' and b.endswith('.yml'):
        return '流·' + b[:-4]
    if d == '工具/githooks':
        return 'git钩·' + b
    return '钩' if rel == '.claude/settings.json' else None


def _本职之跑(v):
    return {(a, b) for a, b in v['跑'] if '（唯自测）' not in a}


def _治之(源, 件名, 环):
    """W908 之环 → (环, 限, 限之源)：废之条（去证列此档）之限先之；无则乙批之环 (环, None, 乙批·无专限)——只 ⚠，⛔借 用之审 之限
    （乙批俟 W907 入主，用之审 之 476 早於其期）；余（甲批）取 待「用之审」之限；俱无 → None（甲批之治而无限：⛔）。"""
    if not 环:
        return None
    if 件名 in 源.get('废治', {}):
        _, 限, i = 源['废治'][件名]
        return (环, 限, '法用#%s·废' % i)
    if (源.get('W908') or {}).get('批', {}).get(环) == '乙':
        return (环, None, '乙批·无专限')
    if 源.get('审限'):
        return (环, 源['审限'], '法用#用之审')
    return None


def _治文(治, 随='随 '):
    """治 → 「随 W908 环7·限 484（法用#…·废）」或「随 W908 环7（乙批·无专限：只 ⚠）」。"""
    if 治[1] is None:
        return '%sW908 %s（%s：只 ⚠）' % (随, 治[0], 治[2])
    return '%sW908 %s·限 %d（%s）' % (随, 治[0], 治[1], 治[2])


def _机判(v, 账):
    if v['有跑'] and v['有读']:
        return '用', '机判：有跑有读'
    if v['有读']:
        return '半用', ('机判：其读者无一有跑' if 账 else ('机判：有读无跑' + ('（唯自测）' if v['跑'] else '')))
    if v['有跑']:
        return '半用', '机判：有跑无读'
    return '未用', ('机判：无一件引之' if 账 else '机判：无跑无读')


_盲名 = {'GitHub': 'GitHub', '闸後': '封版闸後', '载': '被载'}     # 迹之盲处（一眼之读法释之）


def _迹由(源, k, v):
    """器之无迹（末十章之 _器之迹 不见）之由：其跑俱在迹之盲处（GitHub、封版闸後、被载）→「迹盲」；否则书窗外之末见或「全迹无」。"""
    盲 = set()
    for a, b in v['跑']:
        if '（载）' in a:
            盲.add('载')
        elif b.startswith('每章封时（封版 --後 之全测'):
            盲.add('闸後')
        elif a.startswith(('全测·', '流·')) or a == 'GitHub':
            盲.add('GitHub')
        elif a.startswith('封版·後'):
            盲.add('闸後' if k in 源.get('後迟', ()) else '他')
        else:
            盲.add('他')
    if not v['跑'] and v['有跑']:
        盲.add('载')
    窗外 = ('窗外末见第%d章' % 源['迹全'][k]) if k in 源.get('迹全', {}) else ''
    if 盲 and '他' not in 盲:
        return '迹盲：' + '、'.join(_盲名[x] for x in sorted(盲)) + (('·' + 窗外) if 窗外 else '')
    return 窗外 or '全迹无'


def 判之(源, 件):
    """有跑（本职之跑、末十章之迹、载於有跑者）、有读 → 判；W908 名单先之（今之机判与之相抵者书「候复审」；死、未用而仍有本职之跑者书「悖」）；红。"""
    末, 迹, 名单 = 源['末章'], 源['迹'], 源['W908']['表']
    有跑 = {k for k, v in 件.items() if v['类'] in ('席', '流') and v['跑']}
    有跑 |= {k for k, v in 件.items() if v['类'] == '器' and (_本职之跑(v) or k in 迹)}
    干 = {k[:-3]: k for k, v in 件.items() if v['类'] == '器'}
    变 = True
    while 变:                                   # 载於有跑者 → 随之有跑
        变 = False
        for k, v in 件.items():
            if v['类'] == '器' and k not in 有跑 and any(干.get(m) in 有跑 for m in v['载']):
                有跑.add(k)
                变 = True
    跑者 = {标之(k) for k in 有跑} | {'钩', '总章'} | {'git钩·' + x for x in 源['git钩']} | set(源['他读'])
    for k, v in 件.items():
        账 = v['类'] in ('账', '族')
        读 = {b for _, b in v['读']}
        v['有跑'], v['有读'] = (bool(读 & 跑者), bool(读)) if 账 else (k in 有跑, bool(读))
        v['末'] = 迹.get(k) if v['类'] == '器' else None
        v['迹由'] = _迹由(源, k, v) if v['类'] == '器' and not v['末'] else None
        v['机判'], v['机由'] = _机判(v, 账)
        v['机'], v['悖'], v['环'], v['治行'] = False, None, None, False
        if k in 名单:
            v['判'], 由, v['环'], 治类, _ = 名单[k]
            v['由'], v['治'] = 'W908：' + 由, _治之(源, k, v['环'])
            本 = sorted(set(a for a, _ in _本职之跑(v)))
            if not 账 and v['判'] in ('死', '未用') and 治类 == '接入' and v['机判'] == '用':   # 器之治＝接入而已行（改记 入大审之包）：⛔冻於原判而红
                #   （账之死係义判〔陈而不销〕，其读者有跑早在审时——机判之用⛔证其治已行）
                v['治行'] = True
                v['悖'] = '治已行（W908 %s 接入·今机判：用%s）——候复审' % (v['环'], ('；' + _列(本, 3)) if 本 else '')
            elif v['判'] in ('死', '未用') and 本 and not 账:
                v['悖'] = '悖：%s而仍有跑口（%s）' % (v['判'], _列(本, 3))
            elif not 账 and v['判'] == '半用' and v['末'] and v['机判'] == '用':     # 名单之由多係义判（恒 True、0 对），机⛔驳；唯今迹见之方书
                v['悖'] = '今迹见第%d章（机判：用）——候复审' % v['末']
            elif not 账 and v['判'] == '用' and v['机判'] != '用':
                v['悖'] = '今机判：%s（%s）——候复审' % (v['机判'], v['机由'][3:])
        else:
            v['治'], v['机'] = None, True
            v['判'], v['由'] = v['机判'], v['机由']
        v['红'] = None
        if v['判'] in ('未用', '死'):
            if v['治行']:
                v['红'] = '⚠'                    # 接入之治已行：候复审
            elif v['治'] and (v['治'][1] is None or 末 <= v['治'][1]):
                v['红'] = '⚠'                    # 随 W908 之治，未逾其限（乙批无专限：只 ⚠）
            elif 账 and v['机']:
                v['红'] = '⚠'                    # 账之机判未用：候审（同 囤灰闸.档之囤灰 只报）
            else:
                v['红'] = '⛔'
    源['有跑'] = 有跑
    return 件


# ═══ ⑥ 机制之流·⑦ 近之进化·活之色（W912）═══
# 1120 作者令「方法上的更新和不断的进化……整体的那个全图也要随之更新」；续令（四）「只要执行起来，这个全图里面这个东西它不会发亮吗？
#   它或者变绿……执行主义它就要通过这个方式去判断」——图之件须与其真跑之迹相应：跑即亮绿（W912 环5）。
# 节之名、边之语、诸表俱⛔书器之全名（器带 .py：同上文之律）——器书其干，载时以 _展件／_展档 复之；md 之账书「干#md」。
def _展件(x):
    """表中之件 → 件名：「干#md」→ 干.md；带 .js／.yml／.json 者照书；余（器之干）补 .py；None 照返。"""
    if x is None:
        return None
    x = x.replace('+', '')
    if x.endswith('#md'):
        return x[:-3] + '.md'
    return x if x.endswith(('.js', '.yml', '.json', '.md')) else x + '.py'


def _展档(x):
    """源档之表（工具/接棒守、设定/甲+乙#md、.github/workflows/巡.yml）→ 仓内之路。"""
    x = x.replace('+', '')
    if x.endswith('#md'):
        return x[:-3] + '.md'
    if x.startswith('工具/') and not re.search(r'\.(py|js|json|md|yml)$', x):
        return x + '.py'
    return x


# 节：(键, 名, 部, 件〔其灯随此件·器书其干〕, 迹〔平台之件之迹之源·见 _迹之源〕, 期〔'章'｜'兜底'｜'钟'｜'心跳'｜'巡'·None＝按需〕)
_流节 = (
    ('作者', '作者', None, None, None, None),
    ('总编辑', '总编辑之坐', '觉', None, '巡应', '兜底'),
    ('兜底', '兜底之令', '觉', None, '巡应', '兜底'),
    ('钟', '钟之令', '觉', None, '巡钟', '钟'),                     # 接棒守 有 钟之令 方立（W911）
    ('派', '【派】create_session', '觉', None, None, None),
    ('写书', '写书之坐', '心', None, '心跳', '心跳'),
    ('造章', '造章之席', '心', '造章.js', None, None),
    ('封版', '封版', '脉', '封版', None, None),
    ('推', '推（交 治-sha12）', '脉', '推', None, None),
    ('治章枝', '治／章之枝', '脉', None, '报推', '章'),
    ('autopush', 'autopush（gate 分片）', '脉', 'autopush.yml', None, None),
    ('gate', 'gate（分片之闸）', '脉', 'gate.yml', None, None),
    ('主枝', '主枝', '脉', None, '主枝', '章'),
    ('报', '备份/报', '脉', None, '报枝', '章'),
    ('心跳', '心跳', '脉', '心跳', None, None),
    ('存底守', '存底守', '脉', '存底守', None, None),
    ('演练', '演练', '脉', '演练.yml', None, None),
    ('云巡', '云巡（接棒守 --云巡）', '觉', None, '巡印', '巡'),
    ('巡印', '备份/巡印', '觉', None, '巡印', '巡'),
    ('哨PR', '哨 PR', '觉', None, None, None),
    ('巡应', '备份/巡应', '觉', None, '巡应', '兜底'),
    ('巡钟', '备份/巡钟', '觉', None, '巡钟', '钟'),                 # 钟之令在、或流之推之触含其枝 方立
    ('方案', '方案（图之用）', '长', '方案', None, None),
    ('复盘', '复盘', '长', '复盘', None, None),
    ('方法账', '方法账', '长', '方法账#md', None, None),
    ('进化树', '进化树', '长', '进化树', None, None),
    ('法用之守', '法用之守', '长', '法用之守', None, None),
    ('图', '体系总图', '长', '体系总图', None, None),
)
# 流之边（非机取者）：(甲, 乙, 语, 源档, 须含之串)——逐边验其串在其档，不在即 ⓪ 报「流之边失据 N」、其边书虚线（⛔崩）。
#   机取者（⛔入此表）：流之触与 job（.github/workflows/*.yml 之 on 与 job 之 if·uses）、兜底之令／钟之令（接棒守 之表）。
_流边 = (
    ('作者', '总编辑', '令（常令·对谈）', '设定/00_作者常令+_不停之律#md', '总编辑'),
    ('总编辑', '派', '派章（--派令 之参原样）', '工具/接棒守', 'create_session'),
    ('派', '写书', '新坐接写书之锁', '工具/接棒守', 'def 派之参('),
    ('写书', '心跳', '心跳之锁（存底守续之）', '工具/存底守', '续本坐之锁'),
    ('写书', '存底守', '开头之钩起之（每五分）', '.claude/settings.json', '存底守'),
    ('写书', '造章', 'Workflow 派席（自走之印令）', '工具/自走', '造章.js'),
    ('造章', '封版', '料成→封版 --後', '工具/席/造章.js', '封版'),
    ('封版', '法用之守', '--後 --验 N', '工具/封版', '法用之守'),
    ('封版', '进化树', '--後 随三账', '工具/封版', "('进化树随', [器("),
    ('封版', '图', '--後 重画', '工具/封版', "('体系总图', [器("),
    ('封版', '治章枝', '存底 --标 N（推 章-N）', '工具/封版', "'--标'"),
    ('写书', '推', '治之推', '工具/封版', '交治枝'),
    ('总编辑', '推', '治之推（方法之变）', '工具/推', '拦总编辑之纸'),
    ('推', '治章枝', '交 治-sha12', '工具/推', "'HEAD:refs/heads/' + 名"),
    ('法用之守', '推', '纸证之闸（交前）', '工具/推', 'def 纸证之闸('),
    ('图', '推', '图之闸（总编辑之治·交前）', '工具/推', 'def 图之闸('),
    ('autopush', '主枝', '闸过即并（advance）', '.github/workflows/autopush.yml', 'advance:'),
    ('autopush', '报', '果入 报/推', '.github/workflows/autopush.yml', 'REPORT: 备份/报'),
    ('演练', '报', '果入 报/演', '.github/workflows/演练.yml', '报/演'),
    ('云巡', '巡印', '每跑 force 写', '工具/接棒守', "巡印枝 = '备份/巡印'"),
    ('云巡', '哨PR', '非止即唤（一言）', '工具/接棒守', 'def 哨PR('),
    ('哨PR', '总编辑', 'subscribe_pr_activity 唤之', '工具/接棒守', 'subscribe_pr_activity'),
    ('巡印', '总编辑', '--巡 验巡印（旧即 rc 5）', '工具/接棒守', 'def 巡印之由('),
    ('总编辑', '巡应', '--巡 落巡应', '工具/接棒守', 'def 落巡应('),
    ('巡应', '云巡', '验其应（闭环）', '工具/接棒守', 'def 应判('),
    ('总编辑', '手派', 'run_workflow 补起（rc 5）', '工具/接棒守', 'run_workflow'),
    ('复盘', '方法账', '升级链之行（草）', '工具/复盘', 'def 方法账之草('),
    ('方案', '图', '--图 W 取图之用（每设计必用图）', '工具/方案', '图之用'),
    ('法用之守', '图', '--报 末行·图之红与灯（今算）', '工具/法用之守', '图·用之红'),
    ('总编辑', '图', '--随治（方法一变图即随）', '工具/体系总图', "'--随治'"),
    ('图', '总编辑', '执行之图（--巡 印其 --摘）', '工具/接棒守', '── 执行之图 ──'),
)
_接表之键 = ('总编辑', '主枝', '巡警枝', '巡印枝', '巡印档', '巡应枝', '兜底之令', '钟之令', '巡钟枝')


def 接棒之表(根, 文=None):
    """工具/接棒守 之码之表（总编辑、主枝、巡警枝、巡印枝、巡应枝、兜底之令、钟之令〔W911·在方取〕、巡钟枝）——ast 取其字面
    （⛔另抄·⛔载其模：他根之样亦可析）；读不得或析不得 → {}（⓪ 书之）。"""
    文 = 文 if 文 is not None else _读(os.path.join(根, '工具', '接棒守' + '.py'))
    出 = {}
    try:
        树 = ast.parse(文 or '')
    except (SyntaxError, ValueError):
        return 出
    for n in 树.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) and n.targets[0].id in _接表之键:
            try:
                出[n.targets[0].id] = ast.literal_eval(n.value)
            except (ValueError, SyntaxError, TypeError):
                pass
    return 出


def _去前(x):
    return re.sub(r'^(session_|cse_)', '', str(x or '').strip())[:32]


def 本坐():
    """本会话之号：取 心跳.坐（CLAUDE_CODE_REMOTE_SESSION_ID → CLAUDE_SESSION_ID → CLAUDE_CODE_SESSION_ID，去 session_／cse_·⛔另写·坑53）；
    载不得或「未名」→ ''（--随治 即拒）。"""
    try:
        import 心跳
        x = 心跳.坐()
        return '' if x == '未名' else x
    except Exception:
        return ''


def cron之期(式):
    """cron 五栏 → 两跑之隔（秒）：「*/N * * * *」→N 分；「M * * * *」→一时（M 列 k 数→一时／k）；「M */H * * *」→H 时；「M H * * *」→一日；余 None。"""
    f = str(式 or '').split()
    if len(f) != 5 or f[2:] != ['*', '*', '*']:
        return None
    分, 时 = f[0], f[1]
    m = re.fullmatch(r'\*/(\d+)', 分)
    if m and 时 == '*' and int(m.group(1)):
        return int(m.group(1)) * 60
    if re.fullmatch(r'\d+(?:,\d+)*', 分):
        k = len(分.split(','))
        if 时 == '*':
            return 3600 // k
        m = re.fullmatch(r'\*/(\d+)', 时)
        if m and int(m.group(1)):
            return int(m.group(1)) * 3600 // k
        if re.fullmatch(r'\d+(?:,\d+)*', 时):
            return 86400 // (k * len(时.split(',')))
    return None


def _合期(诸):
    """诸令之隔 → 合之隔（率相加：二令各一时 → 三十分）；无即 None。"""
    诸 = [p for p in 诸 if p]
    return int(round(1.0 / sum(1.0 / p for p in 诸))) if 诸 else None


def _令之cron(x, 取开=False):
    """兜底之令（名, 号, 常, 降, 开）／钟之令（名, 号, cron）之一行 → (名, cron, 开)；不识 → None。"""
    if not isinstance(x, (tuple, list)) or not x:
        return None
    诸 = [c for c in x[1:] if isinstance(c, str) and cron之期(c)]
    开 = x[-1] if isinstance(x[-1], bool) else True
    return (str(x[0]), 诸[0], 开) if 诸 else None


# ── 流之构：yml 之 on 与 jobs（缩进析·⛔依 yaml 之库）──
def 流之构(文):
    """yml → {'触': [(事, [参])], 'job': {名: {'if', 'uses', 'needs', '文'}}}（非注之行）。事：push（参＝枝式）、schedule（参＝cron）、
    workflow_dispatch、workflow_call。"""
    触, job = [], {}
    段, 事, 名, 在枝 = None, None, None, False
    for l in (文 or '').split('\n'):
        if l.lstrip().startswith('#') or not l.strip():
            continue
        if re.match(r'^on:\s*$', l):
            段 = 'on'
            continue
        if re.match(r'^jobs:\s*$', l):
            段 = 'jobs'
            continue
        if re.match(r'^\S', l):
            段 = None
            continue
        if 段 == 'on':
            m = re.match(r'^  ([\w\-]+):', l)
            if m:
                事, 在枝 = m.group(1), False
                触.append((事, []))
                continue
            if 事 == 'push':
                m = re.search(r'branches:\s*\[([^\]]*)\]', l)
                if m:
                    触[-1][1].extend(x.strip().strip('\'"') for x in m.group(1).split(',') if x.strip())
                    continue
                if re.match(r'^\s+branches:\s*$', l):
                    在枝 = True
                    continue
                m = re.match(r'^\s+-\s+(.+?)\s*$', l)
                if 在枝 and m:
                    触[-1][1].append(m.group(1).strip('\'"'))
                    continue
                在枝 = False
            elif 事 == 'schedule':
                m = re.search(r'cron:\s*[\'"]([^\'"]+)[\'"]', l)
                if m:
                    触[-1][1].append(m.group(1))
        elif 段 == 'jobs':
            m = re.match(r'^  ([\w\-]+):\s*$', l)
            if m:
                名 = m.group(1)
                job[名] = {'if': '', 'uses': '', 'needs': [], '文': []}
                continue
            if 名 is None:
                continue
            job[名]['文'].append(l)
            m = re.match(r'^    if:\s*(.+?)\s*$', l)
            if m:
                job[名]['if'] = re.sub(r'^\$\{\{\s*|\s*\}\}$', '', m.group(1))
            m = re.match(r'^    uses:\s*\./\.github/workflows/(\S+)', l)
            if m:
                job[名]['uses'] = m.group(1)
            m = re.match(r'^    needs:\s*(.+?)\s*$', l)
            if m:
                job[名]['needs'] = [x.strip(' []\'"') for x in m.group(1).split(',') if x.strip(' []\'"')]
    for v in job.values():
        v['文'] = '\n'.join(v['文'])
    return {'触': 触, 'job': job}


def _分(式, 符):
    """顶层（括号外、引号外）以 符 分。"""
    出, 深, 起, i, 引 = [], 0, 0, 0, None
    while i < len(式):
        c = 式[i]
        if 引:
            引 = None if c == 引 else 引
        elif c in '\'"':
            引 = c
        elif c == '(':
            深 += 1
        elif c == ')':
            深 -= 1
        elif 深 == 0 and 式.startswith(符, i):
            出.append(式[起:i])
            i += len(符)
            起 = i
            continue
        i += 1
    出.append(式[起:])
    return [x.strip() for x in 出]


def _去外括(x):
    x = x.strip()
    while x.startswith('(') and x.endswith(')'):
        深 = 0
        for i, c in enumerate(x):
            深 += 1 if c == '(' else -1 if c == ')' else 0
            if 深 == 0 and i < len(x) - 1:
                return x
        x = x[1:-1].strip()
    return x


def _枝始(枝, 前):
    if not 枝:
        return None
    字 = 枝.split('*')[0]
    if 字.startswith(前):
        return True
    return None if '*' in 枝 and 前.startswith(字) else False


def _式值(式, 事, 枝):
    """GitHub 之式 → True／False／None（不定：inputs.*、always()、needs.* 等）。"""
    式 = _去外括(式)
    或 = _分(式, '||')
    if len(或) > 1:
        vs = [_式值(x, 事, 枝) for x in 或]
        return True if True in vs else (None if None in vs else False)
    且 = _分(式, '&&')
    if len(且) > 1:
        vs = [_式值(x, 事, 枝) for x in 且]
        return False if False in vs else (None if None in vs else True)
    if 式.startswith('!') and not 式.startswith('!='):
        v = _式值(式[1:], 事, 枝)
        return None if v is None else not v
    m = re.fullmatch(r"github\.event_name\s*(==|!=)\s*'([^']*)'", 式)
    if m:
        return (事 == m.group(2)) == (m.group(1) == '==')
    m = re.fullmatch(r"startsWith\(\s*github\.ref_name\s*,\s*'([^']*)'\s*\)", 式)
    if m:
        return _枝始(枝, m.group(1))
    m = re.fullmatch(r"github\.ref_name\s*(==|!=)\s*'([^']*)'", 式)
    if m and 枝:
        等 = (枝 == m.group(2)) if '*' not in 枝 else (None if m.group(2).startswith(枝.split('*')[0]) else False)
        return None if 等 is None else (等 == (m.group(1) == '=='))
    return None


def 若可(式, 事, 枝=None, 主=''):
    """job 之 if 於某触（事、push 之枝式）可真否（不定之项作「或真」）；非 push 之事其 ref_name 作主枝（定时、手派俱於默枝）。"""
    式 = re.sub(r'^\$\{\{\s*|\s*\}\}$', '', (式 or '').strip())
    if not 式:
        return True
    return _式值(式, 事, 枝 if 事 == 'push' else 主) is not False


_节名之禁 = str.maketrans({'"': '', "'": '', '`': '', '(': '（', ')': '）', '[': '［', ']': '］', '{': '｛', '}': '｝',
                       '<': '〈', '>': '〉', '|': '／', '#': '＃', ';': '；', '\n': ' '})


def 节名(x):
    """mermaid 之节名、边语：⛔引号与括号乱其式（ASCII 之括作全角、引号去之）。"""
    return str(x).translate(_节名之禁).strip()


def 立流(源, 件):
    """⑥ 机制之流 → {'节': {键: 节}, '序': [键], '边': [[甲, 乙, 语, 源, 机]], '失据': [..], '机': n, '表': n}。"""
    表 = 源.get('接表') or {}
    主 = 表.get('主枝') or ''
    节, 序 = {}, []

    def 加(键, 名, 部=None, 件名=None, 迹=None, 期=None):
        if 键 not in 节:
            节[键] = {'键': 键, '名': 名, '部': 部, '件': 件名, '迹': 迹, '期': 期}
            序.append(键)
        return 键
    钟令 = [x for x in (_令之cron(y) for y in (表.get('钟之令') or ())) if x]
    兜令 = [x for x in (_令之cron(y) for y in (表.get('兜底之令') or ())) if x]
    钟枝 = 表.get('巡钟枝') or '备份/巡钟'
    构 = {x: 流之构(文) for x, 文 in sorted(源['流'].items())}
    推枝 = {b for c in 构.values() for e, 参 in c['触'] if e == 'push' for b in 参}
    for 键, 名, 部, 件名, 迹, 期 in _流节:   # noqa
        if (键 == '钟' and not 钟令) or (键 == '巡钟' and not (钟令 or 钟枝 in 推枝)):
            continue
        加(键, 名, 部, _展件(件名), 迹, 期)
    if 表.get('总编辑'):
        节['总编辑']['名'] = '总编辑之坐（%s）' % _去前(表['总编辑'])[:10]
    if 表.get('巡警枝'):
        节['哨PR']['名'] = '哨 PR（头枝 %s）' % 表['巡警枝']
    if 兜令:
        节['兜底']['名'] = '兜底之令（%s）' % '·'.join('%s%s' % (n, '' if k else '停') for n, _, k in 兜令)
    if 钟令:
        节['钟']['名'] = '钟之令（%s）' % '·'.join(n for n, _, _ in 钟令)
    件键 = {x['件']: k for k, x in 节.items() if x['件']}
    边 = []

    def 连(甲, 乙, 语, 源_, 机):
        for x in 边:
            if x[0] == 甲 and x[1] == 乙 and x[3] == 源_ and x[4] == 机:
                if 语 not in x[2].split('、'):
                    x[2] += '、' + 语
                return
        边.append([甲, 乙, 语, 源_, 机])

    def 触节(枝):
        if re.match(r'(章|治)-\*', 枝):
            return '治章枝'
        if 枝 == 钟枝:
            return 加('巡钟', '备份/巡钟', '觉', None, '巡钟', '钟')
        return 加('push:' + 枝, 'push ' + 枝, None)
    云巡令 = '接棒守' + '.py --云巡'
    自派, 流之节们 = [], {}
    for x, c in 构.items():
        展 = len(c['job']) >= 2 and any('github.event_name' in j['if'] for j in c['job'].values())   # 诸 job 各依其触：逐 job 立节
        流键 = None if 展 else (件键.get(x) or 加('流:' + x, x[:-4], (件.get(x) or {}).get('部'), x))
        jk = {}
        if 展:
            for j in c['job']:
                jk[j] = 加('%s#%s' % (x, j), '%s·%s' % (x[:-4], j), (件.get(x) or {}).get('部'), None, None, None)
                节[jk[j]]['流'], 节[jk[j]]['job'] = x, j
        for 事, 参 in c['触']:
            诸 = [(触节(b), 'push ' + b, b) for b in 参] if 事 == 'push' else \
                [('定时', 'cron ' + y, None) for y in 参] if 事 == 'schedule' else \
                [('手派', '手派', None)] if 事 == 'workflow_dispatch' else []
            for 甲, 语, 枝 in 诸:
                if 甲 in ('定时', '手派'):
                    加(甲, {'定时': 'GitHub 定时（cron）', '手派': '手派（workflow_dispatch）'}[甲])
                if not 展:
                    连(甲, 流键, 语, '%s on.%s' % (x, 事), True)
                    continue
                for j, v in c['job'].items():
                    if not v['needs'] and 若可(v['if'], 事, 枝, 主):
                        连(甲, jk[j], 语, '%s on.%s·%s.if' % (x, 事, j), True)
        for j, v in c['job'].items():
            自 = jk.get(j, 流键)
            if v['uses'] and v['uses'] in 构:
                连(自, 件键.get(v['uses']) or 加('流:' + v['uses'], v['uses'][:-4], (件.get(v['uses']) or {}).get('部'), v['uses']),
                  'uses', '%s jobs.%s.uses' % (x, j), True)
            for n in v['needs']:
                if 展 and n in jk:
                    连(jk[n], 自, 'needs', '%s jobs.%s.needs' % (x, j), True)
            if 云巡令 in v['文']:
                连(自, '云巡', '--云巡', '%s jobs.%s' % (x, j), True)
                if 展:
                    节[自]['迹'], 节[自]['云巡'] = '巡印', True     # 诸 job 共一迹（巡印⛔辨 job）：灯之 唯最密者认之、余 ⚪
            if '/dispatches' in v['文']:                    # 自派（续／再起）：直连其所派之流（手派之节唯外来之派·⛔作诸流之中转）
                m = re.search(r'workflows/([^/\s"\']+\.yml)/dispatches', v['文'])
                自派.append((自, urllib.parse.unquote(m.group(1)) if m else x, '%s jobs.%s' % (x, j)))
        流之节们[x] = (流键, jk, c)
    for 自, 的, 源_ in 自派:
        流键_, jk_, c_ = 流之节们.get(的) or (None, {}, None)
        if 流键_:
            连(自, 流键_, '自派（续／再起）', 源_, True)
        elif jk_:
            for j_, v_ in c_['job'].items():
                if not v_['needs'] and 若可(v_['if'], 'workflow_dispatch', None, 主):
                    连(自, jk_[j_], '自派（续／再起）', 源_, True)
        else:
            连(自, 加('手派', '手派（workflow_dispatch）'), '自派（续／再起）', 源_, True)
    if 兜令:
        连('兜底', '总编辑', '、'.join('%s %s%s' % (n, c, '' if k else '（停）') for n, c, k in 兜令), '接棒守.兜底之令', True)
    if 钟令:
        连('钟', '巡钟', '、'.join('%s %s' % (n, c) for n, c, _ in 钟令) + '·--钟 推之', '接棒守.钟之令', True)
    机 = len(边)
    失 = []
    for 甲, 乙, 语, 档, 含 in _流边:
        if 甲 not in 节 or 乙 not in 节:
            continue
        p = _展档(档)
        文 = _读(os.path.join(源['根'], p))
        if 文 is None or 含 not in 文:
            失.append('%s→%s（%s 无「%s」）' % (节[甲]['名'], 节[乙]['名'], p, 含))
            连(甲, 乙, 语 + '（失据）', p, False)
        else:
            连(甲, 乙, 语, p, False)
    return {'节': 节, '序': 序, '边': 边, '失据': 失, '机': 机, '表': len(边) - 机, '构': 构}


# ── 近之进化：工作流账 W9xx 之裁之末八 ──
def _裁摘(由, 限=80):
    """裁之由 → 「所废：…；较旧：…」之摘（无则由之首）·≤ 限 字。"""
    由 = re.sub(r'\s+', ' ', str(由 or ''))
    废 = re.search(r'所废[：:]\s*(.*?)(?=[；;。]\s*较旧|较旧[：:]|$)', 由)
    旧 = re.search(r'较旧[：:]\s*(.*)$', 由)
    s = '；'.join(x for x in (('所废：' + 废.group(1).strip(' ；;。')) if 废 else '', ('较旧：' + 旧.group(1).strip()) if 旧 else '') if x) or 由
    return s if len(s) <= 限 else s[:限 - 1] + '…'


def 近之进化(根, 数=8):
    """设定/工作流账.json「件」中 W9xx（总编辑之件）之裁之末 数 → [(件, 名, 法, 时, 摘)]（新者先）；读不得 → None。"""
    try:
        d = json.load(open(os.path.join(根, '设定', '工作流账.json'), encoding='utf-8'))
    except Exception:
        return None
    诸 = []
    for x in (d.get('件') if isinstance(d, dict) else None) or []:
        if not isinstance(x, dict) or not re.fullmatch(r'W9\d\d', str(x.get('id') or '')):
            continue
        for c in x.get('裁') or []:
            if isinstance(c, dict) and c.get('时'):
                诸.append((str(c['时']), str(x['id']), str(x.get('名') or ''), str(c.get('法') or '?'), _裁摘(c.get('由'))))
    诸.sort(key=lambda z: (z[0], z[1]))
    return [(i, 名, 法, 时, 摘) for 时, i, 名, 法, 摘 in 诸[-数:]][::-1]


# ── 活之色：迹之源（件或件之类 → 迹之源与取法·零 token）──
_迹之源 = {
    '巡印': '枝 备份/巡印 之末提交（云巡每跑 force 写）；其 rc 1 ＝器自败',
    '巡应': '枝 备份/巡应 之末提交（总编辑沙盒之 --巡 每跑写）',
    '心跳': '枝 备份/心跳 之末提交（写书之坐之锁·存底守续之）',
    '存底': '枝 备份/存底* 之末提交（树改方推：按改·⛔作末跑）',
    '巡钟': '枝 备份/巡钟 之末提交（钟之令每跑推·W911）',
    '主枝': '枝 主枝 之末提交',
    '报枝': '枝 备份/报 之末提交',
    '报推': '备份/报 之 报/推/*.json 之末（推报.读：时、果、因）——autopush 之跑（果「败」即末跑败；因 merge 书「合入之卡」）',
    '报在': '备份/报 之 报/推/*.json 之末（不论其果）——推报之写已成（报在即成）',
    '报治': '备份/报 之 报/推/治-*.json 之末（不论其果）——推.py 之交（治-sha12）已至 GitHub（章-N 由存底 --标 推·⛔算）',
    '报闸': '备份/报 之 报/推/*.json 之末之「成／红」者——gate 真跑（备候不成〔因 merge〕、拒⛔算）',
    '报演': '备份/报 之 报/演/*.json 之末（推报.读演：时）——演练之跑',
    '卡': '备份/报 之 报/卡.json 之「算於」（运营卡）',
    '封': '本树 HEAD 与 origin/<主枝> 之史并取「封版#N」之提交之时（章之封：封版、造章、封版所跑之器·树落後主枝亦⛔误迟）',
    '图档': 'git log -1 HEAD 与 origin/<主枝> 并取 设定/体系总图.md（图之重画）',
    '迹': '版本/第N章/_器之迹.md（写书之坐之器）→ 第N章之封时；树无而主枝有之章，git show origin/<主枝> 取之',
    '全测': '备份/报 之 报/推 之末之「成／红」者——唯「全测·X」所跑而无真路之件（哨、负测）取之：其格在报之「免」（活态之格）⛔算、在报之「红」即末跑败；'
            '有真路（口·、席·、封版·、流·、钩·、入口……）者取其真路之迹，⛔借闸而绿',
}
# 件之迹表（器书其干）：其件之末跑另取於此源（与「迹」「封」「全测」「流」之通取并，取其末）
_迹表 = {
    '巡.yml': ('巡印',), 'autopush.yml': ('报推',), 'gate.yml': ('报闸',), '演练.yml': ('报演',),
    '接棒守': ('巡印', '巡应'), '心跳': ('心跳',), '存底守': ('存底',), '推': ('报治',), '推报': ('报在',),
    '运营卡': ('卡',), '封版': ('封',), '造章.js': ('封',), '体系总图': ('图档',),
}
_流之迹 = {'autopush.yml': '报推', 'gate.yml': '报闸', '巡.yml': '巡印', '演练.yml': '报演'}
_流迹之别 = {('流·autopush', '全测.py'): '报闸'}       # autopush 之 全测 --并果 唯 GO=1（gate 真跑）方跑：备候不成之报⛔作其跑
_未鲜之源 = ('巡印', '巡应', '巡钟')                    # 总编辑之迹枝：写书之坐⛔取（取=False 而逾期 → ⚪「迹未取」·⛔作当跑而未跑）
_借迹 = {'兜底': '借巡应⛔辨其触：兜底之令、哨 PR 之唤、手跑 --巡 俱写 备份/巡应'}   # 流之节：其迹为他者所共写 → ⚪ 迹不可取
_灯 = ('🟢', '🟡', '🔴', '⚪')


def _刻(t):
    return time.strftime('%m-%d %H:%M', time.gmtime(t)) if t else '?'


def _iso秒(s):
    try:
        import calendar
        return calendar.timegm(time.strptime(str(s)[:19].replace('T', ' '), '%Y-%m-%d %H:%M:%S'))
    except Exception:
        return None


def _期文(秒):
    if not 秒:
        return '?'
    分 = 秒 / 60.0
    return ('%g 分' % round(分)) if 分 < 90 else ('%g 时' % round(分 / 60, 1))


def 可取():
    """活之色先取其旧之迹否：ZM_TU_NOFETCH=1 即⛔（自测、施工之树）；--摘、--件、--印、--随治 默取，写（封版 --後）、--验 ⛔取（⛔拖累写书）。"""
    return os.environ.get('ZM_TU_NOFETCH', '') not in ('1', 'true')


def 读迹(源, 今, 取=False):
    """迹之源 → {'值': {源: (时, 败, 注)}, '封': {N: 时}, '封末', '章期', '旧', '停', '解停', '枝名', '落後', '迹主', '闸免', '闸红'}——零 token：
    git for-each-ref／log／show 於本地之 origin/*；取（--摘 等）：本地之 备份/* 迹枝旧於十五分者先 git fetch 其枝（限八秒·败即用旧而注「迹旧」·主枝⛔取）。
    取不得之源⛔入（⚪「迹不可取」·⛔猜）；本地之引或旧者（取=False 之 巡印／巡应／巡钟、取败者）注「本地未取」——逾期 ⚪「迹未取」⛔作当跑而未跑。
    封与图档取 HEAD 与 origin/<主枝> 之并（总编辑之树落後主枝、封版 --後 之树先於主枝，俱⛔误迟）。"""
    根, 表 = 源['根'], 源.get('接表') or {}
    主 = 表.get('主枝') or ''
    枝名 = {'巡印': 表.get('巡印枝') or '备份/巡印', '巡应': 表.get('巡应枝') or '备份/巡应', '心跳': '备份/心跳',
          '巡钟': 表.get('巡钟枝') or '备份/巡钟', '主枝': 主, '报枝': '备份/报'}
    迹 = {'值': {}, '封': {}, '封末': None, '章期': None, '旧': set(), '停': False, '解停': None, '枝名': 枝名,
         '落後': 0, '迹主': {}, '闸免': set(), '闸红': set()}
    前 = 'refs/remotes/origin/'

    def 枝时():
        try:
            r = _git(根, 'for-each-ref', '--format=%(refname)%09%(committerdate:unix)', 前, timeout=10)
        except Exception:
            return {}
        出 = {}
        for l in (r.stdout or '').split('\n') if r.returncode == 0 else []:
            a, _, b = l.partition('\t')
            if a.startswith(前) and b.strip().isdigit():
                出[a[len(前):]] = int(b)
        return 出
    时们 = 枝时()
    if 取:
        旧 = [b for k, b in sorted(枝名.items()) if k != '主枝' and b in 时们 and 今 - 时们[b] > 15 * 60]
        if 旧:
            try:
                r = _git(根, 'fetch', '-q', 'origin', *['+refs/heads/%s:%s%s' % (b, 前, b) for b in 旧], timeout=8)
                if r.returncode == 0:
                    时们 = 枝时()
                else:
                    迹['旧'] = set(旧)
            except Exception:
                迹['旧'] = set(旧)
    for k in ('巡印', '巡应', '心跳', '巡钟', '主枝', '报枝'):
        b = 枝名[k]
        if b and b in 时们:
            未鲜 = b in 迹['旧'] or (not 取 and k in _未鲜之源)
            迹['值'][k] = (时们[b], False, b + ('·本地未取' if 未鲜 else ''))
    if '巡印' in 迹['值']:                                # 云巡之末 rc 1 ＝器自败（末跑败）
        try:
            r = _git(根, 'show', '%s%s:%s' % (前, 枝名['巡印'], 表.get('巡印档') or '_巡印.json'), timeout=10)
            d = json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else {}
            if isinstance(d, dict) and d.get('rc') == 1:
                t, _, 注 = 迹['值']['巡印']
                迹['值']['巡印'] = (t, True, 注 + '·末巡 rc 1（器自败）')
        except Exception:
            pass
    存 = [(t, b) for b, t in 时们.items() if b.startswith('备份/存底')]
    if 存:
        t, b = max(存)
        迹['值']['存底'] = (t, False, b)
    主引 = [前 + 主] if 主 and 主 in 时们 else []           # HEAD 与 origin/<主枝> 之并（⛔唯 HEAD：树落後主枝即封、迹俱误迟）
    if 主引:
        try:
            r = _git(根, 'rev-list', '--count', 'HEAD..' + 主引[0], timeout=10)
            迹['落後'] = int(r.stdout.strip()) if r.returncode == 0 and r.stdout.strip().isdigit() else 0
        except Exception:
            pass
    try:                                                 # 章之封：「封版#N」之提交（HEAD 与主枝之史·新者先）
        r = _git(根, 'log', '-n', '40', '--format=%ct%x09%s', '--grep=封版#', 'HEAD', *主引, timeout=10)
        for l in (r.stdout or '').split('\n'):
            m = re.match(r'(\d+)\t.*封版#(\d+)）', l)
            if m:
                迹['封'].setdefault(int(m.group(2)), int(m.group(1)))
    except Exception:
        pass
    if 迹['封']:
        末 = max(迹['封'])
        迹['封末'] = (末, 迹['封'][末])
        迹['值']['封'] = (迹['封'][末], False, '第%d章之封' % 末)
        近 = [n for n in sorted(迹['封']) if n > 末 - 11]
        if len(近) >= 2 and 迹['封'][近[-1]] > 迹['封'][近[0]]:
            迹['章期'] = (迹['封'][近[-1]] - 迹['封'][近[0]]) / float(近[-1] - 近[0])
    树章 = max(源.get('迹章') or [0])
    for n in sorted(x for x in 迹['封'] if x > 树章)[-4:] if 主引 else []:   # 树无而主枝有之章之迹（git show·⛔动盘）
        try:
            r = _git(根, 'show', '%s:版本/第%d章/_器之迹.md' % (主引[0], n), timeout=10)
        except Exception:
            continue
        for l in (r.stdout or '').split('\n') if r.returncode == 0 else []:
            m = re.match(r'\|\s*([^|\s]+\.py)\s*\|\s*\d+\s*\|', l)
            if m:
                迹['迹主'][m.group(1)] = max(n, 迹['迹主'].get(m.group(1), 0))
    for 类, 目 in (('报推', '报/推'), ('报演', '报/演')):   # 末数笔之报（新者先）：报推＝末报（败即末跑败）、报闸＝末之「成／红」（gate 真跑：备候不成、拒⛔算）
        try:
            r = _git(根, 'log', '-n', '12', '--format=%x01%ct', '--name-only', 前 + '备份/报', '--', 目, timeout=10)
            名们, ct = [], None
            for x in (r.stdout or '').split('\n') if r.returncode == 0 else []:
                x = x.strip()
                if x.startswith('\x01'):
                    ct = int(x[1:]) if x[1:].isdigit() else None
                elif x.startswith(目 + '/') and x.endswith('.json') and ct and x not in [y for _, y in 名们]:
                    名们.append((ct, x))
            候 = []
            for ct, p in 名们[:16]:
                名 = p[len(目) + 1:-5]
                d = _报之读(根, 类, 名) or {}
                果, 因 = d.get('果', '?'), d.get('因') or ''
                候.append((_iso秒(d.get('时')) or ct, 类 == '报推' and 果 == '败' and 因 != '重派',
                           '%s/%s（%s%s）' % (目, 名, 果, ('·因 ' + 因) if 因 else ''), 果, d, 名))
            if 候:
                迹['值'][类] = _取末([x[:3] for x in 候])
            if 类 == '报推' and 候:
                迹['值']['报在'] = _取末([(x[0], False, x[2]) for x in 候])
                治 = [(x[0], False, x[2]) for x in 候 if x[5].startswith('治-')]
                if 治:
                    迹['值']['报治'] = _取末(治)
            闸 = [x for x in 候 if 类 == '报推' and x[3] in ('成', '红')]
            if 闸:
                t, _, 注 = _取末([x[:3] for x in 闸])
                d = max(闸, key=lambda x: x[0])[4]
                迹['值']['报闸'] = (t, False, 注)
                迹['值']['全测'] = (t, False, 'gate 之全测·' + 注)   # gate 之全测：唯「全测·X」而无真路之件取之（_件之候）
                免 = d.get('免')
                迹['闸免'] = set(免 if isinstance(免, list) else _活态之格(根))
                迹['闸红'] = _报之红格(d)
        except Exception:
            pass
    卡 = 源.get('卡') or {}
    t = _iso秒(卡.get('算於'))
    if t:
        迹['值']['卡'] = (t, False, '报/卡.json 算於')
    try:
        r = _git(根, 'log', '-1', '--format=%ct', 'HEAD', *主引, '--', 图名.replace(os.sep, '/'), timeout=10)
        if r.returncode == 0 and r.stdout.strip().isdigit():
            迹['值']['图档'] = (int(r.stdout.strip()), False, '图之重画')
    except Exception:
        pass
    迹['停'], 迹['解停'] = _停之迹(根)
    return 迹


def _停之迹(根):
    """→ (停, 解停之时｜None)：暂停令在否（暂停令.在）；令已解者取其「解」之时（解停之後首章之期自解停起算·⛔即红）。"""
    try:
        import 暂停令 as _停
        停 = bool(_停.在(根)[0])
        d = _停.读令(根) or {}
    except Exception:
        return False, None
    解 = d.get('解') if isinstance(d, dict) else None
    if 停 or not isinstance(解, dict):
        return 停, None
    try:
        import calendar
        return False, calendar.timegm(time.strptime(str(解.get('时', ''))[:16], '%Y-%m-%d %H:%M'))
    except Exception:
        return False, None


def _活态之格(根):
    """全测.py 之「活态之格」（GitHub 之片闸免之）——报无「免」者以此为免（⛔载全测·只读其文）。"""
    m = re.search(r'^活态之格\s*=\s*\(([^)]*)\)', _读(os.path.join(根, '工具', '全测.py')) or '', re.M)
    return set(re.findall(r"'([^']+)'", m.group(1))) if m else set()


def _报之红格(d):
    """报之「红」之列 → 红之格名之集（「⛔全测未过：甲、乙」为先；无则取「✗ 格名」之行）。"""
    红 = d.get('红') if isinstance(d.get('红'), list) else []
    for l in 红:
        m = re.match(r'\s*⛔全测未过[：:]\s*(.+?)\s*$', str(l))
        if m:
            return {x.strip() for x in re.split(r'[、,，]', m.group(1)) if x.strip()}
    return {m.group(1) for l in 红 for m in [re.match(r'\s*✗\s+(\S+)', str(l))] if m}


def _报之读(根, 类, 名):
    """推报.读／读演（取=False·⛔网）；载不得即自 git show 读之。"""
    try:
        import 推报 as _报
        return (_报.读 if 类 == '报推' else _报.读演)(名, 根, 取=False)
    except Exception:
        try:
            r = _git(根, 'show', 'refs/remotes/origin/备份/报:%s/%s.json' % ('报/推' if 类 == '报推' else '报/演', 名), timeout=10)
            d = json.loads(r.stdout) if r.returncode == 0 else None
            return d if isinstance(d, dict) else None
        except Exception:
            return None


def 期之(时, 章期):
    """何时跑之一语 → (秒, 名)｜None（按需·无定期）：常驻每 N 分；cron（流之触）；含「每章」／自走每跑／每回合／会话之起／每调／push 章-*·治-* → 章期；
    每推 → 章期（推必随章·宁宽）；每十章 → 章期×10；余（并账有冲突时、主环手跑、随 X、手派、每段……）→ None。"""
    m = re.search(r'每 ([\d.]+) 分（常驻', 时)
    if m:
        return float(m.group(1)) * 60, '常驻·每 %s 分' % m.group(1)
    诸 = [(cron之期(c), 'cron ' + c) for c in re.findall(r'cron ((?:[^\s，）]+ ){4}[^\s，）]+)', 时) if cron之期(c)]
    if 章期:
        if '每十章' in 时:
            诸.append((章期 * 10, '每十章'))
        elif 时.startswith('每推'):
            诸.append((章期, '每推（≥ 每章）'))
        elif '每章' in 时 or 时.startswith(('自走每跑', '每回合', '会话之起', '每调')) or re.search(r'push（[^）]*(?:章|治)-\*', 时):
            诸.append((章期, '每章'))
    return min(诸) if 诸 else None


def _灯判(末, 败, 期, 今):
    if 败:
        return '🔴'
    if 末 is None or 期 is None:
        return '⚪'
    d = 今 - 末
    return '🟢' if d <= 期 * 1.5 else '🟡' if d <= 期 * 3 else '🔴'


def _停可(期名):
    """期之名随写书与兜底（暂停令停之）否：每章／每推／每十章（章期）、常驻、兜底之令合、心跳之限、钟之令合 → True；GitHub 之 cron → False（暂停中照跑）。"""
    return bool(期名) and (期名 in ('每章', '每推（≥ 每章）', '每十章', '兜底之令合', '心跳之限', '钟之令合') or 期名.startswith('常驻'))


def _灯由(灯, 候, 期, 按改=False, 停=False, 起=None):
    """→ 由（⛔「〕」）：末跑之刻与其源、期、迟／逾期×3／末跑败（因 merge 书「合入之卡」）；停：暂停中；起：解停之刻（期自此起算）。"""
    if not 候:
        if 停:
            return '暂停中（暂停令在·⛔当跑）·迹不可取'
        return '迹不可取' + (('·期 %s（%s）' % (_期文(期[0]), 期[1])) if 期 else '·按需')
    t, 败, 注 = 候
    末 = '末 %s（%s）' % (_刻(t), 注)
    败语 = '·合入之卡（因 merge·主枝与本推之账相冲）' if 败 and '·因 merge' in 注 else '·末跑败'
    if 按改:
        return '按改（树未改即⛔推·⛔作末跑）·' + 末
    if 灯 == '⚪' and 期 and not 败 and '本地未取' in 注:
        return '迹未取（本地之引或旧·⛔判迟·今算见 --摘）·%s·期 %s（%s）' % (末, _期文(期[0]), 期[1])
    if 期 is None:
        return ('暂停中（暂停令在·⛔当跑）·' if 停 else '按需·') + 末 + (败语 if 败 else '')
    s = '%s·期 %s（%s）' % (末, _期文(期[0]), 期[1]) + (('·自解停 %s 起算' % _刻(起)) if 起 else '')
    return s + {'🔴': 败语 if 败 else '·逾期×3', '🟡': '·迟'}.get(灯, '')


def _灯定(末, 期, 今, 停, 解停):
    """→ (灯, 期, 起)：暂停中随停之期作 None（⚪ 暂停中）；解停之後首期自解停起算（⛔因停而即红）；本地未取之迹逾期 → ⚪（迹未取·⛔猜）。"""
    if 停 and 期 and _停可(期[1]):
        期 = None
    起 = 解停 if (解停 and 期 and 末 and _停可(期[1]) and 末[0] < 解停) else None
    灯 = _灯判(起 or (末[0] if 末 else None), 末[1] if 末 else False, 期[0] if 期 else None, 今)
    if 灯 in ('🟡', '🔴') and 末 and not 末[1] and '本地未取' in 末[2]:
        灯 = '⚪'
    return 灯, 期, 起


def 灯文(灯, 由):
    return '%s〔%s〕' % (灯, str(由).replace('〔', '（').replace('〕', '）').replace('\n', ' '))


def _闸格(a):
    """跑者「全测·X」→ X（gate 跑其本职之格）；「（唯自测）」「全测·X·自测」（唯跑其自测）、非全测 → None。"""
    if not a.startswith('全测·') or '（唯自测）' in a or a.endswith('·自测'):
        return None
    return a[3:]


def _真路(跑们):
    """跑者有真路否：全测之格之外（口·、席·、封版·、流·、钩·、入口、派令、GitHub、自驱……）——有即其灯取其真路之迹，⛔借 gate 之全测。"""
    return any(not a.startswith('全测·') for a in 跑们)


def _件之候(源, 迹, k, v):
    """件之末跑之诸候 → [(时, 败, 注)]：迹表所列者唯其专源；余取 迹（写书之坐之器·树无者取主枝之迹）、封（封版所跑）、
    gate 之全测（唯无真路之件：其格⛔在报之「免」，在「红」即末跑败）、流（流所调：只承其时·⛔承其败）。"""
    值, 候 = 迹['值'], []
    干 = k[:-3] if k.endswith('.py') else k
    if 干 in _迹表:                                      # 迹表所列者唯取其专源（其本职之迹：封版＝章之封、推＝报/推/治-*……）
        return [值[s] for s in _迹表[干] if s in 值]
    if v['类'] == '器':
        n = max((源.get('迹全') or {}).get(k, 0), (迹.get('迹主') or {}).get(k, 0))
        t = 迹['封'].get(n) if n else None
        if t:
            候.append((t, False, '迹·第%d章' % n))
    跑名 = {a for a, _ in v['跑'] if '（唯自测）' not in a}
    if any(a.startswith('封版·') for a in 跑名) and '封' in 值:
        候.append(值['封'])
    格们 = {g for g in (_闸格(a) for a in 跑名) if g} - set(迹.get('闸免') or ())
    if 格们 and not _真路(跑名) and '全测' in 值:
        t, _, 注 = 值['全测']
        红 = sorted(格们 & set(迹.get('闸红') or ()))
        候.append((t, bool(红), 注 + (('·其格红：' + '、'.join(红)) if 红 else '')))
    for a in 跑名:
        s = _流迹之别.get((a, k)) or (_流之迹.get(a[2:] + '.yml') if a.startswith('流·') else None)
        if s and s in 值:
            候.append((值[s][0], False, 值[s][2]))           # 流所调者只承其时、⛔承其败（流之败唯着其流与治章枝）
    return 候


def _取末(候):
    if not 候:
        return None
    t = max(x[0] for x in 候)
    同 = [x for x in 候 if x[0] == t]
    败 = [x for x in 同 if x[1]]
    return 败[0] if 败 else 同[0]


def 灯之(源, 件, 流, 今):
    """每件、每流之节之灯（🟢🟡🔴⚪）与其由 → v['灯']、v['灯由']、v['灯文']；流之节同。期：何时跑之机判（期之）；末跑：迹之源（_迹表 等）。
    暂停中：随写书与兜底之期俱 ⚪（暂停中·⛔当跑），GitHub 之 cron 照判；解停之後首期自解停起算。"""
    迹 = 源['活迹']
    章期, 停, 解停 = 迹['章期'], bool(迹.get('停')), 迹.get('解停')
    末们 = {k: _取末(_件之候(源, 迹, k, v)) for k, v in 件.items() if v['类'] not in ('账', '族')}
    原 = dict(末们)                                    # 一层：载者之末取其本迹（⛔链传）
    for k, v in 件.items():                           # 载於有迹之器者（口·自走（载）、封版·後（载））随其载者之末跑（一层）
        if k not in 末们 or (k[:-3] if k.endswith('.py') else k) in _迹表:
            continue
        候 = [末们[k]] if 末们[k] else []
        for a, _ in v['跑']:
            者 = None if not a.endswith('（载）') else ('封版' + '.py') if a.startswith('封版·') else (a[2:-3] + '.py') if a.startswith('口·') else None
            if 者 and 原.get(者):
                候.append((原[者][0], False, '随载者 %s：%s' % (者[:-3], 原[者][2])))
        末们[k] = _取末(候)
    for k, v in 件.items():
        if v['类'] in ('账', '族'):
            v['灯'], v['灯由'] = '⚪', '账（⛔跑·随其读写之器）'
        else:
            跑们 = [(a, b) for a, b in v['跑'] if '（唯自测）' not in a]
            真 = _真路([a for a, _ in 跑们])             # 有真路者：全测之格之期⛔算（每推之期唯 gate 之跑·⛔借以判其真路）
            期们 = [p for p in (期之(b, 章期) for b in {b for a, b in 跑们 if not (真 and a.startswith('全测·'))}) if p]
            期 = min(期们) if 期们 else None
            末 = 末们.get(k)
            按改 = '存底' in _迹表.get(k[:-3] if k.endswith('.py') else k, ())
            if 按改:
                灯, 期2, 起 = '⚪', 期, None
            else:
                灯, 期2, 起 = _灯定(末, 期, 今, 停, 解停)
            v['灯'], v['灯由'] = 灯, _灯由(灯, 末, 期2, 按改, 停 and 期 is not None and 期2 is None, 起)
        v['灯文'] = 灯文(v['灯'], v['灯由'])
    if not 流:
        return
    表 = 源.get('接表') or {}
    兜 = _合期([cron之期(c) for _, c, k in (x for x in (_令之cron(y) for y in (表.get('兜底之令') or ())) if x) if k])
    钟 = _合期([cron之期(c) for _, c, _ in (x for x in (_令之cron(y) for y in (表.get('钟之令') or ())) if x)])
    心 = 源.get('心跳之限')
    期表 = {'章': (章期, '每章') if 章期 else None, '兜底': (兜, '兜底之令合') if 兜 else None, '钟': (钟, '钟之令合') if 钟 else None,
          '心跳': (心, '心跳之限') if 心 else None}
    for x in 流['节'].values():                           # 巡之 job：其触之期（cron→其隔；push 章-*／治-*→章期；余按需）
        if x.get('job'):
            诸 = []
            for e in 流['边']:
                if e[1] != x['键'] or not e[4]:
                    continue
                for 语 in e[2].split('、'):
                    if 语.startswith('cron ') and cron之期(语[5:]):
                        诸.append((cron之期(语[5:]), 语))
                    elif re.match(r'push (?:章|治)-\*', 语) and 章期:
                        诸.append((章期, '每章'))
            x['期值'] = min(诸) if 诸 else None
    云们 = [x for x in 流['节'].values() if x.get('job') and x.get('云巡')]
    巡们 = [x['期值'] for x in 云们 if x.get('期值')]
    期表['巡'] = min(巡们) if 巡们 else 期表['章']
    if len(云们) >= 2:                                   # 诸 job 共写 备份/巡印（force·⛔辨 job）：唯最密者认其迹，余 ⚪（⛔借最密者之跑而绿）
        最 = min(巡们) if 巡们 else None
        for x in 云们:
            if not (最 and x.get('期值') and x['期值'][0] <= 最[0]):
                x['不辨'] = '巡印⛔辨 job：%s 共 force 写一枝，末者恒为最密者（%s）' % (
                    '、'.join(sorted(y['名'] for y in 云们)), 最[1] if 最 else '?')
    for x in 流['节'].values():
        期 = (x['期值'] if x.get('job') else 期表.get(x['期'])) if x['迹'] else None
        if x['件']:
            v = 件.get(x['件'])
            x['灯'], x['灯由'] = (v['灯'], v['灯由']) if v else ('⚪', '件不在盘')
        elif not x['迹']:
            x['灯'], x['灯由'] = '⚪', '按需（平台之件·无迹）'
        elif x['键'] == '写书' and 停:
            x['灯'], x['灯由'] = '⚪', '暂停中（暂停令在·⛔当跑）'
        elif x.get('不辨') or x['键'] in _借迹:
            由 = x.get('不辨') or _借迹[x['键']]
            x['灯'], x['灯由'] = '⚪', '迹不可取（%s）' % 由 + (('·期 %s（%s）' % (_期文(期[0]), 期[1])) if 期 else '')
        else:
            末 = 迹['值'].get(x['迹'])
            灯, 期2, 起 = _灯定(末, 期, 今, 停, 解停)
            x['灯'], x['灯由'] = 灯, _灯由(灯, 末, 期2, False, 停 and 期 is not None and 期2 is None, 起)
        x['灯文'] = 灯文(x['灯'], x['灯由'])


def _灯计(们):
    return [sum(1 for v in 们 if v.get('灯') == g) for g in _灯]


def _灯计文(们):
    return '·'.join('%s %d' % (g, n) for g, n in zip(_灯, _灯计(们)))


_类色 = {'🟢': 'lg', '🟡': 'ly', '🔴': 'lr', '⚪': 'lw'}


def 印流(源, 件):
    """⑥ 机制之流：mermaid（GitHub 即绘·classDef 绿黄红灰著诸节之灯）＋文本之链＋流之节之灯。"""
    流 = 源.get('流图')
    if not 流:
        return ['## ⑥ 机制之流', '', '- （流之构不得：见 ⓪）', '']
    节, 序 = 流['节'], 流['序']
    号 = {k: 'n%02d' % (i + 1) for i, k in enumerate(序)}
    L = ['## ⑥ 机制之流（作者→总编辑→派→写书→封→推→GitHub 之闸→主枝；巡之环与其迹·灯＝其迹之鲜）', '',
         '> 节＝平台之件与诸器（器之节随其件之灯）；边＝谁触谁：流之触与 job 自 `.github/workflows/*.yml` 之 on 与 job 之 if 机取，'
         '兜底之令／钟之令／巡警枝 自 接棒守 之表机取，余照本器 流之边 之表（逐边验其串在其档·失据即 ⓪ 报、书虚线）。'
         '灯（今算·--验 ⛔比）：🟢 当跑而已跑（末跑 ≤ 期×1.5）｜🟡 迟（≤ 期×3）｜🔴 当跑而未跑（逾期×3）或末跑败｜⚪ 按需、账、或迹不可取（⛔猜）。'
         '迹之源与期见下「流之节之灯」与 ⓪。', '', '```mermaid', 'flowchart LR']
    部名 = {'心': '心·作家', '脉': '脉·丝滑', '觉': '觉·守', '长': '长·进化', '学': '学', None: '平台与 GitHub 之触'}
    for i, 部 in enumerate((None,) + 部序):
        们 = [k for k in 序 if 节[k]['部'] == 部]
        if not 们:
            continue
        L.append('  subgraph b%d["%s"]' % (i, 节名(部名[部])))
        L += ['    %s["%s"]' % (号[k], 节名(节[k]['名'])) for k in 们]
        L.append('  end')
    for 甲, 乙, 语, _, 机 in 流['边']:
        L.append('  %s %s|"%s"| %s' % (号[甲], '-->' if 机 or '（失据）' not in 语 else '-.->', 节名(语), 号[乙]))
    L += ['  classDef lg fill:#d8f5d0,stroke:#2e7d32,color:#111', '  classDef ly fill:#fff3c4,stroke:#b8860b,color:#111',
          '  classDef lr fill:#ffd6d6,stroke:#c62828,color:#111', '  classDef lw fill:#eeeeee,stroke:#888888,color:#111']
    for g in _灯:
        们 = [号[k] for k in 序 if 节[k].get('灯') == g]
        if 们:
            L.append('  class %s %s' % (','.join(们), _类色[g]))
    L += ['```', '', '### 流之链（文本·终端可读；机＝机取，表＝流之边之表验过其串）', '']
    for 甲, 乙, 语, 源_, 机 in 流['边']:
        L.append('- %s →〔%s〕→ %s｜%s %s' % (节[甲]['名'], 语, 节[乙]['名'], '机' if 机 else '表', 源_))
    L += ['', '### 流之节之灯（今算·--验 ⛔比）', '', '| 节 | 部 | 灯 | 迹之源 |', '|---|---|---|---|']
    for k in 序:
        x = 节[k]
        源名 = ('随其件 ' + x['件']) if x['件'] else (_迹之源.get(x['迹'], '—') if x.get('迹') else '—（按需）')
        L.append('| %s | %s | %s | %s |' % (_格(x['名']), x['部'] or '平台', _格(x.get('灯文', '⚪')), _格(源名)))
    L.append('')
    return L


def 印近(源):
    近 = 源.get('近')
    L = ['## ⑦ 近之进化（设定/工作流账.json「件」W9xx 之裁·末八·新者先）', '']
    if 近 is None:
        return L + ['- 工作流账读不得（⓪ 书之）', '']
    L += ['| 件 | 名 | 裁 | 时 | 所废／较旧（摘·≤80 字） |', '|---|---|---|---|---|']
    L += ['| %s | %s | %s | %s | %s |' % (i, _格(名[:40] + ('…' if len(名) > 40 else '')), 法, 时, _格(摘)) for i, 名, 法, 时, 摘 in 近]
    return L + ['']


# ═══ 印 ═══
def _格(s):
    return str(s).replace('|', '｜').replace('\n', ' ').strip()


def _列(们, 限=列限):
    们 = list(们)
    return ('、'.join(们[:限]) + ('等 %d' % len(们) if len(们) > 限 else '')) if 们 else '—'


_时序 = ('後台', '会话', '每回合', '每调', '每章', '自走', '巡', '主环', '每十章', '存版', '随', '每 git', '并账', 'autopush', 'gate',
        '演练', '每推')


def _时之序(b):
    """何时跑之序：真之节律（自驱、钩、封版、主环）先，GitHub 之跑後——截时⛔遮其要。"""
    return (next((i for i, x in enumerate(_时序) if b.startswith(x)), len(_时序)), b)


def 行之文(v, 全=False):
    限 = 10 ** 6 if 全 else 列限
    跑 = sorted(set(a for a, _ in v['跑']), key=lambda a: (('全测·' in a or '流·' in a or a == 'GitHub'), a))
    时 = sorted(set(b for _, b in v['跑']), key=_时之序)
    if v['类'] in ('账', '族'):
        跑s, 时s = '—（账：随其读写之器）', '随其器'
    else:
        随载 = v['有跑'] and v['载'] and not _本职之跑(v)
        跑s = _列(跑, 限) if 跑 else ('随其载者' if 随载 else '迹见（末十章）' if v.get('末') else '—')
        if 随载:
            跑s = (跑s + '；' if 跑 else '') + '随其载者（%s）' % _列(sorted(v['载']), 限)
        时s = '；'.join(时[:限]) + ('等 %d' % len(时) if not 全 and len(时) > 限 else '') if 时 else ('随其载者' if 随载 else '—')
    载 = sorted(b for a, b in v['读'] if a == '载')
    引名 = set(b for a, b in v['读'] if a == '引') - set(载)
    引 = sorted(引名 | {b + '（族）' for a, b in v['读'] if a == '族' and b not in 引名 and b not in 载})   # 族＝其 glob 之族（囤灰闸._glob前缀）
    读s = '；'.join(x for x in (('载之者：' + _列(载, 限)) if 载 else '', ('引之者：' + _列(引, 限)) if 引 else '') if x) or '—'
    末s = ('第%d章' % v['末']) if v.get('末') else (('无迹（%s）' % v['迹由']) if v['类'] == '器' else '—')
    判s = '%s（%s）' % (v['判'], v['由']) + (('→' + _治文(v['治'])) if v.get('治') else
                                         ('→W908 %s 而无其限' % v['环']) if v.get('环') else '')
    if v.get('悖'):
        判s += '｜' + v['悖']
    if v['红']:
        判s = v['红'] + ' ' + 判s
    件s = v['名'] + ('（%d 档）' % v['数'] if v['类'] == '族' and v.get('数') else '')
    return [件s, v['部'] or '未归', v['职'], 跑s, 时s, 读s, 末s, 判s, v['路'], v.get('灯文') or '⚪〔—〕']


def 生(根=None, 今=None, 取=False):
    """→ (档之文, 源, 件)。今：灯之今（默此刻·自测注之）；取：迹枝之旧者先 git fetch（--摘、--件、--印、--随治；写与 --验 ⛔取）。"""
    源 = 读源(根 or ROOT)
    件 = 立件(源)
    析跑读(源, 件)
    判之(源, 件)
    今 = int(今 or time.time())
    源['今'] = 今
    try:                                         # 〔W912 环1〕⑥ 机制之流：崩即 ⓪ 书之（析崩）、余照出
        源['流图'] = 立流(源, 件)
    except Exception as e:
        源['流图'] = None
        源['崩'].append('机制之流（%s %s）' % (type(e).__name__, str(e)[:60]))
    try:                                         # 〔W912 环5〕活之色：迹取不得⛔崩——其件 ⚪「迹不可取」
        源['活迹'] = 读迹(源, 今, 取)
    except Exception as e:
        源['活迹'] = {'值': {}, '封': {}, '封末': None, '章期': None, '旧': set(), '停': False, '解停': None, '枝名': {}, '落後': 0, '迹主': {},
                    '闸免': set(), '闸红': set(), '误': '%s %s' % (type(e).__name__, str(e)[:60])}
    try:
        灯之(源, 件, 源['流图'], 今)
    except Exception as e:                       # 灯之算崩：俱 ⚪（⛔崩全图·⓪ 书之）
        源['崩'].append('活之色（%s %s）' % (type(e).__name__, str(e)[:60]))
        for v in list(件.values()) + list(((源['流图'] or {}).get('节') or {}).values()):
            v['灯'], v['灯由'] = '⚪', '灯之算崩'
            v['灯文'] = 灯文('⚪', '灯之算崩')
    return 印图(源, 件), 源, 件


def _部计(们):
    计 = lambda f: sum(1 for v in 们 if f(v))
    return [计(lambda v, j=j: v['判'] == j) for j in ('用', '半用', '未用', '死')] + [计(lambda v: v['红'] == '⛔'), 计(lambda v: v['红'] == '⚠')]


def 印图(源, 件):
    计 = lambda 们, f: sum(1 for v in 们 if f(v))
    全 = list(件.values())
    器们 = [v for v in 全 if v['类'] == '器']
    账们 = [v for v in 全 if v['类'] in ('账', '族')]
    族们 = [v for v in 账们 if v['类'] == '族']
    未归 = sorted(k for k, v in 件.items() if not v['部'])
    无职 = [k for k, v in 件.items() if v['职'].startswith('（无')]
    迹外 = sorted(x for x in 源['迹'] if x not in 源['器'])
    名单 = 源['W908']
    名单无 = sorted(k for k in 名单['表'] if k not in 件)
    封, 测, 可 = 源.get('封版'), 源.get('全测'), 源.get('可达')
    格无函 = sorted(k for k, g in (测 or {}).items() if not g['在'])
    钩数 = sum(len(g.get('hooks') or []) for 们 in (源['钩'] or {}).values() for g in 们 or [])
    器崩 = [x for x in 源['崩'] if re.fullmatch(r'工具/[^/（]+\.py', x)]
    红 = sorted((v for v in 全 if v['红'] == '⛔'), key=lambda v: v['名'])
    警 = sorted((v for v in 全 if v['红'] == '⚠'), key=lambda v: v['名'])
    合 = _部计(全)
    流, 近 = 源.get('流图'), 源.get('近') or []
    流节 = list((流 or {}).get('节', {}).values())
    L = ['# 体系总图（心—脉—觉—长—学·一件一行·用之审入图）', '', 首行, '',
         '## 一眼', '',
         '- 截至第 %d 章（正文之末章）；末真用之窗：%s。' % (源['末章'], ('第%d—%d章之 _器之迹.md' % (源['迹章'][0], 源['迹章'][-1])) if 源['迹章'] else '无迹'),
         '- 件 %d＝器 %d、席 %d、流 %d、账 %d｜用 %d、半用 %d、未用 %d、死 %d｜⛔ %d、⚠ %d' % (
             len(全), len(器们), len(源['席']), len(源['流']), len(账们), *合),
         '- ' + '｜'.join('%s %d（用 %d·半 %d·未 %d·死 %d%s）' % (部, len(们), *c[:4], ('·⛔ %d' % c[4]) if c[4] else '')
                          for 部, 们, c in ((部, 们, _部计(们)) for 部, 们 in ((部, [v for v in 全 if v['部'] == 部]) for 部 in 部序 + ((None,) if 未归 else ())))
                          if 们).replace('None', '未归'),
         '- ⛔ 即红 %d%s' % (len(红), ('：' + '、'.join('%s（%s）' % (v['名'], v['判']) for v in 红)) if 红 else '：无'),
         '- ⚠ 随治、候审 %d（W908 之治而未逾限 %d、账之机判未用 %d）——逐件见 ③' % (
             len(警), 计(警, lambda v: bool(v.get('治'))), 计(警, lambda v: not v.get('治'))),
         '- 机制之流（⑥）：节 %d、边 %d（机取 %d、表 %d）%s——mermaid（GitHub 即绘）与文本之链见 ⑥' % (
             len(流节), len(流['边']), 流['机'], 流['表'], ('；⛔ 流之边失据 %d' % len(流['失据'])) if 流['失据'] else '；流之边俱有据')
         if 流 else '- 机制之流（⑥）：流之构不得（见 ⓪）',
         '- 近之进化之末（⑦）：%s' % (('%s %s「%s」（%s）——%s' % (近[0][0], 近[0][2], 近[0][1][:24], 近[0][3], 近[0][4][:48])) if 近 else '无（工作流账无 W9xx 之裁）'),
         '- 灯（今算·--验 ⛔比·跑即亮）：件 %s；流之节 %s%s' % (_灯计文(全), _灯计文(流节), ('；' + 灯文('🔴', '、'.join(
             [x['名'] for x in 流节 if x.get('灯') == '🔴' and not x['件']] + [v['名'] for v in 全 if v.get('灯') == '🔴'])))
             if any(x.get('灯') == '🔴' for x in 流节 + 全) else ''),
         '- 读法·判：照 W908「用之审之果」；名单外者机判（有跑且有读＝用、有一缺＝半用、俱无＝未用）。「悖」＝判死／未用而仍有跑口；'
         '「今迹见……候复审」＝名单判半用而今迹已见。⛔＝器红级（全测之格「体系总图」报之、入器红账，⛔拦写书之封）；⚠＝只报。',
         '- 读法·末真用：末十章 _器之迹.md 所见。其迹只录写书之坐「料成→器之迹之步」之跑（_账 记 __main__）——GitHub、他坐、封版闸後、'
         '被载者俱不入，故「无迹」必书其由：迹盲（其跑俱在盲处）／窗外末见第N章／全迹无。',
         '- 读法·谁跑谁读：「（印令）」＝只印其令（自走、封毕之语）而主环照跑；「（载）」＝被 import；「（唯自测）」＝全测只跑其 --自测。'
         '载之者＝import 之者，引之者＝提其名之档。格中「等 N」者，`python3 工具/体系总图.py --件 名` 见其全。', '']
    # ⓪
    封数 = ''
    if 封:
        封数 = '--前 调器 %d；--後 调器 %d（步 %d、闸 %d〔含左移之拦 %d〕、存 %d 去重）、载 %d、印令 %d——三者之名见 ① 封版之序' % (
            len(封['前']), len(封['後']), len(封['序']['後·步']), len(封['序']['後·闸']) + len(封['序']['後·拦']), len(封['序']['後·拦']),
            len(封['序']['後·存']), len([m for m in 封['载後'] if m + '.py' in 源['器'] and m != '封版']), len(封['印後']))
    L += ['## ⓪ 源之鲜', '', '| 源 | 所至 | 不识／缺 |', '|---|---|---|',
          '| 器 `工具/*.py` | %d 件（常驻自驱 %d：%s） | 析崩 %d%s；无 docstring %d |' % (
              len(器们), 计(器们, lambda v: bool((v.get('析') or {}).get('驱'))),
              _列(sorted(v['名'][:-3] for v in 器们 if (v.get('析') or {}).get('驱'))),
              len(器崩), ('：' + _列(器崩, 6)) if 器崩 else '', 计(器们, lambda v: v['职'].startswith('（无'))),
          '| 席 `工具/席/*.js` | %d 件 | — |' % len(源['席']),
          '| 流 `.github/workflows/*.yml` | %d 件（触与调见 ① GitHub 之流） | — |' % len(源['流']),
          '| 钩 `.claude/settings.json` | 事 %d、钩 %d | %s |' % (len(源['钩'] or {}), 钩数, '缺或坏' if 源['钩'] is None else '—'),
          '| git 钩 `工具/githooks/*` 与 merge 驱 | %d 件（%s）；merge 驱 %d | — |' % (len(源['git钩']), _列(sorted(源['git钩'])), len(re.findall(r'merge=\S+', 源['属']))),
          '| 账册 `设定/` | json %d、md %d、子目 %d → 行 %d（单档 %d、族 %d 含档 %d） | 无首题／说明之键 %d |' % (
              len([x for x in 源['账'] if x.endswith('.json')]), len([x for x in 源['账'] if x.endswith('.md')]), len(源['子目']), len(账们),
              len(账们) - len(族们), len(族们), sum(v.get('数', 0) for v in 族们), len([k for k in 无职 if 件[k]['类'] in ('账', '族')])),
          '| 封版 `工具/封版.py` | %s | %s |' % (封数 or '—', '—' if 封 else '缺或析崩'),
          '| 全测 `工具/全测.py` | %s | %s |' % (('格 %d、格所跑之器 %d（唯取调；只印之示⛔算）' % (len(测), len(set(x for g in 测.values() for x in g['器'])))) if 测 else '—',
                                            ('格之函寻不着 %d：%s' % (len(格无函), _列(格无函))) if 格无函 else ('—' if 测 else '缺或析崩')),
          '| 入口 `工具/囤灰闸.py` | 真跑口 %d；闭包可达 %s | %s |' % (len(源['入口']), ('%d／%d' % (len(可[0]), len(可[1]))) if 可 else '—',
                                                            ('囤灰 %d：%s' % (len(可[1] - 可[0]), _列(sorted(可[1] - 可[0])))) if 可 and 可[1] - 可[0] else ('—' if 可 else '析崩')),
          '| 读者 | %d（器 %d、席、流、钩、git 钩、总章、README、总圣经、canon；⛔本器） | — |' % (len(源['读者']), len([x for x in 源['读者'] if '·' not in x and x not in ('钩', '总章') and x not in 源['他读']])),
          '| 账之读 `囤灰闸.档之囤灰`（一义一判） | glob 之族而读 %d 件；顶层 md 无引 %d（日＝0 核之） | %s |' % (
              计(账们, lambda v: any(a == '族' for a, _ in v['读'])), 计(账们, lambda v: v['名'].endswith('.md') and not v['读']),
              '；'.join(x for x in (('囤灰闸认有引而本图寻不着读者 %d（书「活档」）：%s' % (len(源.get('活档补') or []), _列(源['活档补'], 6))) if 源.get('活档补') else '',
                                   ('本图有读而囤灰闸认无引 %d：%s' % (len(源['判异']), _列(源['判异'], 6))) if 源.get('判异') else '') if x) or '—'),
          '| 器之迹 `版本/第N章/_器之迹.md` | %s | %s |' % (('窗 第%d—%d章 %d 档、器 %d 名；全迹 %d 档、器 %d 名' % (
              源['迹章'][0], 源['迹章'][-1], len(源['迹章']), len(源['迹']), 源['迹档数'], len(源['迹全']))) if 源['迹章'] else '无',
              ('窗中之器而盘上已无 %d：%s（临时之码或已删之器·⛔入件）' % (len(迹外), _列(迹外))) if 迹外 else '—'),
          '| W908 用之审之名单 `设定/方案/W908.md`（该节之机读之块） | %s | %s |' % (
              ('件 %d（块之行：器 %d、账 %d；判照之，与今机判之对照见 ③）；甲批 %s、乙批 %s' % (
                  len(名单['表']), *名单['数'], '、'.join(sorted((k for k, b in 名单['批'].items() if b == '甲'), key=lambda x: int(x[1:]))) or '—',
                  '、'.join(sorted((k for k, b in 名单['批'].items() if b == '乙'), key=lambda x: int(x[1:]))) or '—')) if 名单['在'] else '—',
              '；'.join(x for x in (('盘上无（已除）%d：%s' % (len(名单无), _列(名单无, 12))) if 名单无 else '',
                                   ('块之误 %d（见「析不得」）' % len(名单['误'])) if 名单['误'] else '', '' if 名单['在'] else '档缺') if x) or '—'),
          '| 部之表（本器） | 已归 %d | %s |' % (len(件) - len(未归), ('未归 %d：%s' % (len(未归), _列(未归, 12))) if 未归 else '—'),
          '| 法用册 `设定/法用册.json` | %s | %s |' % (('法 %d、待 %d、废 %d；W908 治之限：废之条 %d 档、待「用之审」限 %s' % (
              源['法']['法'], 源['法']['待'], 源['法']['废'], len(源['废治']), 源['审限'] or '无')) if 源['法'] else '—', '—' if 源['法'] else '读不得'),
          '| 机制之流 `本器之流节、流边之表`＋流之 on／if＋`接棒守` 之表 | %s | %s |' % (
              ('节 %d、边 %d（机取 %d：流之 on／job 之 if／uses、兜底之令%s；表 %d：逐边验其串在其档）；接棒守 之表 %s' % (
                  len(流节), len(流['边']), 流['机'], '、钟之令' if '钟' in 流['节'] else '', 流['表'],
                  '、'.join(k for k in _接表之键 if k in (源.get('接表') or {})) or '读不得')) if 流 else '—',
              ('⛔ 流之边失据 %d：%s' % (len(流['失据']), _列(流['失据'], 3))) if 流 and 流['失据'] else ('—' if 流 else '析崩（见下）')),
          '| 迹之源（活之色） `本器之迹表` | 源 %d 类：%s | 灯以本地 origin/* 算（--摘、--件、--印、--随治 先取其旧者；写、--验 ⛔取；'
          'ZM_TU_NOFETCH=1 即⛔取）；取不得之件 ⚪「迹不可取」（⛔猜） |' % (len(_迹之源), '、'.join(_迹之源)),
          '| 工作流账 `设定/工作流账.json` | %s | %s |' % (('W9xx 之裁之末 %d（⑦）' % len(近)) if 源.get('近') is not None else '—',
                                                    '—' if 源.get('近') is not None else '读不得')]
    for x in [y for y in 源['崩'] if y not in 器崩]:
        L.append('| （析不得） | — | %s |' % _格(x))
    if 源['缺']:
        L.append('| （缺） | — | %s |' % _列(源['缺'], 9))
    L.append('')
    # ①
    L += ['## ① 五部之脊', '', '| 部 | 其职 | 件 | 器／席／流／账 | 用 | 半用 | 未用 | 死 | ⛔ | ⚠ |', '|---|---|---|---|---|---|---|---|---|---|']
    for 部 in 部序 + (None,):
        们 = [v for v in 全 if v['部'] == 部]
        if 部 is None and not 们:
            continue
        L.append('| %s | %s | %d | %d／%d／%d／%d | %d | %d | %d | %d | %d | %d |' % (
            部 or '未归', 部之职.get(部, '部之表未归之件（⛔猜）'), len(们), 计(们, lambda v: v['类'] == '器'), 计(们, lambda v: v['类'] == '席'),
            计(们, lambda v: v['类'] == '流'), 计(们, lambda v: v['类'] in ('账', '族')), *_部计(们)))
    L.append('| 合 | — | %d | %d／%d／%d／%d | %d | %d | %d | %d | %d | %d |' % (len(全), len(器们), len(源['席']), len(源['流']), len(账们), *合))
    L.append('')
    if 封:
        L += ['### 封版之序（静析 `工具/封版.py`；⛔＝红即停、⚠＝只报不拦、〔若…〕＝其条件、并〔…〕＝并起）', '',
              '- --前：%s%s' % ('→'.join(x[:-3] for x in 封['序']['前']) or '—', ('（并起：%s）' % '、'.join(x[:-3] for x in 封['序']['前·并'])) if 封['序']['前·并'] else '')]
        L += ['- --後·%s：%s' % (组, 文) for 组, 文 in 封['序']['後·全']] or ['- --後：—']
        载 = sorted(m for m in 封['载後'] if m + '.py' in 源['器'] and m != '封版')
        L += ['- --後 所载之库（import·随其函）：%s；所印之令：%s' % ('、'.join(载) or '—', '、'.join(sorted(x[:-3] for x in 封['印後'])) or '—'), '']
    if 源['流']:
        L += ['### GitHub 之流（静析 `.github/workflows/*.yml`：调＝非注、非 echo 之行中 python3 所调之器与 `uses:` 之流）', '',
              '| 流 | 部 | 职 | 触 | 调 |', '|---|---|---|---|---|']
        for x in sorted(源['流']):
            调 = ['%s%s' % (y[:-3] if y.endswith('.py') else y, ('（%s）' % '、'.join(z[:-3] for z in 源['流调'].get(y, []) if z.endswith('.py')))
                             if y.endswith('.yml') and 源['流调'].get(y) else '') for y in 源['流调'].get(x, [])]
            v = 件.get(x) or {}
            L.append('| %s | %s | %s | %s | %s |' % (x, v.get('部') or '未归', _格(v.get('职', '')), _格(源['触'].get(x, '—')), '、'.join(调) or '—'))
        L.append('')
    # ②
    L += ['## ② 一件一行', '']
    for 部 in 部序 + (None,):
        们 = sorted((v for v in 全 if v['部'] == 部), key=lambda v: ('器席流账族'.index(v['类']), v['名']))
        if not 们:
            continue
        L += ['### %s（%d）' % (部 or '未归', len(们)), '', '| 件 | 部 | 何职 | 谁跑 | 何时跑 | 谁读其出 | 末真用 | 判 | 其源档 | 灯 |',
              '|---|---|---|---|---|---|---|---|---|---|']
        L += ['| ' + ' | '.join(_格(x) for x in 行之文(v)) + ' |' for v in 们]
        L.append('')
    # ③
    L += ['## ③ 用之审之红', '',
          '> 未用、死者逐件列。⛔（器红级：全测之格「体系总图」报之、入器红账，⛔拦写书之封）：器之机判未用、名单之死而无治、甲批之治而无限、逾其限者。'
          '⚠：随 W908 之治而未逾其限者（限取 法用册：废之条之限先之；无则甲批取 待「用之审」之限，乙批无专限只 ⚠）；'
          '接入之治已行而今机判用者（候复审）；账之机判未用（候审·同 囤灰闸.档之囤灰「只报」）。', '',
          '- ⛔ 即红 %d%s' % (len(红), '' if 红 else '：无')]
    for v in 红:
        L.append('  - ⛔ %s（%s·%s）——%s' % (v['名'], v['判'], v['由'], ('逾限：' + _治文(v['治'], '')) if v.get('治')
                                           else ('W908 %s 而法用册无其限：入废带限或接之' % v['环']) if v.get('环') else '无治：废之或接之，书其治'))
    L.append('- ⚠ 随治、候审 %d%s' % (len(警), '' if 警 else '：无'))
    for v in 警:
        L.append('  - ⚠ %s（%s·%s）——%s%s' % (v['名'], v['判'], v['由'], _治文(v['治']) if v.get('治') else
                                             '治已行' if v.get('治行') else '候审：废之、接之或书其由',
                                             ('｜' + v['悖']) if v.get('悖') else ''))
    L.append('')
    名单 = 源['W908']['表']
    对 = [件[k] for k in 名单 if k in 件]
    L += ['### W908 名单之对照（原判｜今之机判｜今态｜治）', '',
          '> W908「用之审之果」之名单 %d 名：死、未用者俱列；半用、用者唯列今之迹、跑与之相抵者（候复审）。' % len(名单), '',
          '| 件 | 原判（W908 之由） | 今之机判 | 今态（谁跑之摘·末真用） | 治 |', '|---|---|---|---|---|']
    序 = {'死': 0, '未用': 1, '半用': 2, '用': 3}
    for v in sorted(对, key=lambda v: (序.get(v['判'], 9), v['类'] != '器', v['名'])):
        if v['判'] in ('半用', '用') and not v.get('悖'):
            continue
        态 = ('账·%s' % 行之文(v)[5]) if v['类'] in ('账', '族') else \
            '%s；%s' % (_列(sorted(set(a for a, _ in v['跑'])), 3) if v['跑'] else '无跑口', 行之文(v)[6])
        if (v.get('悖') or '').startswith('悖'):
            态 += '｜悖'
        elif v.get('治行'):
            态 += '｜治已行'
        L.append('| %s | %s（%s） | %s | %s | %s |' % (v['名'], v['判'], _格(v['由'][5:]), v['机判'], _格(态),
                                                   _治文(v['治'], '') if v.get('治') else ('W908 %s·无其限' % v['环']) if v.get('环') else '无'))
    L.append('')
    L += 印流(源, 件) + 印近(源)
    # ☁
    卡 = 源['卡']
    L += ['## ☁ GitHub 之卡（报/卡.json·随 备份/报 而变，--验 ⛔比）', '']
    if 卡:
        流 = 卡.get('流') if isinstance(卡.get('流'), dict) else {}
        L.append('%s 报/卡.json：在（算於 %s；末 run %s）' % (云记, 卡.get('算於', '?'), 卡.get('末 run id', 卡.get('末', '?'))))
        for k in sorted(流):
            v = 流[k]
            L.append('%s %s：分 %s' % (云记, k, v.get('分', '?') if isinstance(v, dict) else v))
    else:
        L.append('%s 报/卡.json：卡未立（W908 环5·乙批方立；或本地未取 备份/报）' % 云记)
    L.append('')
    return '\n'.join(L)


# ═══ 令 ═══
_灯式 = re.compile(r'[🟢🟡🔴⚪](?:〔[^〕\n]*〕| \d+)?')
_色行式 = re.compile(r'^\s*class [\w,]+ l[gyrw]\s*$')
_红尾式 = re.compile(r'；🔴〔[^〕\n]*〕$')      # 一眼之灯行：有 🔴 方附其名（红与不红之翻⛔作档旧）


def _比之文(文):
    """--验 之比：☁ 之行、灯（🟢〔…〕之符与其数）、一眼之红名之尾（「；🔴〔…〕」·有红方附）、mermaid 之 class 行（灯之色）⛔比——
    随时、随 origin/* 而变，非档之旧。"""
    return [_灯式.sub('灯', _红尾式.sub('', l)) for l in (文 or '').split('\n') if not l.startswith(云记) and not _色行式.match(l)]


def 败图(根, 迹):
    """器崩之最小之图：「截至第 N 章」（N＝正文之末章，以文件名之汉数计；⛔依囤灰闸——其或即崩之源）、⓪ 书器败与迹之末。"""
    _数 = {'零': 0, '〇': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}

    def 汉(t):
        n, 段 = 0, 0
        for ch in t:
            if ch in _数:
                段 = _数[ch]
            elif ch in '十百千':
                n += (段 or 1) * {'十': 10, '百': 100, '千': 1000}[ch]
                段 = 0
        return n + 段
    末 = max([汉(m.group(1)) for f in glob.glob(os.path.join(根, '正文', '*.md'))
             for m in [re.search(r'第([零〇一二两三四五六七八九十百千]+)章', os.path.basename(f))] if m] or [0])
    尾 = '\n'.join((迹 or '').strip().split('\n')[-6:])
    return ('# 体系总图（器败·最小之图）\n\n- 截至第 %d 章（正文之末章）；⛔ 器败：工具/体系总图.py 生图时崩——五部、一件一行、用之红俱缺；治器後由下一封版重生。\n\n'
            '## ⓪ 源之鲜\n\n- ⛔ 器败：\n\n```\n%s\n```\n' % (末, 尾))


def 写(根=None, 取=False):
    """封版 --後 之步与总编辑之治（--随治）——两写者：封版 --後 与总编辑之治（--随治）；两写之并由 账并 之生成之图一支（取 ours·⚠ 待下回重生）。
    rc 恒 0（⛔拦封），析崩只印——全测之格「体系总图」红之。取：迹枝之旧者先取（--随治；封版之步⛔取·⛔拖累写书）。"""
    根 = 根 or ROOT
    p = os.path.join(根, 图名)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    try:
        文, 源, 件 = 生(根, 取=取)
    except Exception:                    # 〔1119·法用#体系总图之行为之证〕器崩亦写最小之图——题照末章、⓪书器败；rc 1 而封版之步非必：⛔拦封
        import traceback
        with open(p, 'w', encoding='utf-8') as f:
            f.write(败图(根, traceback.format_exc()))
        print('⛔ 体系总图 器败——已写最小之图（截至末章、⓪书其迹）；治器後由下一封版重生')
        return 1
    with open(p, 'w', encoding='utf-8') as f:
        f.write(文)
    计 = lambda 判: sum(1 for v in 件.values() if v['判'] == 判)
    print('✓ 写 %s：件 %d（用 %d、半用 %d、未用 %d、死 %d）｜用之红 %d｜析崩 %d（全测之格「体系总图」报之）' % (
        图名, len(件), 计('用'), 计('半用'), 计('未用'), 计('死'), sum(1 for v in 件.values() if v['红'] == '⛔'), len(源['崩'])))
    for x in 源['崩']:
        print('  ⚠ 析崩：%s' % x)
    return 0


_核心之源 = ('工具/封版.py', '工具/全测.py')        # 缺即红（与析崩同）：封版之序、全测之格俱出其中


def 验(根=None):
    根 = 根 or ROOT
    print('════ 体系总图·验 ════')
    文, 源, 件 = 生(根)
    旧 = _读(os.path.join(根, 图名))
    if 旧 is None:
        print('  ⚠ 档旧：%s 不在——封版 --後 与总编辑之治（--随治）生之；两写之并由 账并 之生成之图一支——欲看即 --印（⛔写）' % 图名)
    else:
        a, b = _比之文(旧), _比之文(文)
        if a == b:
            print('  ✓ 不旧：%s 与今盘再生逐字同（☁ 之行⛔比）' % 图名)
        else:
            i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
            x, y = _异窗(a[i] if i < len(a) else '（无）', b[i] if i < len(b) else '（无）', 50)
            print('  ⚠ 档旧：首异在第 %d 行（档「%s」｜今「%s」）——封版 --後 与总编辑之治（--随治：python3 工具/体系总图.py --随治）重写；'
                  '两写之并由 账并 之生成之图一支' % (i + 1, x, y))
    for x in ((源.get('流图') or {}).get('失据') or []):
        print('  ⚠ 流之边失据：%s（⓪ 书之、其边书虚线）' % x)
    崩 = list(源['崩']) + ['%s（缺·核心之源）' % x for x in 源['缺'] if x in _核心之源]
    for x in 崩:
        print('  ⛔ 析崩：%s（⓪ 书之，余照出；析崩即红）' % x)
    for x in 源['缺']:
        if x not in _核心之源:
            print('  ⚠ 源缺：%s（⓪ 书之）' % x)
    红 = sorted((v for v in 件.values() if v['红'] == '⛔'), key=lambda v: v['名'])
    for v in 红:
        print('  ⛔ ③用之红：%s（%s·%s）——%s' % (v['名'], v['判'], v['由'], ('逾 ' + _治文(v['治'], '')) if v.get('治')
                                               else ('W908 %s 而法用册无其限' % v['环']) if v.get('环') else '无治：废之或接之'))
    print('  %s 件 %d｜用之红 %d｜析崩 %d｜随治、候审 %d' % ('⛔' if 红 or 崩 else '✓', len(件), len(红), len(崩),
                                                  sum(1 for v in 件.values() if v['红'] == '⚠')))
    return 1 if 红 or 崩 else 0


def 一件(名, 根=None):
    文, 源, 件 = 生(根 or ROOT, 取=可取())
    候 = [k for k in sorted(件) if 名 in (k, 件[k]['路']) or k in (名 + '.py', 名 + '.md', 名 + '.json', 名.rstrip('/') + '/')]
    if not 候:
        print('⛔ 无此件：%s（名：存底守、法用册.json、设定/段案/……）' % 名)
        return 1
    v = 件[候[0]]
    for h, x in zip(('件', '部', '何职', '谁跑', '何时跑', '谁读其出', '末真用', '判', '其源档', '灯'), 行之文(v, 全=True)):
        print('%-6s %s' % (h, x))
    if v['类'] == '流':
        print('%-6s %s' % ('所调', '、'.join(源['流调'].get(候[0], [])) or '—'))
    for a, b in sorted(v['跑']):
        print('  · 跑：%s｜%s' % (a, b))
    if v.get('员'):
        print('  · 族员 %d：%s' % (len(v['员']), _列(v['员'], 12)))
    return 0


def _异窗(x, y, 宽=30):
    """二行之首异处之窗（⛔只示同首：首异在行中者自其前八字起）。"""
    j = next((k for k in range(min(len(x), len(y))) if x[k] != y[k]), min(len(x), len(y)))
    k = max(0, j - 8)
    return ('…' if k else '') + x[k:k + 宽], ('…' if k else '') + y[k:k + 宽]


def _名由(们, 限=170, 由长=18):
    """[件] → 「名（由）、…」·至多 限 字，余书「等 N」。"""
    出, n = '', 0
    for v in 们:
        x = '%s（%s）' % (v['名'], _去括(re.sub(r'^(W908：|机判：)', '', v['由'])).strip()[:由长])
        if 出 and len(出) + len(x) > 限:
            break
        出 += ('、' if 出 else '') + x
        n += 1
    return (出 + ('等 %d' % len(们) if n < len(们) else '')) or '无'


def 摘(根=None, 今=None, 取=None):
    """执行之查之据（W912 环4）：今树即算（⛔读旧档之数）——一眼之数、⛔即红、🔴🟡 之件与其由、⚠ 之件、半用／未用之件各带其由、
    图档旧否与首异·≤25 行。→ [行]。"""
    根 = 根 or ROOT
    今 = int(今 or time.time())
    t0 = time.time()
    文, 源, 件 = 生(根, 今, 取=可取() if 取 is None else 取)
    全 = sorted(件.values(), key=lambda v: v['名'])
    流 = 源.get('流图') or {'节': {}, '边': [], '失据': [], '机': 0, '表': 0}
    节们 = [流['节'][k] for k in 流.get('序', [])]
    计 = lambda f: sum(1 for v in 全 if f(v))
    红 = [v for v in 全 if v['红'] == '⛔']
    警 = [v for v in 全 if v['红'] == '⚠']
    活 = 源.get('活迹') or {}
    注 = ''.join(x for x in (('·树落後主枝 %d 提交（封、迹取主枝）' % 活['落後']) if 活.get('落後') else '',
                            '·暂停中（随写书与兜底之期 ⚪·⛔当跑）' if 活.get('停') else '') if x)
    L = ['体系总图·摘（今算·截至第 %d 章·%s UTC·⛔读旧档%s）' % (源['末章'], _刻(今), 注),
         '件 %d：用 %d、半用 %d、未用 %d、死 %d｜⛔ %d、⚠ %d｜灯 %s' % (len(全), 计(lambda v: v['判'] == '用'), 计(lambda v: v['判'] == '半用'),
                                                         计(lambda v: v['判'] == '未用'), 计(lambda v: v['判'] == '死'), len(红), len(警), _灯计文(全)),
         '流：节 %d、边 %d（机 %d、表 %d%s）｜流之节之灯 %s' % (len(节们), len(流['边']), 流['机'], 流['表'],
                                                  ('·⛔失据 %d' % len(流['失据'])) if 流['失据'] else '', _灯计文(节们)),
         '⛔ 即红 %d：%s' % (len(红), '、'.join('%s（%s）' % (v['名'], v['判']) for v in 红) if 红 else '无')]
    for g, 题, 限 in (('🔴', '当跑而未跑或末跑败', 6), ('🟡', '迟', 4)):
        诸 = [(x['名'], x['灯由']) for x in 节们 if x.get('灯') == g and not x['件']] + [(v['名'], v['灯由']) for v in 全 if v.get('灯') == g]
        L.append('%s %s %d%s' % (g, 题, len(诸), '' if 诸 else '：无'))
        L += ['  %s %s：%s' % (g, a, b) for a, b in 诸[:限]] + (['  …另 %d（python3 工具/体系总图.py --件 名）' % (len(诸) - 限)] if len(诸) > 限 else [])
    L.append('⚠ 随治、候审 %d：%s' % (len(警), _列([v['名'] for v in 警], 8)))
    L.append('半用 %d：%s' % (计(lambda v: v['判'] == '半用'), _名由([v for v in 全 if v['判'] == '半用'])))
    L.append('未用 %d：%s' % (计(lambda v: v['判'] == '未用'), _名由([v for v in 全 if v['判'] == '未用'])))
    旧 = _读(os.path.join(根, 图名))
    if 旧 is None:
        L.append('图档：⚠ 不在——python3 工具/体系总图.py --随治（总编辑之治）或候下一封版')
    else:
        a, b = _比之文(旧), _比之文(文)
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), None if len(a) == len(b) else min(len(a), len(b)))
        if i is None:
            L.append('图档：✓ 不旧（与今树再生同·灯与 ☁ ⛔比）')
        else:
            x, y = _异窗(a[i] if i < len(a) else '（无）', b[i] if i < len(b) else '（无）')
            L.append('图档：⚠ 旧·方法已变——首异第 %d 行（档「%s」｜今「%s」）→ python3 工具/体系总图.py --随治' % (i + 1, x, y))
    if 流['失据']:
        L.append('⛔ 流之边失据 %d：%s' % (len(流['失据']), _列(流['失据'], 2)))
    近 = 源.get('近') or []
    if 近:
        L.append('近之进化之末：%s %s「%s」（%s）' % (近[0][0], 近[0][2], 近[0][1][:20], 近[0][3]))
    红灯 = sum(1 for x in 节们 if x.get('灯') == '🔴' and not x['件']) + 计(lambda v: v.get('灯') == '🔴')
    L.append('%s 摘：用之红 %d、⚠ %d、🔴 %d、析崩 %d（%.1f 秒）' % ('⛔' if 红 or 红灯 or 源['崩'] else '✓', len(红), len(警), 红灯,
                                                           len(源['崩']), time.time() - t0))
    return L[:24] + L[-1:] if len(L) > 25 else L


def 图之数(根=None, 今=None):
    """→ {'红', '警', '🔴', '🟡', '崩'}（今树即算·⛔取：法用之守 --报 之末行用之·⛔另析）。"""
    _, 源, 件 = 生(根 or ROOT, 今, 取=False)
    节们 = [x for x in ((源.get('流图') or {}).get('节') or {}).values() if not x['件']]
    数 = lambda g: sum(1 for v in list(件.values()) + 节们 if v.get('灯') == g)
    return {'红': sum(1 for v in 件.values() if v['红'] == '⛔'), '警': sum(1 for v in 件.values() if v['红'] == '⚠'),
            '🔴': 数('🔴'), '🟡': 数('🟡'), '崩': len(源['崩'])}


def 随治(根=None):
    """总编辑之治（W912 环2③）：方法一变图即随——唯总编辑之坐（接棒守.总编辑）写，他坐 rc 2 拒（写书之坐之图随封版 --後）。
    两写者（封版 --後、总编辑之治）之并由 账并 之生成之图一支：两侧俱改图即取 ours、⚠ 待下回重生（坑63 之由即去）。"""
    根 = 根 or ROOT
    总 = _去前(接棒之表(根).get('总编辑'))
    坐 = 本坐()
    if not 总 or 坐 != 总:
        print('⛔ --随治 唯总编辑之坐（接棒守.总编辑 %s）；本坐 %s——写书之坐之图随封版 --後，⛔手写' % (总 or '读不得', 坐 or '未名'))
        return 2
    return 写(根, 取=可取())


# ═══ 自测 ═══
_样代 = (('〔跑〕', 'python3 '), ('〔欠哨〕', '看官欠' + '哨'), ('〔进化树〕', '进化' + '树'))


def _样W908(多=''):
    """小样之 W908：上文之列（器四判、复核之题、账册页二判）、机读之块、分批之行——多＝添於上文「死」之名（块与上文异之局）。"""
    P = lambda 干: '工具/' + 干 + '.py'
    行 = lambda 原, 件, 判, 环, 治: {'原': 原, '件': 件, '判': 判, '由': '样之由', '环': 环, '治': 治}
    块 = {'器': [行('外声闸', [P('外声闸')], '半用', '环8', '接入'), 行('〔进化树〕', [P('〔进化树〕')], '半用', None, None),
                行('接入样', [P('接入样')], '未用', '环8', '接入'), 行('乙样', [P('乙样')], '未用', '环7', '接入'),
                行('〔欠哨〕', [P('〔欠哨〕')], '死', '环7', '废'), 行('甲样', [P('甲样')], '死', '环1', '废'),
                行('迹器', [P('迹器')], '用', None, None)],
          '账': [行('死样账', ['设定/死样账.json'], '死', None, None), 行('样账', ['设定/样账.md'], '半用', None, None),
                行('报/样', [], '半用', None, None)]}
    return ('# 方案·W908（样）\n\n## 由\n\n- 样。\n\n## 用之审之果\n\n### 所造\n\n'
            '- **器**（样）：用 1、半用 2、未用 2、死 2。\n  - **半用 2**：\n    - 外声闸（恒 True，全测:1-2）\n    - 〔进化树〕（未经一封之随）\n'
            '  - **未用 2**：\n    - 接入样（迹窗无真跑）\n    - 乙样（不入全测）\n  - **死 2**：\n    - 〔欠哨〕（看官之账冻）\n    - 甲样（事毕）\n%s'
            '  - **用而有疵 1**：\n    - 迹器：有疵之样。\n  - **复核驳去一判**：\n    - 孤器非死。\n'
            '- **账册页**（3 行）：死 1、半用 2。\n  - **死 1**：死样账（冻、无读）。\n  - **半用 2**：样账（用-乙之审）、报/样。\n'
            '- **GitHub 之物**：\n  - 流俱用。\n\n### 机读之块\n\n```json 用之审\n%s\n```\n\n## 逐环\n\n| 环 | 做什么 |\n|---|---|\n\n'
            '## 裁\n\n**分批**：\n- 甲批（今即·样）：环1、环8——互不相交之档。\n- 乙批（W907 入主後）：环7、环9（样）。\n'
            % (多, json.dumps(块, ensure_ascii=False)))


def _造仓(t, 去=()):
    """小样之仓：封版、全测、流、钩、席、账、迹、正文——去 者⛔立（源缺之局）。⛔真器之全名入本器之文；样之令以「〔跑〕」代其解释器之名、
    名单之器以「〔欠哨〕」「〔进化树〕」代其干，落盘方复（⛔死处方哨、处方旗哨 误认本器开死处方；⛔囤灰闸 误认本器引名单之器）。"""
    def 落(p, s):
        if any(p.startswith(x) for x in 去):
            return
        os.makedirs(os.path.dirname(os.path.join(t, p)), exist_ok=True)
        for a, b in _样代:
            s, p = s.replace(a, b), p.replace(a, b)
        os.makedirs(os.path.dirname(os.path.join(t, p)), exist_ok=True)
        open(os.path.join(t, p), 'w', encoding='utf-8').write(s)
    落('工具/封版.py', '"""封版——docstring 提 甲注.py ⛔算。"""\nimport os, json, subprocess\n分栏之始 = 411\n'
                     "def 器(n):\n    return n\n"
                     "def 跑(a, r=None):\n    return 0, '', 0\n"
                     "def 正文档(n):\n    from 甲库 import 章号\n    return 章号\n"
                     "def 前(n):\n    正文档(n)\n    跑([器('甲前.py'), str(n)])  # 注里 乙注.py ⛔算\n"
                     "def 慢检并起(n):\n    跑([器('甲慢.py')])\n"
                     "def 记之缺(n):\n    import 记缺库\n    return []\n"
                     "def 活态之报(n):\n    跑([器('全测.py'), '--只', ','.join(活态之格)])\n"
                     "def 泊之语(n):\n    import 泊库\n    return '泊'\n"
                     "def 封毕之语(n):\n    return '下一步：〔跑〕工具/印器.py --候 %d' % n\n"
                     "def 後(n, 演=False):\n    缺 = 记之缺(n)\n    if 缺:\n        print('缺')\n        return False\n"
                     "    步 = [('甲步', [器('甲後.py'), '--随'], False), ('二步', [器('乙後.py')], True)]\n"
                     "    for 名, a, 必 in 步:\n        if 必 and 跑(a)[0]:\n            return False\n"
                     "    闸 = 後之闸(n)\n    for 名, a in 闸:\n        if 跑(a)[0]:\n            return False\n"
                     "    p = os.path.join('版本', '_席记.json')\n    j = json.load(open(p))\n    j.setdefault('段', {})['封版'] = '过'\n"
                     "    活态之报(n)\n    if 演:\n        return True\n"
                     "    subprocess.run(['git', 'commit', '-m', 'x'])\n"
                     "    for 名, a in 後之存(n):\n        跑(a)\n"
                     "    print(泊之语(n))\n    print(封毕之语(n))\n    return True\n"
                     "def 後之闸(n):\n    闸 = [('囤灰闸', [器('丙闸.py')])]\n    if n >= 分栏之始:\n        闸.append(('守甲', [器('守甲.py')]))\n"
                     "    闸 += [(名, [器(档)]) for 名, 档, 参 in 左移之拦]\n"
                     "    return 闸 + [('快', [器('全测.py'), '--只', ','.join(读者之快)]), ('慢一', [器('慢一.py')]), ('慢二', [器('慢二.py')])]\n"
                     "def 後之存(n):\n    return [('存', [器('丁存.py'), '--存'])]\n"
                     "左移之拦 = (('戊拦', '戊拦.py', []),)\n读者之快 = ('格乙',)\n读者之慢 = ()\n活态之格 = ('格丙',)\n後之并 = ('慢一', '慢二')\n")
    落('工具/全测.py', '"""全测"""\nimport os\n'
                     "def run(d, a):\n    return ''\n"
                     "def _助():\n    return run('助', ['工具/助跑.py'])\n"
                     "def chk_a():\n    return run('甲', ['工具/格甲.py', '--自测'])\n"
                     "def chk_b():\n    import 格乙载\n    _助()\n    run('入', ['工具/接入样.py'])\n    return run('乙', ['工具/格乙.py'])\n"
                     "def chk_c():\n    return run('丙', ['工具/格丙.py', '--自测'])\n"
                     "def chk_d():\n    run('丁', ['工具/〔欠哨〕.py'])\n    return False, '⛔ 先跑 〔跑〕工具/示器.py --修'\n"
                     "def 诸项(quick):\n    items = [('格甲', chk_a)]\n    if not quick:\n        items.append(('格乙', chk_b))\n"
                     "        items.append(('格丙', chk_c))\n        items.append(('格丁', chk_d))\n    return items\n")
    落('.github/workflows/autopush.yml', "# 主枝之自推（注）：沙盒只推暂存之枝。\n# 〔跑〕工具/流注.py ⛔算\non:\n  push:\n    branches: ['章-*']\n"
                                         "jobs:\n  g:\n    uses: ./.github/workflows/gate.yml\n  a:\n    steps:\n      - run: 〔跑〕工具/流跑.py --写\n"
                                         "      - run: echo \"⛔拒——沙盒兜底 〔跑〕工具/推示.py --直\" >> \"$O\"\n")
    落('.github/workflows/gate.yml', "# 分片之闸\non:\n  workflow_call:\n    inputs: {}\njobs:\n  x:\n    steps:\n      - run: 〔跑〕工具/格甲.py\n")
    落('.claude/settings.json', json.dumps({'permissions': {'allow': ['Bash(〔跑〕工具/权串.py:*)']},
                                           'hooks': {'Stop': [{'matcher': '', 'hooks': [{'type': 'command',
                                                                                          'command': '〔跑〕工具/钩停.py || echo "或 〔跑〕工具/钩停示.py"'}]}]}},
                                          ensure_ascii=False))
    落('工具/githooks/pre-push', '#!/bin/sh\n# 注：见 设定/钩注之档.md\nOUT=$(〔跑〕工具/钩全测.py 2>&1)\n'
                              'echo "⛔ 未过——再 〔跑〕工具/钩示.py（交 GitHub 之闸）"\nprintf \'%s\\n\' "〔跑〕工具/钩示二.py"\n')
    落('工具/席/造章.js', "export const meta = { name: '造章', description: '造式二代·一章：执笔写整章。余从略' }\n"
                       "// 〔跑〕工具/席注.py ⛔算\nconst 令 = '〔跑〕工具/席跑.py N'\n")
    落('工具/自走.py', '"""自走——此刻该干哪一件。"""\nimport subprocess\nL = "Workflow({scriptPath:\'工具/席/造章.js\'})"\n'
                     "def 断():\n    print('下一步：〔跑〕工具/印令器.py')\n    M = []\n    M.append('〔跑〕工具/处方器.py --甲')\n"
                     "    subprocess.run(['python3', '工具/调器.py'])\n")
    for x, s in (('甲库', '"""甲库——章号之库。"""\nimport 子库\n'), ('孤器', '"""孤器（1119 立）——无人跑亦无人读。"""\n'),
                 ('只读器', '"""只读器——有人提而无人跑。"""\n'), ('迹读', 'import 迹器\n'), ('坏器', 'def (:\n'),
                 ('常驻器', '"""常驻器——後台自驱。"""\nimport time\n间 = 5 * 60\ndef 守():\n    while True:\n        time.sleep(间)\n'),
                 ('提者', "P = '只读器.py'\nQ = '设定/样账.md'\nimport glob\nG = glob.glob('设定/回执_*.md')\nR = '设定/段案'\n"
                          "S = '大审_至第%d章.md'\nT = '孤账.json'\nU = '长名之样账簿'\nV = '〔进化树〕.py'\nW = '常驻器.py'\n"),
                 ('族读', "import glob, os\nG = glob.glob(os.path.join('设定', '剧样_*.md'))\n"),
                 ('判异器', 'X = (\n"""设定/判异之档.md"""\n)\n')):
        落('工具/%s.py' % x, s)
    for x in ('甲前 甲慢 甲後 乙後 丙闸 丁存 戊拦 守甲 慢一 慢二 格甲 格乙 格丙 格乙载 助跑 流跑 推示 示器 钩停 席跑 甲注 乙注 流注 席注 权串 子库 迹器 '
              '记缺库 泊库 印器 印令器 处方器 调器 外声闸 窗界哨 〔欠哨〕 〔进化树〕 钩全测 钩示 钩示二 钩停示 接入样 乙样 甲样'.split()
              + ['负测_甲前', '负测_窗界哨']):
        落('工具/%s.py' % x, '"""%s——样之器也。"""\n' % x)
    落('设定/法用册.json', json.dumps({'说明': '法用册——已取之法', '法': [1], '待': [{'id': '用之审', '限': 15}],
                                     '废': [{'id': '欠哨之废', '待合': 'W908·环7', '限': 20, '去证': [{'无档': '工具/〔欠哨〕.py'}]}]},
                                    ensure_ascii=False))
    落('设定/孤账.json', '{"说明": "孤账——无人引"}')
    落('设定/死样账.json', '{"a": 1}')
    落(W908名, _样W908())
    for p in ('设定/样账.md', '设定/长名之样账簿.md', '设定/无引之档.md', '设定/回执_0901_第9章.md', '设定/回执_0902_甲.md',
              '设定/剧样_甲.md', '设定/判异之档.md', '设定/钩注之档.md',
              '设定/大审_至第10章.md', '设定/大审_至第20章.md', '设定/段案/a.md', '设定/段案/b.md'):
        落(p, '# 样之首题\n')
    for n in range(1, 13):
        落('版本/第%d章/_器之迹.md' % n, '| 器 | 跑 | 败 |\n|---|---|---|\n| %s | 1 | 0 |\n| %s | 1 | 0 |\n%s'
           % (('甲前' if n <= 2 else '无此器' if n == 12 else '格甲') + '.py', '迹器' + '.py', '| 〔进化树〕.py | 1 | 0 |\n' if n == 11 else ''))
    落('正文/镇冢秘术_第十二章_测.md', '测\n')
    落('.gitignore', '设定/器红样.json\n')
    落('设定/器红样.json', '{}')


def 自测():
    ok, 坏 = 0, []

    def T(名, 真, 注=''):
        nonlocal ok
        if 真:
            ok += 1
        else:
            坏.append(名 + ('（%s）' % 注 if 注 else ''))

    P = lambda 干: 干 + '.py'
    t = tempfile.mkdtemp(prefix='体系总图_')
    try:
        _造仓(t)
        _git(t, 'init', '-q')
        文, 源, 件 = 生(t)
        跑 = lambda k: set(a for a, _ in 件[P(k)]['跑']) if P(k) in 件 else set()
        读 = lambda k: set(件[k]['读']) if k in 件 else set()
        判 = lambda k: 件[P(k)]['判']
        欠, 树 = '看官欠' + '哨', '进化' + '树'
        T('①部之归属：外声闸→心、自走→心、全测→脉；名以「哨」终者（窗界哨、看官欠哨与其负测）→觉（W909「觉＝……诸哨」·用之证环3）；'
          '负测_X 随 X、负测之部；表外者（孤器）入⓪未归（⛔猜）',
          件[P('外声闸')]['部'] == '心' and 件[P('自走')]['部'] == '心' and 件[P('全测')]['部'] == '脉'
          and 件[P('窗界哨')]['部'] == '觉' and 件[P(欠)]['部'] == '觉' and 件[P('负测_窗界哨')]['部'] == '觉' and 部之(P('某新哨')) == '觉'
          and 部之(P('负测_外声闸')) == '心' and 部之(P('负测_推闸')) == '脉' and 件[P('孤器')]['部'] is None
          and '未归' in 文.split('## ① 五部之脊')[0] and P('孤器') in 文.split('## ① 五部之脊')[0])
        T('①之三 并主之件归部（W909 复核①c：W907 之剧情全图 并主後⛔入未归）：剧情全图→心', 部之(P('剧情' + '全图')) == '心')
        T('①之二 账之部：表中「+」断之名复其全（总圣经→心、方法账→长）；子目、族之名照认',
          部之(_展('00_镇冢秘术+_唯一总圣经')) == '心' and 部之(_展('方法账')) == '长' and 部之('设定/段案/') == '心'
          and 部之('回执_*.md') == '心' and 部之('版本/第N章/_器之迹.md') == '长')
        T('②封版：调（步、闸、存、左移之拦）、载（正文档→甲库、记之缺→记缺库）、印令（封毕之语之 印器）分书；docstring 与注之名⛔算',
          '封版·前' in 跑('甲前') and '封版·前' in 跑('甲慢') and '封版·後' in 跑('甲後') and '封版·後' in 跑('丙闸')
          and '封版·後' in 跑('丁存') and '封版·後' in 跑('戊拦') and '封版·前（载）' in 跑('甲库') and '封版·後（载）' in 跑('记缺库')
          and 跑('印器') == {'封版·後（印令）'} and P('印器') not in 源['封版']['後'] and not 跑('甲注') and not 跑('乙注'),
          str((跑('甲库'), 跑('印器'), 跑('甲注'))))
        序 = 源['封版']['序']['後·全']
        T('②之二 封版 --後 之全序（用之证环3）：前置（记之缺 ⛔）→步（必者 ⛔）→闸 ⛔（条件、左移之拦之插、格、并起）→其後（席记、活态 ⚠、--演 止、提交）→存 ⚠→收',
          序 == [('前置', '记之缺 ⛔（载 记缺库）'), ('步', '甲步（甲後）→二步（乙後） ⛔'),
                ('闸⛔', '囤灰闸（丙闸）→守甲〔若 N≥411〕→戊拦→快（全测；格：格乙）→并〔慢一、慢二〕'),
                ('其後', '席记「封版」段→活态之报 ⚠（全测；格：格丙）→〔--演 至此止〕→提交'), ('存⚠', '存（丁存）'),
                ('收', '泊之语（载 泊库）→封毕之语（印令 印器）')]
          and 源['封版']['序']['後·步'] == [('甲步', P('甲後')), ('二步', P('乙後'))] and '- --後·闸⛔：囤灰闸（丙闸）→守甲' in 文
          and '载 2、印令 1' in 文, str(序))
        T('③全测：格甲唯自测、格乙本职、助函之器与格中之载随格；读者之快之格兼「每章封时」；格中只印之示（示器）⛔算其跑',
          跑('格甲') >= {'全测·格甲（唯自测）'} and '全测·格乙' in 跑('格乙') and '全测·格乙' in 跑('助跑')
          and '全测·格乙' in 跑('格乙载') and any('每章封时' in b for _, b in 件[P('格乙')]['跑']) and not 跑('示器'), str(跑('格甲')))
        T('④流：run 之器→流·autopush、uses gate.yml→gate 之跑；注行与 echo 之引文之器⛔算（推示）；触之语；① GitHub 之流之表书其调',
          '流·autopush' in 跑('流跑') and '流·autopush' in set(a for a, _ in 件['gate.yml']['跑']) and '流·gate' in 跑('格甲')
          and not 跑('流注') and not 跑('推示') and 源['流调']['autopush.yml'] == ['gate.yml', P('流跑')]
          and 源['触']['autopush.yml'] == 'push（章-*）' and 源['触']['gate.yml'] == '他流所调'
          and '| autopush.yml | 脉 |' in 文 and '| push（章-*） | gate.yml（格甲）、流跑 |' in 文, str(源['流调']))
        T('⑤钩：Stop 之令→钩·Stop（每回合之末）；permissions 之串⛔算', ('钩·Stop', '每回合之末') in 件[P('钩停')]['跑'] and not 跑('权串'))
        T('⑤之三 git 钩与钩之令先去 echo／printf 之引文（W909 复核①a：pre-push 唯调 全测并，「再 python3 工具/推.py」之示旧误算其跑）：'
          '钩全测→git钩·pre-push（每 git push）；钩示、钩示二（echo、printf 之引）、钩停示（钩之令之 echo）⛔跑⛔读；注中之档名⛔算',
          ('git钩·pre-push', '每 git push') in 件[P('钩全测')]['跑'] and ('引', 'git钩·pre-push') in 读(P('钩全测'))
          and not 跑('钩示') and not 跑('钩示二') and not 读(P('钩示')) and not 读(P('钩示二')) and not 跑('钩停示') and not 读(P('钩停示'))
          and not any(b.startswith('git钩') for _, b in 读('钩注之档.md')), str((件[P('钩全测')]['跑'], 读(P('钩示')), 跑('钩停示'))))
        T('⑤之二 自驱：while 中 sleep（间＝5*60）→ 自驱（後台常驻）·後台每 5 分；⓪书其数（用之证环3：存底守之每五分）',
          ('自驱（後台常驻）', '後台每 5 分（常驻·自驱）') in 件[P('常驻器')]['跑'] and '常驻自驱 1：常驻器' in 文
          and 行之文(件[P('常驻器')])[4].startswith('後台每 5 分'), str(件[P('常驻器')]['跑']))
        T('⑥席：令中之器→席·造章、注之器⛔算；造章.js 由自走派令（囤灰闸.派令之席）', '席·造章' in 跑('席跑') and not 跑('席注')
          and '派令·自走' in set(a for a, _ in 件['造章.js']['跑']))
        T('⑥之二 入口：print 与 L.append 之令→口·自走（印令）；subprocess 之列→口·自走（调）',
          跑('印令器') == {'口·自走（印令）'} and 跑('处方器') == {'口·自走（印令）'} and 跑('调器') == {'口·自走'},
          str((跑('印令器'), 跑('处方器'), 跑('调器'))))
        T('⑦谁读：import 与函中 from…import 入载、档名之串入引；注之名⛔、自引⛔；行书「载之者／引之者」',
          ('载', '甲库') in 读(P('子库')) and ('载', '封版') in 读(P('甲库')) and ('引', '提者') in 读(P('只读器')) and not 读(P('甲注'))
          and 行之文(件[P('子库')])[5].startswith('载之者：甲库'), str((读(P('子库')), 读(P('甲注')))))
        T('⑦之二 账之读：全名（样账.md、孤账.json）与六字以上之干（长名之样账簿）俱认；无引之档无读', ('引', '提者') in 读('样账.md')
          and ('引', '提者') in 读('孤账.json') and ('引', '提者') in 读('长名之样账簿.md') and not 读('无引之档.md'))
        囤 = 源['囤']
        无引 = {os.path.basename(p) for p, _ in 囤.档之囤灰(t, 日=0, 末改={'设定/' + os.path.basename(f): 0 for f in glob.glob(os.path.join(t, '设定', '*.md'))})}
        本无 = {k for k, v in 件.items() if v['类'] == '账' and k.endswith('.md') and not v['读'] and k != os.path.basename(图名)}
        无引 &= {k for k, v in 件.items() if v['类'] == '账'}           # 族（大审_至第N章 之类）囤灰闸 逐档判之，本图以族判之——唯比单档
        T('⑦之三 账之读·一义一判（W909 复核①b③：旧律缺 glob 之族，剧情庭_*、方法升级_*、硬条_* 之档误判未用）：活档之 glob（剧样_*.md）→「族读（族）」；'
          '囤灰闸 认有引而本图寻不着读者者（git 钩之注）书「活档」；本图有读而囤灰闸认无引者（行首三引号之串）⓪ 书其异；余之「无读」与 档之囤灰（日＝0）同',
          ('族', '族读') in 读('剧样_甲.md') and '族读（族）' in 行之文(件['剧样_甲.md'])[5] and 件['剧样_甲.md']['机由'] == '机判：其读者无一有跑'
          and ('引', '活档') in 读('钩注之档.md') and 源['活档补'] == ['钩注之档.md'] and 源['判异'] == ['判异之档.md']
          and 本无 == 无引 - set(源['判异']) and '无引之档.md' in 本无 and '本图有读而囤灰闸认无引 1：判异之档.md' in 文,
          str((本无, 无引, 源['活档补'], 源['判异'])))
        T('⑧末真用：格甲第11章、迹器第12章；甲前只见於窗外（第1—2章）→无迹（窗外末见第2章）；无此器入⓪',
          件[P('格甲')]['末'] == 11 and 件[P('迹器')]['末'] == 12 and 件[P('甲前')]['末'] is None and 源['迹章'] == list(range(3, 13))
          and 行之文(件[P('甲前')])[6] == '无迹（窗外末见第2章）' and ('窗中之器而盘上已无 1：' + P('无此器')) in 文,
          str((件[P('格甲')]['末'], 行之文(件[P('甲前')])[6], 源['迹章'])))
        T('⑧之二 无迹之由：唯全测所跑而在封时之格（格丙）→迹盲：GitHub、封版闸後；无跑无迹（孤器）→全迹无；唯被载（甲库）→迹盲：被载',
          行之文(件[P('格丙')])[6] == '无迹（迹盲：GitHub、封版闸後）' and 行之文(件[P('孤器')])[6] == '无迹（全迹无）'
          and 行之文(件[P('甲库')])[6] == '无迹（迹盲：被载）', str((行之文(件[P('格丙')])[6], 行之文(件[P('甲库')])[6])))
        T('⑨判·名单（设定/方案/W908.md 之机读之块·⛔抄於码）：外声闸照 W908 判半用（其机判当为未用）；块之「原」与上文逐判同、分批之行得',
          判('外声闸') == '半用' and 件[P('外声闸')]['由'].startswith('W908') and 源['W908']['误'] == [] and 源['W908']['数'] == (7, 3)
          and 源['W908']['批'] == {'环1': '甲', '环8': '甲', '环7': '乙', '环9': '乙'} and '死样账.json' in 源['W908']['表']
          and not [x for x in 源['崩'] if 'W908' in x], str((源['W908']['误'], 源['W908']['数'], 源['W908']['批'])))
        T('⑨之二 悖与候复审：名单判死而仍有跑口（全测·格丁）→「悖」；名单判半用而今迹见、机判用→「候复审」；无迹之半用（外声闸）⛔书',
          (件[P(欠)]['悖'] or '').startswith('悖：死而仍有跑口（全测·格丁）') and 件[P(树)]['悖'] == '今迹见第11章（机判：用）——候复审'
          and 件[P('外声闸')]['悖'] is None and '### W908 名单之对照' in 文 and ('| ' + P(树) + ' | 半用') in 文,
          str((件[P(欠)]['悖'], 件[P(树)]['悖'])))
        T('⑩机判：格乙＝用、只读器＝半用（有读无跑）、孤器＝未用；子库随甲库随封版有跑＝用；迹器（迹见）＝用；格甲（唯自测而迹见）＝用',
          判('格乙') == '用' and (判('只读器'), 件[P('只读器')]['由']) == ('半用', '机判：有读无跑') and 判('孤器') == '未用'
          and 判('子库') == '用' and 判('迹器') == '用' and 判('格甲') == '用',
          str({k: 判(k) for k in ('格乙', '只读器', '孤器', '子库', '迹器', '格甲')}))
        T('⑩之二 唯自测而无迹者（格丙）＝半用（有读无跑·唯自测）', (判('格丙'), 件[P('格丙')]['由']) == ('半用', '机判：有读无跑（唯自测）'),
          str((判('格丙'), 件[P('格丙')]['由'])))
        T('⑪红与限之源（用之证环3：限⛔书死）：看官欠哨 之限取 法用册 废之条（20）、外声闸（甲批 环8）无废之条取 待「用之审」（15）；'
          '孤器（器·未用·无治）⛔；看官欠哨（死·末章 12 ≤ 20）⚠；死样账（死·无治）⛔；无引之档（账·机判未用）⚠',
          件[P(欠)]['治'] == ('环7', 20, '法用#欠哨之废·废') and 件[P('外声闸')]['治'] == ('环8', 15, '法用#用之审')
          and 件[P('孤器')]['红'] == '⛔' and 件[P(欠)]['红'] == '⚠' and 件['死样账.json']['红'] == '⛔' and 件['无引之档.md']['红'] == '⚠'
          and ('⛔ ' + P('孤器')) in 文 and '随 W908 环7·限 20（法用#欠哨之废·废）' in 文, str((件[P(欠)]['治'], 件[P('外声闸')]['治'])))
        T('⑪之三 乙批⛔借 用之审 之限、治已行⛔红（W909 复核⑨）：乙样（未用·乙批 环7·无废之条）→（乙批·无专限）只 ⚠；'
          '接入样（未用·甲批 环8·治＝接入·今有本职之跑与读→机判用）→ ⚠「治已行——候复审」；甲样（死·甲批 环1）取 用之审 之 15',
          件[P('乙样')]['治'] == ('环7', None, '乙批·无专限') and 件[P('乙样')]['红'] == '⚠'
          and 件[P('接入样')]['机判'] == '用' and 件[P('接入样')]['红'] == '⚠' and (件[P('接入样')]['悖'] or '').startswith('治已行（W908 环8 接入')
          and 件[P('甲样')]['治'] == ('环1', 15, '法用#用之审') and 件[P('甲样')]['红'] == '⚠'
          and '随 W908 环7（乙批·无专限：只 ⚠）' in 行之文(件[P('乙样')])[7] and '｜治已行' in 文,
          str((件[P('乙样')]['治'], 件[P('接入样')]['悖'], 件[P('甲样')]['治'])))
        件2 = {P(欠): dict(件[P(欠)], 跑=set(), 读=set(), 载=set())}
        判之(dict(源, 末章=21), 件2)
        件3 = {P(欠): dict(件[P(欠)], 跑=set(), 读=set(), 载=set())}
        判之(dict(源, 末章=16), 件3)
        件4 = {k: dict(件[k], 跑=set(), 读=set(), 载=set()) for k in (P(欠), P('甲样'), P('乙样'))}
        判之(dict(源, 末章=12, 废治={}, 审限=None), 件4)
        件5 = {k: dict(件[k], 跑=set(), 读=set(), 载=set()) for k in (P('甲样'), P('乙样'))}
        判之(dict(源, 末章=999), 件5)
        T('⑪之二 逾限即红：末章 21 ＞ 废之限 20 → ⛔；末章 16（逾用之审之 15 而未逾废之 20）→ ⚠；法用册无其限：甲批之治（甲样）→ ⛔「W908 环1 而无其限」、'
          '乙批（看官欠哨）→ ⚠；末章 999：甲样（逾 15）⛔、乙样（乙批）仍 ⚠',
          件2[P(欠)]['红'] == '⛔' and 件3[P(欠)]['红'] == '⚠' and 件4[P(欠)]['红'] == '⚠' and 件4[P('甲样')]['红'] == '⛔'
          and 件4[P('甲样')]['治'] is None and '→W908 环1 而无其限' in 行之文(件4[P('甲样')])[7]
          and 件5[P('甲样')]['红'] == '⛔' and 件5[P('乙样')]['红'] == '⚠',
          str((件2[P(欠)]['红'], 件3[P(欠)]['红'], 件4[P(欠)]['红'], 件4[P('甲样')]['红'], 件5[P('乙样')]['红'])))
        T('⑫账之族：回执_*.md（2）、大审_至第N章.md（2）、设定/段案/（2）各一行；提者引之', 件['回执_*.md']['数'] == 2
          and 件['大审_至第N章.md']['数'] == 2 and 件['设定/段案/']['数'] == 2 and ('引', '提者') in 读('回执_*.md')
          and ('引', '提者') in 读('设定/段案/') and ('引', '提者') in 读('大审_至第N章.md'))
        T('⑫之二 gitignored 之档（器红样.json）⛔入件之集（沙盒有而 GitHub 无，图即两样）', '器红样.json' not in 件 and '孤账.json' in 件)
        T('⑬析崩之器（坏器）⓪书之、余照出（⛔崩）', ('工具/' + P('坏器')) in 源['崩'] and P('坏器') in 件 and '析崩 1' in 文)
        T('⑭首句：以段连行、去名与括注、截至「。」；首段只名或纯 ASCII 者取首行括注之末节（⛔「某日 立」）', 首句('囤灰闸——**造了没人用的器**。其余', P('囤灰闸')) == '造了没人用的器'
          and 首句('外声闸（2026-09-01 立）\n\n听者之声。', P('外声闸')) == '听者之声' and 首句('甲（注）：乙丙丁。', 'x') == '甲：乙丙丁'
          and 首句('演练（1027 坑54·丝滑主义：改流程之物先演一回）——workflow_dispatch（ref）。', '演练.yml') == '改流程之物先演一回'
          and 首句('账并（1119 立）——两写者之账之并器：甲\n乙之治。', P('账并')) == '两写者之账之并器：甲乙之治')
        T('⑭之二 首句之残而补（用之证环3）：零 token→本器之句；PreToolUse 钩→其法；「法用#X」→首行之引语；「某日立」→其法；诸检之列',
          首句('甲链（1015 立）——零 token。\n\n为何立：旧法二病。\n  本器把诸段之记并成每人从头到尾之一条链；余。', P('甲链')) == '零 token：把诸段之记并成每人从头到尾之一条链'
          and 首句('丙钩（1022 立·坑：甲）——PreToolUse 钩。\n\n【其由】旧事。\n【其法】见其 pid 尚活而工具之调用要写设定者即拦。', P('丙钩'))
          == 'PreToolUse 钩：见其 pid 尚活而工具之调用要写设定者即拦'
          and 首句('丁谱（1119 立·作者令「进化路线俱存主线而⛔倒车」·法用#丁谱）。\n\n作者原话。', P('丁谱')) == '进化路线俱存主线而⛔倒车'
          and 首句('戊重 · 2026-09-04 立（甲轮）\n\n★其法：逐拍与其後三拍求最长公共子串，≥6字即报。', P('戊重')) == '逐拍与其後三拍求最长公共子串，≥6字即报'
          and 首句('己检之四（立）\n\n  ① 人名之误 —— 甲\n  ② 撞号之误 —— 乙\n  ③ 锚之长短 —— 丙', P('庚检')) == '己检之四：诸检：人名之误、撞号之误、锚之长短')
        T('⑭之三 账职：首行为引者取其首句；首题为条之号与日者书「逐条之录」与其目；json 无说明之键者标之',
          _账职('> 本档由 工具/甲.py --写 生成，⛔手改；余\n\n# 目录\n', '甲谱.md') == '本档由 工具/甲.py --写 生成，⛔手改'
          and _账职('## G0925-01 ｜ 2026-09-25 11:36\n- **改什么**：甲\n- **改了更好在哪**：乙\n', '改单.md') == '逐条之录（首条 G0925-01）：每条书 改什么、改了更好在哪'
          and _账职('{"章": 1, "时": 2}', '基线.json') == '（无说明之键）键：章、时')
        T('⑭之四 一眼：图首短而全——件数、五部之数、⛔之名、⚠之数、读法俱在 ⓪ 之前', '## 一眼' in 文 and 文.index('## 一眼') < 文.index('## ⓪')
          and '- 件 ' in 文.split('## ⓪')[0] and '觉 ' in 文.split('## ⓪')[0] and ('⛔ 即红' in 文.split('## ⓪')[0] and P('孤器') in 文.split('## ⓪')[0])
          and '读法·判' in 文.split('## ⓪')[0] and '读法·末真用' in 文.split('## ⓪')[0])
        T('⑮文之定：同盘再生逐字同（灯之今同）', 生(t, 源['今'])[0] == 文)
        import io, contextlib

        def _验():
            b = io.StringIO()
            with contextlib.redirect_stdout(b):
                rc = 验(t)
            return rc, b.getvalue()
        with contextlib.redirect_stdout(io.StringIO()):
            写(t)
        rc1, o1 = _验()
        p = os.path.join(t, 图名)
        s = open(p, encoding='utf-8').read()
        open(p, 'w', encoding='utf-8').write(s.replace('卡未立', '卡在·异'))
        rc2, o2 = _验()
        open(p, 'w', encoding='utf-8').write(s.replace('## ② 一件一行', '## ② 一件一行（手改）'))
        rc3, o3 = _验()
        T('⑯--验：同→✓不旧；☁ 之异⛔算旧；改一行→⚠ 档旧；用之红（孤器）→⛔ rc 1', '✓ 不旧' in o1 and '✓ 不旧' in o2 and '⚠ 档旧' in o3
          and rc1 == rc2 == rc3 == 1 and ('⛔ ③用之红：' + P('孤器')) in o1 and '体系总图·验' in o1, o3[-200:])
        os.remove(p)
        rc3b, o3b = _验()
        T('⑯之五 写者之语（W912 环2③·坑63 之由即去）：档旧、档缺俱书「封版 --後 与总编辑之治（--随治）」与「两写之并由 账并 之生成之图一支」，'
          '⛔「唯封版」「⛔手跑入主」之旧语、⛔「手跑……亦可」；档旧示 --随治 之令、缺档示 --印（⛔写）',
          all('封版 --後 与总编辑之治（--随治' in o and '两写之并由 账并 之生成之图一支' in o and '亦可' not in o and '唯封版' not in o
              and '手跑入主' not in o for o in (o3, o3b)) and 'python3 工具/体系总图.py --随治' in o3 and '--印（⛔写）' in o3b, o3b[-200:])
        open(p, 'w', encoding='utf-8').write(s)
        _旧根 = ROOT
        globals()['ROOT'] = t
        try:
            b = io.StringIO()
            with contextlib.redirect_stdout(b):
                rc印 = main(['--印'])
        finally:
            globals()['ROOT'] = _旧根
        T('⑯之六 --印：只印、⛔写（人手之看）', rc印 == 0 and b.getvalue().startswith('# 体系总图') and open(p, encoding='utf-8').read() == s)
        for _ in range(6):                             # 去诸 ⛔ 之件（器、账；去一或令其所读者亦未用，故递去）→ 无红而档旧
            去 = [v['路'] for v in 生(t)[2].values() if v['红'] == '⛔' and v['类'] in ('器', '账')]
            for x in 去:
                os.remove(os.path.join(t, x))
            if not 去:
                break
        rc4, o4 = _验()
        T('⑯之二 无红而档旧 → ⚠ rc 0（旧只 ⚠）', rc4 == 0 and '⚠ 档旧' in o4 and not any(l.strip().startswith('⛔') for l in o4.split('\n')),
          o4[-300:])
        乙p = os.path.join(t, '工具', P('格乙'))
        乙文 = open(乙p, encoding='utf-8').read()
        open(乙p, 'w', encoding='utf-8').write('def (:\n')          # 用之器（全测之格跑之、全测引之）之码坏：⛔用之红，唯析崩
        rc5, o5 = _验()
        open(乙p, 'w', encoding='utf-8').write(乙文)
        T('⑯之三 析崩即红（W909 复核②：旧 rc 0 只印「⚠ 析不得」）：用之器之码坏 → 「⛔ 析崩」rc 1（全测之格据 rc 与此行而红）',
          rc5 == 1 and ('⛔ 析崩：工具/' + P('格乙')) in o5 and '⛔ ③' not in o5, o5[-300:])
        坏囤 = os.path.join(t, '坏囤.py')
        诸崩 = []
        for 码 in ('raise SystemExit(3)\n', 'def (:\n'):
            open(坏囤, 'w', encoding='utf-8').write(码)
            globals()['_囤灰闸之路'] = 坏囤
            try:
                文6, 源6, _ = 生(t)
                rc6, o6 = _验()
            finally:
                globals()['_囤灰闸之路'] = None
            诸崩.append((源6['崩'], 源6['末章'], 文6, rc6, o6))
        T('⑯之四 囤灰闸 载不得（首行 raise SystemExit(3)：旧 --验 只印其头即 rc 3；或其码坏）→ ⛔崩、⓪书之；末章不得（0）亦书崩（⛔静默遮诸限·复核②⑧）；rc 1',
          all(any(x.startswith('囤灰闸（载不得：') for x in 崩) and any(x.startswith('正文之末章不得') for x in 崩) and 末 == 0
              and '截至第 0 章' in 文6 and '（析不得）' in 文6 and rc6 == 1 and '⛔ 析崩：囤灰闸（载不得' in o6 for 崩, 末, 文6, rc6, o6 in 诸崩)
          and '载不得：SystemExit 3' in ' '.join(诸崩[0][0]) and '载不得：SyntaxError' in ' '.join(诸崩[1][0]),
          str([x[0][:2] for x in 诸崩]))
        w = os.path.join(t, W908名)
        w文 = open(w, encoding='utf-8').read()
        样代 = lambda x: [x := x.replace(a, b) for a, b in _样代][-1]
        诸误 = []
        for 改 in (样代(_样W908('    - 多出之器（样）\n')), re.sub(r'```json 用之审\n.*?\n```', '', w文, flags=re.S),
                   w文.replace('{"器": [', '{"器": [,')):
            open(w, 'w', encoding='utf-8').write(改)
            诸误.append((生(t)[1]['崩'], _验()[0]))
        open(w, 'w', encoding='utf-8').write(w文)
        T('⑲名单之块（W909 复核③：W908 之名单⛔抄於码）：上文添一名而块不随 →「块与上文异·器 死：块少 多出之器」；块缺；块之 JSON 坏——俱析崩、rc 1',
          any('块与上文异·器 死：；块少 多出之器' in x for x in 诸误[0][0]) and any('无机读之块' in x for x in 诸误[1][0])
          and any('机读之块坏' in x for x in 诸误[2][0]) and all(rc == 1 for _, rc in 诸误), str([x[0] for x in 诸误]))
        t2 = tempfile.mkdtemp(prefix='体系总图缺_')
        try:
            _造仓(t2, 去=('工具/封版.py', '工具/全测.py', '.github', '.claude', '版本', '正文'))
            文2, 源2, _ = 生(t2)
            T('⑰源缺⛔崩：封版、全测、流、钩、迹俱缺 → 照生、⓪书其缺', '## ② 一件一行' in 文2 and '（缺）' in 文2
              and all(x in 源2['缺'] for x in ('工具/封版.py', '工具/全测.py', '.claude/settings.json', '版本/第N章/_器之迹.md')), str(源2['缺']))
            open(os.path.join(t2, '工具', '全测.py'), 'w', encoding='utf-8').write('def (:\n')
            open(os.path.join(t2, '工具', '封版.py'), 'w', encoding='utf-8').write('x = 1\n')
            文3, 源3, _ = 生(t2)
            T('⑰之二 全测析崩、封版无前後 → ⓪书「析不得」、⛔崩；正文缺 → 末章不得亦书崩', '工具/全测.py（诸项之析）' in 源3['崩']
              and '工具/封版.py（前／後之析）' in 源3['崩'] and '## ③' in 文3 and any(x.startswith('正文之末章不得') for x in 源2['崩']), str(源3['崩']))
            os.remove(os.path.join(t2, '工具', '封版.py'))
            b = io.StringIO()
            with contextlib.redirect_stdout(b):
                rc7 = 验(t2)
            T('⑰之三 核心之源（封版、全测）缺 → 与析崩同：「⛔ 析崩：工具/封版.py（缺·核心之源）」rc 1；他源之缺只 ⚠',
              rc7 == 1 and '⛔ 析崩：工具/封版.py（缺·核心之源）' in b.getvalue() and '⚠ 源缺：.claude/settings.json' in b.getvalue(), b.getvalue()[-300:])
        finally:
            shutil.rmtree(t2, ignore_errors=True)
    finally:
        shutil.rmtree(t, ignore_errors=True)
    # ㉑—㉚〔W912〕机制之流、近之进化、活之色、--摘、--随治、执行之查之接线（小样之仓＋其枝之时）
    _旧取 = os.environ.get('ZM_TU_NOFETCH')
    os.environ['ZM_TU_NOFETCH'] = '1'
    t3 = tempfile.mkdtemp(prefix='体系总图流_')
    try:
        _造仓(t3)
        接 = '工具/接棒守' + '.py'
        os.makedirs(os.path.join(t3, '工具'), exist_ok=True)
        open(os.path.join(t3, 接), 'w', encoding='utf-8').write(
            '"""接棒守（样）——巡与派。"""\n主枝 = \'主样\'\n总编辑 = \'session_总样号ABCDEFG\'\n巡警枝 = \'备份/巡警\'\n巡印枝 = \'备份/巡印\'\n'
            '巡印档 = \'_巡印.json\'\n巡应枝 = \'备份/巡应\'\n巡钟枝 = \'备份/巡钟\'\n'
            "兜底之令 = (('甲', 'trig_甲', '27 * * * *', '27 * * * *', True), ('乙', 'trig_乙', '57 * * * *', '47 * * * *', True),\n"
            "         ('丙', 'trig_丙', '7 * * * *', '7 * * * *', False))\n钟之令 = (('子', '', '12 * * * *'), ('午', '', '42 * * * *'))\n"
            "def 派之参(n):\n    return 'create_session'\n")
        open(os.path.join(t3, '工具', '心跳' + '.py'), 'w', encoding='utf-8').write('"""心跳（样）——写书之坐之锁。"""\n限 = 25 * 60\n')
        云令 = 'python3 工具/接棒守' + '.py --云巡'
        open(os.path.join(t3, '.github', 'workflows', '巡.yml'), 'w', encoding='utf-8').write(
            "# 巡（样）：章推之環与疏 cron\non:\n  schedule:\n    - cron: '*/30 * * * *'\n  workflow_dispatch:\n    inputs: {}\n  push:\n"
            "    branches: ['备份/巡演', '备份/巡钟', '章-*']\njobs:\n  huan:\n"
            "    if: (github.event_name == 'workflow_dispatch' && inputs.huan == '1') || (github.event_name == 'push' && startsWith(github.ref_name, '章-'))\n"
            "    steps:\n      - run: %s\n  xun:\n"
            "    if: github.event_name == 'schedule' || (github.event_name == 'workflow_dispatch' && inputs.huan != '1') || (github.event_name == 'push' && !startsWith(github.ref_name, '章-'))\n"
            "    steps:\n      - run: %s\n      - run: curl -X POST \"$API/actions/workflows/%%E5%%B7%%A1.yml/dispatches\" -d \"$J\"\n" % (云令, 云令))
        件们 = [{'id': 'W9%02d' % i, '名': '样件%d' % i, '裁': [{'时': '2026-11-%02dT10:00Z' % i, '法': '取' if i % 2 else '续',
                                                             '由': '所废：旧法%d；较旧：效升%d' % (i, i) if i != 10 else '长' * 120}]} for i in range(1, 12)]
        件们 += [{'id': 'W151', '名': '章件', '裁': [{'时': '2026-11-30T10:00Z', '法': '取', '由': '章'}]},
                {'id': 'W90', '名': '旧号', '裁': [{'时': '2026-11-29T10:00Z', '法': '取', '由': '旧'}]}]
        open(os.path.join(t3, '设定', '工作流账.json'), 'w', encoding='utf-8').write(json.dumps({'说明': '样', '件': 件们}, ensure_ascii=False))
        T0 = 1795000000
        环 = dict({k: v for k, v in os.environ.items() if k not in _定库之变}, GIT_AUTHOR_NAME='t', GIT_AUTHOR_EMAIL='t@t',
                 GIT_COMMITTER_NAME='t', GIT_COMMITTER_EMAIL='t@t', GIT_CONFIG_GLOBAL=os.devnull)

        def gt(*a, 时=None):
            e = dict(环, **({'GIT_COMMITTER_DATE': '@%d +0000' % 时, 'GIT_AUTHOR_DATE': '@%d +0000' % 时} if 时 else {}))
            return subprocess.run(['git', '-c', 'core.quotepath=off'] + list(a), cwd=t3, capture_output=True, text=True, env=e)
        gt('init', '-q', '-b', '主样')
        gt('add', '-A')
        gt('commit', '-q', '-m', '基', 时=T0 - 9000)
        gt('commit', '-q', '--allow-empty', '-m', '第11章《样》封版（造式二代·封版#11）：诸闸', 时=T0 - 7200)
        gt('commit', '-q', '--allow-empty', '-m', '第12章《样》封版（造式二代·封版#12）：诸闸', 时=T0 - 3600)
        gt('update-ref', 'refs/remotes/origin/主样', 'HEAD')
        gt('remote', 'add', 'origin', t3)                  # 本地之 origin（取=True 之 fetch 自取·⛔网）

        def 枝(名, 档们, 时, 父=None):
            """临时之枝（refs/remotes/origin/<名>）：其树唯 档们、其提交之时＝时（commit-tree·⛔动工作区）。"""
            idx = os.path.join(t3, '.git', 'idx_' + 名.replace('/', '_'))
            if os.path.exists(idx):
                os.remove(idx)
            e = dict(环, GIT_INDEX_FILE=idx)
            for 档, 文 in 档们:
                b = subprocess.run(['git', 'hash-object', '-w', '--stdin'], cwd=t3, input=文, capture_output=True, text=True, env=环).stdout.strip()
                subprocess.run(['git', 'update-index', '--add', '--cacheinfo', '100644,%s,%s' % (b, 档)], cwd=t3, capture_output=True, env=e)
            树 = subprocess.run(['git', 'write-tree'], cwd=t3, capture_output=True, text=True, env=e).stdout.strip()
            c = gt('commit-tree', 树, '-m', 名, *(['-p', 父] if 父 else []), 时=时).stdout.strip()
            gt('update-ref', 'refs/remotes/origin/' + 名, c)
            gt('update-ref', 'refs/heads/' + 名, c)
            return c
        刻 = lambda x: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(x))
        枝('备份/巡印', [('_巡印.json', json.dumps({'rc': 0}))], T0 - 600)
        枝('备份/巡应', [('_巡应.json', json.dumps({'rc': 0}))], T0 - 4000)
        枝('备份/心跳', [('_心跳.json', json.dumps({'章': 13}))], T0 - 4600)
        乙报 = ('报/推/治-样乙.json', json.dumps({'时': 刻(T0 - 1200), '果': '红', '因': '', '免': ['格免样'],
                                                '红': ['✗ 格丁             ⛔样之红', '⛔全测未过：格丁']}, ensure_ascii=False))
        c报 = 枝('备份/报', [乙报], T0 - 1200)
        枝('备份/报', [乙报, ('报/推/治-样.json', json.dumps({'时': 刻(T0 - 300), '果': '败', '因': 'merge'}, ensure_ascii=False))], T0 - 300, c报)
        文3, 源3, 件3 = 生(t3, T0, 取=True)                  # 取：迹枝旧於十五分者自本地之 origin 取（取=False 之局见 ㉗之四）
        流3 = 源3['流图']
        节3 = 流3['节']
        边3 = {(a, b): 语 for a, b, 语, _, _ in 流3['边']}
        机3 = {(a, b) for a, b, _, _, 机 in 流3['边'] if 机}
        T('㉑ 机取之边（巡之 on 与 job 之 if）：push 章-* → huan（⛔xun）、cron → xun（⛔huan）、push 备份/巡演·备份/巡钟 → xun（⛔huan）、手派 → 二 job；'
          'job 之 --云巡 → 云巡；push 章-* → autopush、uses → gate；兜底之令（名与 cron·停者注之）→ 总编辑、钟之令 → 巡钟（接棒守 之表·ast）',
          {('治章枝', '巡.yml#huan'), ('定时', '巡.yml#xun'), ('push:备份/巡演', '巡.yml#xun'), ('巡钟', '巡.yml#xun'), ('手派', '巡.yml#huan'),
           ('手派', '巡.yml#xun'), ('巡.yml#huan', '云巡'), ('巡.yml#xun', '云巡'), ('治章枝', 'autopush'), ('autopush', 'gate'),
           ('兜底', '总编辑'), ('钟', '巡钟')} <= 机3
          and not {('治章枝', '巡.yml#xun'), ('定时', '巡.yml#huan'), ('push:备份/巡演', '巡.yml#huan'), ('巡钟', '巡.yml#huan')} & set(边3)
          and 边3[('兜底', '总编辑')] == '甲 27 * * * *、乙 57 * * * *、丙 7 * * * *（停）' and 边3[('定时', '巡.yml#xun')] == 'cron */30 * * * *'
          and '流:巡.yml' not in 节3 and 节3['总编辑']['名'] == '总编辑之坐（总样号ABCDEFG）' and 节3['哨PR']['名'] == '哨 PR（头枝 备份/巡警）',
          str(sorted(机3))[:300])
        T('㉑之二 若可（GitHub 之式）：event_name、startsWith、!、&&、||、括号；inputs.* 不定作或真；非 push 之事 ref 作主枝',
          若可("github.event_name == 'push' && !startsWith(github.ref_name, '章-')", 'push', '备份/巡钟')
          and not 若可("github.event_name == 'push' && !startsWith(github.ref_name, '章-')", 'push', '章-*')
          and 若可("(github.event_name == 'workflow_dispatch' && inputs.huan == '1') || x", 'workflow_dispatch')
          and not 若可("github.event_name == 'schedule'", 'push', '章-*') and 若可('${{ always() }}', 'push', '治-*')
          and 若可("startsWith(github.ref_name, '章-')", 'push', '章-*') and not 若可("startsWith(github.ref_name, '章-')", 'schedule', None, '主样')
          and 若可("github.ref_name == '备份/巡钟'", 'push', '备份/巡钟') and not 若可("github.ref_name == '备份/巡钟'", 'push', '章-*'))
        失3 = 流3['失据']
        表边 = [(a, b) for a, b, _, _, _ in _流边 if a in 节3 and b in 节3]
        有据 = [(a, b) for a, b in 表边 if '（失据）' not in 边3.get((a, b), '（失据）')]
        T('㉒ 流之边之验：其串在其档者有据（样之接棒守含 create_session、def 派之参(、巡印枝，样之自走含 造章.js）、余俱「失据」——⓪ 报「流之边失据 N」、'
          '其边书虚线、--验 只 ⚠（⛔崩）',
          sorted(有据) == sorted([('总编辑', '派'), ('派', '写书'), ('写书', '造章'), ('云巡', '巡印')]) and len(失3) == len(表边) - 4
          and any('哨 PR' in x and '无「def 哨PR(」' in x for x in 失3) and ('⛔ 流之边失据 %d' % len(失3)) in 文3 and '-.->' in 文3
          and '（失据）' in 边3[('云巡', '哨PR')], str((有据, 失3[:2])))
        块 = 文3.split('```mermaid\n', 1)[1].split('\n```', 1)[0].split('\n') if '```mermaid\n' in 文3 else []
        合 = re.compile(r'^(?:flowchart LR|  subgraph b\d+\["[^"\[\](){}<>|]*"\]|    n\d+\["[^"\[\](){}<>|]*"\]|  end|'
                       r'  n\d+ (?:-->|-\.->)\|"[^"\[\](){}<>|]*"\| n\d+|  classDef l[gyrw] [\w:#,]+|  class n\d+(?:,n\d+)* l[gyrw])$')
        坏行 = [l for l in 块 if not 合.match(l)]
        T('㉓ mermaid 之节名、边语合法（⛔ASCII 之括号与引号乱其式：节名() 作全角、去引号）；节 %d、边 %d、classDef 绿黄红灰' % (len(节3), len(流3['边'])),
          块 and not 坏行 and 节名('甲（"乙"）[丙](丁)|戊') == '甲（乙）［丙］（丁）／戊' and all('  classDef l%s' % c in 文3 for c in 'gyrw'),
          str(坏行[:2]))
        近3 = 源3['近']
        T('㉔ 近之进化：工作流账「件」W9xx 之裁之末八、新者先（W151、W90 ⛔入）；摘取「所废／较旧」·≤80 字（长者截而带…）；⑦ 之表、一眼之末件',
          近3 is not None and [x[0] for x in 近3] == ['W911', 'W910', 'W909', 'W908', 'W907', 'W906', 'W905', 'W904']
          and 近3[0][4] == '所废：旧法11；较旧：效升11' and len(近3[1][4]) == 80 and 近3[1][4].endswith('…') and 近3[0][2] == '取'
          and '## ⑦ 近之进化' in 文3 and '| W911 | 样件11 | 取 | 2026-11-11T10:00Z | 所废：旧法11；较旧：效升11 |' in 文3
          and '- 近之进化之末（⑦）：W911 取「样件11」' in 文3, str(近3[:2]))
        T('㉕ 期之判：常驻每 5 分→300；cron */30→1800、27 */3→三时、二令（:27 :57）合→1800；每章／自走每跑／每回合／push 章-*→章期；每十章→章期×10；'
          '每推→章期；并账有冲突时、主环手跑→None（按需）；源之章期取「封版#N」之提交（近十章之均隔）',
          期之('後台每 5 分（常驻·自驱）', 3600) == (300.0, '常驻·每 5 分') and 期之('巡（cron */30 * * * *，手派，push（章-*））', 3600)[0] == 1800
          and cron之期('27 */3 * * *') == 10800 and cron之期('7,37 * * * *') == 1800 and cron之期('0 0 1 * *') is None
          and _合期([3600, 3600]) == 1800 and 期之('每章封时（封版 --後）', 3600) == (3600, '每章') and 期之('自走每跑（主环）', 3600)[0] == 3600
          and 期之('autopush（push（章-*、治-*），手派）', 3600)[0] == 3600 and 期之('每十章（大审之包）', 3600)[0] == 36000
          and 期之('每推（GitHub 全测）', 3600) == (3600, '每推（≥ 每章）') and 期之('并账有冲突时（git merge）', 3600) is None
          and 期之('主环手跑', 3600) is None and 期之('每章封时', None) is None and 源3['活迹']['章期'] == 3600.0,
          str(源3['活迹']['章期']))
        T('㉖ 灯之界：末跑 ≤ 期×1.5 🟢｜≤ 期×3 🟡｜逾 🔴｜末跑败 🔴｜无期或无迹 ⚪', [_灯判(0, False, 100, d) for d in (150, 151, 300, 301)]
          == ['🟢', '🟡', '🟡', '🔴'] and _灯判(0, True, 100, 1) == '🔴' and _灯判(0, False, None, 1) == '⚪' and _灯判(None, False, 100, 1) == '⚪')
        灯3 = lambda k: (节3[k].get('灯'), 节3[k].get('灯由', ''))
        T('㉗ 迹之取（临时仓之枝之时·取自本地之 origin）：巡印 10 分前→云巡 🟢（期 30 分·二 job 之最密）；巡应 4000 秒前→总编辑 🟡（兜底二令合 30 分）；'
          '心跳逾 3×25 分→写书 🔴；末报「败·因 merge」→autopush 🔴「合入之卡」、gate 取其前之真跑之报（备候不成⛔算 gate 之跑）🟢；主枝 🟢；'
          '甲前（封版·前·章之封 3600 秒前·章期 3600）🟢、封版（迹表·无定期）⚪ 按需；格乙（唯全测之格·gate 之全测）🟢；huan 之期＝章期、xun 之期＝cron',
          灯3('云巡')[0] == '🟢' and '期 30 分' in 灯3('云巡')[1] and 灯3('总编辑')[0] == '🟡' and 灯3('写书')[0] == '🔴' and '逾期×3' in 灯3('写书')[1]
          and 件3['autopush.yml']['灯'] == '🔴' and '合入之卡（因 merge' in 件3['autopush.yml']['灯由'] and 件3['gate.yml']['灯'] == '🟢'
          and '治-样乙（红）' in 件3['gate.yml']['灯由'] and not 源3['活迹']['旧']
          and 灯3('主枝')[0] == '🟢' and 件3[P('甲前')]['灯'] == '🟢' and '第12章之封' in 件3[P('甲前')]['灯由']
          and 件3[P('封版')]['灯'] == '⚪' and 件3[P('封版')]['灯由'].startswith('按需·末') and '第12章之封' in 件3[P('封版')]['灯由']
          and 件3[P('格乙')]['灯'] == '🟢' and 'gate 之全测' in 件3[P('格乙')]['灯由']
          and 节3['巡.yml#huan']['期值'][0] == 3600 and 节3['巡.yml#xun']['期值'][0] == 1800,
          str((灯3('云巡'), 灯3('总编辑'), 灯3('写书'), 件3[P('封版')]['灯由'], 件3['autopush.yml']['灯由']))[:300])
        T('㉗之二 共迹⛔借（W912 怀疑之验）：huan、xun 共 force 写 备份/巡印 → 唯最密之 xun 认其迹（🟢）、huan ⚪「迹不可取（巡印⛔辨 job）」；'
          '兜底之令之节 ⚪「借巡应⛔辨其触」（总编辑之坐仍取巡应）；xun 之自派直连本流之 job（⛔经手派之节中转）',
          灯3('巡.yml#xun')[0] == '🟢' and 灯3('巡.yml#huan')[0] == '⚪' and '巡印⛔辨 job' in 灯3('巡.yml#huan')[1]
          and 灯3('兜底')[0] == '⚪' and '借巡应⛔辨其触' in 灯3('兜底')[1] and 灯3('总编辑')[0] == '🟡'
          and {('巡.yml#xun', '巡.yml#huan'), ('巡.yml#xun', '巡.yml#xun')} <= {(a, b) for a, b, 语, _, _ in 流3['边'] if '自派' in 语}
          and not any(b == '手派' and '自派' in 语 for a, b, 语, _, _ in 流3['边']), str((灯3('巡.yml#huan'), 灯3('兜底')))[:300])
        迹样 = {'值': {'报推': (T0 - 300, True, '报/推/章-样（败·因 merge）'), '报在': (T0 - 300, False, '报/推/章-样（败·因 merge）'),
                     '报治': (T0 - 900, False, '报/推/治-样丙（成）'), '报闸': (T0 - 1200, False, '报/推/治-样乙（红）'),
                     '全测': (T0 - 1200, False, 'gate 之全测·报/推/治-样乙（红）')}, '封': {}, '闸免': {'格免样'}, '闸红': {'格丁'}}
        候样 = lambda k, 跑: _件之候(源3, 迹样, k, {'类': '器', '跑': set(跑)})
        T('㉗之三 败报⛔连坐（W912 怀疑之验）：末报「败·因 merge」→ 唯 autopush 与治章枝 🔴「合入之卡」；推取 报/推/治-*（交已至）、推报取报在（⛔承败）；'
          '流·autopush 所调者只承其时（⛔承败）、全测之 流·autopush 取 gate 真跑之报（备候不成⛔作其跑）',
          候样('推.py', []) == [(T0 - 900, False, '报/推/治-样丙（成）')] and 候样('推报.py', [('流·autopush', 'x')]) == [迹样['值']['报在']]
          and 候样('存底.py', [('流·autopush', 'x')]) == [(T0 - 300, False, '报/推/章-样（败·因 merge）')]
          and 候样('全测.py', [('流·autopush', 'x')]) == [(T0 - 1200, False, '报/推/治-样乙（红）')]
          and '合入之卡' in _灯由('🔴', 迹样['值']['报推'], (3600, '每章')) and '末跑败' in _灯由('🔴', (T0, True, '报/推/治-样（败·因 片）'), (3600, '每章'))
          and 灯3('治章枝')[0] == '🔴' and '合入之卡' in 灯3('治章枝')[1] and 件3[P('流跑')]['灯'] == '🟢', str(候样('存底.py', [('流·autopush', 'x')])))
        T('㉗之四 gate 之全测⛔借而静绿（W912 怀疑之验）：唯「全测·X」所跑而无真路之件取之；有真路（口·、席·、封版·……）者⛔取（其灯取其真路之迹）；'
          '其格在报之「免」（活态之格）⛔算、「全测·X·自测」⛔算；其格在报之「红」→ 🔴（其格红）——真报之「免」「红」读入',
          候样('格乙.py', [('全测·格乙', '每推')]) == [迹样['值']['全测']] and 候样('口样.py', [('口·自走', '自走每跑'), ('全测·口样', '每推')]) == []
          and 候样('免样.py', [('全测·格免样', '每推')]) == [] and 候样('自测样.py', [('全测·自测样·自测', '每推')]) == []
          and 候样('丁样.py', [('全测·格丁', '每推')]) == [(T0 - 1200, True, 'gate 之全测·报/推/治-样乙（红）·其格红：格丁')]
          and 源3['活迹']['闸免'] == {'格免样'} and 源3['活迹']['闸红'] == {'格丁'} and 件3[P('看官欠' + '哨')]['灯'] == '🔴'
          and '其格红：格丁' in 件3[P('看官欠' + '哨')]['灯由'] and 件3[P('助跑')]['灯'] == '🟢',
          str((源3['活迹']['闸免'], 源3['活迹']['闸红'], 件3[P('看官欠' + '哨')].get('灯由'))))
        文3f, 源3f, 件3f = 生(t3, T0, 取=False)
        节3f = 源3f['流图']['节']
        T('㉗之五 本地之引或旧（取=False：封版 --後 之写、--验、图之数）：巡应 逾期 → 总编辑之坐 ⚪「迹未取」（⛔作当跑而未跑）、巡印 在期内仍 🟢、'
          '写书之坐之迹（心跳·其坐自取）照判 🔴',
          节3f['总编辑']['灯'] == '⚪' and '迹未取' in 节3f['总编辑']['灯由'] and 节3f['云巡']['灯'] == '🟢' and 节3f['写书']['灯'] == '🔴'
          and '本地未取' in 节3f['云巡']['灯由'], str((节3f['总编辑']['灯由'], 节3f['云巡']['灯由']))[:300])
        T('㉘ 取不得 → ⚪「迹不可取」（⛔猜）：巡钟之枝无 → 钟、巡钟 ⚪；无期之件 ⚪ 按需；账 ⚪；② 之表带「灯」栏、mermaid 以 classDef 著色、一眼书四色之数',
          灯3('巡钟')[0] == '⚪' and '迹不可取' in 灯3('巡钟')[1] and 灯3('钟')[0] == '⚪' and 件3[P('孤器')]['灯'] == '⚪'
          and 件3['孤账.json']['灯'] == '⚪' and '| 其源档 | 灯 |' in 文3 and re.search(r'  class n\d+(,n\d+)* lr', 文3) is not None
          and re.search(r'- 灯（今算·--验 ⛔比·跑即亮）：件 🟢 \d+·🟡 \d+·🔴 \d+·⚪ \d+', 文3) is not None, 灯3('巡钟')[1])
        文3b = 生(t3, T0 + 10 ** 6)[0]
        with open(os.path.join(t3, 图名), 'w', encoding='utf-8') as f:
            f.write(文3)
        import io as _io, contextlib as _cl
        with _cl.redirect_stdout(_io.StringIO()) as _b:
            _rc验 = 验(t3)
        T('㉙ 灯随时而变而 --验 ⛔比（_比之文 去灯之符、四色之数与 class 之行）：今异之二图俱「✓ 不旧」；流之边失据只 ⚠',
          文3b != 文3 and _比之文(文3b) == _比之文(文3) and '✓ 不旧' in _b.getvalue() and '⚠ 流之边失据' in _b.getvalue(), _b.getvalue()[-200:])
        _存灯 = [(v, v.get('灯')) for v in list(件3.values()) + list(节3.values())]
        for v, g in _存灯:
            v['灯'] = '🟢' if g == '🔴' else g
        文3绿 = 印图(源3, 件3)                                # 同树同时而无一 🔴 之图（一眼之灯行无「；🔴〔…〕」之尾）
        for v, g in _存灯:
            v['灯'] = g
        with open(os.path.join(t3, 图名), 'w', encoding='utf-8') as f:
            f.write(文3绿)
        with _cl.redirect_stdout(_io.StringIO()) as _b2:
            验(t3)
        摘绿 = 摘(t3, T0, 取=False)
        T('㉙之二 红与不红之翻⛔作档旧（W912 怀疑之验：一眼之灯行有 🔴 方附「；🔴〔…〕」）：档无红、今有红——_比之文 同、--验「✓ 不旧」、--摘「图档：✓ 不旧」',
          '；🔴〔' in 文3 and '；🔴〔' not in 文3绿 and _比之文(文3绿) == _比之文(文3) and '✓ 不旧' in _b2.getvalue()
          and any(x.startswith('图档：✓ 不旧') for x in 摘绿), _b2.getvalue()[-200:] + str([x for x in 摘绿 if x.startswith('图档')]))
        with open(os.path.join(t3, 图名), 'w', encoding='utf-8') as f:
            f.write(文3)
        T12 = T0 + 12 * 3600
        源3['活迹']['停'] = True
        灯之(源3, 件3, 流3, T12)
        停红 = sorted([k for k, x in 节3.items() if x.get('灯') == '🔴' and not x['件']] + [k for k, v in 件3.items() if v.get('灯') == '🔴'])
        停灯 = (灯3('写书'), 灯3('总编辑'), 灯3('主枝'), 件3[P('甲前')]['灯'], 件3[P('甲前')]['灯由'], 灯3('云巡')[0], 灯3('治章枝')[0])
        源3['活迹']['停'], 源3['活迹']['解停'] = False, T12 - 1800
        灯之(源3, 件3, 流3, T12)
        解灯 = (件3[P('甲前')]['灯'], 件3[P('甲前')]['灯由'], 灯3('写书')[0], 灯3('总编辑')[0])
        源3['活迹']['解停'] = None
        灯之(源3, 件3, 流3, T0)
        open(os.path.join(t3, '设定', '暂停令.json'), 'w', encoding='utf-8').write(json.dumps(
            {'立': 'x', '令': '作者令：样', '据': 'x:1', '解': {'时': '2026-11-09 17:14 UTC', '言': '作者令：解'}}, ensure_ascii=False))
        _停解 = _停之迹(t3)
        os.remove(os.path.join(t3, '设定', '暂停令.json'))
        import calendar as _cal
        T('㉙之三 暂停中⛔红潮（W912 怀疑之验）：停逾十二时——随写书与兜底之期（每章、每推、兜底之令合、心跳之限）俱 ⚪「暂停中」，'
          'GitHub 之 cron（巡印、云巡、巡·xun）照判、末跑败（因 merge）、其格红照 🔴；解停之後首期自解停起算（⛔即红）；暂停令之「解」之时读入',
          set(停红) <= {'云巡', '巡印', '巡.yml#xun', '巡.yml', '接棒守.py', 'autopush.yml', '治章枝', P('看官欠' + '哨')} and '云巡' in 停红
          and 停灯[0][0] == '⚪' and '暂停中' in 停灯[0][1] and 停灯[1][0] == '⚪' and '暂停中' in 停灯[1][1] and 停灯[2][0] == '⚪'
          and 停灯[3] == '⚪' and 停灯[4].startswith('暂停中') and 停灯[5] == '🔴' and 停灯[6] == '🔴'
          and 解灯[0] == '🟢' and '自解停' in 解灯[1] and 解灯[2] == '🟢' and 解灯[3] == '🟢'
          and _停解 == (False, _cal.timegm((2026, 11, 9, 17, 14, 0))), str((停红, 停灯, 解灯, _停解))[:400])
        摘3 = 摘(t3, T0, 取=False)
        T('㉚ --摘（今树即算·≤25 行）：一眼之数、⛔即红、🔴 之件带其由（写书之坐、autopush）、⚠、半用／未用带由、图档旧否、失据',
          len(摘3) <= 25 and 摘3[0].startswith('体系总图·摘（今算·截至第 12 章') and any(x.startswith('🔴 当跑而未跑或末跑败') for x in 摘3)
          and any('🔴 写书之坐：' in x for x in 摘3) and any('🔴 autopush.yml：' in x and '合入之卡' in x for x in 摘3)
          and any(x.startswith('图档：✓ 不旧') for x in 摘3) and any(x.startswith('未用 ') and '（' in x for x in 摘3)
          and any(x.startswith('⛔ 流之边失据') for x in 摘3) and 摘3[-1].startswith('⛔ 摘：'), '\n'.join(摘3)[-300:])
        _坐旧 = {k: os.environ.get(k) for k in ('CLAUDE_CODE_REMOTE_SESSION_ID', 'CLAUDE_SESSION_ID', 'CLAUDE_CODE_SESSION_ID')}
        os.remove(os.path.join(t3, 图名))
        try:
            for k in _坐旧:
                os.environ.pop(k, None)
            os.environ['CLAUDE_CODE_REMOTE_SESSION_ID'] = 'cse_他坐号XYZ'
            with _cl.redirect_stdout(_io.StringIO()) as _b1:
                _rc他 = 随治(t3)
            _在他 = os.path.exists(os.path.join(t3, 图名))
            os.environ['CLAUDE_CODE_REMOTE_SESSION_ID'] = 'session_总样号ABCDEFG'
            with _cl.redirect_stdout(_io.StringIO()):
                _rc总 = 随治(t3)
            _在总 = os.path.exists(os.path.join(t3, 图名))
        finally:
            for k, v in _坐旧.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
        T('㉛ --随治 唯总编辑之坐（接棒守.总编辑·照 心跳.坐 取本坐）：他坐 rc 2 ⛔写；总编辑之坐 rc 0 写之', _rc他 == 2 and not _在他 and _rc总 == 0 and _在总
          and '唯总编辑之坐' in _b1.getvalue(), _b1.getvalue()[:120])
        头 = gt('rev-parse', 'HEAD').stdout.strip()            # 主枝先於本树一章（封版#13 与其 _器之迹 只在 origin/主样）
        e13 = dict(环, GIT_INDEX_FILE=os.path.join(t3, '.git', 'idx_主13'))
        subprocess.run(['git', 'read-tree', 头], cwd=t3, capture_output=True, env=e13)
        b13 = subprocess.run(['git', 'hash-object', '-w', '--stdin'], cwd=t3, input='| 器 | 跑 | 败 |\n|---|---|---|\n| 孤器.py | 1 | 0 |\n',
                             capture_output=True, text=True, env=环).stdout.strip()
        subprocess.run(['git', 'update-index', '--add', '--cacheinfo', '100644,%s,版本/第13章/_器之迹.md' % b13], cwd=t3, capture_output=True, env=e13)
        树13 = subprocess.run(['git', 'write-tree'], cwd=t3, capture_output=True, text=True, env=e13).stdout.strip()
        c13 = gt('commit-tree', 树13, '-p', 头, '-m', '第13章《样》封版（造式二代·封版#13）：诸闸', 时=T0 - 600).stdout.strip()
        gt('update-ref', 'refs/remotes/origin/主样', c13)
        _, 源13, 件13 = 生(t3, T0)
        摘13 = 摘(t3, T0, 取=False)
        gt('update-ref', 'refs/remotes/origin/主样', 头)
        T('㉛之二 树落後主枝（W912 怀疑之验：总编辑之树 --巡 ⛔ff）：封与图档取 HEAD 与 origin/<主枝> 之并（封末 13·⛔误迟）；树无而主枝有之章之迹 git show 取之；'
          '--摘 首行注「树落後主枝 N 提交」',
          源13['活迹']['封末'][0] == 13 and 源13['活迹']['落後'] == 1 and 源13['活迹']['迹主'] == {'孤器.py': 13}
          and '迹·第13章' in 件13['孤器.py']['灯由'] and '第13章之封' in 件13[P('甲前')]['灯由'] and '树落後主枝 1 提交' in 摘13[0],
          str((源13['活迹']['封末'], 源13['活迹']['落後'], 源13['活迹']['迹主'], 摘13[0]))[:300])
    finally:
        shutil.rmtree(t3, ignore_errors=True)
        if _旧取 is None:
            os.environ.pop('ZM_TU_NOFETCH', None)
        else:
            os.environ['ZM_TU_NOFETCH'] = _旧取
    接文 = (_读(os.path.join(ROOT, '工具', '接棒守' + '.py')) or '').split("if __name__ == '__main__':")[-1]
    巡段 = 接文.split("if '--巡' in a:", 1)[1].split('sys.exit(_rc)', 1)[0] if "if '--巡' in a:" in 接文 else ''
    法文 = _读(os.path.join(ROOT, '工具', '法用之守' + '.py')) or ''
    推文 = _读(os.path.join(ROOT, '工具', '推' + '.py')) or ''
    T('㉜ 执行之查之接线（W912 环4）：接棒守 --巡 之沙盒之路於活守（补印）之後、巡(查印=True) 之前印「── 执行之图 ──」＋ --摘（timeout 20·逾即「⚠ 图之摘逾时」⛔拦）、'
      'GitHub 之路（巡()）与 --代 ⛔印；法用之守 --报 於总结行之上添图之行（--无图 即免）、推.py 速检传 --无图（⛔拖累写书）',
      巡段.find('_态 = 活守(') < 巡段.find('── 执行之图 ──') < 巡段.find('_rc = 巡(查印=True)') and "'--摘'" in 巡段 and 'timeout=20' in 巡段
      and '图之摘逾时' in 巡段 and "if '--代' not in a" in 巡段 and '── 执行之图 ──' not in 巡段.split("if os.environ.get('GITHUB_ACTIONS') == 'true':")[1].split('sys.stderr.write(第一律之印()')[0]
      and 'L.insert(len(L) - 1, 图之行())' in 法文 and "'--无图' not in a" in 法文 and "('法用之守', ['法用之守.py', '--报', '--无图'])" in 推文,
      巡段[:80])
    # ⑱真仓
    t0 = time.time()
    文R, 源R, 件R = 生(ROOT)
    秒 = time.time() - t0
    器数 = len(glob.glob(os.path.join(ROOT, '工具', '*.py')))
    T('⑱真仓：生之 %.1f 秒 ＜ 15、器 %d 件俱入、封版 --後 之步含「体系总图」（接线）' % (秒, 器数), 秒 < 15
      and sum(1 for v in 件R.values() if v['类'] == '器') == 器数
      and any(b == 本器 for _, b in ((源R.get('封版') or {}).get('序') or {}).get('後·步', [])), '%.1f 秒' % 秒)
    T('⑱之二 真仓：全测之格「体系总图」跑本器（--验 本职）、本器判用', '全测·体系总图' in set(a for a, _ in 件R[本器]['跑'])
      and 件R[本器]['判'] == '用', str(件R[本器]['跑']))
    文件 = open(os.path.abspath(__file__), encoding='utf-8').read()
    W = 源R['W908']['表']
    书 = [k for k in W if k.endswith('.py') and W[k][0] != '用' and k in 文件] + [
        k for k in 件R if 件R[k]['类'] == '账' and k.endswith('.md') and k != os.path.basename(图名)
        and (k in 文件 or (len(k) - 3 >= 6 and k[:-3] in 文件)) and os.path.join('设定', k) not in [p for _, p in 他读之档]]
    T('⑱之三 本器之文⛔书名单之器之全名、账之全名与长档之干（囤灰闸 之闭包、候退、档之囤灰 ⛔因本器而误认其引）', not 书, str(书[:3]))
    T('⑱之四 真仓：设定/方案/W908.md 之机读之块可读、「原」与上文逐判同、甲乙二批俱得（名单唯此一份）',
      源R['W908']['在'] and not 源R['W908']['误'] and len(W) >= 40 and set(源R['W908']['批'].values()) == {'甲', '乙'}
      and not [x for x in 源R['崩'] if 'W908' in x], str((源R['W908']['误'], 源R['W908']['数'])))
    T('⑱之五 真仓：析崩 0（囤灰闸 载得、末章得、诸器之码可析）', not 源R['崩'] and 源R['末章'] > 0, str(源R['崩'][:3]))
    流R = 源R.get('流图') or {'节': {}, '边': [], '失据': []}
    块R = 文R.split('```mermaid\n', 1)[1].split('\n```', 1)[0].split('\n') if '```mermaid\n' in 文R else []
    合R = re.compile(r'^(?:flowchart LR|  subgraph b\d+\["[^"\[\](){}<>|]*"\]|    n\d+\["[^"\[\](){}<>|]*"\]|  end|'
                    r'  n\d+ (?:-->|-\.->)\|"[^"\[\](){}<>|]*"\| n\d+|  classDef l[gyrw] [\w:#,]+|  class n\d+(?:,n\d+)* l[gyrw])$')
    T('⑱之六 真仓·机制之流：mermaid 合法（节名⛔括号与引号）、平台之件俱入（总编辑、写书、派、兜底、哨 PR、巡印、巡应、治章枝、主枝、备份/报）、'
      '巡之 job 逐立、机取之边自流与接棒守之表（兜底之令→总编辑）、⑦ 近之进化（W9xx 之裁）在',
      块R and not [l for l in 块R if not 合R.match(l)] and {'总编辑', '写书', '派', '兜底', '哨PR', '巡印', '巡应', '治章枝', '主枝', '报'} <= set(流R['节'])
      and sum(1 for k in 流R['节'] if k.startswith('巡.yml#')) >= 2 and any(a == '兜底' and b == '总编辑' and m for a, b, _, _, m in 流R['边'])
      and len(源R.get('近') or []) == 8 and '## ⑦ 近之进化' in 文R, str([l for l in 块R if not 合R.match(l)][:2]))
    if 流R['失据']:                                 # 失据只 ⚠（⛔崩·⛔红：源档之串变即其边书虚线，⓪ 与 --验 报之）
        print('  ⚠ 真仓·流之边失据 %d：%s' % (len(流R['失据']), '；'.join(流R['失据'][:3])))
    import tempfile as _tf, shutil as _sh
    _d = _tf.mkdtemp(prefix='体系败_')
    try:
        os.makedirs(os.path.join(_d, '正文'))
        for _nm in ('镇冢秘术_第四章_死局.md', '镇冢秘术_第四百七十六章_某.md'):
            open(os.path.join(_d, '正文', _nm), 'w', encoding='utf-8').write('x')
        _b = 败图(_d, 'Traceback\n  File x\nZeroDivisionError: 假')
        T('⑳ 器崩之护（1119·法用#体系总图之行为之证）：败图「截至第 476 章」、⓪书器败与其迹（⛔依囤灰闸）', '截至第 476 章' in _b and '⛔ 器败' in _b and 'ZeroDivisionError' in _b, _b[:80])
    finally:
        _sh.rmtree(_d, ignore_errors=True)
    print('体系总图·自测 %d/%d%s' % (ok, ok + len(坏), ' 全通' if not 坏 else '｜未过：' + '；'.join(坏)))
    return not 坏


def main(argv):
    if '--自测' in argv:
        return 0 if 自测() else 1
    if '--验' in argv:
        return 验()
    if '--印' in argv:                           # 人手之看：只印、⛔写（写者：封版 --後 与总编辑之 --随治）
        print(生(取=可取())[0])
        return 0
    if '--摘' in argv:                           # 〔W912 环4〕执行之查之据：今树即算·≤25 行（接棒守 --巡 之执行之图印之）
        print('\n'.join(摘()))
        return 0
    if '--随治' in argv:                         # 〔W912 环2③〕总编辑之治：方法一变图即随（他坐 rc 2）
        return 随治()
    if '--件' in argv:
        k = argv.index('--件')
        if k + 1 >= len(argv):
            print('⛔ --件 须带名')
            return 2
        return 一件(argv[k + 1])
    if argv:
        print(__doc__)
        return 2
    return 写()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
