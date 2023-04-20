import sys
input = sys.stdin.readline

n, q = map(int, input().split())
B = sorted(map(int, input().split()))
prefixSum = [0]*(n+1)

for i in range(n):
    prefixSum[i+1] = prefixSum[i] + B[i]

for _ in range(q):
    L, R = map(int, input().split())
    print(prefixSum[R] - prefixSum[L-1])
