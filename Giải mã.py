def decode(n):
    for i in range(0, len(n), 2):
        tmp = int(n[i+1])
        while tmp > 0:
            print(n[i], end='')
            tmp -= 1


t = int(input())
while (t > 0):
    n = input()
    decode(n)
    print()
    t -= 1
