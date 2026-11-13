"""Мета-пакет «Граф идеи»: сам кода почти не содержит, его задача — потянуть за собой все пакеты."""

__version__ = "0.1.0"

# Имя репозитория (idea-graph-<имя>) -> имя пакета Python
PACKAGES = {
    "core": "idea-graph-core",
    "shell": "idea-graph-shell",
    "problem": "idea-graph-problem",
    "clarify": "idea-graph-clarify",
    "check": "idea-graph-check",
    "decider": "idea-graph-decider",
    "composer": "idea-graph-composer",
    "export": "idea-graph-export",
    "research": "idea-graph-research",
    "formalize": "idea-graph-formalize",
    "handoff": "idea-graph-handoff",
}
