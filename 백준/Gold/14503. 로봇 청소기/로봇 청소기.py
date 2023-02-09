dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] #북동남서 0-3

n, m = map(int, input().split(" "))
r, c, d = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for _ in range(n)]

cnt = 0
turn = 0
while True:
    if arr[r][c] == 0: #현재칸청소
        cnt += 1
        arr[r][c] = -cnt

    for _ in range(4): #4번회전
        dir = (d+3)%4
        nr, nc = r+dirs[dir][0], c+dirs[dir][1]
        if arr[nr][nc] == 0: #왼쪽봤을때 청소가능하면
            d = dir #그방향으로 회전
            r, c = nr, nc #그 방향으로 한칸이동
            turn = 0
            break
        else: #청소 불가능하면
            d = dir #왼쪽으로 한번 회전 후
            turn += 1
    if turn == 4: #네방향 모두 청소/벽이면
    #모두 봤을때 청소, 벽이면 바라보는 방향을 유지한채로 한칸 후진하고 다시 현재방향 기준으로 왼쪽부터 탐색
        if arr[r-dirs[d][0]][c-dirs[d][1]] == 1:
            break
        else:
            r, c = r-dirs[d][0], c-dirs[d][1] #후진
            turn = 0
print(cnt)