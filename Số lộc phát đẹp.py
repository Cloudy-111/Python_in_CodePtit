a = []

s = input()
chk = 0
for i in s:
    if i == '6':
        a.append(i)
    else:
        if len(a) > 0:
            a[-1] += i
            if a[-1] != '68' and a[-1] != '688':
                chk = 1
        else:
            chk = 1
if chk == 1:
    print('NO')
else:
    print('YES')
