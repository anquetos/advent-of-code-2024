# --- Part One ---

# Read input file in a list
with open("/home/thomas/advent-of-code-2024/day-01/input.txt") as f:
    lines = f.readlines()

# Remove new line caracters
lines = [line.strip() for line in lines]

left_list = sorted([int(line[:5]) for line in lines])
right_list = sorted([int(line[-5:]) for line in lines])

distances = [abs(distance[0] - distance[1]) for distance in zip(left_list, right_list)]

total_distance = sum(distances)

print(f"Total distane between lists : {total_distance}.")