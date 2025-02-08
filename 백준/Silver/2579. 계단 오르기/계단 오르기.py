n = int(input())
stairs = [int(input()) for _ in range(n)]

dp = [0]*(n+1)
dp[1] = stairs[0]

for i in range(2, n+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i-2], dp[i-2] + stairs[i-1])

print(dp[-1])