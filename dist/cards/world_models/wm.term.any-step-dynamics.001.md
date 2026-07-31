# Super Library card: wm.term.any-step-dynamics.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### any-step dynamics model

`wm.term.any-step-dynamics.001` · term · world_models · related_work, method

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A dynamics model trained to predict transitions over variable temporal offsets rather than only a fixed one-step transition.

**Use:** Specify how the prediction interval is represented, which offsets are trained, and how multi-step targets enter the loss.

**Avoid:** Do not assume variable-offset prediction removes compounding error; evaluate rollout fidelity at the horizons used downstream.

**Patterns:**

- Conditioned on temporal offset {delta}, the dynamics model predicts the state after {delta} environment steps.

**Verify in primary sources:**

- `lin2025-any-step-dynamics-model` — [Any-step Dynamics Model Improves Future Predictions for Online and Offline Reinforcement Learning](https://iclr.cc/virtual/2025/poster/30099) (ICLR 2025)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/world_models.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/dynamics_representation.md)
