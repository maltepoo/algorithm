def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])

    """
    틀림
    st, ed = routes[0][0], routes[0][1]
    for s, e in routes:
        if st <= s <= ed or st <= e <= ed:
            continue
        else:
            answer += 1
            st = min(st, s, e)
            ed = max(ed, s, e)
    """
    cmr = routes[0][1]
    for s, e in routes:
        if s > cmr:
            answer += 1
            cmr = e
    return answer