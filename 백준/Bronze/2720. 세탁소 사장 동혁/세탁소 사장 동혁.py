t = int(input())
coin = [25, 10, 5, 1]

for _ in range(t):
    money = int(input())
    answer = [0, 0, 0, 0]

    for i in range(4):
        answer[i] = money // coin[i]
        money %= coin[i]

    print(*answer)