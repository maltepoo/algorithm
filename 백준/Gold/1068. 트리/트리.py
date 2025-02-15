n = int(input())
parents = list(map(int, input().split()))
d = int(input())

graph = [[] for _ in range(n)]
root = -1
for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        graph[parents[i]].append(i)

# 노드 지우기
graph[d] = []
for j in range(n):
    if d in graph[j]:
        graph[j].remove(d)


# 리프노드 개수세기
def count_leaves(node):
    if not graph[node]:
        return 1
    return sum(count_leaves(child) for child in graph[node])


if d == root:
    print(0)
else:
    print(count_leaves(root))