import heapq

# n = 지점개수, s = 출발지점, a = A의 도착지점, b = B의 도착지점
# fares = [c(노드1), d(노드2), f(비용)]
def solution(n, s, a, b, fares):
    answer = 0

    # 각각의 최단거리를 구한 후 겹치는부분의 요금을 빼기(다익스트라)
    graph =[[] for _ in range(n+1)]
    for n1, n2, f in fares:
        graph[n1].append((n2, f))
        graph[n2].append((n1, f))

    def dijkstra(s):
        dist = [int(1e9)] * (n + 1)
        q = []
        heapq.heappush(q, (0, s))

        dist[s] = 0
        while q:
            d, now = heapq.heappop(q)

            for b, c in graph[now]:
                cost = d + c
                if cost < dist[b]:
                    dist[b] = cost
                    heapq.heappush(q, (cost, b))
        return dist

    path = [0]
    totalFee = int(1e9)
    for i in range(1, n+1):
        path.append(dijkstra(i))

    for j in range(1, n+1):
        # 출발점 s ~ 임의의 i까지 거리(합승 또는 따로 가는 비용) + i에서 a + i에서 b
        totalFee = min(totalFee, path[s][j] + path[j][a] + path[j][b])

    return totalFee