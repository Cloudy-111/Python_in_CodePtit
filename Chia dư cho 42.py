arr = []
x = 0
b = [0 for _ in range(42)]
while 1:
    arr = [int(x) for x in input().split()]
    x += len(arr)
    for i in range(len(arr)):
        b[arr[i] % 42] = 1
    if (x == 10):
        break
for i in range(len(arr)):
    arr[i] %= 10
res = 0
for i in b:
    if i:
        res += 1
print(res)
