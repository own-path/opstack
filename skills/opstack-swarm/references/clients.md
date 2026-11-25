# Client execution adapters

The role policy belongs to opstack; execution belongs to the active client's native subagent runtime. Model availability and policy differ across accounts and harnesses. Configuration examples contain no universal provider model IDs or API credentials.

| Client | Native execution | Worker model setup |
| --- | --- | --- |
| Copilot | Use the selected harness's native delegation tool. Current Copilot harness uses `task`; the older VS Code Local harness exposes `agent/runSubagent`. Inspect the actual tool list. | Select a suitable smaller, cheaper model available in that environment through the actual delegation tool or a supported custom-agent `model` field. Use editor completions/model picker; verify what ran. Do not assume Local-harness model rules apply to Copilot. |
| Cursor | Use native subagents in foreground/background and collect their results. | Configure/pass an available cheaper model through the supported subagent mechanism; resolve names from that environment. Avoid inherited main-model workers. |
| Claude Code | Use native `Agent` delegation with read-only restrictions where appropriate. | Choose a supported smaller, lower-cost alias or configured model for the task; `model: sonnet` is one supported example, not a requirement. The main conversation remains the orchestrator. Check `/tasks` model metadata when available; account policies can substitute models. Never assume Luna is offered by Claude. |
| Codex | Use the session's exposed native spawn, message, status, and wait operations. Inspect the real tool schema. | Select an available smaller, cheaper model explicitly. In the development test harness, `gpt-6-luna` is exposed; a full-history fork may prohibit overrides, so use a clean-context worker with a complete brief when required. Other clients may expose different IDs or configuration. |

Example pairings include GPT 6.1 Sol → an available Luna model and Claude Opus 5.5 → an available Sonnet model. These examples do not restrict eligible families or providers. Use any suitable smaller, lower-cost model exposed by the developer’s environment, subject to its policies and actual selection controls. If a runtime has no cheaper-model selector, do not simulate it with a system prompt or enable experimental settings silently: report the limit and work sequentially.

Model-policy setup: inspect the client's exposed models, select a main and explicit worker ID, check the worker fits the task and the developer’s lower-cost policy, record the resolved IDs in the user's existing personal opstack settings/instructions, and verify the first worker's metadata when available. The example JSON is a record of role policy for the agent to read, not a client-native configuration file. Do not tell the user that copying it alone configures their client.

Sources checked: [Copilot/VS Code harness differences](https://code.visualstudio.com/docs/agents/run/subagents), [Cursor subagents](https://cursor.com/docs/subagents), [Claude model selection](https://code.claude.com/docs/en/sub-agents#choose-a-model). Codex's adapter was checked against this development session's actual delegation tool schema.
