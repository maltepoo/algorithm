import sys
input = sys.stdin.readline


def is_row_ok(i, num):
    for k in range(9):
        if board[i][k] == num:
            return False
    return True


def is_column_ok(j, num):
    for k in range(9):
        if board[k][j] == num:
            return False
    return True


def is_square_ok(i, j, num):
    for k in range(3):
        for l in range(3):
            if board[k+(i//3*3)][l+(j//3*3)] == num:
                return False
    return True


def solve(idx):
    if idx == len(blank): # 모든 빈칸을 채움
        for jdx in range(9):
            print(*board[jdx])
        exit() # 다른 경우의 수 볼 필요x

    x, y = blank[idx][0], blank[idx][1]
    for num in range(1, 10):
        if is_row_ok(x, num) and is_column_ok(y, num) and is_square_ok(x, y, num):
            board[x][y] = num
            solve(idx+1)
            board[x][y] = 0


board = [list(map(int, input().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

solve(0)