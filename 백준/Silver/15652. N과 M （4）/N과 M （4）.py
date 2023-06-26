n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
# visited = [False]*n

def perm(lst, d, l):
    if d == m:
        print(*lst)
        return
    for i in range(n):
        if arr[i] >= l:
            lst.append(arr[i])
            perm(lst, d+1, arr[i])
            lst.pop()

perm([], 0, 1)