n = int(input())
dp = [0]*11
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3, 11):
    dp[i] = sum(dp[i-3:i])

for _ in range(n):
    tc = int(input())
    print(dp[tc-1])

"""
n > 3
f(n) = f(n-1) + f(n-2) + f(n-3) 
"""