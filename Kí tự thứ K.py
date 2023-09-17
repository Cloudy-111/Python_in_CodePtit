a = [0, 1]
for i in range(2, 27):
    a.append(a[-1] * 2 + 1)


def determine(n, k):
    if k == 0:
        return n
    elif n == 1:
        return 0
    else:
        if k < a[n] // 2:
            return determine(n - 1, k)
        else:
            return determine(n - 1, k - (a[n] + 1) / 2)


t = int(input())
while t > 0:
    n, k = map(int, input().split())
    print(chr(determine(n, k) + 65))
    t -= 1
