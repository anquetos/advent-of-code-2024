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

# --- Part Two ---

text= "75,97,47,61,53"
test = [num for num in text.split(',')]

rules_t = "47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13"
rules = [r.split("|") for r in rules_t.split()]

print(rules)

combi = [list(combination) for combination in combinations(test, 2)]
print(combi)


for pair in combi:
    if pair in rules:
        print("ok")
    elif pair[::-1] in rules:
        print("reverse_ok")
        x = pair[0]
        y = pair[1]
        print("number to switch", pair[0], pair[1])
        

        x_idx = test.index(x)
        y_idx = test.index(y)

        test[x_idx] = y
        test[y_idx] = x
print(test)