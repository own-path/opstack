# Make opstack my default

Paste this into your coding agent after cloning or downloading this repository:

```text
Set up opstack from this repository as my default personal coding workflow. Read README.md, detect my client, run the installer dry run, then install its core skills. Add instructions/opstack.instructions.md to this client's supported personal instructions, preserving existing guidance and company/repository rules. Use opstack-mode automatically for non-trivial coding tasks; keep small edits proportionate and reviews read-only. Verify skill discovery and instruction activation in a fresh chat where possible. Report anything you could not activate. Do not change shared work-repo settings or install unrelated dependencies.
```

For an agent that cannot register personal instructions, attach `instructions/opstack.instructions.md` to the chat and say:

```text
Use opstack-mode as the default workflow for the coding tasks in this chat. Follow the attached personal instructions alongside this repository's rules.
```

Personal instruction activation differs by client. The installer copies skills; it does not silently modify your global agent configuration. A personal local installation does not automatically configure a cloud agent.
