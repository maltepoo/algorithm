"""
우선순위 큐 구현문제
"""
def solution(priorities, location):
    answer = 0
    queue = [_ for _ in range(len(priorities))] # 인쇄목록
    while priorities:
        p, q = priorities.pop(0), queue.pop(0)
        if len(priorities) == 0 or p >= max(priorities): # 현재 인쇄X 면 순서 ++
            answer += 1
            if q == location: # 인쇄순서가 나오면 종료
                return answer
        elif p < max(priorities): # 다시 큐로
            priorities.append(p)
            queue.append(q)
    return answer