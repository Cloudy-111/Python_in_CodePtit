while True:
    s = input()
    if s == '-1':
        break
    else:
        l, r = map(int, s.split())
        n = int(input())
        m = max(n + 1, r + 1)
        mark = [0 for _ in range(m)]
        for i in range(2, n + 1):
            mark[i] = 1
        for i in range(2, n + 1):
            for j in range(i, m, i):
                mark[j] = 1
        res = 0
        for i in range(l, r + 1):
            if mark[i] == 0:
                res += 1
        print(res)
