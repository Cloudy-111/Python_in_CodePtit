class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

        self.point = 0
        self.stat = ''

    def setData(self, data):
        x = 10 - data.count('m') - data.count('v') * 2
        self.point = x if x > 0 else 0
        self.stat = '' if x > 0 else 'KDDK'

    def __str__(self):
        return f'{self.id} {self.name} {self.grade} {self.point} {self.stat}'


t = int(input())
tmp = t
students = {}
while t > 0:
    a = Student(input(), input(), input())
    students[a.id] = a
    t -= 1

while tmp > 0:
    id, data = input().split()
    students[id].setData(data)
    tmp -= 1

for key, value in students.items():
    print(value)
