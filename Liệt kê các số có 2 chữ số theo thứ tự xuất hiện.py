n = input()
if len(n) % 2:
    n = n[:-1]
lst = []
while n != '':
    tmp = n[:2]
    if tmp not in lst:
        lst.append(tmp)
    n = n[2:]
for i in lst:
    print(i, end=' ')
