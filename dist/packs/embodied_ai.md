# Super Library pack: embodied_ai

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

### active perception

`emb.definition.active-perception.001` · definition · embodied_ai, robot_learning · introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Perception in which an agent's actions influence which observations become available, coupling information acquisition with control.

**Use:** Describe the action-dependent sensing process and whether actions are chosen explicitly for information gain or jointly for task reward.

**Avoid:** Do not call ordinary data augmentation active perception.

**Patterns:**

- The task requires active perception because the agent must move to reveal {occluded or unobserved information}.
- Actions affect both {task progress} and the observations available for future decisions.

**Verify in primary sources:**

- `xia2018gibson` — [Gibson Env: Real-World Perception for Embodied Agents](https://openaccess.thecvf.com/content_cvpr_2018/html/Xia_Gibson_Env_Real-World_CVPR_2018_paper.html) (CVPR 2018)
- `savva2019habitat` — [Habitat: A Platform for Embodied AI Research](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) (ICCV 2019)

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

### cross-embodiment transfer

`emb.definition.cross-embodiment.001` · definition · robot_learning, embodied_ai · abstract, introduction, related_work, experiments, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The application or adaptation of learned knowledge across robots or agents with different morphologies, sensors, action spaces, or control interfaces.

**Use:** State whether transfer is zero-shot, requires fine-tuning, or only shares pretraining. Reserve 'generalization' for a held-out evaluation that directly supports it.

**Avoid:** Do not claim cross-embodiment generalization when every evaluated robot appears in training under the same interface.

**Patterns:**

- We evaluate cross-embodiment transfer by adapting the pretrained policy to {held-out robot} with {amount of data}.
- The embodiments differ in {morphology, camera setup, and action space}.

**Verify in primary sources:**

- `ghosh2024octo` — [Octo: An Open-Source Generalist Robot Policy](https://www.roboticsproceedings.org/rss20/p090.html) (RSS 2024)

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

### diffusion policy / action diffusion

`emb.definition.diffusion-policy.001` · definition · robot_learning, embodied_ai · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A policy that represents a conditional distribution over actions or action sequences through a denoising diffusion process.

**Use:** Specify the predicted horizon, conditioning observations, diffusion parameterization, sampling steps, and how generated actions are executed.

**Avoid:** Do not describe any stochastic policy as a diffusion policy.

**Patterns:**

- The diffusion policy generates an action sequence conditioned on {observation history}.
- At inference, we execute {action horizon} actions from each denoised sequence before replanning.

**Verify in primary sources:**

- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

### domain randomization

`emb.definition.domain-randomization.001` · definition · embodied_ai, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Training over deliberately varied simulation parameters to make a model robust across a distribution intended to cover or bracket variability encountered in the real system.

**Use:** List randomized parameters and distributions, and separate visual randomization from dynamics randomization. Whether the real domain lies within effective support is an empirical question.

**Avoid:** Do not use domain randomization as a generic label for ordinary image augmentation or claim coverage of the real domain without evaluation.

**Patterns:**

- During simulation training, we randomize {textures, lighting, camera, dynamics, or latency} over {specified ranges}.
- Domain randomization exposes the policy to {variation} before real-world deployment.

**Verify in primary sources:**

- `tobin2017domainrandomization` — [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://ieeexplore.ieee.org/document/8202133/) (IROS 2017)

### embodied AI

`emb.definition.embodied-ai.001` · definition · embodied_ai, robot_learning · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The study of agents that perceive and act within an environment, where their observations, actions, and learning are shaped by embodiment and closed-loop interaction.

**Use:** Specify the body, sensors, action space, environment, and task. For simulated agents, state which physical or interaction constraints are modeled.

**Avoid:** Do not use 'embodied' for a passive model that only processes a fixed image or text dataset without an interaction formulation.

**Patterns:**

- We study embodied AI agents that perceive {sensory inputs} and act through {action space} in {environment}.
- The agent's observations depend on its previous actions, creating a closed perception–action loop.

**Verify in primary sources:**

- `xia2018gibson` — [Gibson Env: Real-World Perception for Embodied Agents](https://openaccess.thecvf.com/content_cvpr_2018/html/Xia_Gibson_Env_Real-World_CVPR_2018_paper.html) (CVPR 2018)
- `savva2019habitat` — [Habitat: A Platform for Embodied AI Research](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) (ICCV 2019)

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

### embodied question answering (EQA)

`emb.definition.embodied-question-answering.001` · definition · embodied_ai · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An embodied-agent task in which a system uses observations acquired from an environment, through a provided observation history or active exploration, to answer natural-language questions about that environment.

**Use:** Specify whether the agent receives episodic memory or explores actively, the observation modalities, question and answer format, environment split, exploration budget, memory access, and scoring protocol. For knowledge-based EQA, distinguish evidence observed in the environment from external knowledge used for reasoning.

**Avoid:** Do not call static image question answering EQA when the system has no embodied observation history, exploration process, or environment-grounded evidence acquisition.

**Patterns:**

- The EQA agent explores {environment} for at most {budget} steps before producing a natural-language answer.
- We evaluate episodic-memory and active-exploration EQA under {environment split and scoring protocol}.

**Verify in primary sources:**

- `tan2023-knowledge-based-embodied-question` — [Knowledge-Based Embodied Question Answering](https://doi.org/10.1109/tpami.2023.3277206) (TPAMI 2023)
- `majumdar2024-openeqa-embodied-question-answering` — [OpenEQA: Embodied Question Answering in the Era of Foundation Models](https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html) (CVPR 2024)

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

### generalist robot policy

`emb.definition.generalist-policy.001` · definition · robot_learning, embodied_ai · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A policy trained across diverse tasks, environments, or robot data with the aim of supporting multiple behaviors and transfer beyond a single narrowly trained task.

**Use:** State the diversity actually represented in training and evaluation. Distinguish multi-task performance, zero-shot generalization, and fine-tuning ability.

**Avoid:** Do not call a policy generalist solely because one architecture is reused across several separately trained tasks.

**Patterns:**

- We train a generalist robot policy on {tasks, environments, and embodiments}.
- We separately evaluate in-distribution multi-task performance and transfer to {new setting}.

**Verify in primary sources:**

- `brohan2023rt1` — [RT-1: Robotics Transformer for Real-World Control at Scale](https://roboticsproceedings.org/rss19/p025.html) (RSS 2023)
- `ghosh2024octo` — [Octo: An Open-Source Generalist Robot Policy](https://www.roboticsproceedings.org/rss20/p090.html) (RSS 2024)
- `khazatsky2024droid` — [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://roboticsproceedings.org/rss20/p120.html) (RSS 2024)

### grounded instruction following

`emb.definition.grounded-instruction.001` · definition · embodied_ai, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Mapping linguistic instructions to actions by relating language to perceived entities, spatial relations, state changes, and interaction possibilities in the environment.

**Use:** State the grounding modalities and whether supervision includes demonstrations, symbolic plans, object annotations, or only task success.

**Avoid:** Do not claim grounding when language is used only as an opaque class label.

**Patterns:**

- The agent grounds {instruction phrase} in {visual entities and state changes} before selecting actions.
- We learn grounded instruction following from {demonstrations or interaction feedback}.

**Verify in primary sources:**

- `anderson2018vln` — [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html) (CVPR 2018)
- `shridhar2020alfred` — [ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html) (CVPR 2020)

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

### multimodal embodied perception

`emb.definition.multimodal-perception.001` · definition · embodied_ai, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Perception that integrates information from distinct sensory modalities, such as vision, audio, touch, language, or proprioception, for embodied decision making.

**Use:** Name the modalities and distinguish representation, alignment, fusion, translation, and co-learning. Explain which signals are available during training and deployment.

**Avoid:** Do not use multimodal to describe multiple views from the same modality without clarification.

**Patterns:**

- The agent fuses {vision} and {audio} to localize {target} from egocentric observations.
- We align {language} with {visual and proprioceptive representations} before action prediction.

**Verify in primary sources:**

- `chen2020soundspaces` — [SoundSpaces: Audio-Visual Navigation in 3D Environments](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123510018.pdf) (ECCV 2020)
- `baltrusaitis2019multimodal` — [Multimodal Machine Learning: A Survey and Taxonomy](https://ieeexplore.ieee.org/document/8269806/) (TPAMI 2019)

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

### object-goal navigation (ObjectNav)

`emb.definition.object-goal-navigation.001` · definition · embodied_ai · abstract, introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An embodied navigation task in which an agent must reach an instance of a target object category from egocentric observations.

**Use:** State target specification, sensors, environment split, success radius, stopping rule, and evaluation metrics such as success and path efficiency.

**Avoid:** Do not conflate ObjectNav with point-goal navigation, where the target is a coordinate.

**Patterns:**

- In ObjectNav, the agent receives {target category} and must navigate to a valid instance using {observations}.

**Verify in primary sources:**

- `zhu2025-move-understand-3d-scene` — [Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.html) (ICCV 2025)
- `liu2025-citywalker-learning-embodied-urban` — [CityWalker: Learning Embodied Urban Navigation from Web-Scale Videos](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_CityWalker_Learning_Embodied_Urban_Navigation_from_Web-Scale_Videos_CVPR_2025_paper.html) (CVPR 2025)

### open-vocabulary manipulation

`emb.definition.open-vocabulary-manipulation.001` · definition · embodied_ai, robot_learning · introduction, related_work, experiments

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Manipulation conditioned on object or task descriptions whose evaluation vocabulary is not restricted to a fixed closed set used during task-specific training.

**Use:** Define the held-out unit, language source, object and task splits, perception assumptions, and any foundation-model supervision.

**Avoid:** Do not claim open-vocabulary generalization when test names are new strings for training-seen objects or skills.

**Patterns:**

- We evaluate open-vocabulary manipulation on held-out {objects, concepts, or instructions} while holding {other axis} fixed.

**Verify in primary sources:**

- `wen2025-diffusionvla-scaling-robot-foundation` — [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://proceedings.mlr.press/v267/wen25g.html) (ICML 2025)
- `zhang2025-vlabench-large-scale-benchmark` — [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.html) (ICCV 2025)

### simulation-to-real (sim-to-real) transfer

`emb.definition.sim-to-real.001` · definition · embodied_ai, robot_learning · abstract, introduction, related_work, experiments, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Training or developing a model in simulation and deploying or adapting it to a physical system whose observations or dynamics differ from the simulator.

**Use:** Name what transfers, what is randomized or adapted, the real-world evaluation, and whether real data is used before deployment.

**Avoid:** Do not claim zero-shot sim-to-real if any real-world fine-tuning or calibration materially updates the policy.

**Patterns:**

- We evaluate zero-shot sim-to-real transfer by deploying the simulation-trained policy without {real-world policy updates}.
- The transfer gap arises from mismatches in {appearance, dynamics, sensing, or actuation}.

**Verify in primary sources:**

- `tobin2017domainrandomization` — [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://ieeexplore.ieee.org/document/8202133/) (IROS 2017)
- `kumar2021rma` — [RMA: Rapid Motor Adaptation for Legged Robots](https://roboticsproceedings.org/rss17/p011.html) (RSS 2021)

### synthetic data generation

`emb.definition.synthetic-data-generation.001` · definition · embodied_ai, robot_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Producing training scenes, trajectories, or annotations with generative or procedural models instead of collecting them from human operators or real environments, so dataset scale and diversity are limited by generation quality rather than collection effort.

**Use:** State what is generated (scenes, actions, or labels), the generative mechanism, how physical feasibility is enforced or filtered, and how much real data remains in the loop. Report downstream policy performance, not only generation fidelity or speed.

**Avoid:** Do not equate synthetic data generation with domain randomization, which varies parameters of an existing scene rather than generating new scenes or trajectories, and do not claim realism from visual quality alone.

**Patterns:**

- We generate {scenes or trajectories} from {conditioning input} with {generative model}, filtering samples that violate {feasibility check}.
- Policies trained on the generated data improve {metric} by {amount} over {human-collected baseline}.

**Verify in primary sources:**

- `lee2025-dynscene-scalable-generation-dynamic` — [DynScene: Scalable Generation of Dynamic Robotic Manipulation Scenes for Embodied AI](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DynScene_Scalable_Generation_of_Dynamic_Robotic_Manipulation_Scenes_for_Embodied_CVPR_2025_paper.html) (CVPR 2025)

### topological memory for visual navigation

`emb.definition.topological-memory.001` · definition · embodied_ai · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A graph-based spatial memory whose nodes represent selected observations, places, or landmarks and whose edges encode reachability, adjacency, or local navigational transitions for planning.

**Use:** Specify how nodes are created and merged, what an edge means, how the agent localizes or retrieves in the graph, whether the memory is updated online, and whether unexplored or predicted locations are represented.

**Avoid:** Do not call a dense occupancy grid or an arbitrary scene graph a topological memory unless nodes and edges support navigational connectivity or reachability.

**Patterns:**

- The agent incrementally builds a topological memory whose nodes store {observation features} and whose edges represent {reachability criterion}.
- Planning queries the memory for a path from {localized node} to {goal node or frontier}.

**Verify in primary sources:**

- `cui2024-frontier-enhanced-topological-memory` — [Frontier-enhanced Topological Memory with Improved Exploration Awareness for Embodied Visual Navigation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8905_ECCV_2024_paper.php) (ECCV 2024)
- `taniguchi2021-pose-invariant-topological-memory` — [Pose Invariant Topological Memory for Visual Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Taniguchi_Pose_Invariant_Topological_Memory_for_Visual_Navigation_ICCV_2021_paper.html) (ICCV 2021)

### visuomotor policy

`emb.definition.visuomotor-policy.001` · definition · robot_learning, embodied_ai · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A policy that maps visual observations, often together with proprioception or goals, to motor actions or action sequences.

**Use:** Specify visual inputs, auxiliary conditioning, action representation, control frequency, and whether perception and control are trained end to end.

**Avoid:** Do not call a pipeline visuomotor if vision only labels a dataset and is unavailable to the deployed controller.

**Patterns:**

- The visuomotor policy maps {image history and proprioception} to {action chunk}.
- We train the policy end to end from {visual input} to {robot command}.

**Verify in primary sources:**

- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)
- `gu2017asynchronous` — [Deep Reinforcement Learning for Robotic Manipulation with Asynchronous Off-Policy Updates](https://ieeexplore.ieee.org/document/7989385) (ICRA 2017)

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

### vision-and-language navigation (VLN)

`emb.definition.vln.001` · definition · embodied_ai · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A task in which an embodied agent follows a natural-language route instruction by grounding it in visual observations and selecting navigation actions.

**Use:** Specify environment type, action space, instruction source, navigation graph or continuous control, and generalization split.

**Avoid:** Do not conflate VLN with object-goal navigation that has no free-form instruction.

**Patterns:**

- In VLN, the agent maps a route instruction and a sequence of egocentric observations to navigation actions.
- We evaluate generalization to {unseen environments or instructions}.

**Verify in primary sources:**

- `anderson2018vln` — [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html) (CVPR 2018)

### AI feedback

`rl.definition.ai-feedback.001` · definition · reinforcement_learning, embodied_ai · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A training signal, such as rewards, preferences, or critiques, produced by a separate pretrained model that evaluates the learner's behavior, used in place of or in addition to environment reward or human feedback.

**Use:** Identify the evaluator model, what it scores, and how often it is queried; state how its judgments are validated and how exploitation of evaluator weaknesses is detected. Keep AI feedback distinct from reward models fit to environment reward and from direct human feedback.

**Avoid:** Do not present evaluator scores as ground-truth task success, and do not report gains from AI feedback without stating the evaluator's known failure modes.

**Patterns:**

- A {evaluator model} scores {agent behavior}, and the score is used as {reward or preference signal} during training.
- We validate AI feedback against {human labels or task metrics} on {validation set}.

**Verify in primary sources:**

- `li2025-larm-large-auto-regressive` — [LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence](https://proceedings.mlr.press/v267/li25dj.html) (ICML 2025)

### human-in-the-loop reinforcement learning

`rl.definition.human-in-the-loop-rl.001` · definition · reinforcement_learning, embodied_ai · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A training regime in which humans participate during learning, for example by intervening in control, providing demonstrations on demand, or shaping rewards, so the policy is optimized from both autonomous interaction and human guidance.

**Use:** Specify when and how humans intervene, how their input enters the objective (auxiliary loss, replay prioritization, or reward shaping), the amount of human effort required, and how performance behaves once guidance is withdrawn.

**Avoid:** Do not conflate human-in-the-loop training with offline imitation from fixed demonstrations or with preference-based reward learning from post-hoc comparisons; state the interaction protocol explicitly.

**Patterns:**

- A human supervisor intervenes when {trigger condition}, and the intervention is incorporated through {mechanism}.
- We report performance as a function of {human effort measure} to quantify the cost of guidance.

**Verify in primary sources:**

- `wu2023-human-guided-reinforcement-learning` — [Human-Guided Reinforcement Learning With Sim-to-Real Transfer for Autonomous Navigation](https://doi.org/10.1109/tpami.2023.3314762) (TPAMI 2023)

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

### embodied world model

`wm.definition.embodied-world-model.001` · definition · world_models, embodied_ai, robot_learning · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An action-aware predictive model of how an embodied environment evolves in space and time, designed to support capabilities such as planning, policy learning, or interaction prediction.

**Use:** Specify the predicted modalities and geometry, action conditioning, temporal horizon, and downstream decision use. Contemporary methods differ substantially, so treat this as an umbrella term rather than a fixed architecture.

**Avoid:** Do not infer physical consistency, controllability, or policy utility solely from visually plausible generated video.

**Patterns:**

- We use an embodied world model to predict {future sensory or geometric state} conditioned on {robot action sequence}.
- The model supports {planning or policy learning} by coupling {environment prediction} with {action representation}.

**Verify in primary sources:**

- `zhen2025embodiedworld` — [Learning 4D Embodied World Models](https://openaccess.thecvf.com/content/ICCV2025/html/Zhen_Learning_4D_Embodied_World_Models_ICCV_2025_paper.html) (ICCV 2025)
- `zhu2025unifiedworld` — [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](https://www.roboticsproceedings.org/rss21/p015.html) (RSS 2025)
- `koh2021pathdreamer` — [Pathdreamer: A World Model for Indoor Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Koh_Pathdreamer_A_World_Model_for_Indoor_Navigation_ICCV_2021_paper.html) (ICCV 2021)

### navigation world model

`wm.definition.navigation-world-model.001` · definition · world_models, embodied_ai · related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A predictive environment model specialized for forecasting navigation-relevant observations, states, or transitions under candidate agent motions.

**Use:** Specify its spatial representation, action interface, prediction target, and how a planner or policy consumes predictions.

**Avoid:** Do not use the label for a static map or localization model without a predictive transition component.

**Patterns:**

- The navigation world model predicts {navigation-relevant target} under {candidate motion} and supports {planning or policy update}.

**Verify in primary sources:**

- `bar2025-navigation-world-models` — [Navigation World Models](https://openaccess.thecvf.com/content/CVPR2025/html/Bar_Navigation_World_Models_CVPR_2025_paper.html) (CVPR 2025)
- `koh2021pathdreamer` — [Pathdreamer: A World Model for Indoor Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Koh_Pathdreamer_A_World_Model_for_Indoor_Navigation_ICCV_2021_paper.html) (ICCV 2021)

### occupancy world model

`wm.definition.occupancy-world-model.001` · definition · world_models, embodied_ai · abstract, introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A world model that predicts future spatial occupancy, often together with motion or semantic attributes, rather than synthesizing only RGB observations.

**Use:** Name the spatial representation, coordinate frame, temporal horizon, supervised targets, and use in planning or forecasting.

**Avoid:** Do not equate occupancy accuracy with collision-free or task-success performance without downstream evaluation.

**Patterns:**

- The occupancy world model forecasts {spatial representation} over {horizon} and provides {downstream module} with {predicted quantity}.

**Verify in primary sources:**

- `feng2025-gaussian-based-world-model` — [Gaussian-based World Model: Gaussian Priors for Voxel-Based Occupancy Prediction and Future Motion Prediction](https://openaccess.thecvf.com/content/ICCV2025/html/Feng_Gaussian-based_World_Model_Gaussian_Priors_for_Voxel-Based_Occupancy_Prediction_and_ICCV_2025_paper.html) (ICCV 2025)
- `huang2024-neural-volumetric-world-models` — [Neural Volumetric World Models for Autonomous Driving](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2571_ECCV_2024_paper.php) (ECCV 2024)

### visual world model for embodied agents

`wm.definition.visual-world-model.001` · definition · world_models, embodied_ai · introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A predictive model that represents how an embodied agent's visual environment may evolve, often conditioned on motion or actions and used for navigation, planning, or policy learning.

**Use:** Specify predicted modalities, spatial frame, action or path conditioning, and whether the output is used by the agent. Separate plausible generation from geometrically accurate prediction.

**Avoid:** Do not infer physical consistency or control utility from visual realism alone.

**Patterns:**

- The visual world model predicts {RGB, depth, or semantics} at {future viewpoints} conditioned on {agent path or actions}.
- We evaluate whether predicted observations support {navigation or manipulation decision}.

**Verify in primary sources:**

- `koh2021pathdreamer` — [Pathdreamer: A World Model for Indoor Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Koh_Pathdreamer_A_World_Model_for_Indoor_Navigation_ICCV_2021_paper.html) (ICCV 2021)
- `zhen2025embodiedworld` — [Learning 4D Embodied World Models](https://openaccess.thecvf.com/content/ICCV2025/html/Zhen_Learning_4D_Embodied_World_Models_ICCV_2025_paper.html) (ICCV 2025)

### Embodied systems should be grouped by geometry, memory, interaction, and supervision.

`emb.sentence-pattern.related-work-memory-geometry.001` · sentence_pattern · embodied_ai · related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

A Related Work scaffold that distinguishes representational and data assumptions instead of listing agents by publication date.

**Use:** Use only axes that materially separate the cited methods and verify every assigned category.

**Avoid:** Do not treat 2D versus 3D representation as the only meaningful difference when memory and interaction regimes also differ.

**Patterns:**

- Embodied approaches vary in their geometric representation ({geometry}), temporal memory ({memory}), interaction regime ({regime}), and supervision ({signals}).

### Embodied methods should be positioned by supervision, interaction regime, and deployment assumptions.

`emb.sentence-pattern.related-work.001` · sentence_pattern · embodied_ai, robot_learning · related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Structures embodied-AI related work around how data is obtained, whether learning is interactive, and what information or hardware is available at deployment.

**Use:** Use concrete axes such as demonstrations versus rewards, simulation versus real data, online versus offline collection, and privileged versus deployable observations.

**Avoid:** Do not group methods only by architecture when their data and deployment assumptions dominate the comparison.

**Patterns:**

- We organize prior work by its supervision signal, whether training uses online interaction, and the sensory information available at deployment.
- Unlike methods trained on {data regime}, our approach assumes {different verified regime}.

**Verify in primary sources:**

- `xia2018gibson` — [Gibson Env: Real-World Perception for Embodied Agents](https://openaccess.thecvf.com/content_cvpr_2018/html/Xia_Gibson_Env_Real-World_CVPR_2018_paper.html) (CVPR 2018)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)
- `khazatsky2024droid` — [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://roboticsproceedings.org/rss20/p120.html) (RSS 2024)
- `gu2017asynchronous` — [Deep Reinforcement Learning for Robotic Manipulation with Asynchronous Off-Policy Updates](https://ieeexplore.ieee.org/document/7989385) (ICRA 2017)

### Each real-system condition is evaluated in {trials} trials, with success defined as {criterion}.

`general.sentence-pattern.real-system-trials.001` · sentence_pattern · general, embodied_ai, robot_learning, vision_language_action · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines the trial count and success criterion for a physical or deployed-system evaluation.

**Use:** Also state reset procedure, intervention policy, trial independence, task allocation, and the denominator used for success rate.

**Avoid:** Do not report a success percentage without the number and composition of physical trials.

**Patterns:**

- Each real-robot task is evaluated in {trials} trials, with success defined as {terminal condition}.
- We conduct {number} trials per {task and object} pair and count an intervention as {outcome}.

### 3D scene memory

`emb.term.3d-scene-memory.001` · term · embodied_ai, world_models · related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A persistent spatial representation that aggregates observations into a three-dimensional memory for embodied exploration, grounding, or reasoning.

**Use:** Specify coordinate frame, stored features, update rule, memory lifetime, and how queries access the memory.

**Avoid:** Do not use the term for a single-frame 3D feature tensor that is not maintained across interaction.

**Patterns:**

- The agent updates a 3D scene memory with {features} in {coordinate frame} and queries it for {task}.

**Verify in primary sources:**

- `yang2025-3d-mem-3d-scene` — [3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-Mem_3D_Scene_Memory_for_Embodied_Exploration_and_Reasoning_CVPR_2025_paper.html) (CVPR 2025)
- `lin2025-bip3d-bridging-2d-images` — [BIP3D: Bridging 2D Images and 3D Perception for Embodied Intelligence](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_BIP3D_Bridging_2D_Images_and_3D_Perception_for_Embodied_Intelligence_CVPR_2025_paper.html) (CVPR 2025)

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

### affordance grounding

`emb.term.affordance-grounding.001` · term · embodied_ai, robot_learning · related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The association of a task or action description with scene regions, objects, poses, or interactions that support the action.

**Use:** Name the affordance representation, grounding target, supervision source, and whether feasibility is verified by execution.

**Avoid:** Do not call semantic relevance an affordance unless it expresses an action possibility or interaction relation.

**Patterns:**

- The model grounds {instruction or action} to {object, region, or pose} that affords {interaction}.

**Verify in primary sources:**

- `wu2025-garmentpile-point-level-visual` — [GarmentPile: Point-Level Visual Affordance Guided Retrieval and Adaptation for Cluttered Garments Manipulation](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_GarmentPile_Point-Level_Visual_Affordance_Guided_Retrieval_and_Adaptation_for_Cluttered_CVPR_2025_paper.html) (CVPR 2025)
- `li2025-coa-vla-improving-vision` — [CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance](https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html) (ICCV 2025)

### egocentric observation

`emb.term.egocentric-observation.001` · term · embodied_ai · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Sensory input represented from the agent's current first-person viewpoint rather than from a fixed external or global viewpoint.

**Use:** Name the modality and field of view, and distinguish current observations from accumulated maps or privileged simulator state.

**Avoid:** Do not describe a third-person camera or global map as egocentric.

**Patterns:**

- At each step, the agent receives an egocentric {RGB, depth, or audio-visual} observation.
- The policy does not access {global map or privileged state}.

**Verify in primary sources:**

- `anderson2018vln` — [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html) (CVPR 2018)
- `shridhar2020alfred` — [ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html) (CVPR 2020)
- `chen2020soundspaces` — [SoundSpaces: Audio-Visual Navigation in 3D Environments](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123510018.pdf) (ECCV 2020)

### embodiment

`emb.term.embodiment.001` · term · embodied_ai, robot_learning · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The agent-specific physical or simulated form that determines its sensing, actuation, kinematics, and interaction constraints.

**Use:** Name the aspects that differ across embodiments—camera placement, morphology, control frequency, action coordinates, or dynamics—rather than using the term abstractly.

**Avoid:** Do not use embodiment as a synonym for environment or task.

**Patterns:**

- The policy is evaluated on embodiments that differ in {morphology, sensors, or action space}.
- We encode embodiment-specific {proprioceptive or action information}.

**Verify in primary sources:**

- `savva2019habitat` — [Habitat: A Platform for Embodied AI Research](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) (ICCV 2019)
- `brohan2023rt1` — [RT-1: Robotics Transformer for Real-World Control at Scale](https://roboticsproceedings.org/rss19/p025.html) (RSS 2023)
- `hansen2024tdmpc2` — [TD-MPC2: Scalable, Robust World Models for Continuous Control](https://proceedings.iclr.cc/paper_files/paper/2024/hash/cf73d57b6dcda32b293df7c2d5341f49-Abstract-Conference.html) (ICLR 2024)

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

### long-horizon interaction

`emb.term.long-horizon-interaction.001` · term · embodied_ai, robot_learning · abstract, introduction, related_work, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A task requiring a temporally extended sequence of dependent decisions, often with delayed outcomes and opportunities for errors to accumulate.

**Use:** Quantify horizon in steps, subgoals, elapsed time, or state changes, and explain what makes dependencies consequential.

**Avoid:** Do not call a task long-horizon solely because episodes have a large maximum length.

**Patterns:**

- The task requires long-horizon interaction across {number} dependent subgoals.
- Early execution errors can alter the states available to later subgoals.

**Verify in primary sources:**

- `shridhar2020alfred` — [ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html) (CVPR 2020)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

### proprioceptive observation

`emb.term.proprioception.001` · term · robot_learning, embodied_ai · method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Internal measurements of the agent's body state, such as joint positions, velocities, actuator states, or inertial readings.

**Use:** List the included signals, normalization, sampling rate, and temporal alignment with exteroceptive observations.

**Avoid:** Do not include external camera observations under proprioception.

**Patterns:**

- The policy conditions on visual features and proprioceptive observations comprising {signals}.
- We synchronize proprioception with {camera frames} at {rate}.

**Verify in primary sources:**

- `kumar2021rma` — [RMA: Rapid Motor Adaptation for Legged Robots](https://roboticsproceedings.org/rss17/p011.html) (RSS 2021)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

### reality gap

`emb.term.reality-gap.001` · term · embodied_ai, robot_learning · introduction, related_work, limitations, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The discrepancy between simulated and physical observations, dynamics, contacts, sensors, or actuation that can degrade real-world deployment.

**Use:** Identify the relevant mismatch instead of treating the gap as a single scalar phenomenon.

**Avoid:** Do not attribute every real-world failure to the reality gap without diagnosis.

**Patterns:**

- We study the visual component of the reality gap while holding {controller or dynamics} fixed.
- Residual failures are associated with mismatches in {specific factor}.

**Verify in primary sources:**

- `tobin2017domainrandomization` — [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://ieeexplore.ieee.org/document/8202133/) (IROS 2017)
- `xia2018gibson` — [Gibson Env: Real-World Perception for Embodied Agents](https://openaccess.thecvf.com/content_cvpr_2018/html/Xia_Gibson_Env_Real-World_CVPR_2018_paper.html) (CVPR 2018)

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

### decompose the embodiment gap into physical and visual disparities

`emb.usage-note.embodiment-gap.001` · usage_note · embodied_ai · related_work, experiments, limitations

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Differences between training and deployment embodiments can arise from morphology and dynamics as well as camera geometry, appearance, sensing, and observation statistics.

**Use:** Evaluate or discuss physical and visual shifts separately before attributing transfer failure to embodiment as a single factor.

**Avoid:** Do not use embodiment gap as an unexplained catch-all for every domain shift.

**Patterns:**

- We isolate physical disparity in {factor} from visual disparity in {factor} and evaluate each under {controlled protocol}.

**Verify in primary sources:**

- `wang2025-rethinking-embodied-gap-vision` — [Rethinking the Embodied Gap in Vision-and-Language Navigation: A Holistic Study of Physical and Visual Disparities](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Rethinking_the_Embodied_Gap_in_Vision-and-Language_Navigation_A_Holistic_Study_ICCV_2025_paper.html) (ICCV 2025)
- `yuan2025-cross-embodiment-dexterous-grasping` — [Cross-Embodiment Dexterous Grasping with Reinforcement Learning](https://iclr.cc/virtual/2025/poster/28010) (ICLR 2025)

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

### imitation learning versus behavioral cloning

`emb.usage-note.imitation-bc.001` · usage_note · robot_learning, embodied_ai · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Imitation learning is the broader problem of learning behavior from demonstrations, while behavioral cloning usually denotes direct supervised prediction of expert actions from observations.

**Use:** Use behavioral cloning for the supervised objective and imitation learning for the wider family, which may include interactive data collection, occupancy matching, or other objectives.

**Avoid:** Do not use the two terms as universally interchangeable when the algorithm is not direct supervised cloning.

**Patterns:**

- We use behavioral cloning to fit the policy to demonstration state–action pairs.
- The method belongs to imitation learning but differs from behavioral cloning in {interactive or distributional mechanism}.

**Verify in primary sources:**

- `ho2016gail` — [Generative Adversarial Imitation Learning](https://papers.nips.cc/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html) (NeurIPS 2016)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

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

### name the generalization axis and held-out unit

`general.usage-note.generalization-axis.001` · usage_note · general, embodied_ai, robot_learning · abstract, introduction, experiments, limitations, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Generalization is always relative to a specified shift, such as unseen objects, tasks, environments, users, embodiments, or combinations.

**Use:** State what was held out during training and what unit is averaged at evaluation. Prefer 'generalization to unseen objects' over an unqualified 'generalization ability.'

**Avoid:** Do not infer broad out-of-distribution generalization from a random train–test split over nearly identical samples.

**Patterns:**

- We evaluate generalization to unseen {objects or tasks} by holding out {unit} during training.
- The current study does not establish transfer across unseen {embodiments or environments}.
