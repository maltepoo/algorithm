n = int(input())
res = 0
loc = [0]*n
def isPromising(i):
    for j in range(i):
        if loc[i] == loc[j] or abs(i - j) == abs(loc[i] - loc[j]):
            return False
    return True

def backTrack(x): #열 탐색
    global res
    if n == x: # 끝까지 도달하면
        res += 1
        return
    else:
        for i in range(n): #행 탐색
            loc[x] = i
            if isPromising(x):
                backTrack(x+1)
backTrack(0)
print(res)