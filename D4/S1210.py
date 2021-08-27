#1210. Ladder1
for _ in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    #거꾸로 올라오며 찾기
    y = 99
    x = arr[99].index(2)

    while y > 0:
        y -= 1
        if x>0 and arr[y][x-1] == 1:
            while x>0 and arr[y][x-1] == 1:
                x -= 1
        elif x<99 and arr[y][x+1] == 1:
            while x<99 and arr[y][x+1] == 1:
                x += 1

    print('#{} {}'.format(N, x))