n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
visited = [False]*n

def perm(lst, d, loc):
    if d == m:
        print(*lst)
        return
    for i in range(loc, n):
        if not visited[i]:
            lst.append(arr[i])
            visited[i] = True
            perm(lst, d+1, i)
            visited[i] = False
            lst.pop()

perm([], 0, 0)