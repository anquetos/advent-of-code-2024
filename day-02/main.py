from pathlib import Path

INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    lines = f.readlines()

# Remove new line caracterss
lines = [line.strip() for line in lines]

reports = [[int(i) for i in line.split()] for line in lines]

# --- Part One ---

deltas = [[(report[i] - report[i+1]) for i in range(len(report)-1)] for report in reports]

def find_safe(delta: list):
    safe = False
    if (all(d < 0 for d in delta) or all(d > 0 for d in delta)) and all(0 < abs(d) <= 3 for d in delta):
        safe = True
    else:
        safe = False
    return safe

reports_status = [find_safe(delta) for delta in deltas]

nb_safe_reports = sum(reports_status)

print(nb_safe_reports)
