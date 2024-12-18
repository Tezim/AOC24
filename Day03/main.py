import re

def read(filename):
    with open(filename, "r") as f:
        content = f.read()
    return content

def part1(eq):
    result = 0
    patt =  r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(patt, eq)
    for equation in matches:
        x, y = int(equation[0]), int(equation[1])
        result+= x * y
    return result

def part2(eq):
    result = 0
    patt = r"(mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\))"
    matches = re.findall(patt,eq)
    enabled = True
    for equation in matches:
        if equation[0] == "don't()":
            enabled = False
        elif equation[0] == "do()":
            enabled = True
            continue
        if enabled:
            x, y = int(equation[1]), int(equation[2])
            result+= x * y
    return result

print(part1(read("input.txt")))
print(part2(read("input.txt")))