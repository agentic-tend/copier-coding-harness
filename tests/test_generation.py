"""Structural tests: the template renders and the generated harness honors its own contracts."""

from pathlib import Path

import copier
import pytest
import yaml

TEMPLATE_ROOT = str(Path(__file__).resolve().parents[1])

ANSWERS = {
    "project_name": "DemoProject",
    "description": "DemoProject is a demonstration project for the coding-harness template.",
    "author": "Demo Author",
}

EXPECTED_FILES = {
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "LICENSE",
    ".gitignore",
    ".copier-answers.yml",
    "decisions/README.md",
    "decisions/development.md",
    "decisions/documentation-style.md",
    "decisions/testing-policy.md",
    "docs/README.md",
    "notes_local/README.md",
}


def generate(tmp_path, answers_file=None, **extra):
    dst = tmp_path / "generated"
    options = {"answers_file": answers_file} if answers_file is not None else {}
    copier.run_copy(
        TEMPLATE_ROOT,
        dst,
        data={**ANSWERS, **extra},
        defaults=True,
        vcs_ref="HEAD",
        unsafe=False,
        **options,
    )
    return dst


def generated_files(dst):
    return {
        str(p.relative_to(dst))
        for p in dst.rglob("*")
        if p.is_file() and ".git" not in p.parts
    }


def test_exact_file_set(tmp_path):
    dst = generate(tmp_path)
    assert generated_files(dst) == EXPECTED_FILES


def test_notes_local_excluded(tmp_path):
    dst = generate(tmp_path, include_notes_local=False)
    files = generated_files(dst)
    assert not any(f.startswith("notes_local") for f in files)
    assert files == EXPECTED_FILES - {"notes_local/README.md"}
    # When excluded, notes_local is not mentioned anywhere either.
    assert "notes_local" not in (dst / "README.md").read_text()
    assert "notes_local" not in (dst / ".gitignore").read_text()


def test_no_unrendered_jinja(tmp_path):
    dst = generate(tmp_path)
    for rel in EXPECTED_FILES:
        text = (dst / rel).read_text()
        assert "{{" not in text and "{%" not in text, f"unrendered Jinja in {rel}"


def first_content_line(text):
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return stripped
    return ""


def test_markdown_boundary_sentence_and_budget(tmp_path):
    dst = generate(tmp_path)
    for rel in EXPECTED_FILES:
        # CLAUDE.md has `@AGENT.md` at first line
        if not rel.endswith(".md") or rel == "CLAUDE.md":
            continue
        text = (dst / rel).read_text()
        first = first_content_line(text)
        assert first.endswith("."), (
            f"{rel} does not open with a boundary sentence: {first!r}"
        )
        assert len(text.splitlines()) < 100, (
            f"{rel} exceeds the 100-line documentation budget"
        )


def test_answers_round_trip(tmp_path):
    dst = generate(tmp_path)
    answers = yaml.safe_load((dst / ".copier-answers.yml").read_text())
    for key, value in ANSWERS.items():
        assert answers[key] == value


def test_overlay_answers_file(tmp_path):
    dst = generate(tmp_path, answers_file=".copier-answers.harness.yml")
    files = generated_files(dst)
    assert ".copier-answers.harness.yml" in files
    assert ".copier-answers.yml" not in files
    answers = yaml.safe_load((dst / ".copier-answers.harness.yml").read_text())
    assert answers["project_name"] == ANSWERS["project_name"]


def test_substitutions(tmp_path):
    dst = generate(tmp_path)
    assert "# DemoProject" in (dst / "README.md").read_text()
    assert ANSWERS["description"] in (dst / "README.md").read_text()
    assert "Copyright (c) Demo Author" in (dst / "LICENSE").read_text()


@pytest.mark.parametrize(
    "bindings,expected",
    [
        ("", "Not yet bound"),
        (
            "Exploration agent → ChatGPT; Architecture reviewer → Claude; Execution agent → Codex",
            "Exploration agent → ChatGPT",
        ),
    ],
)
def test_role_bindings_branches(tmp_path, bindings, expected):
    dst = generate(tmp_path, role_bindings=bindings)
    text = (dst / "decisions/development.md").read_text()
    assert expected in text
