answer = []

def hanoi(n, st, ed, via):
    if n == 1:
        answer.append([st, ed])
    else:
        hanoi(n-1, st, via, ed)
        answer.append([st, ed])
        hanoi(n-1, via, ed, st)


def solution(n):
    hanoi(n, 1, 3, 2)
    return answer