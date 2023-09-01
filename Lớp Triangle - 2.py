import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, b):
        return math.sqrt((self.x - b.x)**2+(self.y - b.y)**2)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        ab = self.a.distance(self.b)
        bc = self.b.distance(self.c)
        ac = self.a.distance(self.c)
        if ab + bc <= ac or ab + ac <= bc or bc + ac <= ab:
            return 'INVALID'
        else:
            s = math.sqrt((ab + bc+ac)*(ab + bc-ac) *
                          (ab - bc+ac)*(-ab + bc+ac)) / 4
            return f'{s:.2f}'


# chưa hiểu tại sao nhập từng test một, xuất ra kết quả thì WA,
# còn nhập hết test, xuất kết quả các test thì lại AC
n = []
t = int(input())
for i in range(t):
    n += [float(x) for x in input().split()]
i = 0
for idx in range(t):
    Tri = Triangle(Point(n[i], n[i+1]), Point(n[i+2],
                   n[i+3]), Point(n[i+4], n[i+5]))
    print(Tri.area())
    i += 6
