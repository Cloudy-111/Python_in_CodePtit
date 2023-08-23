import sys


def isPrime(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while i*i <= n:
        if (n % i) == 0 or (n % (i+2)) == 0:
            return 0
        i += 6
    return 1


def sum(n):
    res = 0
    while n >= 1:
        res += n % 10
        n //= 10
    return res


def digit(n):
    while n >= 1:
        b = n % 10
        if isPrime(b) == 0:
            return 0
        n //= 10
    return 1


def rev(n):
    tmp = ''.join(reversed(str(n)))
    return int(tmp)


t = int(input())
cnt = 0
for line in sys.stdin:
    n = int(line)
    if isPrime(n) and isPrime(rev(n)) and isPrime(sum(n)) and digit(n):
        print('Yes')
    else:
        print('No')
    cnt += 1
    if cnt == t:
        break
