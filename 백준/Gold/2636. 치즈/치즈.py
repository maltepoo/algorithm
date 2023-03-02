dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = [(x, y)]
    visited[x][y] = 1
    melt = []
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni, nj = i + dirs[k][0], j + dirs[k][1]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj] == 1:  # 녹일 치즈
                    melt.append((ni, nj))
                else: # 공기(0)이면 계속탐색
                    q.append((ni, nj))
    for mi, mj in melt:
        arr[mi][mj] = 0
    return len(melt)

n, m = map(int, input().split(" "))
arr = []
cheese = 0
for i in range(n):
    temp = list(map(int, input().split(" ")))
    arr.append(temp)
    cheese += sum(temp)

bfsCnt = 0
while True:
    visited = [[0] * m for _ in range(n)]
    bfsCnt += 1
    melted = bfs(0, 0)
    cheese -= melted
    if cheese == 0:
        print(bfsCnt, melted, sep="\n")
        break