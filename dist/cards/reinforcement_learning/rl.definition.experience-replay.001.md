# Super Library card: rl.definition.experience-replay.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

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

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/rl_theory_evaluation.md)
