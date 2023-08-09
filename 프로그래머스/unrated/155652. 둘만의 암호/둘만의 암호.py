def solution(s, skip, index):
    answer = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for sk in skip:
        alpha = alpha.replace(sk, "")
    
    length = len(alpha)
    for st in s:
        answer += alpha[(alpha.index(st)+index) % length]
        
    return answer