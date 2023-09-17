def change(n):
    res = 0
    for i in n:
        res += ord(i) - ord('0')
    return res


n = input()
cnt = 0
while len(n) > 1:
    n = str(change(n))
    cnt += 1
print(cnt)
