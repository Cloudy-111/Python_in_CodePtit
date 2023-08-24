t = int(input())
while t > 0:
    n, m = map(int, input().split())
    src = []
    for i in range(n):
        a = [int(x) for x in input().split()]
        src.append(a)
    kernel = []
    for i in range(3):
        a = [int(x) for x in input().split()]
        kernel.append(a)

    res = 0
    for i in range(n-2):
        for j in range(m-2):
            res += src[i][j]*kernel[0][0]+src[i][j+1]*kernel[0][1]+src[i][j+2]*kernel[0][2]+src[i + 1][j]*kernel[1][0]+src[i+1][j+1] * \
                kernel[1][1]+src[i+1][j+2]*kernel[1][2]+src[i+2][j]*kernel[2][0] + \
                src[i+2][j+1]*kernel[2][1]+src[i+2][j+2]*kernel[2][2]
    print(res)
    t -= 1
