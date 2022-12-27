def countProduct(w, d):
    if w == d:
        return True
    return False

def solution(want, number, discount):
    answer = 0

    for i in range(len(want)):
        if number[i] > 1:
            for k in range(number[i]-1):
                want.append(want[i])
                
    for j in range(len(discount)-9):
        if countProduct(sorted(want), sorted(discount[j:j+10])):
            answer += 1
    return answer