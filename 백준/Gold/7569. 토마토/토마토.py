import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = []
res = 0

riped = deque()
for k in range(h):
    box = []
    for i in range(n):
        tmt = list(map(int, input().split()))
        for j in range(m):
            if tmt[j] == 1:
                riped.append((k, i, j))
        box.append(tmt)
    arr.append(box)

dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)] # 상 하 좌 우 앞 뒤
while riped:
    k, i, j = riped.popleft()
    for d in range(6):
        nk, ni, nj = k+dirs[d][0], i+dirs[d][1], j+dirs[d][2]
        if 0 <= nk < h and 0 <= ni < n and 0 <= nj < m and arr[nk][ni][nj] == 0:
            riped.append((nk, ni, nj))
            arr[nk][ni][nj] = arr[k][i][j] + 1

for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 0: # 모든 토마토가 익지 못함
                print(-1)
                exit(0)
        res = max(res, max(arr[k][i]))
print(res-1)