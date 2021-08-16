#2001. 파리 퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    tot = 0
    for i in range(N):
        for j in range(N):
            fly = 0
            if i < N-M+1 and j < N-M+1:
                for y in range(M):
                    for x in range(M):
                        fly += arr[i+y][j+x]
                if tot < fly:
                    tot = fly

    print('#{} {}'.format(tc, tot))