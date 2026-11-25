---
name: opstack-debug
description: "Reproduce a reported defect, find its root cause, prove the regression, and verify the smallest corrective change."
---

# Debug from evidence

Define the failing input, expected behavior, observed behavior, and environment. Trace the real execution path and rank explanations against evidence. Reproduce the issue using the repository's nearest test or executable path before changing code when feasible. When reproduction is blocked, name what is missing and do the independent investigation that remains possible.

For a confirmed code defect, write a focused behavioral test that fails against the old behavior and passes with the fix when a meaningful test path exists. If a UI or integration harness is needed instead, preserve the concrete reproduction and before/after observation. Fix the cause rather than adding retry loops or catch-all fallbacks that hide it.

Consider adjacent callers and the same failure class without expanding into unrelated cleanup. For races, retries, ownership, or persistence, use [opstack-state-review](../opstack-state-review/SKILL.md). Re-run the failing path and relevant neighboring checks, then inspect the final diff. Describe unproven suspicions as open questions, not findings. A passing test is not evidence of a cause it never exercises.
