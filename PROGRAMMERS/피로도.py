from itertools import permutations

def solution(k, dungeons):
    answer = -1
    many = len(dungeons)
    arr = list(permutations([i for i in range(many)], many))

    def adventure(k, order):
        res = 0
        for o in order:
            needK, useK = dungeons[o][0], dungeons[o][1]
            if k < needK:  # 필요피로도 확인
                return res
            else:  # 탐험
                k -= useK
                res += 1
        return res

    for order in arr:  # 개별순서
        res = adventure(k, order)
        if res > answer:
            answer = res
    return answer