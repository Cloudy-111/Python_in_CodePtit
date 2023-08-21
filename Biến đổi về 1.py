def count(n):
    s.add(n)
    if n == 1:
        return len(s)
    else:
        if n % 2 == 0:
            return count(n/2)
        else:
            return count(n*3+1)


while 1:
    n = int(input())
    if n == 0:
        break
    s = set()
    print(count(n))
