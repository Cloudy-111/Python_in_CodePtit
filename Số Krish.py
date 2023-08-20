a = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
t = int(input())
while t > 0:
    n = input()
    res = 0
    for i in range(len(n)):
        res += a[int(n[i])]
    if res == int(n):
        print('YES')
    else:
        print('NO')
    t -= 1
