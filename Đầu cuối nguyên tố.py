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


t = int(input())
while t > 0:
    n = input()
    a = int(n[:3])
    b = int(n[len(n)-3:])
    if isPrime(a) and isPrime(b):
        print('YES')
    else:
        print('NO')
    t -= 1
