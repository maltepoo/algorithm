n, m = map(int, input().split(" "))
arr = [list(map(int, list(input()))) for _ in range(n)]

for size in range(min(n, m), 0, -1): #가장 큰 사각형부터 거꾸로 찾음
    for i in range(n):
        for j in range(m):
            num = arr[i][j] #현재 숫자(왼상단)
            ni = i+(size-1)
            nj = j+(size-1)
            if 0 <= ni < n and 0 <= nj < m and num == arr[ni][j] == arr[i][nj] == arr[ni][nj]:
                print(size**2)
                exit(0)