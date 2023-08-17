def check(a, i):
    if i == 1001:
        return -1
    else:
        n = int(a)
        if n % 7 == 0:
            return n
        else:
            rev_n = int(''.join(reversed(a)))
            n = n+rev_n
            return check(str(n), i+1)


t = int(input())
while t > 0:
    a = input()
    print(check(a, 0))
    t -= 1
