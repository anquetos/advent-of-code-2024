test_map = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."

map = [list(line) for line in test_map.split()]

guard_orientations = [">", "<", "v", "^"]

def calculate_matrix_shape(matrix: list[list]) -> tuple[int, int]:
    """Calculate shape of a 2D matrix.

    Args:
        matrix (list[list]): the 2D matrix for which to calculate shape.

    Returns:
        tuple[int, int]: x length and y length.
    """

    return len(matrix), len(matrix[0])

map_shape = calculate_matrix_shape(map)
print("- map shape", map_shape)

def get_guard_position(map: list[list]) -> tuple[int, int]:
    for y, line in enumerate(map):
        for x, value in enumerate(line):
            if value in guard_orientations:
                print("- guard position : ", (x, y))
                return (x, y)

guard_position = get_guard_position(map)

def get_guard_direction(map: list[list], position: tuple[int, int]) -> tuple[int, int]:
    if map[position[1]][position[0]] == "^":
        direction = (0, 1)
    elif map[position[1]][position[0]] == ">":
        direction = (1, 0)
    elif map[position[1]][position[0]] == "v":
        direction = (0, -1)
    elif map[position[1]][position[0]] == "<":
        direction = (-1, 0)

    print("- guard direction : ", direction)

    return direction

get_guard_direction(map, guard_position)

               
def get_obstruction_positions(map: list[list]) -> list[tuple[int, int]]:
    positions_list = []
    for y, line in enumerate(map):
        for x, value in enumerate(line):
            if value == "#":
                positions_list.append((x, y))
    print("- obstacles positions : ", positions_list)
    return positions_list


in_map = True
obstructions = get_obstruction_positions(map)
while in_map:
    px, py = get_guard_position(map)
    dx, dy = get_guard_direction(map, (px, py))
    next_position = ((px + dx), (py + dy))
    print(next_position)

    if next_position in obstructions:
        dx, dy = dy, -dx
        next_position = ((px + dx), (py + dy))

    px, py = next_position[0], next_position[1]  

print(px, py)