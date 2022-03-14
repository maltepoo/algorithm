def solution(scoville, K):
    answer = 0
    while True:
        scoville.sort()
        p = scoville.pop(0)
        if len(scoville) <= 0:
            return -1
        if p >= K:
            break
        else:
            scoville.append(p+(scoville.pop(0)*2))
        answer+=1
    return answer
print(solution([1, 2, 3, 9, 10, 12], 7))