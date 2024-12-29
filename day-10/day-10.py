from pathlib import Path


INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    lines = f.readlines()

topographic_map = [list(map(int, line.strip())) for line in lines]


def check_coordinates_validity(
    matrix: list[list], coordinates: tuple[int, int]
) -> bool:
    max_x, max_y = len(matrix[0]) - 1, len(matrix) - 1
    x, y = coordinates

    if 0 <= x <= max_x and 0 <= y <= max_y:
        return True

    return False


def get_position_height(matrix: list[list], coordinates: tuple[int, int]) -> int:
    x, y = coordinates
    if check_coordinates_validity(matrix, (x, y)):
        return matrix[y][x]
    return None


def get_trailheads_coordinates(matrix: list[list[int]], height: int = 0):
    trailheads = []
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == height:
                trailheads.append((x, y))
    return trailheads


# Get trailheads
trailheads = get_trailheads_coordinates(topographic_map)
print(f"Trailheads coordinates : {trailheads}\n")


def get_valid_step_positions(
    matrix: list[list[int]],
    current_positions: list[tuple[int, int]],
    current_height: int,
) -> list[tuple[int, int]]:
    valid_step_positions = set()

    for current_position in current_positions:
        cx, cy = current_position

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            next_height = get_position_height(matrix, (nx, ny))

            if (
                check_coordinates_validity(matrix, (nx, ny))
                and next_height is not None
                and (next_height - current_height == 1)
            ):
                valid_step_positions.add((nx, ny))

    return list(valid_step_positions)


scores_sum = 0
for trailhead in trailheads:
    positions = [trailhead]

    for height in range(9):
        valid_steps = get_valid_step_positions(topographic_map, positions, height)
        positions = valid_steps

    scores_sum += len(positions)

# --- Part One ---

print("--- Part One ---")
print(f"Sum of the scores of all trailheads : {scores_sum}\n")
