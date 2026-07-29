# Super Library card: emb.term.egocentric-observation.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### egocentric observation

`emb.term.egocentric-observation.001` · term · embodied_ai · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Sensory input represented from the agent's current first-person viewpoint rather than from a fixed external or global viewpoint.

**Use:** Name the modality and field of view, and distinguish current observations from accumulated maps or privileged simulator state.

**Avoid:** Do not describe a third-person camera or global map as egocentric.

**Patterns:**

- At each step, the agent receives an egocentric {RGB, depth, or audio-visual} observation.
- The policy does not access {global map or privileged state}.

**Verify in primary sources:**

- `anderson2018vln` — [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html) (CVPR 2018)
- `shridhar2020alfred` — [ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html) (CVPR 2020)
- `chen2020soundspaces` — [SoundSpaces: Audio-Visual Navigation in 3D Environments](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123510018.pdf) (ECCV 2020)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/embodied_ai.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
