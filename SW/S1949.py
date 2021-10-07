#1949. [모의 SW 역량테스트] 등산로 조성
def dfs(i, j, K, path):
    global res
    if path > res: res = path
    visited[i][j] = 1

    for k in range(4):
        ni, nj = i+dir[k][0], j+dir[k][1]
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
            if arr[i][j] > arr[ni][nj]:
                dfs(ni, nj, K, path+1)
            elif arr[i][j] > arr[ni][nj] - K and K:
                temp = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1
                dfs(ni, nj, 0, path+1)
                arr[ni][nj] = temp
    visited[i][j] = 0

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    maxh = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > maxh:
                maxh = arr[i][j]
    res = 0
    dir = [(-1,0), (1,0), (0,-1), (0,1)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == maxh:
                dfs(i, j, K, 1)
    print('#{} {}'.format(tc, res))

# 풀이 2 ################################################
def dfs(i, j, K, path, now):
    global res
    if path > res: res = path
    visited[i][j] = 1

    for k in range(4):
        ni, nj = i+dir[k][0], j+dir[k][1]
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
            if now > arr[ni][nj]:
                dfs(ni, nj, K, path+1, arr[ni][nj])
            elif now > arr[ni][nj] - K and K:
                dfs(ni, nj, 0, path+1, arr[i][j]-1)
    visited[i][j] = 0

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    maxh = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > maxh:
                maxh = arr[i][j]
    res = 0
    dir = [(-1,0), (1,0), (0,-1), (0,1)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == maxh:
                dfs(i, j, K, 1, arr[i][j])
    print('#{} {}'.format(tc, res))