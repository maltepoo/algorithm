def solution(survey, choices):
    answer = ''
    board = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    # RT, CF, JM, AN
    for i in range(len(survey)):
        type1, type2 = list(survey[i])
        if choices[i] < 4:
            board[type1] += 4-choices[i]
        elif choices[i] > 4:
            board[type2] += choices[i]-4
            
    scores = list(board.keys())
    for j in range(0, len(scores), 2):
        if board[scores[j]] >= board[scores[j+1]]:
            answer += scores[j]
        else: answer += scores[j+1]
    return answer