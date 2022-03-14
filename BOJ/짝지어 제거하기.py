def solution(s):
    s = list(s)
    idx = 0
    while idx < len(s)-1:
        if s[idx] == s[idx+1]:
            s.pop(idx)
            s.pop(idx-1)
            idx = 0
        else: idx += 1
    return 1 if idx == 0 else 0
print(solution("cdcd"))