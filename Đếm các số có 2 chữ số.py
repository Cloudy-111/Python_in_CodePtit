n = input()
if len(n) % 2:
    n = n[:-1]
lst = dict()
while n != '':
    tmp = n[:2]
    if tmp in lst:
        lst[tmp] += 1
    else:
        lst[tmp] = 1
    n = n[2:]
for key, val in lst.items():
    print(key, val)
