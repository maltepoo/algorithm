import heapq
def solution(n, works):
    answer = 0
    
#     while n > 0:
#         works[works.index(max(works))] -= 1
#         n -= 1
    
#     for i in range(len(works)):
#         if works[i] > 0:
#             answer += works[i]**2
    
    rev_works = list(map(lambda x: x*-1, works))
    heapq.heapify(rev_works)
    
    while n > 0:
        h = heapq.heappop(rev_works)
        heapq.heappush(rev_works, h+1)
        n -= 1
        
    for i in range(len(rev_works)):
        num = rev_works[i]*-1
        if num > 0:
            answer += num**2
    return answer