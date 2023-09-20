n, m = map(int, input().split())
a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])
inter = []
b_a = []
a_b = []
for i in a:
    if i in b:
        inter.append(i)
    else:
        a_b.append(i)
for i in b:
    if i not in a:
        b_a.append(i)

for i in sorted(inter):
    print(i, end=' ')
print()
for i in sorted(a_b):
    print(i, end=' ')
print()
for i in sorted(b_a):
    print(i, end=' ')
