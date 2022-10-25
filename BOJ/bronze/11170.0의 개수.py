t = int(input())
for i in range(t):
    res = 0
    n, m = map(int, input().split(" "))
    for j in range(n, m+1):
        res += str(j).count("0")
    print(res)