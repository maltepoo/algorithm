from collections import deque
def solution(queue1, queue2):
    que1, que2 = deque(queue1), deque(queue2)
    sumq1, sumq2 = sum(que1), sum(que2)
    limit = len(queue1)*4
    cnt = 0
    while sumq1 != sumq2:
        if sumq1 > sumq2:
            q1 = que1.popleft()
            sumq1 -= q1
            sumq2 += q1
            que2.append(q1)
        else:
            q2 = que2.popleft()
            sumq2 -= q2
            sumq1 += q2
            que1.append(q2)
        cnt += 1
        if cnt >= limit:
            return -1
    return cnt
print('answer = {}'.format(solution([1, 2, 1, 2], [1, 10, 1, 2])))