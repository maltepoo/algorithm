l, c = map(int, input().split())
alph = sorted(input().split())
m = ('a', 'e', 'i', 'o', 'u')

def dfs(d, s, i):
    if d == l:
        co, vo = 0, 0
        for ss in s:
            if ss in m:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(s)
    for j in range(i, c):
        dfs(d+1, s+alph[j], j+1)

dfs(0, "", 0)