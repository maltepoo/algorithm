#3431. 준환이의 운동관리
T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())
    res = 0
    if X < L:
        res = L-X
    elif U <= X:
        res = -1
    print('#{} {}'.format(tc, res))