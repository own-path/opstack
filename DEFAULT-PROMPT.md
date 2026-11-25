# Make opstack my default

Paste this into your coding agent after cloning or downloading this repository:

```text
Set up opstack from this repository as my default personal coding stack. Install the bundled 146 domain skills and 13 opstack workflows for this client, run --check-library, and preserve existing customizations and company/repository rules. Register instructions/opstack.instructions.md at personal scope. Use the relevant bundled domain skills for each task and pass them explicitly to swarm workers. Keep planning, architecture, integration, and verification on the strong main model; select capable smaller, cheaper workers available in this developer environment, with no silent expensive fallback. Verify skill discovery and default activation in a fresh chat where possible.
```

For an agent that cannot register personal instructions, attach `instructions/opstack.instructions.md` to the chat and say:

```text
Use opstack-mode as the default workflow for the coding tasks in this chat. Follow the attached personal instructions alongside this repository's rules.
```

Personal instruction activation differs by client. The installer copies skills; it does not silently modify your global agent configuration. A personal local installation does not automatically configure a cloud agent.
