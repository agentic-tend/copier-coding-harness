# copier-coding-harness

This repository is a [Copier](https://copier.readthedocs.io/) template that generates a language-independent, contract-first AI coding harness: an `AGENTS.md` agent contract, a `decisions/` directory of durable workflow contracts, a `docs/` boundary, and a .gitignored `notes_local/` private-notes convention.

**This template owns only the harness layer.** It ships no language tooling; when overlaid onto an existing project you review and resolve the resulting diff yourself.

## Standalone generation

Generate a fresh project from the harness (swap `gh:…` for a local path to render from a clone):

```bash
uvx copier copy gh:swanchristmas/copier-coding-harness path/to/new-project
```

Copier asks for `project_name`, `description`, `author`, `role_bindings`, and `include_notes_local`; everything else is fixed.

> [!NOTE]
> Copier can't read `git config` (its Jinja is sandboxed), so pass your name explicitly — e.g. `-d author="$(git config user.name)"` — or set it once under `defaults:` in `~/.config/copier/settings.yml`.

## Overlay on an existing project

The harness can be layered onto a project that already exists, including one generated from another Copier template. Run from the project root and give the harness its own answers file (`.copier-answers.harness.yml`) so it never touches the host's own `.copier-answers.yml`:

```bash
uvx copier copy -a .copier-answers.harness.yml gh:swanchristmas/copier-coding-harness .
```

`project_name`, `description`, and `author` have no defaults, so this prompts for them interactively. To run unattended, supply them with `-d` (`description` must end with a period, per the `copier.yml` validator):

```bash
uvx copier copy -a .copier-answers.harness.yml \
  -d project_name=my-project \
  -d "description=My project does X." \
  -d author="$(git config user.name)" \
  gh:swanchristmas/copier-coding-harness .
```

> [!WARNING]
> **Overlaying is intrusive.** The harness ships `README.md`, `LICENSE`, `CLAUDE.md`, `AGENTS.md`, and `.gitignore` — files a host usually already has. Copier resolves conflicts per file with a Y/N overwrite (no git-style hunk merge), so start from a clean, committed tree (no `.git`? `git init` first, or accept no safety net), generate without `--overwrite`, then `git diff` and `git checkout -- <paths>` to keep exactly the harness changes you want.

## Update the harness layer

Pull a newer harness version independently of the host's own templates:

```bash
copier update -a .copier-answers.harness.yml --defaults
```

### Why a separate harness answers file

A host project generated from a language or native Copier template already owns `.copier-answers.yml`. Writing the harness's answers to a dedicated `.copier-answers.harness.yml` keeps the two layers from colliding, so each can be applied, re-answered, and updated with `copier update` on its own. The answers filename is templated as `{{ _copier_conf.answers_file }}.jinja`, so the `-a` flag chooses the layer; standalone generation with no flag still produces the default `.copier-answers.yml`.

| Answers file | Owns | Written by |
| --- | --- | --- |
| `.copier-answers.yml` | the host project's own template | standalone generation, or the host's native template |
| `.copier-answers.harness.yml` | this harness layer | `copier copy`/`update -a .copier-answers.harness.yml` |

## Generated topology

```
new-project/
├── README.md            # project boundary sentence and contributor pointers
├── AGENTS.md            # executable contract for coding agents
├── CLAUDE.md            # shim: @AGENTS.md
├── LICENSE              # MIT
├── .gitignore           # .DS_Store, .claude, notes_local contents
├── .copier-answers.yml  # enables `copier update`
├── decisions/           # durable development-process contracts
│   ├── README.md
│   ├── development.md   # four-role workflow loop and change control
│   ├── documentation-style.md
│   └── testing-policy.md
├── docs/README.md       # public-result boundary, empty until results exist
└── notes_local/README.md  # private notes placeholder (contents gitignored; omit via include_notes_local)
```

## Develop the template

Generated files live under `template/`; `.jinja` files are rendered, and other files are copied verbatim. Validate with:

```bash
uv run --with copier --with pytest --with pyyaml -- pytest tests/
```

## [Roadmap](docs/roadmap.md)

Incremental milestones and their status.

## For contributors

- [AGENTS.md](AGENTS.md) is the executable contract for coding agents.
- [decisions/](decisions/) records durable development-process decisions.
- [docs/](docs/) presents the public project result.
- [notes_local/](notes_local/) holds private local notes; its contents are gitignored and must not define project behavior.
