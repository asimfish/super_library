import { Button, Callout, Divider, Grid, H1, H2, Pill, Row, Stack, Table, Text, useHostTheme, useState } from "cursor/canvas";

const roles = [
  {id:"evidence_reader",name:"证据 Agent",budget:24000,input:"作者的完整事实、来源定位、必需项与边界",output:"逐项 supported / unverified 核对，以及未解决的问题",check:"每条证据恰好检查一次；未核验来源不能被自动升级",exclude:"不读取语言库或作者原论文段落"},
  {id:"argument_planner",name:"论证 Agent",budget:36000,input:"原始事实、证据核对、最多两张结构卡",output:"带 evidence_ids 的主张与段落功能顺序",check:"每个主张有已支持的证据；必需项和反例保留",exclude:"不读取完整语言 bundle"},
  {id:"writer",name:"写作 Agent",budget:48000,input:"原始事实、证据核对、论证计划、一次语言 bundle",output:"原创正文 + 每个主张对应的精确片段",check:"主张与必需证据覆盖；片段实际出现在正文",exclude:"内部计划和检查项不作为论文正文"},
  {id:"evidence_reviewer",name:"证据审查 Agent",budget:48000,input:"原始事实、计划、当前正文及主张映射",output:"逐证据与主张审查，pass 或 revise",check:"量值、范围、来源支持、遗漏和推断",exclude:"不看语言 bundle，不看另一位审查的判断"},
  {id:"narrative_reviewer",name:"叙事审查 Agent",budget:48000,input:"原始事实、计划、结构卡、当前正文",output:"问题、证据取舍、衔接、范围和内部语言泄漏检查",check:"独立会话；与写作者及另一审查者不同 actor_id",exclude:"不看另一位审查的判断"},
];

export default function SuperLibraryAgentTeam() {
  const t=useHostTheme();
  const [selected,setSelected]=useState("writer");
  const role=roles.find(r=>r.id===selected)!;
  return <Stack gap={20} style={{padding:24,maxWidth:1400,color:t.text.primary}}>
    <Row justify="space-between" wrap><H1>Super Library：多 Agent 论证写作架构</H1><Pill>2026-10-15 · 功能分支</Pill></Row>
    <Callout tone="info">宿主负责调用真正的独立 Agent；本地协调器负责限定材料、保存产物、验证依赖与修订轮次。最终正文需要证据审查和叙事审查同时通过。</Callout>
    <H2>按依赖协作，审查可并行</H2>
    <div style={{overflowX:"auto"}}><svg viewBox="0 0 1180 335" style={{width:"100%",minWidth:900}} role="img" aria-label="作者事实进入证据、论证、写作阶段，之后并行证据审查与叙事审查；通过后导出，否则有界修订">
      <defs><marker id="team-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill={t.stroke.primary}/></marker></defs>
      {[{x:15,y:100,w:180,a:"作者事实",b:"数值／协议／反例"},{x:235,y:100,w:160,a:"证据核对",b:"每项来源与范围"},{x:435,y:100,w:160,a:"论证规划",b:"问题—证据—结论"},{x:635,y:100,w:160,a:"原创写作",b:"正文＋主张映射"},{x:850,y:40,w:170,a:"证据审查",b:"支持与准确性"},{x:850,y:170,w:170,a:"叙事审查",b:"逻辑与表达"},{x:1060,y:100,w:100,a:"导出",b:"纯正文"}].map(n=><g key={n.a}><rect x={n.x} y={n.y} width={n.w} height={75} rx={3} fill={t.bg.elevated} stroke={t.stroke.secondary}/><text x={n.x+12} y={n.y+29} fontSize={17} fill={t.text.primary}>{n.a}</text><text x={n.x+12} y={n.y+54} fontSize={12} fill={t.text.secondary}>{n.b}</text></g>)}
      {["M195 137H235","M395 137H435","M595 137H635","M795 137H820V77H850","M820 137V207H850","M1020 77H1040V137H1060","M1020 207H1040V137"].map(p=><path key={p} d={p} fill="none" stroke={t.stroke.primary} markerEnd="url(#team-arrow)"/>)}
      <path d="M935 245V280H715V175" fill="none" stroke={t.accent.primary} strokeDasharray="6 4" markerEnd="url(#team-arrow)"/>
      <text x={730} y={307} fill={t.text.secondary} fontSize={13}>需要修改：保留旧稿与审查，最多两次修订</text>
      <text x={15} y={30} fill={t.text.secondary} fontSize={14}>协调 Agent：冻结任务和上下文 → 调度就绪角色 → 提交原始产物 → 管理轮次</text>
      <text x={435} y={202} fill={t.text.secondary} fontSize={12}>最多两张论证结构卡</text>
      <text x={635} y={225} fill={t.text.secondary} fontSize={12}>原始事实＋一个语言 bundle</text>
    </svg></div>
    <Row wrap gap={8}>{roles.map(r=><Button key={r.id} variant={selected===r.id?"primary":"secondary"} onClick={()=>setSelected(r.id)}>{r.name}</Button>)}</Row>
    <Grid columns="1.2fr 1fr" gap={24}>
      <Stack gap={10}><H2>{role.name}的材料边界</H2><Text>输入：{role.input}</Text><Text>输出：{role.output}</Text><Text>完整 packet 上限：{role.budget.toLocaleString()} 字符，包含序列化格式。</Text></Stack>
      <Stack gap={10}><H2>验收与访问</H2><Text>{role.check}</Text><Text tone="secondary">{role.exclude}</Text><Text tone="secondary">字符上限不是模型 token。宿主有本地文件访问能力，packet 分离不是操作系统沙箱。</Text></Stack>
    </Grid>
    <Divider/>
    <H2>四点吸收与各自的规范来源</H2>
    <Table headers={["设计", "实现", "边界"]} rows={[
      ["论证作为单元", "7 张 original_synthesis 结构卡", "复用既有审校导航；没有新增通读论文数"],
      ["按功能检索", "章节／意图／证据关系／实验类型", "一次最多两张，完整序列化预算 6,000 字符"],
      ["内部计划先于正文", "claim → evidence_ids → exact quote", "引用存在和片段匹配不能证明语义支持"],
      ["独立逻辑与证据评价", "两份当前轮次审查＋保留修订历史", "真实模型调用由宿主执行；actor_id 为宿主记录"],
    ]}/>
    <Grid columns="1fr 1fr" gap={24}>
      <Stack gap={10}><H2>明确的工程约束</H2><Text>初始化冻结事实、检索上下文和配置。角色输入包含校验值，旧稿对应的审查不能放行新稿。状态通过原子写入和本地文件锁维护。</Text><Text>语言 bundle 默认最多 16,000 字符，只进入写作角色；读者和规划者没有反复加载全库的需求。</Text></Stack>
      <Stack gap={10}><H2>实际效果的证据边界</H2><Text>回归与真实角色试运行验证协作接口。既有公开表格任务已被检查过，不能作为新的盲测样本。</Text><Text>是否比单 Agent 更专业、更省总成本，仍需新的平衡盲测和调用用量记录。多 Agent 本身不构成质量证明。</Text></Stack>
    </Grid>
    <Text tone="secondary">来源：功能分支中的 ADR-010、TEAM_WORKFLOW.md、team_workflow.py、argument_frames.json。此图展示实现的模块与契约；交互图的呈现不是效果证据。</Text>
  </Stack>;
}
