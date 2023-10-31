n = int(input())
st = set()
while n > 0:
    s = input().split()
    st.add(s[0])
    st.add(s[2])
    lst = list(st)
    lst = sorted(lst, key=lambda x: len(x))
    n -= 1
print(lst)
