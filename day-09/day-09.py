from pathlib import Path
import pprint


INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    input = f.readlines()

disk_map = input[0].strip()

# --- Part One ---

blocks = ""
file_id = 0
for i, digit in enumerate(disk_map):
  
# File
    if i % 2 == 0:
        # blocks.append(str(file_id) * int(digit))
        blocks += str(file_id) * int(digit)
        file_id += 1
# Free space
    else:
        blocks += "." * int(digit)

blocks_list = list(blocks)

def check_gaps_between_file_blocks(blocks: list) -> bool:
    nb_space_blocks = blocks.count(".")
    if blocks[-nb_space_blocks:].count(".") != nb_space_blocks:
        return True
    return False

def get_last_file_block(blocks: list) -> tuple[int, str]:
    blocks_length = len(blocks)
    for i, block in enumerate(blocks[::-1]):
        if block != ".":
            idx =  blocks_length -1 - i
    return idx, block

def get_first_space_block(blocks: list) -> int:
  for i, block in enumerate(blocks):
    if block == ".":
      return i
    
remaining_gaps = True
while remaining_gaps:
    space_index = get_first_space_block(blocks_list)
    file_index, file_id = get_last_file_block(blocks_list)
    blocks_list[space_index] = file_id
    blocks_list[file_index] = "."
    
    remaining_gaps = check_gaps_between_file_blocks(blocks_list)



print("--- Part One ---")
print(f"Unique antinode locations : {0}\n")
