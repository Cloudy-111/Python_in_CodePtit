import math


class Phanso:
    def __init__(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso

    def ouput(self):
        print(f'{self.tuso}/{self.mauso}')

    def simplify(self):
        UCLN = math.gcd(self.tuso, self.mauso)
        self.tuso //= UCLN
        self.mauso //= UCLN
        return self

    def sum(self, b):
        new_t = self.tuso * b.mauso + self.mauso * b.tuso
        new_m = self.mauso * b.mauso
        return Phanso(new_t, new_m)


n = input().split()
a = Phanso(int(n[0]), int(n[1]))
b = Phanso(int(n[2]), int(n[3]))
res = a.sum(b).simplify().ouput()
