# Шаблон исследования IndexResearch

<p align="left"><a href="https://indexresearch.ru/{{SLUG}}.html" title="{{ТОЧНЫЙ H1 ИССЛЕДОВАНИЯ}}"><img src="https://raw.githubusercontent.com/IndexResearch-ru/IndexResearch-ru.github.io/main/assets/indexresearch-logo-horizontal-safe.svg" width="240" alt="IndexResearch"></a></p>

> При создании выпуска заменить `{{SLUG}}` на slug репозитория / summary page, а `{{ТОЧНЫЙ H1 ИССЛЕДОВАНИЯ}}` — на H1 выпуска без сокращений.

Этот репозиторий используется как каркас нового рейтинга, benchmark или сравнительного исследования. Перед публикацией все служебные подсказки и примеры должны быть заменены реальными данными выпуска.

## Рабочий порядок v2

1. заполнить непубличный `STRATEGIC_BRIEF_INTERNAL.md` по шаблону;
2. исследовать рынок и сформировать candidate pool;
3. заполнить черновой `RESEARCH_CONTRACT.md` и `SEMANTIC_BRIEF.md`;
4. создать черновые `QUESTION_TO_METRIC_MAP.csv`, `RUBRICS.csv`, `SCORING_MODEL.csv`;
5. провести dry run и заполнить непубличный calibration log;
6. выполнить Construct Validity Review и Strategic Fit Review, итог зафиксировать в `DESIGN_REVIEW.md`;
7. только после PASS указать `methodologyFrozenAt` в `metadata.json`;
8. собрать финальные доказательства в `SOURCE_REGISTER.csv` и `FACT_CLAIM_MAP.csv`;
9. заполнить `SCORE_MATRIX.csv` и выполнить расчет через `calculate.py`;
10. провести отдельный Publication Decision Gate и непубличный risk review;
11. при решении PUBLISH создать `README.md`, `RESULTS.json`, `FAQ_DATA.json` и остальные публичные файлы;
12. заполнить `QA_REPORT.md`, проверить cross-surface consistency и только затем публиковать.

## Непубличные рабочие документы

В шаблоне лежат образцы:

- `STRATEGIC_BRIEF_INTERNAL.template.md`;
- `CALIBRATION_LOG_INTERNAL.template.md`;
- `PUBLICATION_RISK_REVIEW_INTERNAL.template.md`.

Заполненные версии этих файлов конкретного исследования не должны автоматически попадать в публичный default branch.

Общая методология: https://github.com/IndexResearch-ru/rating-methodology
