t = int(input())
while t > 0:
    n = input()
    len_n = len(n)
    if n[len_n-2:] == '86':
        print('YES')
    else:
        print('NO')
    t -= 1
