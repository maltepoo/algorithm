"""
Latest Recently Used 가장 사용한지 오래된 것을 내보내는 알고리즘
"""
def solution(cacheSize, cities):
    time = 0
    memory = [] # tail <=> head
    if cacheSize == 0:
        return len(cities)*5
    for c in cities:
        c = c.upper()
        if c in memory:
            memory.remove(c)
            memory.append(c)
            time += 1
        else:
            time += 5
            if len(memory) < cacheSize:
                memory.append(c)
            else:
                memory.pop(0)
                memory.append(c)
    return time
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))