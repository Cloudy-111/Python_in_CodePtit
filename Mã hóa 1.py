def encode(n):
    n += '.'
    i = 0
    s = ''
    while i < len(n)-1:
        cnt = 1
        while n[i] == n[i+1]:
            cnt += 1
            i += 1
        print(cnt, n[i], sep='', end='')
        i += 1


t = int(input())
while (t > 0):
    n = input()
    encode(n)
    print()
    t -= 1
