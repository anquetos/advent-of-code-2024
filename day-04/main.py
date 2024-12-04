from pathlib import Path

INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    lines = f.readlines()

# Remove new line caracterss
input = [line.strip() for line in lines]

# Create matrix of characters
matrix = [list(chars) for chars in input]

# --- Part One ---


def calculate_matrix_shape(matrix: list[list]) -> tuple[int, int]:
    return len(matrix), len(matrix[0])


matrix_shape = calculate_matrix_shape(matrix)


def check_coordinates_validity(coord: tuple[int, int], shape: tuple[int, int]) -> bool:
    max_x, max_y = shape[0] - 1, shape[1] - 1

    if 0 <= coord[0] <= max_x and 0 <= coord[1] <= max_y:
        return True

    return False


def find_char_coordinates(char: str, matrix: list[list]) -> tuple[int, int]:
    char_coordinates = []
    for r, line in enumerate(matrix):
        for c, line_char in enumerate(line):
            if line_char == char:
                char_coordinates.append((r, c))
    return char_coordinates


def find_word(word: str, start: tuple[int, int], direction: tuple[int, int]):
    word_char_list = [char for char in word]

    for i in range(len(word)):
        coordinates = (start[0] + direction[0] * i, start[1] + direction[1] * i)
        if not check_coordinates_validity(coordinates, matrix_shape):
            return False
        elif word_char_list[i] != matrix[coordinates[0]][coordinates[1]]:
            return False
    return True


x_coordinates = find_char_coordinates("X", matrix)

directions = [(0, 1), (1, -1), (-1, 0), (-1, -1), (0, -1), (-1, 1), (1, 0), (1, 1)]

xmas_found = []
for x_coordinate in x_coordinates:
    for direction in directions:
        xmas_found.append(find_word("XMAS", x_coordinate, direction))

xmas_count = sum(xmas_found)

print("--- Part One ---")
print(f'Number of "XMAS" : {xmas_count}.\n')
