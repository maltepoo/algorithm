import sys
input = sys.stdin.readline
a, b = map(int, input().split())
res = 0

def dfs(depth, l, v):
    global res
    if depth == l:
        if a <= int(v) <= b:
            res += 1
        return
    dfs(depth, l+1, v+'4')
    dfs(depth, l+1, v+'7')

maxdepth = len(str(b))
for i in range(1, maxdepth+1):
    dfs(i, 0, '')

print(res)