def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    answer = 0

    rmv = set()
    while True:
        # 터트릴 블록 체크
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != "" and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    rmv.update({(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)})

        # 블록 터트리기
        if rmv:
            answer += len(rmv)
            for r in rmv:
                ri, rj = r
                board[ri][rj] = ""
            rmv.clear()
        else:
            return answer

        # board 정렬
        for i in range(m-1, 0, -1):
            for j in range(n):
                if board[i][j] == "":
                    for k in range(i, -1, -1):
                        if board[k][j] != "":
                            board[i][j], board[k][j]  = board[k][j], ""
                            break
    return answer