import math
import sys
N = 10**6 + 1
prime = [1]*(N)
prime[0] = prime[1] = 0
i = 2
while i <= math.sqrt(N):
    if prime[i]:
        for j in range(i*i, N, i):
            prime[j] = 0
    i += 1

t = int(input())
cnt = 0
for line in sys.stdin:
    n = int(line)
    res = 0
    for i in range(n - 6):
        if prime[i] and prime[i+2] and prime[i+6]:
            res += 1
        if prime[i] and prime[i+4] and prime[i+6]:
            res += 1
    print(res)
    cnt += 1
    if cnt == t:
        break
