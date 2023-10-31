from datetime import date
from math import *


def during(begin, end):
    b = [int(x) for x in begin.split('/')]
    e = [int(x) for x in end.split('/')]
    res = date(e[2], e[1], e[0]) - date(b[2], b[1], b[0])
    return res.days


def price(x):
    if x == 1:
        return 25
    elif x == 2:
        return 34
    elif x == 3:
        return 50
    else:
        return 80


idx = 1


class Guess:
    def __init__(self, name, roomId, begin, end, arise):
        global idx
        self.id = f'KH{idx:02d}'
        idx += 1
        self.name = name.strip()
        self.roomId = roomId
        self.during = during(begin, end) + 1
        self.price = price(floor(roomId / 100))
        self.arise = arise
        self.Total = self.price * self.during + arise

    def __str__(self):
        return f'{self.id} {self.name} {self.roomId} {self.during} {self.Total}'


t = int(input())
lst = []
while t > 0:
    name = input()
    roomId = int(input())
    begin = input()
    end = input()
    arise = int(input())
    lst.append(Guess(name, roomId, begin, end, arise))
    t -= 1

lst = sorted(lst, key=lambda x: -x.Total)
for i in lst:
    print(i)
