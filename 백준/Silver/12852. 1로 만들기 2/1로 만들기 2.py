x = int(input())
dp = [0]*(x+1)
path = [0]*(x+1)

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    path[i] = i - 1

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        path[i] = i // 3
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        path[i] = i // 2

print(dp[x])

# path 출력
res = []
cur = x
while cur:
    res.append(cur)
    cur = path[cur]

print(*res)