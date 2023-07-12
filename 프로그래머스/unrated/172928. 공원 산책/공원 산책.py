def solution(park, routes):
    dirs = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    R, C = len(park), len(park[0])
    i, j = 0, 0
    for r in range(R):
        for c in range(C):
            if park[r][c] == 'S':
                i, j = r, c
    for rt in routes:
        d, n = rt.split(" ")
        tempi, tempj = i, j
        for k in range(int(n)): # n번이동
            ni, nj = tempi+dirs[d][0], tempj+dirs[d][1]
            if 0<=ni<R and 0<=nj<C and park[ni][nj] != 'X':
                tempi, tempj = ni, nj
            else:
                break
        else:
            i, j = tempi, tempj
    return [i, j]