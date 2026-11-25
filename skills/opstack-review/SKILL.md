---
name: opstack-review
description: "Perform a read-only defect-focused review of a diff, commit, or branch. Inspect affected callers, verify actionable regressions, and report precise findings by severity."
---

# Review a change

Resolve the requested diff and applicable repository instructions. For a branch review use its merge base with the intended target, resolving an upstream when appropriate. Inspect the complete diff and enough surrounding implementation, callers, and tests to understand the affected behavior. Keep review-only work read-only.

Check correctness, architecture fit, security boundaries, error behavior, edge cases, and regressions. For stateful code read [opstack-state-review](../opstack-state-review/SKILL.md); for UI include [opstack-ui-review](../opstack-ui-review/SKILL.md). Confirm each finding from a concrete reachable scenario, with a small test or executable reproduction when possible. Do not run destructive or externally mutating tests just to validate a review.

Report only discrete, actionable problems introduced by the change that the author would reasonably fix. Avoid speculative issues, pre-existing defects, preferences, and formatting nits. Use [P0] for a universal blocker, [P1] urgent, [P2] ordinary defect, [P3] low-impact issue. Each finding cites the tight relevant diff location and explains trigger, consequence, and evidence. Distinguish proven defects from untested concerns. If nothing qualifies, say no findings and state material verification limits. Never invent findings to fill a quota.
