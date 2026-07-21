# Agentic tooling

This file defines the public model for extending an agentic coding harness without confusing guidance, reusable workflows, and mechanical enforcement.

## Mechanisms

| Mechanism | Activation | Primary role | Enforcement |
| --- | --- | --- | --- |
| Rules | Loaded from the applicable scope, as with `AGENTS.md` | Declare ambient constraints and project context | Interpreted by the agent |
| Skills | Discovered by metadata and loaded when a task calls for them | Package specialized knowledge, workflows, and resources | Interpreted by the agent |
| Hooks | Triggered by a defined event | Observe, automate, block, or transform an operation | May execute mechanically, call external systems, or delegate back to an agent |

Rules, skills, and hooks often become more specialized and mechanically constrained in that order, but this is a tendency rather than their definition.
A repository rule can be highly specific, a skill can be portable, and a hook may lose determinism when it delegates judgment to a model or relies on nondeterministic external state.

## Extension boundary

The harness supplies structure rather than a fixed catalog of customizations.
Developers add or remove rules, skills, and hooks according to both the developer's workflow and the system being developed.

This repository currently provides the rules framework and its documented design philosophy.
The companion [skills collection](https://github.com/swanchristmas/skills) owns reusable on-demand workflows.
Hooks are an unshipped extension point that may later justify a separate companion repository; no hook interface or distribution contract is defined yet.

## Evaluation

Rendered files prove structure, not improved agent behavior.
Evaluation should compare observable agent outcomes before and after a context change against an explicit oracle, then attribute the result to the relevant rule, skill, or hook.

The [Tessl documentation](https://docs.tessl.io/) is a practical reference for reviewing agent context and using [scenario evaluations](https://docs.tessl.io/improving-your-skills/evaluate-skill-quality-using-scenarios) to test whether a skill changes agent output.
It is a reference rather than a project dependency, adopted evaluation platform, or general-purpose agent benchmark.

## See also

- [decisions/](../decisions/) records the concrete workflow, implementation, testing, documentation, and delivery recipes adopted by this repository.
- [roadmap.md](roadmap.md) tracks the evidence still needed to validate this model in practice.
