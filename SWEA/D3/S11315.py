#11315. 오목 판정
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    di = [1, 1, 1, 0]  # 좌하 하 우하 우
    dj = [-1, 0, 1, 1]

    mcnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                cnt = 0
                ni, nj = i, j
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += di[k]
                        nj += dj[k]
                if cnt > mcnt:
                    mcnt = cnt
    if mcnt >= 5:
        print('#{} {}'.format(tc, "YES"))
    else:
        print('#{} {}'.format(tc, "NO"))