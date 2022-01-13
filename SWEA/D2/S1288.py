#1288. 새로운 불면증 치료법
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = N
    nums = [0 for _ in range(10)]
    while 0 in nums:
        for i in str(M):
            nums[int(i)] = 1
        M += N

    print('#{} {}'.format(tc, M-N))