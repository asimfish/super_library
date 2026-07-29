# Super Library card: wm.term.stochastic-latent-state.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

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

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/world_models.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
