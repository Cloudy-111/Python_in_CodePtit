n, k = map(int, input().strip().split())
arr = [int(x) for x in input().split()]
arr = sorted(list(set(arr)))
n = len(arr)
a = [0]*(k+1)


def loop(i):
    for j in range(a[i-1]+1, n-k+i+1):
        a[i] = j
        if i == k:
            for i in range(1, k+1):
                print(arr[a[i] - 1], end=' ')
            print()
        else:
            loop(i+1)
    # if i == k - 1:
    #     for j in range(1, k+1):
    #         print(arr[a[i]-1], end=' ')
    #         print()
    # for j in range(a[i]+1, n+1):
    #     a[i+1] = j
    #     loop(i+1)


loop(1)
