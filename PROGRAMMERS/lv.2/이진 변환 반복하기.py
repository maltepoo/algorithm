def solution(s):
    answer = [0, 0]
    while s != '1':
        temp = ''
        for i in s:
            if i == '0':
                answer[1] += 1
            else:
                temp += '1'
        s = str(bin(len(temp)))[2:]
        answer[0] += 1
    return answer