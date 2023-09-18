# vl, đề là ghi đủ n số trong các dòng tiếp theo chứ không phải là nhập n số trong 1 dòng
n = int(input())
arr = []
while 1:
    a = [int(x) for x in input().split()]
    arr += a
    if len(arr) == n:
        break
e = [x for x in arr if x % 2 == 0].sort(reverse=True)
o = [x for x in arr if x % 2 != 0].sort()
for i in a:
    if i % 2:
        print(o[-1])
        o.pop()
    else:
        print(e[-1])
        e.pop()
