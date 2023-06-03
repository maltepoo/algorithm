def dist(n):
    # A -> n or Z -> n
    return min(ord(n)-65, 91-ord(n))

def solution(name):
    answer = 0
    
    cursor = len(name)-1
    for i, n in enumerate(name):
        answer += dist(n) # ▲▼ 알파벳 변경 최소값
        
        # ◀/▶
        next = i+1 # 현재 이후부터 연속 A 찾기
        while next < len(name) and name[next] == 'A':
            next += 1
        # 평범이동, 연속A왼쪽부터가는것, 연속A오른쪽부터가는것의 최소값
        cursor = min(cursor, 2*i+len(name)-next, i+2*(len(name)-next))
    answer += cursor
    return answer