import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
base = list(map(int, input().rstrip().split()))

arr = [0]*n
arr[0] = base[0]

res = sum(base[:k])
for i in range(1, n):
    arr[i] = base[i] + arr[i-1]
    if i > k-1:
        res = max(res, arr[i] - arr[i-k])

print(res)