def solution(sticker):
    # 크게 0부터 떼는 경우, 1부터 떼는 경우 두가지의 경우
    size = len(sticker)
    if size == 1:
        return sticker[0]
    
    dp1 = [0]*size
    dp2 = [0]*size
    
    dp1[0] = sticker[0] # 0 스티커를 뗌
    dp1[1] = sticker[0] # 1번째는 0스티커를 뗐으니 뗄 수 없어 최대값은 sticker[0]
    
    dp2[0] = 0 # 1 스티커를 뗄것이니 0번째는 뗄 수 없음
    dp2[1] = sticker[1] # 1을 떼는 경우
    
    for i in range(2, size-1): # 0번째를 떼서 마지막 스티커를 사용할 수 없음
        dp1[i] = max(dp1[i-2]+sticker[i], dp1[i-1])
    
    for j in range(2, size):
        dp2[j] = max(dp2[j-2]+sticker[j], dp2[j-1])
    
    """
    dp를 활용하는 이유는 스티커를 전에 떼었어도 떼는경우, 안떼는경우 둘다 봐야 하기 때문에
    단순 0, 1번부터 시작해 더해가는 반복문 더하기는 맞지 않을 수 있음
    tc 33의 런타임 에러는 size가 1일 경우
    """
    return max(dp1[-2], dp2[-1])