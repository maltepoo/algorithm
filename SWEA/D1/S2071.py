#2071. 평균값 구하기
T = int(input())
for t in range(T):
    case = list(map(int,input().split()))
    print(f'#{t+1} {round(sum(case)/10)}')