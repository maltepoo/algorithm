n = int(input())
lose = list(map(int, input().split(" ")))
get = list(map(int, input().split(" ")))

#Basic knapsack
# value = [[0]*101 for _ in range(n+1)]
# for i in range(1, n+1): #사람들
#     for j in range(1, 101): #체력
#         if j <= lose[i-1]: #현재 체력이 인사 후 잃는 체력보다 같거나 적으면
#             value[i][j] = value[i-1][j] #새로 인사하지 않고 넘어간다
#         else:
#             value[i][j] = max(value[i-1][j], get[i-1]+value[i-1][j-lose[i-1]])
#             # 안만나는 경우, 새로운 사람을 만나 인사하는 경우 둘 중 최적의 값 선택
# print(value[n][100])

#1차원배열
value = [0]*101
for i in range(1, n+1):
    for j in range(100, 0, -1):
        if j > lose[i-1]:
            value[j] = max(value[j], get[i-1]+value[j-lose[i-1]])
print(value[-1])