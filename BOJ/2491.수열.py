n = int(input())
m = list(map(int, input().split()))
dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]
for i in range(1, n):
    # 증가하는 수
    if m[i-1] <= m[i]:
        dp1[i] = dp1[i-1] + 1
for j in range(1, n):
    # 감소하는 수
    if m[j-1] >= m[j]:
        dp2[j] = dp2[j-1] + 1
print(max(max(dp1), max(dp2))+1)