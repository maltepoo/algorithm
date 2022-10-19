# row > network
# column > connection

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            dfs(i, n, computers, visited)
            answer += 1
    return answer

def dfs(v, n, computers, visited):
    visited[v] = True
    for c in range(n):
        if computers[v][c] == 1 and v != c and visited[c] == False:
            # 연결된 컴퓨터가 있고 computer[v][v] 가 아니고 방문기록이 없으면
            dfs(c, n, computers, visited)