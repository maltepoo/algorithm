#14716. 현수막
dirs = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]
def dfs(i, j):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        arr[i][j] = 0
        for k in range(8):
            ni, nj = i + dirs[k][0], j + dirs[k][1]
            if 0<=ni<H and 0<=nj<W and arr[ni][nj] == 1:
                stack.append((ni, nj))

H, W = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(H))
num = 0
for i in range(H):
    for j in range(W):
        if arr[i][j] == 1:
            num += 1
            dfs(i, j)
print(num)