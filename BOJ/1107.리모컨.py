n, m = int(input()), int(input())
if m: broken = input().split()
else: broken = []
far = abs(100 - n) # 최대 이동 거리
for i in range(1000000):
    for j in str(i):
        if j in broken:
            break
    else:
        far = min(far, len(str(i)) + abs(i - n))
print(far)