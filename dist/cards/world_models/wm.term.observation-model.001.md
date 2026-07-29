# Super Library card: wm.term.observation-model.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

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

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/world_models.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
