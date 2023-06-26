n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
visited = [False]*n

def perm(lst, d):
    if d == m:
        print(*lst)
        return
    for i in range(n):
        lst.append(arr[i])
        perm(lst, d+1)
        lst.pop()

perm([], 0)