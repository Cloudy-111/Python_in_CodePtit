def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


t = int(input())
while t > 0:
    a = int(input())
    b = int(''.join(reversed(str(a))))
    if gcd(a, b) == 1:
        print('YES')
    else:
        print('NO')
    t -= 1
