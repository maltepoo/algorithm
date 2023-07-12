def solution(players, callings):
    rank = {} # 초기등수
    for i in range(len(players)):
        rank[players[i]] = i
    
    for c in callings:
        r = rank[c] # 현재등수(idx)
        target = players[r-1] # 추월대상
        players[r-1], players[r] = players[r], players[r-1] # 추월(swap)
        rank[c] -= 1 # 등수 재기록
        rank[target] += 1

    return sorted(rank,key=lambda x:rank[x])