def cal(n):
    res = 0
    if n % 2:
        for i in range(1, n+1, 2):
            res += 1/i
    else:
        for i in range(2, n+1, 2):
            res += 1/i
    return res


t = int(input())
while t > 0:
    n = int(input())
    print(f'{cal(n):.6f}')
    t -= 1
