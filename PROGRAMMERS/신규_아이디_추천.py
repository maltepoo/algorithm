def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    for id in new_id:
        if id.isalnum() or (id in '-_.'):
            answer += id
    while '..' in answer:
        answer = answer.replace('..', '.')
    if len(answer) >= 1:
        if answer[0] == '.' or answer[-1] == '.':
            answer = answer.strip('.')
    if answer == '': answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.': answer = answer[:-1]
    if len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))
    return answer