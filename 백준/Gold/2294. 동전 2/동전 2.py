n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [float('inf')]*(k+1) #i원을 만들기 위한 최소 동전개수
dp[0] = 0
for c in coins:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c] + 1) #최솟값 다시 갱신

print(dp[k] if dp[k] != float('inf') else -1)