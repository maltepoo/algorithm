def solution(msg):
    dicts = {}
    for i in range(1, 27):
        dicts[chr(64 + i)] = i

    answer = []
    st, ed = 0, 1
    while ed < len(msg)+1: # 슬라이싱을 위해 end를 +1
        w = msg[st:ed]
        if w in dicts: # 사전O idx + 1 하여 다음 단어 검증
            ed += 1
        else:
            answer.append(dicts[w[:-1]]) # 사전X 색인번호 출력
            dicts[w] = len(dicts)+1 # 새로운단어 사전 등록
            st += (len(w)-1) # 다음 단어 찾기위해 idx 초기화
            ed = st+1
    answer.append(dicts[w])
    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))