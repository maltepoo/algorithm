n, m = map(int, input().split())

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
arr = []

def bfs(start):
    answer = 0
    q = [start]

    while q:
        i, j = q.pop()

        for k in range(4):
            ni, nj = i + dirs[k][0], j + dirs[k][1]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != 'X':
                if arr[ni][nj] == 'P':
                    answer += 1

                arr[ni][nj] = 'X'
                q.append((ni, nj))
    return answer


start = ()
for ti in range(n):
    tmp_arr = list(input())
    for tj in range(m):
        if tmp_arr[tj] == 'I':
            start = (ti, tj)
    arr.append(tmp_arr)

res = bfs(start)

print(res if res > 0 else "TT")