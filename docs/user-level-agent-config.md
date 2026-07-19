# User-level agent config

This file distinguishes repository-owned agent contracts and skills from personal deployments and defaults.

## AGENTS.md

The generated `AGENTS.md` is self-contained by design. Keep a rule in the repository when it should travel with the project and be reviewed with the project, including directory contracts, workflow change control, and project-specific validation commands.

Keep personal defaults that should apply across unrelated repositories in user-level guidance such as `~/.codex/AGENTS.md` or the equivalent file for another agent. Examples include concise diffs, no commits unless requested, validation reporting, and public-boundary tests.

## Skills

A skill packages a reusable task workflow in one `SKILL.md`; there is no aggregate `SKILLS.md`. Repository skills belong in `.agents/skills/`, while user-level deployments belong in `~/.agents/skills/`.

The repository's [clarifying-contracts skill](../.agents/skills/clarifying-contracts/SKILL.md) is its canonical, reviewable source. To use it across repositories, link the corresponding user-level directory to this source instead of maintaining an independent copy.

Codex may discover the same named skill from both repository and user scopes. Keeping the user-level deployment linked to the canonical source prevents semantic drift even if both entries are visible.
