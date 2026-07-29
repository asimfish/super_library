# Super Library pack: world_models

Corpus `0.2.0` · snapshot `2026-07-30`.

These are paraphrases, canonical terms, and original sentence patterns.
Verify technical claims in the linked primary sources before citing them.
Read the [selective agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) and [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md) before using this exhaustive pack.

### 3D vision-language-action generative world model (paper-specific usage)

`emb.definition.3d-vla-world-model.001` · definition · embodied_ai, robot_learning, world_models · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

In 3D-VLA, a model that uses 3D scene information and language-conditioned representations to generate future scene or action-related predictions for embodied manipulation.

**Use:** Attribute this formulation to the specific paper and describe its generated variables. Do not present the phrase as a universally standardized VLA architecture.

**Avoid:** Do not infer that every 3D-grounded VLA is a world model or that every world model predicts robot actions.

**Patterns:**

- Following {source}, we use '3D VLA world model' for a model that predicts {paper-specific outputs}.
- Our system differs because it predicts {actions only or future observations only}.

**Verify in primary sources:**

- `zhen2024vla` — [3D-VLA: A 3D Vision-Language-Action Generative World Model](https://proceedings.mlr.press/v235/zhen24a.html) (ICML 2024)

### temporal-difference (TD) learning

`rl.definition.temporal-difference.001` · definition · reinforcement_learning, world_models · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Learning a value-related prediction by moving it toward a target that combines an observed reward with a bootstrapped estimate of subsequent value.

**Use:** State the exact target, discount, update horizon, target network or stop-gradient treatment, and whether the estimate is on-policy or off-policy.

**Avoid:** Do not describe every loss across adjacent time steps as temporal-difference learning.

**Patterns:**

- We minimize a temporal-difference error against $r_t+\gamma V_{\bar\theta}(s_{t+1})$.
- The latent value is trained with an $n$-step TD target.

**Verify in primary sources:**

- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)

### short branched model rollout

`wm.definition.branched-rollout.001` · definition · world_models, reinforcement_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A finite learned-model rollout initialized from a state sampled from real experience, used to generate synthetic transitions without simulating an entire episode from the initial-state distribution.

**Use:** Report the branch-state distribution, rollout length, policy used inside the model, and how synthetic and real transitions enter learning.

**Avoid:** Do not call a full model-generated episode or an arbitrary imagined trajectory a branched rollout without specifying the real-data branch point.

**Patterns:**

- We start $k$-step model rollouts from states in the replay buffer and add the synthetic transitions to {training buffer}.
- Each branched rollout follows the current policy for {length} learned transitions.

**Verify in primary sources:**

- `janner2019mbpo` — [When to Trust Your Model: Model-Based Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html) (NeurIPS 2019)

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

### latent state

`wm.definition.latent-state.001` · definition · world_models, reinforcement_learning · method, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A learned representation intended to retain information relevant to the modeled or predicted quantities while abstracting away some details of raw observations.

**Use:** Explain whether the state is Markovian by assumption or approximation, how it is inferred, and which downstream quantities depend on it. State separately when task objectives make the representation task-oriented.

**Avoid:** Do not call an arbitrary feature vector a state without explaining its temporal role.

**Patterns:**

- The latent state summarizes {observation history} for predicting {future quantity}.
- We infer {latent state} from {observation and previous state}.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)

### model-based reinforcement learning

`wm.definition.model-based-rl.001` · definition · world_models, reinforcement_learning · introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Reinforcement learning that uses a model of environment dynamics, learned or known, to improve decision making through planning, synthetic experience, value estimation, or policy optimization.

**Use:** Explain the role of the model rather than applying the label solely because the architecture contains a predictor.

**Avoid:** Do not conflate model-based RL with supervised next-step prediction that never affects decisions.

**Patterns:**

- The method is model-based because the learned dynamics model is used to {plan actions or optimize the policy}.
- Model-based reinforcement learning can use predicted transitions for {downstream decision process}.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### probabilistic dynamics model

`wm.definition.probabilistic-dynamics.001` · definition · world_models, reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A dynamics model that represents a conditional distribution over future states or latent states rather than returning only one point prediction.

**Use:** State what is random, how the distribution is parameterized, and whether it is intended to model environment stochasticity, model uncertainty, or both.

**Avoid:** Do not assume that any predicted variance is calibrated or that it cleanly separates aleatoric and epistemic uncertainty.

**Patterns:**

- We learn a probabilistic dynamics model $p_\theta(s_{t+1}\mid s_t,a_t)$ and propagate multiple particles during planning.
- The latent transition predicts a distribution over {next latent variable} conditioned on {state and action}.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)
- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)

### task-oriented latent dynamics model

`wm.definition.task-oriented-model.001` · definition · world_models, reinforcement_learning · introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A latent dynamics model trained to preserve decision-relevant predictive structure without necessarily reconstructing raw observations.

**Use:** Name the task signals, such as reward, value, or latent consistency, that shape the representation. Use 'implicit world model' only when a cited paper defines that label for its own model.

**Avoid:** Do not treat 'task-oriented' and 'implicit' as general synonyms, or claim that reconstruction is unnecessary for every task family.

**Patterns:**

- We learn a task-oriented latent dynamics model using {reward, value, and consistency objectives} rather than pixel reconstruction.
- The model predicts {decision-relevant quantities} in latent space.

**Verify in primary sources:**

- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)
- `hansen2024tdmpc2` — [TD-MPC2: Scalable, Robust World Models for Continuous Control](https://proceedings.iclr.cc/paper_files/paper/2024/hash/cf73d57b6dcda32b293df7c2d5341f49-Abstract-Conference.html) (ICLR 2024)

### uncertainty-aware model-based planning

`wm.definition.uncertainty-aware-planning.001` · definition · world_models, reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Planning that represents or uses uncertainty in learned dynamics when evaluating candidate action sequences, rather than optimizing only a single deterministic forecast.

**Use:** State whether uncertainty is marginalized, sampled, penalized, or used as a constraint. Distinguish predictive uncertainty from risk preference.

**Avoid:** Do not imply safety or robustness solely because the planner propagates a distribution.

**Patterns:**

- The planner samples predictive dynamics and optimizes expected return under the resulting trajectory distribution.
- We penalize candidate plans with high {validated uncertainty statistic}.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)

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

### world model

`wm.definition.world-model.001` · definition · world_models, reinforcement_learning · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A learned predictive model of how an environment evolves, typically conditioned on the agent's actions and used to support prediction, planning, or policy learning.

**Use:** State what variables the model predicts, whether prediction occurs in observation or latent space, and how the model is used downstream. Community usage is broad, so define the paper's operational scope.

**Avoid:** Do not treat every video generator or static scene representation as a world model without an action, temporal, or decision-making connection.

**Patterns:**

- We use a world model to predict {future latent states or observations} conditioned on {current state and action sequence}.
- Here, world model refers to {learned transition components} used for {planning or policy optimization}.

**Verify in primary sources:**

- `ha2018worldmodels` — [Recurrent World Models Facilitate Policy Evolution](https://papers.nips.cc/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html) (NeurIPS 2018)
- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)

### World-model methods can be organized by {representation}, {training objective}, and {decision mechanism}.

`wm.sentence-pattern.related-work.001` · sentence_pattern · world_models · related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Provides a technical-axis structure for a world-model related-work paragraph.

**Use:** Instantiate each axis with verified method families: observation-space versus latent prediction, reconstruction versus task-oriented objectives, and online planning versus imagined policy learning.

**Avoid:** Do not force methods into mutually exclusive categories when they combine mechanisms.

**Patterns:**

- World-model methods can be organized by the space in which they predict, the objectives used to learn the representation, and whether decisions arise from online planning or policy learning in imagination.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)
- `hansen2024tdmpc2` — [TD-MPC2: Scalable, Robust World Models for Continuous Control](https://proceedings.iclr.cc/paper_files/paper/2024/hash/cf73d57b6dcda32b293df7c2d5341f49-Abstract-Conference.html) (ICLR 2024)

### bootstrapped target

`rl.term.bootstrapped-target.001` · term · reinforcement_learning, world_models · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A learning target that contains a prediction produced by the current model or a target model for a later state, rather than relying entirely on observed outcomes.

**Use:** Name the prediction being reused and where gradients are stopped. Distinguish RL bootstrapping from statistical bootstrap resampling.

**Avoid:** Do not imply that a bootstrapped target is unbiased or independent of the network being trained.

**Patterns:**

- The critic is updated toward a bootstrapped target computed with the target value network.
- We stop gradients through the $n$-step return target.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)

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

### compounding model error

`wm.term.compounding-model-error.001` · term · world_models, reinforcement_learning · introduction, related_work, experiments, limitations, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Prediction errors that accumulate as a learned model is recursively unrolled, potentially moving rollouts away from states represented in the training data.

**Use:** Tie the claim to rollout horizon, distribution shift, and the evaluated quantity. Distinguish accumulation from a formally exponential error rate unless proven.

**Avoid:** Do not write 'errors exponentially explode' without a bound or measurement supporting that rate.

**Patterns:**

- Long model rollouts are susceptible to compounding model error as predictions feed into subsequent transitions.
- We limit the rollout horizon to {H} to reduce error accumulation.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### discrete latent representation

`wm.term.discrete-latent.001` · term · world_models · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A latent representation whose stochastic variables take values from discrete categories rather than a continuous distribution.

**Use:** Describe the parameterization and estimator used for learning. Attribute benefits such as optimization stability or expressivity only to verified experiments.

**Avoid:** Do not equate discreteness with symbolic or interpretable representation.

**Patterns:**

- The world model encodes observations into a discrete latent representation parameterized by {categorical structure}.

**Verify in primary sources:**

- `hafner2021dreamerv2` — [Mastering Atari with Discrete World Models](https://openreview.net/forum?id=0oabwyZbOu) (ICLR 2021)

### ensemble dynamics model / probabilistic ensemble

`wm.term.dynamics-ensemble.001` · term · world_models, reinforcement_learning · related_work, method, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A collection of separately fitted dynamics predictors whose aggregate predictions can improve robustness and provide a practical disagreement signal.

**Use:** Describe initialization, data resampling, ensemble size, and how predictions are combined or sampled. Call disagreement a heuristic for epistemic uncertainty unless a stronger interpretation is justified.

**Avoid:** Do not present an ensemble as an exact Bayesian posterior or treat members trained identically as independent evidence.

**Patterns:**

- We fit an ensemble of {number} dynamics models and sample a member when propagating each particle.
- Planning penalizes action sequences with high ensemble disagreement.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)
- `janner2019mbpo` — [When to Trust Your Model: Model-Based Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html) (NeurIPS 2019)

### imagined trajectories / model rollouts

`wm.term.imagined-trajectories.001` · term · world_models, reinforcement_learning · related_work, method, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Sequences of predicted states, rewards, or observations generated by repeatedly applying a learned model under a chosen action sequence or policy.

**Use:** Use 'imagined trajectories' for Dreamer-style latent rollouts and 'model rollouts' as the broader term. Report rollout horizon and starting-state distribution.

**Avoid:** Do not call logged or simulator-generated trajectories imagined merely because they are off-policy.

**Patterns:**

- We generate imagined trajectories of length {H} from latent states inferred from the replay buffer.
- Model rollouts provide {training targets} for {policy or value function}.

**Verify in primary sources:**

- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### latent dynamics model

`wm.term.latent-dynamics.001` · term · world_models, reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A transition model that predicts the evolution of a learned latent state rather than directly predicting raw observations.

**Use:** Specify the latent state, deterministic and stochastic components if relevant, and the training signals that make it useful for the downstream task.

**Avoid:** Do not imply that operating in latent space automatically yields accurate long-horizon predictions.

**Patterns:**

- We learn a latent dynamics model that maps {latent state, action} to {next latent state distribution}.
- Planning is performed by unrolling the latent dynamics model over {horizon} steps.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### latent imagination

`wm.term.latent-imagination.001` · term · world_models, reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The generation of hypothetical future state sequences by unrolling a learned dynamics model in latent space.

**Use:** Use for model-generated trajectories rather than replayed environment trajectories. State how imagined data trains or evaluates the policy/value function.

**Avoid:** Do not anthropomorphize the model or imply physical execution.

**Patterns:**

- The actor and critic are optimized on trajectories generated through latent imagination.
- Latent imagination enables {policy update} without additional environment interaction.

**Verify in primary sources:**

- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hafner2021dreamerv2` — [Mastering Atari with Discrete World Models](https://openreview.net/forum?id=0oabwyZbOu) (ICLR 2021)

### learned dynamics model

`wm.term.learned-dynamics.001` · term · world_models, reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A model fitted from data to predict state or latent-state transitions under actions.

**Use:** Use 'dynamics model' for the transition component; use 'world model' when the broader system may also include representation, observation, reward, continuation, or uncertainty components.

**Avoid:** Do not use 'dynamic model' when referring to environment dynamics; that phrase can mean a model that changes over time.

**Patterns:**

- The learned dynamics model predicts {next representation} from {current representation} and {action}.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### learned reward model

`wm.term.learned-reward-model.001` · term · world_models, reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A component that predicts task reward from modeled states, latent states, actions, or transitions when reward is included in the learned world-model objective.

**Use:** Specify its inputs, target, loss, and whether the environment reward function is otherwise available at planning time.

**Avoid:** Do not conflate a learned reward predictor with human preference modeling or with the complete world model.

**Patterns:**

- The latent model jointly predicts rewards and observations from the recurrent state.
- Planning evaluates imagined trajectories with a learned reward predictor $r_\theta(z_t,a_t)$.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### model bias in model-based reinforcement learning

`wm.term.model-bias.001` · term · world_models, reinforcement_learning · introduction, related_work, method, limitations, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Distortion in policy learning or planning caused by systematic discrepancies between learned model transitions and the environment transitions relevant to the evaluated policy.

**Use:** Identify the state–action distribution and downstream quantity affected. Separate model bias from finite-sample variance and generic policy-estimation error.

**Avoid:** Do not equate low average one-step validation loss with negligible policy-relevant model bias.

**Patterns:**

- Long synthetic rollouts can amplify model bias when the policy visits state–action pairs poorly covered by real data.
- We evaluate model error under the current policy distribution rather than only on the training split.

**Verify in primary sources:**

- `janner2019mbpo` — [When to Trust Your Model: Model-Based Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html) (NeurIPS 2019)
- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)

### exploitation of model errors

`wm.term.model-exploitation.001` · term · world_models, reinforcement_learning · introduction, related_work, method, limitations, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A failure mode in which optimization selects actions that look favorable under an inaccurate learned model but do not yield the predicted outcomes in the real environment.

**Use:** Use the term when the optimizer or policy actively seeks regions where model errors are favorable. Support the diagnosis with real-environment evaluation or an appropriate uncertainty/error analysis.

**Avoid:** Do not label every performance gap as model exploitation without showing that optimization interacts with model error.

**Patterns:**

- The policy may exploit optimistic model errors outside the support of the collected transitions.
- Constraining planning to {supported region} reduces opportunities for model exploitation.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)
- `janner2019mbpo` — [When to Trust Your Model: Model-Based Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html) (NeurIPS 2019)

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

### observation model (decoder)

`wm.term.observation-model.001` · term · world_models · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A component that maps a latent state to a distribution over observations or reconstructs observation-space outputs.

**Use:** Use 'decoder' when emphasizing architecture and 'observation model' when emphasizing the probabilistic generative role. Some task-oriented world models intentionally omit it.

**Avoid:** Do not refer to a transition model as a decoder.

**Patterns:**

- An observation model decodes the latent state into {pixels, depth, or other sensory prediction}.
- Our task-oriented model omits an observation decoder and is trained with {predictive objective}.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hansen2024tdmpc2` — [TD-MPC2: Scalable, Robust World Models for Continuous Control](https://proceedings.iclr.cc/paper_files/paper/2024/hash/cf73d57b6dcda32b293df7c2d5341f49-Abstract-Conference.html) (ICLR 2024)

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

### stochastic latent state

`wm.term.stochastic-latent-state.001` · term · world_models · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A latent state represented by a distribution or sampled variable to capture uncertainty or multiple possible futures.

**Use:** Distinguish stochasticity in the latent transition from randomness in policy actions or observation noise. Name the distributional parameterization when relevant.

**Avoid:** Do not claim that stochastic latents capture calibrated uncertainty unless calibration is evaluated.

**Patterns:**

- The model samples a stochastic latent state from {posterior or prior distribution} at each step.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2021dreamerv2` — [Mastering Atari with Discrete World Models](https://openreview.net/forum?id=0oabwyZbOu) (ICLR 2021)

### trajectory sampling for uncertainty propagation

`wm.term.trajectory-sampling.001` · term · world_models, reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A sampling procedure that propagates multiple hypothetical trajectories through a probabilistic dynamics model to approximate distributions over future outcomes.

**Use:** Specify the particle count, how ensemble members are selected across time, and how predicted returns are aggregated for action selection.

**Avoid:** Do not use the term as a synonym for collecting real environment trajectories or for generic Monte Carlo evaluation without a learned model.

**Patterns:**

- We propagate {number} particles through the probabilistic ensemble and rank candidate action sequences by their predicted returns.
- Each particle samples {model or transition noise} according to {sampling rule}.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)

### aleatoric versus epistemic uncertainty in learned dynamics

`wm.usage-note.aleatoric-epistemic.001` · usage_note · world_models, reinforcement_learning · related_work, method, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Aleatoric uncertainty describes conditional variability that remains even with complete knowledge, whereas epistemic uncertainty reflects limited knowledge about the predictive model and may shrink with informative data.

**Use:** Explain which modeling component is intended to represent each uncertainty and validate the interpretation when it matters to planning or risk.

**Avoid:** Do not claim perfect decomposition merely because a network predicts a variance and an ensemble produces disagreement.

**Patterns:**

- The output distribution represents conditional stochasticity, while ensemble disagreement serves as a practical proxy for model uncertainty.
- We do not assume that the two uncertainty sources are perfectly identifiable from the available transitions.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)

### one-step accuracy does not by itself establish long-horizon fidelity

`wm.usage-note.one-vs-multistep.001` · usage_note · world_models · method, experiments, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Accurate next-step prediction and stable recursive rollout are related but distinct evaluation properties.

**Use:** Report multi-step or task-level metrics when the downstream method unrolls the model. Specify open-loop versus closed-loop evaluation.

**Avoid:** Do not use low one-step loss as the sole evidence that a model supports long-horizon planning.

**Patterns:**

- Although the model achieves low one-step error, we separately evaluate rollout fidelity over {horizon}.
- One-step prediction accuracy does not by itself establish decision-relevant long-horizon fidelity.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `koh2021pathdreamer` — [Pathdreamer: A World Model for Indoor Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Koh_Pathdreamer_A_World_Model_for_Indoor_Navigation_ICCV_2021_paper.html) (ICCV 2021)

### online planning versus policy learning in imagination

`wm.usage-note.planning-vs-policy.001` · usage_note · world_models, reinforcement_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

World models may support decisions by optimizing actions at test time, by training an amortized policy on imagined experience, or by combining both.

**Use:** State when computation occurs and whether the deployed controller replans. This is a useful axis for organizing related work.

**Avoid:** Do not classify all world-model methods as planners.

**Patterns:**

- Whereas {method family} performs online planning in the learned model, {method family} trains a policy on imagined trajectories.
- Our method combines {online trajectory optimization} with {learned value or policy prior}.

**Verify in primary sources:**

- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### model rollout horizon trades synthetic coverage against accumulated error

`wm.usage-note.rollout-horizon.001` · usage_note · world_models, reinforcement_learning · method, experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Increasing the number of learned transitions can provide more synthetic experience but also exposes training or planning to errors that compound under the rollout distribution.

**Use:** Treat rollout length as an algorithmic choice tied to model accuracy and policy shift. Report its schedule and include a sensitivity study when central to the claim.

**Avoid:** Do not state that shorter or longer model rollouts are universally better across data regimes and tasks.

**Patterns:**

- We use a rollout horizon of {k}; longer rollouts degrade {metric} as prediction errors accumulate.
- The rollout horizon increases from {a} to {b} as the model is trained on more real data.

**Verify in primary sources:**

- `janner2019mbpo` — [When to Trust Your Model: Model-Based Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html) (NeurIPS 2019)
- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
