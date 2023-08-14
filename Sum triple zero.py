def countTriple(arr):
    res = 0
    n = len(arr)
    for i in range(n-2):  # kĩ thuật 2 con trỏ để giảm xuống O(n^2)
        left = i+1
        right = n-1

        while left < right:
            sum = arr[i]+arr[left]+arr[right]
            if sum == 0:
                res += 1
                left += 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return res


t = int(input())
while (t > 0):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    print(countTriple(arr))
    t -= 1
