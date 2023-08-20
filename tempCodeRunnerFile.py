def loop(n, k, i):
    for j in range(a[i-1]+1, n-k+i+1):
        a[i] = j
        if i == k:
            for i in range(1, k+1):
                print(arr[a[i] - 1], end=' ')
            print()
        else:
            loop(n, k, i+1)


loop(n, k, 1)
