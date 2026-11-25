---
name: opstack-setup
description: "Install or check opstack for Copilot, Cursor, Claude, or Codex and register its workflow as the user default when requested, preserving existing instructions and skills."
---

# Set up opstack

Identify the active client and supported personal skill location before copying anything. Read the distribution README and use its Python installer when the repository is available. Run a dry run first; preserve conflicting skills and existing personal instructions. Core installs 12 original workflows. The optional local-library import adds the user's own previously exported skills; do not fetch an unverified archive or execute bundled helpers during installation.

For default activation, use the distribution's DEFAULT-PROMPT.md and instructions/opstack.instructions.md. Register the instruction text at personal user scope through the actual client's supported mechanism. Do not put personal defaults in a shared employer repository unless the user explicitly requests that scope. Installing a skill and making a default instruction active are separate steps.

Use the client's current documentation or customization UI to resolve paths; do not invent a cross-client settings key. Keep repository and organization guidance authoritative for conflicts. Do not change models, store tokens, or install external services as part of copying skills. If the client cannot support a default personal instruction, give a manual invocation and explain that limitation.

Open a new chat or reload discovery if the client requires it. Check that opstack-mode is listed and that the personal instruction is included. A listing proves discovery, not compliance: validate the workflow on a small real coding task when requested. Report what was installed, the activation scope, and unavailable tools without claiming untested client behavior.
