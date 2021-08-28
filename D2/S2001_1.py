#2001. 파리 퇴치
def kill(r, c):
    k = 0
    for i in range(r, r+M):
        for j in range(c, c+M):
            k += fly[i][j]
    return k


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    tot = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            res = kill(i,j)
            if tot <= res:
                tot = res

    print('#{} {}'.format(tc, tot))