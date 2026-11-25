# Maintaining opstack

This repository contains original portable workflow skills, client plugin manifests, a personal instruction template, and a Python installer. Read README.md before changing the package. Keep DEFAULT-PROMPT.md and the README's activation prompt aligned. Keep opstack-mode and personal instructions consistent. The 146 selected domain skills are bundled under skills/ alongside the 13 opstack workflows. Preserve their supporting files, notices, and provenance. Do not add private project rules or credentials.

Use only actual supported client capabilities; do not invent a universal settings key or hardcode model tiers. Use the selected domain skills as the foundation for task routing and worker briefs. Keep workflow orchestration self-contained and report unavailable provider-specific capabilities accurately.

After edits, run `python3 scripts/refresh_integrity.py`, `python3 scripts/install.py --verify`, and `python3 -m unittest discover -s tests -v`. Installer tests must use temporary destinations, never the real home skill folders. Review affected lifecycle transitions against docs/state-machines.md before committing installer changes. Do not execute imported skill helpers to package or copy them.

Report actual evidence and limits. Package tests do not establish that every client has discovered or followed a skill. Do not claim public marketplace approval unless the plugin is actually listed.
