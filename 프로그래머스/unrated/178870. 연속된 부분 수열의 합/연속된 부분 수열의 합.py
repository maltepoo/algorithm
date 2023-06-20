def solution(sequence, k):
    answer = []
    ps = [0]*(len(sequence)+1)

    for p in range(1, len(sequence)+1):
        ps[p] = sequence[p-1] + ps[p-1]

    i, j = 0, 0
    while i < len(ps) and j < len(ps):
        구간합 = ps[j] - ps[i]
        if 구간합 == k:
            answer.append([i, j-1])
            i += 1
        elif 구간합 < k:
            j += 1
        else:
            i += 1

    answer.sort(key=lambda x:(x[1]-x[0]))
    return answer[0]