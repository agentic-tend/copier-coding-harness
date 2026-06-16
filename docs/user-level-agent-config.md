# User-level agent config

This file explains how the generated repository-level agent contract relates to personal agent defaults.

The generated `AGENTS.md` is self-contained by design. It may duplicate personal defaults stored in `~/.codex/AGENTS.md`, `~/.claude/CLAUDE.md`, or other tool-specific memory files.

Keep a rule in the generated repository when it should travel with the project and be reviewed with the project. Examples of repository-level rules include `docs/`, `decisions/`, `notes_local/`, workflow change control, and project-specific validation commands.

Move or duplicate a rule into user-level config only when it is a personal preference that should apply across unrelated repositories. Examples of user-level defaults include concise diffs, no commits unless requested, validation reporting, and public-boundary tests.
