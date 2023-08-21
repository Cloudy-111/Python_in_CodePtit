t = int(input())
while t > 0:
    n = int(input())
    b = [0] * 1001
    m = 0
    while n > 0:
        x = int(input())
        b[x] += 1
        m = max(m, b[x])
        n -= 1
    for i in range(len(b)):
        if b[i] == m:
            print(i)
            break
    t -= 1
