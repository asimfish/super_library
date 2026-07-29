# Super Library pack: reinforcement_learning

Corpus `0.1.0` · snapshot `2026-07-29`.

These are paraphrases, canonical terms, and original sentence patterns.
Verify technical claims in the linked primary sources before citing them.
Read the [self-contained mini contract](https://raw.githubusercontent.com/asimfish/super_library/v0.1.0/dist/super-library-compact.md) before using this pack directly.

### actor–critic method

`rl.definition.actor-critic.001` · definition · reinforcement_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A reinforcement-learning method with an actor that represents or updates the policy and a critic that estimates a value-related signal used to guide the actor.

**Use:** State which value quantity the critic estimates, how the actor uses it, and whether updates are on-policy, off-policy, stochastic, or deterministic.

**Avoid:** Do not call every two-network method actor–critic; the functional roles matter.

**Patterns:**

- The actor parameterizes {policy}, while the critic estimates {value quantity} for policy improvement.
- We train the actor and critic from {real or imagined transitions}.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)

### conservative Q-function learning

`rl.definition.conservative-q.001` · definition · reinforcement_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Learning value estimates with an objective that penalizes overly high Q-values, especially for actions not supported by the offline dataset.

**Use:** Describe the exact regularizer and theoretical or empirical property established by the cited method; conservative bias can trade off underestimation and robustness.

**Avoid:** Do not claim that every pessimistic penalty provides a valid lower bound.

**Patterns:**

- The objective regularizes Q-values for out-of-distribution actions while fitting Bellman targets on dataset transitions.
- Conservative value estimation mitigates {specified offline optimization failure}.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)

### multi-agent credit assignment

`rl.definition.credit-assignment.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The problem of determining how individual agents' actions contribute to a shared outcome so that each policy receives an informative learning signal.

**Use:** State whether credit is temporal, agent-specific, or both. Explain the baseline or decomposition used to isolate an agent's contribution.

**Avoid:** Do not equate a global team reward with solved credit assignment.

**Patterns:**

- A counterfactual baseline improves credit assignment by comparing an agent's chosen action with {alternative actions} while holding {other agents} fixed.
- The shared reward provides weak agent-specific credit in {setting}.

**Verify in primary sources:**

- `foerster2018coma` — [Counterfactual Multi-Agent Policy Gradients](https://ojs.aaai.org/index.php/AAAI/article/view/11794) (AAAI 2018)

### maximum-entropy reinforcement learning

`rl.definition.maximum-entropy.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A reinforcement-learning formulation that augments expected reward with a policy-entropy term, trading off task return and stochasticity according to a temperature parameter.

**Use:** Define the sign, temperature, and whether the target entropy or temperature is learned. Avoid vague claims that entropy always improves exploration.

**Avoid:** Do not describe entropy regularization as random action noise; it is part of the policy objective.

**Patterns:**

- We optimize a maximum-entropy objective that combines expected return with {temperature}-weighted policy entropy.
- The temperature controls the reward–entropy trade-off.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

### Markov decision process (MDP)

`rl.definition.mdp.001` · definition · reinforcement_learning · method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A formal sequential decision process defined by states, actions, transition dynamics, and rewards, together with a discount factor or finite horizon when required by the formulation; the next-state distribution depends on the current state and action.

**Use:** List the tuple used in the paper and define any departure, such as partial observability, finite horizon, goal conditioning, or multiple agents.

**Avoid:** Do not assert the Markov property for raw observations when the agent only has partial information.

**Patterns:**

- We model the task as an MDP {tuple}, where {symbol definitions}.
- Because observations are partial, the policy conditions on {history or belief representation}.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

### distribution shift in offline RL

`rl.definition.offline-distribution-shift.001` · definition · reinforcement_learning · introduction, related_work, method, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A mismatch between state–action distributions represented in a fixed dataset and those induced by the learned policy, which makes value estimates for unsupported actions unreliable.

**Use:** Specify whether the shift concerns states, actions, transitions, tasks, or observations. Connect the failure mode to bootstrapping or policy optimization when applicable.

**Avoid:** Do not use 'distribution shift' without naming the two distributions being compared.

**Patterns:**

- Offline policy optimization can induce distribution shift by assigning probability to actions poorly covered by the dataset.
- We regularize {policy or value estimate} toward the support of the behavior data.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

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

### reinforcement learning (RL)

`rl.definition.reinforcement-learning.001` · definition · reinforcement_learning · introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A decision-making framework in which an agent interacts with an environment and learns behavior to maximize expected cumulative reward.

**Use:** Specify observation/state, action, reward, horizon or discount, and whether training is online or offline when these choices matter.

**Avoid:** Do not describe supervised imitation from a fixed dataset as reinforcement learning unless a reward-based objective or RL update is used.

**Patterns:**

- We formulate {task} as reinforcement learning, where the agent observes {observation}, selects {action}, and receives {reward}.
- The objective is to maximize the expected discounted return under {environment distribution}.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

### return-conditioned sequence modeling

`rl.definition.return-conditioned-sequence.001` · definition · reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Modeling actions as a sequence prediction problem conditioned on a desired return together with past states and actions.

**Use:** Specify tokenization, context, conditioning signal, and how desired returns are chosen at inference. Do not assume conditioning guarantees achievement of the requested return.

**Avoid:** Do not describe a return-conditioned model as optimizing return through online RL unless it actually performs such updates.

**Patterns:**

- The policy predicts the next action conditioned on {return-to-go} and {trajectory context}.
- At inference, we condition the sequence model on {target return}.

**Verify in primary sources:**

- `chen2021decisiontransformer` — [Decision Transformer: Reinforcement Learning via Sequence Modeling](https://papers.nips.cc/paper_files/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html) (NeurIPS 2021)

### discounted return

`rl.definition.return.001` · definition · reinforcement_learning · method, experiments, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The cumulative sum of future rewards, commonly weighting a reward received k steps later by a discount factor raised to k.

**Use:** Define horizon, discount convention, termination handling, and whether reported return is undiscounted even if training uses discounting.

**Avoid:** Do not use reward and return interchangeably: reward is typically per transition, whereas return aggregates rewards over time.

**Patterns:**

- The objective maximizes the expected discounted return {equation}.
- We report undiscounted episode return while using {discount} for training.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

### state-value and action-value functions

`rl.definition.value-functions.001` · definition · reinforcement_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A state-value function estimates expected future return from a state under a policy, whereas an action-value function additionally conditions on the current action.

**Use:** Define the policy and return convention under which the expectation is taken. Use Q-function as the standard short form for an action-value function.

**Avoid:** Do not describe Q(s,a) as immediate reward or as a transition probability.

**Patterns:**

- The critic estimates the action-value function {Q symbol} under the current policy.
- The state-value function provides {bootstrap or baseline role}.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)

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

### RL methods should be compared at matched interaction, data, and evaluation budgets.

`rl.sentence-pattern.related-work.001` · sentence_pattern · reinforcement_learning · related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Frames a fair reinforcement-learning comparison around the budgets that determine efficiency and performance.

**Use:** Report environment steps, dataset size, number of seeds, evaluation episodes, compute where relevant, and tuning access. Separate final performance from sample efficiency.

**Avoid:** Do not compare results taken from incompatible protocols without a caveat.

**Patterns:**

- We compare methods at matched environment-interaction budgets and report performance over {number} seeds using {aggregation}.
- Because {prior result} uses a different data budget, we report it separately rather than treating it as a controlled baseline.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### advantage-weighted behavioral cloning

`rl.term.advantage-weighted-bc.001` · term · reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A policy-learning objective that imitates dataset actions with weights increasing with an estimated advantage, favoring actions judged better than the state-dependent baseline.

**Use:** State the weighting function, temperature or clipping, and the source of advantage estimates. It remains constrained to observed actions at training time.

**Avoid:** Do not describe it as ordinary behavior cloning when weights materially change the data contribution.

**Patterns:**

- The policy is trained by advantage-weighted behavioral cloning over actions in the offline dataset.
- Weights are computed from {advantage estimate} with temperature {beta}.

**Verify in primary sources:**

- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

### behavior policy

`rl.term.behavior-policy.001` · term · reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The policy or mixture of policies that generated the data used for learning, which may differ from the policy being evaluated or optimized.

**Use:** Use when data provenance matters. If the dataset combines multiple or unknown collectors, state that rather than implying a single known policy.

**Avoid:** Do not use behavior policy as a synonym for learned target policy.

**Patterns:**

- The offline dataset was collected by an unknown mixture of behavior policies.
- The target policy may select actions outside the support of the behavior data.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

### centralized training with decentralized execution (CTDE)

`rl.term.ctde.001` · term · reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A multi-agent learning paradigm that permits access to joint or global information during training while each agent acts from locally available information at execution time.

**Use:** Specify what is centralized—critic, value, state, communication, or data—and what each deployed policy observes.

**Avoid:** Do not call execution decentralized if agents require unavailable global information at test time.

**Patterns:**

- We adopt CTDE: the centralized critic conditions on {joint information}, whereas each actor observes only {local information}.
- At execution time, agents act without {training-only signal}.

**Verify in primary sources:**

- `foerster2018coma` — [Counterfactual Multi-Agent Policy Gradients](https://ojs.aaai.org/index.php/AAAI/article/view/11794) (AAAI 2018)

### expectile value regression

`rl.term.expectile-regression.001` · term · reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

An asymmetric squared-loss regression objective whose expectile parameter emphasizes different portions of the target distribution; in IQL it is used to fit an upper expectile of in-dataset action values.

**Use:** Define the expectile parameter and targets. Do not describe expectiles as quantiles; they use asymmetric squared rather than absolute loss.

**Avoid:** Do not claim that an upper expectile is the maximum unless limiting conditions are established.

**Patterns:**

- The value function is fitted by expectile regression to emphasize high-valued actions present in the dataset.
- We set the expectile parameter to {tau}.

**Verify in primary sources:**

- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

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

### trust-region policy update

`rl.term.trust-region.001` · term · reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A policy update constrained to keep the new policy sufficiently close to the old policy, commonly measured by KL divergence, to improve optimization stability.

**Use:** Specify whether the constraint is hard, approximate, or implemented through a penalty or clipped surrogate. Do not transfer theoretical guarantees across variants.

**Avoid:** Do not claim monotonic improvement for a practical approximation unless its assumptions and guarantee apply.

**Patterns:**

- The policy update is restricted by a KL-divergence constraint between {old and new policies}.
- A trust region limits the step size in policy space.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)

### value overestimation

`rl.term.value-overestimation.001` · term · reinforcement_learning · introduction, related_work, method, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Systematic upward bias in estimated values, often amplified when optimization selects actions whose estimates are erroneously high.

**Use:** Identify the estimator and distribution on which overestimation is measured. In offline RL, relate it to actions not well supported by data when justified.

**Avoid:** Do not infer overestimation solely because a policy performs poorly.

**Patterns:**

- The critic overestimates values for actions outside the dataset support.
- We measure value overestimation by comparing {predicted quantity} with {reference return}.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)

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

### on-policy versus off-policy learning

`rl.usage-note.on-off-policy.001` · usage_note · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

On-policy updates estimate or optimize the target policy using data generated by that same policy, whereas off-policy methods can learn about a target policy from data generated by a different behavior policy.

**Use:** Describe the actual behavior and target policies, correction mechanism, and data reuse. Finite policy lag is an implementation approximation whose effect depends on the algorithm; recency alone does not make data on-policy.

**Avoid:** Do not equate off-policy with offline: off-policy training may still collect new environment data.

**Patterns:**

- The algorithm is off-policy and reuses transitions from {replay buffer or fixed dataset}.
- Unlike on-policy updates, the critic can learn from data collected by {behavior policy}.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `gu2017asynchronous` — [Deep Reinforcement Learning for Robotic Manipulation with Asynchronous Off-Policy Updates](https://ieeexplore.ieee.org/document/7989385) (ICRA 2017)
- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

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
