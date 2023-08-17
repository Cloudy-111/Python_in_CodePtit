import math
from bisect import bisect_left
import sys


def CountDivisor(n):
    res = 0
    i = 1
    while i < math.sqrt(n):
        if n % i == 0:
            res += 2
        i += 1

    if n % math.sqrt(n) == 0:
        res += 1
    return res


def phannt(n):
    num = 1
    cnt = CountDivisor(1)
    i = 1
    while i <= n:
        tmp = CountDivisor(i)
        if tmp > cnt:
            cnt = tmp
            num = i
        i += 1
    return num


# ẢO VL, lấy hàm trên để tạo mảng a
# nhập hết từ stdin, xuất ra kết quả từng dòng
# bisect_left để lấy phần tử lớn hơn hoặc bằng đầu tiên
a = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160,
     110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
t = int(input())
i = 0
for line in sys.stdin:
    n = int(line)
    print(a[bisect_left(a, n)])
    i += 1
    if i == t:
        break
