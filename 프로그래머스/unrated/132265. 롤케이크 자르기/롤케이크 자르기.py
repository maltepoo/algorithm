# 시간초과 --------
# def solution(topping):
#     answer = 0
#     for i in range(len(topping)):
#         x, y = set(topping[:i]), set(topping[i:])
#         if len(x) == len(y):
#             answer += 1
#     return answer

from collections import Counter
def solution(topping):
    answer = 0
    tp = Counter(topping)
    
    e = len(tp)
    st = set()
    
    for t in topping:
        if tp[t] > 0:
            st.add(t)
        tp[t] -= 1
        if tp[t] == 0:
            e -= 1
        if len(st) == e: answer += 1
    return answer
