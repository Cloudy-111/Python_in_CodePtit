def solve(s):
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]
    # print(left, right)
    a, b = rotate(left), rotate(right)
    # print(a, b)
    print(merge(a, b))


def rotate(s):
    sum = 0
    for i in s:
        sum += ord(i) - ord('A')
    res = ''
    for i in s:
        res += chr((ord(i) + sum - 65) % 26 + 65)
    return res


def merge(s, b):
    res = ''
    for i in range(len(s)):
        res += chr((ord(s[i]) + ord(b[i]) - 65 - 65) % 26 + 65)
    return res


n = int(input())
while n > 0:
    s = input()
    solve(s)
    n -= 1

# 3
# EWPGAJRB
# BB
# TPQJDRJWSQXGRRIPXFMINTELHBJA
