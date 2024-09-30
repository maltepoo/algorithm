def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    if len(score) < m:
        return answer
    
    n = len(score) // m # 상자개수
    for i in range(0, len(score)-m+1, m):
        answer += (score[i+m-1]*m)
    return answer