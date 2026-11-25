# Installer state and invariants

The installer has a single synchronous lifecycle. `--only` narrows the selected install set before conflict checks; unknown names fail before writes. `--check-library` checks all 146 domain entrypoints for basic name/description frontmatter and rejects symlinked entrypoints without copying; it does not prove service-tool availability. `--require-library` refuses a setup missing any required domain skill before creating the target. It does not configure accounts, models, external dependencies, or personal instructions.

| State | Transition | Guard / observable outcome |
| --- | --- | --- |
| Start | Verified | Every expected repository file matches integrity.json; no unexpected skill files |
| Start | Failed | Missing or changed file, unsafe path, or unexpected skill payload |
| Verified | Finished | Verification-only request; no installation writes |
| Verified | Planned | Target is outside the source repository; optional library paths and checksums validate |
| Planned | Conflict | Any existing skill differs; no installation copies or lock writes |
| Planned | Finished | Dry run; destination not created |
| Planned | Locked | Destination exists and exclusive lock creation succeeds |
| Planned | Failed | Existing lock; leave it untouched and report recovery procedure |
| Locked | Copying | Every new skill uses exclusive directory creation; no merging into existing folders |
| Copying | Checked | Installed file maps equal expected maps |
| Copying | Failed | Filesystem error, destination appeared, or installed data mismatch |
| Checked / Failed after lock | Released | Finally block releases this invocation's lock |

## Invariants and failure recovery

- Existing different skills are never overwritten. Identical existing skills remain untouched.
- The lock serializes opstack installers for one target. It is not a general filesystem lock against manual edits or other installers. There is no automatic stale-lock deletion.
- Source and archive verification refuse traversing paths and symlink payloads. A selected skill must have a verified SKILL.md and all copied files must be checksum-covered.
- Copying is not an all-or-nothing transaction. A crash or I/O error can leave partial new folders. Confirm the installer has stopped, inspect any stale lock, and reconcile partial folders or use a fresh target. A subsequent preflight detects partial folders as conflicts.
- A normal failure after acquiring the lock releases it; an abrupt process kill may leave it behind. Never delete a lock on an assumed timeout while another process may still own it.
- A matching repeat install verifies the payload without rewriting existing skill files. Upgrades with changed same-name skills require manual reconciliation; there is no silent force mode.

The installer owns no background process, retry loop, database, watchdog, or persistent job state. Tests cover the transitions involving dry runs, conflicts, repeat installs, locks, selected variants, and invalid sources. Native client discovery and instruction inclusion are separate lifecycle steps verified in the client.

## Swarm tasks

The native multi-agent protocol is defined in [the swarm lifecycle](../skills/opstack-swarm/references/lifecycle.md). Worker returned is distinct from parent verified; only verified results unblock dependents. Write ownership, attempt identity, cancellation, explicit model selection, and stale output are checked by the parent agent against actual native handles. This is an agent protocol, not a background service installed by the Python copier.
