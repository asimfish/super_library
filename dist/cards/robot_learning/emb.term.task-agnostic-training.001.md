# Super Library card: emb.term.task-agnostic-training.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### task-agnostic training (paper-specific usage)

`emb.term.task-agnostic-training.001` · usage_note · robot_learning · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

In RT-1, this label describes joint training with shared parameters across a broad task collection rather than separate task-specific models.

**Use:** Prefer the more explicit phrase 'joint multi-task training with shared parameters' unless discussing the cited paper's terminology. Explain what task information remains available, such as language commands.

**Avoid:** Do not treat 'task-agnostic' as a universally standardized term or imply absence of task conditioning merely because parameters are shared.

**Patterns:**

- The model uses joint multi-task training with shared parameters and conditions on {task instruction}.
- Following {source}, we use 'task-agnostic training' to mean {paper-specific definition}.

**Verify in primary sources:**

- `brohan2023rt1` — [RT-1: Robotics Transformer for Real-World Control at Scale](https://roboticsproceedings.org/rss19/p025.html) (RSS 2023)

Catalog routes:
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
