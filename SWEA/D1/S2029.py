#2029. 몫과 나머지 출력하기
T = int(input())
for t in range(T):
    case = list(map(int,input().split()))
    print(f'#{t+1} {case[0] // case[1]} {case[0] % case[1]}')