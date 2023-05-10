import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[y] = x
    else:
        parent[x] = y


v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
edges.sort(key=lambda x: x[2])
parent = [i for i in range(v+1)]

answer = 0
for s, e, c in edges:
    if find(s) != find(e): # 부모가 같지 않으면 싸이클이 없는 것
        union(s, e)
        answer += c
print(answer)