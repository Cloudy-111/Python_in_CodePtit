def cmp(item):
    return ((501 - item[1], item[2]), item[0])


lst = []
t = int(input())
while t > 0:
    name = input()
    x1, x = map(int, input().split())
    tup = (name, x1, x)
    lst.append(tup)
    t -= 1
lst = sorted(lst, key=cmp)
for i in lst:
    print(i[0], i[1], i[2])
