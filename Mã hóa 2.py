P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while 1:
    s = input().strip()
    t = s.split()
    k = int(t[0])
    if s.count(' '):
        S = list(t[1])
        for i in range(len(S)):
            S[i] = P[(P.find(S[i])+k) % 28]
        res = ''.join(S)
        print(''.join(reversed(res)))

    if k == 0:
        break
