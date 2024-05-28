def solution(string):
    answer = []
    dictionary = {}
    
    for i in range(len(string)):
        if not string[i] in dictionary:
            dictionary[string[i]] = i
            answer.append(-1)
        else:
            loc_bf = dictionary[string[i]]
            answer.append(i-loc_bf)
            dictionary[string[i]] = i
            
    return answer