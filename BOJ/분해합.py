n = int(input())
for i in range(1, n+1):
    temp = i
    for j in str(i):
        temp += int(j)
    if temp == n:
        print(i)
        exit(0)
print(0)