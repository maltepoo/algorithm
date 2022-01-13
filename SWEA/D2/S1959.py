#1959. 두 개의 숫자열
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))

    res = -999999
    if N > M:
        N, M, ai, bj = M, N, bj, ai
    for i in range(M-N+1):
        tot = 0
        for k in range(N):
            tot += ai[k]*bj[i+k]
        if res < tot:
            res = tot
    print('#{} {}'.format(tc, res))