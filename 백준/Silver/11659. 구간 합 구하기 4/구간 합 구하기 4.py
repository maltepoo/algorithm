n, m = map(int, input().split())
arr = list(map(int, input().split()))
ij = [tuple(map(int, input().split())) for _ in range(m)]

prefix_sum = [0]*(n+1)
for i in range(n):
    prefix_sum[i+1] = arr[i] + prefix_sum[i] # 누적합

for i, j in ij:
    print(prefix_sum[j]-prefix_sum[i-1]) # 구간합은 누적합에서 i 이전까지의 구간합을 뺀 것