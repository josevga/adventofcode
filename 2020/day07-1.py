"""
https://adventofcode.com/2020/day/7
"""

filename = "day07-rules.txt"
# filename = "day07-examples.txt"
with open(filename, "r") as f:
    lines = [line.rstrip(".\n") for line in f.readlines()]

print(f"Input {filename=} with {len(lines)=}")

sep1 = " bags contain "
sep2 = ", "
my_bag = "shiny gold"

rules = {k: set([color.rstrip("bags").rstrip("bag").strip()
         for num, color in [item.split(" ", 1)
         for item in v.split(sep2)]])
         for k, v in (line.split(sep1) for line in lines)}


def check(color, my_color):
    # print(f"Cheking: {color} : {rules[color]}")
    if rules[color] == {'other'}:
        return False
    if my_color in rules[color]:
        return True
    return any(check(inside_color, my_color) for inside_color in rules[color])


print(sum(
    check(bag, my_bag) for bag in rules.keys()
))
