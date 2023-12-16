import re


def change(s):

    if s[-1] not in '.!?':
        s += '.'
    seq = []
    st, end = 0, 0
    for i in range(len(s)):
        if s[i] in '.!?':
            end = i + 1
            seq.append(fix(s[st: end]))
            st = end
    return seq


def fix(s):
    s = ' '.join(s.lower().capitalize().split())
    if s[-2] == ' ':
        return s[:-2] + s[-1:]
    return s


lst = []
while True:
    try:
        s = input()
        lst += change(s)
    except EOFError:
        break
# print(lst)
for i in lst:
    print(i)
