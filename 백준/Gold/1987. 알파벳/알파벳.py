r, c = map(int, input().split(" "))
arr = [list(input()) for _ in range(r)]
word = 0
visited = [0]*26

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(x, y, d):
    global word
    if word < d:
        word = d

    for k in range(4):
        nx, ny = x+dirs[k][0], y+dirs[k][1]
        if 0<=nx<r and 0<=ny<c and visited[ord(arr[nx][ny])-65] == 0:
            visited[ord(arr[nx][ny]) - 65] = 1
            dfs(nx, ny, d+1)
            visited[ord(arr[nx][ny]) - 65] = 0
    return

visited[ord(arr[0][0]) - 65] = 1
dfs(0, 0, 1)
print(word)