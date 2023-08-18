def isDivisible3(n):
    return n % 3 == 0


t = int(input())
while t > 0:
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if isDivisible3(sum):
        print('YES')
    else:
        print('NO')
    t -= 1
