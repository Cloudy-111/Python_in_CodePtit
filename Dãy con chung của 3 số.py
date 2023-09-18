t = int(input())
while t > 0:
    n, m, k = map(int, input().split())
    res = []
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    i, j, l, chk = 0, 0, 0, 0
    while i < n and j < m and l < k:
        if a[i] == b[j] == c[l]:
            chk = 1
            print(a[i], end=' ')
            i += 1
            j += 1
            l += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[l]:
            j += 1
        elif c[l] < a[i]:
            l += 1
    if chk == 0:
        print('NO')
    else:
        print()
    t -= 1
