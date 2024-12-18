from pathlib import Path


INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    input = f.readlines()

disk_map = input[0].strip()
disk_map = list(map(int, disk_map))

# disk_map = "2333133121414131402"
# disk_map = list(map(int, disk_map))
# print(disk_map)

# --- Part One ---

blocks = []
file_id = 0
for i, number in enumerate(disk_map):
    # File
    if i % 2 == 0:
        blocks.extend([file_id for _ in range(number)])
        file_id += 1
    # Free space
    else:
        blocks.extend(["." for _ in range(number)])


def get_first_space_block(blocks: list) -> int:
    for i, block in enumerate(blocks):
        if block == ".":
            return i


def check_remaining_gaps(blocks: list) -> bool:
    if "." in blocks:
        return True
    return False


remaining_gaps = True
while remaining_gaps:
    last_block = blocks.pop()
    remaining_gaps = check_remaining_gaps(blocks)
    if last_block != ".":
        first_space_idx = get_first_space_block(blocks)
        blocks[first_space_idx] = last_block


checksum = sum([i * n for i, n in enumerate(blocks)])

print("--- Part One ---")
print(f"Filesystem checksum : {checksum}\n")
