t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))

    pf = [0]*(k+1) #구간합
    for i in range(1,k+1):
        pf[i] = files[i-1] + pf[i-1]

    dp = [[0]*(k+1) for _ in range(k+1)]
    for cnt in range(1, k): # cnt개를 합칠 때
        for s in range(1, k-cnt+1): # 시작idx
            e = s+cnt
            MIN = float('inf')

            for m in range(s, e): #최소구간합구하기
                MIN = min(MIN, dp[s][m] + dp[m+1][e])
            dp[s][e] = MIN + pf[e] - pf[s-1] #이미구해논구간합으로 s~e사이의 합만 구한다

    print(dp[1][k])