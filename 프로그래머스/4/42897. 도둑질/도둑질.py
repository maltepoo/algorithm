def solution(money):
    dp1 = [0]*(len(money)+1) # 첫번쨰집 무조건 터는 경우
    dp1[0] = money[0]
    
    dp2 = [0]*(len(money)+1) # 첫번째집 안터는경우
    dp2[1] = money[1]
    
    for i in range(1, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
    
    for j in range(2, len(money)):
        dp2[j] = max(dp2[j-1], dp2[j-2]+money[j])
    
    return max(max(dp1), max(dp2))