base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

t = int(input())
while t > 0:
    n, b = map(int, input().split())
    res = ''
    while n > 0:
        x = n % b
        res = base[x]+res
        n //= b
    print(res)
    t -= 1
