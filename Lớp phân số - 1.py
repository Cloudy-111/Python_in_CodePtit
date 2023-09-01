import math


class Phanso:
    def __init__(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso

    def sum(self, a, b):
        self.tuso = a.tuso * b.mauso + a.mauso * b.tuso
        self.mauso = a.mauso * b.mauso

    def output(self):
        print(f'{self.tuso}/{self.mauso}')

    def simplify(self):
        UCLN = math.gcd(self.tuso, self.mauso)
        self.tuso //= UCLN
        self.mauso //= UCLN
        return self


n = input().split()
a = Phanso(int(n[0]), int(n[1])).simplify()
a.output()
