def solution(prices):
    answer = []
    for j in range(len(prices)):
        cnt = 0
        for i in range(j+1, len(prices)):
            if prices[i] < prices[j]:
                break
            cnt += 1
        answer.append(cnt)
    return answer