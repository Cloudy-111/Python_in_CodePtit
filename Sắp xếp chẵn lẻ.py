n = int(input())
odd = []
even = []
arr = []
# vl, đề là ghi đủ n số trong các dòng tiếp theo chứ không phải là nhập n số trong 1 dòng
while 1:
    a = [int(x) for x in input().split()]
    arr += a
    if len(arr) == n:
        break
for i in arr:
    if i % 2:
        odd.append(i)
    else:
        even.append(i)
even.sort(reverse=True)
odd.sort()
for i in range(n):
    if arr[i] % 2:
        print(odd[-1], end=' ')
        odd.pop()
    else:
        print(even[-1], end=' ')
        even.pop()
