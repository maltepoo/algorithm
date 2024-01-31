dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
oil_info = {}
n = 2

def size_check(i, j, land, size, answer):
    global n
    
    q = [(i, j)]
    size[i][j] = n

    oil = 1
    while q:
        i, j = q.pop(0)

        for k in range(4):
            ni, nj = i+dirs[k][0], j+dirs[k][1]
            if 0 <= ni < len(land) and 0 <= nj < len(land[0]) and land[ni][nj] == 1 and size[ni][nj] == 0:
                oil += 1
                size[ni][nj] = n
                q.append((ni, nj))

    oil_info[n] = oil
    n += 1
    return

def solution(land):
    answer = 0
    size = [[0]*len(land[0]) for _ in range(len(land))]

    for i in range(len(land[0])):
        temp_oil = set()
        for j in range(len(land)):
            if land[j][i] == 1 and size[j][i] == 0:
                size_check(j, i, land, size, answer)

            if land[j][i] == 1:
                temp_oil.add((size[j][i], oil_info[size[j][i]]))

        answer = max(answer, sum(map(lambda x: x[1], temp_oil)))
    return answer