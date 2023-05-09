import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0 # 몇 번 dfs를 도는지 = 연결 요소의 개수

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    st = [v]
    while st:
        nd = st.pop()
        visited[nd] = 1
        for i in graph[nd]:
            if not visited[i]:
                st.append(i)
    return

for i in range(1, n+1): # 방문한적 없는 노드로 dfs를 도는 회수가 연결 요소의 개수가 된다
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)