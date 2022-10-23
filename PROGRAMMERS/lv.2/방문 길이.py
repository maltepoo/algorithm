def solution(dirs):
    answer = 0
    roads = set()
    y, x, ny, nx = 0, 0, 0, 0
    for d in dirs:
        if d == 'U':
            ny -= 1
        elif d == 'D':
            ny += 1
        elif d == 'R':
            nx += 1
        elif d == 'L':
            nx -= 1
        if abs(ny) > 5 or abs(nx) > 5:
            ny, nx = y, x
            continue
        if (y, x, ny, nx) not in roads:
            roads.add((y, x, ny, nx))
            roads.add((ny, nx, y, x))
            answer += 1
        y, x = ny, nx
    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))