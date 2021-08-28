#1926. 간단한 369게임
N = int(input())
game = list(map(str,list(i for i in range(1, N+1))))
nums = ['3', '6', '9']
for i in range(N):
    cnt = 0
    if game[i] in nums:
        game[i] = '-'
    elif len(game[i]) >= 2:
        for j in range(len(game[i])):
            if game[i][j] in nums:
                cnt += 1
        if cnt:
            game[i] = cnt*'-'
print(*game)