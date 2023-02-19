n, r, c = map(int, input().split(" "))
size = 2**n

cnt = 0
def runZ(i, j, N):
    global cnt
    if i==r and j==c:
        print(cnt)
        exit(0)

    if not (i <= r < i+N and j <= c < j+N): #r,c 범위에 없으면 패스
        cnt += N*N
        return

    runZ(i, j, N//2) #1사분면
    runZ(i, j+N//2, N//2) #2사분면
    runZ(i+N//2, j, N//2) #3사분면
    runZ(i+N//2, j+N//2, N//2) #4사분면

runZ(0, 0, size)
"""
arr에 하나하나 적어가며 풀이하면 최악 1073741824번 연산
= 위치를 먼저 찾은 후 그부분만 z 하면 됨
"""