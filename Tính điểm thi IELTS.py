def point(x):
    if 3 <= x and x <= 4:
        return 2.5
    elif 5 <= x and x <= 6:
        return 3.0
    elif 7 <= x and x <= 9:
        return 3.5
    elif 10 <= x and x <= 12:
        return 4.0
    elif 13 <= x and x <= 15:
        return 4.5
    elif 16 <= x and x <= 19:
        return 5.0
    elif 20 <= x and x <= 22:
        return 5.5
    elif 23 <= x and x <= 26:
        return 6.0
    elif 27 <= x and x <= 29:
        return 6.5
    elif 30 <= x and x <= 32:
        return 7.0
    elif 33 <= x and x <= 34:
        return 7.5
    elif 35 <= x and x <= 36:
        return 8.0
    elif 37 <= x and x <= 38:
        return 8.5
    elif 39 <= x and x <= 40:
        return 9.0


t = int(input())
while t > 0:
    x = input().split()
    a, b = int(x[0]), int(x[1])
    c, d = float(x[2]), float(x[3])
    ave = (point(a) + point(b)+c+d)/4.0
    if ave - int(ave) >= 0.75:
        print(int(ave) + 1.0)
    elif ave - int(ave) >= 0.25:
        print(int(ave) + 0.5)
    else:
        print(int(ave))
    t -= 1
