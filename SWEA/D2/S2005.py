#2005. 파스칼의 삼각형
def pascal():
    P = [[0] * i for i in range(1, 11)]
    for i in range(11):
        if i < len(P):
            P[i][0], P[i][i] = 1, 1
            for j in range(i):
                if P[i][j] == 0:
                    P[i][j] = P[i-1][j-1] + P[i-1][j]
    return P

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    for i in range(N):
        print(*pascal()[i])