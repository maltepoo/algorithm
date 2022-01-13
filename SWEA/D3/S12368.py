#12368. 24시간
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    res = a+b
    while res >= 24:
        res -= 24
    print('#{} {}'.format(tc, res))