"""
https://adventofcode.com/2020/day/3

Tobogan slope: Right 3, down 1.
"""

filename = "day03-trees.txt"
with open(filename, "r") as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

width = len(lines[0])
print(f"{width=}")

trees = 0
row, column = 0, 0
inc_row, inc_column = 1, 3
while row < (len(lines) - 1):
    row, column = row + inc_row, column + inc_column
    if lines[row][column % width] == "#":
        trees += 1
print(f"{trees=}")
