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


n = int(input())
a = [int(x) for x in input().split()]
arr = list((tmp, 0) for tmp in a)
b = dict(arr)
for i in range(len(a)):
    b[a[i]] += 1
for i, j in b.items():
    if isPrime(i):
        print(i, j)
# print(b)
