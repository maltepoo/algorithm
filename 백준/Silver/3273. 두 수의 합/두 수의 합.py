n = int(input())
seq = list(map(int, input().split()))
x = int(input())

ans = 0

seq.sort()
i, j = 0, n-1
while i < j:
    if seq[i] + seq[j] == x:
        ans += 1
        i += 1
        j -= 1
    elif seq[i] + seq[j] < x:
        i += 1
    elif seq[i] + seq[j] > x:
        j -= 1

print(ans)