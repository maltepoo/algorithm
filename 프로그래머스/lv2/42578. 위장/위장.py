def solution(clothes):
    answer = 1
    clotheList = {}
    for c, v in clothes:
        if v in clotheList:
            clotheList[v] += 1
        else: clotheList[v] = 1
    for i in clotheList.values():
        answer *= (i+1)
    return answer - 1