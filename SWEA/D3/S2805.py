#2805. 농작물 수확하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int,list(input()))) for _ in range(N)]

    tot = 0
    mid = N//2
    s = e = mid

    for i in range(N):
        for j in range(s, e+1):
            tot += farm[i][j]
        if i < mid:
            s, e = s -1, e + 1 #양 쪽 늘어나
        else:
            s, e = s + 1, e - 1 #양 쪽 줄어들어
    print('#{} {}'.format(tc, tot))
