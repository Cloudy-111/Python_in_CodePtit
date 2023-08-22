n = int(input())
b = [0]*30002
a = [int(x) for x in input().split()]
for i in a:
    b[i] = 1
for i in range(1, len(b) + 1):
    if b[i] == 0:
        print(i)
        break
