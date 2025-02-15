from itertools import combinations
from collections import deque
import copy

# 조합 + BFS
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

wall = []
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            wall.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

res = 0
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def calc_safe(arr_bfs):
    cnt = 0
    for a in arr_bfs:
        cnt += a.count(0)
    return cnt


def bfs():
    arr_bfs = copy.deepcopy(arr)
    q = deque(virus)

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + dirs[k][0], j + dirs[k][1]
            if 0 <= ni < n and 0 <= nj < m and arr_bfs[ni][nj] == 0:
                arr_bfs[ni][nj] = 2
                q.append((ni, nj))

    return calc_safe(arr_bfs)


for w in list(combinations(wall, 3)):
    arr[w[0][0]][w[0][1]], arr[w[1][0]][w[1][1]], arr[w[2][0]][w[2][1]] = 1, 1, 1
    res = max(res, bfs())
    arr[w[0][0]][w[0][1]], arr[w[1][0]][w[1][1]], arr[w[2][0]][w[2][1]] = 0, 0, 0

print(res)