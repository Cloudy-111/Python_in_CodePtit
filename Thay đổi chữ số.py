n = int(input())
while (n > 0):
    x, y = [x for x in input().split()]
    x1 = input().strip()  # đầu nhập theo 2 cách, nhập 2 số cùng 1 dòng hoặc khác dòng
    if (x1.count(' ')):
        x1, x2 = x1.split()
    else:
        x2 = input()
    p = max(x, y)
    q = min(x, y)
    print(int(x1.replace(p, q))+int(x2.replace(p, q)),
          int(x1.replace(q, p))+int(x2.replace(q, p)))
    n -= 1
