from pathlib import Path

INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    line = f.read()

stones = list(map(int, line.split()))


def has_even_number_of_digits(number: int) -> bool:
    if len(str(number)) % 2 == 0:
        return True
    return False


def split_number_in_two(number: int) -> list[int, int]:
    split_lenght = len(str(number)) // 2
    left_number = str(number)[:split_lenght]
    right_number = str(number)[-split_lenght:]

    return list(map(int, (left_number, right_number)))


def flatten_list(initial_list: list) -> list:
    flattened = []
    for item in initial_list:
        if isinstance(item, list):
            flattened.extend(item)
        else:
            flattened.append(item)
    return flattened


blinks_number = 25

for blink in range(1, blinks_number + 1):
    rearranged_stones = stones.copy()
    for idx, stone in enumerate(stones):
        if stone == 0:
            rearranged_stones[idx] = 1
        elif has_even_number_of_digits(stone):
            rearranged_stones[idx] = split_number_in_two(stone)
        else:
            rearranged_stones[idx] = stone * 2024

    stones = flatten_list(rearranged_stones)

number_of_stones = len(stones)

# --- Part One ---

print("--- Part One ---")
print(f"Number of stones after {blinks_number} blinks : {number_of_stones}\n")

# --- Part Two ---

print("--- Part Two ---")
print(f"P2 : {None}\n")
