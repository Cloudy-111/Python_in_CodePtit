class Person:
    def __init__(self, id, name, enter, outer):
        self.id = id
        self.name = name
        self.time = outer[0] * 60 + outer[1] - enter[0] * 60 - enter[1]
        self.x = int(self.time / 60)
        self.y = self.time % 60

    def output(self):
        print(self.id, self.name, f'{self.x} gio {self.y} phut')


lst = []
n = int(input())
for i in range(n):
    id = input()
    name = input()
    enter = [int(x) for x in input().split(':')]
    outer = [int(x) for x in input().split(':')]
    lst.append(Person(id, name, enter, outer))
lst.sort(key=lambda x: -x.time)
for i in lst:
    i.output()
