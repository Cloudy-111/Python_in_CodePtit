t = int(input())
while t > 0:
    n = int(input())
    s = ''
    div = 2
    while n > 1:
        cnt = 0
        while n % div == 0:
            cnt += 1
            n //= div
        if cnt != 0:
            s += ' * '+f'{div}^{cnt}'
        div += 1
    s = '1'+s
    print(s)
    t -= 1
