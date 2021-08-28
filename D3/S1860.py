#1860. 진기의 최고급 붕어빵
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split()) #N명 에게 M초만에 K개의 붕어빵을 만들어 준다
    cos = list(map(int,input().split())) #3 4이면 3초 4초에 손님이 각각 도착

    cos.sort()
    result = "Possible"

    for i in range(N):
        fish = cos[i] // M * K
        if fish < i + 1:
            result = "Impossible"

    print('#{} {}'.format(tc, result))