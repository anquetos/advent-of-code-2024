from pathlib import Path
from itertools import product, combinations

INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    input = f.readlines()

map_matrix = [list(line.strip()) for line in input]


def calculate_matrix_shape(matrix: list[list]) -> tuple[int, int]:
    """Calculate shape of a 2D matrix.

    Args:
        matrix (list[list]): the 2D matrix for which to calculate shape.

    Returns:
        tuple[int, int]: x length and y length.
    """

    return len(matrix), len(matrix[0])


def check_coordinates_validity(coord: tuple[int, int], shape: tuple[int, int]) -> bool:
    """Check if given coordinates are in or out a matrix based on its shape.

    Args:
        coord (tuple[int, int]): coordinates (x, y) to check.
        shape (tuple[int, int]): shape of the matrix.

    Returns:
        bool: validity of the coordinate.
    """

    max_x, max_y = shape[0] - 1, shape[1] - 1

    if 0 <= coord[0] <= max_x and 0 <= coord[1] <= max_y:
        return True

    return False


map_bounds = calculate_matrix_shape(map_matrix)

# --- Part One ---


def get_antennas_coordinates_and_frequencies(
    map: list[list],
) -> dict[tuple[int, int], str]:
    coordinates_dict = {}
    for y in range(len(map) - 1):
        for x, char in enumerate(map[y]):
            if char != ".":
                coordinates_dict[(x, y)] = char
    return coordinates_dict


all_antennas = get_antennas_coordinates_and_frequencies(map_matrix)


def remove_lone_antennas(
    coordinates: dict[tuple[int, int], str],
) -> dict[tuple[int, int], str]:
    frequencies = [values for values in coordinates.values()]
    for frequency in set(frequencies):
        if frequencies.count(frequency) == 1:
            for key, value in coordinates.items():
                if value == frequency:
                    del coordinates[key]

    return coordinates


antennas_without_lones = remove_lone_antennas(all_antennas)


def group_antennas_by_frequency(
    coordinates: dict[tuple[int, int], str],
) -> dict[str, list[tuple[int, int]]]:
    frequencies_dict = {}
    found_frequencies = set(coordinates.values())

    for frequency in found_frequencies:
        frequencies_dict[frequency] = list()
        for key, value in coordinates.items():
            if value == frequency:
                frequencies_dict[frequency].append(key)

    return frequencies_dict


frequencies_coordinates = group_antennas_by_frequency(antennas_without_lones)


def list_antennas_combinations(
    frequencies_coordinates: dict[str, list[tuple[int, int]]],
) -> list[list[tuple[int, int], tuple[int, int]]]:
    antennas_combinations = []

    for value in frequencies_coordinates.values():
        antennas_combinations.extend(
            [list(combination) for combination in combinations(value, 2)]
        )
    return antennas_combinations


antennas_combinations = list_antennas_combinations(frequencies_coordinates)


def calculate_antinodes_directions(antennas_combinations):
    antinodes_direction = []

    for antenna_combination in antennas_combinations:
        x_direction = antenna_combination[0][0] - antenna_combination[1][0]
        y_direction = antenna_combination[0][1] - antenna_combination[1][1]
        direction = list((x_direction, y_direction))
        antinodes_direction.append(direction)

    return antinodes_direction


antinodes_directions = calculate_antinodes_directions(antennas_combinations)

antinodes = set()
for i, antenna_combination in enumerate(antennas_combinations):
    for j, antenna in enumerate(antenna_combination):
        if j == 0:
            x_antinode = antenna[0] + antinodes_directions[i][0]
            y_antinode = antenna[1] + antinodes_directions[i][1]
        elif j == 1:
            x_antinode = antenna[0] - 1 * antinodes_directions[i][0]
            y_antinode = antenna[1] - 1 * antinodes_directions[i][1]

        if check_coordinates_validity((x_antinode, y_antinode), map_bounds):
            antinode = (x_antinode, y_antinode)
            antinodes.add(antinode)


print("--- Part One ---")
print(f"Unique antinode locations : {len(antinodes)}\n")
