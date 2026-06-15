# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a [Copier](https://copier.readthedocs.io/) template, not an application. It generates a
language-independent, contract-first coding harness (an `AGENTS.md` contract, a `decisions/`
directory, a `docs/` boundary, and a gitignored `notes_local/` convention) into a new project. It
emits no language tooling and has no runtime of its own — the only executable code here is the test
suite that renders the template and validates the output.

To change what generated projects receive, edit files under `template/`. Editing files at the
repository root only changes the template's own packaging, not the generated output.

## Commands

```bash
# Run the full validation suite (no local install needed; uv pulls deps on the fly)
uv run --with copier --with pytest --with pyyaml -- pytest tests/

# Run a single test
uv run --with copier --with pytest --with pyyaml -- pytest tests/test_generation.py::test_exact_file_set

# Render the template locally to inspect generated output
uvx copier copy . /tmp/harness-smoke
```

CI ([.github/workflows/ci.yml](.github/workflows/ci.yml)) runs only the pytest command above.

## How rendering works

- [copier.yml](copier.yml) sets `_subdirectory: template`, so everything under [template/](template/)
  is the template root. Anything outside `template/` (this file, `README.md`, `tests/`) is template
  *development* scaffolding and is never copied into generated projects.
- Files ending in `.jinja` are rendered with Jinja2 and emitted with the suffix stripped (e.g.
  `template/README.md.jinja` → `README.md`). All other files are copied verbatim.
- The questionnaire variables are `project_name`, `description`, `author`, and optional
  `role_bindings`. They substitute into `README.md.jinja`, `LICENSE.jinja`,
  `{{ _copier_conf.answers_file }}.jinja`, and `decisions/development.md.jinja` (where
  `role_bindings` drives a conditional block). `description` has a validator requiring a sentence
  ending in a period.
- The answers filename is itself templated (`{{ _copier_conf.answers_file }}.jinja`), so a caller
  can pick a layer-specific answers file via `-a` (e.g. `.copier-answers.harness.yml`) to overlay
  the harness onto a host project; with no flag it renders the default `.copier-answers.yml`.

## Tests are the contract

[tests/test_generation.py](tests/test_generation.py) renders the template into a temp dir and asserts
structural invariants. Treat these as the spec for any template change:

- `EXPECTED_FILES` is the authoritative list of what the template emits. **Adding or removing a file
  under `template/` requires updating this set**, or `test_exact_file_set` fails.
- Every generated `.md` (except the `CLAUDE.md` shim) must open with a boundary sentence — its first
  non-heading line ends with a period — and stay under 100 lines. These same rules are the
  documentation contract the harness ships; template markdown you edit must satisfy them too.
- No rendered file may contain unrendered Jinja (`{{` / `{%`).

## The harness the template ships

The generated files form a layered contract system; understanding the layering matters when editing
any of them under `template/`:

- `AGENTS.md` is the *executable* contract — only rules that constrain an agent's read/change/decide/
  verify behavior. The generated `CLAUDE.md` is a one-line `@AGENTS.md` shim.
- `decisions/` holds *durable* process contracts (workflow roles, testing policy, documentation
  style). Workflow changes update `decisions/development.md` first; `AGENTS.md` changes only when
  executable agent behavior changes.
- `docs/` is the public result boundary; `notes_local/` is private and gitignored.

This repository itself follows the contract it ships, so keep edits scoped, keep markdown under the
100-line budget, and lead each file with its boundary sentence.
