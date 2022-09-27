def solution(arr):
    answer = [0, 0]  # 0, 1
    m = len(arr)

    def divide(i, j, n):  # arr를 4등분으로 나누는 함수
        start = arr[i][j]
        if n == 1:
            answer[start] += 1
            return
        for x in range(i, i + n):
            for y in range(j, j + n):
                if arr[x][y] != start:
                    idx = n // 2
                    divide(i, j, idx)  # 1
                    divide(i, j + idx, idx)  # 2
                    divide(i + idx, j, idx)  # 3
                    divide(i + idx, j + idx, idx)  # 4
                    return # 종료해주어야 더이상 x,y를 탐색하지 않음
        answer[start] += 1
        return
    divide(0, 0, m)
    return answer
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
print(solution([[[1],[0],[1],[0]]))