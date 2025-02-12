from collections import deque

n = int(input())
scv = list(map(int, input().split()))
scv.extend([0, 0])

dp = {}  # (a, b, c) 상태에서 최소 공격 횟수를 저장
attacks = [(-9, -3, -1), (-9, -1, -3), (-3, -9, -1),
           (-3, -1, -9), (-1, -3, -9), (-1, -9, -3)]

def bfs(a, b, c):
    queue = deque([(a, b, c)])
    dp[(a, b, c)] = 0

    while queue:
        x, y, z = queue.popleft()

        if x == 0 and y == 0 and z == 0:
            return dp[(0, 0, 0)]

        for dx, dy, dz in attacks:
            nx, ny, nz = max(x + dx, 0), max(y + dy, 0), max(z + dz, 0)

            if (nx, ny, nz) not in dp:
                dp[(nx, ny, nz)] = dp[(x, y, z)] + 1  # 최소 공격 횟수 저장
                queue.append((nx, ny, nz))

    return -1

print(bfs(scv[0], scv[1], scv[2]))