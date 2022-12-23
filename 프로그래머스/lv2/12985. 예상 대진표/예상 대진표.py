def solution(n,a,b):
    라운드 = 1
    players = [i+1 for i in range(n)]
    while len(players) > 2:
        fight = []
        for j in range(0, len(players), 2):
            if sorted([players[j], players[j+1]]) == sorted([a, b]):
                return 라운드
            if players[j+1] == a or players[j+1] == b:
                fight.append(players[j+1])
            else: fight.append(players[j])
        라운드 += 1
        players = fight
    return 라운드