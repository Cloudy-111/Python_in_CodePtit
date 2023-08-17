def check(n):
    for i in range(len(n)):
        if n[i] != '1' and n[i] != '2' and n[i] != '0':
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
