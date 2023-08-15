t = int(input())
while (t > 0):
    n = list(input())
    carry = 0
    for i in range(len(n) - 1, 0, -1):
        n[i] = str(int(n[i])+carry)
        if n[i] != '0':
            if n[i] < '5':
                n[i] = '0'
                carry = 0
            elif n[i] >= '5':
                n[i] = '0'
                carry = 1

    n[0] = str(int(n[0])+carry)
    print(''.join(n))

    t -= 1
