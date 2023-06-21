S = input()
n = len(S)
string = {'': 0}
answer = 0

for i in range(n):
    for j in range(n-i+1):
        if not S[i:i+j] in string:
            string[S[i:i+j]] = 0
            answer += 1
print(answer)