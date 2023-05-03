def solution(n):
    answer = 0
    arr = [0]*n # i의 위치에 j를 놓음
    
    def isPromising(x, y):        
        # 1. 같은 행에 q가 없을 때
        # 2. 왼, 오 대각선에 q가 없을 때
        # 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선임
        for j in range(x):
            if arr[j] == y or x-j == abs(arr[x] - arr[j]):
                return False
        return True
    
    def nq(x):
        cnt = 0
        if x == n:
            return 1
        
        for i in range(n):
            # x열에 i를 놓아봄
            arr[x] = i
            if isPromising(x, i): # 놓을 수 있으면
                cnt += nq(x+1)
        return cnt
    
    answer = nq(0)
    return answer