#1948. 날짜 계산기
T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T+1):
    m1, d1, m2, d2  = map(int,input().split())
    res = 0
    if m1 != m2:
        res = (days[m1-1]-d1) + d2
        for i in range(m1+1, m2):
            res += days[i-1]
    else:
        res += (d2-d1)
    print('#{} {}'.format(tc, res+1))