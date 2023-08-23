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


def rev(n):
    tmp = ''.join(reversed(str(n)))
    return int(tmp)


t = int(input())
cnt = 0
for line in sys.stdin:
    n = int(line)
    mark = [1]*n
    res = []
    for i in range(13, n+1):
        tmp = rev(i)
        if i != tmp:
            if prime[i] and prime[tmp] and tmp <= n and mark[i] and mark[tmp]:
                res = res+[i]
                res = res+[tmp]
                mark[i] = mark[tmp] = 0
    for i in res:
        print(i, end=' ')
    print()
    cnt += 1
    if cnt == t:
        break
