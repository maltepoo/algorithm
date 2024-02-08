import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = {}
for _ in range(n):
    w = input().rstrip()
    if len(w) >= m:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

for wd in sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(wd[0])