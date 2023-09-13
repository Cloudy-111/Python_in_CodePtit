arr = []
mod = 10**9 + 7


def solve(k):
    i = 0
    while k > 0:
        b = k % 2
        if b == 1:
            arr.append(i)
        k //= 2
        i += 1


t = int(input())
while t > 0:
    n, k = map(int, input().split())
    arr.clear()
    solve(k)
    res = 0
    for i in arr:
        res = (res + (n ** i) % mod) % mod
    print(res)
    t -= 1
