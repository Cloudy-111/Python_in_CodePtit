def hoanvi(n, i):
    for j in range(0, len(n)):
        if used[j] == 0:
            used[j] = 1
            a[i] = j
            if i == len(n)-1:
                for i in a:
                    print(n[i], end='')
                print()
            else:
                hoanvi(n, i+1)
            used[j] = 0


n = input()
used = [0 for _ in range(len(n))]
a = [0 for _ in range(len(n))]
hoanvi(n, 0)
