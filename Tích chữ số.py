t = int(input())
while t > 0:
    n = input()
    sum = 1
    for i in range(len(n)):
        if n[i] != '0':
            sum *= int(n[i])
    print(sum)
    t -= 1
