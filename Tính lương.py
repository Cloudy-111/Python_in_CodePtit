def multi(group, year):
    if 1 <= year <= 3:
        if group == 'A':
            return 10
        elif group == 'B':
            return 10
        elif group == 'C':
            return 9
        else:
            return 8
    elif 4 <= year <= 8:
        if group == 'A':
            return 12
        elif group == 'B':
            return 11
        elif group == 'C':
            return 10
        else:
            return 9
    elif 9 <= year <= 15:
        if group == 'A':
            return 14
        elif group == 'B':
            return 13
        elif group == 'C':
            return 12
        else:
            return 11
    else:
        if group == 'A':
            return 20
        elif group == 'B':
            return 16
        elif group == 'C':
            return 14
        else:
            return 13


depart = []


def room(dep):
    for i in depart:
        if dep == i[:2]:
            return i[3:]


class Staff:
    def __init__(self, id, name, base_wage, days):
        self.id = id
        self.name = name
        self.base_wage = int(base_wage)
        self.days = int(days)
        self.group = id[:1]
        self.year = int(id[1:3])
        self.dep = room(id[3:])
        self.total = base_wage * 1000 * days * multi(self.group, self.year)

    def output(self):
        print(f'{self.id} {self.name} {self.dep} {self.total}')


t = int(input())
for i in range(t):
    depart.append(input())
lst = []
n = int(input())
while n > 0:
    id = input()
    name = input()
    base_wage = int(input())
    days = int(input())
    lst.append(Staff(id, name, base_wage, days))
    n -= 1
for i in lst:
    i.output()
# 2
# HC Hanh chinh
# KH Ke hoach Dau tu
# 2
# C06HC
# Tran Binh Minh
# 65
# 25
# D03KH
# Le Hoa Binh
# 59
# 24
