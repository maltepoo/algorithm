# def solution(n, stations, w):
#     answer = 0
#     apt = [0] * (n)

#     for s in stations:
#         for i in range(s - w - 1, s + w):
#             if i < n:
#                 apt[i] = 1

#     r = 0
#     rg = (w * 2) + 1
#     for i in range(n):
#         if apt[i] == 1:
#             if r > 0:
#                 if r % rg == 0:
#                     answer += r // rg
#                 else:
#                     answer += (r // rg) + 1
#                 r = 0
#         else:
#             r += 1
#     if r > 0:
#         if r % rg == 0:
#             answer += r // rg
#         else:
#             answer += (r // rg) + 1
#     return answer

def distCalc(dist, r):
    if dist % r == 0:
        return dist // r
    else:
        return (dist // r) + 1

def solution(n, stations, w):
    answer = 0

    rg = (w*2)+1
    st = 0
    for s in stations:
        answer += distCalc(((s-w)-st)-1, rg)
        st = s+w

    if st < n:
        answer += distCalc(n-st, rg)
    return answer