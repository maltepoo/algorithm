def solution(wallpaper):
    answer = []
    row, col = len(wallpaper), len(wallpaper[0])
    
    files = []
    x, y, mx, my = 51, 51, 0, 0
    for i in range(row):
        for j in range(col):
            if wallpaper[i][j] == '#':
                files.append((i, j))
                x = min(x, i)
                y = min(y, j)
                mx = max(mx, i+1)
                my = max(my, j+1)
    # print(files)
    return [x, y, mx, my]