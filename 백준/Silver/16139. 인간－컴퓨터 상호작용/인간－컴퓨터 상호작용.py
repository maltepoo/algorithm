S = input()
q = int(input()) # 질문의 수

dp = [[0]*26 for _ in range(len(S))]
dp[0][ord(S[0])-97] = 1

for i in range(1, len(S)):
    dp[i] = dp[i-1].copy()
    dp[i][ord(S[i])-97] = dp[i-1][ord(S[i])-97] + 1

for _ in range(q):
    n, st, ed = input().split()
    n, st, ed = ord(n)-97, int(st), int(ed)
    if st == 0:
        print(dp[ed][n])
    else:
        print(dp[ed][n] - dp[st-1][n])