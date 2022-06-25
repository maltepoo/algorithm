n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
p = []
for i in range(n-8+1):
    for j in range(m-8+1):
        def check(x, y):
            w = 0
            b = 0
            for i in range(x, x + 8):
                for j in range(y, y + 8):
                    # 행/열 합이 짝수, 홀수이면 각 일정한 색을 가짐
                    if (j + i) % 2 == 0:
                        if arr[i][j] == 'W':
                            b += 1
                        else:
                            w += 1
                    else:
                        if arr[i][j] == 'B':
                            b += 1
                        else:
                            w += 1
            p.append(w)
            p.append(b)
            return
        check(i, j)
print(min(p))