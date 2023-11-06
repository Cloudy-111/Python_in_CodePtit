from datetime import *

idx = 1


class Customer:
    def __init__(self, name, sex, dob, address):
        global idx
        self.id = f'KH{idx:03d}'
        idx += 1
        self.name = ' '.join(name.title().split())
        self.sex = sex
        a, b, c = [int(x) for x in dob.split('/')]
        self.dob = f'{a:02d}/{b:02d}/{c}'
        self.address = address

    def __str__(self):
        return f'{self.id} {self.name} {self.sex} {self.address} {self.dob}'


t = int(input())
lst = []
while t > 0:
    name = input()
    sex = input()
    dob = input()
    address = input()
    lst.append(Customer(name, sex, dob, address))
    t -= 1

lst = sorted(lst, key=lambda x: -(datetime.today() -
             datetime.strptime(x.dob, '%d/%m/%Y')))
for i in lst:
    print(i)
