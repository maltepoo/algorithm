#1211. Ladder2
for _ in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    starts = []
    for i in range(100):
        if arr[0][i] == 1:
            starts.append(i)

    minS = starts[0]
    minCnt = 9999
    for start in starts:
        y, x = 0, start
        cnt = 0

        while y < 99:
            y += 1
            cnt += 1
            if x>0 and arr[y][x-1] == 1:
                while x>0 and arr[y][x-1] == 1:
                    x -= 1
                    cnt += 1
            elif x<99 and arr[y][x+1] == 1:
                while x<99 and arr[y][x+1] == 1:
                    x += 1
                    cnt += 1

        if cnt < minCnt:
            minCnt = cnt
            minS = start

    print('#{} {}'.format(N, minS))
