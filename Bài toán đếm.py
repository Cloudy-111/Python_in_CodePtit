n = int(input())
lst = []
while True:
    try:
        a = [int(x) for x in input().split()]
        lst += a
    except EOFError:
        break
chk = 0
for i in range(1, lst[-1] + 1):
    if i not in lst:
        chk = 1
        print(i)
if chk == 0:
    print('Excellent!')
