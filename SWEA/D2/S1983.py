#1983. 조교의 성적 매기기
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    score = [list(map(int,input().split())) for _ in range(N)]
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    total = []

    for i in score:
        tot = i[0] * 0.35 + i[1] * 0.45 + i[2] * 0.20
        total.append(round(tot,2))

    target = total[K-1]
    total.sort(reverse=True)

    idx = total.index(target)+1
    if idx % (N//10):
        res = idx // (N//10)
    else:
        res = idx // (N//10)-1

    print('#{} {}'.format(tc, grades[res]))