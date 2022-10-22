def solution(land):
    h = len(land)

    for i in range(1, h):
        for j in range(4):
            temp = []
            for k in range(4):
                if j != k:
                    temp.append(land[i - 1][k])
            land[i][j] += max(temp)
    return max(land[h-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))