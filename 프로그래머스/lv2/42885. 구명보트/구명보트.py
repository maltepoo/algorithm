def solution(people, limit):
    answer = 0
    p = sorted(people)
    i, j = 0, len(p)-1
    while i <= j:
        if p[i]+p[j] > limit:
            j -= 1
        else:
            i += 1
            j -= 1
        answer += 1
    return answer