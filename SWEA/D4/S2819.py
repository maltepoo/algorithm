#2819. 격자판의 숫자 이어 붙이기
def find_dfs(i, j, n):
    if len(n) == 7:
        number.add(n)
        return
    for k in range(4):
        ni, nj = i+dir[k][0], j+dir[k][1]
        if 0<=ni<4 and 0<=nj<4:
            find_dfs(ni, nj, n+arr[ni][nj])

for tc in range(1, int(input())+1):
    arr = [list(input().split()) for _ in range(4)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    number = set()
    for i in range(4):
        for j in range(4):
            find_dfs(i, j, arr[i][j])

    print('#{} {}'.format(tc, len(number)))