from decimal import Decimal, ROUND_HALF_UP

idx = 1


class Staff:
    id = 'TS0'
    # đề đểu, 01, 02, 03,....., 010, 011, 012,......
    Total = 0
    stat = ''

    def __init__(self, name, p1, p2):
        global idx
        self.id += '{:d}'.format(idx)
        idx += 1
        self.name = name
        if p1 > 10:
            p1 /= 10
        if p2 > 10:
            p2 /= 10
        self.Total = (p1 + p2) / 2
        if self.Total < 5:
            self.stat = 'TRUOT'
        elif self.Total < 8:
            self.stat = 'CAN NHAC'
        elif self.Total < 9.5:
            self.stat = 'DAT'
        else:
            self.stat = 'XUAT SAC'

    def output(self):
        print(self.id, self.name, '{:.2f}'.format(self.Total), self.stat)


lst = []
n = int(input())
for i in range(n):
    lst.append(Staff(input(), float(input()), float(input())))
lst = sorted(lst, key=lambda x: -x.Total)
for i in lst:
    i.output()
