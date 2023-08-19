def isPrime(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while i*i < n:
        if (n % i == 0) or ((n % (i+2)) == 0):
            return 0
        i += 6
    return 1


def check(n):
    for i in range(len(n)):
        if (i % 2 and int(n[i]) % 2 == 0) or (i % 2 == 0 and int(n[i]) % 2):
            return 0
    return 1


t = int(input())
while t > 0:
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if isPrime(sum) and check(n):
        print('YES')
    else:
        print('NO')
    t -= 1
