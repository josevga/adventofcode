"""
https://adventofcode.com/2020/day/4
"""

filename = "day01-expenses.txt"

with open(filename, "r") as f:
    data = [int(x) for x in f.readlines()]
print(f"Input {filename=} with lines: {len(data)}")

look_for = 2020
n1, n2 = data[0:2]
sums = {(n1 + n2): (n1, n2), }
nums = [n1, n2, ]
lines = 2
for x in data[2:]:
    lines += 1
    if (look_for - x) in sums.keys():
        a, b = sums[(look_for - x)]
        print(f"Found {a, b, x} in first {lines=}.")
        print(f"{a*b*x}")
        break
    for y in nums:
        if (x + y) < look_for:
            sums[x + y] = (x, y)
    nums.append(x)
else:
    print(f"Not found in {lines=}.")
