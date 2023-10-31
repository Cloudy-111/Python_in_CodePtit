class Product:
    def __init__(self, id, name, amount, price, discount):
        self.id = id
        self.name = name
        self.amount = amount
        self.price = price
        self.discount = discount
        self.last = price * amount - discount

    def __str__(self):
        return f'{self.id} {self.name} {self.amount} {self.price} {self.discount} {self.last}'


t = int(input())
lst = []
while t > 0:
    id = input()
    name = input()
    amount = int(input())
    price = int(input())
    discount = int(input())
    lst.append(Product(id, name, amount, price, discount))
    t -= 1

lst = sorted(lst, key=lambda x: -x.last)
for i in lst:
    print(i)
