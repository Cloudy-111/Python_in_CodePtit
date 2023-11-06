from math import *

idx = 1


class Student:
    def __init__(self, name, res1, res2, res3):
        global idx
        self.rank = 0
        self.id = f'SV{idx:02d}'
        idx += 1
        self.name = ' '.join(name.title().split())
        self.res = (res1 * 3 + res2 * 3 + res3 * 2) / 8

    def setRank(self, ord):
        self.rank = ord

    def __str__(self):
        return f'{self.id} {self.name} {(ceil(self.res * 100) / 100):.2f} {self.rank}'


t = int(input())
lst = []
while t > 0:
    name = input()
    res1 = int(input())
    res2 = int(input())
    res3 = int(input())
    lst.append(Student(name, res1, res2, res3))
    t -= 1


lst = sorted(lst, key=lambda x: -x.res)

curres = lst[0].res
cur = 1
d = 0
for i in lst:
    if i.res != curres:
        curres = min(curres, i.res)
        cur += d
        d = 1
    else:
        d += 1
    i.setRank(cur)
lst = sorted(lst, key=lambda x: (-x.res, x.id))
for i in lst:
    print(i)
