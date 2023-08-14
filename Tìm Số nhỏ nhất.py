n = int(input())
while (n > 0):
    a = input()
    lst = list()
    s = ''
    for i in a:
        if i.isdigit():
            s += i
        elif s != '':
            lst += [int(s)]
            s = ''
        else:
            pass
    lst.sort()
    print(lst[0])
    n -= 1
