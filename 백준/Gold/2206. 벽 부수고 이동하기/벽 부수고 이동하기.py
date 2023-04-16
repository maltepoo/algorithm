from collections import deque

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)] # 0 부순적 없음 1 부순적 있음

def bfs():
    q = deque() # 출발지점
    q.append((0, 0, 0))
    visited[0][0][1] = 1
    while q:
        i, j, c = q.popleft()
        if i == n-1 and j == m-1:
            return visited[i][j][c]+1
        for k in range(4):
            ni, nj = i+dirs[k][0], j+dirs[k][1]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 0 and visited[ni][nj][c] == 0: # 길이 있고, 벽을 부쉈을 때
                    q.append((ni, nj, c))
                    visited[ni][nj][c] = visited[i][j][c] + 1
                if arr[ni][nj] == 1 and c == 0: # 길이 없고, 벽을 안 부쉈을 때 (부수고 이동)
                    q.append((ni, nj, c+1))
                    visited[ni][nj][c+1] = visited[i][j][c] + 1
    return -1
print(bfs())