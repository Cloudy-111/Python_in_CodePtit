t = int(input())
while t > 0:
    n = int(input())
    lst = []
    while n > 0:
        a, b = map(int, input().split())
        tup = (a, b)
        lst.append(tup)
        n -= 1

    lst = sorted(lst, key=lambda x: (x[1], x[0]))
    res = []
    for i in lst:
        if (len(res)) == 0:
            res.append(i)
        else:
            if i[0] >= res[-1][1]:
                res.append(i)
    print(len(res))
    t -= 1

# 1
# 10
# 39 55
# 37 74
# 0 1
# 19 25
# 65 76
# 51 52
# 19 21
# 5 94
# 46 65
# 32 40
