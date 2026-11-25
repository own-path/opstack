# Worker brief and return contract

The parent fills in these fields for each dispatch. Include the actual instruction content or accessible file paths; never assume history or loaded skills are inherited.

```text
Task ID / attempt:
Objective and acceptance criteria:
Repository, source revision, and assigned worktree:
Mode: read-only discovery/review OR bounded implementation
Allowed files / owned paths:
Forbidden edits / shared files owned by parent:
Dependencies already verified by parent:
Relevant repository instructions:
Domain skills to read and their accessible paths:
Explicit native worker model and allowed tier:
Checks to run and observable evidence required:
Constraints: no subdelegation, no unrequested commits/pushes/external actions
Return: task ID + attempt, actual model metadata if exposed, changed paths and
patch/commit reference, checks actually run with results, findings/evidence,
limits and blockers. Do not claim parent integration or final verification.
```

For review tasks, use a bounded diff/revision and return precise reachable failure scenarios. For implementation, do not edit outside owned paths: report a required shared-file change to the parent. A worker finding a blocked dependency must stop that slice and report the block rather than altering its prerequisites.
