#5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
def dfs(n, tot):
    global res
    if tot > res:
        return
    if n == N:
        if tot < res:
            res = tot
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, tot+arr[n][i])
            visited[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    res = 9999
    dfs(0,0)
    print('#{} {}'.format(tc, res))