# Super Library card: emb.definition.embodied-question-answering.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### embodied question answering (EQA)

`emb.definition.embodied-question-answering.001` · definition · embodied_ai · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An embodied-agent task in which a system uses observations acquired from an environment, through a provided observation history or active exploration, to answer natural-language questions about that environment.

**Use:** Specify whether the agent receives episodic memory or explores actively, the observation modalities, question and answer format, environment split, exploration budget, memory access, and scoring protocol. For knowledge-based EQA, distinguish evidence observed in the environment from external knowledge used for reasoning.

**Avoid:** Do not call static image question answering EQA when the system has no embodied observation history, exploration process, or environment-grounded evidence acquisition.

**Patterns:**

- The EQA agent explores {environment} for at most {budget} steps before producing a natural-language answer.
- We evaluate episodic-memory and active-exploration EQA under {environment split and scoring protocol}.

**Verify in primary sources:**

- `tan2023-knowledge-based-embodied-question` — [Knowledge-Based Embodied Question Answering](https://doi.org/10.1109/tpami.2023.3277206) (TPAMI 2023)
- `majumdar2024-openeqa-embodied-question-answering` — [OpenEQA: Embodied Question Answering in the Era of Foundation Models](https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html) (CVPR 2024)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: embodied_reasoning_agents](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_reasoning_agents.md)
