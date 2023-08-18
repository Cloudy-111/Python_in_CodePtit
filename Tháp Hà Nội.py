def chuyen(a, c):
    print(f'{a} -> {c}')


def thap(n, a, b, c):
    if n == 1:
        chuyen(a, c)
    else:
        thap(n-1, a, c, b)  # chuyen n-1 tu a sang b qua c
        chuyen(a, c)  # chuyen dia n tu a sang c
        thap(n-1, b, a, c)  # chuyen n-1 tu b sang c qua a


n = int(input())
thap(n, 'A', 'B', 'C')
