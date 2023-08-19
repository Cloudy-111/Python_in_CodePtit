import math

t = int(input())
while t > 0:
    n = input()
    sum = 0
    mul = 1
    cnt = 0
    for i in range(len(n)):
        if i % 2:
            sum += int(n[i])
        else:
            if n[i] != '0':
                mul *= int(n[i])
            else:
                cnt += 1
    if cnt == math.ceil(len(n)/2):
        mul = 0
    print(mul, sum)
    t -= 1
