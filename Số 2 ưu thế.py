from collections import deque


def check(s):
    cnt = 0
    for i in s:
        if i == '2':
            cnt += 1
    if cnt > len(s) / 2:
        return True
    return False


def solve(n):
    a = ['0', '1', '2']
    lst = deque(['1', '2'])
    cnt = 0
    while 1:
        tmp = lst.popleft()
        if check(tmp):
            print(tmp, end=' ')
            cnt += 1
        lst.append(tmp + a[0])
        lst.append(tmp + a[1])
        lst.append(tmp + a[2])
        if cnt == n:
            break


t = int(input())
while t > 0:
    n = int(input())
    solve(n)
    print()
    t -= 1
