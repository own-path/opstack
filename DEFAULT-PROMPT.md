# Make opstack my default

Paste this into your coding agent after cloning or downloading this repository:

```text
Set up or update opstack as my default personal coding workflow. Read README.md and use the supported setup for this client. Preserve customized skills and existing company/repository rules; use --only opstack-swarm to add swarm without overwriting older skills. Enable native opstack-swarm for useful independent tasks. Keep planning, architecture, integration, and verification on a strong main model such as GPT 6.1 Sol or Claude Opus 5.5; explicitly select smaller, cheaper workers available in the developer’s environment from this client's available models, with no silent expensive fallback. Import my exported 146-skill library if needed and run --check-library; report missing skills rather than claiming full setup. Register instructions/opstack.instructions.md at personal scope and verify activation in a fresh chat where possible.
```

For an agent that cannot register personal instructions, attach `instructions/opstack.instructions.md` to the chat and say:

```text
Use opstack-mode as the default workflow for the coding tasks in this chat. Follow the attached personal instructions alongside this repository's rules.
```

Personal instruction activation differs by client. The installer copies skills; it does not silently modify your global agent configuration. A personal local installation does not automatically configure a cloud agent.
