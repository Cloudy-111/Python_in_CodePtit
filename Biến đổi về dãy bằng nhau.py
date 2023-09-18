n = int(input())
a = [int(x) for x in input().split()]
res = 10**9
for i in a:
    tmp = 0
    for j in a:
        tmp += abs(j - i)
    if res > tmp:
        res = tmp
        idx = i
print(res, idx)
