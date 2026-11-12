# Граф идеи (idea-graph)

Готовое решение «из коробки»: ведёт идею от сырой формулировки до передачи в разработку.
Этот пакет ставит всю систему одной командой. Сами части живут в отдельных репозиториях.

## Установка одной командой

Нужны Python 3.10+, git и хотя бы один агент: [Claude Code](https://claude.com/claude-code)
или [OpenCode](https://opencode.ai), установленный и вошедший в учётную запись.

```
python -m venv .venv
.venv\Scripts\python -m pip install git+https://github.com/senia-glitch/idea-graph.git
.venv\Scripts\ideagraph
```

На macOS и Linux вместо `.venv\Scripts\` — `.venv/bin/`.
Откроется страница `http://127.0.0.1:8765`. Оболочка работает, пока открыт терминал.

## Что ставится

| Репозиторий | Что делает | Нужна модель |
|---|---|---|
| [idea-graph-core](https://github.com/senia-glitch/idea-graph-core) | Ядро графа: карточки, связи, операции, журнал, отмена | нет |
| [idea-graph-shell](https://github.com/senia-glitch/idea-graph-shell) | Оболочка: холст, чат, вопросы с вариантами, настройки агентов | нет |
| [idea-graph-clarify](https://github.com/senia-glitch/idea-graph-clarify) | Уточнение идеи: один вопрос за ход | да |
| [idea-graph-check](https://github.com/senia-glitch/idea-graph-check) | Проверка графа: противоречия, дубли, пробелы | частично |
| [idea-graph-decider](https://github.com/senia-glitch/idea-graph-decider) | Решатель: отвечает на вопросы вместо вас | да |
| [idea-graph-composer](https://github.com/senia-glitch/idea-graph-composer) | Компоновщик: карта пакетов и прогон по ней | нет |
| [idea-graph-export](https://github.com/senia-glitch/idea-graph-export) | Выгрузка графа в `idea.md` | нет |
| [idea-graph-research](https://github.com/senia-glitch/idea-graph-research) | Исследование: конкуренты и факты из сети | да |
| [idea-graph-formalize](https://github.com/senia-glitch/idea-graph-formalize) | Формализация: решения → требования | да |
| idea-graph-handoff | Передача в pacage-studio-ide (репозиторий ещё не опубликован) | нет |

Пакет передачи пока ставится отдельно, после его публикации:
`pip install "idea-graph[handoff]"` (или `pip install git+https://github.com/senia-glitch/idea-graph-handoff.git`).

## Как пользоваться

1. На экране «Идеи» введите идею одной строкой и папку, где она будет жить. Граф хранится в её подпапке `.ideagraph`.
2. В «Настройках» нажмите «Подключить» у своего агента и выберите модель для каждого пакета.
3. На экране «Граф» выберите пакет «Уточнение идеи» и нажмите «Запустить».

Принятые при проектировании решения: [docs/ПРОЕКТ.md](docs/ПРОЕКТ.md).

## Обновление

```
.venv\Scripts\python -m pip install --upgrade --force-reinstall git+https://github.com/senia-glitch/idea-graph.git
```

## Тесты

```
pip install -e ".[test]"
python -m pytest
```
