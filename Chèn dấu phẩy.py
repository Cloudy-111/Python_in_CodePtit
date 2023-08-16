n = input().strip()
comma = ','
cnt = 0
res = ''
for i in range(len(n)-1, -1, -1):
    res = n[i]+res
    cnt += 1
    if cnt == 3:
        res = comma+res
        cnt = 0
print(res.strip(','))
