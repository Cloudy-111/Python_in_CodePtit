class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color.title()

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def check(self):
        if self.length <= 0 or self.width <= 0:
            return 0
        return 1

    def output(self):
        if self.check() == 1:
            print(f'{self.perimeter()} {self.area()} {self.color}')
        else:
            print("INVALID")


arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
r.output()
