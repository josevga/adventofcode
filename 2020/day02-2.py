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
    positions, letter = policy.split(" ")
    pos1, pos2 = (int(x) for x in positions.split("-"))
    find1 = password[pos1 - 1] == letter if pos1 <= len(password) else False
    find2 = password[pos2 - 1] == letter if pos2 <= len(password) else False
    if (find1 and not find2) or (not find1 and find2):
        valid += 1
print(f"{valid=}")
