# Development Workflow

This file records durable workflow decisions. Executable rules for local coding agents remain in [AGENTS.md](../AGENTS.md).

## Decision

Separate theory and architecture review, bounded implementation, validation, and final review.

## Roles

Use a four-role loop for nontrivial development work where the role boundary is based on uncertainty type:

- Human: goal alignment, taste, final empirical acceptance
- Exploration agent: knowledge-surface uncertainty and path exploration
- Architecture reviewer: topology, contracts, documentation boundaries
- Execution agent: executable identity, local API details, tests, and concrete diffs

The pipeline is allowed to iterate. If implementation exposes a wrong abstraction, return to *the Architecture reviewer*. If architecture review exposes missing theory or package-level uncertainty, return to *the Exploration agent*. If exploration produces multiple plausible routes, the Human selects or rejects based on project taste and observed cost.

## Current Bindings

Exploration agent → ChatGPT; Architecture reviewer → Claude; Execution agent → Codex

## Change Control

- Workflow-level changes update this file first. Update [AGENTS.md](../AGENTS.md) only when executable agent behavior changes.
- Public project explanation belongs in [docs/](../docs/), while development-process decisions belong in this directory.
- Transient execution state belongs in issues, pull-request bodies, prompts, commits, or test failures.
