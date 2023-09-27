def kt(k):
    for i in a:
        if i//k == i//(k+1):
            return 0
    return 1


n = int(input())
a = [int(x) for x in input().split()]
s, res = min(a), 0
for i in range(s, 0, -1):
    if kt(i):
        for j in range(n):
            res += a[j]//(i+1) + 1
        break
print(res)
