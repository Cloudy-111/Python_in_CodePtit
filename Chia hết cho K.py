a, k, n = map(int, input().split())
res = 0
if a < k:
    x = k-a
    while a+x <= n:
        print(x, end=' ')
        x += k
        res = 1
else:
    x = round(a/k)
    y = k*x-a
    if y <= 0:
        y += k
    while a+y <= n:
        print(y, end=' ')
        y += k
        res = 1
if res == 0:
    print(-1)
