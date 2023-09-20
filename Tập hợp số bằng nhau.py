n, m = map(int, input().split())
a = sorted(set([int(x) for x in input().split()]))
b = sorted(set([int(x) for x in input().split()]))
chk = 0

if len(a) != len(b):
    print('NO')
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            chk = 1
            break
    if chk == 1:
        print('NO')
    else:
        print('YES')
