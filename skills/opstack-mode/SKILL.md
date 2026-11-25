---
name: opstack-mode
description: "Run Daryl's default engineering workflow for non-trivial coding tasks: understand the repository, choose a focused approach, implement, review state transitions, and verify the result. Use when opstack is requested or registered as the user's default workflow."
---

# opstack mode

## Foundation in the selected skills

[find-skills](../find-skills/SKILL.md), [ecosystem-primer](../ecosystem-primer/SKILL.md), [ask-emil](../ask-emil/SKILL.md)

Use the existing discovery/router skills for their actual domains, then route to the relevant selected skill rather than substituting a generic recipe. The complete routing index covers all 146. Read only the sources applicable to the current task and preserve their scope and requirements.


Start with the requested outcome and the smallest observable acceptance criterion. Keep the user's objective across follow-up turns. For trivial edits, work directly and verify proportionately; do not turn them into a planning ceremony.

## Choose the path

Read applicable repository instructions and inspect the working tree before changing code. Preserve unrelated work. This stack is built on the bundled 146 domain skills. First use the [domain routing index](references/domain-routing.md) to select the actual domain skills needed for the task, and read their SKILL.md and required references. Then choose the opstack coordination steps below. These workflows organize the domain skills; they do not replace them.

Read only the sibling workflows needed for this task:

| Task | Read |
| --- | --- |
| Independent discovery, implementation slices, or review lenses | [opstack-swarm](../opstack-swarm/SKILL.md) |
| Unfamiliar repository or subsystem | [opstack-discover](../opstack-discover/SKILL.md) |
| Cross-module feature or structural decision | [opstack-architect](../opstack-architect/SKILL.md), then [opstack-build](../opstack-build/SKILL.md) |
| Reproducible defect | [opstack-debug](../opstack-debug/SKILL.md) |
| Diff review | [opstack-review](../opstack-review/SKILL.md) |
| Lifecycle, concurrency, locks, persistence | [opstack-state-review](../opstack-state-review/SKILL.md) |
| Interface work | [opstack-ui-review](../opstack-ui-review/SKILL.md) alongside implementation |
| Check changed behavior | [opstack-verify](../opstack-verify/SKILL.md) |
| Capture an explicit correction | [opstack-learn](../opstack-learn/SKILL.md) |

A review-only request stays read-only. A discovery request produces evidence, not unsolicited changes. For implementation, continue through the relevant verification and review steps without requiring the user to reissue the task. Clarify genuine product ambiguity; resolve routine implementation choices from the repository.

## Keep ownership

Own architecture, planning, integration, and verification. When the user explicitly requests swarm or enables it in their personal default instructions, use [opstack-swarm](../opstack-swarm/SKILL.md) for useful independent work. Keep a strong main model (such as GPT 6.1 Sol or Claude Opus 5.5) and explicitly select smaller, cheaper workers available in the developer’s environment from the actual runtime. Assign bounded tasks with file ownership, relevant domain skills, and acceptance criteria. Treat every delegate's result as a draft: inspect the diff and run the relevant checks yourself. If delegation is unavailable, do the work sequentially. Do not silently change the main model, let workers inherit an expensive model, install extra model clients, or invent subagent APIs.

Before a commit, apply the state review at the scale of the change. Inspect the complete resulting diff for regressions. Use the relevant bundled domain skills as the implementation/review foundation and pass their paths to workers. If a skill requires tools unavailable in this environment, report that limitation and choose a supported approach rather than claiming that capability was exercised. Project and organization rules govern conflicts with personal preferences.

Deliver the outcome first, what changed and why, checks actually run, and any remaining limitation. Claim completion only when the requested acceptance criteria are met; distinguish verified behavior from inference. This workflow does not authorize publishing, merging, messaging, or changing account settings beyond the user's request.
