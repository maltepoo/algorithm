t, w = map(int, input().split())
plums = [int(input()) for _ in range(t)]

dp = [[0]*(w+1) for _ in range(t+1)] # t초에 w번 이동

for i in range(1, t+1):
    loc = plums[i-1]
    for j in range(w+1):
        where = (j % 2) + 1
        plum = 1 if loc == where else 0

        # 이동한 경우
        dp[i][j] = dp[i-1][j] + plum

        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + plum)

print(max(dp[t]))