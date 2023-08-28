f = open('DATA.in', 'r')
data = f.readlines()
arr = []
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
for i in data:
    if i != data[-1]:
        arr.append(i[:-1])
    else:
        arr.append(i)
t = arr[0]
for i in range(1, len(arr), 2):
    b = int(arr[i])
    x = arr[i+1]
    dec = int(x, 2)
    res = ''
    while dec > 0:
        tmp = dec % b
        res = str(lst[tmp])+res
        dec //= b
    print(res)
