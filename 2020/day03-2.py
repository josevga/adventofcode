"""
https://adventofcode.com/2020/day/3

Tobogan slopes:
- Right 1, down 1.
- Right 3, down 1. (This is the slope you already checked.)
- Right 5, down 1.
- Right 7, down 1.
- Right 1, down 2
"""

filename = "day03-trees.txt"
with open(filename, "r") as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

slopes = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))

width = len(lines[0])
print(f"{width=}")

product = 1
for inc_row, inc_column in slopes:
    trees = 0
    row, column = 0, 0
    while row < (len(lines) - 1):
        row, column = row + inc_row, column + inc_column
        if lines[row][column % width] == "#":
            trees += 1
    print(trees)
    product = product * trees
print(f"{product=}")
