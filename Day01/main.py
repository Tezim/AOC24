
with open("input.txt", "r") as f:
    content = f.readlines()

l = []
r = []

for line in content:
    tmp = line.strip().split(' ')
    l.append(int(tmp[0]))
    r.append(int(tmp[-1]))

l.sort()
r.sort()

sum = 0
for i in range(len(content)):
    sum += abs(l[i] - r[i])

sum2 = 0
for num in l:
    sum2 += (num * r.count(num))
    
print(sum)
print(sum2)