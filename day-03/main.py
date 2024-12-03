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

def find_mul(instructions: str) -> list[tuple]:

    # Set pattern for regex to extract mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Find matching patterns
    matching = re.findall(pattern, instructions)

    return matching

mul_instructions = find_mul(instructions)

mul_sum = sum([(int(mul[0]) * int(mul[1])) for mul in mul_instructions])

print("--- Part One ---")
print(f"Sum of multiplications : {mul_sum}.\n")