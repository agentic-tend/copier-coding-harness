# copier-coding-harness

This repository is a [Copier](https://copier.readthedocs.io/) template that generates a language-independent, contract-first AI coding harness: an `AGENTS.md` agent contract, a `decisions/` directory of durable workflow contracts, a `docs/` boundary, and a .gitignored `notes_local/` private-notes convention.

<details>
<summary><strong>Why this harness?</strong></summary>

- **Contract before code.** Establish a reviewable source of truth before implementation.
  - [**Clarify contracts.**](https://github.com/agentic-tend/skills/tree/main/clarifying-contracts): The companion skills layer operationalizes the [development workflow](decisions/development.md) with a meta-level procedure that resolves user-owned uncertainty before execution.
  - [**Test before implementation.**](decisions/testing-policy.md): Verifiability over readability[^shinaoka] moves trust from line-by-line reading to tests and external oracles; readable intent remains in the contract.
  - **Make the ontology explicit.** Name the domain entities, relationships, responsibilities, and reasons before implementation mechanics. ("Why" constrains future "how"; "how" alone only describes today's code.)
- **Give the agent a map, not the whole repository.** Self-describing files and linked maps of content keep concerns decoupled, help humans navigate, and spend limited context tokens only on the contracts and decisions relevant to the current task.
- **Improve the production line.** Agents necessitate a new craftsmanship: review and improve the production line, not only each product. Generalize recurring failures into repository-resident contracts, tests, decisions, or procedures so the next run is constrained by what the project has learned.[^shinaoka][^sustainable-automation]

</details>

**This template owns only the harness layer.** It ships no language tooling; when overlaid onto an existing project you review and resolve the resulting diff yourself.

> **Prerequisite: `uv`**
>
> [`uv`](https://docs.astral.sh/uv/) is a Python package and project manager written in Rust. Its `uvx` command runs Copier in an isolated environment, so Copier does not need to be installed globally.

## Standalone generation

Generate a fresh project from the harness (swap `gh:…` for a local path to render from a clone):

```bash
uvx copier copy gh:agentic-tend/copier-coding-harness path/to/new-project
```

Copier asks for `project_name`, `description`, `role_bindings`, and `include_notes_local`; everything else is fixed.

## Overlay on an existing project

The harness can be layered onto a project that already exists, including one generated from another Copier template. Run from the project root and give the harness its own answers file (`.copier-answers.harness.yml`) so it never touches the host's own `.copier-answers.yml`:

```bash
uvx copier copy -a .copier-answers.harness.yml gh:agentic-tend/copier-coding-harness .
```

`project_name` and `description` have no defaults, so this prompts for them interactively. To run unattended, supply them with `-d` (`description` must end with a period, per the `copier.yml` validator):

```bash
uvx copier copy -a .copier-answers.harness.yml \
  -d project_name=my-project \
  -d "description=My project does X." \
  gh:agentic-tend/copier-coding-harness .
```

> [!WARNING]
> **Overlaying is intrusive.** The harness ships `README.md`, `CLAUDE.md`, `AGENTS.md`, and `.gitignore` — files a host usually already has. Copier resolves conflicts per file with a Y/N overwrite (no git-style hunk merge), so start from a clean, committed tree (no `.git`? `git init` first, or accept no safety net), generate without `--overwrite`, then `git diff` and `git checkout -- <paths>` to keep exactly the harness changes you want.
> `copier copy` does not abort on a dirty tree; only `copier update` refuses to run when the tree is dirty, so this clean-tree discipline is on you.

## Update the harness layer

Pull a newer harness version independently of the host's own templates:

```bash
uvx copier update -a .copier-answers.harness.yml
```

### Why a separate answers file

A host project generated from another template already owns `.copier-answers.yml`; the `-a` flag stores this harness's answers in `.copier-answers.harness.yml`, keeping both template layers independently updateable, while standalone generation without `-a` still uses the default file.

| Answers file | Owns | Written by |
| --- | --- | --- |
| `.copier-answers.yml` | the host project's own template | standalone generation, or the host's native template |
| `.copier-answers.harness.yml` | this harness layer | `copier copy`/`update -a .copier-answers.harness.yml` |

## Develop the template

Files under `template/` are copied verbatim unless their names end in `.jinja`, in which case Copier renders them. Validate with:

```bash
uv run --with copier --with pytest --with pyyaml -- pytest tests/
```

## Project Map

- [Roadmap](docs/roadmap.md) tracks incremental milestones and their status.
- [AGENTS.md](AGENTS.md) is the executable contract for coding agents.
- The companion [skills layer](https://github.com/agentic-tend/skills) packages reusable agent skills outside this repository's rules.
- The [development workflow](decisions/development.md) defines roles, stages, and uncertainty routing.
- The [delivery policy](decisions/delivery.md) defines completion, validation, and repository-action boundaries.
- The [implementation policy](decisions/implementation-policy.md) defines how topology may evolve without unnecessary expansion.
- The [testing policy](decisions/testing-policy.md) defines public acceptance evidence.
- The [documentation style](decisions/documentation-style.md) defines how the repository keeps its source of truth readable.
- The [agentic tooling model](docs/agentic-tooling.md) distinguishes rules, skills, and hooks by activation and enforcement.
- [docs/](docs/) presents the public project result.
- `notes_local/` holds private local notes; it is gitignored and must not define project behavior.
- [User-level agent config](docs/user-level-agent-config.md) shows where advanced users can keep personal defaults.

[^shinaoka]: Hiroshi Shinaoka, [*Agentic AI Coding × Rust*](https://shinaoka.github.io/docs/agentic-ai-coding-rust): growing computational-physics code through mechanical verification and an evolving source of truth.
[^sustainable-automation]: Quantum Bay, [*Sustainable Automation: Programming the Programmer*](https://www.jinguo-group.science/sustainable-automation/): persistent instructions and reusable skills for human–AI collaboration across sessions.
