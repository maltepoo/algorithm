import sys
input = sys.stdin.readline

n, m, b = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for _ in range(n)]
ans = float("inf")
height = 0

minv, maxv = 999, -1
for i in range(n):
    mintemp, maxtemp = min(arr[i]), max(arr[i])
    if mintemp < minv:
        minv = mintemp
    if maxtemp > maxv:
        maxv = maxtemp

for val in range(minv, maxv+1):
    remove = 0
    add = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] < val: #인벤토리에 있는만큼 땅채우기
                add += (val - arr[i][j])
            else: #val에 맞게 땅파기
                remove += (arr[i][j] - val)
    inven = remove + b
    if inven < add:
        continue
    time = 2 * remove + add
    if time <= ans: #최소시간이면
        ans = time
        height = val #최소시간일경우 땅의높이
print(ans, height)