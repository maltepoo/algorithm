n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
mzp = [0, 0, 0]
def divide(x, y, n):
    global mzp
    std = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if std != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        divide(x+k*n//3, y+l*n//3, n//3)
                return
    if std == -1:
        mzp[0] += 1
    elif std == 0:
        mzp[1] += 1
    else:
        mzp[2] += 1
divide(0, 0, n)
print(*mzp, sep='\n')
