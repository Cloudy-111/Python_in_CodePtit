t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    seq = []
    for i in range(n):
        while len(seq) > 0 and a[seq[-1]] <= a[i]:
            seq.pop()
        if len(seq) == 0:
            print(i+1, end=' ')
        else:
            print(i-seq[-1], end=' ')
        seq.append(i)

    t -= 1
