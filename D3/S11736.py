#11736. 평범한 숫자
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pi = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if 0 <= i-1 < N and 0 <= i+1 < N:
            if pi[i-1] < pi[i] < pi[i+1] or pi[i-1] > pi[i] > pi[i+1]:
                cnt+=1
    print('#{} {}'.format(tc, cnt))