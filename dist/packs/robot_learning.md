# Super Library pack: robot_learning

Corpus `0.1.0` · snapshot `2026-07-29`.

These are paraphrases, canonical terms, and original sentence patterns.
Verify technical claims in the linked primary sources before citing them.
Read the [self-contained mini contract](https://raw.githubusercontent.com/asimfish/super_library/v0.1.0/dist/super-library-compact.md) before using this pack directly.

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
