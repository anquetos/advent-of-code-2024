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

print([i for i in range(1, 10)])

# Look for 1 in all directions [(1, 0), (0, 1), (-1, 0), (0, -1)]
# If find 1, look for two in all directions

def create_generator():
    start = (4, 2)
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for d in dir:
        coord = ((start[0] + d[0]), (start[1]) + d[1])
        if topographic_map[coord[0]][coord[1]] == 1:
            # print(coord)
            # print(topographic_map[coord[1]][coord[0]])
            yield coord

gen = create_generator()

for i in gen:
    print(i)

# --- Part One ---

print("--- Part One ---")
print(f"Result : {None}\n")
