#1945. 간단한 소인수분해
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    div = [2, 3, 5, 7, 11]
    ans = [0] * 5

    for idx in range(len(div)):
        while 1:
            if N % div[idx] == 0:
                N = N//div[idx]
                ans[idx] += 1
            else:
                break

    print('#{} {}'.format(tc, ' '.join(map(str,ans))))