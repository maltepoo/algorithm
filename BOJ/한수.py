def ishan(n):
    if 100 > n:
        return True
    else:
        n = list(map(int, str(n)))
        if n[0] - n[1] == n[1] - n[2]:
            return True
    return False
n = int(input())
cnt = 0
for i in range(1, n+1):
    if ishan(i):
        cnt += 1
print(cnt)