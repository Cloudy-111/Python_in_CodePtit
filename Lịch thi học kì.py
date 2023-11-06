class Subject:
    def __init__(self, idSub, nameSub):
        self.idSub = idSub
        self.nameSub = nameSub

    def show(self):
        return f'{self.idSub} {self.nameSub}'


idx = 1


class Schedule(Subject):
    def __init__(self, idSub, nameSub, date, time, group):
        global idx
        self.id = f'T{idx:03d}'
        idx += 1
        super().__init__(idSub, nameSub)
        self.time = time
        self.day = date[:2]
        self.month = date[3:5]
        self.year = date[6:]
        self.group = group

    def __str__(self):
        return self.id + ' ' + Subject.show(self) + ' ' + f'{self.day}/{self.month}/{self.year} {self.time} {self.group}'


n, m = [int(x) for x in input().split()]
lstSub = []
while n > 0:
    lstSub.append(Subject(input(), input()))
    n -= 1
lstSche = []
while m > 0:
    tmp = input().split()
    idSub = tmp[0]
    nameSub = ''
    for i in lstSub:
        if i.idSub == idSub:
            nameSub = i.nameSub
    date = tmp[1]
    time = tmp[2]
    group = tmp[3]
    lstSche.append(Schedule(idSub, nameSub, date, time, group))
    m -= 1

lstSche = sorted(lstSche, key=lambda x: (
    x.year, x.month, x.day, x.time, x.idSub))
for i in lstSche:
    print(i)
