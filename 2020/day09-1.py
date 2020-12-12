"""
https://adventofcode.com/2020/day/9
"""


from itertools import combinations

filename = "day09-numbers.txt"
# filename = "day09-example.txt"
preamble = 25
with open(filename, "r") as f:
    numbers = [int(line.rstrip("\n").strip(" ")) for line in f.readlines()]

print(f"Input {filename=} with {len(numbers)=}")

print(f"for i in range({preamble=}, {len(numbers)=})")
for i in range(preamble, len(numbers)):
    print(f"Looking sums for {i=}: {numbers[i]=}")
    candidates = combinations(numbers[i-preamble:i], 2)
    for a, b in candidates:
        if (a + b) == numbers[i]:
            print(f"  {a} + {b}")
            break
    else:
        print(f"  Not sum found for {numbers[i]=}.")
        break
