"""
숫자 개수별로 정리
가장 숫자 많은것부터 더해가기
"""
def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    tangerCount = dict()
    
    for t in tangerine:
        if t in tangerCount:
            tangerCount[t] += 1
        else:
            tangerCount[t] = 1
    sortedTangerine = sorted(tangerCount.items(), key = lambda x: x[1], reverse = True)
    
    tot = 0
    for idx in range(len(sortedTangerine)):
        종류, 개수 = sortedTangerine[idx]
        tot += 개수
        if tot >= k:
            return idx+1
    return answer