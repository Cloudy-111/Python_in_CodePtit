res = -1
chk = 0
l, r = 10001, 0
n, m = map(int, input().split())
mat = []
for i in range(n):
    a = [int(x) for x in input().split()]
    for j in a:
        l = min(l, j)
        r = max(r, j)
    mat.append(a)

lst = []
res = r - l
for i in range(n):
    for j in range(m):
        if mat[i][j] == res:
            lst.append(f'Vi tri [{i}][{j}]')
if len(lst) > 0:
    print(res)
    for i in lst:
        print(i)
else:
    print('NOT FOUND')
