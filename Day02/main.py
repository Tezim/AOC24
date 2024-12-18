
ascending = [1, 2, 3]
descending = [-1, -2, -3]

def read(filename):
    with open(filename, "r") as f:
        content = f.readlines()
    return content

def tolerance(lvl):
    for i in range(len(lvl)):
        tmp = lvl.copy()
        tmp.pop(i)
        if is_safe(tmp, False):
            return 1
    return 0

def is_safe(line, part):
    tmp = [int(line[i]) - int(line[i + 1]) for i in range(len(line) - 1)]
    check = set(tmp)
    asc = all(num in ascending for num in check)
    desc = all(num in descending for num in check)
    if not part:
        return 1 if asc or desc else 0
    else:
        return 1 if asc or desc else tolerance(line)

def part1(content):
    safe = 0
    for lvl in content:
        level = lvl.strip().split()
        safe += is_safe(level, False)
    return safe

def part2(content):
    safe = 0
    for lvl in content:
        level = lvl.strip().split()
        safe += is_safe(level, True)
    return safe

print(part1(read("input.txt")))
print(part2(read("input.txt")))