def check(n):
    for i in range(2, len(n)):
        if n[i] != n[i-2]:
            return 0
    return 1


t = int(input())
while t > 0:
    n = input()
    if check(n):
        print('YES')
    else:
        print('NO')
    t -= 1
