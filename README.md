# opstack

**Daryl’s 146 selected skills, organized into a native coding stack.**

The actual skill folders, scripts, references, templates, and assets are in this repository under [`skills/`](skills/). A normal clone contains the full library. No separate ZIP, private archive, or import step is required.

The **146 domain skills are the foundation**. Thirteen opstack workflows provide planning, native multi-agent coordination, review, and verification around them: **159 primary skills installed by default**. Workers receive the domain skills relevant to their assigned task; the workflow layer does not replace those skills.

## Where the 146 skills are

[Browse the complete grouped list](library/README.md) · [Workflow foundations](library/workflow-foundations.json) · [Source/provenance records](library/provenance.json) · [Domain routing index](skills/opstack-mode/references/domain-routing.md)

| Selected group | Count | Examples bundled in this repo |
| --- | ---: | --- |
| UI design, implementation, reviews | 21 | `emil-design-eng`, `break-ui`, `mobile-native`, `review-animations` |
| Code review, development, discovery, tooling | 13 | `review-agent`, `write-swift`, `eval-engineering`, `find-skills` |
| AI application development | 22 | `ecosystem-primer`, `langchain-rag`, `langgraph-fundamentals`, `langsmith-evaluator` |
| Databricks development, data, operations | 38 | `databricks-core`, `databricks-apps`, `databricks-jobs`, `databricks-unity-catalog` |
| Visual assets, programmatic animation | 8 | `imagegen`, `canvas-design`, `manim-composer`, `visualize` |
| Documents and workspace tools | 24 | `documents`, `pdf`, `google-docs`, `spreadsheets` |
| Artifact templates | 20 | `artifact-template-system-design`, `artifact-template-project-tracker` |
| **Selected domain skills** | **146** | **Real folders and supporting files under `skills/`** |

Skill folders are flat so sibling references resolve after installation. The grouped list retains your seven categories. Two alternate Claude versions of `pdf` and `skill-creator` are preserved under [`variants/claude/`](variants/claude/); the Python installer selects those for Claude, keeping the primary installed count at 159.

## Install the full stack

Use a supported work-approved Python runtime, preferably **Python 3.12 or newer**. The installer uses only the standard library and remains compatible with Python 3.9+; it does not install or downgrade Python.

```sh
git clone https://github.com/own-path/opstack.git
cd opstack
python3 scripts/install.py --agent copilot --require-library --dry-run
python3 scripts/install.py --agent copilot --require-library
python3 scripts/install.py --agent copilot --check-library
```

Expected result: **159 installed skills**, and **146/146 domain skills available**. On Windows use `py -3` instead of `python3`. The availability check validates basic entrypoint names/frontmatter and rejects symlinked entrypoints; it does not prove that a model has loaded the skills or that every external integration works.

| Client | Installer argument | Default user-level destination |
| --- | --- | --- |
| Copilot | `--agent copilot` | `~/.copilot/skills` |
| Cursor | `--agent cursor` | `~/.cursor/skills` |
| Claude Code | `--agent claude` | `~/.claude/skills` |
| Codex | `--agent codex` | `~/.codex/skills` |

The default is personal across projects, not system-wide. For one repository, pass its supported skill directory explicitly; for example, from a Copilot project use `--target .github/skills`. Files there may enter version control if committed. No credentials, model clients, service accounts, or external packages are installed.

### Existing installations

The installer skips identical skills and stops before copying if a selected existing skill differs. Compare those folders, keep a dated backup, and reconcile personal edits before replacing them. No force-overwrite mode is provided. Native plugin users update through their client’s plugin manager.

`--only NAME ...` intentionally installs a subset and preserves everything else. It is useful for a targeted addition, but it is not a full-stack install. `--check-library` reports missing skills without changing files. The old `--library` archive-import option is no longer needed or supported: the selected library is now part of this repo.

## Make it the default workflow

Open this cloned repo in your agent and paste:

```text
Set up opstack from this repository as my default personal coding stack. Install the bundled 146 domain skills and 13 opstack workflows for this client, run --check-library, and preserve existing customizations and company/repository rules. Register instructions/opstack.instructions.md at personal scope. Use the relevant bundled domain skills for each task and pass them explicitly to swarm workers. Keep planning, architecture, integration, and verification on the strong main model; select capable smaller, cheaper workers available in this developer environment, with no silent expensive fallback. Verify skill discovery and default activation in a fresh chat where possible.
```

[Copy the default prompt](DEFAULT-PROMPT.md) · [Personal instruction template](instructions/opstack.instructions.md)

Installing skills and activating default instructions are separate steps. Register the template at personal user scope using your client’s supported instructions or user-rules mechanism, preserving existing guidance. For VS Code use **Chat: Open Customizations → Instructions → + next to User**. If personal defaults are unsupported, attach the template to the chat and invoke `opstack-mode` explicitly. Local settings do not automatically configure cloud/remote agents.

## How opstack uses your skills

Each opstack workflow explicitly names and links the selected skills it is based on. For example, `opstack-review` uses `review-agent` plus relevant language/UI review skills; `opstack-ui-review` uses your actual design, mobile, gesture, and animation skills; `opstack-learn` uses `learn-taste` and `skill-creator`; native `opstack-swarm` adapts your selected `swarm` skill’s task-table/dispatch/aggregate/retry pattern to native client subagents. See the [complete workflow-to-skill foundation map](library/workflow-foundations.json).

The main agent reads the [domain routing index](skills/opstack-mode/references/domain-routing.md), selects the relevant bundled skills, and reads their actual `SKILL.md` and required references. For example:

- UI work uses the relevant design, component, mobile, gesture, and motion skills.
- AI agent work starts with `ecosystem-primer`, then the appropriate framework and evaluation skills.
- Databricks work uses the applicable core and domain skills.
- A swarm worker receives exact domain skill names and accessible paths/instructions in its bounded brief.

Only relevant skills are loaded for a task; all 146 do not enter every worker’s context. Some bundled skills require provider-specific tools, applications, or accounts. The agent must report unavailable capabilities and use a supported approach where possible; copying instructions does not create those integrations.

## Native swarm

[`opstack-swarm`](skills/opstack-swarm/SKILL.md) is part of opstack itself. It uses client-native subagents, with no QuickJS/PTC swarm runtime or third-party orchestration framework. The older bundled `swarm` skill remains available for its original QuickJS environment; it does not replace opstack’s native orchestration.

The strong main agent owns planning, architecture, integration, and final verification. Examples include GPT 6.1 Sol or Claude Opus 5.5. Workers use **capable smaller, cheaper models available in the developer’s environment**. Luna/Sonnet are examples, not an allowlist. Resolve actual supported model IDs and relative cost from the client or developer-approved configuration; never silently inherit an expensive main model or claim an unknown price is cheaper.

Run up to three independent workers by default. Parallel discovery and review stay read-only. Implementation workers have separate file ownership; shared interfaces are settled first. Only parent-verified results unblock dependencies. A retry waits for the previous worker to stop, uses a new attempt ID, and rejects stale results. If suitable delegation/model selection is unavailable, work sequentially and report that limit.

[Model policy example](skills/opstack-swarm/references/model-policy.example.json) · [Client adapters](skills/opstack-swarm/references/clients.md) · [Task lifecycle](skills/opstack-swarm/references/lifecycle.md)

## Workflow entrypoints

| Workflow | Purpose |
| --- | --- |
| `opstack-mode` | Select domain skills and coordinate delivery |
| `opstack-swarm` | Native parallel discovery, implementation slices, and review lenses |
| `opstack-discover` | Map relevant code and checks |
| `opstack-architect` | Shape boundaries, invariants, and validation |
| `opstack-build` | Implement with repository and domain conventions |
| `opstack-debug` | Reproduce, explain, and prove a fix |
| `opstack-review` | Read-only actionable defect review |
| `opstack-state-review` | Lifecycle, ownership, retries, and concurrency |
| `opstack-ui-review` | Coordinate interface checks with your UI skills |
| `opstack-verify` | Check actual behavior and report evidence |
| `opstack-learn` | Capture explicit corrections at the right scope |
| `opstack-setup` | Install the full stack and activate defaults |
| `opstack-help` | Pick the right skill or workflow |

Example: `Use opstack-mode to add cancellation to this export job.` For a review: `Use opstack-swarm to review this branch with independent correctness and state-transition lenses; keep it read-only.`

## Native plugins

Cursor: import `own-path/opstack` through **Customize → From GitHub Repository**. This repo provides its marketplace and plugin manifests; it is not claimed to be listed in the public Cursor marketplace.

Claude Code:

```text
/plugin marketplace add own-path/opstack
/plugin install opstack@opstack
```

Native Claude commands are namespaced, for example `/opstack:opstack-mode`. Native plugins discover the 159 primary skill folders; the Python Claude installer additionally selects the two bundled Claude-specific alternates. Use either native plugins or copied personal skills in a client to avoid duplicate discovery. Codex plugin metadata is included; the documented Codex setup path is the Python installer.

## Verify and maintain

```sh
python3 scripts/install.py --verify
python3 -m unittest discover -s tests -v
```

After intentional changes regenerate `integrity.json` with `python3 scripts/refresh_integrity.py`. Keep the 146 domain folders and their supporting files intact; preserve source records and notices. Root MIT licensing applies to original opstack content; bundled third-party skills retain their original terms. Databricks license/notice files ship with its skills.

Tests use temporary targets. Package/installer tests and native plugin validation do not certify every model’s behavior or every external service. See [state-machine notes](docs/state-machines.md) and [behavioral evaluation cases](docs/evaluation.md).
