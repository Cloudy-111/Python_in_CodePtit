class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def sum(self, b):
        return Complex(self.real + b.real, self.img + b.img)

    def mul(self, b):
        return Complex(self.real * b.real - self.img * b.img, self.img * b.real + self.real * b.img)

    def output(self):
        if self.img < 0:
            print(f'{self.real} - {-self.img}i', end=', ')
        else:
            print(f'{self.real} + {self.img}i', end=', ')


t = int(input())
while t > 0:
    a, b, c, d = map(int, input().split())
    x = Complex(a, b)
    y = Complex(c, d)
    tmp = x.sum(y)
    c = tmp.mul(x).output()
    d = tmp.mul(tmp)
    if d.img < 0:
        print(f'{d.real} - {-d.img}i')
    else:
        print(f'{d.real} + {d.img}i')
    t -= 1
