def solution(x, y, n):
    dp = [1e9]*(y+1)
    dp[x] = 0
    
    for i in range(x, y+1):
        # bottom-up : i를 기준으로 3가지 경우의 수의 위치에 대해 최소 회수 갱신
        if i * 3 <= y:
            dp[i*3] = min(dp[i]+1, dp[i*3])
        if i * 2 <= y:
            dp[i*2] = min(dp[i]+1, dp[i*2])
        if i + n <= y:
            dp[i+n] = min(dp[i]+1, dp[i+n])
            
    return dp[y] if dp[y] < 1e9 else -1
