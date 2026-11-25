---
name: opstack-state-review
description: "Review state machines and lifecycle transitions before committing changes involving retries, background jobs, approvals, locks, concurrency, or persistence."
---

# Review state and transitions

Scale the check: wording or styling needs a glance; lifecycle, retries, background work, approvals, locks, and persistence need a full review. Look for docs/state-machines.md or the repository's equivalent. When a full review is needed and no document exists, audit the relevant explicit and implicit machines and document them in a separate coherent change. Do not interrupt a small unrelated edit with a whole-repository rewrite.

For each affected machine, identify states, owners, invariants, allowed transitions, transition guards, and side effects. Look beyond enums: booleans, nullable IDs, lock files, heartbeats, and timestamps can encode a stage together.

Check retries and duplicate delivery; timeouts and late results; concurrent requests or processes; cancellation and owner/watchdog races; crash/restart; and sleep/wake. Prove that stale workers cannot finalize a newer run and that success, failure, and cleanup preserve the intended ownership where relevant. Trace the actual guards instead of asserting that a lock exists.

Prove confirmed bugs with a test that fails on the old behavior. Rank findings by impact and group related fixes. Keep suspected but unproven problems open with their missing evidence. Update states, invariants, transition tables, watchdog behavior, and finding status alongside the related code change. Keep read-only reviews read-only: recommend document updates rather than making them. State-machine documentation supports executable evidence; it does not replace it.
