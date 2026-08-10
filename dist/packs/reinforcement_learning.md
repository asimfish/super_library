# Super Library pack: reinforcement_learning

Corpus `0.4.0` · snapshot `2026-08-09`.

These are paraphrases, canonical terms, and original sentence patterns.
Verify technical claims in the linked primary sources before citing them.
Read the [selective agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) and [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md) before using this exhaustive pack.

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

### advantage function

`rl.definition.advantage-function.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The difference between the action value and the state value under a policy, measuring how an action compares with the policy's average action at that state.

**Use:** Specify the policy and estimator. When using generalized advantage estimation or another approximation, name its bias–variance parameters.

**Avoid:** Do not interpret a positive estimated advantage as a universal guarantee that the action is optimal.

**Patterns:**

- We estimate $A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s)$ and use it to weight the policy update.
- Positive estimated advantages increase the relative likelihood of the sampled actions.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

### average-reward reinforcement learning

`rl.definition.average-reward-rl.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A continuing-task reinforcement-learning formulation that evaluates a policy by its long-run reward per time step rather than by a finite-horizon or geometrically discounted return.

**Use:** State the limiting-average convention and assumptions such as ergodicity or unichain structure. Distinguish average reward from the differential value or bias function used for policy evaluation and optimization.

**Avoid:** Do not use average-reward RL to mean the arithmetic mean of episodic returns across evaluation runs.

**Patterns:**

- We optimize the long-run average reward under {ergodicity or unichain assumptions}.
- Unlike discounted RL, the average-reward objective evaluates continuing behavior without a geometric discount factor.

**Verify in primary sources:**

- `ganesh2025-sharper-global-convergence-analysis` — [A Sharper Global Convergence Analysis for Average Reward Reinforcement Learning via an Actor-Critic Approach](https://proceedings.mlr.press/v267/ganesh25b.html) (ICML 2025)
- `suttle2023-beyond-exponentially-fast-mixing` — [Beyond Exponentially Fast Mixing in Average-Reward Reinforcement Learning via Multi-Level Monte Carlo Actor-Critic](https://proceedings.mlr.press/v202/suttle23a.html) (ICML 2023)
- `hairi2022-finite-time-convergence-sample` — [Finite-Time Convergence and Sample Complexity of Multi-Agent Actor-Critic Reinforcement Learning with Average Reward](https://iclr.cc/virtual/2022/poster/6851) (ICLR 2022)

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

### constrained Markov decision process (CMDP)

`rl.definition.constrained-mdp.001` · definition · reinforcement_learning · related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An MDP augmented with one or more cumulative cost constraints, so the policy objective optimizes return while satisfying specified cost limits.

**Use:** Define reward, every cost signal, discounting or horizon, thresholds, feasibility assumptions, and whether constraints apply in expectation or with another risk criterion.

**Avoid:** Do not describe an unconstrained penalty objective as a CMDP without stating the corresponding constraints and thresholds.

**Patterns:**

- We formulate the task as a CMDP that maximizes {return} subject to {expected cumulative cost} not exceeding {threshold}.

**Verify in primary sources:**

- `khattar2023-cmdp-within-online-framework` — [A CMDP-within-online framework for Meta-Safe Reinforcement Learning](https://iclr.cc/virtual/2023/poster/11412) (ICLR 2023)
- `zhou2025-chpo-constrained-hybrid-action` — [CHPO: Constrained Hybrid-action Policy Optimization for Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5eca2e4fe7858cbbfef4e08573cfcb25-Abstract-Conference.html) (NeurIPS 2025)

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

### diffusion-based trajectory planning / diffusion planning

`rl.definition.diffusion-planning.001` · definition · reinforcement_learning, world_models · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A decision-making approach that represents trajectories or related planning variables with a diffusion generative model and produces a plan through conditioned or guided iterative denoising.

**Use:** State which states and actions are denoised, the trajectory horizon, conditioning or guidance objective, number of denoising steps, how a plan is selected, and which portion is executed before replanning. Report inference cost separately from task quality.

**Avoid:** Do not conflate trajectory-level diffusion planning with a diffusion policy that predicts only actions conditioned on observations, and do not imply real-time execution without a measured latency protocol.

**Patterns:**

- The diffusion planner iteratively denoises length-{H} state–action trajectories conditioned on {return, goal, or constraint}.
- At each decision point, we sample {number} trajectories, execute {portion}, and replan after {feedback event}.

**Verify in primary sources:**

- `janner2022-planning-diffusion-flexible-behavior` — [Planning with Diffusion for Flexible Behavior Synthesis](https://proceedings.mlr.press/v162/janner22a.html) (ICML 2022)
- `huang2024-diffusion-models-optimizers-efficient` — [Diffusion Models as Optimizers for Efficient Planning in Offline RL](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6735_ECCV_2024_paper.php) (ECCV 2024)

### distributional reinforcement learning

`rl.definition.distributional-rl.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A value-based perspective that models a probability distribution over random returns rather than only their expected value.

**Use:** Specify the distributional parameterization, projection or regression objective, and how action selection reduces the distribution to a decision criterion.

**Avoid:** Do not equate a return distribution with epistemic uncertainty about the value estimate.

**Patterns:**

- The critic approximates the distribution of discounted returns with {atoms or quantiles}.
- Actions are selected by the expectation of the learned return distribution.

**Verify in primary sources:**

- `bellemare2017distributional` — [A Distributional Perspective on Reinforcement Learning](https://proceedings.mlr.press/v70/bellemare17a.html) (ICML 2017)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)

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

### goal-conditioned reinforcement learning

`rl.definition.goal-conditioned-rl.001` · definition · reinforcement_learning · abstract, introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A reinforcement-learning formulation in which the policy or value function is conditioned on a goal representation and optimized to reach or satisfy that goal.

**Use:** Specify the goal space, reward or success definition, goal-sampling distribution, horizon, and generalization split.

**Avoid:** Do not conflate goal conditioning with language conditioning unless language is the defined goal representation.

**Patterns:**

- The policy conditions on goal {g} and maximizes {objective} under goals sampled from {distribution}.

**Verify in primary sources:**

- `cho2023-outcome-directed-reinforcement-learning` — [Outcome-directed Reinforcement Learning by Uncertainty \& Temporal Distance-Aware Curriculum Goal Generation](https://iclr.cc/virtual/2023/poster/11888) (ICLR 2023)

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

### offline-to-online reinforcement learning

`rl.definition.offline-to-online.001` · definition · reinforcement_learning · introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A learning protocol that initializes from a fixed offline dataset and subsequently improves the policy using additional online environment interaction.

**Use:** Report offline data provenance, initialization method, online interaction budget, replay mixture, and whether baselines receive the same data.

**Avoid:** Do not label online fine-tuning as an offline-RL result without separately reporting the online budget.

**Patterns:**

- We initialize from {offline dataset} and continue learning for {online budget} transitions using {data-mixture strategy}.

**Verify in primary sources:**

- `wagenmaker2023-leveraging-offline-data-online` — [Leveraging Offline Data in Online Reinforcement Learning](https://proceedings.mlr.press/v202/wagenmaker23a.html) (ICML 2023)
- `wang2024-making-offline-rl-online` — [Making Offline RL Online: Collaborative World Models for Offline Visual Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b041cbfcc3f282a9b3c8eb9c16177529-Abstract-Conference.html) (NeurIPS 2024)

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

### reward-free exploration

`rl.definition.reward-free-exploration.001` · definition · reinforcement_learning · abstract, introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An exploration setting in which an agent collects information without knowing the downstream reward and later uses the collected data to solve one or more reward-specified tasks.

**Use:** State whether rewards are entirely absent during exploration, which task class is considered, and how planning or learning proceeds after reward revelation.

**Avoid:** Do not use reward-free as a synonym for intrinsic-reward exploration when a designed exploration reward drives data collection.

**Patterns:**

- During reward-free exploration, the agent collects {data}; after receiving {reward specification}, it computes {policy or value function} without further interaction.

**Verify in primary sources:**

- `cheng2023-improved-sample-complexity-reward` — [Improved Sample Complexity for Reward-free Reinforcement Learning under Low-rank MDPs](https://iclr.cc/virtual/2023/poster/11380) (ICLR 2023)
- `qiao2023-near-optimal-deployment-efficiency` — [Near-Optimal Deployment Efficiency in Reward-Free Reinforcement Learning with Linear Function Approximation](https://iclr.cc/virtual/2023/poster/11300) (ICLR 2023)

### unsupervised skill discovery

`rl.definition.skill-discovery.001` · definition · reinforcement_learning · introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The learning of a diverse set of temporally extended behaviors without task-specific external rewards, typically by optimizing an intrinsic diversity or predictability objective.

**Use:** State the skill variable, intrinsic objective, temporal horizon, diversity measure, and downstream adaptation protocol.

**Avoid:** Do not equate visually different trajectories with useful or controllable skills without a downstream criterion.

**Patterns:**

- The agent learns a skill-conditioned policy by maximizing {intrinsic objective} over {skill distribution} before downstream adaptation.

**Verify in primary sources:**

- `chalumeau2023-neuroevolution-competitive-alternative-reinforcement` — [Neuroevolution is a Competitive Alternative to Reinforcement Learning for Skill Discovery](https://iclr.cc/virtual/2023/poster/10722) (ICLR 2023)

### state–action occupancy measure

`rl.definition.state-action-occupancy-measure.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A measure of how frequently a policy visits each state–action pair under the environment dynamics, with the precise weighting determined by a discounted, finite-horizon, or stationary formulation.

**Use:** State the horizon or discounting convention, normalization, initial-state distribution, and whether the measure is stationary. Use it to make a policy objective or coverage assumption explicit.

**Avoid:** Do not confuse a policy occupancy measure with a spatial occupancy map or an occupancy-prediction world model.

**Patterns:**

- We express the objective as a utility of the discounted state–action occupancy measure induced by $\pi$.
- The constraint is defined over the stationary occupancy measure under {ergodicity assumptions}.

**Verify in primary sources:**

- `barakat2025-global-optimality-policy-gradient` — [On the Global Optimality of Policy Gradient Methods in General Utility Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/72411ab2fd50c0d1f1a4489896d96489-Abstract-Conference.html) (NeurIPS 2025)

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

### RL literature should be organized by data regime, interaction budget, information structure, and optimization objective.

`rl.sentence-pattern.related-work-regime.001` · sentence_pattern · reinforcement_learning · related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

A Related Work scaffold for avoiding comparisons between methods that solve materially different reinforcement-learning problems.

**Use:** Select the axes relevant to the cited family and explicitly mark changes in assumptions or supervision.

**Avoid:** Do not present offline, online, model-based, multi-agent, and constrained methods as directly comparable without a common problem setting.

**Patterns:**

- These methods share {objective}, but differ in their data regime ({regimes}), interaction budget ({budgets}), information structure ({information}), and optimization objective ({objectives}).

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

### action gap

`rl.term.action-gap.001` · term · reinforcement_learning · related_work, method

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The difference between the value of a preferred action and that of an alternative action at a state, with the precise comparator determined by the formulation.

**Use:** Define which actions are compared, which value functional or return distribution is used, and whether time is discrete or continuous.

**Avoid:** Do not use action gap as a generic synonym for advantage without specifying the baseline action or policy.

**Patterns:**

- We define the action gap as {value of selected action} minus {value of comparator} under {value criterion}.

**Verify in primary sources:**

- `wiltzer2024-action-gaps-advantages-continuous` — [Action Gaps and Advantages in Continuous-Time Distributional Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/55769e1208c7f45e9acc98f06279c10c-Abstract-Conference.html) (NeurIPS 2024)

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

### deployment efficiency

`rl.term.deployment-efficiency.001` · term · reinforcement_learning · related_work, experiments, method

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The amount of distinct real-world or environment deployment rounds required to collect interaction data, separated from the total number of transitions.

**Use:** Define a deployment round, parallelism, batch size, adaptivity between rounds, and both round and sample complexity.

**Avoid:** Do not call a method deployment-efficient solely because it is sample-efficient.

**Patterns:**

- The algorithm uses {rounds} deployment rounds and {samples} transitions, with policy updates occurring {between or within rounds}.

**Verify in primary sources:**

- `qiao2023-near-optimal-deployment-efficiency` — [Near-Optimal Deployment Efficiency in Reward-Free Reinforcement Learning with Linear Function Approximation](https://iclr.cc/virtual/2023/poster/11300) (ICLR 2023)

### entropy regularization / entropy-augmented objective

`rl.term.entropy-regularization.001` · term · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

An objective term that rewards policy entropy in addition to task return, encouraging stochasticity according to a specified temperature or coefficient.

**Use:** State the entropy convention, coefficient or temperature, and whether it is fixed or adapted. Distinguish action entropy from state-distribution diversity.

**Avoid:** Do not claim that entropy regularization necessarily improves exploration or robustness in every environment.

**Patterns:**

- The actor maximizes expected return and policy entropy with temperature $\alpha$.
- We adapt the entropy temperature toward a target entropy of {value}.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

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

### policy-gradient estimator

`rl.term.policy-gradient-estimator.001` · term · reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A sample-based estimate of the gradient of an expected-return objective with respect to policy parameters.

**Use:** State the objective, sampling policy, advantage or return estimator, importance weights, and variance-reduction method.

**Avoid:** Do not call an arbitrary gradient through a policy network a policy-gradient estimator when it optimizes a supervised or model-predictive loss.

**Patterns:**

- We form the policy-gradient estimator with generalized advantage estimates from on-policy trajectories.
- Importance weights correct the estimator for the difference between {behavior policy} and {target policy}.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

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

### return distribution / value distribution

`rl.term.return-distribution.001` · term · reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The probability distribution of cumulative discounted reward induced by environment randomness and policy actions from a specified state or state–action pair.

**Use:** Condition the distribution explicitly and distinguish its expectation from the full random-return law.

**Avoid:** Do not call a collection of value-network predictions a return distribution unless the learning formulation models random returns.

**Patterns:**

- We approximate the state–action return distribution $Z^\pi(s,a)$ with {representation}.
- The expected value is recovered by taking the mean of the learned return distribution.

**Verify in primary sources:**

- `bellemare2017distributional` — [A Distributional Perspective on Reinforcement Learning](https://proceedings.mlr.press/v70/bellemare17a.html) (ICML 2017)

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

### separate centralized information during training from each agent's execution-time observations

`rl.usage-note.marl-observability.001` · usage_note · reinforcement_learning · related_work, method, experiments

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Multi-agent algorithms may use global state or joint information in training while each deployed agent acts from local observations and internal memory.

**Use:** Report information available to actor, critic, mixer, and replay data at both training and execution; state the partial-observability model.

**Avoid:** Do not call execution decentralized if an actor directly receives privileged global information.

**Patterns:**

- During training, {module} observes {centralized information}; at execution, agent {i} acts from {local history or observation}.

**Verify in primary sources:**

- `phan2023-attention-based-recurrence-multi` — [Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability](https://proceedings.mlr.press/v202/phan23a.html) (ICML 2023)
- `kuba2022-trust-region-policy-optimisation` — [Trust Region Policy Optimisation in Multi-Agent Reinforcement Learning](https://iclr.cc/virtual/2022/poster/6244) (ICLR 2022)

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

### policy evaluation versus control

`rl.usage-note.policy-evaluation-control.001` · usage_note · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Policy evaluation estimates returns for a fixed policy, whereas control additionally seeks or improves a policy to obtain higher return.

**Use:** State whether a theoretical property or operator applies only under a fixed policy or also under policy improvement and maximization.

**Avoid:** Do not transfer a convergence or contraction statement from policy evaluation to control without checking the additional assumptions.

**Patterns:**

- The distributional operator is analyzed separately for fixed-policy evaluation and control.
- Our theorem concerns policy evaluation; the control variant is assessed empirically.

**Verify in primary sources:**

- `bellemare2017distributional` — [A Distributional Perspective on Reinforcement Learning](https://proceedings.mlr.press/v70/bellemare17a.html) (ICML 2017)
- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)

### distinguish safety constraints from robustness to perturbations

`rl.usage-note.safe-robust.001` · usage_note · reinforcement_learning · related_work, experiments, limitations

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Safety concerns satisfaction of specified cost or risk criteria, whereas robustness concerns stability of performance or constraint satisfaction under distributional or observational perturbations.

**Use:** Name the safety criterion, perturbation set or shift, and evaluate reward and violations separately.

**Avoid:** Do not infer safety from average-return robustness or robustness from nominal constraint satisfaction.

**Patterns:**

- We report nominal and perturbed return together with {violation metric} under {specified perturbation set}.

**Verify in primary sources:**

- `liu2023-robustness-safe-reinforcement-learning` — [On the Robustness of Safe Reinforcement Learning under Observational Perturbations](https://iclr.cc/virtual/2023/poster/11925) (ICLR 2023)
- `khattar2023-cmdp-within-online-framework` — [A CMDP-within-online framework for Meta-Safe Reinforcement Learning](https://iclr.cc/virtual/2023/poster/11412) (ICLR 2023)

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
