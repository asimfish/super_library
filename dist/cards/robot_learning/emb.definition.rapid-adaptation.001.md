# Super Library card: emb.definition.rapid-adaptation.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### rapid online adaptation

`emb.definition.rapid-adaptation.001` · definition · robot_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Updating an internal estimate, context, or behavior during deployment from a short history of recent interaction so the policy can respond to changing dynamics or conditions.

**Use:** Specify what adapts, whether policy parameters change, the adaptation window, supervision, and latency.

**Avoid:** Do not call ordinary recurrent inference adaptation unless the changing context and adaptation mechanism are made explicit.

**Patterns:**

- The adaptation module infers {environment context} from a recent history of {states and actions}.
- The base policy responds to changing {terrain or dynamics} without gradient updates at deployment.

**Verify in primary sources:**

- `kumar2021rma` — [RMA: Rapid Motor Adaptation for Legged Robots](https://roboticsproceedings.org/rss17/p011.html) (RSS 2021)

Catalog routes:
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: sim_to_real_robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/sim_to_real_robot_learning.md)
- [topic: locomotion_dexterity](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/locomotion_dexterity.md)
