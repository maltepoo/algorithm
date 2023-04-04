def solution(babbling):
    answer = 0
    available = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        for a in available:
            babbling[i] = babbling[i].replace(a, "-")
        if not babbling[i].replace('-', ""):
            answer += 1
    return answer