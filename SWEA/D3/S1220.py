#1220. [S/W 문제해결 기본] 5일차 - Magnetic
for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    #1: N극 2:극 테이블 위 N 아래 S
    cnt = 0
    for j in range(N):
        color = 1
        for i in range(N):
            if color == 1 and table[i][j] == 1:
                color = 2
            elif color == 2 and table[i][j] == 2:
                color = 1
                cnt += 1

    print('#{} {}'.format(tc, cnt))
