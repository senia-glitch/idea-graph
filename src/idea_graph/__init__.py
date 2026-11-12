"""Мета-пакет «Граф идеи»: сам кода почти не содержит, его задача — потянуть за собой все пакеты."""

__version__ = "0.1.0"

# Имя репозитория (idea-graph-<имя>) -> имя пакета Python
PACKAGES = {
    "core": "ideagraph-core",
    "shell": "ideagraph-shell",
    "clarify": "ideagraph-clarify",
    "check": "ideagraph-check",
    "decider": "ideagraph-decider",
    "composer": "ideagraph-composer",
    "export": "ideagraph-export",
    "research": "ideagraph-research",
    "formalize": "ideagraph-formalize",
    "handoff": "ideagraph-handoff",
}
