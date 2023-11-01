

def separate(n, i, s):
    for j in range(n, 0, -1):
        lst[i] = j
        if j == s:
            tmp = '('
            for k in range(1, i + 1):
                tmp += str(lst[k])
                if k != i:
                    tmp += ' '
            tmp += ')'
            res.append(tmp)
        elif j < s:
            separate(j, i + 1, s - j)


t = int(input())
while t > 0:
    n = int(input())
    lst = [0] * (n + 1)
    res = []
    separate(n, 1, n)
    print(len(res))
    for i in res:
        print(i, end=' ')
    print()
    t -= 1
