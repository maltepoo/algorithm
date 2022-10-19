def solution(n):
    answer = []
    arr = [list(0 for _ in range(a+1)) for a in range(n)]
    cnt = 1
    dirs = [(1, 0), (0, 1), (-1, -1)]  # 하 우 상좌

    r, c = 0, 0
    d = 0
    while cnt <= ((n * (n + 1)) // 2):
        if 0 <= r < n and 0 <= c < n and arr[r][c] == 0:  # 유효범위체크
            arr[r][c] = cnt
            cnt += 1
        else:  # 채워진경우 한칸 뒤로 간 후 채우기 / 방향전환
            r, c = r - dirs[d][0], c - dirs[d][1]
            d = (d + 1) % 3
        r, c = r + dirs[d][0], c + dirs[d][1]
    # for res in arr:
    #     answer += res
    return sum(arr, [])

print(solution(4))
print(solution(5))
print(solution(6))