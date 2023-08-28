f = open('SOTAY.txt', 'r')
data = f.readlines()

arr = []
i = 0
while i < len(data):
    if data[i][:4] == 'Ngay':
        tmp = data[i]
    else:
        arr.append((data[i][:-1]+":", data[i+1][:-1], tmp[:-1]))
        i += 1
    i += 1
for i in arr:
    print(f'{i[0]} {i[1]} {i[2][5:]}')
f1 = open('DIENTHOAI.txt', 'w')
for i in arr:
    a, b, c = i[0], i[1], i[2][5:]
    f1.write("{} {} {}\n".format(a, b, c))
