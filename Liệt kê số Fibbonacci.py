a = [0, 1, 1]
x1 = 1
x2 = 1
for i in range(3, 93):
    tmp = x1+x2
    a = a+[tmp]
    x2 = x1
    x1 = tmp
t = int(input())
while t > 0:
    l, r = map(int, input().strip().split())
    for i in range(l, r+1):
        print(a[i], end=' ')
    print()
    t -= 1
