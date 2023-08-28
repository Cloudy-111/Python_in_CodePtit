t = int(input())
while t > 0:
    n, m = map(int, input().split())
    arr = [int(x) for x in input().split()]
    x = max(arr)
    arr.insert(arr.index(x), m)
    arr1 = []
    arr2 = []
    for i in arr:
        if i < 0:
            arr1.append(i)
        else:
            arr2.append(i)
    res = arr1+arr2
    for i in res:
        print(i, end=' ')
    print()
    t -= 1
