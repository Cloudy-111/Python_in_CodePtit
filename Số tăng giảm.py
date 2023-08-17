def check(n):
    if len(n) < 3:
        return 0
    l = 0
    r = len(n)-1
    while l < len(n) and n[l+1] > n[l]:
        l += 1
    while r >= 0 and n[r-1] > n[r]:
        r -= 1
    return l == r


t = int(input())
while t > 0:
    n = input()
    if check(n):
        print('YES')
    else:
        print('NO')
    t -= 1
