import itertools
def solution(number):
    answer = 0
    comb = list(itertools.combinations(number, 3))
    for i in comb:
        if sum(i) == 0:
            answer += 1
    return answer