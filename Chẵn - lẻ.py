def sum(n):
    res = 0
    for i in range(len(n)):
        res += int(n[i])
    if res % 10:
        return 0
    return 1


def check(n):
    for i in range(len(n)-1):
        if abs(int(n[i])-int(n[i+1])) != 2:
            return 0
    return 1


t = int(input())
while t > 0:
    n = input()
    if check(n) and sum(n):
        print('YES')
    else:
        print('NO')
    t -= 1
