t = int(input())
for _ in range(t):
    closet = {}
    n = int(input())
    for _ in range(n):
        name, category = input().split()
        if category in closet:
            closet[category] += 1
        else: closet[category] = 1
    res = 1
    for cnt in closet.values():
        res *= (cnt+1) # 안입는 경우를 더해줌
    print(res-1) # 알몸일 경우의 수 -1