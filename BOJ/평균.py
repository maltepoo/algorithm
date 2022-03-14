sub = int(input())
scores = list(map(int, input().split()))
m = max(scores)
for i in range(sub):
    scores[i] = scores[i]/m*100
print(sum(scores)/sub)