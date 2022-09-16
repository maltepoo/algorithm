def solution(s):
    answer = ''
    s = s.lower()
    if s[0].isalpha():
        answer = s[0].upper()
    else: answer = s[0]
    for i in range(1, len(s)):
        if s[i-1] == " ":
            answer += s[i].upper()
        else: answer += s[i]
    return answer

def solution(s):
    answer = ''
    s = s.split(" ")
    for i in s:
        answer += i.capitalize()
        answer += " "
    return answer[:-1]