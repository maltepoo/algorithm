def solution(N, stages):
    stages.sort()

    answer = []
    uncleared = {i: 0 for i in range(0, N+2)} # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수(1)
    cleared = [0 for _ in range(0, N+2)] # 스테이지에 도달한 플레이어 수(2)
    # 실패율 = (1)÷(2)

    for s in stages:
        uncleared[int(s)] += 1

    cleared[N+1] = uncleared[N+1]
    for i in range(N, 0, -1):
        cleared[i] = (cleared[i+1] + uncleared[i])

    for j in range(1, N+1):
        if cleared[j] != 0:
            answer.append([j, uncleared[j] / cleared[j]])
        else:
            answer.append([j, 0])

    answer.sort(key=lambda x:x[1], reverse=True)
    return [k[0] for k in answer]