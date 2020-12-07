import re

"""
https://adventofcode.com/2020/day/4

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

filename = "day04-passports.txt"
with open(filename, "r") as f:
    data = f.read()
lines = [" ".join(line.split("\n")) for line in data.split("\n\n")]


def check_byr(value):
    "byr (Birth Year) - four digits; at least 1920 and at most 2002."
    pattern = r"^[0-9]{4}$"
    if re.match(pattern, value):
        if 1920 <= int(value) <= 2002:
            return True
    return False


def check_iyr(value):
    "iyr (Issue Year) - four digits; at least 2010 and at most 2020."
    pattern = r"^[0-9]{4}$"
    if re.match(pattern, value):
        if 2010 <= int(value) <= 2020:
            return True
    return False


def check_eyr(value):
    "eyr (Expiration Year) - four digits; at least 2020 and at most 2030."
    pattern = r"^[0-9]{4}$"
    if re.match(pattern, value):
        if 2020 <= int(value) <= 2030:
            return True
    return False


def check_hgt(value):
    """
    hgt (Height) - a number followed by either cm or in:
    - If cm, the number must be at least 150 and at most 193.
    - If in, the number must be at least 59 and at most 76.
    """
    pattern = r"^([0-9]{2,3})(cm|in)$"
    match = re.match(pattern, value)
    if match:
        num, unit = match.groups()
        if unit == "cm" and 150 <= int(num) <= 193:
            return True
        if unit == "in" and 59 <= int(num) <= 76:
            return True
    return False


def check_hcl(value):
    "hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."
    pattern = r"^\#[0-9a-f]{6}$"
    if re.match(pattern, value):
        return True
    return False


def check_ecl(value):
    "ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."
    colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return value in colors


def check_pid(value):
    "pid (Passport ID) - a nine-digit number, including leading zeroes."
    pattern = r"^[0-9]{9}$"
    return re.match(pattern, value)


required = {
    "byr": check_byr, "iyr": check_iyr, "eyr": check_eyr, "hgt": check_hgt,
    "hcl": check_hcl, "ecl": check_ecl, "pid": check_pid,
}
passports = []
valid = 0
for line in lines:
    items = [item.split(":") for item in line.split(" ")]
    passport = {k: v for k, v in items}
    passports.append(passport)
    print(passport)
    if sum((field in passport.keys() for field in required.keys())) > 6:
        if all(function(passport[key]) for key, function in required.items()):
            valid += 1
            print("OK!")
print(f"{len(lines)=}")
print(f"{valid=}")
