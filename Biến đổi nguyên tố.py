a, b = [1 for _ in range(10001)], []
a[0] = a[1] = 0
i = 2
for i in range(2, 10001):
    if a[i] == 1:
        for j in range(i * i, 10001, i):
            a[j] = 0
        b.append(i)
        i += 1

n = int(input())
lst = [int(x) for x in input().split()]
res = 0
for i in lst:
    tmp = 10**9
    for j in b:
        tmp = min(tmp, abs(j - i))
    res = max(res, tmp)
print(res)
