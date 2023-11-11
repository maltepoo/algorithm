dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution(board):
    start = []
    r, c = len(board), len(board[0])
    visited = [[float('inf')] * c for _ in range(r)]

    # 로봇 시작위치 초기화, 방문처리
    for i in range(r):
        if board[i].find("R") > -1:
            start = [i, board[i].find("R"), 0]
            visited[i][board[i].find("R")] = 0

    def ricochet(st):
        q = []
        q.append(st)

        while q:
            i, j, d = q.pop(0)

            if board[i][j] == 'G':
                return d

            for k in range(4):
                ni, nj = i + dirs[k][0], j + dirs[k][1]  # 방향을 정하면 장애물, 벽이 있을때까지 가야한다

                while 0 <= ni < r and 0 <= nj < c and board[ni][nj] != 'D':
                    ni += dirs[k][0]
                    nj += dirs[k][1]

                if not(0 <= ni < r and 0 <= nj < c) or board[ni][nj] == 'D':
                    ni -= dirs[k][0]
                    nj -= dirs[k][1]

                if visited[ni][nj] > d + 1:
                    visited[ni][nj] = d + 1
                    q.append((ni, nj, d + 1))

        return -1  # 목표지점에 도착하지 못할 경우

    return ricochet(start)