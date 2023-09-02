class Student:
    def __init__(self, name, birth, p1, p2, p3):
        self.name = name
        a = birth.split('/')
        res = ''
        for i in range(len(a)):
            if len(a[i]) == 1:
                res += '0' + a[i]
            else:
                res += a[i]
            if i != len(a) - 1:
                res += '/'
        self.birth = res
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.sum = p1 + p2 + p3

    def output(self):
        print(f'{self.name} {self.birth} {self.sum:.1f}')


name = input()
birth = input()
p1 = float(input())
p2 = float(input())
p3 = float(input())
s = Student(name, birth, p1, p2, p3)
s.output()
