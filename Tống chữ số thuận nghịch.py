def isPalin(n):
    if len(n) == 1:
        return 0
    i = 0
    while i < len(n)/2:
        if n[i] != n[len(n) - 1 - i]:
            return 0
        i += 1
    return 1


t = int(input())
while t > 0:
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if isPalin(str(sum)):
        print('YES')
    else:
        print('NO')
    t -= 1
