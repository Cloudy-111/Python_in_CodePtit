t = int(input())
while t > 0:
    n, m = map(int, input().split())
    mt = []
    for i in range(n):
        a = [int(x) for x in input().split()]
        mt.append(a)
    dis_mt = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(mt[j][i])
        dis_mt.append(a)
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(m):
                s += mt[i][k] * dis_mt[k][j]
            print(s, end=' ')
        print()
    t -= 1
