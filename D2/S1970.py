#1970. 쉬운 거스름돈
T = int(input())
for tc in range(1, T+1):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0]*len(money)
    N = int(input())

    for m in range(len(money)):
        cnt[m] += N//money[m]
        N %= money[m]

    print('#{} '.format(tc))
    print(*cnt)