# opstack

**Daryl's engineering workflow, across coding agents.**

Understand the codebase. Shape the change. Build with intent. Review the transitions. Verify the behavior.

opstack turns those habits into 13 focused skills for Copilot, Cursor, Claude Code, and Codex. It includes a native swarm, a default mode, repository discovery, architecture, implementation, debugging, code review, state-machine review, UI review, verification, and learning from corrections. Simple edits stay simple.

## Make it your default

Clone this repo, open it in your agent, and paste:

```text
Set up or update opstack as my default personal coding workflow. Read README.md and use the supported setup for this client. Preserve customized skills and existing company/repository rules; use --only opstack-swarm to add swarm without overwriting older skills. Enable native opstack-swarm for useful independent tasks. Keep planning, architecture, integration, and verification on a strong main model such as GPT 6.1 Sol or Claude Opus 5.5; explicitly select cheaper Luna/Sonnet workers from this client's available models, with no silent expensive fallback. Import my exported 146-skill library if needed and run --check-library; report missing skills rather than claiming full setup. Register instructions/opstack.instructions.md at personal scope and verify activation in a fresh chat where possible.
```

[Default prompt and fallback](DEFAULT-PROMPT.md) · [Personal instruction template](instructions/opstack.instructions.md)

## Install

Python 3.9 or newer, standard library only. No service accounts, model routing, or external dependencies are configured during installation.

```sh
git clone git@github.com:own-path/opstack.git
cd opstack
python3 scripts/install.py --agent copilot --dry-run
python3 scripts/install.py --agent copilot
```

Use `--agent cursor`, `--agent claude`, or `--agent codex` for another client. On Windows use `py -3` instead of `python3`. Add `--target PATH` to use a custom skills location.

| Client | Default personal destination | Invocation |
| --- | --- | --- |
| Copilot | `~/.copilot/skills` | Ask it to use `opstack-mode`, or select the discovered skill |
| Cursor | `~/.cursor/skills` | `/opstack-mode` |
| Claude Code | `~/.claude/skills` | `/opstack-mode` for copied personal skills |
| Codex | `~/.codex/skills` | `$opstack-mode` |

The installer verifies source and destination files. Identical existing skills stay unchanged. Conflicting skills stop installation before copies begin. It never merges into or overwrites an existing skill directory. An installation lock prevents two opstack installers from writing the same target concurrently. Filesystem errors can leave a partial new skill folder; reconcile that folder or choose a fresh target before retrying.

Installing skills does **not** activate always-on instructions. Use the prompt above to register the personal template through your client's supported customization mechanism. For VS Code, use **Chat: Open Customizations → Instructions → + next to User**. For other clients use their supported personal instructions or user rules. Preserve the existing instruction text. If a personal default is unsupported, attach the template to the chat and invoke the skill explicitly. Local settings do not automatically configure remote/cloud agents.

### Native plugins

Cursor: import `own-path/opstack` through Customize → From GitHub Repository; this repo supplies `.cursor-plugin/marketplace.json` and the `opstack` plugin manifest. The repo is ready for repository import; it is not claimed to be listed in the public Cursor marketplace.

Claude Code:

```text
/plugin marketplace add own-path/opstack
/plugin install opstack@opstack
```

Native Claude plugin commands are namespaced, for example `/opstack:opstack-mode`. For a local development session, `claude --plugin-dir /absolute/path/to/opstack` loads this plugin. Use either the native plugin or copied personal skills in a client to avoid duplicate skill discovery.

The `.codex-plugin/plugin.json` metadata is included for plugin packaging. The Python personal-skills installer is the documented Codex setup path. Native manifest validation and client runtime behavior should be verified with the actual client; automated tests here cover the package and installer.

## Use it

```text
Use opstack-mode to add cancellation to the background export job.
Use opstack-discover to explain how authentication reaches the database.
Use opstack-swarm to review this branch with independent correctness and state-transition lenses.
Use opstack-review to review this branch against main. Keep it read-only.
Use opstack-state-review to check retries, timeouts, and stale workers.
Use opstack-ui-review to check the mobile checkout and its error states.
```

| Skill | Outcome |
| --- | --- |
| `opstack-swarm` | Native parallel discovery, independent implementation slices, and review lenses using cheaper workers |
| `opstack-mode` | Routes the task and owns delivery and verification |
| `opstack-discover` | Evidence-backed map of the relevant code and checks |
| `opstack-architect` | Data shapes, boundaries, invariants, and validation plan |
| `opstack-build` | Focused implementation using the repository's conventions |
| `opstack-debug` | Reproduction, root cause, regression proof, and fix |
| `opstack-review` | Actionable diff findings, ordered by severity |
| `opstack-state-review` | Transition guards, invariants, ownership, and lifecycle risks |
| `opstack-ui-review` | Interaction, accessibility, responsive, and motion checks |
| `opstack-verify` | Actual behavior checks with honest limits |
| `opstack-learn` | Narrow, scoped rules from explicit corrections |
| `opstack-setup` | Client-aware installation and default activation |
| `opstack-help` | Picks a starting workflow and gives an invocation |

The main agent keeps architecture, integration, and verification. The default personal setup enables native swarms for useful independent work: GPT 6.1 Sol / Claude Opus 5.5 main-agent preferences, with explicitly selected cheaper Luna/Sonnet workers. Resolve actual model IDs from the client; never silently inherit an expensive main model for workers. Without suitable native delegation/model selection, work sequentially and report the limit. Worker output is verified by the main agent.

For stateful changes, review the real transition guards under retries, timeouts, concurrency, crash/restart, and sleep/wake. Keep the repository's state-machine document current when relevant. For simple wording or style changes, a proportionate check is enough. Workflows do not add permission to publish, merge, send messages, or change accounts.

## Native swarm

opstack owns the swarm workflow and model-role policy. The client provides the actual subagent execution; no QuickJS/PTC swarm runtime or external orchestrator is required. The strong main agent plans and verifies; up to three Luna/Sonnet workers take independent bounded tasks. Only parent-verified results unblock dependencies. Writers never share ownership of a file concurrently. Retries wait for the previous worker to stop, use a new attempt ID, and reject stale results.

[Workflow](skills/opstack-swarm/SKILL.md) · [Model policy example](skills/opstack-swarm/references/model-policy.example.json) · [Client adapters](skills/opstack-swarm/references/clients.md)

The model-policy JSON records preferences; copying it does not configure a client's models. At setup, the agent resolves the available main/worker model IDs and saves that mapping in personal instructions/settings. If the runtime cannot explicitly select a cheaper worker, it reports the limit and executes sequentially.

### Add swarm to an existing installation

```sh
git pull
python3 scripts/install.py --agent copilot --only opstack-swarm --dry-run
python3 scripts/install.py --agent copilot --only opstack-swarm
```

Then use the updated default prompt above to refresh your personal instructions and activate swarm. `--only` preserves every older skill, including local edits. A full reinstall still stops if older skills differ: compare those opstack folders, keep a dated backup, and reconcile deliberately before installing the newer copies. Native plugin users update their plugin through the client's plugin manager instead. No force-overwrite option is added.

## Full stack: your 146 domain skills

The 13 original workflows have no dependency on a private library or a provider-specific tool. If you have Daryl's previously exported `portable-skills` archive, extract it locally and add it to the same personal skill destination:

```sh
python3 scripts/install.py --agent copilot --library /path/to/portable-skills --require-library --dry-run
python3 scripts/install.py --agent copilot --library /path/to/portable-skills --require-library
python3 scripts/install.py --agent copilot --check-library
```

For the previous `daryls-skills` repository export, point `--library` at its `library` folder. The importer checks the archive's manifest and file checksums, preserves scripts/assets/references, and flattens its 146 selected skills next to the 13 opstack skills: **159 installed skills**. Claude uses that archive's alternate `pdf` and `skill-creator` versions. Copilot and Cursor receive lowercase frontmatter names for the two original capitalized skills. Originals remain unchanged.

The personal archive is not published in this public repo. A clone contains the 13 opstack workflows and a catalog of the 146 skills, not their contents. Full-stack setup must transfer/extract that archive locally and verify availability; it must not claim the 146 were installed from the public repo alone. Domain-specific integrations still require their corresponding tools and accounts on the destination. The swarm assigns the relevant installed UI, coding, AI, Databricks, visual, document, and template skills to each worker; a copied instruction cannot create an unavailable tool.

## Develop and verify

```sh
python3 scripts/install.py --verify
python3 -m unittest discover -s tests -v
```

After intentional changes, regenerate `integrity.json` with `python3 scripts/refresh_integrity.py`. Tests use temporary targets, not real user configuration. See [installer state transitions](docs/state-machines.md) and [behavioral evaluation cases](docs/evaluation.md). Structural and installer tests do not prove that a model will follow every instruction.

## Sources and compatibility

opstack's workflow text is original, grounded in Daryl's stated preferences. Its packaging was inspired by [pstack](https://github.com/cursor/plugins/tree/main/pstack); no pstack skill text or subagents are bundled.

References checked while authoring: [Cursor plugin format](https://cursor.com/docs/plugins), [Cursor skill locations](https://cursor.com/docs/skills), [Claude plugin manifests](https://code.claude.com/docs/en/plugins/manifest-reference), [Copilot personal skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), and [VS Code personal instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions). Codex metadata was compared with an installed plugin manifest; its personal-skills install path follows the user's existing local setup.
