# Swarm task lifecycle

This is the parent agent's task protocol, not a distributed service or an executable model runner. Native tool handles and observed results are authoritative. Track task ID and attempt separately from a worker's display name.

| State | Can advance to | Guard |
| --- | --- | --- |
| pending | ready | All prerequisites parent-verified, exact revision settled, no write-owner collision |
| ready | running | Slot available, explicit cheaper model selected, brief complete, native handle obtained |
| running | returned | Matching active attempt returns evidence |
| returned | verified | Parent inspects actual output and passes acceptance checks |
| running / returned | failed | Actual error, timeout, rejected evidence, or wrong revision/model |
| failed | ready | Previous attempt stopped, partial edits reconciled, retry count below limit, new attempt assigned |
| pending / ready / running | cancelled | User cancellation or invalidated scope; stop worker before releasing write ownership |

Only verified unblocks dependents. A pending row with failed/cancelled prerequisites remains blocked; do not silently treat it as skipped success. Claims of verification without parent checks stay returned.

Ignore late output from superseded attempts and invalidate dependent evidence after a relevant source revision changes. Release write ownership only after the prior worker is known to have stopped. A disconnected or unresponsive worker with unknown liveness retains its ownership; keep conflicting work blocked, preserve known partial work, and report the limitation.

A review-only swarm may inspect the same diff in parallel but cannot acquire write scope. The parent owns conflict resolution, result aggregation, verification, and the final summary. Worker roles cannot create more workers unless the user deliberately changes this bounded policy.
