---
name: opstack-setup
description: "Install or check opstack for Copilot, Cursor, Claude, or Codex and register its workflow as the user default when requested, preserving existing instructions and skills."
---

# Set up opstack

Identify the active client and supported personal skill location before copying anything. Read the distribution README and use its Python installer when the repository is available. Run a dry run first; preserve conflicting skills and existing personal instructions. Core installs 13 original workflows, including native opstack-swarm. For an existing installation, `--only opstack-swarm` adds the new swarm skill without replacing customized older skills; compare and back up changed older opstack folders before reconciling and reinstalling them. Never force-overwrite local edits. Full-stack setup uses `--library PATH --require-library` and verifies all 146 domain skills with `--check-library`. If the archive is unavailable, locate it with the user or report core-only setup; a repo clone alone does not contain it. The local-library import adds the user's own previously exported skills; do not fetch an unverified archive or execute bundled helpers during installation.

For default activation, use the distribution's DEFAULT-PROMPT.md and instructions/opstack.instructions.md. Register the instruction text at personal user scope through the actual client's supported mechanism. Do not put personal defaults in a shared employer repository unless the user explicitly requests that scope. Installing a skill and making a default instruction active are separate steps.

Use the client's current documentation or customization UI to resolve paths; do not invent a cross-client settings key. Keep repository and organization guidance authoritative for conflicts. Do not change models, store tokens, or install external services as part of copying skills. If the client cannot support a default personal instruction, give a manual invocation and explain that limitation.

Open a new chat or reload discovery if the client requires it. Check that opstack-mode is listed and that the personal instruction is included. A listing proves discovery, not compliance: validate the workflow on a small real coding task when requested. Report what was installed, the activation scope, and unavailable tools without claiming untested client behavior.

For swarm models, read the installed opstack-swarm references/model-policy.example.json. Resolve actual main/worker IDs from this client; main preferences are GPT 6.1 Sol or Claude Opus 5.5, workers are selected from suitable smaller, cheaper models in that environment. Record the chosen IDs in personal instructions/settings. Do not enable worker model inheritance or substitute expensive workers. The model-policy example is a record for the agent, not a universal client settings file.
