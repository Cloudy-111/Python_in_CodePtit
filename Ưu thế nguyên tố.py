def isPrime(n):
    if n < 2:
        return 0
    elif n == 2 or n == 3:
        return 1
    elif n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while i*i <= n:
        if (n % i) == 0 or (n % (i+2)) == 0:
            return 0
        i += 6
    return 1


prime = '2357'


def check(n):
    if isPrime(len(n)) == 0:
        return 0
    cnt = 0
    for i in range(len(n)):
        if n[i] in prime:
            cnt += 1
    return cnt > len(n)-cnt


t = int(input())
while t > 0:
    n = input()
    if check(n):
        print('YES')
    else:
        print('NO')
    t -= 1
