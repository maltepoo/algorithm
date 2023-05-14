def solution(n, costs):
    answer = 0
    parent = [i for i in range(n+1)]
    
    costs.sort(key=lambda x: x[2])
    
    def union(x, y):
        x = parent[x]
        y = parent[y]

        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    def find(x):
        if not parent[x] == x:
            parent[x] = find(parent[x])
        return parent[x]
    
    for e in costs:
        a, b, c = e
        if find(a) != find(b):
            union(a, b)
            answer += c
            
    return answer