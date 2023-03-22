n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드 와샬 알고리즘: 모든 정점에서 다른 모든 정점으로부터의 최단경로를 구함
for k in range(n): #시작 i, 도착 j, 거치는 간선 k
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
for g in graph:
    print(*g)