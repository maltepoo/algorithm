n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)] #세방향 경우의수
dp[0][1][0] = 1  # (1,2) 위치에서 가로 방향으로 시작

# 0:→, 1:↓, 2:↘
for x in range(n):
    for y in range(2, n):
        if arr[x][y] == 1:
            continue

        #가로(가로/대각이동가능)
        dp[x][y][0] = dp[x][y-1][0] + dp[x][y-1][2]

        #세로(세/대각)
        if x > 0:
            dp[x][y][1] = dp[x - 1][y][1] + dp[x - 1][y][2]

        #대각(가/세/대)
        if x > 0 and arr[x - 1][y] == 0 and arr[x][y - 1] == 0:
            dp[x][y][2] = dp[x - 1][y - 1][0] + dp[x - 1][y - 1][1] + dp[x - 1][y - 1][2]

print(sum(dp[n-1][n-1]))