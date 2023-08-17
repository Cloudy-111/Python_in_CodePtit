def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def isCoprime(a, b):
    return gcd(a, b) == 1


l, r = map(int, input().strip().split())
r += 1
for i in range(l, r):
    for j in range(i+1, r):
        for k in range(j+1, r):
            if isCoprime(i, j) and isCoprime(k, j) and isCoprime(i, k):
                print(f'({i}, {j}, {k})')
