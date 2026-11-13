"""Мета-пакет «Граф идеи»: сам кода почти не содержит, его задача — потянуть за собой ядро, оболочку и этап «Проблема»."""

__version__ = "0.1.0"

# Имя репозитория (idea-graph-<имя>) -> имя пакета Python
PACKAGES = {
    "core": "idea-graph-core",
    "shell": "idea-graph-shell",
    "problem": "idea-graph-problem",
}
