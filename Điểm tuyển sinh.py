idx = 1


class Student:
    def __init__(self, name, result, ethnic, area):
        global idx
        self.id = f'TS{idx:02d}'
        idx += 1
        self.name = ' '.join(name.title().split())
        self.ethnic = ethnic
        self.area = area
        self.result = result + self.calBonus()
        self.stat = self.calStat()

    def calBonus(self):
        res = 0
        if self.area == 1:
            res += 1.5
        elif self.area == 2:
            res += 1
        else:
            pass
        if self.ethnic != 'Kinh':
            res += 1.5
        return res

    def calStat(self):
        bonus = self.calBonus()
        res = self.result + bonus
        if res < 20.5:
            return 'Truot'
        else:
            return 'Do'

    def __str__(self):
        return f'{self.id} {self.name} {self.result} {self.stat}'


t = int(input())
lst = []
while t > 0:
    name = input()
    result = float(input())
    ethnic = input()
    area = int(input())
    lst.append(Student(name, result, ethnic, area))
    t -= 1

lst = sorted(lst, key=lambda x: (-x.result, x.id))
for i in lst:
    print(i)
