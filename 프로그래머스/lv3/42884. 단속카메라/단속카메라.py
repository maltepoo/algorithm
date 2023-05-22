def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    st, ed = routes[0][0], routes[0][1]
    for s, e in routes:
        if s > ed:  # 시작점(s)이 이전 구간의 끝점(ed)보다 큰 경우
            answer += 1
            st = s
            ed = e
        else:  # 시작점(s)이 이전 구간의 끝점(ed)보다 작은 경우
            st = max(st, s)
            ed = min(ed, e)
    return answer