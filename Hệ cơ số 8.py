def binToOct(s):
    res = 0
    for i in range(len(s)):
        if s[i] != '0':
            res += 2**(len(s)-i-1)
    return str(res)


n = input()
res = ''
while len(n) % 3 != 0:
    n = '0'+n
for i in range(0, len(n), 3):
    tmp = n[i:i+3]
    res += binToOct(tmp)
print(res)
