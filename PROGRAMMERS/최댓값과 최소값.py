def solution(s):
    answer = ''
    s = s.split(' ')
    maxN, minN = -99999, 99999
    for i in s:
        n = int(i)
        if n >= maxN:
            maxN = n
        if minN >= n:
            minN = n
    answer = "{} {}".format(minN, maxN)
    return answer