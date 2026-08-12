# Super Library card: rl.definition.differentiable-simulation.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

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

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
- [topic: imitation_sequence](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/imitation_sequence.md)
