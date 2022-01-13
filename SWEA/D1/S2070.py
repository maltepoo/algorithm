#2070. 큰 놈, 작은 놈, 같은 놈
T = int(input())
for t in range(T):
    case = list(map(int,input().split()))
    if case[0] > case[-1]:
        print(f'#{t+1} >')
    elif case[0] == case[-1]:
        print(f'#{t+1} =')
    elif case[0] < case[-1]:
        print(f'#{t+1} <')