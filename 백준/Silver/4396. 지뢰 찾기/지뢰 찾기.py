n = int(input())
mine = [list(input()) for _ in range(n)]
open = [list(input()) for _ in range(n)]

dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def findMines(i, j):
    cnt = 0
    for k in range(8):
        ni, nj = i+dirs[k][0], j+dirs[k][1]
        if 0<=ni<n and 0<=nj<n and mine[ni][nj] == '*':
            cnt += 1
    return cnt

mine_loc = []
flag = False
for i in range(n):
    for j in range(n):
        if mine[i][j] == '*':
            mine_loc.append((i, j))
        if open[i][j] == 'x' and mine[i][j] != '*':
            open[i][j] = str(findMines(i, j))
        elif open[i][j] == 'x' and mine[i][j] == '*':
            flag = True

if flag:
    for i, j in mine_loc:
        open[i][j] = '*'

for o in open:
    print(''.join(o))