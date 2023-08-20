a = [1]


i1 = i2 = i3 = 0
while a[-1] < 10**18:
    next = min(a[i1]*2, a[i2]*3, a[i3]*5)
    a.append(next)

    if next == a[i1]*2:
        i1 += 1
    if next == a[i2]*3:
        i2 += 1
    if next == a[i3]*5:
        i3 += 1


dict = {1: 1}
cnt = 1
for i in a:
    dict[i] = cnt
    cnt += 1

t = int(input())
while t > 0:
    n = int(input())
    if n in dict:
        print(dict[n])
    else:
        print('Not in sequence')
    t -= 1
