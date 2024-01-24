arr = [list(map(int, input().split())) for _ in range(9)]
answer = -1
location = []

for i in range(9):
    for j in range(9):
        if arr[i][j] > answer:
            answer = arr[i][j]
            location = [i+1, j+1]

print(answer)
print(*location)