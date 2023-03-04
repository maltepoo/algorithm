f, s, g, u, d = map(int, input().split(" ")) #전체층, 시작층, 목적층, 올라감,내려감
arr = [0]*(f+1)
visited = [0]*(f+1)

q = [s]
visited[s] = 1
while q:
    i = q.pop(0) #몇층
    if i == g:
        print(arr[g])
        break
    for k in [u, -d]: #위, 아래로 가봄
        ni = i+k
        if 0 < ni <= f and not visited[ni]:
            arr[ni] = arr[i]+1
            q.append(ni)
            visited[ni] = 1
if not arr[g] and not visited[g]:
    print("use the stairs")