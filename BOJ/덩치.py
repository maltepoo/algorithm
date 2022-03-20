n = int(input())
all = [tuple(map(int, input().split())) for _ in range(n)]
result = []
for i in range(n):
    bulk = 1
    for j in range(n):
        if all[i][0] < all[j][0] and all[i][1] < all[j][1]:
            bulk += 1
    result.append(bulk)
print(*result)