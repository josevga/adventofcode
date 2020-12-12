"""
https://adventofcode.com/2020/day/9
"""

# filename = "day09-example.txt"
# lookfor = 127

filename = "day09-numbers.txt"
lookfor = 22477624

with open(filename, "r") as f:
    numbers = [int(line.rstrip("\n").strip(" ")) for line in f.readlines()]

print(f"Input {filename=} with {len(numbers)=}")

i = 0
j = 1
checksum = numbers[0] + numbers[1]
while not checksum == lookfor:
    if checksum < lookfor:
        j += 1
        checksum += numbers[j]
    else:
        while checksum > lookfor:
            checksum -= numbers[i]
            i += 1

print(f"Found: {i=}, {j=} >> {numbers[i:j+1]} >> {sum(numbers[i:j+1])=}")
print(f"{min(numbers[i:j+1])=} + {max(numbers[i:j+1])=} =", end=" ")
print(min(numbers[i:j+1]) + max(numbers[i:j+1]))
