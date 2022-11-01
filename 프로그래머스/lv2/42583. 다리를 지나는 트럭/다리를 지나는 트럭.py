def solution(bridge_length, weight, truck_weights):
    time = 0
    brdg = [0]*bridge_length
    brdgweight = 0
    while len(brdg) != 0:
        w = brdg.pop(0) # 트럭이 들어갈 공간을 만들어 줌
        brdgweight -= w
        if truck_weights: # 대기중인 트럭이 있으면
            if brdgweight+truck_weights[0] <= weight:
                # 대기중인 트럭+다리무게 합이 다리 최대 무게보다 적으면
                t = truck_weights.pop(0)
                brdg.append(t) # 대기중인 트럭 하나를 다리로
                brdgweight += t
            else:
                brdg.append(0) # 무게초과로 못들어간다면 0을 넣어 길이를 맞춤
        time += 1 # 한 사이클이 돌 때마다 시간은 1씩 ++
    return time