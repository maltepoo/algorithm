def solution(N, road, K):
    arr = [[] for _ in range(N + 1)]
    dist = [float('inf')] * (N + 1)

    for a, b, c in road:
        arr[a].append((b, c))
        arr[b].append((a, c))

    st = [[1, 0]] # 출발노드, 비용
    dist[1] = 0
    while st:
        nd, ct = st.pop() # 현재 방문한 노드
        for node, cost in arr[nd]: # 현 노드에서 갈수 있는 곳들 순회
            if ct+cost < dist[node]:
                dist[node] = ct+cost
                st.append((node, ct+cost))
    return len(list(filter(lambda x: (x <= K), dist)))