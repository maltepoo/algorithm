import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

n, m = map(int, input().split())
answer = 0
parent = [i for i in range(n+1)]
for i in range(1, m+1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        answer = i
        break
    else:
        union(a, b)
print(answer)