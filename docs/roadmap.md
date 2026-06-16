# Roadmap

This file tracks milestones for proving the harness as a reusable agent-governance layer, ticked as they land and appended to rather than rewritten.

## Rationale

- Template tests prove the harness renders.
- Case studies prove it survives real repositories.
- Evals prove it changes agent behavior rather than only repository shape.
- Failure-driven design keeps new rules tied to observed mistakes instead of speculative policy.

## Shipped

- [x] Init skeleton
- [x] Test layered details
- [x] Tag it
- [x] Self-reference

## Near-term reliability

- [ ] Dogfood existing projects
  - [ ] Julia
  - [ ] Python/PyTorch
  - [ ] Obsidian
- [ ] CI drift-check that self-reference stays in sync with `template/`
- [ ] Add rendered-fixture tests for standalone and overlay generation

## Case studies

- [ ] Case study A: overlay on a legacy scientific Julia repository
- [ ] Case study B: standalone or overlay use in a greenfield Python/PyTorch repository
- [ ] Record conflict-resolution decisions from each case study

## Behavioral evidence

- [ ] Add a minimal evaluation policy for agent-harness effectiveness
- [ ] Record one before/after agent task showing reduced scope creep or validation omissions
- [ ] Add a failure-driven design log linking observed agent failures to contract changes

## Later

- [ ] Add optional skills as task workflows, not as base harness policy
- [ ] Add language-dependent skills only behind Copier questions
- [ ] Reconsider the repository name only if skills become a first-class distribution target
