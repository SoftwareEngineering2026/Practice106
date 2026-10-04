# Лабораторная 6. Continuous Integration

Автор: Скляров Константин Александрович, группа РИМ-150975к.
Проект: https://github.com/dyda5505-cloud/textlab-course. Workflow: .github/workflows/ci.yml.

Триггеры: pull_request в main, push в main и workflow_dispatch.
Job test-build последовательно устанавливает зависимости, собирает wheel/sdist,
запускает pytest с порогом покрытия 85%, собирает и запускает Compose,
затем проверяет реальное HTTP-взаимодействие до отдельного worker.
Дополнительные jobs проверяют мониторинг и Linux-команды в контейнере.

Успешный pipeline, вызванный PR: https://github.com/dyda5505-cloud/textlab-course/actions/runs/37193914473.
Завершены все три jobs: test-build, monitoring, linux-docker.
Скриншот: success.png.

Отдельный демонстрационный PR: https://github.com/dyda5505-cloud/textlab-course/pull/2.
В tests/test_intentional_failure.py добавлена проверка assert 1 == 2.
Результат: https://github.com/dyda5505-cloud/textlab-course/actions/runs/37194090166. Job test-build завершился с ошибкой на шаге Run tests,
последующие штатные шаги контейнерной проверки приложения были пропущены.
Скриншот: failure.png. Ошибочный тест не добавлен в основную ветку.

Вывод: CI автоматически проверяет изменения в pull request и отклоняет ветку,
если тесты не проходят. Ошибочный сценарий воспроизведён отдельно от рабочей версии.

После сохранения скриншота ошибочный тест удалён из демонстрационной ветки отдельным коммитом. PR №2 закрыт без слияния; исторический красный запуск доступен по указанной ссылке.
