def check(n):
    if len(n) == 1:
        return 0
    i = 0
    while i < len(n) - 1:
        if n[i] > n[i+1]:
            return 0
        i += 1
    return 1


f1 = open('DATA1.in', 'r')
f2 = open('DATA2.in', 'r')
data1 = f1.read().split()
data2 = f2.read().split()

a = set()
for i in data1:
    if check(i) == 1 and data2.count(i) != 0:
        a.add((int(i), data1.count(i), data2.count(i)))
if len(a) != 0:
    a = sorted(a)
    for i in a:
        print(i[0], i[1], i[2])
