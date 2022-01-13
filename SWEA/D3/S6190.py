#6190. 정곤이의 단조 증가하는 수
def is_danjo(res):
    stres = str(res)
    for i in range(len(stres)-1):
        if stres[i] > stres[i+1]:
            return False
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ns = list(map(int,input().split()))

    danjo = -1
    for i in range(N):
        for j in range(N):
            if i != j and is_danjo(ns[i]*ns[j]):
                if danjo < is_danjo(ns[i]*ns[j]):
                    danjo = is_danjo(ns[i]*ns[j])

    print('#{} {}'.format(tc, danjo))