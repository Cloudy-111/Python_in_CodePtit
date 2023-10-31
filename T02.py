for i in range(int(input())):
    n = int(input())
    a, b = [], []
    for j in range(n):
        x, y = [float(x) for x in input().split()]
        a.append(x)
        b.append(y)
    f, ans = [0] * n, 0
    for j in range(n):
        f[j] = 1
        for k in range(j):
            if a[j] > a[k] and b[j] < b[k] and f[j] <= f[k]:
                f[j] = f[k] + 1
        ans = max(ans, f[j])
    print(ans)
