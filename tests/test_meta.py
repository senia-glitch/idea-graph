import tomllib
from pathlib import Path

from idea_graph import PACKAGES

ROOT = Path(__file__).resolve().parents[1]


def test_dependencies_point_to_github_repos():
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    deps = data["project"]["dependencies"] + data["project"]["optional-dependencies"]["handoff"]
    for key, name in PACKAGES.items():
        expected = f"{name} @ git+https://github.com/senia-glitch/idea-graph-{key}.git"
        assert expected in deps, key
