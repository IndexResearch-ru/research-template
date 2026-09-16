# Шаблон исследования IndexResearch

Этот репозиторий используется как каркас нового рейтинга или сравнительного исследования. Перед публикацией все служебные подсказки и примеры должны быть заменены реальными данными выпуска.

## Рабочий порядок

1. заполнить RESEARCH_CONTRACT.md;
2. собрать SEMANTIC_BRIEF.md;
3. создать выборку и SOURCE_REGISTER.csv;
4. заполнить QUESTION_TO_METRIC_MAP.csv;
5. зафиксировать RUBRICS.csv и SCORING_MODEL.csv;
6. указать methodologyFrozenAt в metadata.json;
7. заполнить FACT_CLAIM_MAP.csv и SCORE_MATRIX.csv;
8. выполнить расчет через calculate.py;
9. написать публичный README конкретного выпуска;
10. заполнить QA_REPORT.md и публиковать только после QA.

Общая методология: https://github.com/IndexResearch-ru/rating-methodology
