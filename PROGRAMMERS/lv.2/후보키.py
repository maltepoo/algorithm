from itertools import combinations
def solution(relation):
    answer = []
    keys = []
    for i in range(1, len(relation[0])+1):
        keys += (list(combinations(range(len(relation[0])), i)))
        
    unique = []
    for k in keys: # 여러개 키 순회
        temp = []
        for r in relation: # 릴레이션 순회하며 후보키 검증
            temp2 = []
            for j in k: # 키가 여러개일 때 여러 값 탐색
                temp2.append(r[j])
            temp.append(tuple(temp2))
        if len(temp) == len(set(temp)): # 중복 제거한 값과 다르면 중복값이 있다는 뜻 = 유일성X
            put = True
            for u in unique:
                if set(u).issubset(set(k)): # 이미 들어간 unique 값이 원소로 들어가있으면 최소성X
                    put = False
                    break
            if put: unique.append(k)
    return len(unique)