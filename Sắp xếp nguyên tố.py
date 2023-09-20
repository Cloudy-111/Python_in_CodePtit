prime = [1 for _ in range(1001)]
prime[0] = prime[1] = 1
i = 2
for i in range(2, 1001):
    if prime[i] == 1:
        for j in range(i * i, 1001, i):
            prime[j] = 0
n = int(input())
a = [int(x) for x in input().split()]
isPrime = []
for i in a:
    if prime[i] == 1:
        isPrime.append(i)
isPrime.sort()
cnt = 0
for i in range(len(a)):
    if prime[a[i]] == 1:
        a[i] = isPrime[cnt]
        cnt += 1
for i in a:
    print(i, end=' ')
