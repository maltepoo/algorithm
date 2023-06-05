def solution(numbers):
    answer = [-1] * len(numbers)
    st = [] # 인덱스를 쌓음

    for i in range(len(numbers)):
        while st and numbers[st[-1]] < numbers[i]: # 스택에 쌓인 인덱스와 현재 수를 비교
            answer[st.pop()] = numbers[i]
        st.append(i)
    return answer