def solution(ingredient):
    answer = 0
    st = []

    for i in ingredient:
        st.append(i)
        if i == 1 and len(st) >= 4:
            ham = st[-4:]
            if ham == [1, 2, 3, 1]:
                answer += 1
                for _ in range(4):
                    st.pop()
    return answer