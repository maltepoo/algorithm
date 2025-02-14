n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

total_chz = 0
for i in range(n):
    total_chz += arr[i].count(1)


def melt_chz(x, y):
    visited[x][y] = 1

    qq = [(x, y)]
    melt = []

    while qq:
        i, j = qq.pop(0)

        for k in range(4):
            ni, nj = i + dirs[k][0], j + dirs[k][1]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj] == 1:
                    melt.append((ni, nj))
                elif arr[ni][nj] == 0:
                    qq.append((ni, nj))
    for mi, mj in melt:
        arr[mi][mj] = 0

    return len(melt)


for sec in range(1, 1001):
    visited = [[0]*m for _ in range(n)]

    melted = melt_chz(0, 0)
    total_chz -= melted

    if total_chz == 0:
        print(sec)
        print(melted)
        break