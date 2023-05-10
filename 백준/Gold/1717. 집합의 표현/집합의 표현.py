import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b: # 일반적으로 수가 작은 값으로 합침
        parent[b] = a
    else:
        parent[a] = b


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x]) # 압축
    return parent[x]


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1: # 원소가 같은 집합에 포함되어있는지 확인
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")
    elif a == 0: # b, c 수가 들어있는 집합을 합침
        union(b, c)