# Super Library pack: world_models

Corpus `0.1.0` · snapshot `2026-07-29`.

These are paraphrases, canonical terms, and original sentence patterns.
Verify technical claims in the linked primary sources before citing them.
Read the [self-contained mini contract](https://raw.githubusercontent.com/asimfish/super_library/v0.1.0/dist/super-library-compact.md) before using this pack directly.

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
