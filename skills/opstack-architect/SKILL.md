---
name: opstack-architect
description: "Design the data shapes, module boundaries, invariants, and validation plan for a feature or refactor before implementation locks in the wrong structure."
---

# Shape the change

Start from a concrete caller and expected output. Read the existing types, public contracts, and nearest comparable implementation. Express states and invalid combinations in the repository's type system where it pays off. Sketch only the changed signatures, ownership boundaries, invariants, and failure behavior.

Use one preferred design with a brief tradeoff. Explore alternatives only when they change a real product or maintenance decision. Reuse existing abstractions when they fit; avoid adding a generic framework for a single caller. Check compatibility, migrations, cancellation, and retry semantics when relevant.

For lifecycle changes, read [opstack-state-review](../opstack-state-review/SKILL.md). Name the smallest behavioral proof before implementing. Settle routine technical choices from repository evidence and proceed into implementation when requested; seek a user decision only for unresolved requirements or consequential product choices. Architecture review does not grant permission to broaden the task.
