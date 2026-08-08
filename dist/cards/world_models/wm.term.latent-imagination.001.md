# Super Library card: wm.term.latent-imagination.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

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

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/world_model_general.md)
- [topic: planning_imagination](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/planning_imagination.md)
