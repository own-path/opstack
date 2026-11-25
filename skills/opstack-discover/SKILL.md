---
name: opstack-discover
description: "Map an unfamiliar repository or subsystem before implementation, or answer how code works using file and runtime evidence. Use for repository discovery and codebase walkthroughs."
---

# Discover the codebase

Inspect applicable AGENTS.md and equivalent instructions, git status, build manifests, entry points, architecture docs, CI configuration, and existing checks. Reach first for rg or the environment's fast file search. Trace one real path from input through validation, domain logic, storage, and output. Read the relevant callers and error paths, not only a symbol definition.

Identify generated files, external services, workspace boundaries, and what can be run locally. Verify documented commands against the actual scripts. For an existing behavior, establish what code and tests prove; distinguish intended behavior from inference. Use history only when the user needs the reason behind a decision.

Return a short map with verified paths, the relevant conventions and checks, and the next concrete step. Do not write a full repository encyclopedia or start changing code during a read-only discovery request. Never expose secrets encountered during inspection.
