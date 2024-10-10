dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def make_danger_zone(board, i, j):
    for k in range(8):
        ni, nj = i + dirs[k][0], j + dirs[k][1]
        if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 0:
            board[ni][nj] = -1


def count_danger_zone(board, n, m):
    cnt = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1

    return cnt


def solution(board):
    n, m = len(board), len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                make_danger_zone(board, i, j)

    return count_danger_zone(board, n, m)
