# copier-coding-harness

This repository is a [Copier](https://copier.readthedocs.io/) template that generates a language-independent, contract-first AI coding harness: an `AGENTS.md` agent contract, a `decisions/` directory of durable workflow contracts, a `docs/` boundary, and a gitignored `notes_local/` private-notes convention.

It generates no language tooling; users add source, tests, and build structure themselves after generation.

## Generate a project

```bash
uvx copier copy gh:swanchristmas/copier-coding-harness path/to/new-project
```

Or from a local clone:

```bash
uvx copier copy path/to/copier-coding-harness path/to/new-project
```

Copier asks for `project_name`, `description`, `author`, and optional `role_bindings`; everything else is fixed.

## Generated topology

```
new-project/
├── README.md            # project boundary sentence and contributor pointers
├── AGENTS.md            # executable contract for coding agents
├── CLAUDE.md            # shim: @AGENTS.md
├── LICENSE              # MIT
├── .gitignore           # notes_local/, .DS_Store, .claude
├── .copier-answers.yml  # enables `copier update`
├── decisions/           # durable development-process contracts
│   ├── README.md
│   ├── development.md   # four-role workflow loop and change control
│   ├── documentation-style.md
│   └── testing-policy.md
└── docs/README.md       # public-result boundary, empty until results exist
```

## Develop the template

Generated files live under `template/`; only `.jinja`-suffixed files are rendered. Validate with:

```bash
uv run --with copier --with pytest --with pyyaml -- pytest tests/
```

## Roadmap

- Language layers (Julia package, Python package, Markdown/Obsidian vault) introduced through Copier tasks once the core template is stable; until then, users add language-specific structure themselves.
- Language style contracts (e.g. a generalized hybrid Julia style decision) ship with their language layer, not with the core.
