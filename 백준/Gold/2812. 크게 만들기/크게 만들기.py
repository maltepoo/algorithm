import sys
input = sys.stdin.readline
N, K = map(int, input().split())
num = list(input())
s, k = [], K
for i in range(N):
    while k>0 and s and s[-1] < num[i]:
        s.pop()
        k -= 1
    s.append(num[i])
print(''.join(s[:N-K]))