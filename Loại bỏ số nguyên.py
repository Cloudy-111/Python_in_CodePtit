f = open('DATA.in', 'r')
data = f.readlines()
data = [line.strip() for line in data]
res = []
for i in data:
    a = [x for x in i.split()]
    for j in a:
        if j.isdigit() == False:
            res.append(j)
        else:
            if int(j) > 2147483647:
                res.append(j)
res.sort()
for i in res:
    print(i, end=' ')
