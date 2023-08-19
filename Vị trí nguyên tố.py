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


def isPrimeDigit(n):
    if n == '2' or n == '3' or n == '5' or n == '7':
        return 1
    return 0


def check(n):
    for i in range(len(n)):
        if isPrime(i) and isPrimeDigit(n[i]):
            continue
        elif isPrime(i) == 0 and isPrimeDigit(n[i]) == 0:
            continue
        else:
            return 0
    return 1


t = int(input())
while t > 0:
    n = input()
    if check(n):
        print('YES')
    else:
        print('NO')
    t -= 1
