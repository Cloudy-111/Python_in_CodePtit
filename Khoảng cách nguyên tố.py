import math
n, x = map(int, input().split())
prime = [0] * 10006
prime[0] = prime[1] = 1
i = 2
while i <= math.sqrt(10000) + 1:
    if prime[i] == 0:
        for j in range(i*i, 10001, i):
            prime[j] = 1
    i += 1
arr = []
for i in range(10000):
    if prime[i] == 0:
        arr += [i]
res = [x]
for i in range(n):
    res = res+[res[-1] + arr[i]]
for i in res:
    print(i, end=' ')
