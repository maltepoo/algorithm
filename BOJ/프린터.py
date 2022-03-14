from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    queue = deque([_ for _ in range(len(priorities))])
    while priorities:
        p, q = priorities.popleft(), queue.popleft()
        if len(priorities) == 0 or p >= max(priorities):
            answer += 1
            if q == location:
                return answer
        elif p < max(priorities):
            priorities.append(p)
            queue.append(q)
    return answer
print(solution([1], 0))