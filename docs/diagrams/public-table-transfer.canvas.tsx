import { Button, Callout, Divider, Grid, H1, H2, Pill, Row, Stack, Table, Text, useHostTheme, useState } from "cursor/canvas";

const cases = [
  {
    "id": "T01",
    "title": "VLA：速度与成功率",
    "baseline": "Table T01 shows that L1 regression achieves 90.7% success on LIBERO-Long while generating 109.7 actions/s, compared with 91.1% and 4.2 actions/s for 50-step diffusion. Reducing diffusion to 10 steps raises throughput to 19.3 actions/s and lowers chunk latency from 1.9070 to 0.4145 s, with success at 91.0%. At one step, diffusion approaches L1's generation throughput (109.4 versus 109.7 actions/s) and chunk latency (0.0731 versus 0.0729 s), but success falls to 0.0%. Thus, the fastest diffusion setting does not preserve task success, whereas L1 combines high generation throughput with a similar reported success rate to multi-step diffusion. These measurements concern action generation, not end-to-end robot control; per-cell uncertainty and independent-run counts are not supplied.",
    "drafting": "In Table T01, L1 regression combines high generation throughput with a LIBERO-Long success rate close to those of diffusion with 10 or 50 DDIM steps. It generates 109.7 actions/s at 90.7% success, whereas 50-step diffusion reaches 91.1% at 4.2 actions/s. Reducing diffusion to 10 steps raises throughput to 19.3 actions/s with 91.0% success, but one-step diffusion approaches L1 throughput while yielding 0.0% success. Thus, reducing denoising steps does not preserve success throughout the tested range. Latency is measured per eight-action chunk, and these generation statistics do not establish closed-loop control rates. The reported success differences remain descriptive because this packet supplies neither per-cell uncertainty nor independent training-run counts.",
    "primary": [
      "baseline",
      "baseline"
    ],
    "sensitivity": [
      "drafting",
      "tie"
    ],
    "finding": "Baseline enumerates more speed/latency endpoints. Drafting leads with the L1 tradeoff, but both also recap the already stated diffusion failure and end with reporting boundaries."
  },
  {
    "id": "T02",
    "title": "VLA：自解释表注",
    "baseline": "Table T02. OpenVLA with parallel decoding (PD) and PD plus action chunking (PD+AC). Both generate 7-dimensional actions; AC generates eight actions per query. Throughput (actions/s; higher is better) and latency (s/query; lower is better) are averaged over 100 queries on an NVIDIA A100, each using one 224×224 image and a LIBERO task command. Latency covers one action for PD and an eight-action chunk for PD+AC. LIBERO-Long success (%; higher is better) uses 500 episodes (10 tasks × 50), with the best tested checkpoint selected per run. Independent training-run counts and per-cell uncertainty are not supplied. The success-rate dash denotes an unreported value, not zero or inapplicability. Throughput measures generation, not closed-loop control.",
    "drafting": "Table T02. OpenVLA generation efficiency and LIBERO-Long success with parallel decoding (PD) and PD plus action chunking (PD+AC). Both produce 7-dimensional actions; each query yields one action for PD or eight for PD+AC. Inference statistics average 100 queries on an NVIDIA A100, each with one 224×224 image and a LIBERO task command. Throughput is generated actions/s (higher is better), not closed-loop control rate; latency is seconds/query (lower is better), covering different output lengths. Success is a percentage (higher is better) over 500 episodes (10 tasks × 50), using the best tested checkpoint per run. A dash means not reported, not zero or not applicable. Independent training-run counts and per-cell uncertainty are not supplied.",
    "primary": [
      "tie",
      "drafting"
    ],
    "sensitivity": [
      "tie",
      "drafting"
    ],
    "finding": "Caption cells remain in the table. Both are self-contained with it; reported-condition-only SR scope is resolved by their missing-value definition rather than an explicit PD+AC qualifier."
  },
  {
    "id": "T03",
    "title": "持续 RL：终态与在线表现",
    "baseline": "Table T03 shows different rankings for final average performance (AP) and online-learning regret in the six-task sequence. Perfect Memory attains the highest reported final AP (73.09%), compared with 72.93% for OA and 61.83% for Coreset. OA has the lowest regret (27.62%); Coreset and Perfect Memory reach 30.83% and 30.95%, respectively. AP averages success over all seen tasks at the final training step, whereas regret is the time-normalized accumulated current-task success shortfall relative to an oracle with success rate 1. Regret therefore is not the complement of final AP. These are joint agent/CEM-MPC outcomes, not isolated world-model prediction errors or memory/runtime measurements; per-cell uncertainty and significance tests are not supplied.",
    "drafting": "Table T03 separates final task performance from online learning: OA has lower regret than both comparison agents, but not the highest final AP. OA's AP is 72.93%, just below Perfect Memory's 73.09%, while its regret is 27.62% versus 30.95%. Relative to Coreset, OA has both higher AP and lower regret. AP averages success over all seen tasks at the final training step; regret instead measures time-normalized accumulated current-task shortfall against an oracle with success rate 1, so it is not the complement of AP. These CEM/MPC agent comparisons do not isolate world-model prediction quality or establish memory or runtime savings. Without uncertainty or significance tests in the packet, the differences support descriptive comparisons only.",
    "primary": [
      "drafting",
      "drafting"
    ],
    "sensitivity": [
      "drafting",
      "drafting"
    ],
    "finding": "Both organize around different final/online rankings. Drafting summarizes Coreset rather than repeating its cells; both repeat metric definitions recoverable in setup and finish with constraints."
  },
  {
    "id": "T04",
    "title": "世界模型：步长与退化",
    "baseline": "Table T04 shows higher exact-sequence success for GeoWorld than for V-JEPA 2 at each reported planning horizon under the shared ViT-g384 encoder scale. The difference is 1.55 percentage points at T=3 (51.71% versus 50.16%), 2.03 at T=4, 1.66 at T=5, and 1.38 at T=6. Success decreases with horizon for both methods, reaching 18.26% and 16.88%, respectively, at T=6. Both use frozen VideoMix22M-pretrained encoders and CEM planning. This comparison concerns predicted action sequences matching the ground truth given observation and goal clips; it does not establish physical execution performance, performance beyond T=6, a causal mechanism, or equal total training compute. Per-cell uncertainty is not supplied.",
    "drafting": "With the same ViT-g384 encoder scale, GeoWorld exceeds V-JEPA 2 in CrossTask exact-sequence success at every tested planning horizon (Table T04). The gains range from 1.38 to 2.03 percentage points across T=3–6. However, both methods' success rates fall as the horizon increases: GeoWorld declines from 51.71% at T=3 to 18.26% at T=6. This advantage is observed with frozen VideoMix22M-pretrained encoders and CEM planning, but matching encoder scale does not establish equal total training compute. The results concern matching ground-truth action sequences from video observations and goals, not physical robot execution, and do not support extrapolation beyond six actions. Per-cell uncertainty is absent from this packet, preventing a statistical-significance claim.",
    "primary": [
      "drafting",
      "drafting"
    ],
    "sensitivity": [
      "drafting",
      "drafting"
    ],
    "finding": "Drafting uses a gain range; baseline lists four margins. Both preserve deterioration, but substantial paragraph space is devoted to setup and unmeasured-outcome disclaimers."
  }
];
const name = (s: string) => s === "drafting" ? "有库" : s === "baseline" ? "无库" : "平";
export default function SuperLibraryRealTransfer() {
  const theme = useHostTheme();
  const [selected, setSelected] = useState("T01");
  const active = cases.find(c => c.id === selected)!;
  return <Stack gap={20} style={{padding:24, color:theme.text.primary, maxWidth:1400}}>
    <Row justify="space-between" wrap><H1>真实表格 → 科研叙事：验证记录</H1><Pill>2026-10-14 · 诊断，不是效果认证</Pill></Row>
    <Callout tone="warning">首轮有库 5 胜、无库 2 胜、1 平，但六维均分仅相差 0.0208。首轮随机布局恰好把有库全部置于 A；追加互补布局保留为单独结果，不替换首轮。尚未验证你自己的原稿。</Callout>
    <Grid columns="2fr 1fr" gap={28}>
      <Stack gap={10}>
        <H2>工程上核验了什么</H2>
        <Text>3 篇已发表论文 · 4 组真实数据任务 · 8 份未改写输出。34 个数值单元与 2 个空值由主 Agent 和独立事实核验者检查；核对的是论文到任务包的保真，不是原始实验测量。</Text>
        <Text>同一事实文件、有库／无库隔离生成。首轮 2 个新匿名 LLM 评审；追加 2 个新评审分别见互补的 2 A／2 B 布局。模型版本与采样参数未暴露，同系列评审可能共享偏差。</Text>
      </Stack>
      <Stack gap={10}>
        <H2>不能因此宣称</H2>
        <Text>顶会录用质量、普遍叙事提升、人类盲评、AI 检测率下降或用户原稿收益。措辞 lint 通过也不能验证这些。</Text>
        <Text>事实包与语言包分开；这些真实数字和生成文本不进入默认写作语料。</Text>
      </Stack>
    </Grid>
    <H2>匿名 LLM 偏好：两阶段不合并</H2>
    <Table headers={["阶段", "有库胜", "无库胜", "平", "有库／无库六维均分"]} rows={[
      ["首轮：未平衡位置", 5, 2, 1, "4.9375 ／ 4.9167"],
      ["追加：互补位置，新评审", 6, 0, 2, "4.9375 ／ 4.7083"],
    ]} columnAlign={["left","right","right","right","right"]}/>
    <Text tone="secondary">来源：public_table_transfer_2026-10.json。每阶段 4 题 × 2 评审；均分为六个 1–5 维度的等权平均。没有评审标记关键错误。追加阶段同时更换了评审上下文，不能把结果差异解释为位置的因果效应。</Text>
    <Divider/>
    <H2>直接比较写作，而不只看分数</H2>
    <Row wrap gap={8}>{cases.map(c => <Button key={c.id} variant={c.id === selected ? "primary" : "secondary"} onClick={() => setSelected(c.id)}>{c.title}</Button>)}</Row>
    <Row justify="space-between" wrap><Text weight="semibold">{active.title}</Text><Text tone="secondary">首轮：{active.primary.map(name).join(" / ")} · 追加：{active.sensitivity.map(name).join(" / ")}</Text></Row>
    <Grid columns={2} gap={24}>
      <Stack gap={10}><H2>无库文本</H2><Text style={{lineHeight:1.7}}>{active.baseline}</Text></Stack>
      <Stack gap={10}><H2>有库 drafting 文本</H2><Text style={{lineHeight:1.7}}>{active.drafting}</Text></Stack>
    </Grid>
    <Text tone="secondary">主 Agent 的条件已知、非盲句子功能观察：{active.finding}</Text>
    <Text>关注：是否形成发现—证据—限制的关系；数字是否支撑关键比较；是否遗漏反例；“this packet” 等内部评测措辞是否漏入论文。数值更少本身不是优势。</Text>
    <Divider/>
    <H2>同查询、同记录、同预算的上下文体积</H2>
    <Table headers={["任务", "完整 reference（字符）", "drafting（字符）"]} rows={[
      ["T01",15043,10588],["T02",12590,9738],["T03",15090,10737],["T04",16023,11560],
    ]} columnAlign={["left","right","right"]}/>
    <Text tone="secondary">合计 58,746 → 42,623 字符，约减少 27.4%。不含用户事实、宿主指令、工具封装；不是 token、推理延迟或质量提升测量。4 个写作包的哈希已重放核对，默认 reference 不变。</Text>
    <H2>公开一级来源与可复核记录</H2>
    <Row wrap gap={20}>
      <a href="https://roboticsproceedings.org/rss21/p017.html" style={{color:theme.text.link}}>OpenVLA-OFT · RSS 2025</a>
      <a href="https://proceedings.mlr.press/v267/liu25p.html" style={{color:theme.text.link}}>Continual RL · ICML 2025</a>
      <a href="https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GeoWorld_Geometric_World_Models_CVPR_2026_paper.html" style={{color:theme.text.link}}>GeoWorld · CVPR 2026</a>
    </Row>
    <Text tone="secondary">所选论文不在候选提交的 337 个来源记录中，但模型预训练重合未知。没有向生成者提供作者分析段落；未进行全面来源重合检测。</Text>
    <Text>下一步：用你的实验表、表注／指标定义和原段落做私有验证；在新任务上预先平衡位置，并增加人类或跨模型判断。不要把本轮胜出文本变成评分答案或语料模板。</Text>
    <Text tone="tertiary">候选 6825f0b · 功能分支 feat/real-table-transfer-validation · 语料仍为 278 词条／337 来源／300 篇 2021–2025 核心论文。仓库报告和原始记录是证据源，Canvas 是阅读伴侣。</Text>
  </Stack>;
}
