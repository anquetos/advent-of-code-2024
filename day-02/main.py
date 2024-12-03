from pathlib import Path
import itertools

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

def find_safe(report: list) -> bool:
    delta = [(report[i] - report[i+1]) for i in range(len(report)-1)]
    if (all(d < 0 for d in delta) or all(d > 0 for d in delta)) and all(0 < abs(d) <= 3 for d in delta):
        return True
    else:
        return False

reports_status = [find_safe(report) for report in reports]

nb_safe_reports = sum(reports_status)

print("--- Part One ---")
print(f"Number of safe reports : {nb_safe_reports}.\n")

# --- Part Two ---

def find_safe_dampener(report: list) -> bool:
    if find_safe(report):
        return True

    modified_reports = [list(combination) for combination in itertools.combinations(report, len(report)-1)]

    if any(find_safe(modified_report) for modified_report in modified_reports):
        return True
    else:
        return False

reports_status_dampener = [find_safe_dampener(report) for report in reports]

nb_safe_reports_dampener = sum(reports_status_dampener)

print("--- Part Two ---")
print(f"Number of safe reports dampener : {nb_safe_reports_dampener}.\n")