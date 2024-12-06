from pathlib import Path
from itertools import combinations

INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    lines = f.readlines()

# Split input in two sperate lists
page_ordering_rules = [line.strip().split("|") for line in lines if "|" in line]
page_updates = [line.strip().split(",") for line in lines if "," in line]

# --- Part One ---


def check_page_update_validity(page_numbers: list[str]) -> bool:
    page_combinations = [
        list(combination) for combination in combinations(page_numbers, 2)
    ]

    if all(
        [
            page_combination in page_ordering_rules
            for page_combination in page_combinations
        ]
    ):
        return True
    return False


middle_page_sum = 0
for page_update in page_updates:
    if check_page_update_validity(page_update):
        update_length = len(page_update)
        middle_page_idx = int((update_length - 1) / 2)
        middle_page_number = int(page_update[middle_page_idx])
        middle_page_sum += middle_page_number

print("--- Part One ---")
print(f'Number of "XMAS" : {middle_page_sum}.\n')
