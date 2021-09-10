#1284. 수도 요금 경쟁
T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    """
    P: a사 리터당 요금
    Q: r리터 이하 요금
    R: b사의 요금전환 기준 리터
    S: r리터 이상 요금
    W: 종민이가 쓰는 수도 양
    """
    a, b = P*W, 0
    if R >= W:
        b = Q
    else:
        b = Q+(S*(W-R))

    print('#{} {}'.format(tc, min(a,b)))
