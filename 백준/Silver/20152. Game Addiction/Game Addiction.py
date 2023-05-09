h, n = map(int, input().split())
m = abs(h-n) # 집과 pc방의 거리차만 알면 사이의 경로개수를 알 수 있음
dp = [[0]*(m+1) for _ in range(m+1)]
for d in range(m+1):
    dp[0][d] = 1

for i in range(1, m+1):
    for j in range(i, m+1): # y>x는 침수되어 지나갈 수 없음
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
print(dp[m][m])