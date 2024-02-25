# from collections import defaultdict

def solution(arrows):
    answer = 0
    
    dirs = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}
    
    i, j = 0, 0
    q = []
    # visited = defaultdict(list)
    visited = {(0, 0) : []}
    for a in arrows:
        for _ in range(2):
            ni, nj = i+dirs[a][0], j+dirs[a][1]
            if (ni, nj) in visited and not (i, j) in visited[(ni, nj)]:
                answer += 1
                visited[(i, j)].append((ni, nj))
                visited[(ni, nj)].append((i, j))
            elif (ni, nj) not in visited: #방문한적x
                visited[(ni, nj)] = []
                visited[(i, j)].append((ni, nj))
                visited[(ni, nj)].append((i, j))
            i, j = ni, nj
                
    return answer