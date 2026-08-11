# Super Library pack: robot_learning

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

### rapid online adaptation

`emb.definition.rapid-adaptation.001` · definition · robot_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Updating an internal estimate, context, or behavior during deployment from a short history of recent interaction so the policy can respond to changing dynamics or conditions.

**Use:** Specify what adapts, whether policy parameters change, the adaptation window, supervision, and latency.

**Avoid:** Do not call ordinary recurrent inference adaptation unless the changing context and adaptation mechanism are made explicit.

**Patterns:**

- The adaptation module infers {environment context} from a recent history of {states and actions}.
- The base policy responds to changing {terrain or dynamics} without gradient updates at deployment.

**Verify in primary sources:**

- `kumar2021rma` — [RMA: Rapid Motor Adaptation for Legged Robots](https://roboticsproceedings.org/rss17/p011.html) (RSS 2021)

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

### differentiable physics simulation

`rl.definition.differentiable-simulation.001` · definition · reinforcement_learning, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A simulator whose state transitions are implemented as differentiable operations, so gradients of task objectives with respect to actions, policy parameters, or physical parameters can be computed by backpropagating through the simulated dynamics.

**Use:** State which quantities gradients flow through, the horizon over which backpropagation remains stable, and how nonsmooth events such as contact are handled. Distinguish analytic differentiable dynamics from learned dynamics models used for the same optimization purpose.

**Avoid:** Do not treat simulation gradients as automatically well behaved; long-horizon or contact-rich rollouts can make them ill-conditioned, and claims should acknowledge this when applicable.

**Patterns:**

- We backpropagate {task objective} through the differentiable simulator to update {policy parameters}.
- Gradients across {contact or discontinuous events} are handled by {smoothing or relaxation scheme}.

**Verify in primary sources:**

- `chen2023-imitation-learning-state-matching` — [Imitation Learning As State Matching via Differentiable Physics](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_Imitation_Learning_As_State_Matching_via_Differentiable_Physics_CVPR_2023_paper.html) (CVPR 2023)

### experience replay / replay buffer

`rl.definition.experience-replay.001` · definition · reinforcement_learning, robot_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A mechanism that stores previously collected transitions or trajectories and resamples them for subsequent learning updates.

**Use:** Report capacity, sampling distribution, sequence length, prioritization, and the ratio of updates to newly collected data when these affect results.

**Avoid:** Do not assume replayed data are on-policy or independent and identically distributed.

**Patterns:**

- Transitions are stored in a replay buffer of capacity {size} and sampled uniformly for critic updates.
- We sample length-{k} sequences from replay to train the recurrent world model.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)
- `gu2017asynchronous` — [Deep Reinforcement Learning for Robotic Manipulation with Asynchronous Off-Policy Updates](https://ieeexplore.ieee.org/document/7989385) (ICRA 2017)

### offline reinforcement learning

`rl.definition.offline-rl.001` · definition · reinforcement_learning, robot_learning · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Reinforcement learning from a fixed dataset of previously collected transitions, without additional environment interaction during training.

**Use:** Describe dataset coverage, behavior policies if known, reward availability, and evaluation protocol. Distinguish offline RL from off-policy online learning and imitation learning.

**Avoid:** Do not call training from a continually growing replay buffer offline RL.

**Patterns:**

- We consider the offline RL setting, where the agent learns from a fixed dataset {D} and cannot collect additional transitions.
- The dataset contains trajectories generated by {behavior policy mixture}.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

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

### forward and inverse dynamics

`wm.definition.forward-inverse-dynamics.001` · definition · world_models, robot_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Forward dynamics predicts a future state or observation from a current state and action, whereas inverse dynamics infers an action from a state transition or desired outcome.

**Use:** Define the conditioning variables precisely; inverse dynamics may be ambiguous when multiple actions can produce similar transitions.

**Avoid:** Do not interchange inverse dynamics with model inversion unless the mapping and objective are actually equivalent.

**Patterns:**

- The forward model predicts {next state} from {state and action}, while the inverse model predicts {action} from {state pair or goal}.
- Joint training couples action prediction with {video or latent dynamics prediction}.

**Verify in primary sources:**

- `zhu2025unifiedworld` — [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](https://www.roboticsproceedings.org/rss21/p015.html) (RSS 2025)
- `zhen2025embodiedworld` — [Learning 4D Embodied World Models](https://openaccess.thecvf.com/content/ICCV2025/html/Zhen_Learning_4D_Embodied_World_Models_ICCV_2025_paper.html) (ICCV 2025)

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

### 6-DoF grasp pose

`emb.term.grasp-pose.001` · term · robot_learning · introduction, related_work, method, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A candidate gripper pose in three-dimensional space parameterized by three translational and three rotational degrees of freedom.

**Use:** Define the coordinate frame, gripper model, collision checks, and evaluation criterion. Separate pose proposal quality from executed grasp success.

**Avoid:** Do not call an image-plane grasp rectangle a full 6-DoF grasp pose.

**Patterns:**

- The network predicts 6-DoF grasp poses from {RGB-D image or point cloud}.
- We transform each grasp pose from {camera frame} to {robot base frame}.

**Verify in primary sources:**

- `fang2020graspnet` — [GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping](https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.html) (CVPR 2020)

### in-the-wild robot data

`emb.term.in-the-wild-data.001` · term · robot_learning · abstract, introduction, related_work, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Robot interaction data collected across naturally varied real-world scenes, tasks, operators, or institutions rather than within one tightly controlled laboratory setup.

**Use:** Quantify collectors, sites, scenes, robots, tasks, and collection protocol. 'In the wild' describes collection diversity, not unrestricted deployment.

**Avoid:** Do not use the term for synthetic variation or a single staged room.

**Patterns:**

- The dataset contains in-the-wild robot data collected across {sites, scenes, and tasks}.
- We evaluate whether collection diversity improves robustness to {held-out environment variation}.

**Verify in primary sources:**

- `khazatsky2024droid` — [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://roboticsproceedings.org/rss20/p120.html) (RSS 2024)

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

### multimodal action distribution

`emb.term.multimodal-action.001` · term · robot_learning · introduction, related_work, method, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

An action distribution with multiple distinct high-probability behaviors, such as different valid trajectories for accomplishing the same task.

**Use:** Explain the source of multimodality and evaluate mode coverage or task success; multiple samples do not by themselves establish meaningful modes.

**Avoid:** Do not use multimodal to mean that the input has multiple sensor modalities.

**Patterns:**

- The policy must represent a multimodal action distribution because {multiple strategies} are valid for the same observation.
- We visualize samples corresponding to {distinct action modes}.

**Verify in primary sources:**

- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

### prehensile and non-prehensile manipulation

`emb.term.prehensile-nonprehensile.001` · term · robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Prehensile manipulation secures an object with a grasp, whereas non-prehensile manipulation changes object state through actions such as pushing without maintaining a grasp.

**Use:** Use the distinction to describe action primitives or coordination between them. Name the actual contact modes studied.

**Avoid:** Do not treat pushing as a failed grasp; it can be an intentional non-prehensile action.

**Patterns:**

- The policy coordinates prehensile grasping with non-prehensile pushing to {task objective}.
- Pushing changes the scene configuration before a grasp is attempted.

**Verify in primary sources:**

- `zeng2018pushgrasp` — [Learning Synergies Between Pushing and Grasping with Self-Supervised Deep Reinforcement Learning](https://ieeexplore.ieee.org/document/8593986/) (IROS 2018)

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

### state–action coverage of the offline dataset

`rl.term.offline-dataset-coverage.001` · term · reinforcement_learning, robot_learning · introduction, related_work, method, experiments, limitations, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The range and frequency of states and actions represented by a fixed dataset relative to those needed by a candidate policy or evaluation task.

**Use:** Operationalize coverage with dataset statistics, support assumptions, distances, or task-specific diagnostics; it is not captured by dataset size alone.

**Avoid:** Do not describe a dataset as diverse or well-covered solely because it contains many transitions.

**Patterns:**

- Performance degrades when the learned policy selects actions poorly represented in the offline dataset.
- We report coverage across {tasks, states, actions, or embodiments} in addition to trajectory count.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)
- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)

### policy

`rl.term.policy.001` · term · reinforcement_learning, robot_learning · method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A rule or conditional distribution that maps an agent's information state, such as an observation or history, to actions.

**Use:** Use π(a|s) for a stochastic policy and state whether conditioning is on state, observation, goal, language, or history.

**Avoid:** Do not call a value function or open-loop action sequence a policy.

**Patterns:**

- The stochastic policy {symbol} maps {observation or state} to a distribution over {actions}.
- We condition the policy on {goal specification} in addition to {observation}.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `brohan2023rt1` — [RT-1: Robotics Transformer for Real-World Control at Scale](https://roboticsproceedings.org/rss19/p025.html) (RSS 2023)

### sample efficiency / data efficiency

`rl.term.sample-efficiency.001` · term · reinforcement_learning, robot_learning · abstract, introduction, related_work, experiments, rebuttal, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The amount of environment interaction or training data required to reach a specified level of performance.

**Use:** Name the sample unit—steps, episodes, demonstrations, images, or hours—and compare learning curves or performance at matched data budgets.

**Avoid:** Do not infer sample efficiency from wall-clock speed or final performance alone.

**Patterns:**

- We evaluate sample efficiency by comparing {metric} after {matched number} environment steps.
- The method reaches {performance threshold} using {data amount}.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

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

### action-conditioned dynamics

`wm.term.action-conditioned-dynamics.001` · term · world_models, robot_learning · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Predictive dynamics in which future states or observations depend explicitly on the agent's action sequence.

**Use:** Use to distinguish controllable prediction from passive video prediction. Specify action representation, temporal alignment, and prediction target. Use 'path-conditioned' or 'viewpoint-conditioned' when a model conditions on a planned path rather than low-level actions.

**Avoid:** Do not infer controllability from temporal prediction alone or relabel viewpoint conditioning as action conditioning.

**Patterns:**

- The model learns action-conditioned dynamics over {latent state or sensory representation}.
- Conditioning on actions allows the model to evaluate {candidate action sequences}.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `zhen2025embodiedworld` — [Learning 4D Embodied World Models](https://openaccess.thecvf.com/content/ICCV2025/html/Zhen_Learning_4D_Embodied_World_Models_ICCV_2025_paper.html) (ICCV 2025)

### model predictive control (MPC)

`wm.term.model-predictive-control.001` · term · world_models, reinforcement_learning, robot_learning · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A control strategy that repeatedly optimizes a finite-horizon action sequence using a model, executes an initial portion, and replans from the new state.

**Use:** State the planning horizon, optimizer, objective, terminal value, and how many actions are executed before replanning.

**Avoid:** Do not use MPC as a synonym for any policy that consumes model predictions.

**Patterns:**

- At each environment step, MPC optimizes {candidate action sequences} over a horizon of {H} and executes {first action or action chunk}.
- We augment the finite-horizon objective with {terminal value estimate}.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### receding-horizon planning

`wm.term.receding-horizon.001` · term · world_models, robot_learning · method, related_work, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Planning in which a finite-horizon solution is repeatedly recomputed as new observations become available.

**Use:** Use when replanning closes the loop. Distinguish action horizon from prediction horizon and note whether an action chunk rather than one action is executed.

**Avoid:** Do not call a single open-loop plan receding-horizon control.

**Patterns:**

- We use receding-horizon planning to reoptimize the action sequence every {k} steps.

**Verify in primary sources:**

- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

### task-agnostic training (paper-specific usage)

`emb.term.task-agnostic-training.001` · usage_note · robot_learning · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

In RT-1, this label describes joint training with shared parameters across a broad task collection rather than separate task-specific models.

**Use:** Prefer the more explicit phrase 'joint multi-task training with shared parameters' unless discussing the cited paper's terminology. Explain what task information remains available, such as language commands.

**Avoid:** Do not treat 'task-agnostic' as a universally standardized term or imply absence of task conditioning merely because parameters are shared.

**Patterns:**

- The model uses joint multi-task training with shared parameters and conditions on {task instruction}.
- Following {source}, we use 'task-agnostic training' to mean {paper-specific definition}.

**Verify in primary sources:**

- `brohan2023rt1` — [RT-1: Robotics Transformer for Real-World Control at Scale](https://roboticsproceedings.org/rss19/p025.html) (RSS 2023)

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

### distinguish interpolation within dataset support from extrapolation beyond it

`rl.usage-note.support-generalization.001` · usage_note · reinforcement_learning, robot_learning · related_work, experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Good performance on held-out samples drawn from familiar coverage does not by itself establish reliable action selection in unsupported regions.

**Use:** Describe how evaluation differs from the behavior-data distribution and whether the policy is constrained or regularized near dataset support.

**Avoid:** Do not call a random trajectory split out-of-distribution evaluation without demonstrating a meaningful shift.

**Patterns:**

- The test tasks use held-out trajectories but remain within the dataset's object and action coverage.
- Generalization beyond the behavior-policy support remains to be established.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

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
