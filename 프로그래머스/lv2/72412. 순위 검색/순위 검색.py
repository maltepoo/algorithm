from itertools import combinations

def getCount(arr, key):
    st, ed = 0, len(arr)
    while st < ed:
        mid = (st + ed) // 2
        if arr[mid] >= key:
            ed = mid
        else:
            st = mid + 1
    return len(arr)-st


def solution(info, query):
    answer = []
    board = {}

    for i in info:
        infos = i.split(" ")
        scores = int(infos[4])
        for j in range(1, 5):
            for k in combinations(infos[:-1], j):
                info_string = "".join(k)
                if not info_string in board:
                    board[info_string] = [scores]
                else:
                    board[info_string].append(scores)
        if "scores" in board:
            board["scores"].append(scores)
        else:
            board["scores"] = [scores]
            
    for v in board.values():
        v.sort()
        
    for q in query:
        nq = q.replace(" and ", "").replace("-", "").split(" ")
        cmd, sc = nq

        if cmd == "":
            answer += [getCount(board["scores"], int(sc))]
        elif cmd in board:
            answer += [getCount(board[cmd], int(sc))]
        else: answer += [0]
    return answer