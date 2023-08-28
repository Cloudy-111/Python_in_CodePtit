# cồng kềnh, nhưng mà chưa nghĩ ra cách khác tốt hơn
arr = []
t = int(input())
while t > 0:
    n = input().split()
    if len(n) == 6 or len(n) == 8:
        arr.append(1)
    else:
        arr.append(2)
    t -= 1
# print(arr)
ans = [arr[0]]
i = 1
while i < len(arr):
    if arr[i] == 1 and arr[i] != ans[-1]:
        ans.append(1)
    elif arr[i] == 2:
        j = i + 1
        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        tmp = (j-i)/4
        while tmp > 0:
            ans.append(2)
            tmp -= 1
        i = j-1
    i += 1
    # print(ans)
if ans[0] == 2:
    print(len(ans) - 1)
    for i in range(1, len(ans)):
        print(ans[i])
elif ans[0] == 1:
    print(len(ans))
    for i in ans:
        print(i)
