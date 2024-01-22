def solution(n, results):
    answer = 0
    player = [[0]*n for _ in range(n)]
    
    for a, b in results:
        player[b-1][a-1] = -1
        player[a-1][b-1] = 1
        
    # 플로이드워셜로 승패기록
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # j > i, i > k면 j > k가 됨
                if player[j][i] == player[i][k] == 1:
                    player[j][k] = 1
                    player[k][j] = -1
    
    # 연결된 선수들은 승패를 가릴 수 있음
    for p in player:
        if p.count(0) == 1:
            answer += 1
            
    return answer