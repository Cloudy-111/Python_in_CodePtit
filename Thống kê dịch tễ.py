n, m = map(int, input().split())
mat = [[0]]*n
pat = []
for i in range(n):
    mat[i] = [int(x) for x in input().split()]
    for j in range(m):
        if mat[i][j] == -1:
            pat.append([i, j])

move = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
res = 0
while len(pat) > 0:
    p = pat[0]
    pat.pop(0)
    for i in move:
        x, y = i[0]+p[0], i[1]+p[1]
        if x >= 0 and x < n and y >= 0 and y < m:
            if mat[x][y] != 0:
                res += mat[x][y]
                mat[x][y] = 0
print(res)
