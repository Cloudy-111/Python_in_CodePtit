import re

separate = r'[.?!]'

data = ''
while 1:
    try:
        data += input()
    except EOFError:
        break

seq = re.split(separate, data)
# print(seq)

for i in seq:
    if i != '':
        res = ' '.join(i.split())
        print(res.strip().capitalize())
