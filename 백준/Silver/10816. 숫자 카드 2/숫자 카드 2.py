n = int(input())
ns = list(map(int, input().split(" ")))
ans = {}
m = int(input())
targets = list(map(int, input().split(" ")))

for nm in ns:
    if nm in ans:
        ans[nm] += 1
    else:
        ans[nm] = 1
        
for tg in targets:
    if tg in ans:
        print(ans[tg], end=" ")
    else:
        print(0, end=" ")