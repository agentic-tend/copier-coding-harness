# Delivery Policy

This file defines when work is complete and how an agent hands it back to the developer.

## Definition of Done

A task is done only when:

- the diff is limited to the requested scope;
- relevant tests were added or updated;
- validation commands ran or the reason for not running is stated.

Record the project's validation commands in [AGENTS.md](../AGENTS.md) once language tooling exists, following the change control in [development.md](development.md).

## Repository Actions

The developer reviews the diff and normally performs the commit manually.

## Completion Report

After completing a task, report:

- what changed;
- what was validated;
- what was not validated and why;
- any remaining blocker;
- a suggested commit message.

## Commit Attribution

Suggested commit messages use an `Assisted-By: <agent> <email>` instead of `Co-Authored-By:`.
