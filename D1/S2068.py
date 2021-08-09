#2068. 최대수 구하기
T = int(input())
for t in range(T):
    case = list(map(int,input().split()))
    print(f'#{t+1} {max(case)}')