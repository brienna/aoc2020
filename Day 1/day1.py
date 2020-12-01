# Read input
with open('./input.txt', 'r') as input_file:
    numbers = [int(line) for line in input_file.readlines()]

# Part 1
import itertools
for pair in itertools.combinations(numbers, r=2):
    if pair[0] + pair[1] == 2020:
        print(pair[0] * pair[1])

# Part 2
for pair in itertools.combinations(numbers, r=3):
    if pair[0] + pair[1] + pair[2] == 2020:
        print(pair[0] * pair[1] * pair[2])

