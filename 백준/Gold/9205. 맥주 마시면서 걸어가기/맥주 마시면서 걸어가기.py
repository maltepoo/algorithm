def distance(frX, frY, toX, toY):
    return abs(frX - toX) + abs(frY - toY)

def bfs(st):
    q = [st]
    while q:
        i, j = q.pop()
        visited.add((i, j)) #현위치방문처리
        if distance(i, j, festival[0], festival[1]) <= 1000: #현재 위치-목적지가 가능하면
            return "happy"
        else: #불가능하면 갈수있는곳으로 이동하여 탐색
            for idx in range(len(store)):
                x, y = store[idx]
                if distance(i, j, x, y) <= 1000 and not (x, y) in visited:
                    q.append([x, y])
    return "sad"

t = int(input())
for _ in range(t):
    n = int(input())
    house = list(map(int, input().split(" ")))
    store = [list(map(int, input().split(" "))) for _ in range(n)]
    festival = list(map(int, input().split(" ")))

    visited = set()
    ans = bfs(house)
    print(ans)