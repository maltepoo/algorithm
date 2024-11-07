def divisor_count(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        divisor = divisor_count(n)
        if divisor % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer