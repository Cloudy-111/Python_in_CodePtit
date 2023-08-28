t = int(input())
while t > 0:
    n = input()
    arr = n.split()
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != arr[-1]:
            cnt += len(arr[i])+1
        else:
            cnt += len(arr[i])
        if cnt < 100:
            print(arr[i], end=' ')
    print()
    t -= 1
