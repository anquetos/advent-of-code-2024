from pathlib import Path
import re

INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    lines = f.readlines()

instructions = str(lines)

# --- Part One ---


def calculate_mul_sum(instructions: str) -> int:
    # Set pattern to look for : "mul(X,Y)"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Find matching pattern and extract X and Y in a list of tuples
    matches = re.findall(pattern, instructions)

    # Multiply X and Y for each tuple
    multiplications = [int(x) * int(y) for x, y in matches]

    # Add up all of the results of the multiplications
    result = sum(multiplications)

    return result


mul_sum = calculate_mul_sum(instructions)

print("--- Part One ---")
print(f"Sum of multiplications : {mul_sum}.\n")

# --- Par Two ---


def calculate_mul_do_sum(instructions: str) -> int:
    # Set variables
    do = True
    result = 0

    # Set pattern to look for : "don't", "do()" and "mul(X,Y)"
    pattern = r"don't\(\)|do\(\)|mul\(\d+,\d+\)"

    # Find ans extract matching patterns in a list
    matches = re.findall(pattern, instructions)

    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False

        if do and "mul" in match:
            x, y = map(int, re.findall(r"\d+", match))
            multiplication = x * y

            result += multiplication

    return result


mul_do_sum = calculate_mul_do_sum(instructions)

print("--- Part Two ---")
print(f"Sum of do multiplications : {mul_do_sum}.\n")
