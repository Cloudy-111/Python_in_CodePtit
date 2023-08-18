a = []
b = ['0', '2', '4', '6', '8']


def loop(x):
    k = list(x)
    k.reverse()
    # so chu so la chan nen chi can dao nguoc roi ghep vao la duoc
    k = int(x+''.join(k))
    a.append(k)
    if len(x) != 3:  # gioi han so chu so < 6
        for i in b:
            loop(x+i)  # de quy tiep tuc them chu so vao


for i in range(1, len(b)):  # duyet tu 1 de bo so 0 o dau
    loop(b[i])
a.sort()
t = int(input())
while t > 0:
    n = int(input())
    for i in range(len(a)):
        if a[i] < n:
            print(a[i], end=' ')
    print()
    t -= 1
