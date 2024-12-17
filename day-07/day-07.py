from pathlib import Path
from itertools import product, chain

# input = "190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20"

# input_lines = input.splitlines()

INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    input = f.readlines()


test_values = [int(line.split(": ")[0]) for line in input.splitlines()]
numbers_list = [
    [int(number) for number in line.split(": ")[1].split()] for line in input
]

# --- Part One ---


def generate_operators_combinations(operators: str, nb_combinations: int) -> list[list]:
    operators_product = product(operators, repeat=nb_combinations)
    combinations = [list(result) for result in operators_product]
    return combinations


def evaluate_left_to_right(equation: list) -> int:
    result = equation[0]
    for i in range(1, len(equation), 2):
        operator = equation[i]
        number = equation[i + 1]

        if operator == "+":
            result += number
        elif operator == "*":
            result *= number

    return result


equations_sum = 0

for test_value, numbers in zip(test_values, numbers_list):
    operators_combinations = generate_operators_combinations("+*", (len(numbers) - 1))

    for combination in operators_combinations:
        result = 0
        equation = list(chain.from_iterable(zip(numbers, combination)))
        equation.append(numbers[-1])
        result = evaluate_left_to_right(equation)
        if result == test_value:
            equations_sum += result
            break


print("--- Part One ---")
print(f"Sum of equations : {equations_sum}.\n")
