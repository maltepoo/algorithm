def solution(participant, completion):
    answer = ''
    
    c_list = dict()
    for c in completion:
        if c in c_list:
            c_list[c] += 1
        else: c_list[c] = 1
    
    for p in participant:
        if p not in c_list or c_list[p] == 0:
            answer = p
            break
        c_list[p] -= 1
        
    return answer