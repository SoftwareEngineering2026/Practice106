# Лабораторная работа №106

## Continuous Integration (CI)

**Выполнил:** Олег Петрухин

## Цель

Настроить автоматическую проверку изменений при Pull Request в ветку `main`.

## Проект

Сделан небольшой Python-проект для анализа текста. Программа считает количество символов, слов и уникальных слов, а также определяет самые частые слова.

Для тестирования используется `pytest`.

## CI

В качестве CI используется **GitHub Actions**.

Workflow находится здесь:

```text
.github/workflows/ci.yml
```

В репозитории workflow должен находиться именно в корневом `.github/workflows`, иначе GitHub Actions его не запустит.

Pipeline запускается при Pull Request в `main` и выполняется по шагам:

```text
Checkout
↓
Python
↓
Установка зависимостей
↓
Build
↓
Tests
```

В workflow используются `actions/checkout@v6` и `actions/setup-python@v7`.

## Локальная проверка

Нужны Python 3.11+ и Git.

Проверка:

```bash
python --version
git --version
```

Создание окружения:

### Windows

```powershell
python -m venv .venv
.venv\\Scripts\\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Сборка:

```bash
python -m build
```

Тесты:

```bash
pytest -v
```

## Проверка CI

После создания Pull Request открыть в GitHub:

```text
Actions → CI
```

Для успешного запуска нужен зелёный статус. На скриншоте желательно показать название workflow, Pull Request и шаги установки зависимостей, сборки и тестов.

### Успешный запуск

Сначала оставить код без ошибок, отправить его в ветку PR и дождаться завершения workflow.

**Сюда вставить реальный скриншот успешного запуска GitHub Actions.**

## Проверка ошибки

Чтобы показать работу CI при проблеме, временно изменить в `src/text_analyzer/analyzer.py`:

```python
"words": len(words),
```

на:

```python
"words": len(words) + 1,
```

После этого:

```bash
git add ПетрухинОИ/
git commit -m "Проверка падения тестов"
git push
```

Новый запуск Actions должен завершиться ошибкой на шаге `Run tests`.

**Сюда вставить реальный скриншот failed pipeline.**

После скриншота вернуть правильный код:

```python
"words": len(words),
```

И выполнить:

```bash
git add ПетрухинОИ/
git commit -m "Исправление тестов"
git push
```

Финальная версия PR должна проходить тесты.

## Git и Pull Request

Если используется fork:

```bash
git clone https://github.com/ВАШ_ЛОГИН/Practice106.git
cd Practice106
git checkout -b practice106-petrukhin-oi
```

После копирования проекта:

```bash
git add ПетрухинОИ/
git add .github/workflows/ci.yml
git commit -m "Лабораторная работа №106"
git push -u origin practice106-petrukhin-oi
```

Pull Request создаётся из:

```text
ВАШ_FORK/Practice106
practice106-petrukhin-oi
```

в:

```text
SoftwareEngineering2026/Practice106
main
```

## Вывод

В ходе работы был настроен CI-процесс на GitHub Actions. При Pull Request workflow устанавливает зависимости, собирает проект и запускает тесты. Отдельно проверяется сценарий с ошибкой в коде: тесты перестают проходить, и pipeline завершается с ошибкой. После исправления кода проверка снова проходит успешно.

## Проверка требований

| Требование | Реализация |
|---|---|
| GitHub Actions | `.github/workflows/ci.yml` |
| Pull Request → `main` | `on: pull_request` |
| Установка зависимостей | `pip install -r requirements.txt` |
| Сборка | `python -m build` |
| Тесты | `pytest -v` |
| Ошибочный pipeline | временная ошибка в коде |
| Каталог сдачи | `ПетрухинОИ/` |
| README | `ПетрухинОИ/README.md` |
