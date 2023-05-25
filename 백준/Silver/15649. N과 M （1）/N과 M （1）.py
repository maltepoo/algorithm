n, m = map(int, input().split())
arr = []
visited = [0]*(n+1)

def perm():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        perm()
        arr.pop()
        visited[i] = False
perm()