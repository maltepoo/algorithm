#2072. 홀수만 더하기
T = int(input())
for t in range(T):
    res = 0
    case = list(map(int,input().split()))
    for c in case:
        if c % 2 == 1:
            res += c
    print(f'#{t+1} {res}')