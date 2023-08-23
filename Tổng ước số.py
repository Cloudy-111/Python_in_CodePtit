import math
prime = [1]*2000001
prime[0] = prime[1] = 0
i = 2
while i <= math.sqrt(2000001):
    if prime[i] == 1:
        for j in range(i*i, 2000001, i):
            if prime[j] == 1:
                prime[j] = i
    i += 1
for j in range(2, 2000001):
    if prime[j] == 1:
        prime[j] = j
t = int(input())
res = 0
while t > 0:
    n = int(input())
    while n > 1:
        res += prime[n]
        n //= prime[n]
    t -= 1
print(res)
