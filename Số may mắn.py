n = input()
res = 0
for i in range(len(n)):
    if n[i] == '4':
        res += 1
    if n[i] == '7':
        res += 1
if res == 4 or res == 7:
    print('YES')
else:
    print("NO")
