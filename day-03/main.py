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

# --- Par Two ---

pattern = r"don't\(\)|do\(\)|mul\(\d+,\d+\)"

matches = re.findall(pattern, instructions)

do = True
mul_do_instructions = ""
for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False

    if do and "mul" in match:
        mul_do_instructions += match
    
m2 = find_mul(mul_do_instructions)
print(m2)
mul_sum2 = sum([(int(mul[0]) * int(mul[1])) for mul in m2])

print("--- Part Two ---")
print(f"Sum of do multiplications : {mul_sum2}.\n")