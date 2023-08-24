def check(n):
    for i in n:
        if i != '.':
            if i < '0' or i > '9':
                return 0
    a = n.split('.')
    if len(a) != 4:
        return 0
    for i in a:
        if int(i) > 255 or int(i) < 0:
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
