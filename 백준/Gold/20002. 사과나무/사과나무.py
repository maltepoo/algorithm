import sys
input = sys.stdin.readline

n = int(input())
prefixSum = [[0]*(n+1) for _ in range(n+1)]

profit = -1001
# 누적합 구하기
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(1, n+1):
        prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[j-1]

# 구간합 구하기
for k in range(n):
    for i in range(1, n-k+1): # 정사각형의 크기에 따른 시작점 설정(n-k+1)
        for j in range(1, n-k+1):
            temp = prefixSum[i+k][j+k] - prefixSum[i-1][j+k] - prefixSum[i+k][j-1] + prefixSum[i-1][j-1]
            # 정사각형의 가작 오른쪽 아래 꼭지점(0,0 부터 i+k, i+k(정사각형꼭짓점) 까지의 누적합
            # - 정사각형 범위가 아닌 부분의 누적합 2개
            # + 누적합 2게를 뺄 때 겹치게 2번 뺐던 부분을 다시 더해줌
            profit = max(profit, temp)
print(profit)