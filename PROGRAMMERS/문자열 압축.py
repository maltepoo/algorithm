def solution(s):
    answer = 9999                                   # 문자열 중 가장 짧은 것의 길이
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):               # i개의 문자열로 쪼개어 탐색
        res = ''                                    # 문자열 갱신
        temp = s[:i]                                # 비교대상
        cnt = 1                                     # 압축횟수
        for j in range(i, len(s), i):
            if temp == s[j:i+j]:                    # 비교대상과 같으면 압축
                cnt += 1
            else:                                   # 다른 문자열이고
                if cnt != 1:                        # 압축된 이력이 있으면
                    res = res + str(cnt)+temp       # 압축된 횟수와 현재 글자를 반영하여 탐색할 문자열 갱신
                else:
                    res = res + temp
                temp = s[j:j+i]                     # 비교대상 다음문자열으로 변경
                cnt = 1
        if cnt != 1:                                # 마지막 남은 한 문자열이 있으면 붙여주기
            res = res+str(cnt)+temp
        else: res = res + temp
        answer = min(answer,len(res))
    return answer
print(solution("aabbaccc"))