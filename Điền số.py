t = int(input())
while t > 0:
    n = int(input())
    arr = [int(x) for x in input().split()]
    l = min(arr)
    r = max(arr)
    s = set(arr)
    print(r-l+1-len(s))
    t -= 1
