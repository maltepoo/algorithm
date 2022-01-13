#7087. 문제 제목 붙이기
T = int(input())
ap = [chr(i) for i in range(65, 91)]
for tc in range(1, T+1):
    N = int(input())
    words = [input() for _ in range(N)]

    cnt = 0
    idx = 0
    find = 0
    while find < len(words):
        for w in words:
            if w[0] == ap[idx]:
                cnt += 1
                idx += 1
        find += 1
    print('#{} {}'.format(tc, cnt))