---
name: opstack-build
description: "Implement an agreed feature or behavior-preserving refactor using existing repository patterns, then verify and review the resulting change."
---

# Build the requested behavior

Read applicable instructions, current working-tree changes, and the relevant callers. State an observable acceptance criterion. Implement a small coherent change using the project's existing dependencies, patterns, errors, and public interfaces. Remove obsolete code only when the change makes it obsolete; preserve unrelated edits.

For refactors, identify the behavior that must remain equivalent and check representative callers. For new behavior, cover the important success and failure paths. A simple reversible text or style change needs proportionate inspection, not tests that just mirror its source.

Use [opstack-debug](../opstack-debug/SKILL.md) for defects, [opstack-ui-review](../opstack-ui-review/SKILL.md) for UI, and [opstack-state-review](../opstack-state-review/SKILL.md) for affected lifecycle transitions. Run [opstack-verify](../opstack-verify/SKILL.md), inspect the final diff, and fix confirmed regressions introduced by the change. Report checks with their actual outcomes. Do not add a deployment or merge step unless the user's request includes it.
