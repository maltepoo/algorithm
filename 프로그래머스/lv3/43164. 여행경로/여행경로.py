def solution(tickets):
    way_dict = {}
    for (st, ed) in tickets:
        if st in way_dict:
            way_dict[st].append(ed)
        else: way_dict[st] = [ed]
    for k in way_dict.keys():
        way_dict[k].sort(reverse=True) #역순으로 정렬하면 사전순으로 스택에 넣을 수 있다

    st = ["ICN"] #경로는 무조건 ICN부터 시작
    path = []
    while st:
        fr = st.pop()
        if fr in way_dict and way_dict[fr]: #갈곳이 있으면
            st.append(fr)
            st.append(way_dict[fr].pop())
        else: #더이상 갈곳이 없으면 path에 넣는다
            path.append(fr)
    return(path[::-1])