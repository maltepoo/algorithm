import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    r, n = map(int, sys.stdin.readline().split())
    tree[r].append(n)
    tree[n].append(r)

def find_parent(node):
    for nd in tree[node]:
        if parents[nd] == 0:
            parents[nd] = node
            find_parent(nd)
    return
find_parent(1)
for p in parents[2:]:
    print(p)