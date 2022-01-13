#1204. 최빈수 구하기
T = int(input())
for _ in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    cnt = [0] * 101

    for i in scores:
        cnt[i] += 1

    ans = 0
    for j in range(1, 101):
        if cnt[ans] <= cnt[j]:
            ans = j

    print('#{} {}'.format(N, ans))