# User-level agent config

This file distinguishes repository-owned agent contracts and skills from personal deployments and defaults.

## AGENTS.md

The generated `AGENTS.md` is self-contained by design. Keep a rule in the repository when it should travel with the project and be reviewed with the project, including directory contracts, workflow change control, and project-specific validation commands.

Keep personal defaults that should apply across unrelated repositories in user-level guidance such as `~/.codex/AGENTS.md` or the equivalent file for another agent. Examples include concise diffs, no commits unless requested, validation reporting, and public-boundary tests.

## Skills

A skill packages a reusable task workflow in one `SKILL.md`; there is no aggregate `SKILLS.md`. Repository-specific skills belong in `.agents/skills/`, while reusable user-level skills belong in `~/.agents/skills/`.

The companion [skills collection](https://github.com/agentic-tend/skills) owns reusable procedures outside this repository's rules layer. Its meta-level [Clarifying Contracts](https://github.com/agentic-tend/skills/tree/main/clarifying-contracts) skill operationalizes the development workflow by resolving user-owned semantic uncertainty before execution.

Keeping reusable skills in the user-level collection gives Codex one canonical deployment across repositories and avoids duplicate repository and user-scope copies.

## See also

- [Agentic tooling](agentic-tooling.md) distinguishes ambient rules from on-demand skills and event-triggered hooks.
