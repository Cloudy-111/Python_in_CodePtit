n = int(input())
while (n > 0):
    ans = 0
    a = input()
    lst = list()
    s = ''
    for i in a:
        if i.isdigit():
            s += i
        elif s != '':
            ans = max(ans, int(s))
            s = ''
        else:
            pass
    print(ans)
    n -= 1
