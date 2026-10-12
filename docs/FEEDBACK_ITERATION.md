# 测试反馈完善记录：检索与实验语义，2026-10-12

## 这一轮解决了什么

本轮以 `9890df2863c51b09bed9635b5938affe44fbb109` 为对照，用相同的
8 个技术查询在隔离旧 checkout 和当前功能 checkout 上复测。
原版 `matched interaction budget` 对应词条排第 4，`model query latency`
把通用 3D-VLA 定义排在延迟用法前面；`confidence interval` 没有领域内
技术候选，`percentage points` 只有 success-rate 词条。正向搭配存在于
字典，但未被检索使用；通用统计表达也会被技术轮的领域／主题筛选漏掉。

完整查询、参数、前后 top-4 和限制保存在
[`feedback_retrieval_2026-10.json`](../library/studies/feedback_retrieval_2026-10.json)。
目前这 8 个开发查询的首条结果都对应维护者指定的概念；这不是留出集
准确率，也没有隔离“内容修改”和“排序修改”各自的贡献，更不是论文
写作偏好或专业度提升。原有 42 项检索评测不改题目、不放宽门槛。

## 架构上的修订

采用 [ADR-007](adr/ADR-007-positive-lexical-retrieval-and-reporting-scope.md)：

- 共享纯函数 `scripts/retrieval.py`，完整 expression／正向搭配匹配优先于
  偶然关键词重叠，旧分数仍用于其余排序；只规范大小写和连字符／空格。
- 反例、`avoid` 和不可互换词不作为正向匹配别名；这不等于普通关键词
  检索完全不读警示文字，也不是自动语义判断。
- 明确跨领域适用的报告用法用现有受控 `domains` 标注；技术轮仍排除
  只属于 general 的通用风格记录。完整匹配不能绕过领域和主题筛选。
- 仓库与独立 Skill 共用同一份匹配实现，增加字节一致性和实际调用测试。
  没有新增向量服务、数值权重调参、依赖、必读目录或第二本字典。
- 末端中文路径检查发现“百分点”无别名而无法命中，已补齐百分点、
  相对百分比变化，并把置信区间别名精确到该概念。两种消费者均测试。

静态 [架构图](assets/ai-writing-architecture.svg) 已同步；交互 Canvas
只是阅读伴侣，不成为规范数据源。

## 内容：两条新增，六条增强

新增 confidence interval 和 percentage-point difference 两条用法记录，
它们分别解释统计量的不确定性与绝对／相对差异；已有
`result-absolute-relative` 句式继续负责表达结构，不复制成新句式集合。

增强现有 latency、systematic generalization、objective mismatch、return、
generalization axis、metric direction／aggregation 六条记录，补齐词性、
语义范围、正向搭配、不可随意互换的概念和同一事实下的正反例。
全部例句和对照由维护者原创；不能把假设事实或模板槽位带进真实结果。

特别修正两种容易制造流畅但错误叙事的指导：

- zero-shot 的目标域适配条件与 held-out 因素分别报告；不能从不做目标
  适配推断预训练完全没见过该概念，也不能把 target-task fine-tuning
  重命名为 zero-shot。
- 较低预测误差不自动证明较高控制回报；没有机制证据时报告两项观察，
  不强填“因为某机制而失败／提升”的解释。

当前为 **278 条词条、337 条来源、14 条可选语义剖析**。规格仍为
12 条，章节协议仍为 17 个，任务路由仍为 19 个，写作套件仍为 47 题。
300 篇核心集合及其 2021–2025 边界保持冻结；新增统计经典来源计入总
来源，不伪装为新核心覆盖。核心集合并非已滚动覆盖 2026 年论文。

一级来源核验定位：

- [Agarwal et al., NeurIPS 2021](https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html)：Section 2、Figure 2 和 Section 4.1，核对点估计、区间、不独立的观测单位和跨任务重采样边界；不把该协议强加到所有机器人试验。
- [VIMA, ICML 2023](https://proceedings.mlr.press/v202/jiang23b.html)：Section 3 / Figure 2 的四种泛化条件，Section 5 的无进一步 fine-tuning 评估；不把一种划分写成 zero-shot 的全局定义。
- [OpenVLA 的官方出版页](https://proceedings.mlr.press/v270/kim25c.html)和[作者 v3 全文](https://arxiv.org/html/2406.09246v3)：Section 5.2、5.4、Discussion，核对目标域适配和模型服务／控制设置；出版年份沿用已有元数据，不导入论文实验数字。
- [BECAUSE, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/cff98e0b76e05fd1df5c9256724b3af1-Abstract-Conference.html)：核对模型预测目标与控制目标不一致的概念，不借其因果解释填补用户未提供的机制。
- [SAC, ICML 2018](https://proceedings.mlr.press/v80/haarnoja18b.html)：Section 3–4 的奖励／目标与折扣约定；报告指标仍以作者给出的评估协议为准。

## 工程验收合同与边界

验收要求：保留单协议、双轮检索和旧预算；可复现原缺陷；正确排除错
领域／错主题词条和非正向别名；root／portable 同步；旧统计、写作和
核心覆盖合同不变。回归范围包括排序、字段过滤、构建卡片、领域目录、
单文件路由和独立 Skill。无新增服务、密钥、网络调用或数据迁移。

原生验收：`make check` 通过 **104 项测试、42/42 检索评测**，重建无
生成漂移；Python 编译与 `git diff --check` 通过。仓库外独立
`lookup.py` 的中英文检索、输出预算与镜像一致性通过。新增 9 项反馈
合同测试，未放宽旧预算或 47 道写作题目。SVG 经 1800×1120 原生
WebKit 渲染并人工查看；目标 Canvas 文件严格 TypeScript 检查通过，
并非整个 Canvas 工作区认证，实际 IDE 宿主交互未自动测试。
未执行的写作盲评不得从这些工程结果推断通过。

上下文实测（四个领域，实验分析协议，limit 4，max-chars 24000）：
8 个 Markdown／JSON 包均成功，输出为 20,355–23,876 字符；4 个 JSON
包都保留 rhetoric 和 technical 两轮，预算内各保留 2 条完整记录。
core 仍为 12,143 字节，analysis 协议仍为 8,917 字节；四个实验单路由
为 19,939–22,142 字节，未增加原有门槛。字符／字节不等于 token 数，
也不宣称扩充后 token 更少或每轮都能返回 limit 个记录。

治理边界：同一 Skill 所有者、独立实现、原论文不再分发、观察到的本地
能力与 capability card 一致。原生治理合同与负例覆盖已通过；未执行
新的模型激活识别试验，没有安装或更新全局 Forge 注册表，也不声称
获得全局治理认证。本轮交付判定为 **CONDITIONAL**：工程行为可验收，
真实写作收益未验证。

## 最大的剩余问题：真实写作效果

历史 38 对 Qwen 配置的盲评未建立普遍收益：有库平均 3.89，无库 4.53，
7 项效果门槛失败 5 项。旧报告和旧题目冻结保留；此次没有重评它们来
制造“提升”。本地既有 vLLM、Ollama、LM Studio 的只读健康检查均连接
失败，未启动模型、购买服务或使用凭据；尚无新的独立双臂生成与评分。

下一轮优先执行实验分析、独立段落保真、延迟 caption、zero-shot／
fine-tuning 区分四类任务的隔离有库／无库测试。固定相同事实、模型和
解码条件，独立生成与盲评；不得给评分者条件映射或隐藏检查。关注
叙事推进、数值归属、概念准确性、材料遗漏和无证据机制；不以“更少
数字”评分。使用已有 benchmark 协议，保留不利结果和跨模型边界。
该阶段需要独立 Agent 授权或用户指定可用模型端点。
