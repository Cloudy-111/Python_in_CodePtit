import math


def count(arr, k):
    n = len(arr)
    res = n + 1
    for i in range(n):
        tmp = arr[i]
        for j in range(i, n):
            tmp = math.gcd(tmp, arr[j])
            if tmp == k:
                res = min(res, j - i + 1)
                break
            if tmp < k:
                break
    if res == len(arr) + 1:
        return -1
    return res
# đề yêu cầu là dãy con liên tiếp không phải dãy con bất kì


data = []
while 1:
    try:
        data += input().split()
    except EOFError:
        break
# đọc hết luồng vào, vì có thể đề cho mảng không cùng 1 dòng
t = int(data[0])
idx = 1
while t > 0:
    n, k = int(data[idx]), int(data[idx + 1])
    arr = []
    idx += 2
    for i in range(idx, n + idx):
        arr.append(int(data[i]))
    idx += n
    print(count(arr, k))
    t -= 1
