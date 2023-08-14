n = int(input())
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
while (n > 0):
    b = int(input())
    X = input()
    res = ''
    dec = int(X, 2)
    while (dec > 0):
        tmp = dec % b
        res = str(lst[tmp])+res
        dec //= b
    print(res)
    n -= 1
