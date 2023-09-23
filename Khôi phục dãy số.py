n = int(input())
b = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    b.append(tmp)
a = []

sum = 0
for i in range(n):
    for j in range(i + 1, n):
        sum += b[i][j]
sum //= (n - 1)
tmp = 0
for i in range(1, n):
    tmp += b[0][i]
if n > 2:
    a.append((tmp - sum) // (n - 2))
    for i in range(1, n):
        a.append(b[0][i] - a[0])
else:
    a.append(sum // 2)
    a.append(sum - a[0])
for i in a:
    print(i, end=' ')
