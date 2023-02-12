n = int(input())
arr = []
high = 0
for _ in range(n):
    tmp = list(map(int, input().split(" ")))
    if max(tmp) > high:
        high = max(tmp)
    arr.append(tmp)

dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
def findSafePlace(x, y, r):
    q = [(x, y)]
    visited[x][y] = 1
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni, nj = i+dirs[k][0], j+dirs[k][1]
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] > r and not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1

res = []
for rain in range(high): #아무 지역도 물에 잠기지 않을수도 있다 = 0부터 최고높이까지 비가 올수 있다
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n): #안전영역이 발견되면 인접공간 탐색하여 넓이를 측정
            if arr[i][j] > rain and not visited[i][j]:
                findSafePlace(i, j, rain) #넓이측정
                cnt += 1 #안전영역이 발견된 수
    res.append(cnt)
print(max(res))