def solution(numbers, target):
    answer = 0

    def reculsion(idx,s):
        nonlocal answer # global X, local X
        if idx == len(numbers):
            if s == target:
                answer += 1
            return
        else:
            reculsion(idx+1,s+numbers[idx])
            reculsion(idx+1,s-numbers[idx])

    reculsion(0, 0)
    return answer