# Super Library card: emb.definition.topological-memory.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### topological memory for visual navigation

`emb.definition.topological-memory.001` · definition · embodied_ai · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A graph-based spatial memory whose nodes represent selected observations, places, or landmarks and whose edges encode reachability, adjacency, or local navigational transitions for planning.

**Use:** Specify how nodes are created and merged, what an edge means, how the agent localizes or retrieves in the graph, whether the memory is updated online, and whether unexplored or predicted locations are represented.

**Avoid:** Do not call a dense occupancy grid or an arbitrary scene graph a topological memory unless nodes and edges support navigational connectivity or reachability.

**Patterns:**

- The agent incrementally builds a topological memory whose nodes store {observation features} and whose edges represent {reachability criterion}.
- Planning queries the memory for a path from {localized node} to {goal node or frontier}.

**Verify in primary sources:**

- `cui2024-frontier-enhanced-topological-memory` — [Frontier-enhanced Topological Memory with Improved Exploration Awareness for Embodied Visual Navigation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8905_ECCV_2024_paper.php) (ECCV 2024)
- `taniguchi2021-pose-invariant-topological-memory` — [Pose Invariant Topological Memory for Visual Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Taniguchi_Pose_Invariant_Topological_Memory_for_Visual_Navigation_ICCV_2021_paper.html) (ICCV 2021)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: embodied_navigation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_navigation.md)
