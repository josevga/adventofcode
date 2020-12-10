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


def run(start=0, acc=0, execs=None):
    "Run code from 'start' line with a given acc(umulator) and lines run"
    if not execs:
        execs = []
    end, error = False, False
    i = start
    jmps = []
    while i not in execs and not error and not end:
        if i == len(lines):
            end = True
            print(f"End! {acc=}")
        elif i > len(lines):
            error = True
            print(f"Error! Line {i=} does not exist. {acc=}")
        else:
            execs.append(i)
            # print(f"{i=}", end=": ")
            if lines[i].instruction == "nop":
                i += 1
            elif lines[i].instruction == "acc":
                acc += lines[i].argument
                i += 1
            elif lines[i].instruction == "jmp":
                jmps.append((i, acc))
                i += lines[i].argument
        # print(f"{acc=}")
    return end, error, acc, execs, jmps


end, error, acc, execs_loop, jmps = run()

print(f"{end=}\n{error=}\n{acc=}\n{execs_loop=}\n{jmps=}\n")

for idx, (jmp, acc_new) in enumerate(jmps):
    print(idx, jmp, end=": ")
    end, error, acc_new, _, _ = run(
        start=jmp+1, acc=acc_new, execs=execs_loop[0:jmp+1])
    print(f"{end=}, {error=}, {acc_new=}")
    if error:
        print("ERROR.")
    if end:
        print("END")
        print(f"line={idx}, {acc_new=}")
        break
