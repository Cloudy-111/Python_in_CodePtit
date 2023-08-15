def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def isPrime(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0

    i = 5
    while i*i < n:
        if n % i == 0 or n % (i+2) == 0:
            return 0
        i += 6
    return 1


t = int(input())
while (t > 0):
    a, b = map(int, input().split())
    x = gcd(a, b)
    res = 0
    while x > 0:
        res += x % 10
        x //= 10
    if isPrime(res):
        print('YES')
    else:
        print('NO')
    t -= 1
