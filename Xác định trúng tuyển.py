def bonus(x):
    if x == '1':
        return 2
    elif x == '2':
        return 1.5
    elif x == '3':
        return 1
    else:
        return 0


def subject(x):
    if x == 'A':
        return 'TOAN'
    elif x == 'B':
        return 'LY'
    else:
        return 'HOA'


idx = 1


class Teacher:
    def __init__(self, name, Id, p1, p2):
        global idx
        self.id = f'GV{idx:02d}'
        idx += 1
        self.name = name
        self.Total = p1 * 2 + p2 + bonus(Id[-1])
        self.subject = subject(Id[0])
        self.stat = 'TRUNG TUYEN' if self.Total >= 18 else 'LOAI'

    def __str__(self):
        return f'{self.id} {self.name} {self.subject} {self.Total:.1f} {self.stat}'


t = int(input())
lst = []
while t > 0:
    name = input()
    Id = input()
    p1 = float(input())
    p2 = float(input())
    lst.append(Teacher(name, Id, p1, p2))
    t -= 1

lst = sorted(lst, key=lambda x: -x.Total)
for i in lst:
    print(i)
