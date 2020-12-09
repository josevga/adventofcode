"""
https://adventofcode.com/2020/day/7
"""

filename = "day07-rules.txt"
# filename = "day07-examples2.txt"
with open(filename, "r") as f:
    lines = [line.rstrip(".\n") for line in f.readlines()]

print(f"Input {filename=} with {len(lines)=}")

sep1 = " bags contain "
sep2 = ", "
my_bag = "shiny gold"

rules = {k: [[color.rstrip("bags").rstrip("bag").strip(),
              int(num) if num != "no" else 0]
         for num, color in [item.split(" ", 1)
         for item in v.split(sep2)]]
         for k, v in (line.split(sep1) for line in lines)}

# print(rules)


def total_bags(color):
    print(f"Cheking: {color} : {rules[color]}")
    if len(rules[color]) == 1 and rules[color][0][1] == 0:
        return 0
    sum_bags = sum(item[1] for item in rules[color])
    print(sum_bags)
    return sum_bags + sum(item[1] * total_bags(item[0])
                          for item in rules[color])


print(total_bags(my_bag))
