res = 0
chk = 0
n, m = map(int, input().split())
mat = []
for i in range(n):
    a = [int(x) for x in input().split()]
    for j in a:
        if str(j)[::-1] == str(j):
            res = max(res, j)
            chk = 1
    mat.append(a)

if res > 10:
    print(res)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == res:
                print(f'Vi tri [{i}][{j}]')
else:
    print('NOT FOUND')
