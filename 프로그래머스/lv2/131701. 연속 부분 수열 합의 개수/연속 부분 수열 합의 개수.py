def solution(elements):
    circled = elements + elements
    total = set()
    total.add(sum(elements))
    
    for i in range(1, len(elements)): # 연속 부분 수열의 길이
        for j in range(0, len(elements)):
            total.add(sum(circled[j:j+i]))
        
    return len(total)