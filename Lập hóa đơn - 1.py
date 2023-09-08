from decimal import Decimal, ROUND_HALF_UP

idx = 1


class Guess:
    id = 'KH'
    Total = 0

    def __init__(self, name, old, new):
        global idx
        self.id += '{:02d}'.format(idx)
        idx += 1
        self.name = name
        self.new = new
        self.old = old
        diff = new - old
        if diff <= 50:
            x = diff * 100 * 1.02
        elif diff <= 100:
            x = (50 * 100 + (diff - 50) * 150) * 1.03
        else:
            x = (50 * 100 + 50 * 150 + (diff - 100) * 200) * 1.05
        self.Total = Decimal(x).quantize(Decimal('0'), ROUND_HALF_UP)

    def output(self):
        print(self.id, self.name, self.Total)


lst = []
n = int(input())
for i in range(n):
    lst.append(Guess(input(), int(input()), int(input())))
lst = sorted(lst, key=lambda x: -x.Total)
for i in lst:
    i.output()
