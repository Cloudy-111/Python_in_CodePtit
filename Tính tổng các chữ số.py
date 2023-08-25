t = int(input())
while t > 0:
    n = input()
    sum = 0
    str = ''
    for i in n:
        if i >= '0' and i <= '9':
            sum += int(i)
        else:
            str += i
    print(''.join(sorted(str)), end='')
    print(sum)
    t -= 1
