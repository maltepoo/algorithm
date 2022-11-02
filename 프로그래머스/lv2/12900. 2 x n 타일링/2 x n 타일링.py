def solution(n):
    answer = 0
    f = [1, 1, 2, 3]
    
    def fibb(m):
        if m < len(f):
            return f[m-1]
        for i in range(4, m+1):
            f.append((f[i-1]+f[i-2])%1000000007)
        return f[m]
    
    answer = fibb(n)
    return answer