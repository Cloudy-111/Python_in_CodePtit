from decimal import Decimal, ROUND_HALF_UP

idx = 1


class Student:
    id = 'HS'
    ave = 0
    Rank = ''

    def __init__(self, name, point):
        global idx
        self.id += '{:02d}'.format(idx)
        idx += 1
        self.name = name

        x = point[0] * 2 + point[1] * 2
        for i in range(2, 10):
            x += point[i]
        x /= 12
        if x < 5:
            self.Rank = 'YEU'
        elif x < 7:
            self.Rank = 'TB'
        elif x < 8:
            self.Rank = 'KHA'
        elif x < 9:
            self.Rank = 'GIOI'
        else:
            self.Rank = 'XUAT SAC'

        self.ave = x.quantize(Decimal('0.1'), ROUND_HALF_UP)
        # dùng đối tượng Decimal trong thư viện decimal mang lại độ chính xác cao hơn round
        # cú pháp Decimal(any).quantize(Decimal('0.1'), ROUND_HALF_UP) -> là làm tròn đến 1 chữ số thập phân, nếu muốn nhiều hơn thì cứ vậy tăng thêm số 0
        # đối số thứ 2 thì nhận 1 trong 2 gía trị : ROUND_HALF_UP hoặc ROUND_HLF_EVEN
        # ROUND_HALF_UP: Phương thức làm tròn này làm tròn số thập phân đến gần giá trị nguyên gần nhất, nếu số thứ hai sau dấu thập phân là 5 hoặc cao hơn. Nếu số thứ hai sau dấu thập phân nhỏ hơn 5, nó sẽ làm tròn xuống.
        # ROUND_HALF_EVEN: Làm tròn số thập phân đến giá trị nguyên gần nhất với quy tắc sau: nếu số ngay sau dấu thập phân là 5 và số thập phân chẵn thì làm tròn xuống; nếu số thập phân lẻ, thì làm tròn lên.

    def output(self):
        print(self.id, self.name,
              self.ave, self.Rank)


lst = []
n = int(input())
for i in range(n):
    name = input()
    point = [Decimal(x) for x in input().split()]
    lst.append(Student(name, point))
sorted_lst = sorted(lst, key=lambda student: (
    -student.ave, student.id))
for student in sorted_lst:
    student.output()
