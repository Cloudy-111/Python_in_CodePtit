n, m = map(int, input().split())
mat = []
for i in range(n):
    a = [int(x) for x in input().split()]
    mat.append(a)
if n > m:
    diff = [0]
    while n > m + len(diff):
        diff.append(diff[-1] + 2)
    for i in range(n):
        if i not in diff:
            for j in range(m):
                print(mat[i][j], end=' ')
            print()
else:
    diff = []
    if m > n:
        diff = [1]
    while m > n + len(diff):
        diff.append(diff[-1] + 2)
    for i in range(n):
        for j in range(m):
            if j not in diff:
                print(mat[i][j], end=' ')
        print()
