t = int(input())
while t > 0:
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    l = a[:k]
    r = a[k:]
    res = r + l
    for i in res:
        print(i, end=' ')
    print()
    t -= 1
