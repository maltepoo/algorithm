#1215. [S/W 문제해결 기본] 3일차 - 회문1
def is_palin(word):
    if word == word[::-1]:
        return 1
    else:
        return 0

for tc in range(1, 11):
    N = int(input())
    board = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            # 가로
            if is_palin(board[i][j:j+N]):
                cnt += 1
            # 세로
            temp = []
            for m in range(N):
                temp.append(board[j+m][i])
            if is_palin(temp):
                cnt += 1
    print('#{} {}'.format(tc, cnt))
