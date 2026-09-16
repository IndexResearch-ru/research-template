from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODEL = ROOT / "SCORING_MODEL.csv"
MATRIX = ROOT / "SCORE_MATRIX.csv"
OUTPUT = ROOT / "RESULTS.json"


def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main():
    model = read_csv(MODEL)
    matrix = read_csv(MATRIX)

    weights = {row["metric_id"]: float(row["weight"]) for row in model if row.get("metric_id")}
    total_weight = sum(weights.values())
    if round(total_weight, 8) != 100:
        raise ValueError(f"Сумма весов должна быть 100, сейчас {total_weight}")

    scores = {}
    for row in matrix:
        participant = row.get("participant_id")
        metric_id = row.get("metric_id")
        if not participant or metric_id not in weights:
            continue
        raw = row.get("normalized_score", "")
        if raw == "":
            continue
        value = float(raw)
        if not 0 <= value <= 1:
            raise ValueError(f"normalized_score должен быть от 0 до 1: {row}")
        scores.setdefault(participant, 0.0)
        scores[participant] += value * weights[metric_id]

    ranking = [
        {"participant_id": p, "score": round(s, 4)}
        for p, s in sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    ]

    result = {"status": "DRAFT", "ranking": ranking}
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
