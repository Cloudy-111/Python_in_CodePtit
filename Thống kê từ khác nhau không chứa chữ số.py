from collections import Counter
import re
n = int(input())
pattern = r'[^\W\d.,\/?!:;()-]+'
res = []
while n > 0:
    a = input()
    res += re.findall(pattern, a.lower())
    n -= 1
dic = Counter(res)
dic = dict(sorted(dic.items(), key=lambda x: (-x[1], x[0])))
for i in dic:
    print(i, dic[i])
