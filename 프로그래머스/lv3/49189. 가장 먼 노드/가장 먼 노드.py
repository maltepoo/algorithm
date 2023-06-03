from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        i, j = e
        graph[i].append(j)
        graph[j].append(i)
    
    q = deque([1])
    dist = [-1]*(n+1) # 1에서의 거리를 기록
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dist[i] == -1: # 방문하지 않은 노드면
                q.append(i)
                dist[i] = dist[now]+1 # 지금까지 온 거리 + 1
                
    answer = dist[2:].count(max(dist[2:]))
    return answer