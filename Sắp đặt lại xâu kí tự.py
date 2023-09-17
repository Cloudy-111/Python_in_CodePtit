t = int(input())
for i in range(1, t + 1):
    a = input()
    b = input()
    a = sorted(a)
    b = sorted(b)
    print(f'Test {i:d}:', end=' ')
    if a == b:
        print('YES')
    else:
        print('NO')
