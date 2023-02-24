import sys
input = sys.stdin.readline
n, m = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))

s, e = 0, max(trees)-1
ans = 0
while s <= e:
    h = (s+e)//2
    treesum = 0
    for i in range(n):
        left = trees[i] - h
        if left > 0:
            treesum += left
    if treesum >= m:
        s = h+1
    else:
        e = h-1
print(e)