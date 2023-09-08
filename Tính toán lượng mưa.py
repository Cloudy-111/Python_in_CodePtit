def time(start, end):
    return end[0] * 60 + end[1] - start[0] * 60 - start[1]


a = dict()
n = int(input())
while n > 0:
    name = input()
    start = [int(x) for x in input().split(':')]
    end = [int(x) for x in input().split(':')]
    amount = int(input())
    if name not in a:
        a[name] = (time(start, end), amount)
    else:
        a[name] = (a[name][0] + time(start, end), a[name][1] + amount)
        # do tuple không thể thay đổi giá trị nên ghi đè thành 1 tuple khác, có thể thay thành list để thay đổi giá trị
    n -= 1

idx = 1
for i in a:
    print('T{:02d}'.format(idx), i, '{:.2f}'.format(a[i][1] * 60 / a[i][0]))
    idx += 1
