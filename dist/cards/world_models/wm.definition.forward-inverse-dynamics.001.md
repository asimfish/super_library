# Super Library card: wm.definition.forward-inverse-dynamics.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

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

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/world_models.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/world_model_general.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/dynamics_representation.md)
