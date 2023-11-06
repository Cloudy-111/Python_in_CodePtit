class CLB:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Match:
    def __init__(self, id, numOfFan):
        self.id = id
        self.numOfFan = numOfFan


class Infor:
    def __init__(self, clb, match):
        self.clb = clb
        self.match = match
        self.price = clb.price * match.numOfFan

    def __str__(self):
        return f'{self.match.id} {self.clb.name} {self.price}'


t1 = int(input())
lst1 = []
while t1 > 0:
    idClb = input()
    nameClb = input()
    price = int(input())
    lst1.append(CLB(idClb, nameClb, price))
    t1 -= 1

t2 = int(input())
lst2 = []
while t2 > 0:
    inp = input().split()
    idMatch = inp[0]
    numOfFan = int(inp[1])
    for i in lst1:
        if i.id == idMatch[1:3]:
            lst2.append(Infor(i, Match(idMatch, numOfFan)))
    t2 -= 1

lst2 = sorted(lst2, key=lambda x: (-x.price, x.clb.id))
for i in lst2:
    print(i)
