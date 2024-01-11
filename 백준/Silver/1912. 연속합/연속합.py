n = int(input())
sequence = list(map(int, input().split()))

dp = [0] + sequence
for i in range(2, n+1):
    dp[i] = max(dp[i-1]+sequence[i-1], dp[i])

print(max(dp[1:]))