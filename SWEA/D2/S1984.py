#1984. 중간 평균값 구하기
T = int(input())
for tc in range(1, T+1):
    nums = list(map(int,input().split()))
    maxV, minV = 0, 10001
    tot = 0
    for i in nums:
        if i > maxV:
            maxV = i
        if i < minV:
            minV = i
        tot += i
    ave = (tot-minV-maxV) / 8
    print('#{} {}'.format(tc, round(ave)))