def solution(n, wires):
    answer = 99999 #송전탑 개수차이
    
    def dfs(graph, visited, start, n):
        visited[start] = 1 #방문처리
        for i in graph[start]:
            if not visited[i]:
                n = dfs(graph, visited, i, n+1)
        return n
    
    for i in range(n-1):
        new_wires = wires[:i]+wires[i+1:] #연결 끊어보기
        
        graph = [[] for _ in range(n)]
        visited = [0] * n
        
        for w in new_wires: #인접리스트 생성
            graph[w[0]-1].append(w[1]-1)
            graph[w[1]-1].append(w[0]-1)
            
        tower = dfs(graph, visited, 0, 1) #한 그룹에 연결된 송전탑 수
        answer = min(answer, abs(n-2*tower))
    return answer