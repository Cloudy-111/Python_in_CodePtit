from datetime import datetime


def during(time):
    start = datetime(2000, 1, 1, 6, 0)
    lst = [int(x) for x in time.split(':')]
    end = datetime(2000, 1, 1, lst[0], lst[1])
    res = end - start
    return res.seconds


class Player:
    def __init__(self, name, unit, time):
        self.name = name
        self.unit = unit
        self.during = during(time)
        self.aveSpd = 120 / (self.during / 3600)
        self.id = ''.join([x[0] for x in unit.split()]) + \
            ''.join([x[0] for x in name.split()])

    def __str__(self):
        return f'{self.id} {self.name} {self.unit} {round(self.aveSpd)} Km/h'


t = int(input())
lst = []
while t > 0:
    name = input()
    unit = input()
    time = input()
    lst.append(Player(name, unit, time))
    t -= 1

lst = sorted(lst, key=lambda x: x.during)
for i in lst:
    print(i)
