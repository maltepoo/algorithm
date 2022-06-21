# BFS
def check_kb(v):
    q = [v]
    visited[v] = 1
    while q:
        tg = q.pop(0)
        for i in kb[tg]:
            if not visited[i]:
                visited[i] = visited[tg] + 1
                q.append(i)

n, m = map(int, input().split())
kb = [[] for _ in range(n+1)]
for fn in range(m):
    a, b = map(int, input().split())
    kb[a].append(b)
    kb[b].append(a)
kb_num = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    check_kb(i)
    kb_num.append(sum(visited))
print(kb_num.index(min(kb_num))+1)