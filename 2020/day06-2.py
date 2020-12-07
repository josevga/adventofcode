"""
https://adventofcode.com/2020/day/6
"""

filename = "day06-answers.txt"
with open(filename, "r") as f:
    data = f.read()

groups = [line.split("\n") for line in data.split("\n\n")]

sums = 0
for group in groups:
    answers = [set(answer) for answer in group]
    everybodyyes = answers[0].intersection(*answers) 
    sums += len(everybodyyes)

print(f"{sums=}")
