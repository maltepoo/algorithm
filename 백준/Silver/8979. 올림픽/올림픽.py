n, k = map(int, input().split(" "))
nations = [list(map(int, input().split()))+[i] for i in range(1, n+1)]
nations.sort(key=lambda x: x[0], reverse=True)
print(list(map(lambda x: x[-1], nations))[k-1])