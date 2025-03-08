dp = [0]*(1001)
dp[0] = 1

for i in range(1, 1001):
    for j in range(i):
        dp[i] += dp[j] * dp[i-1-j] # 카탈린수

while True:
    n = int(input())
    if n == 0:
        break

    print(dp[n])
