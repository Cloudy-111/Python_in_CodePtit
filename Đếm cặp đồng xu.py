n = int(input())
Comb = [[1, 0, 0] for _ in range(n+1)]
Comb[1][0] = Comb[1][1] = 1
Comb[1][2] = 0
for i in range(2, n+1):
    for j in range(1, 3):
        Comb[i][j] = Comb[i-1][j-1]+Comb[i-1][j]
res = 0
grid = []
for i in range(n):
    tmp = input()
    res += Comb[tmp.count('C')][2]
    grid.append(tmp)
for j in range(n):
    cnt = 0
    for i in grid:
        if i[j] == 'C':
            cnt += 1
    if cnt:
        res += Comb[cnt][2]


print(res)
