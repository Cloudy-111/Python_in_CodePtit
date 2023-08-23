n = int(input())
matrix = []
for i in range(n):
    a = [int(x) for x in input().split()]
    matrix.append(a)
k = int(input())
top = bot = 0
for i in range(n):
    for j in range(n):
        if j > n - i - 1:
            top += matrix[i][j]
        elif j < n - i - 1:
            bot += matrix[i][j]

diff = abs(top - bot)
if diff > k:
    print("NO")
else:
    print("YES")
print(diff)
