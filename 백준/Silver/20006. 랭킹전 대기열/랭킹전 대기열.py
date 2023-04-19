p, m = map(int, input().split())
players = [list(input().split()) for _ in range(p)]
games = []

for ply in players:
    flag = True
    lv, n = ply
    if not games: # 참여 가능한 방이 하나도 없으면
        games.append([int(lv), [ply]])
    else:
        for g in games: # 모든 방 순회
            if g[0]-10 <= int(lv) <= g[0]+10 and len(g[1]) < m: # 참여 가능한 방 들어가기
                g[1].append(ply)
                flag = False
                break
        if flag:
            games.append([int(lv), [ply]]) # 모든 방을 돌았는데도 참여 가능한 방이 없으면 방 생성

for g in games:
    long = len(g[1])
    g[1].sort(key=lambda x:x[1])
    if long == m:
        print("Started!")
        for j in range(m):
            print(*g[1][j])
    else:
        print("Waiting!")
        for j in range(long):
            print(*g[1][j])