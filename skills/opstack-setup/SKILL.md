---
name: opstack-setup
description: "Install or check opstack for Copilot, Cursor, Claude, or Codex and register its workflow as the user default when requested, preserving existing instructions and skills."
---

# Set up opstack

## Foundation in the selected skills

[skill-installer](../skill-installer/SKILL.md), [plugin-management](../plugin-management/SKILL.md), [find-skills](../find-skills/SKILL.md)

Use the selected installer/discovery/plugin guidance within its stated scope when extending or connecting the stack. Installing this already-bundled repository uses opstack’s local copier; it does not need to download the selected skills again or connect accounts. Read only the sources applicable to the current task and preserve their scope and requirements.


Identify the active client and supported personal skill location before copying anything. Read the distribution README and use its Python installer when the repository is available. Run a dry run first; preserve conflicting skills and existing personal instructions. The default install copies all 146 bundled domain skills plus 13 opstack workflows: 159 primary skills. No separate archive is needed. Run `--require-library` for a full install and `--check-library` afterwards. The repo includes scripts, assets, references, and two Claude alternate versions; the installer selects the alternates for Claude automatically. For existing installs, compare conflicting folders, keep a dated backup, and reconcile custom edits before replacing them. Never force-overwrite local work. `--only` deliberately installs a subset and does not claim full-stack setup. Do not execute bundled domain helpers merely to install them.

For default activation, use the distribution's DEFAULT-PROMPT.md and instructions/opstack.instructions.md. Register the instruction text at personal user scope through the actual client's supported mechanism. Do not put personal defaults in a shared employer repository unless the user explicitly requests that scope. Installing a skill and making a default instruction active are separate steps.

Use the client's current documentation or customization UI to resolve paths; do not invent a cross-client settings key. Keep repository and organization guidance authoritative for conflicts. Do not change models, store tokens, or install external services as part of copying skills. If the client cannot support a default personal instruction, give a manual invocation and explain that limitation.

Open a new chat or reload discovery if the client requires it. Check that opstack-mode is listed and that the personal instruction is included. A listing proves discovery, not compliance: validate the workflow on a small real coding task when requested. Report what was installed, the activation scope, and unavailable tools without claiming untested client behavior.

For swarm models, read the installed opstack-swarm references/model-policy.example.json. Resolve actual main/worker IDs from this client; main preferences are GPT 6.1 Sol or Claude Opus 5.5, workers are selected from suitable smaller, cheaper models in that environment. Record the chosen IDs in personal instructions/settings. Do not enable worker model inheritance or substitute expensive workers. The model-policy example is a record for the agent, not a universal client settings file.
