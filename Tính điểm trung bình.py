n = int(input())
a = [float(x) for x in input().split()]
# print(a)
a.sort()
l = min(a)
r = max(a)
res = sum(a)
while a[0] == l:
    res -= l
    a.remove(l)
while a[-1] == r:
    res -= r
    a.remove(r)
res /= len(a)
print(f'{res:.2f}')
