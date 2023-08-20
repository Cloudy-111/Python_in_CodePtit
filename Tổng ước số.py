import sys


def ptich(n):
    sum = 0
    i = 2
    while n > 1:
        while n % i == 0:
            n //= i
            sum += i
        i += 1
    return sum


t = int(input())
i = 0
res = 0
for line in sys.stdin:
    n = int(line)
    res += ptich(n)
    i += 1
    if i == t:
        break
print(res)
