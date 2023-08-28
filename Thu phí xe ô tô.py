t = int(input())
a = []
day = []
while t > 0:
    n = input().split()
    a.append(n)
    day.append(n[-1])
    t -= 1
d = dict.fromkeys(day, 0)
for i in a:
    if i[-2] == 'IN':
        if i[1] == 'Xe_con':
            if i[2] == '5':
                d[i[-1]] += 10
            else:
                d[i[-1]] += 15
        elif i[1] == 'Xe_tai':
            d[i[-1]] += 20
        elif i[1] == 'Xe_khach':
            if i[2] == '29':
                d[i[-1]] += 50
            else:
                d[i[-1]] += 70
res = []
for k, v in d.items():
    res.append((k, v*1000))
res.sort()
for i in res:
    print(f'{i[0]}: {i[1]}')
