idx = 1


def defineStat(res):
    if res < 5:
        return 'Yeu'
    elif res < 7:
        return 'Trung Binh'
    elif res < 9:
        return 'Kha'
    else:
        return 'Gioi'


class Student:
    def __init__(self, name, result):
        global idx
        self.id = f'HS{idx:02d}'
        idx += 1
        self.name = name
        self.result = result
        self.stat = defineStat(result)
        self.rank = 0

    def setRank(self, rank):
        self.rank = rank

    def __str__(self):
        return f'{self.id} {self.name} {self.result:.1f} {self.stat} {self.rank}'


t = int(input())
lst = []
while t > 0:
    name = input()
    result = float(input())
    lst.append(Student(name, result))
    t -= 1

tmp = sorted(lst, key=lambda x: -x.result)

curResult = tmp[0].result
cur = 1
d = 0
for i in tmp:
    if i.result != curResult:
        curResult = min(curResult, i.result)
        cur += d
        d = 1
    else:
        d += 1
    i.setRank(cur)
for i in lst:
    print(i)
