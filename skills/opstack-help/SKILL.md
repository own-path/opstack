---
name: opstack-help
description: "Explain opstack, select the right workflow for a concrete task, and provide a ready-to-use invocation without doing unrelated implementation."
---

# Help use opstack

## Foundation in the selected skills

[ask-emil](../ask-emil/SKILL.md), [animation-vocabulary](../animation-vocabulary/SKILL.md), [find-skills](../find-skills/SKILL.md)

Use the existing design/motion and capability-discovery routers in their domains, and the complete selected-skill index for other tasks. Recommend the actual relevant selected skill, with an opstack workflow only when coordination is needed. Read only the sources applicable to the current task and preserve their scope and requirements.


Find the user's immediate task and recommend one starting skill. Use opstack-mode for a non-trivial implementation, opstack-discover for understanding, opstack-debug for a bug, opstack-review for read-only defect review, opstack-state-review for lifecycle behavior, and opstack-ui-review for interface quality. Use opstack-swarm for native parallel work with smaller, cheaper workers available in the developer’s environment, and opstack-setup for installation or default activation.

Give a short ready-to-paste example. Bare personal skills use the client's discovered skill name; native plugins can namespace commands (for example, Claude's opstack:opstack-mode). Prefer natural language when the client's slash syntax is unknown. Do not imply an unpublished plugin is listed on a public marketplace.

The core workflows are original and provider-neutral. Optional imported domain skills may require tool-specific integrations. Do not load the entire library to answer a small question. If the user is asking how to make opstack the default, direct them to DEFAULT-PROMPT.md in the distribution.
