t = int(input())
while t > 0:
    n = int(input())
    b = [0]*1000001
    a = [int(x) for x in input().split()]
    m = 0
    a.sort()
    for i in range(len(a)):
        b[a[i]] += 1
        m = max(m, b[a[i]])
    if m > n/2:
        for i in range(len(a)):
            if b[a[i]] == m:
                print(a[i])
                break
    else:
        print('NO')
    t -= 1
