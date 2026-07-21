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
- [x] Add and dogfood the first repo-level skill, then extract it into the companion skills layer

## Near-term reliability

- [ ] Dogfood existing projects
  - [x] Julia
  - [x] Python/PyTorch
  - [ ] Rust
- [ ] CI drift-check that self-reference stays in sync with `template/`
- [ ] Add rendered-fixture tests for standalone and overlay generation

## Case studies

- [ ] Case study A: overlay on a legacy scientific Julia repository
- [ ] Case study B: standalone or overlay use in a greenfield Python/PyTorch repository
- [ ] Record conflict-resolution decisions from each case study

## Behavioral evidence

- [ ] Add a minimal evaluation policy for the [agentic tooling mechanisms](agentic-tooling.md)
- [ ] Record one before/after agent task showing reduced scope creep or validation omissions
- [ ] Add a failure-driven design log linking observed agent failures to contract changes

## Later

- [ ] Add language-dependent skills only behind Copier questions
- [ ] Evaluate a hooks companion repository only after concrete event and enforcement contracts emerge
