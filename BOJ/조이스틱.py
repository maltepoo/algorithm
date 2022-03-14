def solution(name):
    # answer, move = 0, True
    # if name[1] == 'A':
    #     move = False
    # answer += min(ord(name[0]) - 65, 91 - ord(name[0]))
    # if move == True:
    #     for i in range(1, len(name)):
    #         if name[i] == 'A' and name[i:] in 'A':
    #             break
    #         answer += min(ord(name[i])-65, 91-ord(name[i]))
    #         answer += 1
    # else:
    #     for i in range(len(name)-1, 0, -1):
    #         if name[i] == 'A' and name[1:i] in 'A':
    #             break
    #         answer += min(ord(name[i])-65, 91-ord(name[i]))
    #         answer += 1
    return answer
print(solution("AAABBAB"))