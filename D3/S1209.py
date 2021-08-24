#1209. [S/W 문제해결 기본] 2일차 - Sum
n = 100
for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    rc = lc = 0
    for i in range(n):
        rc += arr[i][i] #왼-오 대각선
        r = c = 0
        for j in range(n):
            r += arr[i][j] #행
            c += arr[j][i] #열
            if j == n - 1 - i:
                lc += arr[i][j] #오-왼 대각선

        #최대값 찾기
        if rc > ans:
            ans = rc
        if lc > ans:
            ans = lc
        if r > ans:
            ans = r
        if c > ans:
            ans = c

    print('#{} {}'.format(tc, ans))