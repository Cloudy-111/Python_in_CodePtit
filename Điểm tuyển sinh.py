idx = 1


class Student:
    id = 'TS'

    def __init__(self, name, res, ethnic, area):
        global idx
        self.id += '{:02d}'.format(idx)
        idx += 1
        self.name = name
        self.res = res
        self.ethnic = ethnic
        self.area = area
        self.total = res + priority(ethnic, area)
        self.stat = 'Do' if self.total >= 20.5 else 'Truot'

    def output(self):
        print(f'{self.id} {self.name} {self.total:.1f} {self.stat}')


def priority(ethnic, area):
    ans = 0
    if area == 1:
        ans += 1.5
    elif area == 2:
        ans += 1.0
    if ethnic != 'Kinh':
        ans += 1.5
    return ans


def standard(s):
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s.title()


n = int(input())
lst = []
while n > 0:
    name = standard(input())
    res = float(input())
    ethnic = input()
    area = int(input())
    lst.append(Student(name, res, ethnic, area))
    n -= 1

lst = sorted(lst, key=lambda x: (-x.total, x.id))
for i in lst:
    i.output()
# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3
