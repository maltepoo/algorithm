n = int(input())
ns = list(map(int, input().split()))

dp1 = [1]*(n) # 증가
dp2 = [1]*(n) # 감소

for i in range(1, n):
    for j in range(0, i):
        if ns[j] < ns[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if ns[j] < ns[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

max_len = 0
for k in range(n):
    max_len = max(max_len, dp1[k] + dp2[k] - 1)
    
print(max_len)