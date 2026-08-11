# Super Library card: vla.usage-note.control-latency.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### policy inference latency and control frequency

`vla.usage-note.control-latency.001` · usage_note · vision_language_action, robot_learning · experiments, limitations, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Inference latency measures computation time per policy update, while control frequency describes how often commands are issued; chunking and asynchronous execution can make them differ.

**Use:** Report hardware, batch size, observation resolution, action horizon, synchronization policy, latency statistic, and achieved control rate.

**Avoid:** Do not infer deployability from model size or nominal frequency alone.

**Patterns:**

- On {hardware}, the policy requires {latency statistic} per update and sustains {frequency} Hz with {execution scheme}.

**Verify in primary sources:**

- `hou2025-dita-scaling-diffusion-transformer` — [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html) (ICCV 2025)
- `zheng2025-tracevla-visual-trace-prompting` — [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://iclr.cc/virtual/2025/poster/29130) (ICLR 2025)

Catalog routes:
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [topic: vla_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/vla_models.md)
- [topic: action_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/action_representation.md)
