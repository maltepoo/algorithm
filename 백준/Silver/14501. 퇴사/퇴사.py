n = int(input())
tb = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)

# top-down
# for i in range(n-1, -1, -1):
#     if i + tb[i][0] > n: # 상담을 끝내면 퇴사날이 지날 때
#         dp[i] = dp[i+1] # 상담을 하지 않아 이전 최고값을 그대로 가져옴
#         # i: 현재일수, tb[i][0]: 상담소요일수
#     else:
#         dp[i] = max(dp[i+1], tb[i][1] + dp[i+tb[i][0]])
#         # dp[i+1]: 상담을 안할경우 / tb[i][1]: i일의 상담 이익 + dp[i+tb[i][0]]: i일 + i일의 상담일 의 최대 이익 계산값
# print(dp[0])

# bottom-up
# dp에는 i번째 일까지 일했을 때의 최대 이익이 담김
for i in range(n):
    for j in range(i+tb[i][0], n+1): # i일 상담 이후 가능한 상담들
        if dp[j] < dp[i]+tb[i][1]:
            dp[j] = dp[i] + tb[i][1]
print(dp[-1])