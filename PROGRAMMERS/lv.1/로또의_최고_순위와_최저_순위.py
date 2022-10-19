def solution(lottos, win_nums):
    cnt = []  # 일치하는 숫자
    zero = []  # 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt.append(lotto)
        elif lotto == 0:
            zero.append(lotto)
        else:
            pass
        if len(cnt) == 6:
            rank = 1
        elif len(cnt) == 5:
            rank = 2
        elif len(cnt) == 4:
            rank = 3
        elif len(cnt) == 3:
            rank = 4
        elif len(cnt) == 2:
            rank = 5
        elif len(cnt) < 2:
            rank = 6
    if len(cnt) == 0 and len(zero) == 0:
        return 6, 6

    return 7 - len(cnt + zero), rank