dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(maps, x, y):
    visited = [[0]*(len(maps[0])) for _ in range(len(maps))]
    land_sum = 0
    
    q = [(x, y)]
    while q:
        i, j = q.pop()
        land_sum += int(maps[i][j])
        maps[i][j] = 'X'
        
        for k in range(4):
            ni, nj = i+dirs[k][0], j+dirs[k][1]
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and maps[ni][nj] != 'X' and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return land_sum

def solution(maps):
    answer = []
    
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                answer.append(bfs(maps, i, j))
    
    if not answer:
        answer.append(-1)
    return sorted(answer)