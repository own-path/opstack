---
name: opstack-swarm
description: Run opstack's native multi-agent workflow for independent discovery, implementation slices, or review lenses. A strong main model owns planning and verification; smaller, cheaper workers available in the developer’s environment execute bounded tasks using the relevant installed skills from Daryl's 146-skill library.
---

# Native opstack swarm

opstack owns the plan, role policy, briefs, task lifecycle, and verification. Use the current client's native subagent execution and result collection. Use opstack-swarm for orchestration even when the older imported `swarm` skill is present. This workflow does not require that optional QuickJS swarm skill, a third-party orchestration framework, or separate model credentials.

## Resolve roles before dispatch

The main agent is the orchestrator: preferred models are GPT 6.1 Sol or Claude Opus 5.5. It owns repository understanding, architecture, task decomposition, integration, and final verification. Workers use a smaller, lower-cost model available in the developer’s environment that is capable of the assigned task. Luna and Sonnet are examples, not an exclusive list. See [model policy](references/model-policy.example.json) and [client adapters](references/clients.md).

Identify actual model IDs/aliases offered by the current client’s tools or model picker. Select the smallest/lightest available model that can meet the task’s acceptance criteria and is lower-cost than the orchestrator under the developer’s environment or approved budget policy. Use client-provided cost tiers, configured rates, or the developer’s explicit selection; do not infer price from a family name. There is no model-family allowlist. If relative cost is unknown, report that uncertainty and resolve the worker choice rather than claiming it is cheaper. Use the configured explicit worker model on every dispatch; never let workers silently inherit the main model. Verify the effective model from runtime metadata when available. A prompt that calls a worker "cheap" does not select a model or establish its cost. Do not silently substitute an expensive model, change the main conversation's model, or bypass organization restrictions. If a cheaper worker cannot be selected, do the work sequentially in the main session and report that fallback. If the client substitutes a different model, stop further dispatch and reconcile the mapping. Do not claim an unobservable effective model was confirmed.

Start with up to 3 active workers, bounded by the client's available capacity and the user's limits. Use fewer when that is enough. Never create recursive swarms. Follow user-configured role choices when they differ from the example.

## Attach the domain library

The [catalog](references/library-catalog.json) lists the 146 selected skills across UI (21), coding/tooling (13), AI (22), Databricks (38), visuals (8), documents (24), and templates (20). Identify which are actually installed or exposed by the client. A catalog entry alone is not an installed capability. Full-stack setup must check all 146; explicitly report missing skills and unavailable integrations.

Choose only the relevant domain skills per task and give each worker their exact names, accessible SKILL.md paths or provided instructions, and required supporting references. Do not assume a worker inherits the parent's loaded skills or conversation. A UI task may use break-ui and mobile-native; a Swift task write-swift; an AI task ecosystem-primer plus the appropriate framework skill; a Databricks task its relevant core and domain skills. Do not load all 146 into every worker or substitute copied instructions for missing service tools.

If the full library is absent, say which relevant skills are missing. Continue with the self-contained opstack workflows when useful and label that as core-only execution; do not claim it used the full stack. Model tiers and task permissions apply even if an imported skill recommends a different model or nested agents.

## Plan ready, independent work

Keep a compact task table in the parent context, or in the project's existing task-tracking location when persistent tracking is needed. Each row contains: ID, objective, source revision, read-only or write scope, owned files/worktree, dependencies, domain skills, acceptance criteria, attempt, worker handle/model, and status.

Choose one pattern:

- Discovery: parallel read-only questions about separate subsystems; parent reconciles the map.
- Implementation: independent file-owned slices with shared contracts settled first. The parent owns common types, lockfiles, migrations, and integration edits unless explicitly assigned to one worker.
- Review: separate read-only correctness, state/concurrency, UI, or security lenses over the same fixed diff; parent verifies and deduplicates findings. Reviewers may inspect overlapping files because they do not write them.

Only dispatch rows whose dependencies the parent has verified and whose write ownership does not overlap running tasks. Separate worktrees do not make conflicting edits independent. Settle shared interfaces first, then parallelize consumers. Shared-workspace writes need disjoint ownership; use isolated worktrees for larger edits when available. Do not assume an agent API accepts a working-directory field it does not expose.

## Dispatch, collect, integrate

Give each worker a self-contained [brief](references/brief.md): objective, revision/worktree, scope, relevant instructions/skills, constraints, explicit model, acceptance checks, and required result evidence. Workers may not spawn others or broaden the task. Use available runtime read-only restrictions for reviewers; instruction text alone does not enforce a tool boundary.

Track actual handles. Collect results using native status/wait tools, not invented APIs. A worker's "done" means returned, not verified. Inspect its real diff or findings, confirm it used the intended source revision, run the meaningful checks yourself, and accept or reject the result. Integrate in dependency order and run combined checks against the actual integrated build. Keep architecture and final approval in the main agent.

If a worker fails, times out, or loses ownership, stop it or confirm it has stopped before reassignment. Inspect partial edits first. Give a retry a new attempt number and handle, with at most 2 attempts per task unless the user changes that limit. Ignore stale results from earlier attempts. Do not replay external actions blindly. Cancelled tasks do not unblock dependents. On user cancellation, stop outstanding workers and summarize preserved partial work. Never clean up worktrees containing unreviewed changes automatically.

Use the [task lifecycle](references/lifecycle.md). If native delegation is unavailable, execute the same dependency-ordered plan sequentially and label it honestly. Shell background jobs are not model workers.

Finish with verified outcomes, actual model selections (or their verification limits), relevant domain skills used, task statuses, checks run, and remaining work. Swarm authorization does not add permission to publish, merge, message others, or change accounts.
