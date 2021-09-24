#1952. [모의 SW 역량테스트] 수영장
T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    p = [0]+list(map(int, input().split()))
    dp = [0]*13
    dp[1] = min(m, p[1]*d)
    dp[2] = dp[1] + min(m, p[2]*d)
    for i in range(3, 13):
        dp[i] = min(dp[i-3]+m3, dp[i-1]+p[i]*d, dp[i-1]+m)
    print('#{} {}'.format(tc, min(dp[-1], y)))

"""
fail 47/50 : 3/1개월 보다 1/3개월의 값이 이득일 경우를 고려하지 못함
T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    p = list(map(int, input().split()))
    tot = [0]*12
    res = 0
    for i in range(12):
        if p[i]*d > m:
            tot[i] = m
        else:
            tot[i] = p[i]*d
    res = sum(tot)
    for j in range(10):
        if sum(tot[j:j+3]) > m3 and not 1 in tot[j:j+3]:
            tot[j], tot[j+1], tot[j+2] = 1, 1, 1
    if 1 in tot:
        res = (tot.count(1)//3)*m3+sum(tot)-tot.count(1)
    else:
        res = sum(tot)
    if res > y: res = y
    print('#{} {}'.format(tc, res))
"""