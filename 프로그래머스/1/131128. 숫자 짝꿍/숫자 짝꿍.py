def solution(X, Y):
    answer = []
    for i in range(9, -1, -1):
        x_cnt = X.count(str(i))
        y_cnt = Y.count(str(i))

        if min(x_cnt, y_cnt) > 0:
            for _ in range(min(x_cnt, y_cnt)):
                answer.append(i)
    
    if len(answer) > 0 and sum(answer) < 1:
        answer = [0]
        
    return "-1" if len(answer) < 1 else "".join(map(str, answer))