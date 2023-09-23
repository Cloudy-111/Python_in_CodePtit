n = int(input())
mat = []
for i in range(n):
    a = [int(x) for x in input().split()]
    mat.append(a)
k = int(input())
top = 0
bot = 0
for i in range(n):
    for j in range(n):
        if i > j:
            bot += mat[i][j]
        elif i < j:
            top += mat[i][j]
diff = abs(top - bot)
if diff <= k:
    print('YES')
else:
    print('NO')
print(diff)
