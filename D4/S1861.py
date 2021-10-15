#1861. 정사각형 방
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    pos = [0]*(N**2)
    dist = [1]*(N**2)
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(N):
        for j in range(N):
            pos[arr[i][j]-1] = (i,j)

    for d in range(len(pos)):
        y, x = pos[d][0], pos[d][1]
        for k in range(4):
            ny, nx = y+dir[k][0], x+dir[k][1]
            if 0<=ny<N and 0<=nx<N and arr[ny][nx] == arr[y][x]-1:
                dist[d] = dist[d-1]+dist[d]
    mxV = 0
    room = 0
    for f in range(len(dist)):
        if mxV < dist[f]:
            mxV = dist[f]
            room = f+1

    print('#{} {} {}'.format(tc, room-mxV+1, mxV))