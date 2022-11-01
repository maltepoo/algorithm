def fibb(m):
    f = [0, 1]
    if m == 2:
        return f[m-1]
    for i in range(2, m+1):
        f.append(f[i-1]+f[i-2])
    return f[m]

def solution(n):
    answer = fibb(n) % 1234567
    return answer