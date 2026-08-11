# Super Library pack: vision_language_action

Corpus `0.4.0` · snapshot `2026-08-09`.

These are paraphrases, canonical terms, and original sentence patterns.
Verify technical claims in the linked primary sources before citing them.
Read the [selective agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) and [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md) before using this exhaustive pack.

### 3D vision-language-action generative world model (paper-specific usage)

`emb.definition.3d-vla-world-model.001` · definition · embodied_ai, robot_learning, world_models, vision_language_action · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

In 3D-VLA, a model that uses 3D scene information and language-conditioned representations to generate future scene or action-related predictions for embodied manipulation.

**Use:** Attribute this formulation to the specific paper and describe its generated variables. Do not present the phrase as a universally standardized VLA architecture.

**Avoid:** Do not infer that every 3D-grounded VLA is a world model or that every world model predicts robot actions.

**Patterns:**

- Following {source}, we use '3D VLA world model' for a model that predicts {paper-specific outputs}.
- Our system differs because it predicts {actions only or future observations only}.

**Verify in primary sources:**

- `zhen2024vla` — [3D-VLA: A 3D Vision-Language-Action Generative World Model](https://proceedings.mlr.press/v235/zhen24a.html) (ICML 2024)

### action chunking

`emb.definition.action-chunking.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Predicting a block of consecutive future actions in one policy inference step rather than predicting only the next action.

**Use:** Report chunk length, execution or replanning frequency, overlap between chunks, and whether observations are incorporated again before the entire chunk is executed.

**Avoid:** Do not equate action chunking with open-loop execution; implementations may replan or aggregate overlapping chunks.

**Patterns:**

- The policy predicts a chunk of {k} future actions from the current observations.
- We replan every {n} control steps and combine overlapping action chunks with {aggregation rule}.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

### bimanual robotic manipulation

`emb.definition.bimanual-manipulation.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Manipulation in which two robot arms or end effectors must act in a coordinated manner to accomplish a task.

**Use:** Specify whether coordination is symmetric or asymmetric, the control space for each arm, sensing, synchronization, and the task phase requiring coordination.

**Avoid:** Do not call independent single-arm subtasks bimanual coordination unless their actions are coupled by the object or objective.

**Patterns:**

- The benchmark contains contact-rich bimanual tasks that require coordinated motion of both end effectors.
- The policy jointly predicts left- and right-arm actions at {frequency} Hz.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)

### cross-robot data mixture

`emb.definition.cross-robot-data-mixture.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A training collection that combines trajectories from multiple robot platforms, embodiments, institutions, tasks, or data-generation pipelines.

**Use:** Report contributing datasets, sampling weights, action and observation normalization, license or availability constraints, and the target platforms used for evaluation.

**Avoid:** Do not equate a large aggregate trajectory count with balanced coverage across robots or tasks.

**Patterns:**

- We pretrain on a cross-robot mixture and fine-tune on demonstrations from the target embodiment.
- The mixture sampling weights are chosen by {rule} rather than in proportion to raw dataset size.

**Verify in primary sources:**

- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)
- `ghosh2024octo` — [Octo: An Open-Source Generalist Robot Policy](https://www.roboticsproceedings.org/rss20/p090.html) (RSS 2024)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)

### embodied multimodal language model

`emb.definition.embodied-language-model.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A language-model-based system that directly incorporates continuous or encoded sensor modalities to support reasoning or prediction grounded in an embodied environment.

**Use:** Specify the sensor encoders, how their outputs enter the language model, the training tasks, and whether the system predicts language, plans, values, or executable actions.

**Avoid:** Do not assume that multimodal grounding alone makes the model a closed-loop robot controller.

**Patterns:**

- The embodied language model interleaves visual and state-estimation embeddings with text tokens.
- The model supports {planning or question answering}, while a separate controller executes robot actions.

**Verify in primary sources:**

- `driess2023palme` — [PaLM-E: An Embodied Multimodal Language Model](https://proceedings.mlr.press/v202/driess23a.html) (ICML 2023)

### embodied reasoning

`emb.definition.embodied-reasoning.001` · definition · embodied_ai, vision_language_action · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Intermediate inference grounded in an agent's observations and task, such as spatial relations, action consequences, or subgoal structure, produced between perception and control so that decisions follow from stated premises rather than direct pattern matching.

**Use:** State the reasoning format (language, keypoints, or plans), what grounds it (images, scene metadata, demonstrations), and how it is supervised or rewarded. Evaluate reasoning quality separately from downstream control success when the benchmark allows it.

**Avoid:** Do not call generic chain-of-thought embodied reasoning when it never conditions on the agent's observations or task state, and do not report reasoning-benchmark gains as control gains without a control evaluation.

**Patterns:**

- The model produces {reasoning form} conditioned on {observation and task context} before predicting {action or keypoint}.
- We evaluate embodied reasoning on {reasoning benchmark} and report control success separately on {control tasks}.

**Verify in primary sources:**

- `kim2025-robot-r1-reinforcement-learning` — [Robot-R1: Reinforcement Learning for Enhanced Embodied Reasoning in Robotics](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ec46d737282bb408e642ed883a145c40-Abstract-Conference.html) (NeurIPS 2025)

### mobile manipulation

`emb.definition.mobile-manipulation.001` · definition · embodied_ai, robot_learning, vision_language_action · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A robot task family in which a mobile base and a manipulator are controlled together, so task success depends on coordinating base placement or motion with arm trajectories rather than manipulating from a fixed base.

**Use:** State how base and arm are coordinated (a joint policy, decoupled planning, or bi-level optimization), what determines base placement, and which fixed-base assumptions still hold. Report navigation and manipulation outcomes separately when the evaluation allows it.

**Avoid:** Do not present fixed-base manipulation results as mobile manipulation, and do not silently reduce the problem to navigation followed by independent manipulation without stating that decoupling.

**Patterns:**

- The mobile manipulation policy coordinates {base motion} with {end-effector trajectory} to accomplish {task goal}.
- Base waypoints are selected to satisfy {feasibility criterion}, after which the arm executes {manipulation primitive}.

**Verify in primary sources:**

- `wu2025-momanipvla-transferring-vision-language` — [MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html) (CVPR 2025)

### multimodal task prompt

`emb.definition.multimodal-prompt.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A task specification composed of more than one modality, such as interleaved text, images, object crops, goals, or demonstrations.

**Use:** List the modalities, tokenization, temporal order, and information available at test time. Distinguish a prompt that specifies a task from observations generated while executing it.

**Avoid:** Do not call ordinary multimodal observations a task prompt unless they communicate the intended task or goal.

**Patterns:**

- The prompt interleaves a language instruction with images of the target objects.
- We evaluate novel compositions of visual and textual prompt elements.

**Verify in primary sources:**

- `jiang2023vima` — [VIMA: Robot Manipulation with Multimodal Prompts](https://proceedings.mlr.press/v202/jiang23b.html) (ICML 2023)

### vision-language-action (VLA) model

`emb.definition.vla.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A model or policy that conditions on visual observations and language and produces robot actions or an action representation for embodied control.

**Use:** Specify all inputs, the action space, control frequency, training data, and whether actions are generated directly, discretized as tokens, or decoded by a separate head.

**Avoid:** Do not call a vision-language model a VLA merely because its textual output can be interpreted by an external planner.

**Patterns:**

- The VLA policy maps camera observations and a language instruction to a sequence of robot actions.
- We fine-tune the pretrained VLA on {number} demonstrations from {target embodiment}.

**Verify in primary sources:**

- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)
- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)
- `zhen2024vla` — [3D-VLA: A 3D Vision-Language-Action Generative World Model](https://proceedings.mlr.press/v235/zhen24a.html) (ICML 2024)

### hierarchical policy

`rl.definition.hierarchical-policy.001` · definition · reinforcement_learning, vision_language_action · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A control architecture that decomposes decision making across levels, where a high-level policy selects subgoals, skills, or intermediate commands at a coarser timescale and one or more low-level policies execute them as primitive actions.

**Use:** Specify what the high level outputs (subgoals, skills, or language commands), the timescales of the levels, how each level is trained (jointly, separately, or with frozen components), and how the interface between levels is constrained or grounded so low-level execution stays feasible.

**Avoid:** Do not call a pipeline hierarchical merely because it contains multiple modules; the levels must operate at different decision timescales or abstraction levels with a defined interface.

**Patterns:**

- The high-level policy proposes {subgoal or command} every {decision interval}, and the low-level policy executes {primitive actions} conditioned on it.
- We restrict the high-level action space to {reachable or grounded set} so that low-level execution remains feasible.

**Verify in primary sources:**

- `shi2025-hi-robot-open-ended` — [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://proceedings.mlr.press/v267/shi25d.html) (ICML 2025)
- `zhang2023-adjacency-constraint-efficient-hierarchical` — [Adjacency Constraint for Efficient Hierarchical Reinforcement Learning](https://doi.org/10.1109/tpami.2022.3192418) (TPAMI 2023)

### chain-of-affordance reasoning

`vla.definition.chain-of-affordance.001` · definition · vision_language_action, embodied_ai · related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An intermediate reasoning formulation that decomposes a manipulation instruction into action-relevant object, spatial, or interaction affordances before control prediction.

**Use:** State the intermediate representation, its supervision, and whether it is generated explicitly at inference time.

**Avoid:** Do not treat an interpretable-looking intermediate output as causal evidence that the policy used the stated reasoning process.

**Patterns:**

- The model predicts {affordance representation} as an intermediate target before decoding {robot action}.

**Verify in primary sources:**

- `li2025-coa-vla-improving-vision` — [CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance](https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html) (ICCV 2025)
- `zhao2025-cot-vla-visual-chain` — [CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html) (CVPR 2025)

### continuous action head

`vla.definition.continuous-action-head.001` · definition · vision_language_action, robot_learning · method, related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A policy output module that directly parameterizes continuous robot controls rather than representing every action dimension as a discrete language token.

**Use:** Specify the distribution or regression objective, action parameterization, prediction horizon, and embodiment-specific output dimensions.

**Avoid:** Do not use this term as a synonym for the entire policy or assume that a continuous head eliminates temporal discretization.

**Patterns:**

- The continuous action head maps {fused representation} to {horizon} steps of {action parameterization}.

**Verify in primary sources:**

- `hou2025-dita-scaling-diffusion-transformer` — [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html) (ICCV 2025)
- `wen2025-diffusionvla-scaling-robot-foundation` — [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://proceedings.mlr.press/v267/wen25g.html) (ICML 2025)

### latent action representation

`wm.definition.latent-action-representation.001` · definition · world_models, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A learned variable inferred from observation transitions or videos to encode action-like changes when the corresponding low-level action labels are absent, often for conditioning a predictive model or later alignment with executable controls.

**Use:** State the inference inputs, temporal granularity, discrete or continuous parameterization, training objective, and how the latent variable is aligned with or decoded into the target robot action space.

**Avoid:** Do not call a motion code an executable robot action before validating its alignment or decoder, and do not assume that a latent action is identifiable, causal, or embodiment-invariant by construction.

**Patterns:**

- An inverse model infers a latent action from adjacent observations, and the world model predicts the next observation conditioned on that code.
- During robot fine-tuning, latent actions are aligned with {target control representation} using {paired supervision}.

**Verify in primary sources:**

- `zhang2024-prelar-world-model-pre` — [PreLAR: World Model Pre-training with Learnable Action Representation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3363_ECCV_2024_paper.php) (ECCV 2024)
- `schmidt2024-learning-act-without-actions` — [Learning to Act without Actions](https://openreview.net/forum?id=rvUq3cxpDF) (ICLR 2024)
- `gao2025-adaworld-learning-adaptable-world-models` — [AdaWorld: Learning Adaptable World Models with Latent Actions](https://proceedings.mlr.press/v267/gao25u.html) (ICML 2025)

### Latency is measured on {hardware} with {precision, batch, and timing boundary}.

`general.sentence-pattern.latency-protocol.001` · sentence_pattern · general, robot_learning, vision_language_action · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines the hardware and measurement boundary required to interpret latency.

**Use:** State warm-up, synchronization, repeats, input shape, preprocessing, action decoding, and whether the value is model-only or end to end.

**Avoid:** Do not compare latency across hardware or confuse batched throughput with single-sample latency.

**Patterns:**

- Latency is measured on {hardware} at {precision} and batch size {value}, including {timing boundary}.
- End-to-end control latency includes {components} and is averaged over {repetitions} after {warm-up}.

### Each real-system condition is evaluated in {trials} trials, with success defined as {criterion}.

`general.sentence-pattern.real-system-trials.001` · sentence_pattern · general, embodied_ai, robot_learning, vision_language_action · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines the trial count and success criterion for a physical or deployed-system evaluation.

**Use:** Also state reset procedure, intervention policy, trial independence, task allocation, and the denominator used for success rate.

**Avoid:** Do not report a success percentage without the number and composition of physical trials.

**Patterns:**

- Each real-robot task is evaluated in {trials} trials, with success defined as {terminal condition}.
- We conduct {number} trials per {task and object} pair and count an intervention as {outcome}.

### VLA systems should be compared by backbone adaptation, action representation, supervision, and feedback regime.

`vla.sentence-pattern.related-work.001` · sentence_pattern · vision_language_action · related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

A compact Related Work organizer that prevents VLA papers with materially different training and control interfaces from being collapsed into one family.

**Use:** Select only axes relevant to the cited papers and attach verified citations to each factual grouping.

**Avoid:** Do not rank systems across unmatched robots, demonstrations, tasks, or evaluation protocols.

**Patterns:**

- Existing VLA systems differ in whether they {backbone adaptation}, represent actions as {representation}, learn from {supervision}, and execute under {feedback regime}.

### robot-action tokenization

`emb.term.action-tokenization.001` · term · embodied_ai, robot_learning, vision_language_action · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A representation that maps continuous or structured robot controls into discrete tokens or token-like outputs for sequence-model prediction.

**Use:** Describe discretization bins, dimensions, control semantics, decoding, clipping, and any embodiment-specific normalization.

**Avoid:** Do not assume that language-token and action-token probabilities have the same semantics or that tokenization is lossless.

**Patterns:**

- Each action dimension is discretized into {number} bins and represented by a dedicated token range.
- The predicted action tokens are decoded into {control command} at {frequency} Hz.

**Verify in primary sources:**

- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)

### language-conditioned visuomotor policy

`emb.term.language-conditioned-policy.001` · term · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A control policy whose action prediction depends jointly on sensory observations and a linguistic task specification or instruction.

**Use:** State the language granularity, observation modalities, action horizon, and whether language changes the task, goal, or low-level behavior.

**Avoid:** Do not imply compositional language understanding unless it is evaluated under an appropriate held-out split.

**Patterns:**

- The language-conditioned policy predicts actions from {camera views}, proprioception, and the instruction.
- We evaluate whether the policy follows unseen combinations of familiar language concepts.

**Verify in primary sources:**

- `brohan2023rt1` — [RT-1: Robotics Transformer for Real-World Control at Scale](https://roboticsproceedings.org/rss19/p025.html) (RSS 2023)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)
- `jiang2023vima` — [VIMA: Robot Manipulation with Multimodal Prompts](https://proceedings.mlr.press/v202/jiang23b.html) (ICML 2023)

### task success rate

`emb.term.task-success-rate.001` · term · embodied_ai, robot_learning, vision_language_action · experiments, rebuttal, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The fraction or percentage of evaluation trials that satisfy a predefined task-completion criterion.

**Use:** Define the success criterion, trial unit, number of trials, aggregation level, and treatment of partial completion and timeouts. Provide uncertainty where appropriate.

**Avoid:** Do not compare success rates computed with different horizons, reset policies, human interventions, or success detectors without qualification.

**Patterns:**

- Task success rate is computed over {number} independent trials using {completion criterion}.
- The policy succeeds in {count}/{total} trials, corresponding to {percentage}%.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)
- `jiang2023vima` — [VIMA: Robot Manipulation with Multimodal Prompts](https://proceedings.mlr.press/v202/jiang23b.html) (ICML 2023)

### teleoperated robot demonstration

`emb.term.teleoperation-demonstration.001` · term · embodied_ai, robot_learning, vision_language_action · related_work, method, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A robot trajectory collected while a human operator controls the robot through a physical, graphical, wearable, or other remote interface.

**Use:** Report the interface, observation available to the operator, control rate, filtering, intervention policy, and whether unsuccessful attempts are retained.

**Avoid:** Do not use 'human demonstration' without distinguishing robot teleoperation from videos or state–action data generated outside the target robot.

**Patterns:**

- We collect {number} teleoperated demonstrations with a leader–follower interface.
- The dataset retains both successful and unsuccessful teleoperation episodes.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)
- `khazatsky2024droid` — [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://roboticsproceedings.org/rss20/p120.html) (RSS 2024)

### temporal ensembling of overlapping action predictions

`emb.term.temporal-ensembling.001` · term · embodied_ai, robot_learning, vision_language_action · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Combining action predictions made at different policy-query times for the same future control step.

**Use:** Describe the weighting function, overlap window, and whether aggregation occurs in action space or another representation. Mark ACT-specific weighting choices as implementation details rather than universal definitions.

**Avoid:** Do not confuse temporal ensembling with an ensemble of independently trained policies.

**Patterns:**

- At each control step, we aggregate overlapping action predictions using exponentially decaying weights.
- Temporal ensembling smooths predictions from successive action chunks.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)

### action expert

`vla.term.action-expert.001` · term · vision_language_action, robot_learning · abstract, introduction, method, related_work

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A specialized policy component that converts multimodal representations into robot actions, often alongside a pretrained vision-language backbone.

**Use:** Describe which parameters are specialized, how information is exchanged with the backbone, and whether the expert is autoregressive, diffusion-based, or otherwise structured.

**Avoid:** Do not imply a standardized architecture; action expert is an architectural role whose realization varies by paper.

**Patterns:**

- An action expert conditions on {backbone features} and predicts {action representation} for {robot embodiment}.

**Verify in primary sources:**

- `wen2025-diffusionvla-scaling-robot-foundation` — [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://proceedings.mlr.press/v267/wen25g.html) (ICML 2025)
- `hou2025-dita-scaling-diffusion-transformer` — [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html) (ICCV 2025)

### action vocabulary / action-token vocabulary

`vla.term.action-vocabulary.001` · term · vision_language_action, robot_learning · abstract, introduction, related_work, method

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The discrete set of symbols used to encode robot actions when a policy casts action prediction as token generation.

**Use:** State how continuous controls are quantized, which action dimensions are covered, and whether the vocabulary is shared across embodiments.

**Avoid:** Do not imply that discretization is inherent to all VLA models; many policies retain continuous action heads.

**Patterns:**

- We quantize {action dimensions} into an action vocabulary of {size} tokens and decode each predicted token into {control command}.

**Verify in primary sources:**

- `wang2025-vq-vla-improving-vision` — [VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html) (ICCV 2025)
- `chen2025-moto-latent-motion-token` — [Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.html) (ICCV 2025)

### embodiment-specific action decoder

`vla.term.embodiment-specific-decoder.001` · term · vision_language_action, robot_learning · method, related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A decoder specialized to the action space or control interface of one robot embodiment while upstream representations may be shared.

**Use:** Name the shared representation, embodiment identifier, action dimensions, and which decoder parameters remain robot-specific.

**Avoid:** Do not claim cross-embodiment transfer from a shared backbone alone; establish what transfers and what is retrained.

**Patterns:**

- We share {representation} across robots and use an embodiment-specific decoder for {action space}.

**Verify in primary sources:**

- `yuan2025-cross-embodiment-dexterous-grasping` — [Cross-Embodiment Dexterous Grasping with Reinforcement Learning](https://iclr.cc/virtual/2025/poster/28010) (ICLR 2025)
- `miao2025-fedvla-federated-vision-language` — [FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation](https://openaccess.thecvf.com/content/ICCV2025/html/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.html) (ICCV 2025)

### visual trace prompting

`vla.term.visual-trace-prompting.001` · term · vision_language_action, robot_learning · related_work, method

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A prompting mechanism that augments visual input with spatial or temporal traces intended to expose task-relevant motion structure to a policy.

**Use:** Identify how traces are produced, whether they are available at training and inference time, and what spatial-temporal information they encode.

**Avoid:** Do not generalize the mechanism beyond the paper-specific trace construction without evidence.

**Patterns:**

- Visual trace prompting supplies {trace type} to highlight {spatial-temporal relation} before action prediction.

**Verify in primary sources:**

- `zheng2025-tracevla-visual-trace-prompting` — [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://iclr.cc/virtual/2025/poster/29130) (ICLR 2025)

### separate prediction horizon, execution horizon, and feedback frequency

`emb.usage-note.chunking-feedback.001` · usage_note · embodied_ai, robot_learning, vision_language_action · method, experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A policy may predict many future actions while executing only part of them before receiving a new observation, so action horizon alone does not determine whether control is open-loop or closed-loop.

**Use:** Report all three quantities and explain how overlapping predictions are combined. Use 'closed-loop' only when updated observations influence subsequent executed actions.

**Avoid:** Do not infer the control-feedback structure solely from the number of actions output by the network.

**Patterns:**

- Although the policy predicts {k} actions, it replans after executing {n}, using a new observation.
- The controller executes the entire chunk open-loop before the next policy query.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

### heterogeneous robot action spaces require an explicit alignment strategy

`emb.usage-note.heterogeneous-actions.001` · usage_note · embodied_ai, robot_learning, vision_language_action · related_work, method, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Different datasets and embodiments may use controls with different dimensions, frames, grippers, rates, and semantics, so joint training requires a documented representation or adapter.

**Use:** Specify coordinate frames, normalization, missing dimensions, embodiment identifiers, and decoding into each robot's native controller.

**Avoid:** Do not describe actions as standardized when only file formats are shared but control semantics remain different.

**Patterns:**

- We map each dataset's controls into a common {representation} and retain an embodiment-specific action mask.
- Actions are normalized per embodiment before joint training and decoded with {adapter}.

**Verify in primary sources:**

- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)
- `ghosh2024octo` — [Octo: An Open-Source Generalist Robot Policy](https://www.roboticsproceedings.org/rss20/p090.html) (RSS 2024)

### evaluate embodied generalization along separately controlled axes

`emb.usage-note.systematic-generalization.001` · usage_note · embodied_ai, robot_learning, vision_language_action · experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Systematic evaluation varies identified factors—such as objects, placements, task templates, prompt compositions, environments, or embodiments—while documenting which combinations were withheld.

**Use:** Define each split procedurally and report results by axis. Use 'zero-shot' only when the evaluated factor or combination was absent from training under the stated protocol.

**Avoid:** Do not collapse all held-out conditions into one generalization score that hides qualitatively different shifts.

**Patterns:**

- We report separate results for unseen objects, unseen task compositions, and unseen embodiments.
- The hardest split holds out both {factor one} and {factor two} during training.

**Verify in primary sources:**

- `jiang2023vima` — [VIMA: Robot Manipulation with Multimodal Prompts](https://proceedings.mlr.press/v202/jiang23b.html) (ICML 2023)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)
- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)

### distinguish VLA policies from embodied language models

`emb.usage-note.vla-vs-elm.001` · usage_note · embodied_ai, robot_learning, vision_language_action · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A VLA label emphasizes action generation for control, whereas an embodied language model may use sensor inputs for reasoning or prediction without directly producing executable actions.

**Use:** Classify a method by its actual output and control interface rather than model backbone. Some systems may satisfy both descriptions, but the overlap should be stated.

**Avoid:** Do not use VLA, vision-language model, and embodied language model interchangeably.

**Patterns:**

- Unlike embodied language models evaluated on reasoning tasks, our VLA directly predicts {robot control representation}.
- The model supplies high-level plans to a separate low-level policy and is therefore not evaluated as an end-to-end VLA controller.

**Verify in primary sources:**

- `driess2023palme` — [PaLM-E: An Embodied Multimodal Language Model](https://proceedings.mlr.press/v202/driess23a.html) (ICML 2023)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)

### policy inference latency and control frequency

`vla.usage-note.control-latency.001` · usage_note · vision_language_action, robot_learning · experiments, limitations, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Inference latency measures computation time per policy update, while control frequency describes how often commands are issued; chunking and asynchronous execution can make them differ.

**Use:** Report hardware, batch size, observation resolution, action horizon, synchronization policy, latency statistic, and achieved control rate.

**Avoid:** Do not infer deployability from model size or nominal frequency alone.

**Patterns:**

- On {hardware}, the policy requires {latency statistic} per update and sustains {frequency} Hz with {execution scheme}.

**Verify in primary sources:**

- `hou2025-dita-scaling-diffusion-transformer` — [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html) (ICCV 2025)
- `zheng2025-tracevla-visual-trace-prompting` — [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://iclr.cc/virtual/2025/poster/29130) (ICLR 2025)

### open-loop action prediction versus closed-loop execution

`vla.usage-note.open-closed-loop.001` · usage_note · vision_language_action, robot_learning · method, experiments, related_work, limitations

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Open-loop prediction generates an action sequence without incorporating intermediate observations, whereas closed-loop execution refreshes observations and may replan during the sequence.

**Use:** Report prediction horizon, executed chunk length, observation refresh rate, and replanning frequency separately.

**Avoid:** Do not call a chunked policy fully closed-loop merely because a new chunk is eventually predicted.

**Patterns:**

- The policy predicts {prediction horizon} actions, executes {execution horizon}, and replans after receiving a new observation.

**Verify in primary sources:**

- `li2025-reinforcement-learning-action-chunking` — [Reinforcement Learning with Action Chunking](https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html) (NeurIPS 2025)
- `hou2025-dita-scaling-diffusion-transformer` — [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html) (ICCV 2025)

### separate multimodal pretraining from robot-policy fine-tuning

`vla.usage-note.pretrain-finetune.001` · usage_note · vision_language_action, robot_learning · method, experiments, related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Multimodal representation learning and action-policy optimization use different data, objectives, and sometimes different parameter subsets.

**Use:** Report each stage's data sources, objective, trainable parameters, robot supervision, and evaluation role.

**Avoid:** Do not describe all prior training as robot pretraining when much of it contains no robot actions.

**Patterns:**

- We first pretrain {modules} on {data and objective}, then fine-tune {parameters} on {robot demonstrations} for action prediction.

**Verify in primary sources:**

- `li2024-mastering-robot-manipulation-multimodal` — [Mastering Robot Manipulation with Multimodal Prompts through Pretraining and Multi-task Fine-tuning](https://proceedings.mlr.press/v235/li24x.html) (ICML 2024)
- `li2025-llara-supercharging-robot-learning` — [LLaRA: Supercharging Robot Learning Data for Vision-Language Policy](https://iclr.cc/virtual/2025/poster/28695) (ICLR 2025)
