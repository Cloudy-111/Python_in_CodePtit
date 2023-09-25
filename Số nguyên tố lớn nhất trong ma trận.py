def isPrime(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6
    return 1


res = 0
chk = 0
n, m = map(int, input().split())
mat = []
for i in range(n):
    a = [int(x) for x in input().split()]
    for j in a:
        if isPrime(j):
            res = max(res, j)
            chk = 1
    mat.append(a)

if res > 0:
    print(res)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == res:
                print(f'Vi tri [{i}][{j}]')
else:
    print('NOT FOUND')
