n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(max(a[0] * a[1] * a[n - 1], a[n - 1] * a[n - 2],
      a[0] * a[1], a[n - 1] * a[n - 2] * a[n - 3]))
