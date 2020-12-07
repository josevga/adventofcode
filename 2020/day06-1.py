"""
https://adventofcode.com/2020/day/6
"""

filename = "day06-answers.txt"
with open(filename, "r") as f:
    data = f.read()

lines = ["".join(line.split("\n")) for line in data.split("\n\n")]
yes = [set(line) for line in lines]
print(sum(len(item) for item in yes))
