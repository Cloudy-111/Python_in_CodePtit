def check(a, b, op, res):
    if op == '+':
        return a + b == res
    elif op == '-':
        return a - b == res
    elif op == '*':
        return a * b == res
    elif a % b == 0:
        return a // b == res
    return False


def generate(a):  # gen ra các số có thể có
    tmp = []
    if a[0] == '?':
        for i in range(1, 10):
            tmp.append(str(i) + a[1:])
    else:
        tmp.append(a)
    tmp2 = []
    if a[1] == '?':
        for i in tmp:
            for j in range(0, 10):
                tmp2.append(i[0] + str(j))
    else:
        tmp2 = tmp
    return tmp2


def generateOp(a):
    if a == '?':
        return '+-*/'
    return [a]  # đưa dấu vào list để duyệt


def solve(a):
    x = generate(a[0])
    op = generateOp(a[1])
    y = generate(a[2])
    res = generate(a[4])
    for i in x:
        for j in op:
            for k in y:
                for l in res:
                    if check(int(i), int(k), j, int(l)):
                        print(f'{i} {j} {k} = {l}')
                        return
    print('WRONG PROBLEM!')


t = int(input())
while t > 0:
    a = input().split()
    solve(a)
    t -= 1
