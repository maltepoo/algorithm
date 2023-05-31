def solution(n, s):
    answer = []
    
    몫 = s // n
    if 몫 <= 0:
        return [-1]
    
    나머지 = s % n
    answer = [몫]*(n-나머지)
    for _ in range(나머지):
        answer.append(몫+1)
        
    return sorted(answer)