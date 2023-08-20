def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


t = int(input())
while t > 0:
    a = int(input())
    b = int(input())
    print(gcd(a, b))
    t -= 1
