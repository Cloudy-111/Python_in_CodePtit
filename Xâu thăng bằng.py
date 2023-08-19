def check(n):
    rev_n = ''.join(reversed(n))
    for i in range(1, len(n)):
        if abs(ord(n[i])-ord(n[i-1])) != abs(ord(rev_n[i])-ord(rev_n[i-1])):
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
