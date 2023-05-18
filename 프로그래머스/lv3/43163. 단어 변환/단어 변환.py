def dfs(s, wds, cnt, tg):
    global answer
    if s == tg:
        answer = min(cnt, answer)
        return
    for w in wds:
        if isOneDiff(s, w):
            wds.remove(w)
            dfs(w, wds, cnt + 1, tg)
            wds.append(w)

def isOneDiff(s, w):
    diff = 0
    for i in range(len(s)):
        if s[i] != w[i]:
            diff += 1
    if diff == 1:
        return True
    return False


answer = 9999999999
def solution(begin, target, words):
    dfs(begin, words, 0, target)
    if answer >= 9999999999:
        return 0
    return answer