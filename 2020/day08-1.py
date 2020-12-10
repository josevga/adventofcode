"""
https://adventofcode.com/2020/day/8
"""


from collections import namedtuple

Line = namedtuple("Line", ["instruction", "argument"])

filename = "day08-code.txt"
# filename = "day08-example.txt"
with open(filename, "r") as f:
    data = [line.rstrip("\n").split(" ") for line in f.readlines()]

print(f"Input {filename=} with {len(data)=}")

lines = [Line(instruction, int(argument))
         for instruction, argument in data]

# for i, line in enumerate(lines):
#     print(f"{i}: {line.instruction} ({line.argument})")

execs = set()
acc = 0
i = 0
while i not in execs:
    execs.add(i)
    print(f"{i=}", end=": ")
    if lines[i].instruction == "nop":
        i += 1
    elif lines[i].instruction == "acc":
        acc += lines[i].argument
        i += 1
    elif lines[i].instruction == "jmp":
        i += lines[i].argument
    print(f"{acc=}")

print(acc)
