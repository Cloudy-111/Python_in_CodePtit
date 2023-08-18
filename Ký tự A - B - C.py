def loop(s, n, a, b, c):  # a,b,c la so luong chu cai A, B, C
    if len(s) == n and a <= b and b <= c and a >= 1:
        print(s)
    if len(s) < n:
        loop(s+'A', n, a+1, b, c)
        loop(s+'B', n, a, b+1, c)
        loop(s+'C', n, a, b, c+1)


n = int(input())
for i in range(3, n+1):
    loop('', i, 0, 0, 0)
