#1486. 장훈이의 높은 선반
for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    hi = list(map(int, input().split()))
    ps_li = []
    for i in range(0, (1<<N)):
        p = 0
        for j in range(0, N):
            if i & (1 << j):
                p += hi[j]
        if p >= B:
            ps_li.append(p)

    print('#{} {}'.format(tc, min(ps_li)-B))