import json
from pathlib import Path
import math

EXPECTED = {
    "P7": 104743,
    "P18": 1074,
    "P53": 4075,
    "P205": 0.5731441,
    "D1": 4818,
    "D2": 615.156,
    "FINAL": 115325
}

score = 0.0
weight = 1.0 / len(EXPECTED)

output_path = Path("/logs/agent/output.json")

if not output_path.exists():
    Path("/logs/verifier").mkdir(parents=True, exist_ok=True)
    Path("/logs/verifier/reward.txt").write_text("0")
    raise SystemExit("Missing output.json")

data = json.loads(output_path.read_text())

for p in data.get("problems", []):
    pid = p.get("problem_id")
    if pid not in EXPECTED:
        continue

    ans = p.get("final_answer")

    if isinstance(EXPECTED[pid], float):
        if math.isclose(ans, EXPECTED[pid], rel_tol=1e-4):
            score += weight
    else:
        if ans == EXPECTED[pid]:
            score += weight

Path("/logs/verifier").mkdir(parents=True, exist_ok=True)
Path("/logs/verifier/reward.txt").write_text(str(round(score,4)))
print(score)
