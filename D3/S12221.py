#12221. 구구단2
T = int(input())
for tc in range(1, T+1):
    A, B = map(int,input().split())
    res = 0
    if A >= 10 or B >= 10:
        res = -1
    else:
        res = A*B
    print('#{} {}'.format(tc, res))