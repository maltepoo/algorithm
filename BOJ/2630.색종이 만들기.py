n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0
def cut(x, y, m):
    global w, b
    std = arr[x][y]
    for i in range(x, x+m):
        for j in range(y, y+m):
            if arr[i][j] != std:
                cut(x, y, m//2) # 1사분면
                cut(x, y+m//2, m//2) # 2사분면
                cut(x+m//2, y, m//2) # 3사분면
                cut(x+m//2, y+m//2, m//2) #4사분면
                return
    if std == 0:
        w += 1
    else:
        b += 1
cut(0, 0, n)
print(w, b, sep="\n")