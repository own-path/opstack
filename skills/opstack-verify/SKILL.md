---
name: opstack-verify
description: "Choose and run meaningful validation for a code change, verify the actual build under test, and report evidence and remaining limits."
---

# Verify what changed

## Foundation in the selected skills

[eval-engineering](../eval-engineering/SKILL.md), [langsmith-evaluator](../langsmith-evaluator/SKILL.md), [databricks-aibi-dashboards](../databricks-aibi-dashboards/SKILL.md), [manimce-best-practices](../manimce-best-practices/SKILL.md)

Use the domain skill’s actual validation method: evaluation/verifier evidence for agent work, evaluator construction for LangSmith, query validation for Databricks dashboards, and rendering checks for Manim. Keep checks proportionate and scoped to the domain. Read only the sources applicable to the current task and preserve their scope and requirements.


Tie each acceptance criterion to an observable check. Read the project's real scripts and CI expectations before selecting commands. Run the narrow reproduction or behavior test first, plus required type, lint, build, and integration checks relevant to the change. For delegated changes inspect the diff and re-run important checks yourself.

When testing a running app, confirm the process, working tree, and build identity belong to the changed code. Use an existing build/status endpoint if the project has one; do not invent a universal /api/status requirement. For UI inspect actual interactions in the target environment where tools allow it. Test a meaningful failure or boundary path as well as the success path when the change affects recovery.

Record what ran, its result, and any remaining gap. Compare benchmark claims with a reproducible baseline and relevant repeated measurements; do not claim speedups from code inspection. Fix failures caused by this change, distinguish pre-existing failures with evidence, and recheck affected behavior after a fix. Once relevant checks pass, avoid repeating broad suites without a new reason. Do not infer end-to-end success from a unit test or say a check passed when it was skipped.
