"""
https://adventofcode.com/2020/day/4
"""

filename = "day01-expenses.txt"
with open(filename, "r") as f:
    data = [int(x) for x in f.readlines()]
print(f"Input {filename=} with lines: {len(data)}")

look_for = 2020
lines = 0
expenses = set()
for x in data:
    lines += 1
    if x in expenses:
        print(f"Found {look_for-x, x} in first {lines=}.")
        print(f"{x * (look_for-x)}")
        break
    expenses.add(look_for-x)
else:
    print(f"Not found in {lines=}.")
