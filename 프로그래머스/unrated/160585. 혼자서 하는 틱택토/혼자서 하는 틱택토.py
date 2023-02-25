def isWinner(li):
    wins = [
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)]
    ]
    # li안에 win가 다 들어있는지 확인
    for win in wins:
        comp = set(win).union(set(li))
        if len(comp) == len(li):
            return True
    return False

def solution(board):
    answer = 1
    o, x = [], []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o.append((i, j))
            if board[i][j] == 'X':
                x.append((i, j))

    lenx, leno = len(x), len(o)
    if leno - lenx == 1:  # 차이가 정상인데
        if isWinner(x):  # x가 이겼을때
            answer = 0
    elif leno == lenx:  # 동점인데
        if isWinner(o):  # 선공이 이겼을경우 x가 한번더 놓은것
            answer = 0
    else:  # 개수차이가 1이상일때
        answer = 0
    return answer