def isPrime(n):
    if n < 2:
        return 0
    if n == a or n == 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return 0
        i += 6
    return 1


n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in a:
    if i not in b:
        b.append(i)
chk = 0
r = sum(b)
l = 0
for i in range(len(b)):
    l += b[i]
    r -= b[i]
    if isPrime(l) and isPrime(r):
        chk = 1
        print(i)
        break
if chk == 0:
    print('NOT FOUND')
