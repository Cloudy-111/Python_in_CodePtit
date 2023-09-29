from math import *

t = int(input())
while t > 0:
    n, m, l = map(int, input().split())
    mat = []
    for i in range(n):
        a = [int(x) for x in input().split()]
        mat.append(a)
    preMat = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    # dùng mảng cộng dồn để tính từng khối của mảng
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            preMat[i][j] = preMat[i - 1][j] + preMat[i][j - 1] - \
                preMat[i - 1][j - 1] + mat[i - 1][j - 1]
    # print(preMat)
    for i in range(1, n + 2 - l):
        for j in range(1, m + 2 - l):
            print(floor((preMat[i + l - 1][j + l - 1] - preMat[i - 1][j + l - 1] -
                  preMat[i + l - 1][j - 1] + preMat[i - 1][j - 1]) / (l ** 2)), end=' ')
        print()
    t -= 1
"""
4 4 3
2 1 0 0
3 2 1 1
4 5 2 1
2 2 9 0
3 3 3
1 2 3
4 5 6
7 8 9
"""
