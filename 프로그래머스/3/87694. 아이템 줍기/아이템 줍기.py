from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr = [[-1] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]

    # 1. 다각형 테두리 색칠(1)
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2: # 다른 사각형 내부 판별 위함
                    arr[i][j] = 0
                elif arr[i][j] != 0:
                    arr[i][j] = 1

    # 2. 좌/우 테두리를 따라서 이동 > 먼저 아이템 도착이 짧은거리임
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    q = deque()
    q.append((characterX*2, characterY*2))
    visited[characterX*2][characterY*2] = 1

    while q:
        cx, cy = q.popleft()

        if itemX*2 == cx and itemY*2 == cy:
            answer = visited[cx][cy] // 2
            break

        for k in range(4):
            n_characterX = cx + dirs[k][0]
            n_characterY = cy + dirs[k][1]

            if arr[n_characterX][n_characterY] == 1 and visited[n_characterX][n_characterY] == 0:
                q.append((n_characterX, n_characterY))
                visited[n_characterX][n_characterY] = visited[cx][cy] + 1

    return answer