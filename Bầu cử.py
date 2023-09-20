n, m = map(int, input().split())
a = [int(x) for x in input().split()]
d = dict()
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
l = d[0][1]
chk = 0
for i in d:
    if i[1] < l:
        chk = 1
        print(i[0])
        break
if chk == 0:
    print('NONE')
