
"""
https://adventofcode.com/2020/day/2
"""

filename = "day02-passwords.txt"
with open(filename, "r") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]
print(f"Input {filename=} with lines: {len(lines)}")

valid = 0
for line in lines:
    policy, password = (x.strip() for x in line.split(":"))
    times, letter = policy.split(" ")
    min_t, max_t = (int(x) for x in times.split("-"))
    # print(min_t, max_t, letter, password)
    if min_t <= password.count(letter) <= max_t:
        valid += 1
print(f"{valid=}")
