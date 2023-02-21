def solution(maps):
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    startI, startJ = 0, 0
    leverI, leverJ = 0, 0
    endI, endJ = 0, 0
    COL, ROW = len(maps), len(maps[0])

    for i in range(COL):
        maps[i] = list(maps[i])
        for j in range(ROW):
            if maps[i][j] == 'S':
                startI, startJ = i, j
            elif maps[i][j] == 'L':
                leverI, leverJ = i, j
            elif maps[i][j] == 'E':
                endI, endJ = i, j


    def bfs(x, y, goalx, goaly):
        q = [(x, y)]
        visited = [[0] * ROW for _ in range(COL)]
        while q:
            i, j = q.pop(0)
            for k in range(4):
                ni, nj = i + dirs[k][0], j + dirs[k][1]
                if 0 <= ni < COL and 0 <= nj < ROW and visited[ni][nj] == 0:
                    if ni == goalx and nj == goaly:
                        return visited[i][j]+1
                    if maps[ni][nj] != 'X':
                        q.append((ni, nj))
                        visited[ni][nj] = visited[i][j] + 1
        return -1

    startToLever = bfs(startI, startJ, leverI, leverJ)
    leverToEnd = bfs(leverI, leverJ, endI, endJ)

    if startToLever == -1 or leverToEnd == -1:
        return -1
    return startToLever + leverToEnd