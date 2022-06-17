x = int(input())
dp = [0 for _ in range(x+1)]
# dp 배열에 최소 연산 회수를 기록
for i in range(2, x+1):
    dp[i] = dp[i-1] + 1 # -1을 한 경우를 기본으로
    # -1을 했을때, 나누기 2, 3 했을 때 최소 연산 횟수 비교하여 할당
    if i%2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
print(dp[x])