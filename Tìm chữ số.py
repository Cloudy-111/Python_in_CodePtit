from math import *
import decimal


def powmod(a, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return powmod(a * a % 1000, n // 2) % 1000
        else:
            return a * powmod(a * a % 1000, n // 2) % 1000


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    a = 3 + sqrt(5)
    print(f'Case #{i}:', end=' ')
    res_str = str(int(powmod(a, n)))
    # print(res_str)
    while len(res_str) < 3:
        res_str = '0' + res_str
    print(res_str[-3:])
