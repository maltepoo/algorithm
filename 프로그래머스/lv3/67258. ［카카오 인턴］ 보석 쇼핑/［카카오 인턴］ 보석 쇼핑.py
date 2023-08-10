"""
풀이 참고 : 카카오 문제해설
https://tech.kakao.com/2020/07/01/2020-internship-test/
"""
def solution(gems):
    answer = [0, len(gems)-1]
    
    gem_type_size = len(set(gems)) # 보석 최대 종류 수
    gem_diff = {gems[0]: 1} #보석이름 : 빈도수
    
    l, r = 0, 0
    while l < len(gems) and r < len(gems):
        if len(gem_diff) < gem_type_size: # 보석의 종류가 적을때
            r += 1
            if r == len(gems):
                break
            if gems[r] in gem_diff:
                gem_diff[gems[r]] += 1
            else:
                gem_diff[gems[r]] = 1
        else: # 보석의 종류가 같을때
            if answer[1] - answer[0] > r - l: # 보석 종류가 같을 때 더 좋은답인지 체크
                answer = [l, r]
            
            if gem_diff[gems[l]] == 1:
                del gem_diff[gems[l]] # 1인 경우 줄일 때 보석의 종류를 삭제시킴
            else:
                gem_diff[gems[l]] -= 1
                
            l += 1
    return [answer[0]+1, answer[1]+1]