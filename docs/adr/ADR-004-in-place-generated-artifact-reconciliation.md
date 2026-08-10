# ADR-004: Reconcile generated artifacts in place

Status: Accepted
Date: 2026-08-11

## Context

The repository commits generated distribution and standalone-skill snapshots so
URL-only Agents can use a release without running the build. Replacing entire
generated directories during a build caused cloud-synchronized workspaces to
create numbered conflict copies, even when final file contents were deterministic.

## Driving factors

- Keep committed URL-only and standalone-skill artifacts available.
- Preserve byte-deterministic builds and remove obsolete generated files.
- Avoid replacing directory identities under cloud synchronization.
- Tolerate a file disappearing concurrently during stale-path cleanup.

## Considered options

### A. Overwrite expected files and prune only stale paths

Keep generated directories, write every expected artifact, then reconcile each
managed tree against an exact relative-path set.

### B. Delete and recreate every generated directory

This is mechanically simple, but directory replacement triggers conflict copies
in synchronized workspaces and creates avoidable filesystem churn.

### C. Stop committing generated artifacts

This avoids synchronization churn but breaks the repository's URL-only Agent path
and makes the standalone skill unavailable until a local build is run.

## Decision

Adopt option A. The build writes expected files in place and calls
`prune_generated_tree` with the exact managed file set. It deletes only stale
files or symlinks, removes empty stale subdirectories, preserves expected files,
and tolerates concurrent disappearance. Root artifacts are still overwritten
deterministically.

## Impact

- Repeated builds preserve generated directory identities and do not create
  workspace-level numbered conflict copies in the tested cloud-sync setup.
- Stale artifacts remain deterministically removable.
- Every new generated artifact family must be added to its reconciliation set;
  tests cover preservation of expected files and repeated-build byte equality.
