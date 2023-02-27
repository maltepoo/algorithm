n, k = map(int, input().split(" "))
weight_value = [tuple(map(int, input().split(" "))) for _ in range(n)]

knapsack = [0]*(k+1)
for i in range(1, n+1):
    for j in range(k, 0, -1):
        if j >= weight_value[i-1][0]:
            knapsack[j] = max(knapsack[j], weight_value[i-1][1]+knapsack[j-weight_value[i-1][0]])
print(knapsack[-1])