import sys
from collections import deque
input = sys.stdin.readline
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

n, m, k = map(int, input().split(" "))
arr = [list(input()) for _ in range(n)]
visited = [[float('inf')]*m for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split(" "))

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        i, j = q.popleft()
        for l in range(4):
            ni, nj = i+dirs[l][0], j+dirs[l][1] #방향이 정해지면
            cnt = 1
            while cnt <= k and 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != '#' and visited[ni][nj] > visited[i][j]:
                if visited[ni][nj] == float('inf'):
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
                ni += dirs[l][0]
                nj += dirs[l][1]
                cnt += 1
    return
visited[x1-1][y1-1] = 0
bfs(x1-1, y1-1)

if visited[x2-1][y2-1] == float('inf'):
    print(-1)
else:
    print(visited[x2-1][y2-1])