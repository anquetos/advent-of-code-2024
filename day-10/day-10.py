from pathlib import Path


INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    input = f.readlines()

topographic_map = [list(map(int, line.strip())) for line in input]


# Get trailheads (0) coordinates
def get_trailheads_coordinates(
    topographic_map: list[list[int]], trailhead_number: int = 0
):
    trailheads = []
    for i, row in enumerate(topographic_map):
        if trailhead_number in row:
            trailheads.append((row.index(trailhead_number), i))
    return trailheads


trailheads = get_trailheads_coordinates(topographic_map)
print(f"Trailheads coordinates : {trailheads}\n")

# print([i for i in range(1, 10)])

# Look for 1 in all directions [(1, 0), (0, 1), (-1, 0), (0, -1)]
# If find 1, look for two in all directions

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

x, y = trailheads[2]
print("Test", x, y)

value = 0
for dx, dy in directions:
    nx, ny = (x + dx, y + dy)
    if topographic_map[ny][nx] == value + 1:
        pass
        # save coord

# --- Part One ---

print("--- Part One ---")
print(f"Result : {None}\n")
