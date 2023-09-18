while True:
    n = int(input())
    if n == 0:
        break
    x = int(input())
    a = b = x
    n -= 1
    while n > 0:
        x = int(input())
        a = min(a, x)
        b = max(b, x)
        n -= 1
    if a == b:
        print('BANG NHAU')
    else:
        print(a, b)
