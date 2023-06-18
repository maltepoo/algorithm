# 이분탐색으로 돌의 0이 k개 연속이 되는 라운드를 찾음(라운드=건넌 사람의 수)
def solution(stones, k):
    s, e = 1, max(stones)
    while s <= e:
        c = 0
        mid = (s+e) // 2
        for stone in stones:
            if stone - mid <= 0:
                c += 1
            else:
                c = 0 # 0이 연속적으로 나오지 않으면 초기화
            if c >= k:
                e = mid - 1
                break
        else:
            s = mid + 1
    return s