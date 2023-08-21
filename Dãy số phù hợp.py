t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    chk = 0
    for i in range(n):
        if a[i] > b[i]:
            chk = 1
            break
    if chk:
        print('NO')
    else:
        print('YES')
    t -= 1
