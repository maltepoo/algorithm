n = int(input())
movie = [list(map(int, input())) for _ in range(n)]
def divide(x, y, n):
    std = movie[x][y]
    for i in range(x, n+x):
        for j in range(y, n+y):
            if std != movie[i][j]:
                print('(', end="")
                divide(x,y,n//2)
                divide(x,y+n//2,n//2)
                divide(x+n//2,y,n//2)
                divide(x+n//2,y+n//2,n//2)
                print(')', end="")
                return
    return print(std, end="")
divide(0,0,n)