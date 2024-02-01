def solution(weights):
    answer = 0
    wg = {}

    for i in weights:
        if i in wg:
            wg[i] += 1
        else:
            wg[i] = 1

    for i in wg:
        if wg[i] > 1:
            answer += (wg[i] * (wg[i] - 1)) / 2
        if i * 2 in wg:
            answer += wg[i] * wg[2 * i]
        if i * 2 / 3 in wg:
            answer += wg[i] * wg[i * 2 / 3]
        if i * 3 / 4 in wg:
            answer += wg[i] * wg[i * 3 / 4]
            
    return answer