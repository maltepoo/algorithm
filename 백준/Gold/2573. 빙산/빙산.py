def bfs(x, y):
    q = [(x, y)]
    melt = []
    while q:
        i, j = q.pop(0)
        visited[i][j] = 1
        zero = 0
        for k in range(4):
            ni, nj = i + dirs[k][0], j + dirs[k][1]
            if 0 <= ni < n and 0 <= nj < m:
                if not arr[ni][nj]:
                    zero += 1
                elif arr[ni][nj] and not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
        if zero > 0: # 얼음사방에 바다가 하나라도 있으면
            melt.append((i, j, zero)) # 그만큼 녹인다
    # bfs가 끝나면 얼음 녹임
    for mi, mj, c in melt:
        if arr[mi][mj] - c >= 0:
            arr[mi][mj] -= c
        else:
            arr[mi][mj] = 0
    return 1


n, m = map(int, input().split(" "))
arr = []
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ice = []
for c in range(n):
    temp = list(map(int, input().split(" ")))
    arr.append(temp)
    for r in range(m):
        if temp[r] > 0:
            ice.append((c, r))

y = 0
while ice:
    visited = [[0] * m for _ in range(n)]
    group = 0 # 빙산그룹의 개수
    rmv = [] # 녹일 얼음들
    for icei, icej in ice:
        if arr[icei][icej] and not visited[icei][icej]:
            group += bfs(icei, icej) # bfs가 다 돌았다면 1을 리턴, 이떄 bfs가 여러번 돈다면 group이 나뉘었다는 뜻
        if arr[icei][icej] == 0: # bfs내에서 다 녹은 얼음이면 탐색할 리스트에서 제거
            rmv.append((icei, icej))
    for r in rmv: # bfs를 다 돈 후에 제거 > 0 추가로 얼음이 이상하게 녹는 것 방지
        ice.remove(r)
    if group > 1:
        print(y)
        break
    y += 1
if group < 2:
    print(0)