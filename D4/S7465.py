#7465. 창용 마을 무리의 개수
def findset(x):
    if x == parent[x]:
        return x
    else:
        return findset(parent[x])

def union(x, y):
    parent[findset(x)] = findset(y)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    parent = [_ for _ in range(N+1)]
    for f in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)
    cnt = 0
    for i in range(1, N+1):
        if parent[i] == i:
            cnt += 1
    print('#{} {}'.format(tc, cnt))