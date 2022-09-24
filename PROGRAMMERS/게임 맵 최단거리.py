# 캐릭터 (0,0) 상대방 (n,m)
def bfs(maps):
    n, m = len(maps), len(maps[0])
    q = [(0,0)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        i, j = q.pop(0)
        if i == (n-1) and j == (m-1):
            return maps[n-1][m-1]
        for k in range(4):
            ni, nj = i + dirs[k][0], j + dirs[k][1]
            if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1:
                maps[ni][nj] = maps[i][j] + 1
                q.append((ni,nj))
    return -1

def solution(maps):
    return bfs(maps)