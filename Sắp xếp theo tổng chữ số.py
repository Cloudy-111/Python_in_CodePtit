def sum(a):
    res = 0
    while a:
        res += a % 10
        a //= 10
    return res


def comp(x):
    return (sum(x), x)


t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, key=comp)
    for i in a:
        print(i, end=' ')
    print()
    t -= 1
