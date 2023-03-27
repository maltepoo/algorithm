from itertools import combinations
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 10001

#1.순열풀이
nums = [i for i in range(n)]
start = list(combinations(nums, n//2)) #start팀 경우의 수
for team_s in start:
    team_l = tuple(set(nums) - set(team_s))

    #각 팀별 전력 구하기
    s_power, l_power = 0, 0
    for i in range(n//2):
        for j in range(n//2):
            s_power += arr[team_s[i]][team_s[j]]
            l_power += arr[team_l[i]][team_l[j]]
    res = min(abs(s_power-l_power), res)
print(res)