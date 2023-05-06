import sys
input = sys.stdin.readline
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    x, y = find(x), find(y)
    parent[x] = y
V = int(input())
E = int(input())
adjList = [list(map(int, input().split())) for _ in range(E)]
adjList = sorted(adjList, key=lambda x: x[2]) # 가중치를 기준으로 정렬
parent = [i for i in range(0, V+2)]
ans = 0
for i in adjList:
    s, e, v = i
    if find(s) == find(e): #부모가 같으면(싸이클이 생기는지 판별)
        continue
    else:
        ans += v
        union(s, e)
print(ans)