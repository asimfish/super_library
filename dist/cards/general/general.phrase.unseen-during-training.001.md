# Super Library card: general.phrase.unseen-during-training.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### {unit} not seen during training

`general.phrase.unseen-during-training.001` · phrase · general · abstract, experiments, limitations, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Identifies a held-out evaluation unit relative to the training data or task distribution.

**Use:** Replace unit with the exact held-out axis—environment, task, object, embodiment, instruction, or combination—and describe how the split was constructed.

**Avoid:** Do not imply broad out-of-distribution generalization when only one named axis was held out.

**Patterns:**

- We evaluate on {unit} not seen during training while holding {other factors} fixed.

**Usage attestations:**

- `koh2021pathdreamer` — Official abstract
- `mazoure2022-improving-zero-shot-generalization` — Official abstract
- `wen2025-diffusionvla-scaling-robot-foundation` — Official abstract

**Verify in primary sources:**

- `koh2021pathdreamer` — [Pathdreamer: A World Model for Indoor Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Koh_Pathdreamer_A_World_Model_for_Indoor_Navigation_ICCV_2021_paper.html) (ICCV 2021)
- `mazoure2022-improving-zero-shot-generalization` — [Improving Zero-Shot Generalization in Offline Reinforcement Learning using Generalized Similarity Functions](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9fbdfded5c4d2969d889efc72f85c644-Abstract-Conference.html) (NeurIPS 2022)
- `wen2025-diffusionvla-scaling-robot-foundation` — [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://proceedings.mlr.press/v267/wen25g.html) (ICML 2025)

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/general.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
