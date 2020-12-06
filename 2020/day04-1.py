"""
https://adventofcode.com/2020/day/4

The expected passport fields:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

filename = "day04-passports.txt"
with open(filename, "r") as f:
    data = f.read()
lines = [" ".join(line.split("\n")) for line in data.split("\n\n")]

required = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")  # , "cid", )
passports = []
valid = 0
for line in lines:
    items = [item.split(":") for item in line.split(" ")]
    passport = {k: v for k, v in items}
    passports.append(passport)
    if sum((field in passport.keys() for field in required)) > 6:
        valid += 1

print(f"{len(lines)=}")
print(f"{valid=}")
