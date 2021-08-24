#1954. 달팽이 숫자
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    dir = 0
    cnt = 1
    y, x = 0, -1
    while cnt <= N*N:
        ny = y + di[dir]
        nx = x + dj[dir]

        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 0:
            arr[ny][nx] = cnt
            cnt += 1
            y, x = ny, nx
        else:
            dir = (dir + 1) % 4

    print('#{}'.format(tc))
    for row in arr:
        print(*row)


