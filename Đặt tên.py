x = [0 for _ in range(50)]


def comb(n, k, i, a):
    for j in range(x[i - 1] + 1, n - k + i + 1):
        x[i] = j
        if i == k:
            for idx in range(1, k + 1):
                print(a[x[idx] - 1], end=' ')
            print()
        else:
            comb(n, k, i + 1, a)


n, k = map(int, input().split())
a = list(set([x for x in input().split()]))
a = sorted(a)
n = len(a)
comb(n, k, 1, a)
