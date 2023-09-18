t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    res = a[0]
    for i in range(1, n):
        res ^= a[i]
    print(res)
    t -= 1
