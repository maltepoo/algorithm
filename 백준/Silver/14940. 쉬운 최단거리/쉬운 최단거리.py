n, m = map(int, input().split())
arr = []
visited = [[-1]*m for _ in range(n)]
goal = (0, 0)

# 목표지점을 출발지점으로 모든 1에 거리를 기록
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 2:
            goal = (i, j)
        if temp[j] == 0:
            visited[i][j] = 0
    arr.append(temp)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    q = [goal]
    visited[goal[0]][goal[1]] = 0
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni, nj = i+dirs[k][0], j+dirs[k][1]
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == -1:
                if arr[ni][nj] == 1:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
bfs()
for v in visited:
    print(*v)