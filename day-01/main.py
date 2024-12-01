from pathlib import Path

INPUT_FILENAME = "input.txt"
p = Path(__file__).parent.resolve()
q = p / INPUT_FILENAME

# Read input file in a list
with open(q) as f:
    lines = f.readlines()

# Remove new line caracters
lines = [line.strip() for line in lines]

# Create the two lists
left_list = sorted([int(line[:5]) for line in lines])
right_list = sorted([int(line[-5:]) for line in lines])

# --- Part One ---

# Calculate/list distance between each item of the lists
distances = [abs(distance[0] - distance[1]) for distance in zip(left_list, right_list)]

# Calculate total distance
total_distance = sum(distances)

print("--- Part One ---")
print(f"Total distance between lists : {total_distance}.\n")

# --- Part Two ---

# Calculate/list similarity score between each item of the lists
similarity_scores = [number * right_list.count(number) for number in left_list]

# Calculate total similarity score
total_similarity_score = sum(similarity_scores)

print("--- Part Two ---")
print(f"Total similarity score between lists : {total_similarity_score}.\n")
