dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(i, j, d):
    count = 0 # cnt는 두 구슬이 겹치려고 할 때 누가 먼저 왔는지 구분하기 위함
    while True:
        if arr[i+d[0]][j+d[1]] != '#' and arr[i][j] != 'O': #앞이 벽이거나, 현재가 탈출구가 아니면 계속 감
            i += d[0]
            j += d[1]
            count += 1
        else:
            break
    return i, j, count

def bfs(rx, ry, bx, by):
    q = [(rx, ry, bx, by, 1)]
    visited[rx][ry][bx][by] = 1

    while q:
        ri, rj, bi, bj, cnt = q.pop(0)
        if cnt > 10:
            break
        for k in range(4): #벽/출구 한칸 전까지만 이동
            rni, rnj, rmove = move(ri, rj, dirs[k])
            bni, bnj, bmove = move(bi, bj, dirs[k])

            if arr[bni][bnj] == 'O': #파란구슬이 도착하면 다른방향으로 계속
                continue
            if arr[rni][rnj] == 'O': #만약 ri, rj + k가 도착이면 성공
                return cnt

            if rni == bni and rnj == bnj: #같은 위치이면 move수가 많은 것을 한단계 뒤로 배치 = 뒤늦게 도착
                if rmove > bmove:
                    rni -= dirs[k][0]
                    rnj -= dirs[k][1]
                else:
                    bni -= dirs[k][0]
                    bnj -= dirs[k][1]

            if visited[rni][rnj][bni][bnj] == 0:
                q.append((rni, rnj, bni, bnj, cnt+1))
                visited[rni][rnj][bni][bnj] = 1
    return -1

n, m = map(int, input().split(" "))
arr = []
visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
red, blue = (), ()
for i in range(n):
    temp = list(input())
    arr.append(temp)
    if 'R' in temp:
        red = (i, temp.index('R'))
    if 'B' in temp:
        blue = (i, temp.index('B'))
        
print(bfs(red[0], red[1], blue[0], blue[1]))