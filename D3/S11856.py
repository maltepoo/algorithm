#11856. 반반
T = int(input())
for tc in range(1, T+1):
    S = list(input())
    res = 'No'
    s = set(S)
    cnt = 0
    if len(s) == 2:
        for i in S:
            if i == list(s)[0]:
                cnt += 1
    if cnt == 2:
        res = 'Yes'
    print('#{} {}'.format(tc, res))