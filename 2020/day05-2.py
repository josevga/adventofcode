"""
https://adventofcode.com/2020/day/5
"""

filename = "day05-seats.txt"
with open(filename, "r") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

print(f"Input {filename=} with {len(lines)=}")

changes = (("B", "1"), ("F", "0"), ("R", "1"), ("L", "0"))
seats = []
for line in lines:
    # print(f"{line=}", end=" : ")
    for oldvalue, newvalue in changes:
        line = line.replace(oldvalue, newvalue)
    row, column = int(line[:7], 2), int(line[7:10], 2)
    seatid = 8 * row + column
    seats.append(seatid)

min_seat = min(seats)
max_seat = max(seats)
print(f"{min_seat=}")
print(f"{max_seat=}")

for x in range(min_seat+1, max_seat):
    if x not in seats:
        print(x)
