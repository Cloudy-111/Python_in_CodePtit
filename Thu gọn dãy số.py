n = int(input())
arr = [int(x) for x in input().split()]
b = []
for i in arr:
    if len(b) == 0:
        b.append(i)
    else:
        if (b[-1]+i) % 2 == 0:
            b.pop()
        else:
            b.append(i)
print(len(b))
