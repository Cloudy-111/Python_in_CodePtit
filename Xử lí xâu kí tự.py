a = input().lower().split()
b = input().lower().split()
Comb = set(a)
inter = set()
for i in b:
    Comb.add(i)
    if i in a:
        inter.add(i)
inter = sorted(inter)
Comb = sorted(Comb)
for i in Comb:
    print(i, end=' ')
print()
for i in inter:
    print(i, end=' ')
