def solution(n):
    answer = [[0] * n for _ in range(n)]
    answer[0][0] = 1

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    i, j = 0, 1

    cnt = 2
    d = 0
    while cnt <= n**2:
        if answer[i][j] == 0:
            answer[i][j] = cnt
            cnt += 1

        ni, nj = i + dirs[d][0], j + dirs[d][1]
        if 0 <= ni < n and 0 <= nj < n and answer[ni][nj] == 0:
            i, j = ni, nj
        else:
            d = (d + 1) % 4
            i, j = i + dirs[d][0], j + dirs[d][1]
    return answer