import tomllib
from pathlib import Path

from idea_graph import PACKAGES

ROOT = Path(__file__).resolve().parents[1]


def test_dependencies_point_to_github_repos():
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    deps = data["project"]["dependencies"]
    assert len(deps) == len(PACKAGES)
    for package, repo in PACKAGES.items():
        assert f"{package} @ git+https://github.com/senia-glitch/{repo}.git" in deps, package
