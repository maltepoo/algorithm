import heapq

def solution(operations):
    answer = []
    
    for op in operations:
        c, n = op.split()
        if c == 'I':
            heapq.heappush(answer, int(n))
        else:
            if len(answer) > 0:
                if n == '1':
                    answer.pop(answer.index(heapq.nlargest(1, answer)[0]))
                else:
                    heapq.heappop(answer)
    if not answer:
        answer = [0, 0]
    else:
        return [heapq.nlargest(1, answer)[0], answer[0]]
    return answer