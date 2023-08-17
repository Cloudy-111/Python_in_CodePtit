def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def isCoprime(a, b):
    return gcd(a, b) == 1


n, k = map(int, input().strip().split())
l = 10**(k-1)
r = 10**k
cnt = 0
for i in range(l, r):
    if isCoprime(i, n):
        print(i, end=' ')
        cnt += 1
        if (cnt % 10 == 0):
            print()
