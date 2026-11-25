# opstack

**Daryl's engineering workflow, across coding agents.**

Understand the codebase. Shape the change. Build with intent. Review the transitions. Verify the behavior.

opstack turns those habits into 12 focused skills for Copilot, Cursor, Claude Code, and Codex. It includes a default mode, repository discovery, architecture, implementation, debugging, code review, state-machine review, UI review, verification, and learning from corrections. Simple edits stay simple.

## Make it your default

Clone this repo, open it in your agent, and paste:

```text
Set up opstack from this repository as my default personal coding workflow. Read README.md, detect my client, run the installer dry run, then install its core skills. Add instructions/opstack.instructions.md to this client's supported personal instructions, preserving existing guidance and company/repository rules. Use opstack-mode automatically for non-trivial coding tasks; keep small edits proportionate and reviews read-only. Verify skill discovery and instruction activation in a fresh chat where possible. Report anything you could not activate. Do not change shared work-repo settings or install unrelated dependencies.
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
Use opstack-review to review this branch against main. Keep it read-only.
Use opstack-state-review to check retries, timeouts, and stale workers.
Use opstack-ui-review to check the mobile checkout and its error states.
```

| Skill | Outcome |
| --- | --- |
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

The main agent keeps architecture, integration, and verification. Delegation happens only when explicitly authorized and available. It verifies delegate output instead of trusting a success summary. No model provider or tier is hardcoded.

For stateful changes, review the real transition guards under retries, timeouts, concurrency, crash/restart, and sleep/wake. Keep the repository's state-machine document current when relevant. For simple wording or style changes, a proportionate check is enough. Workflows do not add permission to publish, merge, send messages, or change accounts.

## Optional: import your personal skill archive

The 12 original workflows have no dependency on a private library or a provider-specific tool. If you have Daryl's previously exported `portable-skills` archive, extract it locally and add it to the same personal skill destination:

```sh
python3 scripts/install.py --agent copilot --library /path/to/portable-skills --dry-run
python3 scripts/install.py --agent copilot --library /path/to/portable-skills
```

For the previous `daryls-skills` repository export, point `--library` at its `library` folder. The importer checks the archive's manifest and file checksums, preserves scripts/assets/references, and flattens its 146 selected skills next to the 12 opstack skills: **158 installed skills**. Claude uses that archive's alternate `pdf` and `skill-creator` versions. Copilot and Cursor receive lowercase frontmatter names for the two original capitalized skills. Originals remain unchanged.

The personal archive is not published in this public repo. Domain-specific integrations still require their corresponding tools and accounts on the destination. Optional installed UI, AI, Databricks, and document skills can complement opstack; a copied instruction cannot create an unavailable tool.

## Develop and verify

```sh
python3 scripts/install.py --verify
python3 -m unittest discover -s tests -v
```

After intentional changes, regenerate `integrity.json` with `python3 scripts/refresh_integrity.py`. Tests use temporary targets, not real user configuration. See [installer state transitions](docs/state-machines.md) and [behavioral evaluation cases](docs/evaluation.md). Structural and installer tests do not prove that a model will follow every instruction.

## Sources and compatibility

opstack's workflow text is original, grounded in Daryl's stated preferences. Its packaging was inspired by [pstack](https://github.com/cursor/plugins/tree/main/pstack); no pstack skill text or subagents are bundled.

References checked while authoring: [Cursor plugin format](https://cursor.com/docs/plugins), [Cursor skill locations](https://cursor.com/docs/skills), [Claude plugin manifests](https://code.claude.com/docs/en/plugins/manifest-reference), [Copilot personal skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), and [VS Code personal instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions). Codex metadata was compared with an installed plugin manifest; its personal-skills install path follows the user's existing local setup.
