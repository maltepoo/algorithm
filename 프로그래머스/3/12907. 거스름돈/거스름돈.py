def solution(n, money):
    answer = 0
    
    dp = [1] + [0] * n
    for coin in sorted(money):
        for change in range(coin, n+1):
            dp[change] = (dp[change] + dp[change-coin]) % 1000000007
    
    return dp[n]