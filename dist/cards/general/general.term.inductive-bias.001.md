# Super Library card: general.term.inductive-bias.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### inductive bias

`general.term.inductive-bias.001` · term · general · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A structural assumption built into an architecture, objective, or algorithm that restricts or prefers certain solutions before observing data, shaping what is learned and how much experience is required.

**Use:** Name the bias concretely (architecture, symmetry, prior connectivity, or objective structure), state the assumption it encodes about the task, and support claimed benefits with sample-efficiency, transfer, or ablation evidence rather than intuition.

**Avoid:** Do not credit an unspecified inductive bias for empirical gains, and do not present a bias as universally helpful without noting the tasks where its assumption fails.

**Patterns:**

- {Architecture choice} encodes an inductive bias toward {assumed structure}, improving {metric} in {regime}.
- Ablating {bias source} isolates its contribution to {sample-efficiency or transfer result}.

**Verify in primary sources:**

- `bhattasali2022-neural-circuit-architectural-priors` — [Neural Circuit Architectural Priors for Embodied Control](https://proceedings.neurips.cc/paper_files/paper/2022/hash/52e431bd7689d98426300cb103bb0ee3-Abstract-Conference.html) (NeurIPS 2022)

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/general.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
