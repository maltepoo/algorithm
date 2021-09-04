#1946. 간단한 압축 풀기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    res = []
    for ar in arr:
        res.append(ar[0]*int(ar[1]))
    nres = ''.join(res)

    print('#{}'.format(tc))
    for i in range(0, len(nres), 10):
        print(nres[i:i+10])