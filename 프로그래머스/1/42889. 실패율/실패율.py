def solution(N, stages):
    answer = {}
    people = len(stages)
    for i in range(1, N+1):
        if people != 0:
            answer[i] = stages.count(i) / people
            people -= stages.count(i)
        else:
            answer[i] = 0
    return sorted(answer, key=lambda x: answer[x], reverse=True)