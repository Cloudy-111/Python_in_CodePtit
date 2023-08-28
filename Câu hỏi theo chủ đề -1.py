t = int(input())
seq = []
while t > 0:
    seq.append(input())
    t -= 1
title = [seq[0]]
for i in range(len(seq)):
    if seq[i] == '':
        title.append(seq[i+1])
d = dict.fromkeys(title, 0)
for i in seq:
    if i in d:
        check = i
    elif i != '':
        d[check] += 1
for k, v in d.items():
    print(f'{k}: {v}')
