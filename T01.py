def powMod(n, k, Mod):
    if k == 0:
        return 1
    else:
        if k % 2 == 0:
            return powMod(n * n % Mod, k // 2, Mod) % Mod
        else:
            return n * powMod(n * n % Mod, k // 2, Mod) % Mod


def count_substrings(N, M, s):
    dp = [0] * (N + 1)
    dp[0] = 1  # Khởi tạo dp[0] là 1

    for i in range(1, N + 1):
        for j in range(i):
            if dp[j] != 0 and s[j:i] in s:
                dp[i] += dp[j]

    return dp[N]


t = int(input())
while t > 0:
    n, m = map(int, input().split())
    s = input()
    if n >= len(s):
        dis = n - len(s)
        count_substrings()
    else:
        print(0)
    t -= 1
