def checkString(st):
    stack = []
    for l in st:
        if l in ['(', '[', '{']:
            stack.append(l)
        else:
            if stack:
                if l == ')' and stack[-1] == '(':
                    stack.pop()
                elif l == ']' and stack[-1] == '[':
                    stack.pop()
                elif l == '}' and stack[-1] == '{':
                    stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        ss = s[i:]+s[:i]
        if checkString(ss):
            answer += 1
    return answer