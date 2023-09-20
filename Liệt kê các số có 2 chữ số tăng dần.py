n = input()
if len(n) % 2:
    n = n[:-1]
lst = set()
while n != '':
    lst.add(n[:2])
    n = n[2:]
lst = sorted(lst)
for i in lst:
    print(i, end=' ')
