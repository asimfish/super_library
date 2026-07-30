# Super Library card: vla.term.visual-trace-prompting.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### visual trace prompting

`vla.term.visual-trace-prompting.001` · term · vision_language_action, robot_learning · related_work, method

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A prompting mechanism that augments visual input with spatial or temporal traces intended to expose task-relevant motion structure to a policy.

**Use:** Identify how traces are produced, whether they are available at training and inference time, and what spatial-temporal information they encode.

**Avoid:** Do not generalize the mechanism beyond the paper-specific trace construction without evidence.

**Patterns:**

- Visual trace prompting supplies {trace type} to highlight {spatial-temporal relation} before action prediction.

**Verify in primary sources:**

- `zheng2025-tracevla-visual-trace-prompting` — [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://iclr.cc/virtual/2025/poster/29130) (ICLR 2025)

Catalog routes:
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/vision_language_action.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [topic: vla_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/vla_models.md)
