import math

prime = [1] * 1001
prime[0] = prime[1] = 0
i = 2
while i*i <= math.sqrt(1001):
    if prime[i] == 1:
        for j in range(i*i, 1001, i):
            prime[j] = 0
    i += 1

n, m = map(int, input().split())
matrix = []
for i in range(n):
    a = [int(x) for x in input().split()]
    for i in range(len(a)):
        if prime[a[i]]:
            a[i] = 1
        else:
            a[i] = 0
    matrix.append(a)
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
# print(m)
