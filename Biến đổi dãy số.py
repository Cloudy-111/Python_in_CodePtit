while 1:
    a = [int(x) for x in input().split()]
    s = set(a)
    if len(s) == 1 and next(iter(s), None) == 0:
        break
    cnt = 0
    # print(s)
    while len(s) != 1:
        tmp = a[0]
        for i in range(3):
            a[i] = abs(a[i]-a[i+1])
        a[3] = abs(a[3]-tmp)
        s = set(a)
        cnt += 1
        # print(a)
    print(cnt)
