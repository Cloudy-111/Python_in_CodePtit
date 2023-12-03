t = int(input())
while t > 0:
    n = int(input())
    lst = [int(x) for x in input().split()]
    res = 0
    i = 0
    while i < len(lst) - 1:
        if max(lst[i], lst[i + 1]) > 2 * min(lst[i], lst[i + 1]):
            res += 1
            tmp = 2 * min(lst[i], lst[i + 1])
            lst.insert(i + 1, tmp)
        else:
            i += 1
    print(res)
    t -= 1
