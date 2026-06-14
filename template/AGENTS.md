# AGENTS.md

This file is the executable contract boundary for local coding agents: keep only rules that constrain read/change/decision/verification behavior, and move project facts, rationale, and plans elsewhere.

## Context precedence

When instructions conflict, follow this priority: user prompt > AGENTS.md > local code comments > repository docs, and report back the mismatch.

## Project governance

Read [development.md](decisions/development.md) before making workflow-level changes.

Do not modify project scope, dependencies, or public contracts without explicit maintainer approval.

- Public project documentation belongs in [docs/](docs/).
- Development-process decisions belong in [decisions/](decisions/).
- Private local notes belong in [notes_local/](notes_local/) and should not be committed.

## Contract-first workflow

Contract precedes implementation.

For code:

- define public input/output behavior first;
- write tests against the public boundary before relying on internals;
- if a test must depend on hidden implementation details, refactor until the real boundary is explicit;
- create skeletons before internal logic.

For docs:

- create headings before prose;
- pseudo-code is preferred over prose in planning for clarifying language-independent design before real code implementation.

## Documentation budget

Markdown files should stay under 100 lines. If a file grows beyond that, apply:

1. pruning — delete stale, repeated, or non-actionable text;
2. refactor — split durable subtopics into linked files;
3. compress — shorten language without weakening the contract.

## Formatting policy

- Do not manually reflow code only for visual alignment.
- Do not hard-wrap anything beyond code, such as Markdown, comments, git commit messages, and docstrings, merely to satisfy a visual line length.
- For prose, prefer semantic line breaks: one sentence or one logical clause per line when helpful.

## Implementation policy

- Execution briefs must optimize for the smallest conceptual diff, not the cleanest-looking architecture.
- Prefer a correct plain-code first pass.
- After the code works, simplify by removing unnecessary helpers, wrappers, and dead structure.
- Do not add abstraction before two concrete uses or an explicit contract boundary.
- When implementation friction appears, produce the smallest failing evidence before proposing a broader redesign.

## Definition of done

A task is done only when:

- the diff is limited to the requested scope;
- relevant tests were added or updated;
- validation commands ran or the reason for not running is stated.

This project has no language tooling yet; record its validation commands here once it does, following the change control in [development.md](decisions/development.md).

If a command is not run, state why.

## Completion report

Do not commit, push, or open pull requests unless explicitly requested.

After completing a task, report:

- what changed;
- what was validated;
- what was not validated and why;
- any remaining blocker;
- a suggested commit message.

The developer reviews the diff and performs the commit manually.
